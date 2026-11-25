
from abc import ABC, abstractmethod
import math


# ==================================================
# TASK 1 & 2: ABSTRACT CLASS AND ENCAPSULATION
# ==================================================

class Vehicle(ABC):
    """Abstract base class for all rental vehicles."""

    def __init__(self, vehicle_id, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__daily_rate = None

        # Set the daily rate using the validation setter
        self.set_daily_rate(daily_rate)

    # Getter method
    def get_daily_rate(self):
        return self.__daily_rate

    # Setter method
    def set_daily_rate(self, value):
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or value <= 0
        ):
            raise ValueError(
                "Daily rental rate must be a positive number."
            )

        self.__daily_rate = float(value)

    # Property getter
    @property
    def daily_rate(self):
        return self.__daily_rate

    # Property setter
    @daily_rate.setter
    def daily_rate(self, value):
        self.set_daily_rate(value)

    # Abstract method
    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    # Operator overloading: compare vehicles by daily rate
    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented

        return self.daily_rate < other.daily_rate


# ==================================================
# TASK 3 & 4: PASSENGER CAR CLASS
# ==================================================

class PassengerCar(Vehicle):
    """Represents a passenger rental car."""

    def __init__(self, vehicle_id, model, daily_rate, num_seats):
        super().__init__(vehicle_id, model, daily_rate)

        if (
            isinstance(num_seats, bool)
            or not isinstance(num_seats, int)
            or num_seats <= 0
        ):
            raise ValueError("Number of seats must be a positive integer.")

        self.num_seats = num_seats

    # Method overriding
    def calculate_rental_cost(self, days):
        if (
            isinstance(days, bool)
            or not isinstance(days, int)
            or days <= 0
        ):
            raise ValueError("Rental days must be a positive integer.")

        return (self.daily_rate * days) + (15.0 * self.num_seats)

    # Operator overloading: readable vehicle description
    def __str__(self):
        return (
            f"Passenger Car | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Seats: {self.num_seats} | "
            f"Daily Rate: ${self.daily_rate:.2f}"
        )


# ==================================================
# TASK 3 & 4: CARGO TRUCK CLASS
# ==================================================

class CargoTruck(Vehicle):
    """Represents a cargo truck rental vehicle."""

    def __init__(
        self, vehicle_id, model, daily_rate, cargo_capacity_tons
    ):
        super().__init__(vehicle_id, model, daily_rate)

        if (
            isinstance(cargo_capacity_tons, bool)
            or not isinstance(cargo_capacity_tons, (int, float))
            or not math.isfinite(cargo_capacity_tons)
            or cargo_capacity_tons <= 0
        ):
            raise ValueError(
                "Cargo capacity must be a positive number."
            )

        self.cargo_capacity_tons = float(cargo_capacity_tons)

    # Method overriding
    def calculate_rental_cost(self, days):
        if (
            isinstance(days, bool)
            or not isinstance(days, int)
            or days <= 0
        ):
            raise ValueError("Rental days must be a positive integer.")

        return (
            self.daily_rate * days
        ) + (50.0 * self.cargo_capacity_tons)

    # Operator overloading: readable vehicle description
    def __str__(self):
        return (
            f"Cargo Truck | ID: {self.vehicle_id} | "
            f"Model: {self.model} | "
            f"Capacity: {self.cargo_capacity_tons:.1f} tons | "
            f"Daily Rate: ${self.daily_rate:.2f}"
        )


# ==================================================
# TASK 4: POLYMORPHIC FLEET PROCESSING
# ==================================================

def generate_fleet_manifest(fleet_list, days):
    """
    Generate a rental manifest for a mixed fleet.

    The function uses polymorphism to calculate the rental
    cost of each vehicle without checking its specific type.
    """

    if (
        isinstance(days, bool)
        or not isinstance(days, int)
        or days <= 0
    ):
        raise ValueError("Rental days must be a positive integer.")

    print("\n========== LOGITRANS FLEET MANIFEST ==========")
    print(f"Rental Duration: {days} days")
    print("----------------------------------------------")

    total_revenue = 0.0

    for vehicle in fleet_list:

        # Polymorphism: calls the correct overridden method
        rental_cost = vehicle.calculate_rental_cost(days)

        # Calls the vehicle's overridden __str__ method
        print(str(vehicle))
        print(f"Rental Cost: ${rental_cost:.2f}")
        print("----------------------------------------------")

        total_revenue += rental_cost

    print(f"Total Fleet Rental Revenue: ${total_revenue:.2f}")
    print("========== END OF FLEET MANIFEST =============\n")


# ==================================================
# MAIN PROGRAM: OBJECT CREATION AND TESTING
# ==================================================

if __name__ == "__main__":

    print("LOGITRANS LOGISTICS FLEET MANAGEMENT SYSTEM")
    print("=" * 48)

    # 1. Create two passenger car objects
    car1 = PassengerCar("PC101", "Toyota Corolla", 80.0, 5)
    car2 = PassengerCar("PC102", "Honda Civic", 65.0, 4)

    # 2. Create two cargo truck objects
    truck1 = CargoTruck("CT201", "Volvo FH", 150.0, 12.0)
    truck2 = CargoTruck("CT202", "Tata Prima", 120.0, 8.0)

    # 3. Create a mixed fleet list
    fleet = [car1, truck1, car2, truck2]

    # 4. Test getter and setter methods
    print("\n--- TEST 1: ENCAPSULATION ---")

    print("Original Toyota Daily Rate:", car1.get_daily_rate())

    car1.set_daily_rate(85.0)

    print("Updated Toyota Daily Rate:", car1.get_daily_rate())

    # Test property access
    car1.daily_rate = 85.0
    print("Property Access Daily Rate:", car1.daily_rate)

    # 5. Test invalid daily rental rate
    print("\n--- TEST 2: INVALID RENTAL RATE ---")

    try:
        car1.set_daily_rate(-10)
    except ValueError as error:
        print("Validation Error:", error)

    try:
        car1.daily_rate = 0
    except ValueError as error:
        print("Validation Error:", error)

    # 6. Test invalid passenger seat values
    print("\n--- TEST 3: PASSENGER SEAT VALIDATION ---")

    try:
        PassengerCar("PC103", "Invalid Car", 70.0, -5)
    except ValueError as error:
        print("Validation Error:", error)

    # 7. Test invalid cargo capacity
    print("\n--- TEST 4: CARGO CAPACITY VALIDATION ---")

    try:
        CargoTruck("CT203", "Invalid Truck", 140.0, 0)
    except ValueError as error:
        print("Validation Error:", error)

    # 8. Test invalid rental duration
    print("\n--- TEST 5: RENTAL DURATION VALIDATION ---")

    try:
        car1.calculate_rental_cost(0)
    except ValueError as error:
        print("Validation Error:", error)

    # 9. Test abstract class
    print("\n--- TEST 6: ABSTRACT CLASS TEST ---")

    try:
        vehicle = Vehicle("V001", "Generic Vehicle", 100.0)
    except TypeError as error:
        print("Abstract Class Error:", error)

    # 10. Test operator overloading and sorting
    print("\n--- TEST 7: VEHICLE SORTING ---")

    sorted_fleet = sorted(fleet)

    for vehicle in sorted_fleet:
        print(
            f"{vehicle.model}: "
            f"${vehicle.daily_rate:.2f}"
        )

    # 11. Test polymorphic fleet manifest
    print("\n--- TEST 8: POLYMORPHIC FLEET PROCESSING ---")

    generate_fleet_manifest(fleet, 3)
