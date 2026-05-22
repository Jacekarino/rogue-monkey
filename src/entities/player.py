# THIS FILE CREATES A PLAYER OBJECT AND DRAWS IT
# IT INHERITS FROM CHARACTER AND GIVES STATS
# ALSO ADDS METHODS TO EQUIP AND UNEQIP ITEMS
# AS WELL AS LEVELING UP AND BUFFS BASED ON STATS AND EQUIPMENT

from src.entities.character import Character
from src.misc.colors import Colors
from src.essential.logs import game_log

class Player(Character):
    def __init__(self):
        stats = {'str': 3, 'dex': 3, 'per': 3, 'vit': 3, 'int': 3}
        super().__init__(0, 0, '@', Colors.GREEN, "Hero", 85, 35, stats)
        self.level = 1
        self.xp = 0
        self.attribute_points = 0
        self.inventory = []
        self.equipment = {'weapon': None, 'armor': None, 'shield': None}

    def equip_item(self, item):
        current = self.equipment.get(item.slot)
        if current:
            self.inventory.append(current)
        self.equipment[item.slot] = item
        game_log.add(f"{Colors.GREEN}Equipped {item.name}.{Colors.RESET}")

    def unequip_item(self, slot):
        current = self.equipment.get(slot)
        if current:
            self.inventory.append(current)
            self.equipment[slot] = None
            game_log.add(f"{Colors.GREEN}Unequipped {current.name}.{Colors.RESET}")
            return current
        else:
            game_log.add(f"{Colors.GREEN}Nothing to unequip from {slot}.{Colors.RESET}")
            return None

    def get_attack_power(self):
        base = self.stats['str'] * 2
        bonus = self.equipment['weapon'].stat_bonus if self.equipment['weapon'] else 0
        return base + bonus

    def get_defense(self):
        return self.equipment['armor'].stat_bonus if self.equipment['armor'] else 0

    def gain_xp(self, amount):
        self.xp += amount
        game_log.add(f"{Colors.YELLOW}Gained {amount} XP.{Colors.RESET}")
        if self.xp >= self.level * 100:
            self.level += 1
            self.xp = 0
            self.attribute_points += 3
            self._hp = self.max_hp
            self._mp = self.max_mp
            game_log.add(f"{Colors.YELLOW}LEVEL UP! Currently level {self.level}. You gained 3 points.{Colors.RESET}")