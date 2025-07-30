import numpy as np 
import matplotlib.pyplot as plt

# Simpson's 3/8 rule implementation

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

n = int(input("Enter the number of intervals (must be a multiple of 3): "))

if n % 3 != 0:
    raise ValueError("Number of intervals must be a multiple of 3 for Simpson's 3/8 rule.")

h = (b-a)/n

func = input("Enter the function f(x) in terms of x using python syntax (e.g., np.sin(x), np.exp(x)): ")
def f(x , func):
    return eval(func)

def y(x):
    return f(x , func)

x = np.linspace(a, b, n+1)
y_val = [y(xi) for xi in x]
I = y(x[0]) + y(x[n])

for i in range(1, n):
    if i % 3 == 0:
        I += 2 * y(x[i])
    else:
        I += 3 * y(x[i])
I = (3 * h / 8) * I

print(f"The approximate integral value is {I}")

plt.plot(x, y_val, label='f(x)', marker='o')
x_val = np.linspace(a, b, 1000)
plt.plot(x_val, [y(xi) for xi in x_val], label='f(x) - Continuous', color='orange')
plt.fill_between(x_val, [y(xi) for xi in x_val], 0, color='orange', alpha=0.1)

for i in range(0, n, 3):
    xs = x[i:i+4]
    ys = y_val[i:i+4]
    plt.fill_between(xs, ys, 0, color='pink', edgecolor='blue', alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Simpson's 3/8 Rule Approximation")
plt.legend()
plt.grid(True)
plt.show()