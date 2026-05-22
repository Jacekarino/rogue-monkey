# THIS FILE CONTAINS CHEAT CODES FOR DEBUGGING AND TESTING PURPOSES
# CAN BE USED TO ADVANCE QUICKER BY TYPING THE PHRASES DURING GAMEPLAY

from src.items.equipment import Equipment
from src.items.consumable import Consumable
from src.misc.colors import Colors
from src.essential.logs import game_log
from src.database.items_db import WEAPONS_DB, ARMORS_DB, CONSUMABLES_DB, SHIELDS_DB

def cheat_hp(game):
    game.player.hp = game.player.max_hp
    game_log.add(f"{Colors.BLUE}CHEAT: Fully healed!{Colors.RESET}")

def cheat_mp(game):
    game.player.mp = game.player.max_mp
    game_log.add(f"{Colors.BLUE}CHEAT: Mana restored!{Colors.RESET}")

def cheat_xp(game):
    game.player.gain_xp(game.player.level * 100 - game.player.xp)
    game_log.add(f"{Colors.BLUE}CHEAT: Leveled up!{Colors.RESET}")

def cheat_consumables(game):
    consumables = [Consumable(*args) for args in CONSUMABLES_DB]
    game.player.inventory.extend(consumables)
    game_log.add(f"{Colors.BLUE}CHEAT: Added all consumables!{Colors.RESET}")

def cheat_weapons(game):
    weapons = [Equipment(*args) for args in WEAPONS_DB]
    game.player.inventory.extend(weapons)
    game_log.add(f"{Colors.BLUE}CHEAT: Added all weapons!{Colors.RESET}")

def cheat_armors(game):
    armors = [Equipment(*args) for args in ARMORS_DB]
    game.player.inventory.extend(armors)
    game_log.add(f"{Colors.BLUE}CHEAT: Added all armor sets!{Colors.RESET}")

def cheat_shields(game):
    shields = [Equipment(name, slot, 0, bonus) for name, slot, bonus in SHIELDS_DB]
    game.player.inventory.extend(shields)
    game_log.add(f"{Colors.BLUE}CHEAT: Added all shields!{Colors.RESET}")

def cheat_skip(game):
    game.dungeon_level = 5
    game.start_level()
    game_log.add(f"{Colors.BLUE}CHEAT: Jumped to last level!{Colors.RESET}")

def cheat_lowmp(game):
    game.player.mp = 0
    game_log.add(f"{Colors.BLUE}CHEAT: Mana drained!{Colors.RESET}")

def cheat_lowhp(game):
    game.player.hp = 1
    game_log.add(f"{Colors.BLUE}CHEAT: Health extremely low!{Colors.RESET}")

CHEATS = {
    "pleasehelpme": cheat_hp,
    "magicimpulse": cheat_mp,
    "enlightenedmonkey": cheat_xp,
    "hugebagofstuff": cheat_consumables,
    "unstoppableforce": cheat_weapons,
    "ironmantime": cheat_armors,
    "guardianangel": cheat_shields,
    "skiptheadventure": cheat_skip,
    "brainfreeze": cheat_lowmp,
    "onehitknockout": cheat_lowhp
}


def handle_cheat(code, game):
    cheat_exists = code.lower().strip()
    if cheat_exists in CHEATS:
        CHEATS[cheat_exists](game)
        return True
    return False