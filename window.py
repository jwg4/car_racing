import os, pygame, sys

from scroller import *

class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = (180, 120)
        self.window = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        car_location = (self.dimensions[0]/2, 60)
        car_image = pygame.image.load("sprites/car1.png")
        sun_location = (0, 0)
        sun_image = pygame.image.load("sprites/sunny.png")
        self.fixed_sprites = [
            (car_image, car_location),
            (sun_image, sun_location),
        ]
        self.opponent_offset = 0
        self.opponent_image = pygame.image.load("sprites/car2.png")
        self.opponent_location = (self.dimensions[0]/2, 75)
        self.init()

    def init(self):
        # Create the game
        self.speed = 0
        self.scrollers = [
            GrassScroller(self.dimensions[0], 30),
            GrassScroller(self.dimensions[0], 45),
            GrassScroller(self.dimensions[0], 60),
            GrassScroller(self.dimensions[0], 105),
            RoadScroller(self.dimensions[0], 75),
            SkyScroller(self.dimensions[0], 0),
            SpriteScroller(self.dimensions[0], 30)
        ]

        # Draw
        self.draw()

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(40)

        self.listen_for_input()

        for scroller in self.scrollers:
            scroller.advance(self.speed)

        self.update_opponent()
        self.draw()

    def update_opponent(self):
        self.opponent_offset = self.opponent_offset - 2 + self.speed

    # Drawing
    def draw(self):
        self.window.fill((78, 190, 51))
        for scroller in self.scrollers:
            scroller.draw(self.window)
        self.draw_fixed()
        self.draw_opponent()

    def draw_fixed(self):
        for image, location in self.fixed_sprites:
            self.window.blit(image, location)

    def draw_opponent(self):
        location = (self.opponent_location[0] + self.opponent_offset, self.opponent_location[1])
        self.window.blit(self.opponent_image, location)

    def quit(self):
        print "QUIT"
        pygame.quit()
        sys.exit()

    def listen_for_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    if self.speed < 4:
                        self.speed = self.speed + 1
                elif (event.key == pygame.K_RIGHT):
                    if self.speed > 0:
                        self.speed = self.speed - 1
            elif event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYUP:  # Keyboard
                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                    self.quit()
