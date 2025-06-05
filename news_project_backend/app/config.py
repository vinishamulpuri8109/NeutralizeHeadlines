from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")

CATEGORIES = ["business", "entertainment", "health", "science", "sports", "technology"]

MODEL_NAME = os.getenv("MODEL_NAME")
