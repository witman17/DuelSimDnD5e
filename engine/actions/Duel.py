import heapq

from .ActionManager import *
from .BasicActions import *
from .FencingActions import *
from .Score import *


class Duel:
    def __init__(self, duelist1, duelist2):
        self._duelists = {duelist1: 0,
                          duelist2: 0}
        self._score = ScoreTracker(self._duelists)
        duelist1.register_action_logger(self._score)
        duelist2.register_action_logger(self._score)
        self._action_manager = ActionManager()

    def simulate(self, max_rounds):
        while not self._score.winnner and self._score.current_round < max_rounds:
            self.new_round()
            order = self.roll_initiative()
            self.makeFencingActions()
            self.makeMainActions(order)

        print(self._score)

    def new_round(self):
        self._score.new_round()
        for duelist in self._duelists:
            duelist.reset_conditions()

    def roll_initiative(self):
        order = []
        heapq.heapify(order)
        for duelist in self._duelists:
            heapq.heappush(order, (-1 * duelist.initiative(), duelist))
        return order

    def makeFencingActions(self):
        duelists = [*self._duelists]
        self._action_manager.append_action(Natarcie(duelists[0], duelists[1]))
        self._action_manager.append_action(Zaslona(duelists[1], duelists[0]))
        self._action_manager.run_actions()

    def makeMainActions(self, order):
        self._action_manager.append_action(Attack(order[0][1], order[1][1]))
        self._action_manager.append_action(Attack(order[1][1], order[0][1]))
        self._action_manager.run_actions()
