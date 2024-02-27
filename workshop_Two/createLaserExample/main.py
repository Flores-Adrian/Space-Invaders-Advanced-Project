import pygame
import sys
from spaceships import Spaceships
from laser import Laser

# initialize pygame
pygame.init()

# create size of display screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

grey = (128,128,128)

# create spaceship object with sizes
spaceship = Spaceships(SCREEN_WIDTH, SCREEN_HEIGHT)

# create group for spaceship (only holds a single sprite)
spaceship_group = pygame.sprite.GroupSingle()
# add spaceship to group
spaceship_group.add(spaceship)

# create laser object with position as tuple, speed, and screen_height
# laser goes up
laser = Laser((100,100), 6, SCREEN_HEIGHT)
# laser goes down
laser2 = Laser((100, 200), -6, SCREEN_HEIGHT)

# create group to hold all lasers that the spaceship will have
# .Group() can hold multiple sprites since the multiple lasers will be shot
laser_group = pygame.sprite.Group()

# add laser to group
laser_group.add(laser, laser2)

while True:

    for event in pygame.event.get():

        # checking if the game is closed
        if event.type == pygame.QUIT:
            # break out
            pygame.quit()
            # close program
            sys.exit()

    # UPDATE ------------------------
    # update spaceship
    spaceship_group.update()
    # update lasers
    laser_group.update()

    # give space invaders display screen color
    screen.fill(grey)
    # DRAW ------------------------------
    # draw sprite within spaceship_group onto screen
    spaceship_group.draw(screen)
    # draw lasers group
    laser_group.draw(screen)



    # update display for space invaders
    pygame.display.update()

    clock.tick(60)
