class Dinosaur:
    def __init__(self, type, energy, attack_power, health):
        self.type = type
        self.energy = input('What would you like your dino defense power to be?')
        self.attack_power = input('What would you like your dino attack power to be?')
        self.health = input('What would you like your dino max health to be?')

    def attack(self, robot):
        if self.attack_power > robot.power_level:
            damage_taken = robot.health - self.attack_power
            robot.health -= damage_taken
            health_display = str(robot.health)
            print("the robot's health is at" + health_display)
        else:
            print("you did not make a successful attack")
