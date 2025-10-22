Bowling Game Scorer (Python)

This project is a Bowling Game scoring system built in Python.
It accurately calculates a player’s total bowling score based on the official ten-pin bowling rules, handling strikes, spares, open frames, and 10th-frame bonuses.
The program also performs input validation and includes a unit test suite to ensure accuracy.

HOW TO RUN AND TEST THE CODE
 1. Run the Program Interactively

You can execute the program and enter rolls manually:
python bowling_game.py
Example session
Enter your rolls separated by spaces only 10 frames(e.g. 1 4 4 5 6 4 5 5 10 ...):
> 1 4 4 5 6 4 5 5 10 0 1 7 3 6 0 10 2 6
Final Score: ------
 2. Run with Command-Line Rolls

You can also provide the rolls directly through the command line:

python bowling_game.py 1 4 4 5 6 4 5 5 10 0 1 7 3 6 0 10 2 6
3. Run the Automated Tests

The program includes unit tests built with Python’s standard unittest library.

Run all tests:

python bowling_game.py --test


Expected output if everything passes:

--------------------------------------
Ran 9 tests in 0.01s
OK

WHAT EACH TEST CHECKS

Each test validates one specific game rule or condition.
| Test Name                             | Description                        | Expected Behavior                     |
| ------------------------------------- | ---------------------------------- | ------------------------------------- |
| **test_all_zeros**                    | 20 rolls of 0                      | Final score = **0**                   |
| **test_incomplete_rolls_raises**      | Not enough rolls for 10 frames     | Raises `IndexError`                   |
| **test_tenth_frame_spare**            | 10th frame ends with spare (5,5,3) | Correctly adds bonus → Score = **13** |
| **test_invalid_roll_above_10**        | Roll exceeds 10 pins               | Raises `ValueError`                   |
| **test_invalid_frame_sum_exceeds_10** | Frame sum exceeds 10 (e.g., 8+5)   | Raises `ValueError`                   |
| **test_three_strikes_in_a_row**       | Three strikes at start             | Score = **60**                        |
| **test_perfect_game**                 | 12 consecutive strikes             | Score = **300**                       |
| **test_all_spares**                   | [5,5] repeated 10 times + bonus 5  | Score = **150**                       |
| **test_reset_game**                   | Ensures reset() clears game state  | Rolls list reset correctly            |

Additional Notes on Testing

Each test focuses on one rule only, keeping logic simple and reliable.

The tests use the same BowlingGame class that powers the main game.

Running tests ensures that strikes, spares, bonuses, and invalid inputs are all handled correctly.

OW INVALID INPUT IS HANDLED

The program prevents invalid or impossible rolls with clear, user-friendly error messages.
It never crashes with unhandled exceptions.
| Invalid Input Type      | Example                    | Behavior / Message                                                 |
| ----------------------- | -------------------------- | ------------------------------------------------------------------ |
| **Roll < 0 or > 10**    | `game.roll(11)`            | Raises `ValueError("Invalid roll: 11. Must be between 0 and 10.")` |
| **Frame sum > 10**      | Rolls: `8,5`               | Raises `ValueError("Invalid frame: total pins exceed 10.")`        |
| **Non-integer roll**    | `"A"`                      | Raises `TypeError("Pins must be an integer.")`                     |
| **Incomplete game**     | Only 5 rolls entered       | Raises `IndexError("Incomplete rolls — game ended early.")`        |
| **Missing bonus rolls** | `5,5` only (no bonus roll) | Raises `IndexError("Incomplete bonus roll.")`                      |
| **Too many rolls**      | More than 21 rolls         | Extra rolls are ignored after the 10th frame                       |

PROJECT STRUCTURE
bowling_game.py   →  main logic, CLI input, and unit tests
README.md         →  documentation (this file)

CODE OVERVIEW

The project is centered around a class BowlingGame, which tracks and scores rolls.

Key Methods:

roll(pins)
Records a roll and validates that pins per frame ≤ 10.

score()
Calculates the final total score using official bowling rules:

Strike → 10 + next 2 rolls

Spare → 10 + next 1 roll

Open frame → sum of two rolls

is_strike(roll_index)
Checks if a frame is a strike.

is_spare(roll_index)
Checks if a frame is a spare.

strike_bonus(roll_index)
Adds next two rolls as strike bonus.

spare_bonus(roll_index)
Adds next roll as spare bonus.

frame_score(roll_index)
Adds both rolls in a normal frame.

reset()
Clears all rolls to start a new game.

EXAMPLE CALCULATION

Input Rolls:

1 4 4 5 6 4 5 5 10 0 1 7 3 6 0 10 2 6
Output:

Final Score: 109

Explanation:

Frame 1: 1+4 = 5

Frame 2: 4+5 = 9

Frame 3: Spare (6+4) → + next roll (5) = 15

Frame 4: Spare (5+5) → + next roll (10) = 20

Frame 5: Strike (10) → + next two rolls (0+1) = 11

And so on...

 FUTURE IMPROVEMENTS

Here are several potential features and improvements for future versions:

Add a validate_game() method
Pre-checks all rolls before scoring for better user feedback.

Frame-by-frame score display
Show running totals per frame (e.g., a real bowling scorecard).

Interactive game mode
Let the user input rolls one frame at a time, displaying the score after each frame.

Graphical or Web Interface
Use Tkinter or Flask to visualize scoring and frames.

Persistent data storage
Store player scores, history, and averages in a file or database.

Additional edge-case tests
Cover special 10th-frame scenarios like strike-spare combinations or all-zeros games.

Multiple player mode
Add support for multiplayer games with alternating turns.

 SUMMARY

✔ Implements official bowling scoring rules
✔ Includes automated unit tests
✔ Handles invalid inputs safely
✔ Clean, modular, and easy to extend
