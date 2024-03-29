import pygame

from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from ailen import Alien
#_______________________________
# import mystery ship
from ailen import MysteryShip
#____________________________



class Game:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()

        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        # ____________________________________________________
        # create mystery ship attribute for group
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        # _______________________________________________________


    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width - (4 * obstacle_width)) / 5
        obstacles = []

        for i in range(4):
            offset_x = ((i + 1) * gap + i * obstacle_width)
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)


        return obstacles

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = column * 55
                y = row * 55

                alien = Alien(1, x, y)
                self.aliens_group.add(alien)

    # __________________________________________________________________
    def create_mystery_ship(self):

        self.mystery_ship_group.add(MysteryShip(self.screen_width))
    # __________________________________________________________________
