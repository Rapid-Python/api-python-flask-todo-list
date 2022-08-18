from unicodedata import name
import pymongo
from bson.objectid import ObjectId

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.company
    mongo.server_info()
except:
    print("ERROR - Cannot connect to db")


def add_todo_db(name):
    todos_collection = db.todos
    todos_collection.insert_one({'name': name, 'complete': False})


def all_task():
    info = db.todos
    return list(info.find({},
        {
            "_id": {
                "$toString": "$_id"
            },
            "name": 1,
            "complete": 1,
        }
    ))


def test(task_id):
    info = db.todos
    return list(info.find({'_id': ObjectId(task_id)},
                          {
                              "_id": {
                                  "$toString": "$_id"
                              },
                              "name": 1,
                              "complete": 1,
                          }
                          ))


def update(task_id, name):
    todos_collection = db.todos
    todo_item = todos_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"name": name}}
    )


def delete(task_id):
    todos_collection = db.todos
    todo_item = todos_collection.delete_one(
        {
            "_id": ObjectId(task_id)
        }
    )