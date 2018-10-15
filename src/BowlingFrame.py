
class BowlingFrame:

    @classmethod
    def create_bowling_frame(cls):
        return BowlingFrame()

    @classmethod
    def calculate_frame_score(cls, rolls_of_current_frame):
        from functools import reduce
        import operator
        return reduce(operator.add, rolls_of_current_frame)
