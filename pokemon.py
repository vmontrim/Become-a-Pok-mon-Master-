class Pokemon:
    def __init__(self, name, level, pType, koStatus = False):
        self.name = name
        self.level = level
        self.pType = pType
        self.max_health = level * 4 + 100
        self.curr_health = self.max_health
        self.KO = koStatus
    
    # method for taking damage
    def lose_health(self, damage):
        self.curr_health -= damage
        print("{name} has lost {damage} health; current health is {hp} hit points".format(name=self.name, damage=damage, hp=self.curr_health))
    
    #method for gaining HP
    def gain_health(self, healing):
        self.curr_health += healing
        print("{name} has gained {healing} points of health, current health is {health}".format(name=self.name, healing=healing, health=self.curr_health))

    #method for Knocking Out a pokemon
    def knock_out(self):
        self.KO = True

    #method for reviving a pokemon from a KO
    def revive(self):
        self.KO = False

    #Attack a pokemon. Argument is a pokemon object
    def attack(self, other_pokemon):
        damage = 0 
        print("{attacker} ATTACKS {defender}".format(attacker=self.name, defender=other_pokemon.name))
        if self.pType == 'Fire':
            if other_pokemon.pType == 'Water':
                damage = (10 * self.level) / 2
                print("Attack not very affective!")
            
            elif other_pokemon.pType == 'Grass':
                damage = (10 * self.level) * 2
                print("Attack very affectiv!")

            elif other_pokemon.pType == 'Electric':
                damage = 10 * self.level
                print("Attack somewhat affective!")
            
            else:
                damage = 10 * self.level
                print("Attack somewhat affective!")
        
        elif self.pType == 'Water':
            if other_pokemon.pType == 'Fire':
                damage = (10 * self.level) * 2
                print("Attack very affectiv!")

            elif other_pokemon.pType == 'Grass':
                damage = (10 * self.level) / 2
                print("Attack not very affective!")
            
            elif other_pokemon.pType == 'Electric':
                damage = 10 * self.level
                print("Attack somewhat affective!")
            
            else:
                damage = 10 * self.level
                print("Attack somewhat affective!")
        
        elif self.pType == 'Grass':
            if other_pokemon.pType == 'Fire':
                damage = (10 * self.level) / 2
                print("Attack not very affective!")

            elif other_pokemon.pType == 'Water':
                damage = (10 * self.level) * 2
                print("Attack very affectiv!")
            
            elif other_pokemon.pType == 'Electric':
                damage = 10 * self.level
                print("Attack somewhat affective!")
            
            else:
                damage = 10 * self.level
                print("Attack somewhat affective!")
        
        elif self.pType == 'Electric':
            if other_pokemon.pType == 'Fire':
                damage = (10 * self.level)
                print("Attack somewhat affective!")
            
            elif other_pokemon.pType == 'Grass':
                damage = (10 * self.level) / 2
                print("Attack not very affective!")
            
            elif other_pokemon.pType == 'Water':
                damage = 10 * self.level * 2
                print("Attack very affectiv!")
            
            else:
                damage = 10 * self.level
                print("Attack somewhat affective!")
        
        else:
            print("Error: PokemonType ERROR")
        
        other_pokemon.lose_health(damage)

# Defining specific pokemon subclasses
class Pikachu(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Pikachu", level, "Electric")

class Charmander(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Charmander", level, "Fire")

class Squirtel(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Squirtel", level, "Water")

class Bulbasaur(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Bulbasaur", level, "Grass")

#Trainer Class Definition
class Trainer:
    def __init__(self, poke_list, num_potions, name ):
        self.name = name
        self.poke_list = poke_list
        self.potions = num_potions
        self.current_poke = 0
    
    def __repr__(self):
        # Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.poke_list:
            print(pokemon.name)
        return "The current active pokemon is {name}".format(name = self.poke_list[self.current_poke].name)
    # use a potion on current pokemon
    def use_potion(self):
        print("{you} use potion on {poke}".format(you=self.name, poke=self.poke_list[self.current_poke].name))
        self.poke_list[self.current_poke].gain_health(10)
        self.potions -= 1
    
    def attack_trainer(self, target):
        #set up pokemon that are involved in the fight
        atk_poke = self.poke_list[self.current_poke]
        def_poke = target.poke_list[target.current_poke]
        #notify player fight is happening
        print("{self} attacks {targ} with {poke}".format(self=self.name, targ=target.name, poke=atk_poke.name))
        #pokemon fight
        atk_poke.attack(def_poke)
    
    #Switch current pokemon
    def switch_poke(self):
        self.current_poke += 1
        if self.poke_list[self.current_poke].KO:
            self.current_poke += 1
        print("{trainer} switched to {name}".format(trainer=self.name, name=self.poke_list[self.current_poke].name))





pika = Pikachu(2)
char = Charmander(2)
squirt = Squirtel(2)
bulba = Bulbasaur(5)
mander = Charmander(6)



trainer1 = Trainer([pika, char, squirt], 3, "Vito")
trainer2 = Trainer([bulba, mander],5, "Blekas")

trainer1.attack_trainer(trainer2)
trainer2.attack_trainer(trainer1)

trainer1.use_potion()
trainer2.switch_poke()

print(trainer1)
print(trainer2)
