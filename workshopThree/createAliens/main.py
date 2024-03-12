ort pygame
import sys
from game import Game

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


clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

# keeps running until game is closed
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER:
            game.alien_shoot_laser()

    #updating
    game.spaceship_group.update()
    game.move_aliens()
    # game.alien_shoot_laser()
    game.alien_lasers_group.update()

    # change background color
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)



    pygame.display.update()

    clock.tick(60)



