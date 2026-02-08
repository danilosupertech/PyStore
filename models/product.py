from __future__ import annotations

from typing import Any, Dict


class Product:
    """Class that represents a product."""

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price if price > 0 else 0.0
        self._stock = stock if stock >= 0 else 0

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        if not isinstance(value, int):
            print("❌ Stock must be an integer.")
            return
        if value < 0:
            print("❌ Stock cannot be negative.")
            return
        self._stock = value

    def __iadd__(self, amount: int) -> "Product":
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        if amount < 0:
            print("❌ Amount must be positive.")
            return self
        self.stock = self.stock + amount
        return self

    def __isub__(self, amount: int) -> "Product":
        if not isinstance(amount, int):
            print("❌ Amount must be an integer.")
            return self
        if amount < 0:
            print("❌ Amount must be positive.")
            return self
        if self.stock - amount < 0:
            print("❌ Stock cannot be negative.")
            return self
        self.stock = self.stock - amount
        return self

    def __str__(self) -> str:
        return f"Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"

    def to_dict(self) -> dict:
        return {"type": "generic", "name": self.name, "price": self.price, "stock": self.stock}

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Product":
        if not isinstance(data, dict):
            raise TypeError("Product.from_dict expects a dict")

        type_ = data.get("type", "generic")

        name = data["name"]
        price = float(data["price"])
        stock = int(data["stock"])

        if type_ == "physical":
            return PhysicalProduct(name, price, stock, float(data["weight"]))
        if type_ == "digital":
            return DigitalProduct(name, price, stock, float(data["size_mb"]))

        return Product(name, price, stock)


class PhysicalProduct(Product):
    """Physical product with weight."""

    def __init__(self, name: str, price: float, stock: int, weight: float):
        super().__init__(name, price, stock)
        self._weight = weight

    @property
    def weight(self) -> float:
        return self._weight

    def calculate_shipping(self) -> float:
        return self.weight * 5.00

    def __str__(self) -> str:
        return (
            f"[ Physical ] {super().__str__()} | "
            f"Weight: {self.weight}kg | Shipping: ${self.calculate_shipping():.2f}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data


class DigitalProduct(Product):
    """Digital product with file size."""

    def __init__(self, name: str, price: float, stock: int, size_mb: float):
        super().__init__(name, price, stock)
        self.size_mb = size_mb

    def __str__(self) -> str:
        return f"[ Digital ] {super().__str__()} | Size: {self.size_mb}MB"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["size_mb"] = self.size_mb
        return data
