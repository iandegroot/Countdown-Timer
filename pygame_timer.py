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

TOP_RIGHT_COORDS = (0, 0)

# Set up pygame
pygame.init()

# Timer class that will contain everything needed to create a countdown timer
class Timer:

    def __init__(self, secs):
        self.width = 230
        self.height = 50
        self.display = pygame.display.set_mode((self.width, self.height))
        self.init_counter_value_in_secs = secs
        self.counter_value_in_secs = self.init_counter_value_in_secs
        self.count_font = pygame.font.SysFont("couriernew", 48)
        self.background_color = BLACK
        self.start_ticks = 0
        self.in_count_mode = False

    def update_time(self):
        self.update_display(self.calculate_new_time())

    def calculate_new_time(self):
        secs_passed = ((pygame.time.get_ticks() - self.start_ticks) / 1000)
        self.counter_value_in_secs = self.init_counter_value_in_secs - secs_passed
        self.counter_value_in_secs = max(0, self.counter_value_in_secs)
        if self.counter_value_in_secs == 0:
            self.background_color = RED
            self.in_count_mode = False
        minutes, seconds = divmod(self.counter_value_in_secs, SECS_IN_MIN)
        return self.count_font.render("{:02.0f}:{:05.2f}".format(minutes, seconds), True, WHITE)

    def update_display(self, new_text):
        self.display.fill(self.background_color)
        self.display.blit(new_text, TOP_RIGHT_COORDS)

    def toggle_mode(self):
        self.in_count_mode = not self.in_count_mode
        if self.in_count_mode:
            # Get a reference number of ticks to start the timer
            self.start_ticks = pygame.time.get_ticks()
        else:
            self.init_counter_value_in_secs = self.counter_value_in_secs

    def close(self):
        pygame.quit()
        sys.exit()

# Window initialization
clock = pygame.time.Clock()
pygame.display.set_caption("Countdown Timer")
icon = pygame.image.load("resources/images/hourglass2.png")
pygame.display.set_icon(icon)

# Create a Timer
timer = Timer(int(sys.argv[1]))

# Set up the text
minutes, seconds = divmod(timer.init_counter_value_in_secs, SECS_IN_MIN)
text = timer.count_font.render("{:02.0f}:{:05.2f}".format(minutes, seconds), True, WHITE)
timer.display.blit(text, TOP_RIGHT_COORDS)

# Run the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            timer.close()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                timer.close()
        elif event.type == MOUSEBUTTONDOWN:
            if timer.counter_value_in_secs != 0:
                timer.toggle_mode()

    # Check the mode and act accordingly
    if timer.in_count_mode:
        timer.update_time()

    # Refresh the screen
    pygame.display.flip()

    clock.tick(30)
