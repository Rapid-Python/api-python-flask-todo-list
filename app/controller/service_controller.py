from flask import Blueprint, Flask, Response, request, jsonify
from extensions import app
import json
from app.models.query_builder import mongo
from app.models.query_builder import ObjectId
from app.models.query_builder import add_todo_db, test, all_task, update, delete

api = Blueprint('user', 'user')


@app.route("/add_todo", methods=["POST"])
def add_todo():
    print(request.form.get('add-todo'))
    add_todo_db(request.form.get('name'))
    add_todo_db(request.form.get('id'))
    return "task successfully added"


@app.route('/get_all_task', methods=['GET'])
def get_all_task():
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = all_task()
    # response_data['items'] = test(get_all_task)
    response_data['status'] = 200
    response_data['message'] = 'ok'
    return jsonify(response_data)


@app.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = test(task_id)
    response_data['status'] = 200
    response_data['message'] = 'ok'
    return jsonify(response_data)


@app.route("/update_task/<task_id>", methods=["PUT"])
def update_task(task_id):
    update(task_id, request.form["name"])
    print(request.form["name"])
    # todo_item['complete'] = True
    return "task by id is successfully updated"


@app.route("/delete_task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    # todos_collection = mongo.db.todos
    # todo_item = todos_collection.delete_one({'_id': ObjectId(id)})
    delete(task_id)
    # todo_item['complete'] = True
    return "task by id is successfully deleted"



'''
@app.route('/users/page/<int:page>')
def all_users(page=1):
    try:
        users_list = User.query.order_by(
            User.id.desc()
        ).paginate(page, per_page=USERS_PER_PAGE)
    except OperationalError:
        flash("No users in the database.")
        users_list = None
        return render_template(0
        'users.html',
        users_list=users_list,
        form=form
    )
'''