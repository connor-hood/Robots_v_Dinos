from Herd import Herd
from Fleet import Fleet


class Field_of_battle:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def battle(self):
        print(self.fleet.fleet_of_robots[0].__dict__)
        print(self.fleet.fleet_of_robots[1].__dict__)
        print(self.fleet.fleet_of_robots[2].__dict__)
        print(self.herd.herd_of_dinosaurs[0].__dict__)
        print(self.herd.herd_of_dinosaurs[1].__dict__)
        print(self.herd.herd_of_dinosaurs[2].__dict__)

    def display_welcome(self):
        print("Welcome to Dinosaurs Vs. Robots!!!")
    
    def run_game(self):
        self.display_welcome()

    def dino_turn(self, dinosaur):
        self.herd.herd_of_dinosaurs[0].attack(self.fleet.fleet_of_robots[1])


def robo_turn(self, robot):
    self.fleet.fleet_of_robots[0].attack(self.herd.herd_of_dinosaurs[0])


def show_dino_opponent_options(self):
    pass


def show_robo_opponent_options(self):
    pass


def display_winners(self):
    pass
