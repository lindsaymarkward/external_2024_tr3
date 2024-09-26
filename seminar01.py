"""
CP1404 External Seminar 1
Write a program to get a user's item price and
ask for whether it has GST (y/n).
Print the final price using currency formatting (e.g., $16.40).
"""

# item_price = float(input("Price: "))
# gst_status = input("Does that have GST? (y/n): ")
# if gst_status == 'y':
#     final_price = item_price * 1.1
# else:
#     final_price = item_price  # v1
# print(f"Final price: ${final_price:.2f}")


# price = float(input("Price: "))
# gst_status = input("Does that have GST? (y/n): ")
# if gst_status == 'y':
#     price *= 1.1
# print(f"Final price: ${price:.2f}")

sentence = input("Sentence: ")
for character in sentence:
    if character == " ":
        print("space!")
