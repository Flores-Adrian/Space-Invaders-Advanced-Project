import pygame
from laser import Laser

# create a separate class for spaceship
# will use sprite class:
# ==> You can think of it like a container which will hold everything for your character
# ==> how it can look, position, what it does, and can check collision handling
# ALSO you can put similar multiple containers all into one single container
# ==> which will contain all the attribute of the containers

# create class while using the sprite method (will be outside of sprite class)
class Spaceship(pygame.sprite.Sprite):

    # create constructor for class (intiallize the Spaceship object)
    def __init__(self, screen_width, screen_height):
        # allow the class to inherit all attributes and method of the sprite class
        # initializes the object by calling the constructor of the parent class(sprite)
        super().__init__()

        #initalize the variables
        self.screen_width = screen_width
        self.screen_height = screen_height

        # INITIALIZE 2 images inherited from the sprite class
        # self is used to represent the instance of the class which allows you
        # ==> to have access to the methods of the class

        # .load function loads the image and assign it to self.image
        self.image = pygame.image.load("Images/spaceship.png")

        # now we create a rectangular region (Rect object) to define its position and size
        # .get_rect gets a default rectangle for the selected image
        # ==> the rectangle will be the same size as the image
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height))
        # ^WE WANT TO SPECIFY HOW WE WANT TO POSITION THE SPACESHIP ON SCREEN
        # ==>midbottom indicates that we want to position of the rectangle to be
        # aligned with the image

        # create variable for amount of pixels moved to the right or left
        self.speed = 6

        # create new group that will contain all lasers
        self.lasers_group = pygame.sprite.Group()

        # create attribute to indicate the laser is ready to fire
        self.laser_ready = True

        # keeps track how much time has passed since the last shot
        self.laser_time = 0

        # helps control the time delay between shots
        self.laser_delay = 300

    # CREATE NEW METHOD TO GET PLAYER INPUT
    def get_user_input(self):
        # gives list of all keys that are being pressed
        keys = pygame.key.get_pressed()


        # if loop checks if right key is pressed
        if keys[pygame.K_RIGHT]:
            # move spaceship to the right ==> to do so we are moving the rect to the right
            # by a certain amount of pixels
            # to do so we have to change the value of its x-value
            self.rect.x += self.speed

        # checks if the left key is pressed
        if keys[pygame.K_LEFT]:
            # it is subtracting now since we want to go the left of the grid
            self.rect.x -= self.speed

        # checks if the space bar is pressed
        # and if the laser is ready to shoot
        if keys[pygame.K_SPACE] and self.laser_ready:
            # when we create a new laser we have to set laser_ready to false
            self.laser_ready = False
            # create laser object which will take 3 arguments
            # (position, speed, self.screen_height)
            laser = Laser(self.rect.center, 5, self.screen_height)

            # now that the laser beam is created, we have to add it to the group we made
            self.lasers_group.add(laser)

            # marks when a laser was fired
            self.laser_time = pygame.time.get_ticks()

    # create method that updates every fame for each specific use
    def update(self):
        self.get_user_input()
        self.constrain_movement()
        # will call the update method for all the objects in the lasers_group
        self.lasers_group.update()
        # update the laser
        self.recharge_laser()

    # this method helps limit the movement of the spaceship so it cant move outside the window
    def constrain_movement(self):
        # constraint movement to the right
        # checks if the spaceship has moved past the boundaries of the window
        # ==> then it will only be able to stay inside the window width
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        # constraint movement to the left
        if self.rect.left < 0:
            # the same happens here but for the left side of the scren
            self.rect.left = 0

# controls firing rate of the lasers
    def recharge_laser(self):
        # if the laser is not ready then we need to recharge the laser
        if not self.laser_ready:
            # get the current time
            # .get_ticks() gets the current time in miliseconds
            current_time = pygame.time.get_ticks()

            # We need to check if the time now minus the time when laser was fired
            # is greater than the delay time
            if current_time - self.laser_time >= self.laser_delay:
                # allow the laser to be shot again
                self.laser_ready = True
