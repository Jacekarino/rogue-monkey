# THIS FILE DRAWS THE CURRENT EQIUPMENT SCREEN
# ALLOWS THE USER TO UNEQUIP ITEMS FROM THE RESPECTIVE SLOTS

from src.misc.colors import Colors

def show_equipment(game):
    while True:
        game.clear()
        print("=============")
        print(f"= EQUIPMENT =")
        print("=============")
        print("")
        
        eq = game.player.equipment
        
        def format_item(item):
            if not item: return f" "
            return f"{item.name}"

        print(f"  [W] Weapon : {format_item(eq.get('weapon'))}")
        print(f"  [A] Armor  : {format_item(eq.get('armor'))}")
        print(f"  [S] Shield : {format_item(eq.get('shield'))}")
        print("")

        print("---------------------------------------")
        print(" [W/A/S] Unequip Slot  |  [Enter] Back")
        print("---------------------------------------")
        print("")

        eq_choice = input("Action: ").lower().strip()
        if eq_choice == "":
            break
        
        if eq_choice == 'w': game.player.unequip_item('weapon')
        elif eq_choice == 'a': game.player.unequip_item('armor')
        elif eq_choice == 's': game.player.unequip_item('shield')