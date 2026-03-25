"""
Statistics module.

Allows calculation of basic inventory information such as the total value
of stored products and the number of registered products.
"""

# Import the inventory list from the inventory module
from inventory_module import inventory


def calculate_statistics():
    """
    Calculates the total inventory value and the number of registered products.
    """
    # Check if the inventory is empty
    if not inventory:
        print("There are no products to calculate statistics.\n")
        return

    # Calculate total inventory value (price * quantity for each product)
    total_value = sum(product["price"] * product["quantity"] for product in inventory)

    # Count the number of registered products
    registered_products_count = len(inventory)

    # Calculate total number of units
    total_units = sum(product["quantity"] for product in inventory)

    # Display statistics
    print("\n--- STATISTICS ---")
    print("Total inventory value:", total_value)
    print("Number of registered products:", registered_products_count)
    print("Total number of units:", total_units)
    print()
