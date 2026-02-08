
# 🛒 PyStore — CLI Store Management System (Python)

PyStore is a **Python-based CLI (Command Line Interface) store management system** designed to demonstrate solid foundations in **Object-Oriented Programming**, **Clean Architecture**, and **separation of concerns**, with **JSON persistence** as infrastructure.

This project goes beyond a simple CRUD example: it was **intentionally refactored to avoid “God classes/modules”**, making responsibilities explicit and the codebase easy to evolve.

It is an excellent **portfolio project for junior–mid Python developers**, and a strong base for future expansion into **APIs, payment systems, or web frontends**.

---

## 🚀 Key Features

### 📦 Product Catalog
- Generic, Physical, and Digital products
- Real-time stock management
- Automatic shipping calculation for physical products
- Factory-based reconstruction from JSON (`Product.from_dict`)

### 🛒 Shopping Cart
- Dedicated `Cart` domain model
- Add / remove items (partial or full)
- Frozen item price at add time
- Automatic stock reservation and restoration

### 🧾 Order Lifecycle
- Explicit states: `OPEN → PAID → CANCELED`
- Order owns a Cart (composition)
- Stock restoration on cancellation
- Immutable order history records

### 💾 Persistence (JSON)
- `inventory.json` for products
- `orders.json` for order history
- Repositories responsible only for I/O
- Fault-tolerant loading and validation

### 🧠 Clean Architecture
- No “God classes”
- Clear boundaries between:
  - Domain (models)
  - Infrastructure (repositories)
  - Application logic (services)
  - Interface (CLI)
- Ready for future integrations (payments, APIs, DBs)

---

## 🧱 Project Structure

```
PyStore/
│
├── main.py                     # CLI entry point (UI only)
├── inventory.json              # Product catalog (persistent)
├── orders.json                 # Order history
│
├── models/                     # Domain layer (business rules)
│   ├── product.py              # Product hierarchy + factory
│   ├── cart.py                 # Shopping cart logic
│   ├── order.py                # Order lifecycle
│   └── catalog.py              # In-memory catalog
│
├── repositories/               # Infrastructure (persistence)
│   ├── inventory_repo.py       # inventory.json I/O
│   └── orders_repo.py          # orders.json I/O
│
└── services/                   # Application services
    └── store_service.py        # Use-case orchestration
```

---

## 🧩 Architectural Decisions (What & Why)

### 1️⃣ Cart separated from Order
**What:**  
- Introduced a `Cart` model independent from `Order`.

**Why:**  
- Avoided a “God Order” class.
- Isolated cart logic (add/remove/total).
- Makes pricing, discounts, and persistence easier to evolve.

---

### 2️⃣ Services Layer (`StoreService`)
**What:**  
- Centralized application flow in a service.

**Why:**  
- Keeps `main.py` thin (UI only).
- Prevents business logic leakage into CLI.
- Simplifies testing and future API reuse.

---

### 3️⃣ Repository Pattern
**What:**  
- `InventoryRepository` and `OrdersRepository` handle JSON only.

**Why:**  
- Persistence is infrastructure, not business logic.
- Enables easy migration to SQLite/PostgreSQL later.
- Keeps domain models pure and reusable.

---

### 4️⃣ Factory Method in Domain (`Product.from_dict`)
**What:**  
- Object reconstruction moved into the Product model.

**Why:**  
- Prevents `if/else` explosion in repositories.
- Keeps knowledge of product types inside the domain.
- Aligns with Domain-Driven Design principles.

---

### 5️⃣ Explicit Order Lifecycle
**What:**  
- Orders move through well-defined states.

**Why:**  
- Prevents invalid operations.
- Makes payment integration straightforward.
- Improves correctness and readability.

---

## ▶️ How to Run

### Requirements
- Python **3.10+**
- Linux / macOS / WSL recommended

### Run the application

```bash
python3 main.py
```

---

## 📋 CLI Menu

```
1. View Catalog
2. New Order
3. Add Item
4. View Cart
5. Remove Item
6. Cancel Order
7. Finish Order (Checkout)
8. View Order History
0. Exit
```

---

## 🛠 Example Use Case

1. Start the application
2. Catalog is loaded or seeded automatically
3. Create a new order
4. Add or remove items from the cart
5. Checkout (order becomes PAID)
6. Order is persisted to `orders.json`

---

## 🧪 Testing Readiness

The architecture supports:
- Unit testing of domain models (Cart, Order, Product)
- Mocking repositories for service tests
- Future test automation with `pytest` or `unittest`

---

## 📈 Possible Improvements

- Persist open carts
- Add discounts, coupons, and taxes
- Integrate payment gateways
- Replace JSON with a relational database
- Expose REST API (FastAPI)
- Authentication and roles
- Web or mobile frontend

---

## 👨‍💻 Author

**Danilo Côrtes Gonçalves**  
Python Backend Developer | Software Engineering Student  
📍 Porto, Portugal  

- LinkedIn: https://www.linkedin.com/in/daniloctech
- GitHub: (add repository link)

---

## ⭐ Why This Project Matters

PyStore demonstrates **engineering thinking**, not just Python syntax.

It shows:
- Clean separation of responsibilities
- Scalable design decisions
- Real-world business rules
- Professional-level refactoring discipline

Ideal as a **portfolio project**, interview discussion topic, or foundation for production systems.
