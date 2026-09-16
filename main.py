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
    filtered_news = filter_and_classify(raw_news)
    print(f"Відфільтровано {len(filtered_news)} новин")
    
    save_news(filtered_news)
    clear_old_news(days=1)
    
    unprocessed = get_unprocessed_news(limit=50)
    
    if not unprocessed:
        print("Немає нових новин")
        return
    
    print("Генерація дайджесту...")
    digest = generate_digest(unprocessed, config.DIGEST_LANGUAGE)
    
    if len(digest) > 4000:
        print("Скорочуємо...")
        unprocessed = get_unprocessed_news(limit=30)
        digest = generate_digest(unprocessed, config.DIGEST_LANGUAGE)
    
    print("Відправка...")
    result = send_to_telegram(digest)
    
    if result.get('ok'):
        print("Успішно!")
        mark_as_processed(unprocessed)
    else:
        print(f"Помилка: {result}")

if __name__ == "__main__":
    main()
