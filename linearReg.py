import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

n = len(x)
m = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x*x) - (np.sum(x))**2)
b = (np.sum(y) - m*np.sum(x)) / n

print("Slope:", m)
print("Intercept:", b)


x_new = 6
y_pred = m*x_new + b
print("Prediction:", y_pred)
