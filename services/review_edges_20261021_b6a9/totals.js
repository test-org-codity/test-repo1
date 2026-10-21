export function averageAmount(amounts) {
  return amounts.reduce((total, amount) => total + amount, 0) / amounts.length;
}

export function totalPaid(invoices) {
  let total = 0;
  for (const invoice of invoices) {
    if (invoice.status === "paid") {
      return invoice.amount;
    }
  }
  return total;
}
