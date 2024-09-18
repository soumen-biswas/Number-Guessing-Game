import random


def number_guessing_game():
    print("Welcome to Number Guessing Game! \n\nTry to guess the number between 1 to 10")


    number = random.randint(1, 100)
    guess = 0

    while True:
        try:
            user_input = int(input("Enter your guess: "))
            guess += 1

            if user_input < number:
                print("Too low!")
            elif user_input > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {guess} guesses!")
                break

        except ValueError:
            print("Invalid input! please enter a number between 1 and 100")