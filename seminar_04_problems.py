"""
What's wrong with this code from practical 03 files, question 4?
How can we improve it?
"""

total = 0.0
with open("numbers.txt", "r") as input_file:
    for line in input_file:
        total += float(line)
print(f"Total sum of numbers is {total}")
