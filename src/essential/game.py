# THIS FILE CONTAINS THE GAME LOGIC AND DRAWS THE MAIN GAME SCREEN
# IT ALLOWS THE USER TO MOVE AROUND THE DUNGEON AND INTERACT WITH IT
# FIRST IT CREATES ENEMIES, CHESTS, TRAPS AROUND THE MAZE
# THEN IT RUNS THE GAME LOOP UNTIL THE PLAYER DIES OR WINS BY KILLING THE DRAGON

import os
import random
import math
from src.misc.colors import Colors
from src.essential.logs import game_log, GameOver
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.items.consumable import Consumable
from src.items.equipment import Equipment
from src.ui.inventory_ui import show_inventory
from src.ui.character_ui import show_stats
from src.ui.equipment_ui import show_equipment
from src.database.items_db import WEAPONS_DB, ARMORS_DB, CONSUMABLES_DB
from src.database.enemies_db import ENEMIES_DB
from src.essential.combat import combat
from src.essential.map import DungeonMap
from src.essential.generate import generate_loot, get_random_enemy_data
from src.misc.cheats import handle_cheat
from src.misc.how_to_play import INSTRUCTIONS

class Game: 
    def __init__(self):
        self.player = Player()
        self.dungeon_level = 1
        self.difficulty_mod = 1.0
        self.map = None
        self.running = True

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            self.clear()
            print("====================")
            print(f"= {Colors.GREEN}@{Colors.RESET} {Colors.CYAN}ROGUE{Colors.RESET} {Colors.GREEN}MONKEY{Colors.RESET} {Colors.CYAN}@{Colors.RESET} =") 
            print("====================")
            print("")
            print("1. Easy Mode")
            print("2. Normal Mode")
            print("3. Hard Mode")
            print("")
            print("0. How To Play")
            print("")

            menu_choice = input("Choose an option: ")
            if menu_choice == '0':
                self.clear()
                print(INSTRUCTIONS)
                input()
                continue

            elif menu_choice == '1': 
                self.difficulty_mod = 0.5
                break
            elif menu_choice == '2': 
                self.difficulty_mod = 1.0
                break
            elif menu_choice == '3': 
                self.difficulty_mod = 1.5
                break
            else:
                pass

        while True:
            self.clear()
            print("========================")
            print("= Pick a starting item =")
            print("========================")
            print("")
            print("1. Rusty Dagger (Weapon)")
            print("2. Torn Rags (Armor)")
            print("3. Pot Lid (Shield)")
            print("")
            
            item_choice = input("Action: ")
            
            starting_item = None
            if item_choice == '1':
                starting_item = Equipment("Rusty Dagger", "weapon", 3, 5)
                break
            elif item_choice == '2':
                starting_item = Equipment("Torn Rags", "armor", 2)
                break
            elif item_choice == '3':
                starting_item = Equipment("Pot Lid", "shield", 0, 5)
                break
            else:
                continue

        self.player.inventory = []
        self.player.inventory.append(starting_item)
        self.player.hp = self.player.max_hp
        self.player.mp = self.player.max_mp
        self.start_level()

    def start_level(self): 
        w, h = 40, 15
        self.map = DungeonMap(w, h, self.dungeon_level)
        
        while True:
            px, py = random.randint(1, w-2), random.randint(1, h-2)
            if not self.map.is_blocked(px, py):
                self.player.x, self.player.y = px, py
                break
        
        if self.dungeon_level == 5:
            while True:
                bx, by = random.randint(1, w-2), random.randint(1, h-2)
                if not self.map.is_blocked(bx, by) and (bx != self.player.x or by != self.player.y):
                    boss = Enemy(bx, by, "Dragon (Boss)", self.difficulty_mod)
                    self.map.enemies.append(boss)
                    break
        else:
            for _ in range(5 + self.dungeon_level):
                ex, ey = random.randint(1, w-2), random.randint(1, h-2)
                if not self.map.is_blocked(ex, ey):
                    enemy_data = get_random_enemy_data(self.dungeon_level)
                    self.map.enemies.append(Enemy(ex, ey, enemy_data[0], self.difficulty_mod, enemy_data))

        for _ in range(3):
            cx, cy = random.randint(1, w-2), random.randint(1, h-2)
            if not self.map.is_blocked(cx, cy):
                self.map.chests.append((cx, cy))

        for _ in range(3 + self.dungeon_level):
            tx, ty = random.randint(1, w-2), random.randint(1, h-2)
            if not self.map.is_blocked(tx, ty):
                self.map.traps.append({'x': tx, 'y': ty, 'visible': False})

        game_log.add(f"{Colors.MAGENTA}Entered Level {self.dungeon_level}.{Colors.RESET}")

    def draw_game(self):
        self.clear()
        view_range = self.player.stats['per']
        
        for y in range(self.map.height):
            for x in range(self.map.width):
                dist = math.sqrt((x - self.player.x)**2 + (y - self.player.y)**2)
                if dist <= view_range:
                    self.map.explored[y][x] = True

        print("-" * (self.map.width + 2))
        for y in range(self.map.height):
            row = "|"
            for x in range(self.map.width):
                char_to_draw = " "
                color = Colors.RESET
                dist = math.sqrt((x - self.player.x)**2 + (y - self.player.y)**2)
                
                if dist <= view_range:
                    if x == self.player.x and y == self.player.y:
                        char_to_draw = self.player.symbol
                        color = self.player.color
                    else:
                        enemy = next((e for e in self.map.enemies if e.x == x and e.y == y), None)
                        if enemy:
                            char_to_draw = enemy.symbol
                            color = enemy.color
                        elif (x, y) in self.map.chests:
                            char_to_draw = "C"
                            color = Colors.YELLOW
                        else:
                            trap = next((t for t in self.map.traps if t['x'] == x and t['y'] == y), None)
                            if trap and trap['visible']:
                                char_to_draw = "^"
                                color = Colors.BLUE
                            else:
                                char_to_draw = self.map.tiles[y][x]
                                if char_to_draw == '#': color = Colors.CYAN
                                elif char_to_draw == 'E': color = Colors.MAGENTA
                elif self.map.explored[y][x]:
                    char_to_draw = self.map.tiles[y][x]
                    color = Colors.GRAY
                
                row += f"{color}{char_to_draw}{Colors.RESET}"
            row += "|"
            print(row)
        print("-" * (self.map.width + 2))

        p = self.player
        print(f"  HP: {Colors.RED}{p.hp}/{p.max_hp}{Colors.RESET}  | MP: {Colors.BLUE}{p.mp}/{p.max_mp}{Colors.RESET} |  Level: {Colors.YELLOW}{p.level}{Colors.RESET}")
        print("")
        game_log.display()
        print("")
        print("------------------------------------------------------------------------")
        print(" [WASD] Move | [I] Inventory | [C] Character | [E] Equipment | [Q] Quit")
        print("------------------------------------------------------------------------")
        print("")

    def handle_input(self):
        action = input("Action: ").lower()
        
        if handle_cheat(action, self):
            return 

        dx, dy = 0, 0
        if action == 'w': dy = -1
        elif action == 's': dy = 1
        elif action == 'a': dx = -1
        elif action == 'd': dx = 1
        elif action == 'i': show_inventory(self)
        elif action == 'c': show_stats(self)
        elif action == 'e': show_equipment(self)
        elif action == 'q': raise GameOver("You quit the game. Loser.")
        
        if dx != 0 or dy != 0:
            nx, ny = self.player.x + dx, self.player.y + dy
            if self.map.is_blocked(nx, ny): return

            enemy = next((e for e in self.map.enemies if e.x == nx and e.y == ny), None)
            if enemy:
                combat(self, enemy)
                return

            if (nx, ny) in self.map.chests:
                self.map.chests.remove((nx, ny))
                loot = generate_loot(self.dungeon_level)
                self.player.inventory.append(loot)
                game_log.add(f"{Colors.GREEN}Found {loot.name}{Colors.RESET}")

            trap = next((t for t in self.map.traps if t['x'] == nx and t['y'] == ny), None)
            if trap:
                trap['visible'] = True
                self.player.hp -= 10
                game_log.add(f"{Colors.RED}Trap! You got slightly hurt.{Colors.RESET}")
                if self.player.hp <= 0: raise GameOver("You died to a trap. Lame.")

            if self.map.tiles[ny][nx] == 'E':
                self.dungeon_level += 1
                self.start_level()
                return

            self.player.x, self.player.y = nx, ny
            
            for e in self.map.enemies:
                e.take_turn(self.player, self.map)
                if e.x == self.player.x and e.y == self.player.y:
                    combat(self, e)

    def run(self):
        try:
            self.menu()
            while self.running:
                self.draw_game()
                self.handle_input()
        except GameOver as e:
            self.clear()
            print(f"{Colors.RED}============={Colors.RESET}")
            print(f"{Colors.RED}= GAME OVER ={Colors.RESET}")
            print(f"{Colors.RED}=============\n{Colors.RESET}")
            print(e)
        except KeyboardInterrupt:
            self.clear()
            print("Terminal force quit the game with an interrupt signal.")