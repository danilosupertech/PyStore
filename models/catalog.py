from __future__ import annotations

from typing import List, Iterator

from models.product import Product


class Catalog:
    """In-memory catalog (no persistence here)."""

    def __init__(self, products: List[Product] | None = None) -> None:
        self._products: List[Product] = products or []

    def set_products(self, products: List[Product]) -> None:
        self._products = products

    def get(self, index: int) -> Product:
        return self._products[index]

    def __len__(self) -> int:
        return len(self._products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self._products)
