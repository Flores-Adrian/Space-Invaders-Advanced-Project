
import pygame
import sys
import random
from game import Game

# initialize pygame
pygame.init()

# create size of display screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

grey = (128, 128, 128)
yellow = (243, 216, 63)

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL 1", False, yellow)
game_over_surface = font.render("GAME OVER", False, yellow)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

# create event for mystery ship
mystery_ship = pygame.USEREVENT + 1
# set timer with time interval of 4000-8000 milliseconds
pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))


while True:

    for event in pygame.event.get():
        # checking if the game is closed
        if event.type == pygame.QUIT:
            # break out
            pygame.quit()
            # close program
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
        if event.type == mystery_ship and game.run:
            # create random spaceship
            game.create_mystery_ship()
            # set interval of timer
            pygame.time.set_timer(mystery_ship, random.randint(4000, 8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    # UPDATE ------------------------
    # update spaceship
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    # give space invaders display screen color
    screen.fill(grey)

    pygame.draw.rect(screen, yellow, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, yellow, (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    # DRAW ------------------------------
    # draw sprite within spaceship_group onto screen
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)


    # update display for space invaders
    pygame.display.update()

    clock.tick(60)
