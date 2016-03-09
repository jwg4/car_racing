import unittest

from scroller import Scroller, SpriteScroller

class TestScroller(unittest.TestCase):
    class MockImage(object):
        def __init__(self, width):
            self.width = width

        def get_width(self):
            return self.width

    def test_load_correct_number_of_pieces(self):
        image = TestScroller.MockImage(30)
        l = Scroller.load_pieces(image, 90)
        self.assertEqual(len(l), 3)

    def test_load_correct_type_of_pieces(self):
        image = TestScroller.MockImage(30)
        l = Scroller.load_pieces(image, 90)
        self.assertEqual(l[0][0], image)

class TestSpriteScroller(unittest.TestCase):
    def test_correct_pieces(self):
        scroller = SpriteScroller(90, 0)
        self.assertEqual(len(scroller.pieces), 3)

    def test_correct_x_offsets(self):
        scroller = SpriteScroller(90, 0)
        self.assertEqual(set(x[1] for x in scroller.pieces), set([0, 30, 60]))
