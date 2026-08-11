# atividade_python_final

Projeto final de Python com Flask: painel de controle de tarefas, autenticação, CRUD, SQLite, API externa, filtro por status, modo escuro, dashboard com Chart.js e API REST.

## Requisitos
- Python 3.10+
- pip

## Instalação
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Opcionalmente, copie `.env.example` para `.env` e defina `SECRET_KEY`.

## Executar
```bash
python app.py
```
Abra `http://127.0.0.1:5000`.

## Funcionalidades implementadas
- Arquitetura modular Flask com `app.py`, templates e static.
- SQLite com tabelas `usuarios` e `tarefas`.
- Cadastro, login, logout, hash de senha e proteção por sessão.
- CRUD completo de tarefas.
- Dashboard com filtros de status.
- Cards com cores: pendente/amarelo, em andamento/azul, concluída/verde.
- Bootstrap 5 + Bootstrap Icons.
- SECRET_KEY por variável de ambiente e `DEBUG=False`.
- Validação de entradas e consultas SQL parametrizadas.
- Frase motivacional pela API pública Advice Slip.
- Modo escuro persistido em `localStorage`.
- Dashboard de progresso com Chart.js.
- Endpoint REST `GET /api/tarefas` retornando JSON.
- Página de progresso consumindo a rota REST via JavaScript sem recarregar a página.

## Rotas principais
- `/login`
- `/registro`
- `/logout`
- `/dashboard`
- `/nova_tarefa`
- `/editar/<id>`
- `/excluir/<id>`
- `/dashboard/progresso`
- `/api/frase`
- `/api/tarefas`

## Entrega Git
O projeto foi inicializado como repositório Git local com o nome `atividade_python_final`.
