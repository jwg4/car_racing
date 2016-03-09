import unittest

from scroller import Scroller

class TestScroller(unittest.TestCase):
    class MockImage(object):
        def __init__(self, width):
            self.width = width

    def test_load_pieces(self):
        image = TestScroller.MockImage(30)
        l = Scroller.load_pieces(image, 90)
        self.assertEqual(len(l), 3)
