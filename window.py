import os, pygame, sys

from opponent import *
from scroller import *
from dimensions import SCALE, IMAGE_DIMENSIONS, WINDOW_DIMENSIONS

class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = IMAGE_DIMENSIONS
        self.scaled_dimensions = WINDOW_DIMENSIONS
        self.real_window = pygame.display.set_mode(self.scaled_dimensions)
        self.window = pygame.Surface(self.dimensions)
        self.clock = pygame.time.Clock()
        car_location = (self.dimensions[0]/2, 60)
        car_image = pygame.image.load("sprites/car1.png")
        sun_location = (0, 0)
        sun_image = pygame.image.load("sprites/sunny.png")
        self.fixed_sprites = [
            (car_image, car_location),
            (sun_image, sun_location),
        ]
        self.opponent = Opponent("sprites/car2.png", self.dimensions[0]/2, 75)
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

        self.opponent.update(self.speed)
        self.draw()

    # Drawing
    def draw(self):
        self.window.fill((78, 190, 51))
        for scroller in self.scrollers:
            scroller.draw(self.window)
        self.draw_fixed()
        self.opponent.draw(self.window)
        
        self.real_window.blit(pygame.transform.scale(self.window, self.scaled_dimensions), (0, 0))

    def draw_fixed(self):
        for image, location in self.fixed_sprites:
            self.window.blit(image, location)

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
