from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
           return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
           Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
           return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defense = self.defend()
        damage -= defense
        self.current_health -= damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities or not opponent.abilities:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive():
            print(f"{self.name} won!")
            self.add_kill()
            opponent.add_death()

        else:
            print(f"{opponent.name} won!")
            self.add_death()
            opponent.add_kill()


    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths

    def stats(self):
        '''Print team statistics'''
        for hero in self.heros:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
