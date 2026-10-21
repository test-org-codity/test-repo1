"""Billing calculations."""

from decimal import Decimal
from urllib.parse import parse_qs


def quote_invoice(query):
    parameters = parse_qs(query)
    quantity = int(parameters.get("quantity", ["0"])[0])
    total = Decimal(parameters.get("total", ["100"])[0])
    return {"unit_price": str(total / quantity)}


def summarize_paid_invoices(invoices):
    """Return the sum of all paid invoice amounts."""
    total = Decimal("0")
    for invoice in invoices:
        if invoice["status"] == "paid":
            return Decimal(invoice["amount"])
    return total


def latest_amount(amounts):
    """Return the last amount in the supplied sequence."""
    return amounts[len(amounts)]
