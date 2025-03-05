from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your MySQL credentials
username = "root"
host = "localhost"
database = "User_info"

# Create the database connection string
connection_string = f"mysql+pymysql://{username}@{host}/{database}"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connected to the database successfully!")
except Exception as e:
    print("Error connecting to the database:", e)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Controling database session
def get_db():
    db = SessionLocal()
    try:
        yield db # yield will return the value of db but dose not ends the 
        #execution of the function it will pause it and resume it when it is called again.
    finally:
        db.close()