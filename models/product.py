"""Module that represents a product."""


class Product:
    """Class that represents a product."""

    def __init__(self, name: str, price: float, stock: int):
        """Initialize a product."""
        self.name = name
        self.price = price if price > 0 else 0.0
        self._stock = stock if stock >= 0 else 0

    @property
    def stock(self) -> int:
        """Product stock."""
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        """Update the product stock."""
        if not isinstance(value, int):
            print("❌ Stock must be an integer.")
            return
        if value < 0:
            print("❌ Stock cannot be negative.")
            return

        self._stock = value
        print(f"✅ Stock updated to {self.stock}")

    # Magic Methods (the += / -= trick)
    def __iadd__(self, amount: int):
        """Allows: product += 5"""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        self.stock = self.stock + amount  # calls the setter
        return self

    def __isub__(self, amount: int):
        """Allows: product -= 2"""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        self.stock = self.stock - amount  # calls the setter (blocks negative)
        return self

    def update_stock(self, amount: int) -> None:
        """Increase/decrease stock by a given amount."""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return
        self.stock = self.stock + amount  # setter will block negative totals
        print(f"✅ Stock updated to {self.stock}")
    
    def __str__(self) -> str:
        """Return a string with the product data."""
        return f"Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"

class PhysicalProduct(Product):
    """Class that represents a physical product with weight."""

    def __init__(self, name: str, price: float, stock: int, weight: float):
        """Initialize a physical product."""
        super().__init__(name, price, stock)
        self._weight = weight

    @property
    def weight(self) -> float:
        """Product weight."""
        return self._weight

    def __str__(self) -> str:
        """Return a string with the physical product data."""
        return f"[ Physical ] {super().__str__()} | Weight: {self.weight}kg | shipping: ${self.calculate_shipping():.2f}"

    def calculate_shipping(self) -> float:
        """Calculates shipping cost based on weight."""
        return self.weight * 5.00  # Example: $5.00 per kg

class DigitalProduct(Product):
    """Class that represents a digital product with file size."""

    def __init__(self, name: str, price: float, stock: int, size_mb: float):
        """Initialize a digital product."""
        super().__init__(name, price, stock)
        self.size_mb = size_mb

    def __str__(self) -> str:
        """Return a string with the digital product data."""
        return f"[ Digital ] {super().__str__()} | Size: {self.size_mb}MB"

if __name__ == "__main__":
    p1 = Product("Banana", 10.5, 40)
    p2 = PhisicalProduct("Book", 25.0, 10, 0.5)
    p3 = DigitalProduct("E-book", 15.0, 20, 10.5)
    print(p1)

    p1.update_stock(10)
    p1.update_stock(-60)

    print(p1)

    p1 -= 5
    print(p1)
    print(p2)