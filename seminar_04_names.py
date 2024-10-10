"""
Seminar 4 - Lists
Given a list of names, prompt the user to remove names
until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
"""

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print(f"{name_to_remove} is not in the list")
    name_to_remove = input("Who do you want to remove? ")
print(", ".join(names))

# while name_to_remove != "":
#     if name_to_remove in names:
#         names.remove(name_to_remove)
#     else:
#         print(name_to_remove + " is not in the list.")
#     name_to_remove = input("Who do you want to remove? ")
