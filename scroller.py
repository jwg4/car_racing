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
            

class RoadScroller(Scroller):
    height = 30

    def __init__(self):
        self.road_image = pygame.image.load("backgrounds/road.png")
        self.pieces = [
            (self.road_image, 0),
            (self.road_image, 90)
        ]

    def new_piece(self, offset):
        piece = (self.road_image, offset - 90)
