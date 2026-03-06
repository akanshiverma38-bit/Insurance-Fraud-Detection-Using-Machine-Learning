from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("../models/fraud_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [float(x) for x in request.form.values()]
    features = np.array(features).reshape(1,-1)

    prediction = model.predict(features)

    if prediction == 1:
        result = "Fraud Claim"
    else:
        result = "Genuine Claim"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)