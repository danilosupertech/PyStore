# 🛒 PyStore --- Clean Architecture Store Backend (Python)

PyStore is a Python-based store management system designed to
demonstrate clean architecture principles, domain-driven design, and
scalable backend foundations.

The first phase of the project uses **JSON-based persistence** for
simplicity and clarity.\
Future iterations will migrate to a relational database and expose a
RESTful API to support frontend applications and microservice-based
architectures.

------------------------------------------------------------------------

## 🎯 Project Vision

PyStore is structured to evolve into:

-   A REST API backend (FastAPI planned)
-   Database-driven system (SQLite → PostgreSQL)
-   Microservice-ready architecture
-   Consumable backend for any e-commerce frontend

The current CLI version focuses on correctness, separation of concerns,
and business rule modeling.

------------------------------------------------------------------------

## 🧰 Tech Stack (Phase 1)

-   Python 3.10+
-   Object-Oriented Programming
-   Clean Architecture
-   Repository Pattern
-   JSON Persistence
-   CLI Interface

------------------------------------------------------------------------

## 🚀 Core Features

### 📦 Product Catalog

-   Generic, Physical, and Digital products
-   Real-time stock management
-   Automatic shipping calculation for physical products
-   Factory-based reconstruction (`Product.from_dict`)

### 🛒 Shopping Cart

-   Dedicated Cart domain model
-   Add/remove items (partial or full)
-   Price frozen at add time
-   Automatic stock reservation & restoration

### 🧾 Order Lifecycle

-   Explicit states: `OPEN → PAID → CANCELED`
-   Order owns a Cart (composition)
-   Stock restoration on cancellation
-   Immutable order history records

### 💾 Persistence (Current Phase)

-   `inventory.json` for products
-   `orders.json` for order history
-   Repository layer responsible only for I/O
-   Fault-tolerant loading and validation

------------------------------------------------------------------------

## 🧱 Architecture Overview

The system follows clear separation of responsibilities:

-   **Domain Layer (`models/`)** → Business rules and core entities
-   **Infrastructure Layer (`repositories/`)** → Persistence (JSON)
-   **Application Layer (`services/`)** → Use-case orchestration
-   **Interface Layer (`main.py`)** → CLI interaction only

This prevents "God classes" and keeps the codebase extensible and
maintainable.

------------------------------------------------------------------------

## 📁 Project Structure

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

------------------------------------------------------------------------

## ▶️ How to Run

### Requirements

-   Python 3.10+
-   Linux / macOS / WSL recommended

### Run the application

``` bash
python3 main.py
```

------------------------------------------------------------------------

## 🔮 Roadmap (Next Phases)

-   Replace JSON with relational database (SQLite / PostgreSQL)
-   Introduce REST API layer (FastAPI)
-   Authentication & authorization
-   Payment integration
-   Frontend consumption via microservices
-   Containerization (Docker)
-   CI/CD pipeline

------------------------------------------------------------------------

## 🧠 Why This Project Matters

PyStore demonstrates:

-   Clean separation of responsibilities
-   Domain modeling beyond simple CRUD
-   Scalable architectural thinking
-   Readiness for API and database evolution
-   Backend-first mindset suitable for real-world systems

It serves as a strong portfolio foundation for backend Python
development and future microservice-oriented systems.

------------------------------------------------------------------------

## 👨‍💻 Author

Danilo Côrtes Gonçalves\
Python Backend Developer\
Porto, Portugal

LinkedIn: https://www.linkedin.com/in/daniloctech GitHub:
https://github.com/danilosupertech
