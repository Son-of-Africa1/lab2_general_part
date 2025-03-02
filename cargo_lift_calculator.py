# cargo_lift_calculator.py
#Version 1.0.0

class CargoLiftCalculator:
    def __init__(self):
        # Base cost based on weight
        self.base_cost = {
            50: 300,
            100: 1000,
            300: 2000
        }

    def calculate_cost(self, weight, floor, has_elevator):
        # Calculate base cost based on weight
        if weight <= 50:
            cost = self.base_cost[50]
        elif weight <= 100:
            cost = self.base_cost[100]
        elif weight <= 300:
            cost = self.base_cost[300]
        else:
            raise ValueError("Weight exceeds maximum limit (300 kg).")

        # If elevator is available, return base cost
        if has_elevator:
            return cost

        # Calculate additional cost for manual lifting
        additional_cost = 300 * (floor - 1) * (weight // 100 + 1)
        total_cost = cost + additional_cost

        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = CargoLiftCalculator()

    # Input values
    weight = float(input("Enter the weight of the cargo (kg): "))
    floor = int(input("Enter the floor number: "))
    has_elevator = input("Is there an elevator available? (yes/no): ").lower() == "yes"

    # Calculate and display the cost
    try:
        total_cost = calculator.calculate_cost(weight, floor, has_elevator)
        print(f"The total cost of lifting the cargo is: {total_cost} RUB")
    except ValueError as e:
        print(e)