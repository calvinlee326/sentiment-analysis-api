from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import List

# Create FastAPI app
app = FastAPI()

#
sentiment_analyzer = pipeline("sentiment-analysis")

# Define input data models
class TextData(BaseModel):
    text: str

class TextListData(BaseModel):
    texts: List[str]
    
# single text sentiment analysis API
@app.post("/analyze_sentiment/")
async def analyze_sentiment(data: TextData):
    """
    Receive a single text and perform sentiment analysis
    :param data: Data containing the text
    :return: Return the sentiment analysis result
    """
    result = sentiment_analyzer(data.text)
    return {"sentiment": result}

# batch text sentiment analysis API
@app.post("/analyze_batch_sentiment/")
async def analyze_batch_sentiment(data: TextListData):
    """
    Batch receive texts and perform sentiment analysis
    :param data: Data containing multiple texts
    :return: Return a list of sentiment analysis results
    """
    results = sentiment_analyzer(data.texts)
    return {"sentiments": results}