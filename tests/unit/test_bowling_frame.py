import unittest

from Roll import Roll
from src.BowlingFrame import BowlingFrame


class TestBowlingFrame(unittest.TestCase):

    def setUp(self):
        self.current_frame = BowlingFrame()

    def test_create_game_object(self):
        self.assertIsInstance(self.current_frame, BowlingFrame)

    def test_method_calculate_current_score_should_return_10(self):
        rolls = [Roll(7, 1), Roll(3, 2)]

        current_frame_score = self.current_frame.calculate_frame_score(rolls)

        assert current_frame_score == 10

    def test_method_check_frame_award_should_return_strike(self):
        roll = [Roll(10, 1), Roll(0, 2)]

        award = self.current_frame.check_frame_award(roll)

        assert award == 'strike'

    def test_method_check_frame_award_should_return_spare(self):
        roll = [Roll(5, 1), Roll(5, 2)]

        award = self.current_frame.check_frame_award(roll)

        assert award == 'spare'
