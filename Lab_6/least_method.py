import numpy as np
import matplotlib.pyplot as plt

x = np.array(list(map(float, input("Enter all the x-data: ").split())))
y = np.array(list(map(float, input("Enter all the y-data: ").split())))

n = len(x)
A = [
    [n, np.sum(x), np.sum(x**2)],
    [np.sum(x), np.sum(x**2), np.sum(x**3)],
    [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
]
B = [
    np.sum(y),
    np.sum(x * y),
    np.sum((x**2) * y)
]

print('The coefficient matrix of normal equations is:', np.matrix(A))
print('The constants of normal equations are:', np.matrix(B))

inv_A = np.linalg.inv(A)
coefficients = np.dot(inv_A, B)

a = coefficients[0]
b = coefficients[1]
c = coefficients[2]


print(f'The coefficients of the least squares polynomial are: a = {a}, b = {b}, c = {c}')

# Plotting
x_fit = np.linspace(min(x) - 10 , max(x) +10, 1000)
y_fit = a + b * x_fit + c * x_fit**2
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x_fit, y_fit, color='blue', label='Fitted quadratic')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Quadratic Fit')
plt.legend()
plt.grid(True)
plt.show()