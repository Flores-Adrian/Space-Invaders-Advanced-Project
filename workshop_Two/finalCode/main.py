import pygame
import sys
from spaceships import Spaceships


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


    # give space invaders display screen color
    screen.fill(grey)
    # DRAW ------------------------------
    # draw sprite within spaceship_group onto screen
    spaceship_group.draw(screen)
    # (FOURTH) draw laser group
    spaceship_group.sprite.lasers_group.draw(screen)




    # update display for space invaders
    pygame.display.update()

    clock.tick(60)
