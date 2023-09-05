""" Krunal SDEV 300  circel radius calculator """

import math

def main():
    """Main function to calculate and print the area of the circle."""
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * math.pow(radius, 2)
    print(f"The area of the circle with radius {radius} is {area:.2f}")

main()
