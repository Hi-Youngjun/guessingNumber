import random

EASY = 10
HARD = 5
def guessing(guess, number):
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number}")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY
    elif level == 'hard':
        return HARD
    else:
        print("Please choose 'easy' or 'hard' only.")
        playing_game()


def playing_game():
    number = random.randint(1, 100)
    attempt = difficulty()
    guess = 0
    while guess != number:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        guessing(guess, number)
        attempt -= 1
        if attempt == 0:
            print("You've run out of guesses, you lose")
            return

print(
    '''
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    ''')
playing_game()