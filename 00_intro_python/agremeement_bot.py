

"""
**Program Statement:**\n
 Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow! """
def main():
    ask_count = 0
    while ask_count < 3:
        user_input = input("What's your favorite animal? ")
        if user_input:
            print(f"My favorite animal is also {user_input}!")
            return
        ask_count += 1
        if ask_count < 3:
            print("You didn't answer my question.")
        else:
            print("I think you're not interested in talking to me.")

if __name__ == "__main__":
    main()

