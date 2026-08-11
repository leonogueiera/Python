from functools import wraps
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db


auth_bp = Blueprint('auth', __name__)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Faça login para acessar o painel.', 'warning')
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')
        usuario = get_db().execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        if not usuario or not check_password_hash(usuario['senha'], senha):
            flash('E-mail ou senha inválidos.', 'danger')
            return render_template('login.html')
        session.clear()
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('tasks.dashboard'))
    return render_template('login.html')


@auth_bp.route('/registro', methods=('GET', 'POST'))
def registro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')
        confirmar = request.form.get('confirmar_senha', '')

        if not nome or not email or not senha:
            flash('Preencha todos os campos.', 'danger')
        elif senha != confirmar:
            flash('As senhas não coincidem.', 'danger')
        elif len(senha) < 6:
            flash('A senha deve possuir pelo menos 6 caracteres.', 'danger')
        else:
            try:
                db = get_db()
                db.execute(
                    'INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
                    (nome, email, generate_password_hash(senha))
                )
                db.commit()
                flash('Cadastro realizado! Agora faça login.', 'success')
                return redirect(url_for('auth.login'))
            except Exception:
                flash('Este e-mail já está cadastrado.', 'danger')
    return render_template('registro.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('auth.login'))
