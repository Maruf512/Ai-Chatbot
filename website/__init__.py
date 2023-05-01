from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # create app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init(app)

    # import views and auth file
    from .views import views
    from .auth import auth
    
    # create blueprint of app for views and auth files
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # create database
    from .models import User, Conversion
    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            
            print("Database Created!")

