from flask import Flask, render_template, request, redirect, url_for
from classes.add_goal_class import AddGoal
from classes.view_goals_class import ViewGoals

app = Flask(__name__)

add_goal_instance = AddGoal()
view_goals_instance = ViewGoals()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'add_goal':
            return redirect(url_for('add_goal'))
        elif choice == 'view_goals':
            return redirect(url_for('view_goals'))
    return render_template('index.html')

@app.route('/add_goal', methods=['GET', 'POST'])
def add_goal():
    if request.method == 'POST':
        # Hantera stegvis inmatning här
        pass  # Implementera logiken för stegvis inmatning
    return render_template('add_goal.html')

@app.route('/view_goals')
def view_goals():
    goals = view_goals_instance.get_goals()
    return render_template('view_goals.html', goals=goals)

if __name__ == '__main__':
    app.run(debug=True)