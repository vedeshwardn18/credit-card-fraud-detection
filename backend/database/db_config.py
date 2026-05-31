from sqlalchemy import create_engine

DB_USERNAME = "postgres"
DB_PASSWORD = "veduvedu_18"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fraud_detection_db"

DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

print("Database connected successfully!")