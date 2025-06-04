# init_db.py
from backend.database import Base, engine
from backend.models import User  # Import all models here

# Create tables based on the Base metadata
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")