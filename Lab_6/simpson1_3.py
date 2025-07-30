import numpy as np 
import matplotlib.pyplot as plt

#Simpson 1/3 implementation

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

n = int(input("Enter the number of intervals: "))

if n%2 != 0:
    print("The value must be divisible by 2 ! ")
    exit()
else:
    h = (b-a)/n

    func = input("Enter the function f(x) in terms of x using python syntax (e.g., np.sin(x), np.exp(x)): ")
    def f(x , func):
        return eval(func)

    def y(x):
        return f(x , func)


    x = np.linspace(a, b, n+1)
    I = 0
    sum1 = 0
    sum2 = 0

    for i in range(1,n):
        if i%2 != 0:
            sum1+=y(x[i])
        else:
            sum2+=y(x[i])

    I = (h/3 * (y(x[0]) + 4 * sum1 + 2 * sum2 + y(x[n])))

    print(f"The approximate integral value is {I}")

    # Plotting the function and Simpson's 1/3 approximation

    y_val = [y(xi) for xi in x]
    plt.plot(x, y_val, label='f(x)', marker='o')
    x_val = np.linspace(a, b, 1000)
    plt.plot(x_val, [y(xi) for xi in x_val], label='f(x) - Continuous', color='orange')
    for i in range(0, n, 2):
        xs = x[i:i+3]
        ys = y_val[i:i+3]
        plt.fill_between(xs, ys, 0, color='pink', edgecolor='blue', alpha=0.3)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Simpson's 1/3 Rule Approximation")
    plt.legend()
    plt.grid(True)
    plt.show()