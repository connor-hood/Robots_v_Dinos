from Robot import Robot


class Fleet:
    def __init__(self):
        self.fleet_of_robots = []

    def create_fleet(self):
        self.fleet_of_robots = append(robot_one)
        self.fleet_of_robots = append(robot_two)
        self.fleet_of_robots = append(robot_three)


if __name__ == '__main__':
    robot_one = Robot()
    robot_one.name = 'Sam'
    robot_one.power_level = 20
    robot_one.health = 25
    robot_one.weapon = Weapon()

    robot_two = Robot()
    robot_two.name = 'Robert'
    robot_two.power_level = 25
    robot_two.health = 30
    robot_two.weapon = Weapon()

    robot_three = Robot()
    robot_three.name = 'Ted'
    robot_three.power_level = 10
    robot_three.health = 15
    robot_three.weapon = Weapon()
