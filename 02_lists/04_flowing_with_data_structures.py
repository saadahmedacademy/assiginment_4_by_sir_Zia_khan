"""
Point To Understand:

You're learning about mutability in Python, which is a key concept 
when working with data types like lists and dictionaries. Here's a clean and complete version of the solution for your add_three_copies(...) function,
 illustrating how changes to mutable data types (like lists) persist even without returning anything:
"""

def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
