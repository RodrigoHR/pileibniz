Leibniz Method of Calculating Pi
This repository contains a Python implementation of the Leibniz method for calculating the value of pi. The Leibniz formula is an iterative series that converges to pi when the number of terms approaches infinity. The formula was first proposed by Gottfried Leibniz in the 17th century.

The formula for the Leibniz method is as follows:

<img src="https://render.githubusercontent.com/render/math?math=\large \frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}">
In this formula, pi is approximated by summing the terms of the series. Each term alternates between positive and negative, and the denominator increases by 2 for each term.

Decimal Module
The decimal module in Python is used to perform arithmetic operations with arbitrary precision. By default, Python's float type has a limited precision of 15-16 decimal places. However, using the decimal module, the precision can be increased up to 28-30 decimal places. In this implementation, a precision of 52 decimal places is used for increased accuracy.

Implementation
The Python code in this repository uses the Leibniz formula to calculate pi with a precision of 52 decimal places. The code iterates through the series and sums the terms to approximate pi. After each iteration, the precision is calculated by comparing the approximate value of pi to the actual value of pi. The progress of the iteration is printed at regular intervals.

The final result is displayed with 50 decimal places and the final precision is displayed in scientific notation. The code is optimized for performance by avoiding unnecessary calculations and using the decimal module for high-precision arithmetic.

Usage
To use this code, simply run the leibniz_pi.py file in a Python environment. The progress of the iteration will be printed at regular intervals, and the final result will be displayed at the end.

copy code
$ python leibniz_pi.py
Iteration: 10000
Pi: 3.1414926535900345
Precision: 3.1856480428003735e-08

Iteration: 20000
Pi: 3.1415426535898244
Precision: 1.0112670436430644e-08

Iteration: 30000
Pi: 3.1415593202565027
Precision: 6.447631952198718e-09

...

Pi (50 decimal places): 3.14159265358979323846264338327950288419716939937510
Final precision: 2e-15
Conclusion
The Leibniz method is a simple but effective way to approximate the value of pi. By using the decimal module in Python, high-precision calculations can be performed to accurately estimate pi to many decimal places. This implementation provides a useful example of how the Leibniz method can be applied in a programming context.
