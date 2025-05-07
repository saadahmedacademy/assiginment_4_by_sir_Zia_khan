""" 
Program: fahrenheit_to_celsius
--------------------------------
This program asks the user for a temperature in degrees Fahrenheit, 
and then prints out the equivalent temperature in degrees Celsius.
"""

def main():
    degrees_fahrenheit  = float(input("Enter a temperature in degrees Fahrenheit: "))

    degrees_celsius = (degrees_fahrenheit - 32) * (5.0 / 9.0)

    print(f"The temperature {degrees_fahrenheit}F is {degrees_celsius}C")

if __name__ == "__main__":
    main()

