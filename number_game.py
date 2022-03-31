#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells if the number user inputs is correct

import random


def main():
    # this function checks if the number user guessed is correct

    # input
    random_number = random.randint(0, 9)
    guessing_number = int(input("Enter the guessing number:"))
    print("")

    # process and output
    if guessing_number == random_number:
        print("Correct!")
    else:
        print("Incorrect!")


if __name__ == "__main__":
    main()
