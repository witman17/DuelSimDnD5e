from engine.actions.Roller import *
from .Attributes import *

NAME = 'name'
LEVEL = 'level'
ATTRIBUTES = 'attributes'
PROFICIENCY = 'proficiency'
ARMOR = 'armor'
INITIATIVE = 'initiative'
HIT_DICE = 'hit_dice'
ATTACK_MODIFIER = 'attack_modifier'


class Duelist:
    def __init__(self, name: str, level: int, attributes: Attributes, armor: int, initiative: int, hit_dice: int):
        self._logger = None
        self._stats = {}
        self._conditions = {}
        self._hit_observers = []
        self._stats[LEVEL] = level
        self._stats[PROFICIENCY] = math.ceil(level / 4.0) + 1
        self._stats[ATTRIBUTES] = attributes
        self._stats[ARMOR] = armor
        self._stats[INITIATIVE] = initiative
        self._stats[HIT_DICE] = hit_dice
        self._name = name
        self._current_hit_dice = level

    def register_action_logger(self, logger):
        self._logger = logger

    def condition(self, stat, modifier):
        if stat in self._conditions:
            self._conditions[stat] += modifier
        else:
            self._conditions[stat] = modifier

    def reset_conditions(self):
        self._conditions.clear()

    def check_hit(self, to_hit: int) -> bool:
        current_armor = self._stats[ARMOR]
        if ARMOR in self._conditions:
            current_armor += self._conditions[ARMOR]
        return to_hit >= current_armor

    # Standard Actions:
    def attack(self, target):
        attack_bonus = self._stats[PROFICIENCY] + self._stats[ATTRIBUTES].get_modifier(Attribute.STRENGTH)
        if ATTACK_MODIFIER in self._conditions:
            attack_bonus += self._conditions[ATTACK_MODIFIER]
        to_hit = roll_dice(1, 20, attack_bonus)
        hit = target.check_hit(to_hit)
        self._logger.log_action(Duelist.attack, self, {'attack_bonus': attack_bonus,
                                                       'to_hit': to_hit,
                                                       'result': hit
                                                       })

    def initiative(self) -> int:
        initiative = roll_dice(1, 20, self._stats[INITIATIVE])
        self._logger.log_action(Duelist.initiative, self, {'initiative': self._stats[INITIATIVE],
                                                           'result': initiative})
        return initiative

    # Fencing actions
    def natarcie(self, oponent):
        if not self.use_hit_dice():
            return
        boon = roll_dice(1, self._stats[HIT_DICE], self._stats[ATTRIBUTES].get_modifier(Attribute.STRENGTH))
        self.condition(ATTACK_MODIFIER, boon)
        self._logger.log_action(Duelist.natarcie, self, {'hit_dice': self._stats[HIT_DICE],
                                                         'strength': self._stats[ATTRIBUTES].get_modifier(
                                                             Attribute.STRENGTH),
                                                         'boon': ATTACK_MODIFIER,
                                                         'result': boon})

    def przeciw_natarcie(self, oponent):
        if not self.use_hit_dice():
            return
        bane = - roll_dice(1, self._stats[HIT_DICE], self._stats[ATTRIBUTES].get_modifier(Attribute.STRENGTH))
        oponent.condition(ATTACK_MODIFIER, bane)
        self._logger.log_action(Duelist.przeciw_natarcie, self, {'hit_dice': self._stats[HIT_DICE],
                                                                 'strength': self._stats[ATTRIBUTES].get_modifier(
                                                                     Attribute.STRENGTH),
                                                                 'bane': ATTACK_MODIFIER,
                                                                 'result': bane})

    def rozpoznanie(self, oponent):
        if not self.use_hit_dice():
            return
        bane = - roll_dice(1, self._stats[HIT_DICE], self._stats[ATTRIBUTES].get_modifier(Attribute.INTELLIGENCE))
        oponent.condition(ATTACK_MODIFIER, bane)
        self._logger.log_action(Duelist.rozpoznanie, self, {'hit_dice': self._stats[HIT_DICE],
                                                            'intelligence': self._stats[ATTRIBUTES].get_modifier(
                                                                Attribute.INTELLIGENCE),
                                                            'bane': ATTACK_MODIFIER,
                                                            'result': bane})

    def zaslona(self, oponent):
        if not self.use_hit_dice():
            return
        boon = roll_dice(1, self._stats[HIT_DICE], self._stats[ATTRIBUTES].get_modifier(Attribute.INTELLIGENCE))
        self.condition(ARMOR, boon)
        self._logger.log_action(Duelist.zaslona, self, {'hit_dice': self._stats[HIT_DICE],
                                                        'intelligence': self._stats[ATTRIBUTES].get_modifier(
                                                            Attribute.INTELLIGENCE),
                                                        'boon': ARMOR,
                                                        'result': boon})

    def use_hit_dice(self):
        hit_dice_left = self._current_hit_dice > 0
        self._logger.log_action(Duelist.use_hit_dice, self, {'current_hit_dice': self._current_hit_dice,
                                                             'result': hit_dice_left})
        if hit_dice_left:
            self._current_hit_dice -= 1
        return hit_dice_left

    # properties:
    @property
    def name(self) -> str:
        return self._name

    @property
    def stats(self):
        return self._stats

    @property
    def attributes(self) -> Attributes:
        return self._stats[ATTRIBUTES]
