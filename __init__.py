from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from . import filters
from . import resources
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.jinja_env.filters['datetimeformat'] = filters.datetimeformat
    app.jinja_env.filters['file_type'] = filters.file_type
    app.config.from_pyfile('config.py')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .server import server as server_blueprint
    app.register_blueprint(server_blueprint)

    return app
