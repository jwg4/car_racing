import random
import pygame


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


class RoadScroller(Scroller):
    filename = "backgrounds/road.png"
    filename_alt = "backgrounds/bridge_.png"

    def __init__(self, width, y_offset):
        super(RoadScroller, self).__init__(width, y_offset)
        self.image = pygame.image.load(self.filename)
        self.alt_image = pygame.image.load(self.filename_alt)
        self.pieces = self.load_pieces(self.image, width)

    def draw(self, window):
        for piece in self.pieces:
            height = piece[0].get_height()
            extra_offset = 15 - height / 2
            window.blit(piece[0], (piece[1], self.y_offset + extra_offset))

    def new_piece(self, offset):
        if random.random() > 0.8:
            image = self.alt_image
        else:
            image = self.image
        piece = (image, offset - image.get_width())
        return piece


class BGScroller(Scroller):
    def __init__(self, width, y_offset):
        super(BGScroller, self).__init__(width, y_offset)
        self.image = pygame.image.load(self.filename)
        self.pieces = self.load_pieces(self.image, width)

    def new_piece(self, offset):
        piece = (self.image, offset - self.image.get_width())
        return piece


class SkyScroller(BGScroller):
    filename = "backgrounds/sky.png"


class GrassScroller(BGScroller):
    filename = "backgrounds/grass.png"


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

class MudScroller(BGScroller):
    filename = "sprites/mud.png"

    def _load_pieces(self, width):
        x = 0
        while (width - x) >= 0:
            if random.random() < 0.05:
                yield self.new_piece(x)
            x = x + self.image.get_width()

    def load_pieces(self, image, width):
        image_width = image.get_width()
        return list( self._load_pieces(width) )

    def advance(self, speed):
        l = [ (piece[0], piece[1] + speed) for piece in self.pieces ]
        if l:
            if l[-1][1] > self.width:
                l = l[:-1]
        if random.random() * self.image.get_width() < 0.05 * speed:
            l = [ self.new_piece(0) ] + l

        self.pieces = l

