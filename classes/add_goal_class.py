class AddGoal:
    def __init__(self):
        self.goal = ""
        self.deadline = ""
        self.daily_task = ""

    def set_goal(self, goal):
        self.goal = goal

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_daily_task(self, daily_task):
        self.daily_task = daily_task

    def get_goal(self):
        return self.goal

    def get_deadline(self):
        return self.deadline

    def get_daily_task(self):
        return self.daily_task