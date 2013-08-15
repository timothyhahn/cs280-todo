from flask.ext.script import Manager, Server
import sys 

from todo import app

import todo.settings as settings
import os

PORT=8000
PORT=sys.argv[2]

app.debug = settings.debug
app.config['SECRET_KEY'] = settings.secret_key

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=PORT))


@manager.command
def init_db():
    "Sets up the DB"
    print "Setting up DB"
    from todo.database import init_db
    init_db()


@manager.command
def clear_db():
    "Clears the DB"
    print "Clearing DB"
    from todo.database import clear_db
    clear_db()

if __name__ == "__main__":
    manager.run()
