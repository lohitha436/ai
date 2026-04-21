from sklearn.tree import DecisionTreeClassifier

X = [[0, 0], [1, 1]]
y = [0, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[2, 2]]))
