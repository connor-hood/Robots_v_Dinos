class Dinosaur:
    def __init__(self, type, energy, attack_power, health):
        self.type = type
        self.energy = energy
        self.attack_power = attack_power
        self.health = health

    def attack(self, robot):
        if Dinosaur.attack_power > robot.power_level:
            damage_taken = robot.health - Dinosaur.attack_power
            robot.health -= damage_taken
        else:
            print("you did not make a successful attack")