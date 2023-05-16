import decimal
import math

# Configure decimal precision
decimal.getcontext().prec = 52

# Initialize variables
pi = decimal.Decimal(0)
term = decimal.Decimal(1)
sign = 1

# Define the actual value of pi
pi_real = decimal.Decimal("3.14159265358979323846264338327950288419716939937510")

# Iterate through the series
for i in range(1, 10000000000):
    previous_pi = pi
    pi += sign * term
    sign *= -1
    term = decimal.Decimal(1) / decimal.Decimal(2 * i + 1)

    # Calculate precision with respect to actual value of pi
    precision = abs((pi * 4) - pi_real) / pi_real

    # Print progress at regular intervals
    if i % 10000 == 0:
        print("Iteration:", i)
        print("Pi:", pi * 4)
        print("Precision:", precision)
        print()

# Print final result
final_precision = abs((pi * 4) - pi_real) / pi_real
print("Pi (50 decimal places):", "{:.50f}".format(pi * 4))
print("Final precision:", "{:.0f}".format(math.floor(math.log10(final_precision))) + "e" + "{:.0f}".format(math.floor(math.log10(final_precision))))