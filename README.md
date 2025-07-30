# Numerical Methods Lab

This repository contains Python implementations of various numerical methods, including code and visualizations for common integration and curve fitting techniques. Each lab folder contains scripts for a specific numerical method, with interactive input and graphical output.

## Lab Contents

### Lab6
- **trapezoidal.py**: Implements the Trapezoidal Rule for numerical integration. Plots the function and shades the area under the curve using trapezoids.
- **simpson.py**: Implements Simpson's 1/3 Rule for numerical integration. Plots the function and shades the area under the curve using parabolic segments.
- **simpson3_8.py**: Implements Simpson's 3/8 Rule for numerical integration. Plots the function and shades the area under the curve using cubic segments.

### Lab7
- **least_method.py**: Performs least squares fitting for a quadratic polynomial. Plots the original data points and the fitted quadratic curve.

## How to Run
1. Make sure you have Python 3 and `matplotlib` installed:
   ```sh
   pip install matplotlib
   ```
2. Run any script using:
   ```sh
   python <script_name.py>
   ```
3. Follow the prompts to enter data or function expressions as required.

## Features
- Interactive input for data points or function expressions.
- Visualizations of the numerical method and the area under the curve.
- Error handling for invalid input (e.g., interval requirements for Simpson's rules).

## Notes
- For Simpson's 1/3 Rule, the number of intervals must be even.
- For Simpson's 3/8 Rule, the number of intervals must be a multiple of 3.
- Function expressions should use Python/NumPy syntax (e.g., `np.sin(x)`, `np.exp(x)`).

---

Developed for educational purposes in the Numerical Methods Lab.
