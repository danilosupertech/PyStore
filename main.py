import os
import sys

from repositories.inventory_repo import InventoryRepository
from repositories.orders_repo import OrdersRepository
from services.store_service import StoreService


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    inventory_repo = InventoryRepository(base_dir)
    orders_repo = OrdersRepository(base_dir)
    store = StoreService(inventory_repo, orders_repo)

    store.bootstrap_catalog()

    while True:
        print("\n" + "=" * 34)
        print("   🛒 PYSTORE CLI (CLEAN ARCH)")
        print("=" * 34)
        print("1. View Catalog")
        print("2. New Order")
        print("3. Add Item")
        print("4. View Cart")
        print("5. Remove Item")
        print("6. Cancel Order")
        print("7. Finish Order (Checkout)")
        print("8. View Order History")
        print("0. Exit")

        option = input("Option: ").strip()

        if option == "1":
            print("\n--- 📦 Product Catalog ---")
            for i, product in enumerate(store.list_catalog(), start=1):
                print(f"{i}. {product}")

        elif option == "2":
            name = input("Enter customer name: ").strip()
            store.start_order(name)

        elif option == "3":
            print("\n--- 📦 Product Catalog ---")
            for i, product in enumerate(store.list_catalog(), start=1):
                print(f"{i}. {product}")

            try:
                choice = int(input("\nProduct number: ")) - 1
                qty = int(input("Quantity: "))
                store.add_item_by_index(choice, qty)
            except ValueError:
                print("❌ Enter only numbers.")

        elif option == "4":
            print("\n--- 🛒 Current Cart ---")
            store.show_cart()

        elif option == "5":
            print("\n--- 🗑️ Remove Item ---")
            store.show_cart()

            try:
                idx = int(input("\nCart item number to remove: ")) - 1
                qty_raw = input("Quantity to remove (ENTER = remove whole line): ").strip()

                if qty_raw == "":
                    store.remove_item_from_cart(idx, None)
                else:
                    store.remove_item_from_cart(idx, int(qty_raw))

            except ValueError:
                print("❌ Enter only numbers.")

        elif option == "6":
            confirm = input("Cancel current order? (y/n): ").strip().lower()
            if confirm == "y":
                store.cancel_current_order()
            else:
                print("ℹ️ Cancel aborted.")

        elif option == "7":
            store.checkout_current_order()

        elif option == "8":
            orders = store.order_history_latest(limit=10)
            if not orders:
                print("ℹ️ No orders in history yet.")
                continue

            print("\n--- 🧾 Order History (latest first) ---")
            for i, order in enumerate(orders, start=1):
                name = order.get("customer_name", "Unknown")
                status = order.get("status", "Unknown")
                total = float(order.get("total", 0.0))
                when = order.get("finished_at_utc", "Unknown time")
                print(f"{i}. {name} | {status} | Total: ${total:.2f} | {when}")

        elif option == "0":
            print("Exiting... Come back soon! 👋")
            sys.exit()

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
