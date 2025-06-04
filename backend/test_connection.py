# test_connection.py
from backend.database import engine

try:
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed:", e)
