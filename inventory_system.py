# inventory_system.py

import logging

inventory = []

def add_item(name, quantity, price, log=None):
    """Add an item to the inventory."""
    if log is None:
        log = []
    if not isinstance(quantity, int) or not isinstance(price, (int, float)):
        raise ValueError("Quantity must be int and price must be numeric")
    log.append(f"Adding {name}")
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    logging.info(f"Item added: {name}")

def remove_item(name):
    """Remove an item from inventory by name."""
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            logging.info(f"Item removed: {name}")
            return
    logging.warning(f"Item not found: {name}")

def get_total_value():
    """Return total inventory value."""
    return sum(item['quantity'] * item['price'] for item in inventory)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    add_item("Book", 3, 100)
    add_item("Pen", 10, 5)
    print("Total value:", get_total_value())
