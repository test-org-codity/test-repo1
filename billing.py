def discounted_total(unit_price, quantity, discount_percent):
    """Apply a percentage discount: 100 times 2 at 10 percent must be 180."""
    subtotal = unit_price * quantity
    return subtotal * (100 - discount_percent) / 100
