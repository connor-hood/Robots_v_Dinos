from Robot import Robot


class Fleet:

    def __init__(self):
        self.fleet_of_robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot('Tim', 5, 25)
        robot_two = Robot('Phil', 25, 60)
        robot_three = Robot('Rodney', 15, 40)
        self.fleet_of_robots.append(robot_one)
        self.fleet_of_robots.append(robot_two)
        self.fleet_of_robots.append(robot_three)
