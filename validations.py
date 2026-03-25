"""
Validation module.

Contains functions to validate user input,
ensuring that entered values are correct and preventing
runtime errors caused by invalid data.
"""

def get_non_empty_text(message):
    """
    Requests text input from the user and validates that it is not empty.
    """
    while True:
        value = input(message).strip()
        if value:
            return value
        print("The input cannot be empty.")


def get_positive_integer(message):
    """
    Requests an integer and validates that it is greater than zero.
    """
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Enter an integer greater than 0.")
        except ValueError:
            print("Enter a valid integer.")


def get_positive_float(message):
    """
    Requests a decimal number and validates that it is greater than zero.
    """
    while True:
        try:
            text = input(message).strip().replace(",", ".")
            value = float(text)
            if value > 0:
                return value
            print("Enter a number greater than 0.")
        except ValueError:
            print("Enter a valid numeric value.")


def get_menu_option():
    """
    Requests a menu option and validates that it is between 1 and 4.
    """
    while True:
        try:
            option = int(input("Enter your option (1-4): "))
            if 1 <= option <= 4:
                return option
            print("Invalid option.")
        except ValueError:
            print("Enter a valid option.")
