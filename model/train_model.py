import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load the dataset
df = pd.read_csv('../data/housing.csv')

# Display columns for reference
print("Columns available in the dataset:", df.columns.tolist())

# Select relevant features and target
features = ['Bedroom AbvGr', 'Full Bath', 'Gr Liv Area']
target = 'SalePrice'

# Drop rows with missing values in those columns
df = df[features + [target]].dropna()

# Create input (X) and output (y)
X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Ensure app folder exists
output_path = '../app/house_price_model.pkl'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the model
joblib.dump(model, output_path)

print("✅ Model trained and saved to:", output_path)
