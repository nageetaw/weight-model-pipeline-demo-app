import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump

X = np.array([[150], [160], [170], [180], [190]])
y = np.array([50, 60, 70, 80, 90])

model = LinearRegression().fit(X, y)
# save model
dump(model, "model.joblib")
print("Saved model.joblib")
