from .database import SessionLocal  # Import the session from database.py

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
