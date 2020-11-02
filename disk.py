RED_DISK = (255, 0, 0)
YELLOW_DISK = (255, 255, 0)
ZERO = 0
TWO = 2
TEN = 10
RADIUS = 100


class Disk:

    def __init__(self, color):
        self.x = ZERO
        self.y = ZERO
        # define the disk drop speed
        self.y_vel = TEN
        self.radius = RADIUS
        # get the ball_count
        # determine the color
        self.color = color

    def draw_me(self, x_coordinate, y_coordinate):
        # check the ball_count to determine which color to draw
        if self.color == "R":
            self.draw_red(x_coordinate, y_coordinate)
        else:
            self.draw_yellow(x_coordinate, y_coordinate)

    def draw_red(self, x_coordinate, y_coordinate):
        # draw the red disk
        self.x = x_coordinate
        self.y = y_coordinate
        noStroke()
        fill(*RED_DISK)
        circle(self.x, self.y, self.radius)

    def draw_yellow(self, x_coordinate, y_coordinate):
        # draw the yellow disk
        self.x = x_coordinate
        self.y = y_coordinate
        noStroke()
        fill(*YELLOW_DISK)
        circle(self.x, self.y, self.radius)

    def down(self, drop_height):
        # define the changing y coordinate
        # when the disk is dropping
        while self.y <= drop_height:
            self.y = self.y + self.y_vel
            self.draw_me(self.x, self.y)
        # the y coordinate is contant
        # when it reaches to the drop_height
        self.draw_me(self.x, drop_height)
