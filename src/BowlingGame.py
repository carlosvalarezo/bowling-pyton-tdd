class BowlingGame:

    def __init__(self):
        bowling_score = 0
        bowling_frames = []

    @classmethod
    def create_game(cls):
        return BowlingGame()

    @classmethod
    def calculate_game_score(cls, bowling_frames_scores):
        from functools import reduce
        import operator
        return reduce(operator.add, bowling_frames_scores)
