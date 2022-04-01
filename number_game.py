#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells if the number user inputs is correct

import random


def main():
    # this function checks if the number user guessed is correct

    # input
    guessed_number_string = input("Enter a number between 0 and 9: ")
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guessed_number = int(guessed_number_string)
        if guessed_number == random_number:
            print("You Guessed Correctly!")
        else:
            print(
                "You Guessed Incorrectly. The correct number was {}.".format(
                    random_number
                )
            )
    except Exception:
        print("Please input an Integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
