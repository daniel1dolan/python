# Guessing Game
# Generate a rand0m number between 1 and 9 
# Ask the user to guess the number
# Then tell the user whether their guess was right, low, or high
# 

import pickle
import os.path
import random

if os.path.isfile("correct.pickle"):
    with open("correct.pickle", "rb") as fh:
        number_correct = pickle.load(fh)
else:
    number_correct = 0

def prompt(): 
    print("=" * 21)
    print("I generate a number between 1 and 9, try to guess it.")
    print("Type exit to exit.")

user_input = "0"
while user_input != "exit":
    prompt()
    number = random.randint(1, 9)
    user_input = input("=>")
    if user_input == "exit":
        break
    if int(user_input) == number:
        print("You guessed correct!")
        number_correct += 1
    elif int(user_input) > number:
        print("Too high.")
    elif int(user_input) < number:
        print("Too low.")

with open("correct.pickle", "wb") as fh:
    pickle.dump(number_correct, fh)
print("Goodbye.")
print("Number correct:", number_correct)