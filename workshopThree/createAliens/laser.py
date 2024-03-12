import pygame

class Laser(pygame.sprite.Sprite):
    # create constructor
    def __init__(self, position, speed, screen_height):
        super().__init__()
        # create a basic rectangle to use as laser
        # this tuple size is for the rectangle (width, height)
        self.image = pygame.Surface((4, 15))

        # the "laser" is created but empty so we have to fill in the color
        # this tuple is for the color YELLOW
        self.image.fill((243, 216, 63))

        # define the rect for the laser and position the laser which we will center
        # centering the laser is important and do so by giving specific cords
        # the center variable determines where the "starting poing" is going to be
        self.rect = self.image.get_rect(center = position)

        # create speed attribute
        self.speed = speed

        # create screen_height attribute to be able to determine if the laser
        # is outside of the screen window
        self.screen_height = screen_height

    def update(self):
        # moving the lasers requires the reposition of its rect since it could only
        # move up and down (so we just have to add or remove pixels from y-axis)

        # create class argument for the amount of pixels that will be moved
        # IF WE WANT TO MOVE THE LASER UP THEN WE WILL GIVE A POSITIVE VALUE FOR SPEED
        # IF WE WANT TO MOVE THE LASER DOWN THEN WE WILL GIVE A NEGATIVE VALUE FOR SPEED
        self.rect.y -= self.speed

        # Create if loop to check if the laser(the rect) is outside the game window
        # We add 15 pixels since the rectangle we made is 15 pixels long and want
        # to make sure it is fully out of the game window before removing it
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            # When you call the kill method on a sprite object, it removes it the sprite
            # from all the groups it is
            self.kill()
