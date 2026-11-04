# add.py
import sys

if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
    sys.exit(1)

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
except ValueError:
    print("Error: both arguments must be numbers.")
    sys.exit(1)

print(f"{a} + {b} = {a + b}")
