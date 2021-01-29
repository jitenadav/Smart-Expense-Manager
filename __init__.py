from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app()
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    dv.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .server import server as server_blueprint
    app.register_blueprint(server_blueprint)
