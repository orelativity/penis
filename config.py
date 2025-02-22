import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY is missing")
if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Telegram credentials are missing")
