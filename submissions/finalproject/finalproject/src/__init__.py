from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = "password.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../template/')
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .model import Password
    if not path.exists("../instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")

    from .views import main
    app.register_blueprint(main, url_prefix="/")

    return app