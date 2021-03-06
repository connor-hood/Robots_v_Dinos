from Dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.herd_of_dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Bite', 20, 10, 30)
        dino_two = Dinosaur('Claw', 15, 5, 20)
        dino_three = Dinosaur('Tail Whip', 25, 15, 25)
        self.herd_of_dinosaurs.append(dino_one)
        self.herd_of_dinosaurs.append(dino_two)
        self.herd_of_dinosaurs.append(dino_three)
