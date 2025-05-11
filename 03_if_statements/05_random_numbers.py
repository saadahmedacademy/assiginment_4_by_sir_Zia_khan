import random

def main():
    start_range = 1
    end_range = 100

    print("Random integers between", start_range, "and", end_range, ":")

    for i in range(10):
        value = random.randint(start_range, end_range)
        count = i + 1

        # Determine proper suffix
        if 11 <= count <= 13:
            suffix = "th"
        elif count % 10 == 1:
            suffix = "st"
        elif count % 10 == 2:
            suffix = "nd"
        elif count % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"

        print(f"{count}{suffix} time you get {value}")

if __name__ == "__main__":
    main()
