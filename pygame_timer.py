import pygame, sys
from pygame.locals import *

if len(sys.argv) != 2:
    print("Error: Expecting the time in seconds as an argument.")
    sys.exit()

# Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SECS_IN_MIN = 60

# set up pygame
pygame.init()

# Timer class that will contain everything needed to create a countdown timer
class Timer:

    def __init__(self, secs):
        self.width = 230
        self.height = 50
        self.display = pygame.display.set_mode((self.width, self.height))
        self.counter_value = secs
        self.count_font = pygame.font.SysFont("couriernew", 48)
        self.background_color = BLACK


clock = pygame.time.Clock()
pygame.display.set_caption("Countdown Timer")
icon = pygame.image.load("hourglass2.png")
pygame.display.set_icon(icon)

def close_timer():
    pygame.quit()
    sys.exit()

start_ticks = pygame.time.get_ticks()

timer = Timer(int(sys.argv[1]))

# Set up the text
text = timer.count_font.render(str(timer.counter_value), True, WHITE)
textRect = text.get_rect()
textRect.centerx = timer.display.get_rect().centerx
textRect.centery = timer.display.get_rect().centery

# draw the white background onto the surface
timer.display.fill(timer.background_color)

# draw the text onto the surface
timer.display.blit(text, (0, 0))

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            close_timer()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                close_timer()

    seconds = timer.counter_value - ((pygame.time.get_ticks() - start_ticks) / 1000)
    seconds = max(0, seconds)
    if seconds == 0:
        timer.background_color = RED
    minutes, seconds = divmod(seconds, SECS_IN_MIN)
    text = timer.count_font.render("{:02.0f}:{:05.2f}".format(minutes, seconds), True, WHITE)

    # Fill the screen
    timer.display.fill(timer.background_color)
    timer.display.blit(text, (0, 0))

    # Refresh the screen
    pygame.display.flip()

    clock.tick(30)