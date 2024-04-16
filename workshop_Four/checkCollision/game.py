import pygame

from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from ailen import Alien

# import mystery ship
from ailen import MysteryShip




class Game:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()

        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        # create mystery ship attribute for group
        self.mystery_ship_group = pygame.sprite.GroupSingle()


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

    def create_mystery_ship(self):

        self.mystery_ship_group.add(MysteryShip(self.screen_width))

   def check_for_collisions(self):

        # check if spaceship hits anything like alien, mystery ship, or obstacles
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True):
                    laser_sprite.kill()
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    laser_sprite.kill()
            for obstacle in self.obstacles:
                if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                    laser_sprite.kill()

        # check if alien laser hits the spaceship or obstacle
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()
                    print("Spaceship Hit")

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        # checks alien group
        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    print("Spaceship hit")
