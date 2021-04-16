class Dinosaur:
    def __init__(self):
        self.type = ''
        self.energy = 0
        self.attack_power = 0
        self.health = 0

    def __init__(self, type, attack_power):
        self.type = type
        self.attack_power = attack_power

    def attack(self, robot):
        if Dinosaur.attack_power > robot.power_level:
            damage_taken = robot.health - Dinosaur.attack_power
            robot.health -= damage_taken
        else:
            print("you did not make a successful attack")