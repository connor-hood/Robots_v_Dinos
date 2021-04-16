class Dinosaur:
    def __init__(self, type, energy, attack_power, health):
        self.type = type
        self.energy = energy
        self.attack_power = attack_power
        self.health = health

    def attack(self, robot):
        if self.attack_power > robot.power_level:
            damage_taken = robot.health - self.attack_power
            robot.health -= damage_taken
            health_display = str(robot.health)
            print("the robot's health is at" + health_display)
        else:
            print("you did not make a successful attack")
