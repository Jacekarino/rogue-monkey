# THIS FILE CONTAINS THE CONSUMABLE ITEM CLASS
# MEANING ONE TIME ITEMS THAT RECOVER HP OR MP
# AS WELL AS SCROLLS THAT INCREASE STATISTICS

from src.items.item import Item
from src.essential.logs import game_log

class Consumable(Item):
    def __init__(self, name, description, type, amount):
        super().__init__(name, description)
        self.type = type
        self.amount = amount

    def use(self, target):
        if self.type == 'HP':
            target.hp += self.amount
            game_log.add(f"Used {self.name}. Restored {self.amount} HP.")
        elif self.type == 'MP':
            target.mp += self.amount
            game_log.add(f"Used {self.name}. Restored {self.amount} MP.")
        elif self.type == 'XP':
            target.xp += self.amount
            game_log.add(f"Used {self.name}. Gained {self.amount} XP.")
        elif self.type == 'STR':
            target.stats['str'] += self.amount
            game_log.add(f"Used {self.name}. Increased Strength by {self.amount}.")
        elif self.type == 'DEX':
            target.stats['dex'] += self.amount
            game_log.add(f"Used {self.name}. Increased Dexterity by {self.amount}.")
        elif self.type == 'PER':
            target.stats['per'] += self.amount
            game_log.add(f"Used {self.name}. Increased Perception by {self.amount}.")
        elif self.type == 'VIT':
            target.stats['vit'] += self.amount
            game_log.add(f"Used {self.name}. Increased Vitality by {self.amount}.")
        elif self.type == 'INT':
            target.stats['int'] += self.amount
            game_log.add(f"Used {self.name}. Increased Intelligence by {self.amount}.")