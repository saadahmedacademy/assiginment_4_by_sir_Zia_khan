"""
Problem Statement

Ask the user for two numbers, one at a time,
and then print the result of dividing the first number by the second and also the remainder of the division.
"""


def main():
    # Ask for the first number
    num1 = int(input("Please enter an integer to be divided: "))

    # Ask for the second number
    num2 = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient = num1 // num2
    remainder = num1 % num2

    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
