# Credit Card Fraud Detection System

# credit-card-fraud-detection

## Overview

The Credit Card Fraud Detection System is a full-stack machine learning application designed to identify fraudulent credit card transactions in real time. The system uses a trained Logistic Regression model to classify transactions as either Fraudulent or Legitimate and provides a web-based dashboard for monitoring transaction activity, fraud statistics, and alerts.

---

## Features

- Real-time fraud prediction using Machine Learning
- PostgreSQL database integration
- Transaction history tracking
- Fraud alert generation
- Interactive dashboard
- Fraud rate calculation
- REST API using Flask
- Data visualization using Chart.js
- Automatic dashboard refresh

---

## Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- SMOTE (Imbalanced-learn)

### Backend
- Flask
- Flask-SQLAlchemy
- Flask-CORS

### Database
- PostgreSQL
- SQLAlchemy ORM

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

---

## Project Architecture

Dataset
↓
Data Preprocessing
↓
SMOTE Balancing
↓
Logistic Regression Model
↓
Flask API
↓
PostgreSQL Database
↓
Dashboard Visualization

---

## API Endpoints

### Home

GET /

Returns API status.

### Predict Transaction

POST /predict

Example Request:

```json
{
  "features": [
    406.0,
    -2.312227,
    1.951992,
    ...
  ]
}
```

Example Response:

```json
{
  "prediction": "Fraud",
  "alert": "WARNING: Potential fraudulent transaction detected!"
}
```

### Statistics

GET /stats

Returns:

```json
{
  "total_transactions": 11,
  "total_fraud": 1,
  "fraud_rate": 9.09
}
```

### Transaction History

GET /transactions

Returns recent transactions.

### Fraud Alerts

GET /alerts

Returns all fraud transactions.

---

## Machine Learning Workflow

1. Data Collection
2. Exploratory Data Analysis
3. Data Cleaning
4. Handling Class Imbalance using SMOTE
5. Model Training using Logistic Regression
6. Model Evaluation
7. Model Serialization using Joblib
8. Deployment through Flask API

---

## Future Enhancements

- Random Forest and XGBoost integration
- Real-time payment gateway monitoring
- User authentication
- Email and SMS fraud notifications
- Cloud deployment
- Advanced analytics dashboard

---

## Author

Vedeshwar D N

B.Tech AIML
Woxsen University
