from sklearn.tree import DecisionTreeClassifier

# Training data
X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

# Output / Classes
y = [1, 1, 0, 0]

# Create Decision Tree
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Test data
prediction = model.predict([[1, 1]])

print("Predicted class:", prediction[0])
