from flask import Flask, render_template, request, redirect, url_for
from classes.add_goal_class import AddGoal
from classes.view_goals_class import ViewGoals
import json

app = Flask(__name__)

add_goal_instance = AddGoal()
view_goals_instance = ViewGoals()

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'add_goal':
            return redirect(url_for('add_goal'))
        elif choice == 'view_goals':
            return redirect(url_for('view_goals'))
        elif choice == 'exit':
            return redirect(url_for('start'))
    return render_template('menu.html')

@app.route('/add_goal', methods=['GET', 'POST'])
def add_goal():
    if request.method == 'POST':
        # Hämta datan från formuläret och spara i AddGoal-instansen
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

        # Spara datan i JSON-filen
        goals = []  # Skapa en tom lista om filen inte finns
        try:
            with open('goals.json', 'r') as f:
                goals = json.load(f)
        except FileNotFoundError:
            pass  # Filen finns inte, fortsätt med tom lista

        goals.append({
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
                json.dump(goals, f, indent=4, ensure_ascii=False)  # ensure_ascii=False för att hantera svenska tecken
        except Exception as e:
            print(f"Error saving goals to JSON: {e}")
            return "Ett fel uppstod vid sparandet av målet."

        return redirect(url_for('menu'))

    return render_template('add_goal.html')


@app.route('/view_goals')
def view_goals():
    try:
        with open('goals.json', 'r') as f:
            goals = json.load(f)
    except FileNotFoundError:
        goals = []  # Hantera om filen inte finns
    return render_template('view_goals.html', goals=goals)


if __name__ == '__main__':
    app.run(debug=True)