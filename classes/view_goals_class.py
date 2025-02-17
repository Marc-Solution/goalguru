import json

class ViewGoals:
    def __init__(self):
        self.goals = self.load_goals()

    def load_goals(self):
        with open('goals.json', 'r') as f:
            return json.load(f)

    def get_goals(self):
        return self.goals