from fastapi import FastAPI, HTTPException
from typing import List
from .news import fetch_headlines, neutralize_headline
from .config import CATEGORIES
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="News Headline Neutralizer")


# Allow requests from any origin (or specify your frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with ["http://localhost:5500"] if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the News Headline Neutralizer API!"}

@app.get("/neutralize/{category}", response_model=List[str])
async def neutralize_category_headlines(category: str, count: int = 3):
    category = category.lower()
    if category not in CATEGORIES:
        raise HTTPException(status_code=400, detail=f"Category must be one of {CATEGORIES}")

    headlines = await fetch_headlines(category, count)
    neutralized = [neutralize_headline(h) for h in headlines]
    return neutralized
