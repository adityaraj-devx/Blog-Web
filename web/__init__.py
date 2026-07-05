import os
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    from  .routes import routes
    from .auth import auth
    
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app