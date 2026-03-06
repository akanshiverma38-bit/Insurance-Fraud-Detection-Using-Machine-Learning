import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

df = pd.read_csv("data/insurance.csv")
df = df.drop(columns=['_c39'], errors='ignore')

print("Dataset Loaded")
print("Shape:", df.shape)
print("Columns:", df.columns)

# Convert fraud column
if 'fraud_reported' in df.columns:
    df['fraud_reported'] = df['fraud_reported'].map({'Y':1,'N':0})

# Fill missing values instead of dropping
df = df.fillna(0)

df = pd.get_dummies(df)

X = df.drop("fraud_reported", axis=1)
y = df["fraud_reported"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))

pickle.dump(model, open("models/fraud_model.pkl", "wb"))

print("Model Saved")
