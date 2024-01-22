from flask import render_template, jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    print("fdskcidsicdosciodsjmoc")

    return render_template('index.html', tasks=Task.query.all())

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_list = [{'id': task.id, 'title': task.title, 'done': task.done} for task in tasks]
    return jsonify({'tasks': tasks_list})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    task_data = {'id': task.id, 'title': task.title, 'done': task.done}
    return jsonify({'task': task_data})

@app.route('/create_task', methods=['POST'])
def create_task():
    print(request.form["title"], request.input_stream)
    data = request.form["title"]
    new_task = Task(title=data, done=False)
    db.session.add(new_task)
    db.session.commit()
    print(Task.query.all())
    return render_template('index.html', tasks=Task.query.all())

@app.route('/update_task', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data['title']
    task.done = data['done']
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/mark_done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    return render_template('index.html', tasks=Task.query.all())

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return render_template('index.html', tasks=Task.query.all())

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(debug=True, port=8020, use_reloader=False)