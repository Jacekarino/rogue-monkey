# THIS FILE CONTAINS THE EQUIPMENT ITEM CLASS
# MEANING WEAPONS, ARMORS AND SHIELDS

from src.items.item import Item
from src.essential.logs import game_log

class Equipment(Item):
    def __init__(self, name, slot, stat_bonus, type_bonus=0):
        super().__init__(name, f"Equip to enhance your stats.")
        self.slot = slot
        self.stat_bonus = stat_bonus
        self.type_bonus = type_bonus 

    def use(self, target):
        target.equip_item(self)