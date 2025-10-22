# bowling_game.py
'''BowlingGame scoring program----------
We have to calculate final bowling score for a player in a 10 frame bowling game.
In every frame, player has two chances to knock down 10 pins.
If the player knocks down all 10 pins on the first roll, it is called a "strike".
If the player knocks down all 10 pins in two rolls, it is called a "spare".
If all 10 pins are knocked down in one or two tries then the player gets bonus points.
*our program correctly handle-----------------------
normal frames(less than 10 pins in two rolls),
spares(10 pins in two rolls-add next 1 roll as bonus),
strikes(10 pins in first roll-add next 2 rolls as bonus),
10th frame special rules(allowing up to 3 rolls if spare or strike).
invalid inputs(raise clear error messages).

*input-------------------------------------
The program takes a list of rolls, each roll is the number of pins knocked down (0-10).

*output------------------------------------
the program gives the final total bowling scorce after all 10 frames are completed.
If the input is incorrect (eg. more than 10 pins in a frame without strike), it raises an error.

*Rules--------------------------------------
1. A game consists of 10 frames.
2. Each roll must be an integer between 0 and 10.
3.A frames total pins cannot exceed 10(except bonus rolls in 10th frame).
4. Extra rolls are allowed only in the 10th frame if a spare or strike is scored.

*Approach--------------------------------
1. I created a class `BowlingGame` that stores all rolls in a list.
2. The `score()` method loops through 10 frames, checking for Strike or Spare.
3. For each frame:
   - If Strike → add 10 + next two rolls.
   - If Spare → add 10 + next one roll.
   - Else → just add pins from both rolls.
4. I added helper methods (`is_strike`, `is_spare`, `strike_bonus`, etc.) to keep the logic clear.
5. Input validation ensures no invalid or incomplete rolls.
6. Finally, I added unit tests to check normal, spare, strike, and edge cases.

Example:
Input Rolls → [1,4, 4,5, 6,4, 5,5, 10, 0,1, 7,3, 6,0, 10, 2,6]
Output → Final Score: 109'''


import sys
import unittest

# ----- Constants --------------------------------------------------
TOTAL_FRAMES = 10
STRIKE_PINS = 10


class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame_rolls = []  # track current frame pins

    def roll(self, pins: int):
        """Record a roll, validating it against current frame rules."""
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer.")
        if pins < 0 or pins > STRIKE_PINS:
            raise ValueError(f"Invalid roll: {pins}. Must be between 0 and {STRIKE_PINS}.")

        # Validate that total pins in a frame do not exceed 10 (except after strike)
        if len(self.current_frame_rolls) == 1 and self.current_frame_rolls[0] != STRIKE_PINS:
            if self.current_frame_rolls[0] + pins > STRIKE_PINS:
                raise ValueError(f"Invalid frame: total pins exceed {STRIKE_PINS}.")

        self.rolls.append(pins)
        self.current_frame_rolls.append(pins)

        # Reset frame tracker if two rolls or a strike
        if pins == STRIKE_PINS or len(self.current_frame_rolls) == 2:
            self.current_frame_rolls = []

    def score(self) -> int:
        """Compute total bowling score following standard rules."""
        total_score = 0
        roll_index = 0

        for frame in range(TOTAL_FRAMES):
            if roll_index >= len(self.rolls):
                raise IndexError("Incomplete rolls — game ended early.")

            # Strike: all 10 pins on first roll of frame
            if self.is_strike(roll_index):
                total_score += STRIKE_PINS + self.strike_bonus(roll_index)
                roll_index += 1
            # Spare: two rolls in frame total 10 pins
            elif self.is_spare(roll_index):
                total_score += STRIKE_PINS + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                frame_sum = self.frame_score(roll_index)
                if frame_sum > STRIKE_PINS:
                    raise ValueError(f"Invalid frame: total pins exceed {STRIKE_PINS}.")
                total_score += frame_sum
                roll_index += 2

        return total_score

    # ----- Helper methods -----------------------------------------
    def is_strike(self, roll_index: int) -> bool:
        """Return True if roll is a strike (10 pins)."""
        return roll_index < len(self.rolls) and self.rolls[roll_index] == STRIKE_PINS

    def is_spare(self, roll_index: int) -> bool:
        """Return True if frame is a spare (sum of two rolls = 10)."""
        return (
            roll_index + 1 < len(self.rolls)
            and self.rolls[roll_index] + self.rolls[roll_index + 1] == STRIKE_PINS
        )

    def strike_bonus(self, roll_index: int) -> int:
        """Bonus for strike = pins from next two rolls."""
        if roll_index + 2 >= len(self.rolls):
            raise IndexError("Incomplete strike bonus rolls.")
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index: int) -> int:
        """Bonus for spare = pins from next roll."""
        if roll_index + 2 >= len(self.rolls):
            raise IndexError("Incomplete spare bonus roll.")
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index: int) -> int:
        """Sum of two rolls in a frame."""
        if roll_index + 1 >= len(self.rolls):
            raise IndexError("Incomplete frame (missing second roll).")
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def reset(self):
        """Start a new game."""
        self.rolls = []
        self.current_frame_rolls = []


# ----- Input Handling ---------------------------------------------
def get_rolls_from_input() -> list[int]:
    """Prompt user to enter rolls from console or command line."""
    if len(sys.argv) > 1:
        try:
            return [int(x) for x in sys.argv[1:] if x.isdigit()]
        except ValueError:
            print("Error: All inputs must be integers (0–10).")
            sys.exit(1)

    print("Enter your rolls separated by spaces only 10 frames(e.g. 1 4 4 5 6 4 5 5 10 ...):")
    user_input = input("> ")
    try:
        rolls = [int(x) for x in user_input.split()]
    except ValueError:
        print("Error: Please enter only numbers between 0 and 10.")
        sys.exit(1)

    return rolls


# ----- Main Program -----------------------------------------------
def main():
    rolls = get_rolls_from_input()

    if not rolls:
        print("No rolls entered. Exiting.")
        return

    game = BowlingGame()
    try:
        for pins in rolls:
            game.roll(pins)
        print("\nFinal Score:", game.score())
    except (ValueError, IndexError, TypeError) as e:
        print("Error:", e)


# ----- Unit Tests -------------------------------------------------
class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_all_zeros(self):
        for _ in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def test_incomplete_rolls_raises(self):
        for _ in range(5):
            self.game.roll(3)
        with self.assertRaises(IndexError):
            self.game.score()

    def test_tenth_frame_spare(self):
        rolls = [0]*18 + [5, 5, 3]
        for pins in rolls:
            self.game.roll(pins)
        self.assertEqual(self.game.score(), 13)

    def test_invalid_roll_above_10(self):
        with self.assertRaises(ValueError):
            self.game.roll(11)

    def test_invalid_frame_sum_exceeds_10(self):
        self.game.roll(8)
        with self.assertRaises(ValueError):
            self.game.roll(5)

    def test_three_strikes_in_a_row(self):
        for pins in [10, 10, 10] + [0]*14:
            self.game.roll(pins)
        self.assertEqual(self.game.score(), 60)

    def test_perfect_game(self):
        for _ in range(12):
            self.game.roll(10)
        self.assertEqual(self.game.score(), 300)

    def test_all_spares(self):
        for pins in [5,5]*10 + [5]:
            self.game.roll(pins)
        self.assertEqual(self.game.score(), 150)

    def test_reset_game(self):
        self.game.roll(10)
        self.game.reset()
        self.assertEqual(self.game.rolls, [])
        self.assertEqual(self.game.current_frame_rolls, [])


if __name__ == "__main__":
    if "--test" in sys.argv:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        main()

