"""
Inventory module.

Allows adding products to the inventory and displaying them on screen.
Each product contains name, price, and quantity.
"""

# Import validation functions
from validations import get_non_empty_text, get_positive_integer, get_positive_float


# Inventory list
inventory = []


def add_product():
    """
    Requests data from the user and adds a product to the inventory.
    """
    # Get product data with validation
    name = get_non_empty_text("Enter the product to register: ")
    quantity = get_positive_integer("Enter how many units you want to register: ")
    price = get_positive_float("Enter the unit price of the product: ")

    # Create product dictionary
    registered_product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add product to inventory
    inventory.append(registered_product)

    print("Product registered")


def show_inventory():
    """
    Displays all products stored in the inventory.
    """
    # Check if inventory is empty
    if not inventory:
        print("The inventory is empty")
    else:
        print("\n--- INVENTORY ---\n")

        # Iterate through products and display them
        for registered_product in inventory:
            print(
                "Product:", registered_product["name"],
                "| Price:", registered_product["price"],
                "| Quantity:", registered_product["quantity"], "\n")
