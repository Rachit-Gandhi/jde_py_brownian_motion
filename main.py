
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class BrownianBoxSimulation:

    LENGTH = 800
    WIDTH = 300
    EDGE_COLOR = 'red'
    EDGE_WIDTH = 1
    ORIGIN = (0, 0)

    RADIUS_OF_BOT = 5
    START_ANGLE = 90 #so that the ball starts as described in problem initial steps

    def __init__(self): #initialise
        self.box = plt.Rectangle(self.ORIGIN, self.LENGTH, self.WIDTH, edgecolor=self.EDGE_COLOR, facecolor='none', linewidth=self.EDGE_WIDTH)
        self.fig, self._ = plt.subplots()
        self.ax = plt.gca()
        self.ax.add_patch(self.box)
        self.ball_start_position = (self.LENGTH/2, self.WIDTH/2)
        self.ball = plt.Circle(self.ball_start_position,radius=self.RADIUS_OF_BOT,ec="black",fc="blue")
        self.ball.center = self.ball_start_position
        self.ra = self.START_ANGLE
        self.x = self.ball_start_position[0]
        self.y = self.ball_start_position[1]
        self.dx = 0
        self.dy = 0

    def find_temps(self): #displacement after the collision
        self.dx, self.dy = np.cos(np.radians(self.ra)), np.sin(np.radians(self.ra))

    def does_it_collide(self, x, y): #check collision
        if x + self.dx <= self.RADIUS_OF_BOT or x + self.dx >=self.LENGTH - self.RADIUS_OF_BOT \
            or y + self.dy <= self.RADIUS_OF_BOT or y + self.dy >= self.WIDTH - self.RADIUS_OF_BOT:
            
            print("collision",x + self.dx, y + self.dy)
            self.ra = np.random.randint(0,360)
            self.find_temps()
            self.does_it_collide(x, y)

    def update_center(self, x, y): #update rebound angle after collision
        self.x = x + self.dx
        self.y = y + self.dy
        self.ball.center = (self.x, self.y)

    def init_sim(self):
        self.ax.add_patch(self.ball)
        return self.ball,

    def animate(self,i):
        x, y = self.ball.center

        self.find_temps()
        self.does_it_collide(x,y)
        self.update_center(x,y)

        return self.ball,

    def run_sim(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               init_func=self.init_sim, 
                               frames=5000, 
                               interval=10,
                               blit=True,repeat=False)
        plt.axis('scaled')
        plt.show()

box = brownianbox.BrownianBox()

box.run_sim()
