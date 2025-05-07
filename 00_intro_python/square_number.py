"""
Problem Statement
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""

def main():
    # Get the number from the user
    number: float = float(input("Type a number to see its square: "))

    # Print out the square of the number
    print(str(number) + " squared is " + str(number * number))


if __name__ == '__main__':
    main()