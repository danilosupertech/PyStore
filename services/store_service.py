from __future__ import annotations

from typing import Optional, List, Dict, Any

from models.catalog import Catalog
from models.order import Order
from models.product import Product
from repositories.inventory_repo import InventoryRepository, default_seed_products
from repositories.orders_repo import OrdersRepository


class StoreService:
    """
    Orchestrates application use-cases.
    Keeps main.py small and keeps models/repositories focused.
    """

    def __init__(self, inventory_repo: InventoryRepository, orders_repo: OrdersRepository):
        """ Initi inventary"""
        self.inventory_repo = inventory_repo
        self.orders_repo = orders_repo
        self.catalog = Catalog()
        self.current_order: Optional[Order] = None

    def bootstrap_catalog(self) -> None:
        products = self.inventory_repo.load()

        if not self.inventory_repo.exists():
            print("⚠️ inventory.json not found. Creating initial data...")
        elif not products:
            print(
                "⚠️ inventory.json found, but empty/invalid. Recreating initial data...")

        if not products:
            products = default_seed_products()
            self.inventory_repo.save(products)

        self.catalog.set_products(products)

    def list_catalog(self) -> List[Product]:
        return list(self.catalog)

    def start_order(self, customer_name: str) -> None:
        if self.current_order and self.current_order.status == "OPEN":
            print(
                f"⚠️ There is already an open order for {self.current_order.customer_name}.")
            print("   Finish it, cancel it, or view the cart.")
            return

        name = customer_name.strip()
        if not name:
            print("❌ Customer name cannot be empty.")
            return

        self.current_order = Order(name)
        print(f"\n✅ Order started for {name}!")

    def show_cart(self) -> None:
        if not self.current_order:
            print("⚠️ No open order.")
            return
        print(self.current_order.summary())

    def add_item_by_index(self, product_index: int, qty: int) -> None:
        if not self.current_order:
            print("⚠️ Create an order first.")
            return
        if self.current_order.status != "OPEN":
            print("❌ You cannot modify a closed order.")
            return

        if not (0 <= product_index < len(self.catalog)):
            print("❌ Invalid product.")
            return

        product = self.catalog.get(product_index)
        self.current_order.cart.add_item(product, qty)
        self.inventory_repo.save(self.list_catalog())

    def remove_item_from_cart(self, cart_index: int, qty: int | None) -> None:
        if not self.current_order:
            print("⚠️ No open order.")
            return
        if self.current_order.status != "OPEN":
            print("❌ You cannot modify a closed order.")
            return
        if self.current_order.cart.is_empty():
            print("🛒 Cart is empty.")
            return

        self.current_order.cart.remove_item(cart_index, qty)
        self.inventory_repo.save(self.list_catalog())

    def cancel_current_order(self) -> None:
        if not self.current_order:
            print("⚠️ No open order.")
            return

        self.current_order.cancel()
        self.inventory_repo.save(self.list_catalog())
        self.current_order = None

    def checkout_current_order(self) -> None:
        if not self.current_order:
            print("⚠️ No order to finish.")
            return

        self.current_order.finish_order()
        if self.current_order.status == "PAID":
            self.orders_repo.append(self.current_order.to_record())
            self.inventory_repo.save(self.list_catalog())
            self.current_order = None

    def order_history_latest(self, limit: int = 10) -> List[Dict[str, Any]]:
        orders = self.orders_repo.load()
        return list(reversed(orders[-limit:]))
