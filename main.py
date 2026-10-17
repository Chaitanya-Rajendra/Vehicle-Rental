from abc import ABC, abstractmethod

# ==========================================
# 1. VEHICLE PARENT CLASS
# ==========================================

class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.__status = "Available"

    @property
    def status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    @abstractmethod
    def get_type(self):
        pass

    def display_info(self):
        print(
            f"ID: {self.vehicle_id} | "
            f"Type: {self.get_type()} | "
            f"Brand: {self.brand} | "
            f"Model: {self.model} | "
            f"Rent: Rs.{self.rent_per_day}/day | "
            f"Status: {self.status}"
        )


# ==========================================
# 2. CHILD CLASSES
# ==========================================

class Car(Vehicle):

    def get_type(self):
        return "Car"


class Bike(Vehicle):

    def get_type(self):
        return "Bike"


class Truck(Vehicle):

    def get_type(self):
        return "Truck"


# ==========================================
# 3. CUSTOMER CLASS
# ==========================================

class Customer:

    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def display_info(self):
        print(
            f"ID: {self.customer_id} | "
            f"Name: {self.name} | "
            f"Phone: {self.phone}"
        )


# ==========================================
# 4. RENTAL CLASS
# ==========================================

class Rental:

    next_rental_id = 1

    def __init__(self, customer, vehicle, days):
        self.rental_id = Rental.next_rental_id
        Rental.next_rental_id += 1

        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.daily_rate = vehicle.rent_per_day
        self.late_fee_per_day = 300
        self.status = "Active"
        self.actual_days = 0
        self.total_bill = 0

    def calculate_bill(self, actual_days):
        rental_charge = self.daily_rate * self.days

        extra_days = max(0, actual_days - self.days)
        late_fee = extra_days * self.late_fee_per_day

        self.total_bill = rental_charge + late_fee
        self.actual_days = actual_days

        return self.total_bill

    def display_info(self):
        print(
            f"Rental ID: {self.rental_id} | "
            f"Customer: {self.customer.name} | "
            f"Vehicle: {self.vehicle.vehicle_id} | "
            f"Booked Days: {self.days} | "
            f"Status: {self.status}"
        )

        if self.status == "Returned":
            print(f"Final Bill: Rs.{self.total_bill}")


# ==========================================
# 5. VEHICLE RENTAL MANAGEMENT SYSTEM
# ==========================================

