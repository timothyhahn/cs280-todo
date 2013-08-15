from todo import app
from flask import url_for, redirect, request, jsonify
from database import db_session
from models import Task, User
from datetime import datetime


# API
## GET


@app.route('/task', methods=['GET'])
def get_all_tasks():
    ## TODO: Integrate users
    tasks = Task.query.all()
    tasks_dict = dict()
    tasks_list = list()
    for task in tasks:
        tasks_list.append(task.info())
    tasks_dict['tasks'] = tasks_list
    return jsonify(tasks_dict)


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    ## TODO: Integrate users
    task = Task.query.get(task_id)
    return jsonify(task.info())


@app.route('/task', methods=['POST'])
def add_new_task():
    ## TODO: Integrate users
    user_id = 1
    description = 'description'
    notes = 'notes'
    longitude = '1.00'
    latitude = '1.00'
    attachment = ''
    due_date = None

    task = Task(user_id=user_id, description=description, notes=notes, due_date=due_date, longitude=longitude, latitude=latitude, attachment=attachment)
    db_session.add(task)
    db_session.commit(task)
    return jsonify(task.info())


@app.route('/task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    ## Modify Tasks
    db_session.commit()
    return jsonify(task.info())


@app.route('/task/delete/<int:task_id>', methods=['POST', 'DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db_session.delete(task)
    db_session.commit()
    return 'Successfully deleted'


@app.route('/login', methods=['POST'])
def login():
    return 'login'


# TURN OFF DB
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
