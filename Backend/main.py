# backend/main.py

from fastapi import FastAPI, HTTPException, Depends, Header
from models import User, Token, Review, ReviewResponse
from auth import hash_password, verify_password, create_access_token, verify_token
from database import users_collection, reviews_collection
from sentiment import analyze_sentiment
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register", response_model=Token)
def register(user: User):
   
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])
    result = users_collection.insert_one(user_data)
    token = create_access_token({"user_id": str(result.inserted_id)})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/login", response_model=Token)
def login(user: User):
    
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"user_id": str(db_user["_id"])})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(authorization: str = Header(...)):
  
    try:
        token = authorization.split(" ")[1]  
        payload = verify_token(token)
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return payload
    except IndexError:
        raise HTTPException(status_code=401, detail="Token missing or malformed")


@app.post("/reviews", response_model=ReviewResponse)
def submit_review(review: Review, user=Depends(get_current_user)):
    analysis = analyze_sentiment(review.review_text)
    review_data = review.dict()
    review_data.update({
        "sentiment": analysis["sentiment"],
        "confidence": analysis["confidence"],
        "timestamp": datetime.utcnow()
    })
    reviews_collection.insert_one(review_data)
    return ReviewResponse(**review_data)

@app.get("/reviews")
def get_reviews(user=Depends(get_current_user)):
    
    user_reviews = list(reviews_collection.find({"user_id": user["user_id"]}))
    for review in user_reviews:
        review["timestamp"] = review.get("timestamp")
    return user_reviews
