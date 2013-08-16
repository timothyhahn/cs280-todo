from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from settings import debug


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)


if debug:
    from flask.ext.admin import Admin
    from flask.ext.admin.contrib.sqlamodel import ModelView
    from models import User, Task, Category
    from database import db_session
    admin = Admin(app)
    admin.add_view(ModelView(Task, db_session))
    admin.add_view(ModelView(User, db_session))
    admin.add_view(ModelView(Category, db_session))


import todo.views
