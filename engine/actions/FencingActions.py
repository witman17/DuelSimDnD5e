from .Action import Action


class Natarcie(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        self.duelist.natarcie(self.target)


class PrzeciwNatarcie(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        self.duelist.przeciw_natarcie(self.target)


class Rozpoznanie(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        self.duelist.rozpoznanie(self.target)


class Zaslona(Action):
    def __init__(self, duelist, target):
        super().__init__(duelist, target)

    def do(self):
        self.duelist.zaslona(self.target)
