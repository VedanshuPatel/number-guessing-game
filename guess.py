import random
import time

# ---------- Settings ----------
class NumberGuess:
    """
    This class represents a Number Guessing Game which has attempt limits,time challenge and difficulty levels.
    """
    def __init__(self):
        self.DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
        self.TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
        self.low=1               # Lower bound of number range
        self.high=None           # Upper bound of the number game, changes based on difficulty
        self.total_attempts = 0  # total attempts by the user
        self.attempts_allowed = 0 # attempts allowed by the game
        self.win_flag = False  # A flag to check if the user won
        self.time_flag = False # A flag to check if its a time challenge


    # ---------- Helper Functions ----------
    def validate_guess(self,guess: str) -> bool:
        """
        The function checks if the guess is valid input or not.
        :param guess:  the input given by the user.
        :return: A boolean which says if the guess is valid or not.
        """
        guess = guess.strip()
        if guess.isdigit():
            return True
        return False

    def start_game(self):
        """
        The main loop of the game where the user does all the selections in the game.
        :return: The output according to the rules and conditions of the game
        """
        print("Welcome to the Number Guessing Game")

        # ---------- Choose a level ----------
        # Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
        while True:
            print("1. Easy (1 to 50)")
            print("2. Medium (1 to 100)")
            print("3. Hard (1 to 500)")
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
        while True:
            print("1. Classic")
            print("2. Time Challenge")
            challenge_option = input("Please choose a challenge type from the options above: ")
            if challenge_option == "1":
                self.time_flag = False
                break
            elif challenge_option == "2":
                self.time_flag = True
                break
            else:
                print("Invalid input")


        # ---------- Set up the round ----------
        # Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
        self.DEBUG_SECRET = random.randint(1, self.high)
        if self.time_flag:
            start_time = time.time()

        # ---------- Guess loop ----------
        # Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
        while not self.win_flag:
            if self.attempts_allowed <= self.total_attempts: # Condition to check if the user has exhaused all the attempts
                print(f"Sorry, you have reached the limit of attempts! The secret number is {self.DEBUG_SECRET}")
                break
            if self.time_flag: # Condition to check the time limit in the time challenge
                elapsed_time = time.time() - start_time
                if elapsed_time >= self.TIME_LIMIT:
                    print(f"Time limit reached! The secret number is {self.DEBUG_SECRET}")
                    break
                print(f"Time left: {self.TIME_LIMIT - elapsed_time} seconds")

            guess = input("Please enter a number: ")
            if self.validate_guess(guess) and (self.low <= int(guess) <= self.high): #Condition to check if the input is valid
                if self.time_flag: # Condition to check the time limit in the time challenge
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= self.TIME_LIMIT:
                        print(f"Time limit reached! The secret number is {self.DEBUG_SECRET}")
                        break
                self.total_attempts += 1
                guess = int(guess)

        # ---------- End of round ----------
        # Goal: show the result that matches how the round ended.

                if guess == self.DEBUG_SECRET:
                    print(f"Congratulations! You guessed the number {self.DEBUG_SECRET} in {self.total_attempts} attempts!")
                    self.win_flag = True
                elif guess > self.DEBUG_SECRET:
                    print(f"Too high! Attempts left {self.attempts_allowed-self.total_attempts}!")
                else:
                    print(f"Too low! Attempts left {self.attempts_allowed-self.total_attempts}!")
            else:
                print("Invalid input")


if __name__ == "__main__":
    game = NumberGuess()
    game.start_game()