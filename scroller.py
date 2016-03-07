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
    def __init__(self):
        self.image = pygame.image.load(self.filename)
        self.pieces = [
            (self.image, 0),
            (self.image, 90)
        ]

    def new_piece(self, offset):
        piece = (self.image, offset - 90)
        return piece

class RoadScroller(BGScroller):
    height = 30
    filename = "backgrounds/road.png"

