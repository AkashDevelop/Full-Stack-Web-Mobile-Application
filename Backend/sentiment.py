# backend/sentiment.py
import nltk

nltk.download('vader_lexicon')
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Initialize the VADER sentiment analyzer.
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of a given text.
    
    Returns:
      - sentiment: "Positive", "Neutral", or "Negative"
      - confidence: Absolute value of the compound score (reflects confidence)
    """
    scores = sid.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return {"sentiment": sentiment, "confidence": abs(compound)}
