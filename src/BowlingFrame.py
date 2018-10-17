
class BowlingFrame:

    @classmethod
    def create_bowling_frame(cls):
        return BowlingFrame()

    @classmethod
    def calculate_frame_score(cls, rolls_of_current_frame):
        from functools import reduce
        import operator
        pins_knocked_down = cls.___get_pins_knocked_down(rolls_of_current_frame)
        return reduce(operator.add, pins_knocked_down)

    @classmethod
    def check_frame_award(cls, roll):
        total_pins_knocked_down = roll[0].pins_knocked_down + roll[1].pins_knocked_down
        if roll[0].pins_knocked_down == 10 and roll[0].roll_number == 1:
            return 'strike'
        else:
            if total_pins_knocked_down == 10:
                return 'spare'

    @classmethod
    def ___get_pins_knocked_down(cls, rolls_of_current_frame):
        return (current_frame.pins_knocked_down for current_frame in rolls_of_current_frame)

    @classmethod
    def ___get_roll_number(cls, rolls_of_current_frame):
        return (current_roll.rol_number for current_roll in rolls_of_current_frame)


