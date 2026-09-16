import config
from database import init_db, save_news, get_unprocessed_news, mark_as_processed, clear_old_news
from rss_collector import fetch_rss_feeds
from classifier import filter_and_classify
from digest_generator import generate_digest
from telegram_sender import send_to_telegram

def main():
    init_db()
    
    print("Збір новин...")
    raw_news = fetch_rss_feeds()
    print(f"Знайдено {len(raw_news)} новин")
    
    print("Фільтрація...")
    filtered_news = filter_and_classify(raw_news, config.DIGEST_LANGUAGE)
    print(f"Відфільтровано {len(filtered_news)} новин")
    
    save_news(filtered_news)
    
    clear_old_news(days=1)
    
    unprocessed = get_unprocessed_news(limit=50)
    
    if not unprocessed:
        print("Немає нових новин для відправки")
        return
    
    print("Генерація дайджесту...")
    digest = generate_digest(unprocessed, config.DIGEST_LANGUAGE)
    
    # Перевіряємо довжину
    if len(digest) > 4000:
        print(f"Повідомлення занадто довге ({len(digest)} символів), скорочуємо...")
        unprocessed = get_unprocessed_news(limit=30)
        digest = generate_digest(unprocessed, config.DIGEST_LANGUAGE)
    
    print("Відправка в Telegram...")
    print(f"Довжина повідомлення: {len(digest)} символів")
    result = send_to_telegram(digest)
    
    if result.get('ok'):
        print("Успішно відправлено!")
        mark_as_processed(unprocessed)
    else:
        print(f"Помилка відправки: {result}")
    
    clear_old_news(days=7)

if __name__ == "__main__":
    main()