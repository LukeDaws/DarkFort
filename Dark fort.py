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

class Scrolls:
    def __init__(self,name, description, uses):
        self.name = name
        self.description = description
        self.uses = random.randint(1, uses)
    
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
#Weapons
weapon1 = Weapons("warhammer", 6, None)
weapon2 = Weapons("dagger", 4, "+1")
weapon3 = Weapons("sword", 6, "+1")
weapon4 = Weapons("flail", 6+1, None)

#Scrolls
scroll1 = Scrolls("summon weak daemon scroll", "The daemon helps you d4 fights dealing d4 damage.",4)
scroll2 = Scrolls("palms open the southern gate scroll","d6+1 damage", 4)
scroll3 = Scrolls("aegis of sorrow scroll", "-d4 damage", 4)
scroll4 = Scrolls("false omen scroll", "When exploring a room you choose a result on the room table or reroll any die",1)

#items
item1 = Items("set of armour","-d4 damage")
item2 = Items("potion","Heal d6 hp")
item3 = scroll1
item4 = Items("cloak of invisibility", "Avoid d4 fights while acquiring all monster points.")
item5 = Items("rope", "+1 on a trap roll")

#Monsters
monster1 = Monster("blood-drenched skeleton", 3, 3, 4, 6, weapon2)
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
        self.weapons = [self.get_random_start_weapon()]
        self.items = [self.get_random_start_item()]
        self.history = []
        
        #These are only used to get the starting items
    def get_random_start_item(self):
        start_items = [item1,item2,item3,item4]
        return random.choice(start_items)
    def get_random_start_weapon(self):
        start_weapons = [weapon1,weapon2,weapon3,weapon4]
        return random.choice(start_weapons)

    def get_random_item(self,item_type):
        weapons = [weapon1,weapon2,weapon3,weapon4]
        scrolls = [scroll1,scroll2,scroll3,scroll4]
        items = [item1,item2,item3,item4,item5,random.choice(scrolls),random.choice(weapons)]
        if item_type == "weapon":
            selection = random.choice(weapons)
            self.weapons.append(selection)
            return selection
        elif item_type == "scroll":
            selection = random.choice(scrolls)
            self.items.append(selection)
            return selection
        else:
            selection = random.choice(items)
            self.items.append(selection)
            return selection
    
    def combat(self,difficulty):
        if difficulty == "weak":
            w_monsters = [monster1,monster2,monster3,monster4]
            return random.choice(w_monsters)
        else:
            t_monsters = [monster5,monster6,monster7,monster8]
        return random.choice(t_monsters)
    #This is only used when the player starts the game for the first time.
    def entrance(self):
        roll = random.randint(1,4)
        if roll == 1:
            self.get_random_item('item')
            self.history.append(f"You find a {self.items[-1].name}")
            return print(f"You find a {self.items[-1].name}")
        elif roll == 2:
            self.history.append("A " + self.combat("weak").name + " stands guard. Attack!")
            return print("A " + self.combat("weak").name + " stands guard. Attack!")
        elif roll == 3:
            self.get_random_item("scroll")
            self.history.append(f"A dying mystic gives you a {self.items[-1].name}")
            return print(f"A dying mystic gives you a {self.items[-1].name}") 
        else:
            self.history.append("The entrance is eerily quite and desolate.")
            return print("The entrance is eerily quite and desolate. \nWhat do you do?")

    def explore(self):
        pass

    def use_item(self):
        pass

#This is the game function
def darkfort():
    
    player = Player()

    print(f"\nYour name is Kargunt. You begin with 15 hit points (hp) and {player.sp} silver (sp). You may carry unlimited items. \n"
          f"You own one weapon: A {player.weapons[0].name}, and one {player.items[0].name}.\n"
          f"Torch lit and {player.weapons[0].name} raised, you enter the dungeon.")
    player.history.append(f"Torch lit and {player.weapons[0].name} raised, you enter the dungeon.")
    
    while player.hp > 0:
        player.entrance()
        player.hp = 0
        print("\nYou have perished\n")
        #When someone dies their history is shown
        player.history.append("You have perished")
        print("Kargunt's history:")
        for i in player.history:
            print(f">{i}")
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
