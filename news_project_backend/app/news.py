import httpx
from transformers import pipeline
from .config import NEWS_API_KEY, NEWS_API_URL, MODEL_NAME

generator = pipeline("text2text-generation", model=MODEL_NAME)

async def fetch_headlines(category: str, count: int = 3):
    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "country": "us",
        "pageSize": count,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(NEWS_API_URL, params=params)
        data = response.json()
        return [article['title'] for article in data.get('articles', [])]

def neutralize_headline(headline: str):
    prompt = f"Neutralize: {headline}"
    result = generator(prompt, max_length=60, do_sample=False)
    return result[0]['generated_text']
