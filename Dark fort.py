import random
 


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
item5 = Items("rope", "+1 on a trap roll")

#Weapons
weapon1 = Weapons("warhammer", 6, None)
weapon2 = Weapons("dagger", 4, "+1")
weapon3 = Weapons("sword", 6, "+1")
weapon4 = Weapons("flail", 6+1, None)

#Monsters
monster1 = Monster("blood-drenched skeleton", 3, 3, 4, 6, weapon1)
monster2 = Monster("catacomb cultist", 3, 3, 4, 6, "get_random_item(scrolls)")
monster3 = Monster("goblin", 3, 3, 4, 5, item5)
monster4 = Monster("undead hound", 3, 3, 4, 5, None)
monster5 = Monster("necro sorcerer", 4, 4, 4,8, "silver random.randint(3, 24)")
monster6 = Monster("small stone troll",5,7,6+1,9,None)
monster7 = Monster("medusa",4,4,6,10,"sliver random.randint(1,4)*random.randint(1,6)")
monster8 = Monster("ruin basilisk",4,4,6,11,None)

class Player:
    
    
    def __init__(self):
        self.hp = 15
        self.sp = 15 + random.randint(1, 6)
        self.weapons = [self.get_random_item("weapon")]
        self.items = [self.get_random_start_item()]
        self.history = []

    def get_random_start_item(self):
        start_items = [item1,item2,item3,item4]
        return random.choice(start_items)

    def get_random_item(self,item_type):
        if item_type == "weapon":
            weapons = [weapon1,weapon2,weapon3,weapon4]
            return random.choice(weapons)
        else:
            pass

    def explore(self):
        pass
    
    def combat(self):
        pass
    
    def use_item(self):
        pass

#This is the game function
def darkfort():
    
    player = Player()

    print(f"\nYour name is Kargunt. You begin with 15 hit points (hp) and {player.sp} silver (sp). You may carry unlimited items. \n"
          f"You own one weapon: {player.weapons[0].name} and one {player.items[0].name}.\n"
          f"Torch lit and {player.weapons[0].name} raised, you enter the dungeon.")
    player.history.append(f"Torch lit and {player.weapons[0].name} raised, you enter the dungeon.")
    print("What do you do?")
    
    while player.hp > 0:
        player.hp = 0
        print("\nYou have perished\n")

        #When someone dies their history is shown
        player.history.append("You have perished")
        for i in player.history:
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
