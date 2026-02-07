"""
catalog.py
Module that manages a catalog of products.

"""
from __future__ import annotations
from typing import List, Iterator

from models.product import Product, PhysicalProduct, DigitalProduct
from models.database import load_catalog, save_catalog


class Catalog:
    """Manages products in memory and persists them to disk."""

    def __init__(self) -> None:
        self._products: List[Product] = []

    def load_or_seed(self) -> None:
        """Load from file; if empty, seed default products and save."""
        self._products = load_catalog()

        if not self._products:
            print("⚠️ No file found. Creating initial data...")
            self._products = [
                PhysicalProduct("iPhone 15", 900.00, 10, 0.2),
                PhysicalProduct("Notebook Dell", 1500.00, 5, 2.5),
                DigitalProduct("Python Ebook", 29.90, 1000, 15.0),
            ]
            self.save()

    def save(self) -> None:
        """Persist catalog to disk."""
        save_catalog(self._products)

    def get(self, index: int) -> Product:
        """Get product by index."""
        return self._products[index]

    def __len__(self) -> int:
        return len(self._products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self._products)
