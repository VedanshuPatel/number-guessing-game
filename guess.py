import random
import time

# ---------- Settings ----------
class NumberGuess:
    def __init__(self):
        self.DEBUG_SECRET = 42   # For testing, set to a number such as 42. Set back to None before your final commit.
        self.TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
        self.low=1
        self.high=None
        self.total_attempts = 0
        self.attempts_allowed = 0
        self.win_flag = False


    # ---------- Helper Functions ----------
    def validate_guess(self,guess: str) -> bool:
        guess = guess.strip()
        if guess.isdigit():
            return True
        return False

    def start_game(self):
        print("Welcome to the Number Guessing Game")

        # ---------- Choose a level ----------
        # Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
        while True:
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            difficulty = input("Please choose a difficulty level from the options above: ")
            if difficulty == "1":
                self.high = 50
                self.attempts_allowed = 10
                break
            elif difficulty == "2":
                self.high = 100
                self.attempts_allowed = 8
                break
            elif difficulty == "3":
                self.high = 500
                self.attempts_allowed = 10
                break
            else:
                print("Invalid input")

        # ---------- Choose a mode ----------
        # Goal: keep asking until the player picks Classic or Time Challenge.

        # ---------- Set up the round ----------
        # Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
        while not self.win_flag:
            if self.attempts_allowed > self.total_attempts:
                print(f"Sorry, you have reached the limit of attempts! The secret number is {self.DEBUG_SECRET}")
                break
            guess = input("Please enter a number: ")
            if self.validate_guess(guess):
                self.total_attempts += 1
                guess = int(guess)
                if guess == self.DEBUG_SECRET:
                    print(f"Congratulations! You guessed the number {self.DEBUG_SECRET} in {self.total_attempts} attempts!")
                    self.win_flag = True
                elif guess > self.DEBUG_SECRET:
                    print(f"Too high! Attempts left {self.attempts_allowed-self.total_attempts}!")
                else:
                    print("Too low! Attempts left {self.attempts_allowed-self.total_attempts}!")
            else:
                print("Invalid input")

        # ---------- Guess loop ----------
        # Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

        # ---------- End of round ----------
        # Goal: show the result that matches how the round ended.

if __name__ == "__main__":
    game = NumberGuess()
    game.start_game()