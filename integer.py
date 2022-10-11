#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Oct 11, 2022
# This program asks the user to guess a
# number and if they get it wrong they are told so.


def main():
    # a number from user
    user_input = float(input("Enter any integer(number): "))

    # Check to see if the number is negative, positive or zero
    if user_input < 0:
        print(user_input, "is a NEGATIVE number")
    elif user_input > 0:
        print(user_input, "is a POSITIVE number")
    elif user_input == 0:
        print(user_input, "is just zero")


if __name__ == "__main__":
    main()
