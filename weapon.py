import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        """ This method returns a random value betweeen one half ot hte full attack power of the weapon. """
        half_damage = self.max_damage // 2

        return random.randint(half_damage, self.max_damage)
