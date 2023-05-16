## Leibniz Method of Calculating Pi

This repository contains a Python implementation of the Leibniz method for calculating the value of pi. The Leibniz formula is an iterative series that converges to pi when the number of terms approaches infinity. The formula was first proposed by Gottfried Leibniz in the 17th century.

The formula for the Leibniz method is as follows:

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\large \frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}"></p>

In this formula, pi is approximated by summing the terms of the series. Each term alternates between positive and negative, and the denominator increases by 2 for each term.

## Decimal Module

The decimal module in Python is used to perform arithmetic operations with arbitrary precision. By default, Python's float type has a limited precision of 15-16 decimal places. However, using the decimal module, the precision can be increased up to 28-30 decimal places. In this implementation, a precision of 52 decimal places is used for increased accuracy.

## Implementation

The Python code in this repository uses the Leibniz formula to calculate pi with a precision of 52 decimal places. The code iterates through the series and sums the terms to approximate pi. After each iteration, the precision is calculated by comparing the approximate value of pi to the actual value of pi. The progress of the iteration is printed at regular intervals.

The final result is displayed with 50 decimal places and the final precision is displayed in scientific notation. The code is optimized for performance by avoiding unnecessary calculations and using the decimal module for high-precision arithmetic.

## Future Improvements

One possible improvement for this implementation is to split the iteration process between threads. Since each iteration of the Leibniz formula is independent of the previous iterations, the calculation can be easily parallelized. By using multiple threads, the computation time can be significantly reduced, especially for large numbers of iterations.

In addition, there are many other algorithms for calculating the value of pi, each with its own strengths and weaknesses. Some of these algorithms, such as the Bailey-Borwein-Plouffe (BBP) formula and the Chudnovsky algorithm, have been shown to be more efficient than the Leibniz formula for large numbers of decimal places.

By exploring different algorithms and parallelizing the computation, further improvements can be made to the performance and accuracy of pi calculation.
