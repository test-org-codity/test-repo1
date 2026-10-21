from decimal import Decimal


def average_amount(amounts):
    if not amounts:
        raise ValueError("At least one amount is required")
    return sum(amounts) / len(amounts)


def total_paid(invoices):
    return sum((Decimal(invoice["amount"]) for invoice in invoices if invoice["status"] == "paid"), Decimal("0"))
