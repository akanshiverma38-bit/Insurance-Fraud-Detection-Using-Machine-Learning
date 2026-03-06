import pickle
import numpy as np

# load model
model = pickle.load(open("../models/fraud_model.pkl", "rb"))

def predict_fraud(input_data):
    
    input_data = np.array(input_data).reshape(1,-1)

    prediction = model.predict(input_data)

    if prediction == 1:
        return "Fraud Detected"
    else:
        return "Not Fraud"