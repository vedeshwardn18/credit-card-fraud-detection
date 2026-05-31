from sqlalchemy import create_engine, text

DB_USERNAME = "postgres"
DB_PASSWORD = "veduvedu_18"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fraud_detection_db"

DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

create_table_query = """
CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    prediction VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

with engine.connect() as connection:
    connection.execute(text(create_table_query))
    connection.commit()

print("Transactions table created successfully!")