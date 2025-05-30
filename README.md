# Create the README.md file with the nicely formatted project description

readme_content = """
# 🏡 House Price Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange?logo=scikit-learn)


A Flask web application that predicts house prices based on number of bedrooms, bathrooms, and square footage. It uses a simple **linear regression** model trained on the Ames Housing dataset.

---

## 🚀 Features

- 🔢 Predict house prices using:
  - Number of bedrooms
  - Number of bathrooms
  - Living area (sqft)
- 📊 Built using `scikit-learn` Linear Regression
- 🧠 Custom model trained from open dataset
- ⚡ Lightweight and easy to deploy locally

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas
- **Frontend:** HTML (with simple form)
- **Dataset:** [AmesHousing.csv](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```
### 2. Create Virtual Environment & Install Requirements
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
### 3. Train the Model
```
cd model
python train_model.py

```
### 4. Run the Flask App
```
cd ../app
python app.py
```
### 5. Open in Browser
Go to: http://127.0.0.1:5000

### 📸 Screenshots
![image](https://github.com/user-attachments/assets/60e933db-e9cd-4016-abc6-1b59af2c50ce)
![image](https://github.com/user-attachments/assets/23f6d2d2-14c3-4b32-a624-64c96151491b)

### 📂 Project Structure
```
house-price-predictor/
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── house_price_model.pkl
├── model/
│   └── train_model.py
├── data/
│   └── AmesHousing.csv
├── requirements.txt
└── README.md
```
