import pygame
import random

class Alien(pygame.sprite.Sprite):

    def __init__(self, type, x,y):
        super().__init__()

        self.type = type

        #path file
        path = f"Images/alien_{type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x,y))

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.image = pygame.image.load("Images/mystery.png")

        # helps with starting point (either left or right side of screen)
        x = random.choice([0, self.screen_width - self.image.get_width()])

        if x == 0:
            self.speed = 3
        else:
            self.speed = -3

        # 40 pixels down and random x-positionn spawn
        self.rect = self.image.get_rect(topleft = (x, 40))


    def update(self):
        self.rect.x += self.speed

        # deletes spaceship when outside of game screen
        if self.rect.right > self.screen_width:
            self.kill()
        elif self.rect.left < 0:
            self.kill()
