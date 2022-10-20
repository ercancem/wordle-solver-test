# import random

# secret = random.randint(1, 100)
# global guess_array
# global curr_min
# global curr_max

# def get_feedback(guess, secret):        
#     if (guess < 1) or (guess > 100):
#         return print("Out of range")        
#     elif guess == secret:
#         return print("Correct!")
#     elif guess > secret:
#         print("Lower")
#         return make_guess("Lower")
#     else:
#         print("Higher")
#         return make_guess("Higher")
    
# def make_guess(feedback):
#     if feedback == "Correct":
#         print("Game Over!")
#         return
#     elif feedback == "Lower":
#         curr_max = guess_array[-1]
#         new_guess = (guess_array[-1] + curr_min)//2
#         print("I am now guessing: ", new_guess)
#         guess_array.append(new_guess)
#         return get_feedback(new_guess, secret)
#     else:
#         curr_min = guess_array[-1]
#         new_guess = (guess_array[-1] + curr_max)//2
#         print("I am now guessing: ", new_guess)
#         guess_array.append(new_guess)
#         return get_feedback(new_guess, secret)
    
# print("Secret number is: ",  secret)
# get_feedback(guess_array[0], secret)

from random import randint
from itertools import count

def is_guess_correct(number, guess):
    if guess == number:
        return True
    elif guess < number:
        print("The number is HIGHER.")
        return False
    else:
        print("The number is LOWER.")
        return False

def is_valid_guess(number_string):
    return number_string.isdigit()

def get_number(guess_iteration):
    while 1:
        number_string = input("({0}) Guess a number: ".format(guess_iteration))
        if is_valid_guess(number_string):
            return int(number_string)
        else:
            print("Please enter a valid integer!")

def run_game(nmin, nmax):
    number = randint(nmin, nmax)
    print("I'm thinking of a number between {0} and {1}...".format(nmin, nmax))

    for guess_iteration in count(1):
        guess = get_number(guess_iteration)
        if is_guess_correct(number, guess):
            print("YOU WON!")
            break

if __name__ == '__main__':
    run_game(1, 100)