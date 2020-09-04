import random as rd
class Pokemon:
  def __init__(self, name, level, types, health, ko = False):
    self.name = name
    self.level = level 
    self.types = types
    self.health = health
    self.max_health = level
    self.ko = ko

  def __repr__(self):
      return "Pokemon info, name: {}, level: {}, type: {}, health: {}".format(self.name, self.level, self.types, self.health)

  def lose_health(self, damage):
      if damage >= self.health:
        print(f"Your pokemon {self.name} is knocked out")
      else:
        self.health -= damage 
        print(f"{self.name} lost {damage} health and remaining health {self.health}") 
      
  def gain_health(self, gain):
      self.health += gain
      print(f"{self.name} gain {gain} health")
      print(f"{self.name} now has {self.health} health")

 
  def attack(self, other_pokemon):
      dmg = 0
      for a in self.types:
          for b in other_pokemon.types:
              if (a == 'fire' and b == 'grass') or (a == 'grass' and b == 'water') or (a == 'water' and b == 'fire'):
                  dmg += 10
              elif (a == 'grass' and b == 'fire') or (a == 'fire' and b == 'water') or (a == 'water' and b == 'grass'):
                  dmg -= 10
      damage = self.level * dmg + (rd.randint(0, 5) * 10)
      other_pokemon.health = max(other_pokemon.health - damage, 0) 
      print("{} hits {} and made {} damage!".format(self.name, other_pokemon.name, round(damage, 0)))             
      if other_pokemon.health == 0:
          other_pokemon.ko = True
          print(f'{other_pokemon.name} is ko')
  
       
class Trainer:
   def __init__(self, name, pokemons, potions, current_pokemon):
       self.name = name
       self.pokemons = pokemons
       self.potions = potions
       self.current_pokemon = 0

   def potion(self):
       if self.potions > 0:
           self.pokemons[self.current_pokemon].gain_health(10)
           self.potions -= 10
           print(f'{self.current_pokemon} gain + 10 health')
       else:
           print('no potions lefft')
  
   def attack_trainer(self, other_trainer):
        self.pokemons[self.current_pokemon]
      




trainer1 = Trainer('belekas',['ghr', 'dg', 'dj'], 100, 'dj')
trainer2 = Trainer('bs',['ghr', 'dg'], 100, 'dg')


print(Pokemon('pika', 1, 'fire', 100))

pika = Pokemon('pika', 1, 'fire', 100)
eevee = Pokemon('eevee', 1, 'grass',100)


pika.lose_health(70)
pika.gain_health(50)

pika.attack(eevee)


trainer1.attack_trainer(trainer2)

