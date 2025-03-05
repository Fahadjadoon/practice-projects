from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)  # Unique constraint for email
    password = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=True)  # New column