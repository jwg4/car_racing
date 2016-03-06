import os, pygame, sys, time
from pygame.locals import *

import block, game
from scroller import *

class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.window = pygame.display.set_mode((90, 60)
        self.clock = pygame.time.Clock()
        self.car_image = pygame.image.load("sprites/car1.png")
        self.init()

    def init(self):
        # Create the game
        self.speed = 1
        self.scrollers = [
            RoadScroller(),
            #BackGroundScroller(),
            #SkyScroller()
        ]

        # Draw
        self.draw()

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(FPS)

        self.listen_for_input()

        for scroller in self.scrollers():
            scroller.advance(self.speed)

        self.draw()

    # Drawing
    def draw(self):
        self.window.fill(BLACK)
        for scroller in self.scrollers():
            scroller.draw(window)
        self.draw_car()

    def draw_car(self):
        self.window.blit(self.car_image, (30, 15))
