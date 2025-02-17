from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Lista för att spara mål (tillfälligt, vi kan spara i en fil senare)
saved_goals = []

@app.route('/')
def home():
    return render_template('index.html', goals=saved_goals)

@app.route('/add_goal', methods=['POST'])
def add_goal():
    goal = request.form['goal']
    deadline = request.form['deadline']
    daily_task = request.form['daily_task']

    if goal and deadline and daily_task:
        saved_goals.append({'goal': goal, 'deadline': deadline, 'daily_task': daily_task})

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