class RentalSystem:

    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.rentals = []

        self.load_sample_vehicles()

    # --------------------------------------
    # SAMPLE VEHICLES
    # --------------------------------------

    def load_sample_vehicles(self):
        self.vehicles.extend([
            Car("C101", "Toyota", "Innova", 2500),
            Car("C102", "Honda", "City", 2000),
            Car("C103", "Hyundai", "Creta", 2200),
            Bike("B101", "Yamaha", "R15", 800),
            Bike("B102", "Royal Enfield", "Classic 350", 1000),
            Bike("B103", "Honda", "Activa", 500),
            Truck("T101", "Tata", "Ace", 3500),
            Truck("T102", "Ashok Leyland", "Dost", 4000)
        ])

    # --------------------------------------
    # HELPER METHODS
    # --------------------------------------

    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():
                return vehicle

        return None

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id.lower() == customer_id.lower():
                return customer

        return None

    def find_rental(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental

        return None

    def get_integer(self, message, minimum=1):
        while True:
            try:
                value = int(input(message))

                if value < minimum:
                    print(f"Enter a number greater than or equal to {minimum}.")
                    continue

                return value

            except ValueError:
                print("Invalid input. Enter a whole number.")

    # --------------------------------------
    # CUSTOMER MANAGEMENT
    # --------------------------------------

    def register_customer(self):
        print("\n--- Customer Registration ---")

        customer_id = input("Enter customer ID: ").strip()

        if not customer_id:
            print("Customer ID cannot be empty.")
            return

        if self.find_customer(customer_id):
            print("Customer ID already exists.")
            return

        name = input("Enter customer name: ").strip()
        phone = input("Enter phone number: ").strip()

        if not name or not phone:
            print("Name and phone number are required.")
            return

        customer = Customer(customer_id, name, phone)
        self.customers.append(customer)

        print("Customer registered successfully!")

    def view_customers(self):
        print("\n--- Registered Customers ---")

        if not self.customers:
            print("No customers registered.")
            return

        for customer in self.customers:
            customer.display_info()

    # --------------------------------------
    # VEHICLE MANAGEMENT
    # --------------------------------------

    def view_all_vehicles(self):
        print("\n--- Complete Vehicle List ---")

        if not self.vehicles:
            print("No vehicles registered.")
            return

        for vehicle in self.vehicles:
            vehicle.display_info()

    def view_available_vehicles(self):
        print("\n--- Available Vehicles ---")

        found = False

        for vehicle in self.vehicles:
            if vehicle.status == "Available":
                vehicle.display_info()
                found = True

        if not found:
            print("No vehicles are currently available.")

    def search_vehicle(self):
        print("\n--- Search Vehicles ---")
        print("1. Search by vehicle ID")
        print("2. Search by vehicle type")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            vehicle_id = input("Enter vehicle ID: ").strip()
            vehicle = self.find_vehicle(vehicle_id)

            if vehicle:
                vehicle.display_info()
            else:
                print("Vehicle not found.")

        elif choice == "2":
            vehicle_type = input(
                "Enter type (Car/Bike/Truck): "
            ).strip().lower()

            if vehicle_type not in ["car", "bike", "truck"]:
                print("Invalid vehicle type.")
                return

            found = False

            for vehicle in self.vehicles:
                if vehicle.get_type().lower() == vehicle_type:
                    vehicle.display_info()
                    found = True

            if not found:
                print("No vehicles found for this type.")

        else:
            print("Invalid choice.")

    def add_vehicle(self):
        print("\n--- Add New Vehicle ---")
        print("1. Car")
        print("2. Bike")
        print("3. Truck")

        choice = input("Select vehicle type: ").strip()

        vehicle_classes = {
            "1": Car,
            "2": Bike,
            "3": Truck
        }

        vehicle_class = vehicle_classes.get(choice)

        if vehicle_class is None:
            print("Invalid vehicle type.")
            return

        vehicle_id = input("Enter vehicle ID: ").strip()

        if not vehicle_id:
            print("Vehicle ID cannot be empty.")
            return

        if self.find_vehicle(vehicle_id):
            print("Vehicle ID already exists.")
            return

        brand = input("Enter brand: ").strip()
        model = input("Enter model: ").strip()

        if not brand or not model:
            print("Brand and model are required.")
            return

        rent_per_day = self.get_integer(
            "Enter rent per day: Rs.", 1
        )

        vehicle = vehicle_class(
            vehicle_id, brand, model, rent_per_day
        )

        self.vehicles.append(vehicle)

        print("Vehicle added successfully!")

    # --------------------------------------
    # RENTAL BOOKING
    # --------------------------------------

    def rent_vehicle(self):
        print("\n--- Rent a Vehicle ---")

        customer_id = input("Enter customer ID: ").strip()
        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found. Register first.")
            return

        self.view_available_vehicles()

        vehicle_id = input(
            "\nEnter vehicle ID to rent: "
        ).strip()

        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status != "Available":
            print("This vehicle is not available.")
            return

        days = self.get_integer("Enter rental days: ")

        rental = Rental(customer, vehicle, days)

        vehicle.set_status("Rented")
        self.rentals.append(rental)

        print("\nBooking successful!")
        print("Rental ID:", rental.rental_id)
        print("Customer:", customer.name)
        print("Vehicle:", vehicle.brand, vehicle.model)
        print("Booked days:", days)
        print("Daily rate: Rs.", vehicle.rent_per_day)
        print("Estimated rental charge: Rs.", days * vehicle.rent_per_day)

    # --------------------------------------
    # RETURN VEHICLE AND BILLING
    # --------------------------------------

    def return_vehicle(self):
        print("\n--- Return Vehicle ---")

        rental_id = self.get_integer("Enter rental ID: ")
        rental = self.find_rental(rental_id)

        if rental is None:
            print("Rental record not found.")
            return

        if rental.status != "Active":
            print("This rental has already been completed.")
            return

        actual_days = self.get_integer(
            "Enter actual rental days: "
        )

        total_bill = rental.calculate_bill(actual_days)

        rental.status = "Returned"
        rental.vehicle.set_status("Available")

        extra_days = max(0, actual_days - rental.days)
        rental_charge = rental.daily_rate * rental.days
        late_fee = extra_days * rental.late_fee_per_day

        print("\n========== FINAL BILL ==========")
        print("Rental ID:", rental.rental_id)
        print("Customer:", rental.customer.name)
        print("Vehicle:", rental.vehicle.brand, rental.vehicle.model)
        print("Booked days:", rental.days)
        print("Actual days:", actual_days)
        print("Rental charge: Rs.", rental_charge)
        print("Extra days:", extra_days)
        print("Late fee: Rs.", late_fee)
        print("TOTAL BILL: Rs.", total_bill)
        print("================================")

        print("Vehicle returned successfully!")

    # --------------------------------------
    # RENTAL HISTORY
    # --------------------------------------

    def view_rental_history(self):
        print("\n--- Rental History ---")

        if not self.rentals:
            print("No rental records found.")
            return

        for rental in self.rentals:
            rental.display_info()

    def view_active_rentals(self):
        print("\n--- Active Rentals ---")

        found = False

        for rental in self.rentals:
            if rental.status == "Active":
                rental.display_info()
                found = True

        if not found:
            print("No active rentals.")

    # --------------------------------------
    # VEHICLE MAINTENANCE
    # --------------------------------------

    def send_for_maintenance(self):
        print("\n--- Vehicle Maintenance ---")

        vehicle_id = input("Enter vehicle ID: ").strip()
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status != "Available":
            print("Only available vehicles can be sent for maintenance.")
            return

        vehicle.set_status("Maintenance")

        print("Vehicle marked for maintenance.")

    def complete_maintenance(self):
        print("\n--- Complete Maintenance ---")

        vehicle_id = input("Enter vehicle ID: ").strip()
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status != "Maintenance":
            print("This vehicle is not under maintenance.")
            return

        vehicle.set_status("Available")

        print("Maintenance completed.")
        print("Vehicle is now available for rental.")

    # --------------------------------------
    # ADMIN DASHBOARD
    # --------------------------------------

    def dashboard(self):
        print("\n========== ADMIN DASHBOARD ==========")

        total_vehicles = len(self.vehicles)
        available = 0
        rented = 0
        maintenance = 0

        for vehicle in self.vehicles:
            if vehicle.status == "Available":
                available += 1
            elif vehicle.status == "Rented":
                rented += 1
            elif vehicle.status == "Maintenance":
                maintenance += 1

        completed_rentals = 0
        active_rentals = 0
        total_revenue = 0

        for rental in self.rentals:
            if rental.status == "Returned":
                completed_rentals += 1
                total_revenue += rental.total_bill
            else:
                active_rentals += 1

        print("Total vehicles:", total_vehicles)
        print("Available vehicles:", available)
        print("Rented vehicles:", rented)
        print("Vehicles in maintenance:", maintenance)
        print("Registered customers:", len(self.customers))
        print("Total bookings:", len(self.rentals))
        print("Active rentals:", active_rentals)
        print("Completed rentals:", completed_rentals)
        print("Recorded revenue: Rs.", total_revenue)

        print("=====================================")

    # --------------------------------------
    # MAIN MENU
    # --------------------------------------

    def run(self):
        while True:
            print("\n========== VEHICLE RENTAL SYSTEM ==========")
            print("1.  Register Customer")
            print("2.  View Customers")
            print("3.  View All Vehicles")
            print("4.  View Available Vehicles")
            print("5.  Search Vehicles")
            print("6.  Add New Vehicle")
            print("7.  Rent a Vehicle")
            print("8.  Return Vehicle and Generate Bill")
            print("9.  View Rental History")
            print("10. View Active Rentals")
            print("11. Send Vehicle for Maintenance")
            print("12. Complete Maintenance")
            print("13. Admin Dashboard")
            print("14. Exit")
            print("============================================")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.register_customer()

            elif choice == "2":
                self.view_customers()

            elif choice == "3":
                self.view_all_vehicles()

            elif choice == "4":
                self.view_available_vehicles()

            elif choice == "5":
                self.search_vehicle()

            elif choice == "6":
                self.add_vehicle()

            elif choice == "7":
                self.rent_vehicle()

            elif choice == "8":
                self.return_vehicle()

            elif choice == "9":
                self.view_rental_history()

            elif choice == "10":
                self.view_active_rentals()

            elif choice == "11":
                self.send_for_maintenance()

            elif choice == "12":
                self.complete_maintenance()

            elif choice == "13":
                self.dashboard()

            elif choice == "14":
                print("Thank you for using Vehicle Rental System!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 14.")


# ==========================================
# 6. START THE APPLICATION
# ==========================================

if __name__ == "__main__":
    system = RentalSystem()
    system.run()
