from Weapon import Weapon


class Robot:
    def __init__(self):
        self.name: ''
        self.power_level: 0
        self.health: 0
        self.weapon: Weapon()

    def __init__(self, name):
        self.name = name

    def attack(self, dinosaur):
        if Robot.power_level > dinosaur.energy:
            damage_taken = dinosaur.health - Weapon.attack.power
            dinosaur.health -= damage_taken
        else:
            print("you did not make a successful attack")
