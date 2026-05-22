# THIS FILE DRAWS THE INVENTORY SCREEN
# ALLOWS THE USER TO USE OR EQUIP ITEMS
# AS WELL AS INPSECT THEM TO SEE WHAT THEY DO

from src.misc.colors import Colors
from src.items.equipment import Equipment
from src.items.consumable import Consumable

def show_inventory(game):
    while True:
        game.clear()
        print("=============")
        print(f"= INVENTORY =")
        print("=============")
        print("")
        
        items = game.player.inventory
        
        if not items:
            print("Your backpack is empty.")
        else:
            for i, item in enumerate(items):  
                print(f"  {i+1}. {item.name}")

        print("")
        print("-------------------------------------------------")
        print(" [#] Use/Equip  |  [#?] Inspect  |  [Enter] Back")
        print("-------------------------------------------------")
        print("")
        
        inv_choice = input("Action: ").strip()
        
        if inv_choice == '':
            break 
        
        if inv_choice.endswith('?'):
            try:
                idx = int(inv_choice[:-1]) - 1 
                if 0 <= idx < len(items):
                    item = items[idx]
                    print(f"\n--- {item.name} ---\n")
                    print(f"Description: {item.description}")
                    
                    if isinstance(item, Equipment):
                        if item.slot == 'weapon':
                            print(f"Slot: {item.slot}")
                            print(f"Attack power bonus: +{item.stat_bonus}")
                            if item.type_bonus > 0:
                                print(f"Critical chance bonus: +{item.type_bonus}%")
                        elif item.slot == 'armor':
                            print(f"Slot: {item.slot}")
                            print(f"Defense bonus: +{item.stat_bonus}")
                            if item.type_bonus > 0:
                                print(f"Special bonus: +{item.type_bonus}%")
                        elif item.slot == 'shield':
                            print(f"Slot: {item.slot}")
                            print(f"Block Chance: {item.type_bonus}%")   

                    elif isinstance(item, Consumable):
                        print(f"Restores: {item.amount} {item.type}")   
                    
                    input("\n--- Press Enter to return... ---")
                else:
                    input("Invalid item number.")
            except ValueError:
                pass
        
        else:
            try:
                idx = int(inv_choice) - 1
                if 0 <= idx < len(items):
                    item = items[idx]
                    item.use(game.player)
                    items.pop(idx)
                else:
                    pass
            except ValueError:
                pass