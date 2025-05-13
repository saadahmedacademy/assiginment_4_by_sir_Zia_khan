"""
Problem Statement:
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

"""

def is_odd(n):

    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

def main():
    take_input = input("Enter a number: ")
    try:
        number = int(take_input)
        is_odd(number)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()