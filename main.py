import random
########################################################################


def welcome():
    """Function prints a welcome message to the screen."""
    print("\nWelcome to the NUMBER GUESSING GAME!")
    print("You will be guessing a number between 1 and 100.")


def define_target_number():
    """Function picks a random number between 1 and 100.
    Returns int."""
    x = random.choice(range(1, 101))
    return x


def choose_difficulty(user_input):
    """Function asks for an input of "e" or "h".
    It eliminates invalid inputs.
    Returns "e" or "h" as string."""
    while user_input not in ["e", "h"]:
        user_input = input('Invalid input. Please enter "E" for easy or "H" for hard: ').lower()
    return user_input


def easy_or_hard(a):
    """Takes a string "e" or "h".
    Returns number of guesses as int."""
    if a == "e":
        b = 10
    else:
        b = 5
    return b


def how_many_guesses(x):
    """Takes a number of guesses left as int and prints it out."""
    print("\nYou have {} guesses left.".format(x))


def make_a_guess():
    """Takes an int from user input.
    Eliminates invalid inputs."""
    x = input("Make your guess: ")
    while x.isnumeric() is False:
        x = input("Invalid input. Please enter a number: ")
    while int(x) < 1 or int(x) > 100:
        x = input("Number out of range. Enter a number between 1 and 100: ")
    return int(x)


def check_guess(targ, gss):
    if gss < targ:
        print("Too low.")
        return False
    elif gss > targ:
        print("Too high.")
        return False
    else:
        print("You got it!")
        return True


def another_game():
    x = input('\nDo you wanna play again? Type "Y" for yes, or "N" for no: ').lower()
    while x not in ["y", "n"]:
        x = input('Invalid input. Please enter "Y" or "N": ')
    if x == "n":
        return False
    return True


########################################################################

program_running = True
welcome()

while program_running:
    target_number = define_target_number()
    difficulty = choose_difficulty(input('\nChoose your difficulty. Enter "E" for easy, or "H" for hard: ').lower())
    guesses_left = easy_or_hard(difficulty)
    target_number_guessed = False

    while not target_number_guessed:
        how_many_guesses(guesses_left)
        guess = make_a_guess()
        target_number_guessed = check_guess(target_number, guess)
        guesses_left -= 1
        if guesses_left == 0:
            break

    if not target_number_guessed:
        print("\nYou lose. The number was {}.".format(target_number))

    program_running = another_game()

print("\nGoodbye! :)")