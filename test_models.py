import unittest
from models.product import Product
from models.order import Order

class TestProduct(unittest.TestCase):
    def test_product_stock_update(self):
        p = Product("Test", 10.0, 5)
        p.stock = 8
        self.assertEqual(p.stock, 8)
        p.stock = -1  # Should not update
        self.assertEqual(p.stock, 8)
        p.stock = "abc"  # Should not update
        self.assertEqual(p.stock, 8)

    def test_product_iadd_isub(self):
        p = Product("Test", 10.0, 5)
        p += 3
        self.assertEqual(p.stock, 8)
        p -= 2
        self.assertEqual(p.stock, 6)
        p += "abc"  # Should not update
        self.assertEqual(p.stock, 6)

class TestOrder(unittest.TestCase):
    def test_order_add_item(self):
        p = Product("Test", 10.0, 10)
        order = Order("Customer")
        order.add_item(p, 2)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items[0].quantity, 2)
        order.add_item(p, 3)
        self.assertEqual(order.items[0].quantity, 5)

    def test_order_total(self):
        p1 = Product("A", 5.0, 10)
        p2 = Product("B", 2.0, 10)
        order = Order("Customer")
        order.add_item(p1, 2)
        order.add_item(p2, 3)
        self.assertEqual(order.total, 5.0*2 + 2.0*3)

if __name__ == "__main__":
    unittest.main()
