import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")
    
    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT", 8080))
    
    REDIS_URL: str = os.getenv("REDIS_URL")
    DB_URL: str = os.getenv("DB_URL")

    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

settings = Settings()
