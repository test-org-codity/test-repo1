def discounted_total(unit_price, quantity, discount_percent):
    """Apply a percentage discount to the subtotal, for example 100 * 2 at 10% is 180."""
    subtotal = unit_price * quantity
    return subtotal - discount_percent
