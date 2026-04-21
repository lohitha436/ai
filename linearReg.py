import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Mean
mx = np.mean(X)
my = np.mean(Y)

# Slope and Intercept
m = np.sum((X - mx)*(Y - my)) / np.sum((X - mx)**2)
c = my - m * mx

# Line
y_pred = m * X + c

# Plot
plt.scatter(X, Y)
plt.plot(X, y_pred)
plt.show()
