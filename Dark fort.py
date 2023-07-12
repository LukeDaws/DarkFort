from random import randint,choice


#All the random tables that can be selected are listed below
def table_starting_weapon():

    table_starting_weapon = ["warhammer (d6)",
                   "dagger (d4, +1 attack)",
                   "sword (d6, +1 attack)",
                   "flail (d6+1)"
                   ]
    
    chosen_weapon = choice(table_starting_weapon)
    cat = "weapon"
    return chosen_weapon,cat
    

def table_starting_item():
    
    table_starting_item = ["set of armour (-d4 damage)",
                 "potion (heal d6 hp)",
                 "scroll (Summon weak daemon)",
                 "cloak of invisibility"
                 ]
    
    chosen_starting_item = choice(table_starting_item)
    return chosen_starting_item

def table_scrolls():
    
    table_scrolls = ["scroll of summon weak daemon",
                     f"scroll of Palms Open the Southern Gate (d6+1 damage) x{randint(1,4)}", 
                     f"scroll of Aegis of Sorrow (-d4 damage) x{randint(1,4)}",
                     "scroll of False Omen (Either: When exploring a room you choose a result on the room table or reroll any die)"
                     ]
    
    chosen_scroll = choice(table_scrolls)
    cat = "scrolls"
    return chosen_scroll, cat

def table_items():
    
    table_items = [table_starting_weapon(),
             "potion (heal d6 hp)",
             "rope (+1 on a trap roll)",
             table_scrolls(),
             "set of armour (-d4 damage)",
             "cloak of invisibility"
             ]

    chosen_item = choice(table_items)
    if len(chosen_item) == 2:
        if chosen_item[1] == "weapon":
            return chosen_item[0],chosen_item[1]
        elif chosen_item[1] == "scrolls":
            cat = "scroll"
            return chosen_item[0],cat
    cat = "item"
    return chosen_item,cat

def table_weak():
    
    table_weak = ["a Blood-Drenched Skeleton",
                "a Catacomb Cultist",
                "a Goblin",
                "an Undead Hound"
                ]
    
    chosen_weak = choice(table_weak)
    cat = "weak"
    return chosen_weak

def table_entrance():
    
    table_entrance = [table_items(),
            f"you are attacked by {table_weak()}",
             table_scrolls(),
            "you find the entrance is eerily quiet and desolate"
            ]
    
    chosen_entrance = choice(table_entrance)
    if len(chosen_entrance) == 2:
        if chosen_entrance[1] == "weapon":
            return f"you find a {chosen_entrance[0]}.",chosen_entrance[0],chosen_entrance[1]
        elif chosen_entrance[1] == "scroll":
            return f"you find a {chosen_entrance[0]}.",chosen_entrance[0],chosen_entrance[1]
        elif chosen_entrance[1] == "scrolls":
            return f"a dying mystic gives you a {chosen_entrance[0]}.",chosen_entrance[0],chosen_entrance[1]
        else:
            return f"you find a {chosen_entrance[0]}.",chosen_entrance[0],chosen_entrance[1]
    return chosen_entrance, None, None


#This is the game function
def darkfort():

    hp = 15
    sp = 15 + randint(1,6)
    weapons = {table_starting_weapon()[0]:1}
    items = {table_starting_item():1}
    print(f"\nYour name is Kargunt. You begin with 15 hit points (hp) and {sp} silver (sp). You may carry unlimited items. \nYou own one weapon: {list(weapons.keys())[0]} and one {list(items.keys())[0]}.\n")
    
    while hp > 0:
        
        outcome = table_entrance()
        print(f"Torch lit and {list(weapons.keys())[0].split()[0]} raised, you enter the dungeon.\nAs you walk through the entrance {outcome[0]}")

        if outcome[2] == "weapon":
            weapons[outcome[1]] = weapons.get(outcome[1],0) + 1
        elif outcome[2] == "weak":
            

        elif outcome[2] != None:
            items[outcome[1]] = items.get(outcome[1],0) + 1

        print("What do you do?")

        hp = 0
        print("\nYou have perished\n")
    return

# This is the menu to start the game
menu ={1:"Press 1 for New Game",
       2:"Press 2 to Quit"
       } 
answer = True
while answer:
    print("\nWelcome to Dark fort!\n")
    for option in menu:
        print(menu[option])
    answer = input()
    if answer == "1":
        darkfort()
    elif answer == "2":
        print("\nGoodbye \n")
        break
    else:
        print("\nEnter valid selection \n")