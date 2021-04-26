import os
from flask import Flask
from flask_migrate import Migrate
from app.database import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = b"d[12;/[d/2rqpl20rk02KPWDMK923#5U_))%FqwKO^A"
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CSRF_ENABLED'] = True

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    return app
