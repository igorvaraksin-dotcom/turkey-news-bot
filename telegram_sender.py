import requests
import os

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
    data = {
        'chat_id': os.getenv('TELEGRAM_CHAT_ID'),
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=data)
    return response.json()
