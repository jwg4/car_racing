import random
import os, pygame

class Scroller(object):
    def __init__(self, width, y_offset):
        self.width = width
        self.y_offset = y_offset

    def draw(self, window):
        for piece in self.pieces:
            window.blit(piece[0], (piece[1], self.y_offset))

    def advance(self, speed):
        l = [ (piece[0], piece[1] + speed) for piece in self.pieces ]
        if l[-1][1] > self.width:
            l = l[:-1]
        if l[0][1] > 0:
            l = [ self.new_piece(l[0][1]) ] + l

        self.pieces = l
            
    @staticmethod
    def load_pieces(image, width):
        image_width = image.get_width()
        return [ (image, i * image_width) for i in range(width / image_width) ]

class BGScroller(Scroller):
    def __init__(self, width, y_offset):
        super(BGScroller, self).__init__(width, y_offset)
        self.image = pygame.image.load(self.filename)
        self.pieces = self.load_pieces(self.image, width)

    def new_piece(self, offset):
        piece = (self.image, offset - self.image.get_width())
        return piece

class RoadScroller(BGScroller):
    filename = "backgrounds/road.png"

class SkyScroller(BGScroller):
    filename = "backgrounds/sky.png"

class SpriteScroller(Scroller):
    def __init__(self, width, y_offset):
        super(SpriteScroller, self).__init__(width, y_offset)
        self.image1 = pygame.image.load("sprites/tree.png")
        self.image2 = pygame.image.load("sprites/building_block.png")
        self.pieces = list(self.load_pieces(width))

    def load_pieces(self, width):
        x = 0
        while (width - x) >= 0:
            piece = self.new_piece(x)
            x = x + piece[0].get_width()
            yield piece
        
    def new_piece(self, offset):
        image = self.image1 if (random.random() > 0.5) else self.image2
        position = offset - image.get_width()
        return (image, position)
