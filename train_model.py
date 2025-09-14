import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the data
data = pd.read_csv('Laptop_price.csv')

# Convert Brand to categorical codes
data['Brand'] = data['Brand'].astype('category').cat.codes

# Prepare features and target
x = data.drop(["Price"], axis=1)
y = data.Price

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Train the model
model = RandomForestRegressor()
model.fit(x_train, y_train)

# Save the model
joblib.dump(model, 'rf_model.pkl')

print("Model trained and saved as rf_model.pkl")
print(f"Training score: {model.score(x_train, y_train):.4f}")
print(f"Test score: {model.score(x_test, y_test):.4f}")

# Print feature columns for reference
print("\nFeature columns used in training:")
print(list(x.columns))
