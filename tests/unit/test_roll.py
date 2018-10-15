import unittest

from src.Roll import Roll


class TestRoll(unittest.TestCase):

    def setUp(self):
        self.current_roll = Roll()

    def test_create_game_object(self):
        self.assertIsInstance(self.current_roll, Roll)
