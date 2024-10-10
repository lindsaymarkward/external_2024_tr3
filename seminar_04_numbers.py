"""
Seminar 4 - Write the missing functions
"""


def main():
    # numbers = get_numbers()
    # print(numbers)
    numbers = [1, 4.5, 2, 90, -2, 8, 2]
    square_numbers(numbers)
    display_numbers(numbers)
    print(numbers)  # test


def get_numbers():
    strings = input("Enter numbers separated by commas: ").split(',')
    # numbers = []
    # for string in strings:
    #     numbers.append(float(string))
    # return numbers
    return [float(string) for string in strings]


def square_numbers(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = float(number) ** 2


def display_numbers(numbers):
    # numbers.sort()
    # for number in numbers:
    #     print(number, end="..")
    print("..".join((str(number) for number in sorted(numbers))))


main()
