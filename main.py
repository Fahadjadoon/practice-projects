from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine  # Imported from database.py
from models import Base, User  # Imported from models.py
from schemas import SignupRequest, LoginRequest, ResponseMessage  # Imported from schemas.py
from datetime import datetime, timedelta
from jose import JWTError, jwt  # jose library for JWT handling
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer
from fastapi import Security

# Initialize FastAPI app
app = FastAPI()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT secret key and algorithm
SECRET_KEY = "AZ19"  # Change this to a secure random key
ALGORITHM = "HS256"  # Algorithm used to sign the token
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token validity duration


# Utility function to create JWT
def create_access_token(data: dict):
    """
    Creates a JWT token with user information and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/signup/", response_model=ResponseMessage)
def signup(user: SignupRequest, db: Session = Depends(get_db)):
    # Check if the email or username already exists
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.username == user.username)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Create a new user
    new_user = User(email=user.email, password=hashed_password, username=user.username)
    db.add(new_user)
    db.commit()
    return {"message": "User signed up successfully"}


@app.post("/login/")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    # Check if the user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not present")
    
    # Verify the provided password against the stored hashed password
    if not pwd_context.verify(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Wrong email or password")


    # Create JWT token
    access_token = create_access_token(data={"sub": existing_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# OAuth2PasswordBearer will extract the token from the "Authorization" header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email  # Return the user's email if valid
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")



@app.get("/users/")
def get_all_users(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Fetch all users from the database. Protected route: requires a valid token.
    """
    users = db.query(User).all()

    # Create a list to store users without passwords
    users_without_passwords = []
    for user in users:
        user_data = {
            "id": user.id,  # Assuming you have an ID column in your User model
            "email": user.email,
        }
        users_without_passwords.append(user_data)

    return {"current_user": current_user, "users": users_without_passwords}
