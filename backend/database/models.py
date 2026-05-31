from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    prediction = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=db.func.now())