from flask import render_template, redirect, flash, request
from app.commands import app
from app.form import ToDoForm
from app.model import Task


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    shows all tasks and lets you make new ones
    """
    form = ToDoForm()
    tasks_5 = Task.query.filter_by(priority=5).all()
    tasks_4 = Task.query.filter_by(priority=4).all()
    tasks_3 = Task.query.filter_by(priority=3).all()
    tasks_2 = Task.query.filter_by(priority=2).all()
    tasks_1 = Task.query.filter_by(priority=1).all()
    print(tasks_1, tasks_2, tasks_3, tasks_4, tasks_5)
    if request.method == 'POST':
        title = form.title.data
        description = form.description.data
        priority = form.priority.data

        if title and priority:
            Task.add(title, description, priority)

            flash(f'Task "{title}" successfully added!', 'alert-green')

        else:
            print('no validation')
            flash(f'Please input a title and choose a priority', 'alert-red')

        return redirect('/')

    else:
        return render_template('home.html', form=form, t5=tasks_5, t4=tasks_4, t3=tasks_3, t2=tasks_2, t1=tasks_1)
