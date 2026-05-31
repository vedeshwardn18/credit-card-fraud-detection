from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import sys
import os

# Add backend folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from database.models import db, Transaction

app = Flask(__name__)

# Enable CORS
CORS(app)

# PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:veduvedu_18@localhost:5432/fraud_detection_db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Load ML model
model = joblib.load(
    r"C:\credit-card-fraud-detection\backend\ml\fraud_model.pkl"
)


@app.route('/')
def home():
    return "Fraud Detection API Running"


@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    features = np.array(
        data['features']
    ).reshape(1, -1)

    prediction = model.predict(features)[0]

    result = (
        "Fraud"
        if prediction == 1
        else "Legitimate"
    )

    amount = float(data['features'][-1])

    transaction = Transaction(
        amount=amount,
        prediction=result
    )

    db.session.add(transaction)
    db.session.commit()

    alert_message = None

    if result == "Fraud":
        alert_message = (
            "WARNING: Potential fraudulent transaction detected!"
        )

    return jsonify({
        "prediction": result,
        "alert": alert_message
    })


@app.route('/stats')
def stats():

    total_transactions = Transaction.query.count()

    total_fraud = Transaction.query.filter_by(
        prediction="Fraud"
    ).count()

    fraud_rate = 0

    if total_transactions > 0:
        fraud_rate = (
            total_fraud /
            total_transactions
        ) * 100

    return jsonify({
        "total_transactions": total_transactions,
        "total_fraud": total_fraud,
        "fraud_rate": round(fraud_rate, 2)
    })


@app.route('/transactions')
def transactions():

    records = (
        Transaction.query
        .order_by(Transaction.id.desc())
        .limit(10)
        .all()
    )

    result = []

    for record in records:
        result.append({
            "id": record.id,
            "amount": record.amount,
            "prediction": record.prediction,
            "created_at": str(record.created_at)
        })

    return jsonify(result)


@app.route('/alerts')
def alerts():

    fraud_records = (
        Transaction.query
        .filter_by(prediction="Fraud")
        .order_by(Transaction.id.desc())
        .all()
    )

    result = []

    for record in fraud_records:
        result.append({
            "id": record.id,
            "amount": record.amount,
            "prediction": record.prediction,
            "created_at": str(record.created_at)
        })

    return jsonify(result)


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)