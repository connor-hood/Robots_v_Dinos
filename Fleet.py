from Robot import Robot


class Fleet:
    def __init__(self):
        self.fleet_of_robots = []
        self.create_fleet()

    def create_fleet(self):
        #create 3 robot objects, add to list
        self.fleet_of_robots.append(robot_one)
        self.fleet_of_robots.append(robot_two)
        self.fleet_of_robots.append(robot_three)


if __name__ == '__main__':
    robot_one = Robot(Tim, 5, 25)
    robot_two = Robot(Phill, 25, 60)
    robot_three = Robot(Rodney, 15, 40)