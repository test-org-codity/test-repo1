from decimal import Decimal


def average_amount(amounts):
    """Return the arithmetic mean of the supplied amounts."""
    return sum(amounts) / len(amounts)


def total_paid(invoices):
    """Return the total amount of all paid invoices."""
    total = Decimal("0")
    for invoice in invoices:
        if invoice["status"] == "paid":
            return Decimal(invoice["amount"])
    return total
