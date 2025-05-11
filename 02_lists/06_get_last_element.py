"""
Problem Statement
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. 
The list is guaranteed to be non-empty, but there are no guarantees on its length.


"""

def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(F"First way to get the last element : lst[-1] = { lst[-1]}")

    print(f"Second way to get the last element : list[len(lst) - 1 ] = {lst[len(lst) - 1]}")  


def main():
    """
    Main function to test get_last_element.
    """
    # Test cases
    test_list1 = [1, 2, 3, 4, 5]
    test_list2 = ['a', 'b', 'c', 'd']
    test_list3 = [True, False, True]

    print("Test case 1:")
    get_last_element(test_list1)

    print("\nTest case 2:")
    get_last_element(test_list2)

    print("\nTest case 3:")
    get_last_element(test_list3)
if __name__ == "__main__":
    main()