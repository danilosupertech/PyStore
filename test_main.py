import unittest

from models.product import PhysicalProduct, DigitalProduct
from models.order import Order


class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.catalog = [
            PhysicalProduct("Test Phone", 100.0, 5, 0.5),
            DigitalProduct("Test Ebook", 10.0, 100, 5.0),
        ]
        self.order = Order("Test Customer")

    def test_add_item(self):
        self.order.add_item(self.catalog[0], 2)
        self.assertEqual(len(self.order.items), 1)
        self.assertEqual(self.order.items[0].quantity, 2)

        # add same product again
        self.order.add_item(self.catalog[0], 3)
        self.assertEqual(self.order.items[0].quantity, 5)

    def test_finish_order(self):
        self.order.add_item(self.catalog[0], 1)
        self.order.finish_order()
        self.assertEqual(self.order.status, "PAID")

    def test_stock_decreases_when_added(self):
        start_stock = self.catalog[0].stock
        self.order.add_item(self.catalog[0], 2)
        self.assertEqual(self.catalog[0].stock, start_stock - 2)


if __name__ == "__main__":
    unittest.main()
