"""
product.py

Module that represents products.

"""
from __future__ import annotations


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
        """
        Update product stock.
        This setter is silent (no print) to avoid duplicated messages.
        """
        if not isinstance(value, int):
            print("❌ Stock must be an integer.")
            return
        if value < 0:
            print("❌ Stock cannot be negative.")
            return

        self._stock = value

    # Magic Methods (+= / -=)
    def __iadd__(self, amount: int) -> "Product":
        """Allows: product += 5"""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        self.stock = self.stock + amount
        return self

    def __isub__(self, amount: int) -> "Product":
        """Allows: product -= 2"""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        self.stock = self.stock - amount
        return self

    def update_stock(self, amount: int) -> None:
        """Increase/decrease stock by a given amount."""
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return

        new_value = self.stock + amount
        if new_value < 0:
            print("❌ Stock cannot be negative.")
            return

        self._stock = new_value
        print(f"✅ Stock updated to {self.stock}")

    def __str__(self) -> str:
        """Return a string with the product data."""
        return f"Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"

    def to_dict(self) -> dict:
        """Return a dictionary with the product data."""
        return {
            "type": "generic",
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
        }


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

    def calculate_shipping(self) -> float:
        """Calculate shipping cost based on weight."""
        return self.weight * 5.00  # Example: $5.00 per kg

    def __str__(self) -> str:
        """Return a string with the physical product data."""
        return (
            f"[ Physical ] {super().__str__()} | "
            f"Weight: {self.weight}kg | Shipping: ${self.calculate_shipping():.2f}"
        )

    def to_dict(self) -> dict:
        """Return a dictionary with the physical product data."""
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data


class DigitalProduct(Product):
    """Class that represents a digital product with file size."""

    def __init__(self, name: str, price: float, stock: int, size_mb: float):
        """Initialize a digital product."""
        super().__init__(name, price, stock)
        self.size_mb = size_mb

    def __str__(self) -> str:
        """Return a string with the digital product data."""
        return f"[ Digital ] {super().__str__()} | Size: {self.size_mb}MB"

    def to_dict(self) -> dict:
        """Return a dictionary with the digital product data."""
        data = super().to_dict()
        data["type"] = "digital"
        data["size_mb"] = self.size_mb
        return data
