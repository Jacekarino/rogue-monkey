# THIS FILE GENERATES LOOT FROM CHESTS
# AND RANDOMIZES ENCOUNTERED ENEMIES

import random
from src.items.equipment import Equipment
from src.items.consumable import Consumable
from src.database.items_db import WEAPONS_DB, ARMORS_DB, SHIELDS_DB, CONSUMABLES_DB
from src.database.enemies_db import ENEMIES_DB

def generate_loot(level):
    weapons = [Equipment(*args) for args in WEAPONS_DB]
    armors = [Equipment(*args) for args in ARMORS_DB]
    shields = [Equipment(name, slot, 0, bonus) for name, slot, bonus in SHIELDS_DB]
    
    if random.random() < 0.33:
        return random.choice(weapons + armors + shields)
    else:
        consumables = [Consumable(*args) for args in CONSUMABLES_DB]
        return random.choice(consumables)

def get_random_enemy_data(level):
    pool = ENEMIES_DB.get(level, ENEMIES_DB[5])
    return random.choice(pool)