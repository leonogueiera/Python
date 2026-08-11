import requests
from flask import Blueprint, jsonify, flash, redirect, render_template, request, session, url_for
from auth import login_required
from db import get_db


tasks_bp = Blueprint('tasks', __name__)
VALID_STATUS = {'pendente', 'em_andamento', 'concluida'}


def _tasks(status=None):
    query = 'SELECT * FROM tarefas WHERE usuario_id = ?'
    params = [session['usuario_id']]
    if status in VALID_STATUS:
        query += ' AND status = ?'
        params.append(status)
    query += ' ORDER BY id DESC'
    return get_db().execute(query, params).fetchall()


@tasks_bp.route('/')
def index():
    return redirect(url_for('tasks.dashboard') if 'usuario_id' in session else url_for('auth.login'))


@tasks_bp.route('/dashboard')
@login_required
def dashboard():
    status = request.args.get('status', 'todas')
    selected = status if status in VALID_STATUS else None
    tarefas = _tasks(selected)
    counts = {s: sum(1 for t in _tasks(s)) for s in VALID_STATUS}
    return render_template('dashboard.html', tarefas=tarefas, counts=counts, filtro=status)


@tasks_bp.route('/nova_tarefa', methods=('GET', 'POST'))
@login_required
def nova_tarefa():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', 'pendente')
        if not titulo:
            flash('O título é obrigatório.', 'danger')
        elif status not in VALID_STATUS:
            flash('Status inválido.', 'danger')
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)',
                (titulo, descricao, status, session['usuario_id'])
            )
            db.commit()
            flash('Tarefa criada com sucesso!', 'success')
            return redirect(url_for('tasks.dashboard'))
    return render_template('tarefa_form.html', tarefa=None)


@tasks_bp.route('/editar/<int:task_id>', methods=('GET', 'POST'))
@login_required
def editar(task_id):
    tarefa = get_db().execute(
        'SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?',
        (task_id, session['usuario_id'])
    ).fetchone()
    if tarefa is None:
        flash('Tarefa não encontrada.', 'danger')
        return redirect(url_for('tasks.dashboard'))

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', 'pendente')
        if not titulo or status not in VALID_STATUS:
            flash('Informe um título e um status válido.', 'danger')
        else:
            db = get_db()
            db.execute(
                'UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ? AND usuario_id = ?',
                (titulo, descricao, status, task_id, session['usuario_id'])
            )
            db.commit()
            flash('Tarefa atualizada!', 'success')
            return redirect(url_for('tasks.dashboard'))
    return render_template('tarefa_form.html', tarefa=tarefa)


@tasks_bp.post('/excluir/<int:task_id>')
@login_required
def excluir(task_id):
    db = get_db()
    db.execute('DELETE FROM tarefas WHERE id = ? AND usuario_id = ?', (task_id, session['usuario_id']))
    db.commit()
    flash('Tarefa removida.', 'info')
    return redirect(url_for('tasks.dashboard'))


@tasks_bp.post('/concluir/<int:task_id>')
@login_required
def concluir(task_id):
    db = get_db()
    db.execute(
        "UPDATE tarefas SET status = 'concluida' WHERE id = ? AND usuario_id = ?",
        (task_id, session['usuario_id'])
    )
    db.commit()
    flash('Tarefa marcada como concluída.', 'success')
    return redirect(url_for('tasks.dashboard'))


@tasks_bp.route('/api/frase')
@login_required
def frase_api():
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=5)
        response.raise_for_status()
        data = response.json()
        return jsonify({'advice': data.get('slip', {}).get('advice', 'Continue avançando!')})
    except requests.RequestException:
        return jsonify({'advice': 'Pequenos passos também levam a grandes resultados.'})


@tasks_bp.route('/dashboard/progresso')
@login_required
def progresso():
    return render_template('progresso.html')


@tasks_bp.route('/api/tarefas')
@login_required
def api_tarefas():
    status = request.args.get('status')
    tarefas = _tasks(status if status in VALID_STATUS else None)
    return jsonify([
        {'id': t['id'], 'titulo': t['titulo'], 'descricao': t['descricao'], 'status': t['status']}
        for t in tarefas
    ])
