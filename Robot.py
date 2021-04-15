class Robot:
    def __init__(self):
        self.name: ''
        self.power_level: 0
        self.health: 0
        self.weapon: Weapon()

    def __int__(self,name):
        self.name = name

    def attack(self, dinosaur):

