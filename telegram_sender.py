import requests
import config

def send_to_telegram(message):
    """Відправляє повідомлення, розбиваючи на частини якщо потрібно"""
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Максимальна довжина повідомлення в Telegram
    MAX_LENGTH = 4000
    
    # Розбиваємо на частини
    parts = []
    while len(message) > MAX_LENGTH:
        # Знаходимо останній перенос рядка перед MAX_LENGTH
        split_point = message.rfind('\n\n', 0, MAX_LENGTH)
        if split_point == -1:
            split_point = MAX_LENGTH
        
        parts.append(message[:split_point])
        message = message[split_point:]
    
    parts.append(message)  # остання частина
    
    # Відправляємо кожну частину
    results = []
    for i, part in enumerate(parts):
        data = {
            'chat_id': config.TELEGRAM_CHAT_ID,
            'text': part,
            'parse_mode': 'Markdown'
        }
        
        if i > 0:
            # Додаємо позначку для продовження
            data['text'] = f"(продовження {i+1})\n\n" + part
        
        response = requests.post(url, json=data)
        results.append(response.json())
    
    return results[-1] if results else {'ok': False}