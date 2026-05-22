# THIS FILE DEFINES A CHARACTER OBJECT
# IT USES SETTERS TO ADD HP AND MP FUNCTIONALITY
# ALSO DEFINES WHEN A CHARACTER IS CONSIDERED ALIVE

from src.entities.object import GameObject

class Character(GameObject):
    def __init__(self, x, y, symbol, color, name, max_hp, max_mp, stats):
        super().__init__(x, y, symbol, color, name)
        self._max_hp = max_hp
        self._hp = max_hp
        self._max_mp = max_mp
        self._mp = max_mp
        self.stats = stats

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    @property
    def max_hp(self):
        return self._max_hp + (self.stats['vit'] * 5)

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp = max(0, min(value, self.max_mp))
    
    @property
    def max_mp(self):
        return self._max_mp + (self.stats['int'] * 5)

    def is_alive(self):
        return self.hp > 0