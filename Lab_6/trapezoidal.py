import numpy as np 
import matplotlib.pyplot as plt

# Trapezoidal rule implementation

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

n = int(input("Enter the number of intervals: "))

h = (b-a)/n

func = input("Enter the function f(x) in terms of x using python syntax (e.g., np.sin(x), np.exp(x)): ")
def f(x , func):
    return eval(func)

def y(x):
    return f(x , func)


x = np.linspace(a, b, n+1)
I = 0
sum = 0

for i in range(1, n):
    sum += y(x[i])

I = (h/2 * (y(x[0]) + 2 * sum + y(x[n])))

print(f"The approximate integral value is {I}")


# Plotting the function and trapezoidal approximation

plt.plot(x, [y(xi) for xi in x], label='f(x)', marker='o')
x_val = np.linspace(a, b, 1000)
plt.plot(x_val, [y(xi) for xi in x_val], label='f(x) - Continuous', color='orange')
plt.fill_between(x_val, [y(xi) for xi in x_val], 0, color='orange', alpha=0.1)
for i in range(n):
    xs = [x[i], x[i+1]]
    ys = [y(x[i]), y(x[i+1])]
    plt.fill(xs, ys, 0, color='pink', edgecolor='blue', alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trapezoidal Rule Approximation')
plt.legend()
plt.grid(True)
plt.show()