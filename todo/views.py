from todo import app
from flask import Flask, render_template, request, make_response, json, jsonify, url_for, redirect
from models import Todo


@app.route('/')
def index():
    return redirect(url_for('static', filename='todo.html'))

@app.route('/todos', methods=['GET', 'POST'])
def create_or_retrieve_todos():
    if request.method == 'POST':
        return create_todo()
    return retrieve_todos()

@app.route('/todos/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_todo(id):
    if request.method == 'PUT':
        return update_todo(id)
    return delete_todo(id)

def create_todo():
    data = json.loads(request.data)
    todo = Todo(content=data['content'], done=data['done'])
    todo.put()
    return jsonify(id=todo.key().id(),
                   content=todo.content,
                   done=todo.done
                  )

def retrieve_todos():
    content = json.dumps([todo.to_dict() for todo in Todo.all()])
    response = make_response(content)
    response.mimetype = 'application/json'
    return response

def update_todo(id):
    todo = Todo.get_by_id(id)
    data = json.loads(request.data)
    todo.content = data['content']
    todo.done = data['done']
    todo.save()
    return jsonify(id=id, content=todo.content, done=todo.done)

def delete_todo(id):
    Todo.get_by_id(id).delete()
    return jsonify()
