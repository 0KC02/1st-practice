import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")

# Function to calculate the area of a circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius**2
    print(f"The area of the circle is: {area}")

# Function to calculate the area of a triangle
def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

# Main program
calculate_rectangle_area()
calculate_circle_area()
calculate_triangle_area()
