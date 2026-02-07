
# 🛒 PyStore — CLI Store Management System (Python)

PyStore is a **Python-based CLI (Command Line Interface) store management system** designed to demonstrate strong foundations in **Object-Oriented Programming**, **clean architecture**, and **data persistence** using JSON.

This project was built with a focus on **software design principles**, making it an excellent **portfolio project for junior–mid Python developers** and a solid base for future expansion into APIs or full-stack systems.

---

## 🚀 Key Features

- 📦 **Product Catalog**
  - Generic, Physical, and Digital products
  - Real-time stock management
  - Automatic shipping calculation for physical products

- 🛒 **Shopping Cart (Order)**
  - Add / remove items
  - Partial or full item removal
  - Automatic stock updates
  - Cart summary per customer

- 🧾 **Order Lifecycle**
  - OPEN → PAID → CANCELED states
  - Immutable price after item is added
  - Stock restoration on cancellation

- 💾 **Persistent Storage (JSON)**
  - `inventory.json` for products
  - `orders.json` for order history
  - Robust loading with validation

- 🧠 **Clean Architecture**
  - Separation of concerns
  - Domain-driven models
  - Repository-style catalog
  - CLI as interface layer only

---

## 🧱 Project Structure

```
PyStore/
│
├── main.py                 # CLI entry point
├── inventory.json          # Product catalog (persistent)
├── orders.json             # Order history (auto-generated)
│
└── models/
    ├── product.py          # Product domain models
    ├── order.py            # Order and cart logic
    ├── catalog.py          # Catalog repository
    └── database.py         # JSON persistence layer
```

---

## 🧩 Core Concepts Demonstrated

### Object-Oriented Programming (OOP)
- Encapsulation with properties
- Inheritance for product specialization
- Composition (Order → OrderItem)
- Operator overloading (`+=`, `-=`)
- Object state management

### Software Design
- Single Responsibility Principle (SRP)
- Separation of Interface / Domain / Persistence
- Factory-like object reconstruction from JSON
- Defensive programming and validation

### Persistence
- Manual serialization/deserialization
- JSON as lightweight database
- Fault-tolerant loading

---

## ▶️ How to Run

### Requirements
- Python **3.10+**
- Linux / macOS / WSL (recommended)

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
2. Load product catalog from `inventory.json`
3. Create an order for a customer
4. Add/remove items from the cart
5. Finalize the order
6. Persist order to `orders.json`

---

## 🧪 Testing

Basic unit tests validate:
- Order creation
- Item quantity aggregation
- Stock reduction
- Order completion

Tests are written using Python’s built-in `unittest` framework.

---

## 📈 Possible Improvements

- Save and restore open carts
- Apply discounts and coupons
- Support multiple concurrent carts
- Replace JSON with SQLite or PostgreSQL
- Expose REST API with FastAPI
- Add authentication and user roles
- Create a web frontend

---

## 👨‍💻 Author

**Danilo Côrtes Gonçalves**  
Python Backend Developer | Software Engineering Student  
📍 Porto, Portugal  

- LinkedIn: https://www.linkedin.com/in/daniloctech
- GitHub: (add your repository link here)

---

## ⭐ Why This Project Matters

This project shows **how to think like a software engineer**, not just how to write Python code.

It demonstrates:
- Real-world business rules
- Clean and scalable architecture
- Professional coding practices
- Readability and maintainability

Perfect as a **portfolio project**, technical interview discussion, or base for real applications.

---

Feel free to fork, improve, and adapt PyStore to your own needs.
