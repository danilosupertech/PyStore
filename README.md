# 🛒 PyStore - E-commerce Backend System (CLI)

> **Modular E-commerce Backend (CLI) built with Python. Demonstrates advanced OOP patterns including Composition, Aggregation, Inheritance, and strict Encapsulation.**

---

PyStore is a backend logic simulation for an e-commerce platform, built entirely in **Python**. This project was architected to demonstrate a deep understanding of **Object-Oriented Analysis and Design (OOAD)**, specifically focusing on the relationships between objects (Composition vs. Aggregation).

## 🎯 Technical Objectives

Unlike simple scripts, PyStore showcases how to structure a scalable application using:

* **Composition (Strong Relationship):** Implementation of `Order` and `OrderItem`. If an Order is deleted, its Items cease to exist conceptually.
* **Aggregation (Weak Relationship):** Implementation of `Order` and `Customer`. A Customer persists independently of their Orders.
* **Polymorphism:** Unified interface for `PhysicalProduct` (shipping logic) and `DigitalProduct` (download logic).
* **Encapsulation:** Strict control over `_stock` and `_price` attributes to prevent invalid business states.

## 🛠️ Stack & Standards

* **Language:** Python 3.10+
* **Typing:** PEP 484 Type Hints (`List`, `Optional`, custom types).
* **Documentation:** PEP 257 Docstrings for all classes and business methods.
* **Style:** Adherence to PEP 8 coding conventions.

## 📂 Architecture Overview

The system is designed with a clear separation of responsibilities. Below is the class relationship diagram:

```mermaid
classDiagram
    class Product {
        +update_price()
        +reduce_stock()
    }
    class Order {
        +add_item()
        +finish_order()
    }
    class OrderItem {
        -quantity
        -unit_price
        +calculate_subtotal()
    }
    class Customer {
        +name
        +email
    }
    
    Order *-- OrderItem : Composition (Has-a)
    Order o-- Customer : Aggregation (Has-a)
    Product <|-- PhysicalProduct : Inheritance
    Product <|-- DigitalProduct : Inheritance
