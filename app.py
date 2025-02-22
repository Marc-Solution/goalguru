from flask import Flask, render_template, request, redirect, url_for, session
from classes.add_goal_class import AddGoal
from classes.view_goals_class import ViewGoals
import json

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Hemlig nyckel för session, kan ändras till valfri sträng

add_goal_instance = AddGoal()
view_goals_instance = ViewGoals()

@app.route('/')
def start():
    exited = session.pop('exited', False)  # Hämta exited från session, default False
    print(f"Start körs, exited={exited}")  # Debug: Visar värdet på exited
    return render_template('start.html', exited=exited)

# Menyn fungerar som en loop genom navigering:
# /menu -> /add_goal eller /view_goals -> tillbaka till /menu.
# "Exit" bryter loopen genom att gå till /start med ett avslutsmeddelande.
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        choice = request.form.get('choice')
        print(f"Val: {choice}")  # Debug: Skriver ut användarens val
        if choice == 'add_goal':
            return redirect(url_for('add_goal'))
        elif choice == 'view_goals':
            return redirect(url_for('view_goals'))
        elif choice == 'exit':
            session['exited'] = True  # Sätt exited i session
            print("Session['exited'] satt till True")  # Debug: Bekräftar att exit triggas
            return redirect(url_for('start'))
    return render_template('menu.html')

@app.route('/add_goal', methods=['GET', 'POST'])
def add_goal():
    if request.method == 'POST':
        add_goal_instance.set_goal_name(request.form.get('goal_name'))
        add_goal_instance.set_important_goal(request.form.get('important_goal'))
        add_goal_instance.set_meaning_of_goal(request.form.get('meaning_of_goal'))
        add_goal_instance.set_deadline(request.form.get('deadline'))
        add_goal_instance.set_life_changes(request.form.get('life_changes'))
        add_goal_instance.set_impact_on_others(request.form.get('impact_on_others'))
        add_goal_instance.set_achievements_for_others(request.form.get('achievements_for_others'))
        add_goal_instance.set_feelings_if_fail(request.form.get('feelings_if_fail'))
        add_goal_instance.set_life_if_success(request.form.get('life_if_success'))
        add_goal_instance.set_life_details(request.form.get('life_details'))
        add_goal_instance.set_plan(request.form.get('plan'))
        add_goal_instance.set_obstacles(request.form.get('obstacles'))
        add_goal_instance.set_next_milestone(request.form.get('next_milestone'))
        add_goal_instance.set_today_step(request.form.get('today_step'))

        goals = []
        try:
            with open('goals.json', 'r') as f:
                goals = json.load(f)
        except FileNotFoundError:
            pass

        goals.append({
            "goal_name": add_goal_instance.get_goal_name(),
            "important_goal": add_goal_instance.get_important_goal(),
            "meaning_of_goal": add_goal_instance.get_meaning_of_goal(),
            "deadline": add_goal_instance.get_deadline(),
            "life_changes": add_goal_instance.get_life_changes(),
            "impact_on_others": add_goal_instance.get_impact_on_others(),
            "achievements_for_others": add_goal_instance.get_achievements_for_others(),
            "feelings_if_fail": add_goal_instance.get_feelings_if_fail(),
            "life_if_success": add_goal_instance.get_life_if_success(),
            "life_details": add_goal_instance.get_life_details(),
            "plan": add_goal_instance.get_plan(),
            "obstacles": add_goal_instance.get_obstacles(),
            "next_milestone": add_goal_instance.get_next_milestone(),
            "today_step": add_goal_instance.get_today_step()
        })

        try:
            with open('goals.json', 'w') as f:
                json.dump(goals, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving goals to JSON: {e}")
            return "Ett fel uppstod vid sparandet av målet."
        return redirect(url_for('menu'))
    return render_template('add_goal.html')

@app.route('/goal_details/<goal_name>')
def goal_details(goal_name):
    try:
        with open('goals.json', 'r') as f:
            goals = json.load(f)
    except FileNotFoundError:
        goals = []
    for goal in goals:
        if goal['goal_name'] == goal_name:
            return render_template('goal_details.html', goal=goal)
    return "Mål inte hittat"

@app.route('/view_goals')
def view_goals():
    try:
        with open('goals.json', 'r') as f:
            goals = json.load(f)
    except FileNotFoundError:
        goals = []
    return render_template('view_goals.html', goals=goals)

if __name__ == '__main__':
    app.run(debug=True)