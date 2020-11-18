from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)

    def __init__(self, task_name):
        self.name = task_name
        self.done = False
        self.description = ""

db.create_all()

# главная страница со списком задач
@app.route('/', methods=['GET'])
def main_page():
    tasks_list = Task.query.all()
    return render_template('index.html', tasks_list=tasks_list)

# запрос на добавление задачи
@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['input_task_name']
    task = Task(task_name)

    db.session.add(task)
    db.session.commit()
    return redirect('/')

# запрос на удаление задачи
@app.route('/del/<int:task_idx>')
def delete_task(task_idx):
    task = Task.query.get(task_idx)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')

# запрос на изменение статуса задачи
@app.route('/change_status/<int:task_idx>', methods=['POST'])
def change_task_status(task_idx):
    task = Task.query.get(task_idx)

    if not task:
        return redirect('/')

    task.done = not task.done

    db.session.commit()
    return redirect('/')

# запрос на изменение информации о задаче
@app.route('/edit/<int:task_idx>')
def edit_task(task_idx):
    task = Task.query.get(task_idx)

    if not task:
        return redirect('/')

    return render_template('edit_task.html', task=task)

# запрос на запись изменений
@app.route('/edit/apply_changes/<int:task_idx>', methods=['POST'])
def apply_changes(task_idx):
    task = Task.query.get(task_idx)

    if not task:
        return redirect('/')

    task.name = request.form['change_task_name']
    task.description = request.form['change_description']

    db.session.commit()

    return redirect('/')