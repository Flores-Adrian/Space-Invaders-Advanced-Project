import pygame

# create class (sprite class)
class Laser(pygame.sprite.Sprite):

    # create init method to initialize laser object
    def __init__(self, position, speed, screen_height):
        super().__init__()
        
        # create rectangle to represent laser
        # takes tuple to create the size of shape in pixels (width, height)
        self.image = pygame.Surface((4,15))
        
        # give the laser color (yellow)
        self.image.fill((243, 216, 63))
        
        # create rect for laser and position the laser
        self.rect = self.image.get_rect(center = position)
        
        # create speed attribute to control laser speed
        self.speed = speed
        
        # create height attribute to get the window size
        self.screen_height = screen_height

    # create update method
    def update(self):
        
        # reposition rect in the y direction (negative = up)
        self.rect.y -= self.speed

        # check if y-coordinate of the rect we created for the laser is
        # outside of the game window
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            
            print("Killed")
            
            # removes sprite from all groups it belongs too
            # makes it vanish and not keep running continously
            self.kill()

