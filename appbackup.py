from flask import Flask, render_template, request, redirect, url_for
from classes.add_goal_class import AddGoal
from classes.view_goals_class import ViewGoals
import json

app = Flask(__name__)

add_goal_instance = AddGoal()
view_goals_instance = ViewGoals()

@app.route('/', methods=['GET', 'POST'])
def index():
    while True:  # Loop för menyn
        if request.method == 'POST':
            choice = request.form.get('choice')
            if choice == 'add_goal':
                return redirect(url_for('add_goal'))
            elif choice == 'view_goals':
                return redirect(url_for('view_goals'))
            elif choice == 'exit':  # Lägg till ett val för att avsluta
                return "Programmet avslutas"  # Eller en annan lämplig respons
        return render_template('index.html')

@app.route('/add_goal', methods=['GET', 'POST'])
def add_goal():
    if request.method == 'POST':
        add_goal_instance.set_goal(request.form.get('goal'))
        add_goal_instance.set_deadline(request.form.get('deadline'))
        add_goal_instance.set_daily_task(request.form.get('daily_task'))

        # Spara målet i JSON-filen
        goals = view_goals_instance.get_goals()
        goals.append({
            'goal': add_goal_instance.get_goal(),
            'deadline': add_goal_instance.get_deadline(),
            'daily_task': add_goal_instance.get_daily_task()
        })
        try:
            with open('goals.json', 'w') as f:
                json.dump(goals, f, indent=4)
        except Exception as e:
            print(f"Error saving goals to JSON: {e}")
            return "Ett fel uppstod vid sparandet av målet."

        return redirect(url_for('index'))  # Redirect till index efter att mål har lagts till

    return render_template('add_goal.html') # Visa formuläret om det är GET request

@app.route('/view_goals')
def view_goals():
    goals = view_goals_instance.get_goals()
    return render_template('view_goals.html', goals=goals)

if __name__ == '__main__':
    app.run(debug=True)