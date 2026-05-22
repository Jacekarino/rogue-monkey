# THIS FILE DRAWS THE CHARACTER STATS SCREEN
# ALLOWS THE USER TO UPGRADE THEIR STATS WHEN THEY LEVEL UP AS WELL

from src.misc.colors import Colors

def show_stats(game):
    while True:
        game.clear()
        p = game.player
        s = p.stats
        
        print("==========")
        print(f"= STATS: =")
        print("==========")

        total_atk = p.get_attack_power()
        min_dmg = int(total_atk)
        max_dmg = int(total_atk * 1.2)
        total_def = p.get_defense()
        crit_chance = s['dex'] * 3
        if p.equipment['weapon']:
            crit_chance += p.equipment['weapon'].type_bonus 
        crit_chance = min(100, crit_chance) 
        block_chance = 0
        if p.equipment['shield']:
            block_chance = p.equipment['shield'].type_bonus
        
        print("")
        print(f"Hero Level       : {Colors.YELLOW}{p.level}{Colors.RESET}")
        print(f"Current XP       : {Colors.YELLOW}{p.xp} / {p.level * 100}{Colors.RESET}")
        print(f"Available points : {Colors.YELLOW}{p.attribute_points}{Colors.RESET}")
        print("")
        print(f"Total health     : {Colors.RED}{p.max_hp}{Colors.RESET}")
        print(f"Total mana       : {Colors.BLUE}{p.max_mp}{Colors.RESET}")
        print("")
        print(f"Attack power     : {min_dmg} - {max_dmg}")
        print(f"Critical Chance  : {crit_chance}%")
        print(f"Defense amount   : {total_def}")
        print(f"Block Chance     : {block_chance}%")
        print("")
        print(f"[S] Strength     : {s['str']:<3} {Colors.GRAY}(Increases your attack power){Colors.RESET}")
        print(f"[D] Dexterity    : {s['dex']:<3} {Colors.GRAY}(Decides your critical hit chance){Colors.RESET}")
        print(f"[P] Perception   : {s['per']:<3} {Colors.GRAY}(Enhances your vision range){Colors.RESET}")
        print(f"[I] Intelligence : {s['int']:<3} {Colors.GRAY}(How much mana you have){Colors.RESET}")
        print(f"[V] Vitality     : {s['vit']:<3} {Colors.GRAY}(How much HP you have){Colors.RESET}")
        print("")

        print("------------------------------------------------")
        print(" [S/D/P/I/V] Upgrade Attribute  |  [Enter] Back")
        print("------------------------------------------------")
        print("")

        upgrade_choice = input("Action: ").lower().strip()
        
        if upgrade_choice == "":
            break
        
        if p.attribute_points > 0:
            if upgrade_choice == 's': s['str'] += 1; p.attribute_points -= 1
            elif upgrade_choice == 'd': s['dex'] += 1; p.attribute_points -= 1
            elif upgrade_choice == 'p': s['per'] += 1; p.attribute_points -= 1
            elif upgrade_choice == 'i': 
                s['int'] += 1
                p.attribute_points -= 1
                p._mp += 5
            elif upgrade_choice == 'v': 
                s['vit'] += 1
                p.attribute_points -= 1
                p._hp += 5