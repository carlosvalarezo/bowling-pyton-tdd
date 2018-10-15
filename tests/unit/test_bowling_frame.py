import unittest

from src.BowlingFrame import BowlingFrame


class TestBowlingFrame(unittest.TestCase):

    def setUp(self):
        self.current_frame = BowlingFrame()

    def test_create_game_object(self):
        self.assertIsInstance(self.current_frame, BowlingFrame)

    def test_method_calculate_current_score_should_return_10(self):
        rolls = [7, 3]
        current_frame_score = self.current_frame.calculate_frame_score(rolls)
        assert current_frame_score == 10


