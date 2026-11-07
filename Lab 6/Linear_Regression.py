import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20000, 30000, 40000, 50000, 60000])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict salary
prediction = model.predict([[6]])

print("Predicted Salary:", prediction[0])

# Display coefficient and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
