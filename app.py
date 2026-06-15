from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')

    if task:
        tasks.append({
            'text': task,
            'completed': False
        })

    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect(url_for('index'))

@app.route('/toggle/<int:index>')
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)