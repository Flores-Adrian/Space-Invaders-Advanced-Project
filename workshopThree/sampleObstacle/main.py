import pygame
import sys
# import the spaceship and laser class
from spaceship import Spaceship
from obstacle import Obstacle
from laser import Laser

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

# create color for game
# more info on https://pygame.readthedocs.io/en/latest/1_intro/intro.html
GREY = (29, 29, 27)

# create display surface ==> needed to make an empty canvas where we can place game
# set_mode takes tuple as an argument ==> (width, height)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# give title to screen
pygame.display.set_caption("Python Space Invaders")

# create clock object
# needed to control frame rate of the game (how fast the game will run)
clock = pygame.time.Clock()

# create a spaceship project including the width and height being added
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)

spaceship_group = pygame.sprite.GroupSingle()


# now we have to add our chosen object to the group
spaceship_group.add(spaceship)



# create obstacle
obstacle = Obstacle()


# keeps running until game is closed
while True:

    # .get() gets all the events that pygame recognizes and puts them all in list
    # use for loop to loop through the list to check if any event is a QUIT EVENT
    # QUIT EVENT (is when the close button is clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # close program with command (make sure sys (system) is imported)
            sys.exit()
    # calls the update object
    spaceship_group.update()



    # change background color
    screen.fill(GREY)

    spaceship_group.draw(screen)



    spaceship_group.sprite.lasers_group.draw(screen)

    # draw te obstacle_group we made in obstacle class
    obstacle.blocks_group.draw(screen)


    pygame.display.update()


    clock.tick(60)
