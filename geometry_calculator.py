import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":

    calculator = GeometryCalculator()

    # 👇 ADD YOUR CODE HERE (for circle branch)
    radius = 5
    print(f"Circle area = {calculator.calculate_circle_area(radius)}")