# Jordan Leung
#5/3/2019
# random class

from random import choice

class RandomWalk():
    """A Class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired amount of steps
        while len(self.x_values) < self.num_points:
            #decide which direction to go and distance (x axis)
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,5])
            x_step = x_direction * x_distance
            # decide which direction and distance in the y axis
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4,5])
            y_step = y_direction * y_distance

            #reject mpves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x & y values
            # if x has only one point, x[-1] will also access x[0], or the first point
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # adds the value to the list
            self.x_values.append(next_x)
            self.y_values.append(next_y)
