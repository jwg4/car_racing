import pygame

class Opponent(object):
    def __init__(self, filename, x, y):
        self.offset = 0
        self.image = pygame.image.load(filename)
        self.start_x = x
        self.start_y = y

    def update(self, speed):
        self.offset = self.offset - 2 + speed

    def draw(self, window):
        location = (self.start_x + self.offset, self.start_y)
        window.blit(self.image, location)


