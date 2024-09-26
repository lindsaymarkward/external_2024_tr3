from random import randint


def main():
    low_number, high_number = get_valid_range()
    print_smilies(low_number, high_number)

# This commit will...
def get_valid_range():
    low_number = int(input("Enter a low number: "))
    high_number = int(input("Enter a high number: "))
    while low_number >= high_number:
        print("Invalid range!")
        high_number = int(input("Enter a high number: "))
    return low_number, high_number


def print_smilies(low_number, high_number):
    print(randint(low_number, high_number) * ":)")


main()
