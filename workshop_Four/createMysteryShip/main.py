import pygame
import sys
import random
from game import Game

# initialize pygame
pygame.init()

# create size of display screen
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

grey = (128,128,128)

# create event for mystery ship
mystery_ship = pygame.USEREVENT + 1
# set timer with time interval of 4000-8000 miliseconds
pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))


while True:

    for event in pygame.event.get():

        # checking if the game is closed
        if event.type == pygame.QUIT:
            # break out
            pygame.quit()
            # close program
            sys.exit()

        if event.type == mystery_ship:
            # create random spaceship
            game.create_mystery_ship()
            # set interval of timer
            pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))



    # UPDATE ------------------------
    # update spaceship
    game.spaceship_group.update()

  
    game.mystery_ship_group.update()



    # give space invaders display screen color
    screen.fill(grey)
    # DRAW ------------------------------
    # draw sprite within spaceship_group onto screen
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    game.aliens_group.draw(screen)

  
    game.mystery_ship_group.draw(screen)



    # update display for space invaders
    pygame.display.update()

    clock.tick(60)
