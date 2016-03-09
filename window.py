import os, pygame

from scroller import *

class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = (180, 60)
        self.window = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.car_location = (self.dimensions[0]/2, 15)
        self.car_image = pygame.image.load("sprites/car1.png")
        self.init()

    def init(self):
        # Create the game
        self.speed = 0
        self.scrollers = [
            RoadScroller(self.dimensions[0], 30),
            SkyScroller(self.dimensions[0], 0),
            SpriteScroller(self.dimensions[0], 0)
        ]

        # Draw
        self.draw()

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(40)

        self.listen_for_input()

        for scroller in self.scrollers:
            scroller.advance(self.speed)

        self.draw()

    # Drawing
    def draw(self):
        self.window.fill((0, 0, 0))
        for scroller in self.scrollers:
            scroller.draw(self.window)
        self.draw_car()

    def draw_car(self):
        self.window.blit(self.car_image, self.car_location)

    def listen_for_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    if self.speed < 4:
                        self.speed = self.speed + 1
                elif (event.key == pygame.K_RIGHT):
                    if self.speed > 0:
                        self.speed = self.speed - 1
                break
