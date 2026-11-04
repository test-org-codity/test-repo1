import unittest
from billing import discounted_total

class BillingTest(unittest.TestCase):
    def test_percentage_discount(self):
        self.assertEqual(discounted_total(100, 2, 10), 180)
    def test_small_order(self):
        self.assertEqual(discounted_total(10, 3, 10), 27)
    def test_full_discount(self):
        self.assertEqual(discounted_total(100, 2, 100), 0)
