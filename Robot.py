from Weapon import Weapon


class Robot:
    def __init__(self, name, power_level, health):
        self.name = name
        self.power_level = power_level
        self.health = health
        self.weapon: Weapon()

    def attack(self, dinosaur):
        if self.power_level > dinosaur.energy:
            damage_taken = dinosaur.health - Weapon.attack.power
            dinosaur.health -= damage_taken
        else:
            print("you did not make a successful attack")
