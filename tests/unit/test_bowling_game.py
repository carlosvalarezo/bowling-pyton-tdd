import unittest

from src.BowlingGame import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.current_game = BowlingGame()

    def test_create_game_object(self):
        self.assertIsInstance(self.current_game, BowlingGame)

    def test_method_calculate_game_score_should_return_10(self):
        bowling_frames = [7, 3]
        game_score = self.current_game.calculate_game_score(bowling_frames)
        assert game_score == 10

