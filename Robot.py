from Weapon import Weapon


class Robot:
    def __init__(self, name, power_level, health):
        self.name = input("What would you like your robot's name to to be?")
        self.power_level = input("What would you like " + self.name + "'s power level to be?")
        self.health = input("What would you like " + self.name + "'s max health to be?")
        self.weapon: Weapon()

    def attack(self, dinosaur):
        if self.power_level > dinosaur.energy:
            damage_taken = dinosaur.health - Weapon.attack.power
            dinosaur.health -= damage_taken
            health_display = str(dinosaur.health)
            print("the dinosaur's health is at" + health_display)
        else:
            print("you did not make a successful attack")
