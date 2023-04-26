from ..duelist.Duelist import Duelist


class Round:
    def __init__(self):
        self.actions = []

    def log_action(self, action, duelist, data):
        self.actions.append({'action': action,
                             'duelist': duelist,
                             'data': data})

    def __str__(self):
        to_str = []
        for i in range(len(self.actions)):
            to_str.append(f'Action {i}: {self.actions[i]["duelist"].name}->{self.actions[i]["action"]}')
            to_str.append(f' +--->: {self.actions[i]["data"]}')
        return '\n'.join(to_str)


class ScoreTracker:
    def __init__(self, duelists: {}):
        self._winner = None
        self._rounds = []
        self._duelists = duelists

    def log_action(self, action, duelist, data):
        self._rounds[-1].log_action(action, duelist, data)
        if action == Duelist.attack and data['result']:
            self.count_hit(duelist)

    def new_round(self):
        self._rounds.append(Round())

    def count_hit(self, duelist):
        if self._winner:  # do not count hits after winner is revealed
            return

        self._duelists[duelist] += 1
        if self._duelists[duelist] >= 3 and not self._winner:
            self._winner = duelist

    @property
    def current_round(self):
        return len(self._rounds) - 1

    @property
    def winnner(self):
        return self._winner

    def __str__(self):
        duelists = [*self._duelists]
        to_str = [f'After {len(self._rounds)} rounds the winner is {self._winner.name}',
                  f'Score: {duelists[0].name} ({self._duelists[duelists[0]]} - {self._duelists[duelists[1]]}) {duelists[1].name}']

        for i in range(len(self._rounds)):
            to_str.append(f'--- Round {i}:  ---')
            to_str.append(self._rounds[i].__str__())
        return '\n'.join(to_str)
