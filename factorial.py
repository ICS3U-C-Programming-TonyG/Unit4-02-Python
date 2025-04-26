#!/usr/bin/env python3

# Author: Tony G

# Date: 2025-04-26

# Calculates the factorial of the input of the user


def main():
    # Initializations
    loop_counter = 0
    factorial_answer = 1

    # Get the user number
    try:
        user_number = int(input("Enter a positive number: "))
        print("")

        if user_number < 0:
            print("Please enter a non-negative whole number.")
            return

        # Mimics a do-while loop
        # Calculate the factorial of the user number using a loop
        while True:
            loop_counter += 1
            factorial_answer *= loop_counter
            print(f"Tracking {loop_counter} times through loop.")

            if loop_counter >= user_number:
                break

        print("")
        print(f"{user_number}! = {factorial_answer}")

    except ValueError:
        print("Invalid input. Please enter a valid whole number.")


if __name__ == "__main__":
    main()
