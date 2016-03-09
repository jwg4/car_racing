import random
import os, pygame

class Scroller(object):
    def draw(self, window):
        for piece in self.pieces:
            window.blit(piece[0], (piece[1], self.height))

    def advance(self, speed):
        l = [ (piece[0], piece[1] + speed) for piece in self.pieces ]
        if l[-1][1] > 90:
            l = l[:-1]
        if l[0][1] > 0:
            l = [ self.new_piece(l[0][1]) ] + l

        self.pieces = l
            

class BGScroller(Scroller):
    def __init__(self, width, height):
        self.height = height
        self.image = pygame.image.load(self.filename)
        self.pieces = [
            (self.image, 0),
            (self.image, 90)
        ]

    def new_piece(self, offset):
        piece = (self.image, offset - 90)
        return piece

class RoadScroller(BGScroller):
    filename = "backgrounds/road.png"

class SkyScroller(BGScroller):
    filename = "backgrounds/sky.png"

class SpriteScroller(Scroller):
    def __init__(self, width, height):
        self.height = height
        self.image1 = pygame.image.load("sprites/tree.png")
        self.image2 = pygame.image.load("sprites/building_block.png")
        self.pieces = [ self.new_piece(30 * x) for x in range(10) ]

    def new_piece(self, offset):
        image = self.image1 if (random.random() > 0.5) else self.image2
        position = offset - 30
        return (image, position)
