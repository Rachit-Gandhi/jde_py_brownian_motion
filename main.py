import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class BrownianBoxSimulation:

    LENGTH = 400
    WIDTH = 400
    EDGE_COLOR = 'black'
    EDGE_WIDTH = 1
    ORIGIN = (0, 0)

    RADIUS_OF_BOT = 5
    START_ANGLE = 90 #so that the ball starts as described in problem initial steps

    def __init__(self):
        self.box = plt.Rectangle(self.ORIGIN, self.LENGTH, self.WIDTH, edgecolor=self.EDGE_COLOR, facecolor='none', linewidth=self.EDGE_WIDTH)
        self.fig, self._ = plt.subplots()
        self.ax = plt.gca()
        self.ax.add_patch(self.box)
        self.ball_start_position = (self.LENGTH/2, self.WIDTH/2)
        self.ball = plt.Circle(self.ball_start_position,radius=self.RADIUS_OF_BOT,ec="black",fc="blue")
        self.ball.center = self.ball_start_position
        self.ra = self.START_ANGLE
        self.pos = np.array(self.ball_start_position)
        self.vel = np.zeros(2)
        self.find_temps()

    def find_temps(self):
        self.vel[0] = np.cos(np.radians(self.ra))
        self.vel[1] = np.sin(np.radians(self.ra))

    def does_it_collide(self):
        x, y = self.pos
        next_pos = self.pos + self.vel
        collides = np.array([next_pos[0] <= self.RADIUS_OF_BOT, 
                             next_pos[0] >= self.LENGTH - self.RADIUS_OF_BOT,
                             next_pos[1] <= self.RADIUS_OF_BOT,
                             next_pos[1] >= self.WIDTH - self.RADIUS_OF_BOT])
        if np.any(collides):
            self.ra = np.random.randint(0, 360)
            self.find_temps()
            self.does_it_collide()
        else:
            self.pos = next_pos

    def update_center(self):
        self.ball.center = tuple(self.pos)

    def init_sim(self):
        self.ax.add_patch(self.ball)
        return self.ball,

    def animate(self, i):
        self.does_it_collide()
        self.update_center()
        return self.ball,

    def run_sim(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               init_func=self.init_sim, 
                               frames=5000, 
                               interval=10,
                               blit=True,
                               repeat=False)
        plt.axis('scaled')
        plt.show()

box = BrownianBoxSimulation()

box.run_sim()
