"""
Problem Statement
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

"""


# Initialize an empty dictionary to store the counts
counts = {}

def count_numbers():
    # Loop to get user input
    while True:
        # Get user input
        num = input("Enter a number (or 'done' to finish): ")
        
        # Check if the user wants to finish
        if num.lower() == 'done':
            break
        
        # Convert the input to an integer
        try:
            num = int(num)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Update the count in the dictionary
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Print the counts
    for num, count in counts.items():
        print(f"{num} appears {count} times.")


if __name__ == "__main__":
    count_numbers()