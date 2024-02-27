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

        # (FIRST) create attribute for laser group
        self.lasers_group = pygame.sprite.Group()

        # (FIRST FIRST) laser ready attribute to know when laser is ready to be fired
        self.laser_ready = True

        # laser time attribute to know how much time has passed since the last shot was fired
        self.laser_time = 0

        # laser delay attribute to control the delay between shots in milliseconds
        self.laser_delay = 300

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

        # (SECOND) checks if space bar is pressed
        # and if laser is ready to be shot
        if keys[pygame.K_SPACE] and self.laser_ready:\

            # (FOURTH FOURTH)
            # when laser is created we have to set laser_ready as false
            # indicating we have to recharge the laser again
            self.laser_ready = False

            # create laser object that takes 3 arguments
            # (position, speed, screen_height)
            # the position is in the middle center of the spaceship for laser
            laser = Laser(self.rect.center, 5, self.screen_height)

            # add laser to group
            self.lasers_group.add(laser)

            # (FIFTH FIFTH)
            # make laser_time attribute mark when laser was last fired
            self.laser_time = pygame.time.get_ticks()

    # create update method to be called for every frame and update each frame
    def update(self):
        # update user input method
        self.get_user_input()
        # update constrain movement method
        self.constrain_movement()

        # (THIRD) update laser group
        self.lasers_group.update()

        # (THIRD THIRD)
        # update recharge laser
        self.recharge_laser()

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

    # (SECOND SECOND)
    # create method to control fire rate of lasers
    def recharge_laser(self):
        # checks if the laser is not ready to shoot
        # if it isn't then we have to recharge the laser
        if not self.laser_ready:

            # get current time
            current_time = pygame.time.get_ticks()

            # check if current time MINUS the time the laser was last fired is
            # greater than the delay time
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
