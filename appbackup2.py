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