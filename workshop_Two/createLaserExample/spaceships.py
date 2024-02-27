import pygame
from laser import Laser

# create class (which will be child of Sprite class)
class Spaceships(pygame.sprite.Sprite):

    # create init to initializes spaceship object
    def __init__(self, screen_width, screen_height):
        # inherits all attributes and methods of sprite class
        # calls constructor of parent sprite class
        super().__init__()

        # attributes for screen size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # load image file of file directory for visual appearance of ship
        self.image = pygame.image.load("Images/spaceship.png")

        # create default rectangular region (rect object) for position of spaceship
        # takes argument for the position of the spaceship (middle bottom of screen)
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2,self.screen_height))

        # speed attribute to control speed of object movement
        self.speed = 6

    # create method for user input
    def get_user_input(self):
        # get list of all keys that are pressed
        keys = pygame.key.get_pressed()

        # check if Left or Right arrow keys are pressed
        if keys[pygame.K_RIGHT]:
            # change x-axis value of rect to make it move right
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            # change x-axis value of rect to make it move left
            self.rect.x -= self.speed

    # create update method to be called for every frame and update each frame
    def update(self):
        # update user input method
        self.get_user_input()
        # udpate constrain movement method
        self.constrain_movement()

    # create method to constrain movement of spaceship when it goes left to right
    def constrain_movement(self):

        # checks if the spaceship moved passed the boundaries (too far to the right)
        if self.rect.right > self.screen_width:
            # reposition inside window
            self.rect.right = self.screen_width
        # checks if the spaceship is passed the boundaries on the left side
        if self.rect.left < 0:
            # reposition inside window
            self.rect.left = 0

