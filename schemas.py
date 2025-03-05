from pydantic import BaseModel,EmailStr

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    username: str  # New field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ResponseMessage(BaseModel):
    message: str