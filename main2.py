import pygame
import numpy as np

class BrownianBoxSimulation:
    
    LENGTH = 400
    WIDTH = 400
    EDGE_COLOR = (0, 0, 0)
    EDGE_WIDTH = 1
    ORIGIN = (0, 0)
    
    RADIUS_OF_BOT = 5
    START_ANGLE = 90
    
    def __init__(self):
        self.screen = pygame.display.set_mode((self.LENGTH, self.WIDTH))
        self.screen_rect = self.screen.get_rect()
        self.ball_start_position = np.array([self.LENGTH/2, self.WIDTH/2])
        self.ball = pygame.Surface((self.RADIUS_OF_BOT*2, self.RADIUS_OF_BOT*2))
        self.ball.fill((0, 0, 255))
        self.ball_rect = self.ball.get_rect(center=self.ball_start_position)
        self.ra = self.START_ANGLE
        self.pos = self.ball_start_position
        self.vel = np.zeros(2)
        self.find_temps()
        self.clock = pygame.time.Clock()

    def find_temps(self):
        self.vel[0] = np.cos(np.radians(self.ra))
        self.vel[1] = np.sin(np.radians(self.ra))

    def does_it_collide(self):
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
        self.ball_rect.center = tuple(self.pos)

    def run_sim(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, self.EDGE_COLOR, self.screen_rect, self.EDGE_WIDTH)
            
            self.does_it_collide()
            self.update_center()
            self.screen.blit(self.ball, self.ball_rect)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        quit()

box = BrownianBoxSimulation()

box.run_sim()
