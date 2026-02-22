import random


def get_random_numer() -> int:
    return random.randint(1, 100)

def get_number_from_user():
    while True:
        number = int(input('guess a number [1-100]?'))
        if not 1 <= number <= 100:
            print('invalid number')
        return number

def more_than_max(guess, max_guesses_possible)   :
    if guess > max_guesses_possible:
        return True
    else:
        return False

def tell_user_if_guess_higher_lower(user_number, lucky_number):
    if user_number > lucky_number:
        print("Guess lower ...")
    if user_number < lucky_number:
        print('Guess higher ...')

lucky_number = get_random_numer()
max_guess = 10
current_guess = 0

while True:
    user_number = get_number_from_user()
    current_guess += 1
    if user_number == lucky_number:
        print('BINGO!!')
        break
    if more_than_max(current_guess, max_guess):
        print("too many attempts")
        break
    tell_user_if_guess_higher_lower(user_number, lucky_number)
