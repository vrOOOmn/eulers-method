
import math

def euler_method(dydx, x0, y0, deltax, xf):

    steps = int((xf - x0) / deltax)  # Calculate the number of steps
    points = [(x0, y0)]  # Start with the initial condition
    x, y = x0, y0

    for _ in range(steps):
        y += deltax * dydx(x, y)  # Euler's method formula
        x += deltax
        points.append((x, y))

    return points


    # User inputs
print("Euler's Method Calculator")
print("Define your differential equation as a lambda function, e.g. 'lambda x, y: x - y - 1'")
equation_input = input("Enter the differential equation: ")

# Convert user input into a lambda function
try:
    dydx = eval(equation_input)
    if not callable(dydx):
        raise ValueError("The input must be a callable lambda function.")
except Exception as e:
    print(f"Error in processing the differential equation : {e}")
    exit(1)

# Additional inputs
x0 = float(input("Enter the initial x value (x0): "))
y0 = float(input("Enter the initial y value (y0): "))
deltax = float(input("Enter the step size (∆x): "))
xf = float(input("Enter the final x value (xf): "))

# Compute the approximation
solution = euler_method(dydx, x0, y0, deltax, xf)

# Display results
print("\nApproximation using Euler's method:")
for x, y in solution:
    print(f"x = {x:.2f}, y ≈ {y:.3f}")



