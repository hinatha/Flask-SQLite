from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    status = db.Column(db.String(30))

    def __init__(self, task, detail, status):
        self.task = task
        self.detail = detail
        self.status = status


class TodoSchema(ma.Schema):
   class Meta:
       fields = ("id", "task", "detail", "status")

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@app.route("/", methods=["GET"])
def health():
    return "I'm alive!"

@app.route("/tasks", methods=["POST"])
def create_task():
    print("### execute create_task method")
    task = request.json["task"]
    detail = request.json["detail"]
    status = request.json["status"]

    new_todo = Todo(task, detail, status)
    print("new_todo")

    db.session.add(new_todo)

    db.session.commit()

    return todo_schema.jsonify(new_todo)

@app.route("/tasks", methods=["GET"])
def get_all_task():
    print("### execute get_all_task method")
    all_todos = Todo.query.all()
    return todos_schema.jsonify(all_todos)

@app.route("/tasks/<taskId>", methods=["GET"])
def get_task(taskId):
    print("### execute get_task method")
    todo = Todo.query.get(taskId)
    return todo_schema.jsonify(todo)

@app.route("/tasks/<taskId>", methods=["DELETE"])
def delete_task(taskId):
    print("###e execute delete_task method")
    todo = Todo.query.get(taskId)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)

@app.route("/tasks/<taskId>", methods=["PUT"])
def update_task(taskId):
    print("### execute put_task method")
    todo = Todo.query.get(taskId)

    task = request.json["task"]
    detail = request.json["detail"]
    status = request.json["status"]

    todo.task = task
    todo.detail = detail
    todo.status = status

    db.session.commit()
    return todo_schema.jsonify(todo)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)