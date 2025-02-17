import json
import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

def load_goals_from_json():
    if os.path.exists('goals.json'):
        with open('goals.json', 'r') as f:
            return json.load(f)
    else:
        return []

saved_goals = load_goals_from_json() # Laddar in sparade mål när appen startar

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

        # Spara till JSON-filen efter varje nytt mål
        with open('goals.json', 'w') as f:
            json.dump(saved_goals, f, indent=4) # indent gör filen mer läsbar

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)