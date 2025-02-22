import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    """Sends an alert to a Telegram chat and provides error feedback."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("ok"):
            print("✅ Telegram alert sent successfully!")
        else:
            print(f"❌ Telegram API Error: {response_data}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Telegram request failed: {e}")