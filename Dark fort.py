import random


 
class Player:
    def __init__(self):
        self.hp = 15
        self.sp = 15 + random.randint(1, 6)
        self.weapons = [self.get_random_item("Weapons")]
        self.item = [self.get_random_item("starting_item")]
        self.history = []

    def get_random_start_item(self):
        pass
    
    def explore(self):
        pass
    
    def combat(self):
        pass
    
    def use_item(self):
        pass

class Weapons:
    def __init__(self, name, damage, properties):
        self.name = name
        self.damage = damage
        self.properties = properties
    
    def use(self):
        pass
    
class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        pass

class Monster:
    def __init__(self, name, to_hit, points, damage, mhp, loot):
        self.name = name
        self.to_hit = to_hit
        self.points = points 
        self.damage = damage
        self.mhp = mhp
        self.loot = loot

    def combat(self):
        pass

#adding all items, weapons and monsters to the game
#items
item1 = Items("set of armour","-d4 damage")
item2 = Items("potion","heal d6 hp")
item3 = Items("scroll (summon weak daemon)", "The daemon helps you d4 fights dealing d4 damage.")
item4 = Items("cloak of invisibility", "Avoid d4 fights while acquiring all monster points.")


#Weapons
weapon1 = Weapons("warhammer", 6, None)
weapon2 = Weapons("dagger", 4, "+1")
weapon3 = Weapons("sword", 6, "+1")
weapon4 = Weapons("flail", 6+1, None)

#Monsters
Monster1 = Monster("blood-drenched skeleton",3,3,4,6, weapon1)
Monster2 = 
#All the random tables that can be selected are listed below.



tables = {
    "weapons": {
        "items": [
            "warhammer (d6)",
            "dagger (d4, +1 attack)",
            "sword (d6, +1 attack)",
            "flail (d6+1)"
        ],
        "category": "weapon"
    },
    "starting_item": {
        "items": [
            "set of armour (-d4 damage)",
            "potion (heal d6 hp)",
            "scroll (Summon weak daemon)",
            "cloak of invisibility"
        ],
        "category": "item"
    },
    "scrolls": {
        "items": [
            "scroll of summon weak daemon",
            f"scroll of Palms Open the Southern Gate (d6+1 damage) x{random.randint(1, 4)}",
            f"scroll of Aegis of Sorrow (-d4 damage) x{random.randint(1, 4)}",
            "scroll of False Omen (Either: When exploring a room you choose a result on the room table or reroll any die)"
        ],
        "category": "scroll"
    },
}

items_table = {
    "items": {
        "items": [
        tables["weapons"]["items"], 
        "potion (heal d6 hp)",
        "rope (+1 on a trap roll)",
        tables["scrolls"]["items"], 
        "set of armour (-d4 damage)",
        "cloak of invisibility"
        ],
        "category": "item"
    }
}

#dictionary of monsters and their stats
#Weak monsters
monsters = {
    "blood-drenched skeleton": {
        "category": "weak",
        "to_hit": 3,
        "points": 3,
        "damage": 4,
        "mhp": 6,
        "loot": "dagger (d4, +1 attack)"
    },
    "catacomb cultist": {
        "category": "weak",
        "to_hit": 3,
        "points": 3,
        "damage": 4,
        "mhp": 6,
        "loot": get_random_item("scrolls")
    },
    "goblin": {
        "category": "weak",
        "to_hit": 3,
        "points": 3,
        "damage": 4,
        "mhp": 5,
        "loot": "rope (+1 on a trap roll)"
    },
    "undead hound": {
        "category": "weak",
        "to_hit": 3,
        "points": 3,
        "damage": 4,
        "mhp": 5,
        "loot": None
    },
    "necro sorcerer": {
        "category": "tough",
        "to_hit": 4,
        "points": 4,
        "damage": 4,
        "other_attack": False,
        "other_attack_damage": 6,
        "mhp": 8,
        "loot": random.randint(3, 24)  # silver
    },
    "small stone troll":{
        "category": "tough",
        "to hit":5,
        "points":7,
        "damage":6, #+1
        "mhp":9,
    },
    "medusa":{
        "category": "tough",
        "to hit":4,
        "points":4,
        "damage":6, 
        "mhp":10,
        "loot":random.randint(1,4)*random.randint(1,6) #silver
    },
    "ruin basilisk":{
        "category": "tough",
        "to hit":4,
        "points":4,
        "damage":6,
        "mhp":11,
    }
}

def get_random_items(table_name):
    table_data = items_table[table_name]
    chosen_item = random.choice(table_data["items"])
    return chosen_item, table_data["category"]

def get_random_other(table_name):
    table_data = tables[table_name]
    chosen_item = random.choice(table_data["items"])
    return chosen_item, table_data["category"]

def get_random_monster(category):
    monster_list = [monster for monster, data in monsters.items() if data["category"] == category]
    chosen_monster = random.choice(monster_list)
    return chosen_monster, category

def table_entrance():
    options = [
        get_random_items("items"),
        get_random_other("scrolls"),
        f"a dying mystic gives you {get_random_other('scrolls')[0]}",
        f"{get_random_monster('weak')[0]} stands guard. Attack!",
        "You find the entrance is eerily quiet and desolate"
    ]
    
    return random.choice(options)


#This is the game function
def darkfort():

    #Start of game variables
    Player()
    print(f"\nYour name is Kargunt. You begin with 15 hit points (hp) and {sp} silver (sp). You may carry unlimited items. \nYou own one weapon: {list(weapons.keys())[0]} and one {list(items.keys())[0]}.\n")
    print(f"Torch lit and {list(weapons.keys())[0].split()[0]} raised, you enter the dungeon.")
    print("What do you do?")
    table_entrance()
    while hp > 0:
        if attacked:
            combat(outcome[0])
            attacked = False
            

        hp = 0
        #When someone dies their history is shown
        print("\nYou have perished\n")
        history.append("You have perished")
        for i in history:
            print(i)
    return

# This is the menu to start the game
menu ={1:"Press 1 for New Game",
       2:"Press 2 to Quit"
       }

#Start menu for game 
def start_game():
    answer = True
    while answer:
        print("\nWelcome to Dark Fort!\n")
        for option in menu:
            print(menu[option])
        answer = input()
        if answer =="1":
            darkfort()
        elif answer == "2":
            print("\nGoodbye\n")
            break
        else:
            print("\nEnter valid selection \n")
            continue

if __name__ == "__main__":
    start_game()
