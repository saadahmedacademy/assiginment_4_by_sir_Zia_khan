"""
Converts feet to inches. Feet is an American unit of measurement. 
There are 12 inches per foot. Foot is the singular,
 and feet is the plural.
"""

def main():
    while True:
        try:
            # Get the number of feet from the user
             feet_input: str = input("Enter a number of feet or exit to quit: ")

             if feet_input.lower() == "exit":
              print("Goodbye!")
              return
             
             feet: float = float(feet_input)
         
             unit = "foot" if feet == 1 else "feet"

             inches: float = feet * 12

             unit_inches = "inch" if inches == 1 else "inches"

             print(f"{feet} {unit} is {inches} {unit_inches}.")

        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")


if __name__ == "__main__":
    main()
    
