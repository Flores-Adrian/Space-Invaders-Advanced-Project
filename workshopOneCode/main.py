#check if pygame is downloaded correctly
import pygame
import sys

#initialize pygame
pygame.init()

#create variables for length of display screen
SCREEN_WIDTH = 750
SCREEN_LENGTH = 700

#create the display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

#give display screen a title
pygame.display.set_caption("Space Invaders")

#create variable for fps
clock = pygame.time.Clock()

grey = (29, 29, 27)

# create game loop (keeps running until game is closed)
while True:

    # loop through list of events that it recognized
    # check if the game has quit or not
    # .get() gets all the events that pygame recognizes and puts them all in list
    # use for loop to loop through the list to check if any event is a QUIT EVENT
    # QUIT EVENT (is when the close button is clicked)
    for event in pygame.event.get():
        # create if loop
        if event.type == pygame.QUIT:
            # break out
            pygame.quit()
            # close program
            sys.exit()

    # give space invaders background color
    screen.fill(grey)

    # update display
    # (takes all the changes that we made and updates them)

    pygame.display.update()

    # setting fps to display screen
    # initialize how fast we want the game to run
    # we use the the .tick method to do so which takes a int as an argument
    # ==> the int that is inputted will be used as the amount fps the game will run
    # 60 fps is a safe speed
    clock.tick(60)
