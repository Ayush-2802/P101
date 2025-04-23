from flask import Flask , jsonify , request , render_template

app = Flask(__name__)

tasks = [
    {'id': 1,'task':'Buy Groceries'},
    {'id': 2,'task':'Finish Homework'},
    {'id': 3,'task':'Call Mom'}
]

@app.route('/')
def home():
    return render_template('home.html',tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add():
    if request.is_json:
        data = request.get_json()
        task_text = data['task']
    else:
        task_text = request.form['task']
    new = {'id': len(tasks) + 1, 'task': task_text}
    tasks.append(new)
    if request.is_json:
        return jsonify(new), 201
    else:
        return render_template('home.html', tasks=tasks)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_tasks(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = data['task']
            return jsonify(task)
    return jsonify({'error': 'Task not Found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task Deleted!'})

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task_form(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return render_template('home.html', tasks=tasks)

@app.route('/tasks/<int:task_id>/update', methods=['POST'])
def update_task_form(task_id):
    new_text = request.form['task']
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = new_text
            break
    return render_template('home.html', tasks=tasks)

if __name__=="__main__":
    app.run(debug=True)