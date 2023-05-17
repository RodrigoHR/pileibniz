import decimal
import math
import time

# Configure decimal precision
decimal.getcontext().prec = 52

# Initialize variables
pi = decimal.Decimal(0)
term = decimal.Decimal(1)
sign = 1

# Define the actual value of pi
pi_real = decimal.Decimal("3.14159265358979323846264338327950288419716939937510")

# Track start time
start_time = time.time()

# Iterate through the series
for i in range(1, 50):
    previous_pi = pi
    pi += sign * term
    sign *= -1
    term = decimal.Decimal(1) / decimal.Decimal(2 * i + 1)

    # Calculate precision with respect to actual value of pi
    precision = abs((pi * 4) - pi_real) / pi_real

    # Print progress at regular intervals
    if i % 1000000 == 0:
        print("Iteration:", i)
        print("Pi:", pi * 4)
        print("Precision:", precision)
        print()

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Print final result
final_precision = abs((pi * 4) - pi_real) / pi_real
print("Pi (50 decimal places):", "{:.50f}".format(pi * 4))
print("Final precision:", "{:.0f}".format(math.floor(math.log10(final_precision))) + "e" + "{:.0f}".format(math.floor(math.log10(final_precision))))

# Save the last iteration to a file
with open("last_iteration.txt", "w") as file:
    file.write("Last Iteration: {}\n".format(i))
    file.write("Elapsed Time: {} seconds\n".format(elapsed_time))
    file.write("Timestamp: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    file.write("Pi: {}\n".format(pi * 4))
    file.write("Precision: {}\n".format(precision))
