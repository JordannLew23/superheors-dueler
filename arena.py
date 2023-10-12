from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, team_one, team_two):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("what is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt for user Weapon information.
        return Weapon with values from user input.
        '''
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Promt user Armor information.
        return Armor with values from user input.
        '''
        name = input("What is the armor name? ")
        max_block = input("What is max block of the armor? ")

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information.
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3]")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
            elif add_item == "4":
                break
            else:
                print("Invalid chocie. Please choose from 1 to 4.")

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one'''
        team_name = input("Enter team one name: ")
        team_one = Team(team_name)

        numOfTeamMembers = int(input("How many heroes would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input("Enter team two name: ")
        team_two = Team(team_name)

        numOfTeamMembers = int(input("How many heroes would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + "statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + "statistics: ")
        self.team_two.stats()
        print("\n")

        team_kill_one = 0
        team_deaths_one = 0
        for hero in self.team_one.heroes:
            team_kills_one += hero.kills
            team_deaths_one += hero.deaths
        if team_deaths_one == 0:
            team_deaths_one = 1
        print(self.team_one.name + "average K/D was: " + str(team_kills_one/team_deaths_one))

        team_kills_two = 0
        team_deaths_two = 0
        for hero in self.team_two.heroes:
            team_kills_two += hero.kills
            team_deaths_two += hero.deaths
        if team_deaths_two == 0:
            team_deaths_two = 1
        print(self.team_two.name + "average K/D was: " + str(team_kills_two/team_deaths_two))

        print("Surviving heroes from" + self.team_one.name + ":")
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(hero.name)

        print("Surviving heroes from" +self.team_two.name + ":")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(hero.name)

        if len(self.team_one.get_living_heroes()) > len(self.team_two.get_living_heroes()):
            print(self.team_one.name + "is the winning team!")
        elif len(self.team_one.get_living_heroes()) < len(self.team_two.get_living_heroes()):
            print(self.team_two.name + "is the winning team!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    team_one = Team("Team One")
    team_two = Team ("Team Two")
    arena = Arena(team_one, team_two)

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()



    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
