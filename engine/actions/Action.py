from abc import ABC


class Action(ABC):
    def __init__(self, duelist, target):
        self.duelist = duelist
        self.target = target

    def do(self):
        pass
