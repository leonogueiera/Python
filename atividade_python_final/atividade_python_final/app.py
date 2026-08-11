import os
from flask import Flask
from db import init_db
from auth import auth_bp
from tasks import tasks_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')
    app.config['DATABASE'] = os.path.join(app.root_path, 'instance', 'tarefas.db')

    os.makedirs(os.path.dirname(app.config['DATABASE']), exist_ok=True)
    init_db(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    @app.context_processor
    def inject_app_name():
        return {'app_name': 'Painel de Tarefas'}

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
