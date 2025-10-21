# bowling_game.py
class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        """Record a roll."""
        self.rolls.append(pins)

    def score(self) -> int:
        """Compute total score for the game."""
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2
        return total_score

    # ----- Helper methods -------------------------------------
    def is_strike(self, roll_index: int) -> bool:
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index: int) -> bool:
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_bonus(self, roll_index: int) -> int:
        return self.safe_sum(roll_index + 1, 2)

    def spare_bonus(self, roll_index: int) -> int:
        return self.safe_sum(roll_index + 2, 1)

    def frame_score(self, roll_index: int) -> int:
        return self.safe_sum(roll_index, 2)

    def safe_sum(self, start: int, count: int) -> int:
        """Avoid index errors at the end of roll list."""
        return sum(self.rolls[start:start + count])
    
    # our game try ---------------------------------------------
game = BowlingGame()

# Rolls for the our game try that  final score is 109
rolls = [1,4, 4,5, 6,4, 5,5, 10, 0,1, 7,3, 6,0, 10, 2,6]

for pins in rolls:
    game.roll(pins)

print("Final Score:", game.score())



# ---------- Unit Tests -------------------------------------
def test_bowling_game():
    # Test 1: All open frames (no strikes/spares)
    game = BowlingGame()
    for _ in range(20):
        game.roll(4)
    assert game.score() == 80

    # Test 2: One spare (5 + 5 + 3 bonus)-------------------
    game = BowlingGame()
    rolls = [5, 5, 3] + [0] * 17
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 16

    # Test 3: One strike (10 + 3 + 4 bonus)-----------------------
    game = BowlingGame()
    rolls = [10, 3, 4] + [0] * 16
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 24

    # Test 4: Perfect game (12 strikes)-----------------------
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300

    # Test 5: Example game (final score = 109)-----------------------
    example_rolls = [1,4, 4,5, 6,4, 5,5, 10, 0,1, 7,3, 6,0, 10, 2,6]
    game = BowlingGame()
    for pins in example_rolls:
        game.roll(pins)
    assert game.score() ==109

    print(" All tests passed successfully!")


if __name__ == "__main__":
    test_bowling_game()

