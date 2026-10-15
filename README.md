# number-guessing-game

## How to Run the Game

Open your terminal in the project directory and follow the below commands to set up the environment and run the game:

```bash
# 1. Create a virtual environment
python3 -m venv .venv

# 2. Activate the virtual environment
# On macOS / Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# 3. Run the game script
python3 guess.py
```

## Test Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Guess that is too low | Entered `22` when the secret number was higher | "Too low" hint and decreases remaining attempts | `Too low! Attempts left 9!` | Yes |
| 2 | Guess that is too high | Entered `35` when the secret number was lower| "Too high" hint and decreases remaining attempts | `Too high! Attempts left 8!` | Yes |
| 3 | Correct guess and current attempt count | Entered `45` on the 4rd attempt | Game congratulates the player and prints the correct total attempt | `Congratulations! You guessed the number 45 in 4 attempts!` | Yes |
| 4 | string input validation | Typed `zzz` | reject input without incrementing attempt count | `Invalid input` with attempt count remained same | Yes |
| 5 | Blank entry validation | Typed empty string | reject input without incrementing attempt count | `Invalid input` with attempt count remained same | Yes |
| 6 | Number below range validation | Entered `0`, `-5`  | reject input without incrementing attempt count | `Invalid input` with attempt count remained same | Yes |
| 7 | Number above range validation | Entered `999` | reject input without incrementing attempt count | `Invalid input` with attempt count remained same | Yes |
| 8 | Difficulty level range and attempts | Selected option `2` at difficulty level | Range set to 1 to 100, attempts allowed set to 8 | Range set to 1-100, limit set to 8 attempts | Yes |
| 9 | Running out of attempts | Use all 10 allowed attempts with incorrect guesses | The game stops and reveals the secret number | `Sorry, you have reached the limit of attempts! The secret number is 42` | Yes |
| 10 | Time Challenge timeout | Waited over 60 seconds before submitting the correct guess | Game ends immediately upon timeout detection and reveals secret number | `Time limit reached! The secret number is 42` | Yes |
| 11 | Remaining time display | Input guesses | Game prints the time left | `Time left: 51.233405351638794 seconds` | Yes |
| 12 | Invalid difficulty menu input | Typed `-2`, `zzz` at the difficulty selection level | Reject input, and ask the question again | `Invalid input` with the options again | Yes |
| 13 | Invalid chanllenge menu input | Typed `8`, `zzz` at the challenge type | Reject input, and ask the question again | `Invalid input` with the options again | Yes |
| 14 | Difficulty level range and attempts | Selected option `1` at difficulty level | Range set to 1 to 50, attempts allowed set to 10 | Range set to 1-50, limit set to 10 attempts | Yes |
| 15 | Difficulty level range and attempts | Selected option `3` at difficulty level | Range set to 1 to 500, attempts allowed set to 10 | Range set to 1-500, limit set to 10 attempts | Yes |