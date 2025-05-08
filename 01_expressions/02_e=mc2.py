def main():
    # Constant speed of light in meters per second
    C = 299792458

    while True:
        try:
            # Ask the user for mass input
            mass_input = input("Enter kilos of mass (or type 'exit' to quit): ")

            if mass_input.lower() == 'exit':
                print("Goodbye!")
                break

            # Convert input to float
            m = float(mass_input)

            # Calculate energy using E = m * C^2
            print("\ne = m * C^2\n")
            print(f"m = {m} kg")
            print(f"C = {C} m/s")

            E = m * C**2
            print(f"\n{E} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number or 'exit' to quit.\n")


if __name__ == '__main__':
    main()
