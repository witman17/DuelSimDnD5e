class ActionManager:
    def __init__(self):
        self.actions = []

    def append_action(self, action):
        self.actions.append(action)

    def run_actions(self):
        for action in self.actions:
            action.do()
        self.actions.clear()
