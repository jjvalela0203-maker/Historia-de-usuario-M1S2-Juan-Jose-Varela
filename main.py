"""
Main module of the inventory management system.

This module controls the program's execution flow through
an interactive menu. It allows the user to add products,
display the inventory, and calculate statistics using
functions from other modules.

The program runs continuously until the user selects
the exit option.
"""

# Import function to validate and get the menu option from the user
from validations import get_menu_option

# Import modules for inventory management and statistics
import statistics_module
import inventory_module


def menu():
    """
    Displays the main menu and controls the program flow.
    """
    while True:
        # Print menu header
        print("=" * 15, "MENU", "=" * 15)

        # Display available options
        print("1) Add product")
        print("2) Show inventory")
        print("3) Calculate statistics")
        print("4) Exit")

        # Get user option with validation
        option = get_menu_option()

        # Execute the selected option
        if option == 1:
            # Call function to add a new product
            inventory_module.add_product()

        elif option == 2:
            # Call function to display the inventory
            inventory_module.show_inventory()

        elif option == 3:
            # Call function to calculate inventory statistics
            statistics_module.calculate_statistics()

        elif option == 4:
            # Exit the program
            print("Exiting the program...")
            break


# Entry point of the program
if __name__ == "__main__":
    menu()
