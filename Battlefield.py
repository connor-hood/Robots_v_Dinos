from Herd import Herd
from Fleet import Fleet


def display_welcome():
    print("Welcome to Dinosaurs Vs. Robots!!!")


class Field_of_battle:
    def __init__(self):
        hello = 0
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        display_welcome()

    def battle(self):

        pass

    def dino_turn(self, dinosaur):
        self.herd.herd_of_dinosaurs[0].attack(self.fleet.fleet_of_robots[1])
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
