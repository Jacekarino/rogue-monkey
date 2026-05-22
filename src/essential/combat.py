# THIS FILE HANDLES COMBAT BETWEEN PLAYER AND ENEMY
# IT ALSO DRAWS THE BATTLE UI AND CONTAINS A GAME WIN CONDITION

import random
from src.misc.colors import Colors
from src.essential.logs import game_log, GameOver
from src.ui.inventory_ui import show_inventory

def combat(self, enemy):
    game_log.add(f"Starting a battle with {enemy.name}!")
    auto = False
    
    while enemy.is_alive() and self.player.is_alive():
        self.clear()
        game_log.display()

        print("")
        print("==========")
        print(f"= COMBAT =")
        print("==========")
        print("")
        print(f"{Colors.CYAN}You:{Colors.RESET} {self.player.hp} HP | {self.player.mp} MP")
        print("")
        print(f"{Colors.RED}{enemy.name}:{Colors.RESET} {enemy.hp} HP")
        print("")
        print("------------------------------------------------------------------")
        print("[1] Attack | [2] Inventory | [3] Auto-Battle | [4] Wait | [5] Flee") 
        print("------------------------------------------------------------------")
        print("")

        combat_choice = '1' if auto else input("Action: ")
        
        if combat_choice == '':
            continue

        if combat_choice == '1':
            base_dmg = self.player.get_attack_power()
            dmg = int(base_dmg * random.uniform(1.0, 1.2))
            
            crit_chance = self.player.stats['dex'] * 3
            weapon = self.player.equipment['weapon']
            if weapon: crit_chance += weapon.type_bonus
            crit_chance = min(100, crit_chance)
            
            if random.randint(1, 100) <= crit_chance:
                if self.player.mp >= 10:
                    self.player.mp -= 10
                    dmg *= 2
                    game_log.add(f"{Colors.CYAN}CRITICAL HIT! (-10 MP){Colors.RESET}")
                else:
                    game_log.add(f"{Colors.RED}Tried to land a critical hit, but failed due to low MP.{Colors.RESET}")

            enemy.hp -= dmg
            game_log.add(f"{Colors.CYAN}Hit {enemy.name} for {dmg} damage.{Colors.RESET}")

        elif combat_choice == '2':
            show_inventory(self)
            continue
        elif combat_choice == '3':
            auto = True
            game_log.add("Auto-battle enabled.")
            continue
        elif combat_choice == '4':
            game_log.add("You wait...")
        elif combat_choice == '5':
            if random.random() < 0.5:
                self.player.x -= 1
                game_log.add("Escaped battle.")
                return
            else:
                game_log.add(f"{Colors.RED}Escape failed!{Colors.RESET}")
        else:
            continue

        if enemy.is_alive():
            base_dmg = enemy.stats['str'] * 2
            defense = self.player.get_defense()
            dmg_calc = max(1, base_dmg - defense)
            dmg = int(dmg_calc * random.uniform(1.0, 1.2))
            block_chance = 0
            shield = self.player.equipment['shield']
            if shield: block_chance = shield.type_bonus
            
            if random.randint(1, 100) <= block_chance:
                if self.player.mp >= 25:
                    self.player.mp -= 25
                    game_log.add(f"{Colors.CYAN}Blocked enemy attack! (-25 MP){Colors.RESET}")
                else:
                    game_log.add(f"{Colors.CYAN}Tried to block, but failed due to low MP.{Colors.RESET}")
                    self.player.hp -= dmg
                    game_log.add(f"{Colors.RED}Took {dmg} damage.{Colors.RESET}")
            else:
                self.player.hp -= dmg
                game_log.add(f"{Colors.RED}Took {dmg} damage.{Colors.RESET}")

    if not self.player.is_alive(): raise GameOver("You died in a battle.")
    
    xp_gain = getattr(enemy, 'xp_reward', 50 * self.dungeon_level)
    self.player.gain_xp(xp_gain)
    self.map.enemies.remove(enemy)
    game_log.add(f"Defeated {enemy.name}!")
    
    if "Dragon (Boss)" in enemy.name:
        raise GameOver(f"{Colors.YELLOW}You have slain the legendary Dragon!{Colors.RESET}")