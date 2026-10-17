# 🚗 Vehicle Rental Management System

A menu-driven, console-based **Vehicle Rental Management System** written in Python using core **Object-Oriented Programming** principles. It manages cars, bikes and trucks, registers customers, handles bookings and returns, calculates bills with late fees, and gives admins a live dashboard.

No external libraries required, just Python 3.

---

## ✨ Features

- **Customer management**: register and view customers (duplicate IDs are rejected)
- **Vehicle management**: view all vehicles, view only available ones, search by ID or type, add new vehicles
- **Rentals**: book an available vehicle for a number of days
- **Returns & billing**: automatic final bill with late-fee calculation
- **Rental history**: view all rentals or only active ones
- **Maintenance**: send vehicles for maintenance and mark them available again
- **Admin dashboard**: fleet status, bookings and recorded revenue at a glance
- **Input validation**: handles empty input, invalid numbers and unknown IDs

---

## 🧠 OOP Concepts Demonstrated

| Concept | Where it's used |
|---|---|
| **Abstraction** | `Vehicle` is an abstract base class (`ABC`) with the abstract method `get_type()` |
| **Inheritance** | `Car`, `Bike` and `Truck` extend `Vehicle` |
| **Polymorphism** | Each subclass implements `get_type()`; `display_info()` works for any vehicle |
| **Encapsulation** | Vehicle status is private (`__status`), exposed via a `status` property and `set_status()` |
| **Composition** | `Rental` holds a `Customer` and a `Vehicle`; `RentalSystem` manages all collections |

---

## 🗂️ Class Overview

```
Vehicle (ABC)
├── Car
├── Bike
└── Truck

Customer
Rental          → links a Customer and a Vehicle, calculates the bill
RentalSystem    → menu, business logic and data storage
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher

### Run

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python main.py
```
---

## 📋 Menu

```
========== VEHICLE RENTAL SYSTEM ==========
1.  Register Customer
2.  View Customers
3.  View All Vehicles
4.  View Available Vehicles
5.  Search Vehicles
6.  Add New Vehicle
7.  Rent a Vehicle
8.  Return Vehicle and Generate Bill
9.  View Rental History
10. View Active Rentals
11. Send Vehicle for Maintenance
12. Complete Maintenance
13. Admin Dashboard
14. Exit
============================================
```

---

## 🚘 Sample Fleet

The system starts with these vehicles preloaded:

| ID | Type | Brand | Model | Rent/day |
|---|---|---|---|---|
| C101 | Car | Toyota | Innova | Rs.2500 |
| C102 | Car | Honda | City | Rs.2000 |
| C103 | Car | Hyundai | Creta | Rs.2200 |
| B101 | Bike | Yamaha | R15 | Rs.800 |
| B102 | Bike | Royal Enfield | Classic 350 | Rs.1000 |
| B103 | Bike | Honda | Activa | Rs.500 |
| T101 | Truck | Tata | Ace | Rs.3500 |
| T102 | Truck | Ashok Leyland | Dost | Rs.4000 |

---

## 💰 Billing Logic

```
Rental charge = daily rate × booked days
Extra days    = max(0, actual days − booked days)
Late fee      = extra days × Rs.300
Total bill    = rental charge + late fee
```

**Example:** Innova (Rs.2500/day) booked for 3 days, returned after 5 days:

- Rental charge = 2500 × 3 = Rs.7500
- Late fee = 2 × 300 = Rs.600
- **Total = Rs.8100**

Returning early does not reduce the charge; the customer pays for the booked days.

---

## 🔄 Vehicle Status Flow

```
Available ──rent──▶ Rented ──return──▶ Available
    │
    └──maintenance──▶ Maintenance ──complete──▶ Available
```

Only **Available** vehicles can be rented or sent for maintenance.

---

## 🖥️ Example Session

```
Enter your choice: 1
--- Customer Registration ---
Enter customer ID: CU01
Enter customer name: Rahul
Enter phone number: 9876543210
Customer registered successfully!

Enter your choice: 7
Enter customer ID: CU01
Enter vehicle ID to rent: C101
Enter rental days: 3

Booking successful!
Rental ID: 1
Estimated rental charge: Rs. 7500
```

---


---

## 🤝 Contributing

Contributions, issues and feature requests are welcome. Feel free to fork the repo and open a pull request.

## 📄 License

This project is licensed under the MIT License. Add a `LICENSE` file to your repository if you choose this license.

## 👤 Author

**D Chaitanya Rajendra**
GitHub: [@Chaitanya-Rajendra](https://github.com/Chaitanya-Rajendra)
