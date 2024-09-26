"""Seminar 2 Do this now warmup program."""
from random import randint


def main():
    """Program to print smilies using user-defined range."""
    low_number, high_number = get_valid_range()
    print_smilies(low_number, high_number)


def get_valid_range():
    """Get valid range."""
    low_number = int(input("Enter a low number: "))
    high_number = int(input("Enter a high number: "))
    while low_number >= high_number:
        print("Invalid range!")
        high_number = int(input("Enter a high number: "))
    return low_number, high_number


def print_smilies(low_number, high_number):
    """Print random number of smilies."""
    print(randint(low_number, high_number) * ":)")


main()
