from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("house_price_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST']) 
def predict():
    if request.method == 'POST':
        try:
            bedrooms = float(request.form['bedrooms'])
            bathrooms = float(request.form['bathrooms'])
            sqft = float(request.form['sqft'])
            features = np.array([[bedrooms, bathrooms, sqft]])
            prediction = model.predict(features)[0]
            return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction:,.2f}')
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
