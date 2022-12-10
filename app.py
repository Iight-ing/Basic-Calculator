import sys
import time

print("Please enter both of your number below.")

number_one = float(input("Number one: "))
number_two = float(input("Number two: "))
print("\n")

print("Choose which unit you would like to use.")
units = input("Units: (A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision:  ")

if units.lower() in ["a", "add", "addition"]:
    addition = number_one + number_two
    print(f"Answer: {addition}")

elif units.lower() in ["s", "sub", "subtraction"]:
    subtraction = number_one - number_two
    print(f"Answer: {subtraction}")

elif units.lower() in ["m", "mul", "multiplication"]:
    multiplication = number_one * number_two
    print(f"Answer: {multiplication}")

elif units.lower() in ["d", "div", "division"]:
    division = number_one / number_two
    print(f"Answer: {division}")
