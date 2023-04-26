from .Action import Action


class Attack(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        self.duelist.attack(self.target)


class Initiative(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        return self.duelist.initiative()
