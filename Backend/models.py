# backend/models.py

from pydantic import BaseModel, EmailStr
from datetime import datetime

# User model for registration/login
class User(BaseModel):
    username: str
    email: EmailStr
    password: str  

# Token model for authentication responses
class Token(BaseModel):
    access_token: str
    token_type: str

# Review model for user-submitted reviews
class Review(BaseModel):
    user_id: str
    review_text: str

# ReviewResponse model: used to return review data after sentiment analysis
class ReviewResponse(BaseModel):
    review_text: str
    sentiment: str
    confidence: float
    timestamp: datetime
