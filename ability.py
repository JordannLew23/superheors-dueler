import random
random.randint(2,7)

class Ability:
    def __init__(self, name, max_damage):
        '''Initalize the values passed into this method as instance variables.'''

        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage'''
        random_value= random.randint(0,self.max_damage)
        return random_value







if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())
