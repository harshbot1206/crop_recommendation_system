import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

df = pd.read_csv('Crop_recommendation.csv')


# Features & Labels
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Create 'ML' folder if not exists
os.makedirs('CropSystem/ML', exist_ok=True)

# Save model
with open('CropSystem/ML/crop_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved to CropSystem/ML/crop_model.pkl")
