import random

class Team:
    def __init__(self, name):
        '''Initalize your team with its team name and an empty list of heros'''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heros list. If hero isn't found return 0.'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heros(self):
        '''Print out all heros to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes'''
        self.heroes.append(hero)

    def revive_heros(self, health=100):
        '''Reset all heros health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''Battle each team against each other.'''
        living_heros = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heros.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heros) >0 and len(living_opponents) >0:
            hero = random.choice(living_heros)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            if hero.is_alive():
                living_opponents.remove(opponent)
            else:
                living_heros.remove(hero)
