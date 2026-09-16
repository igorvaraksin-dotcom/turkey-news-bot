# Telegram
TELEGRAM_BOT_TOKEN = "7746575131:AAHurcRbPLtg3RBoXwwyk77e_7HZlkrL_yA"
TELEGRAM_CHAT_ID = "690141522"

# Мова: 'uk', 'ru', 'tr', 'en'
DIGEST_LANGUAGE = "uk"

# Час відправки (години, хвилини)
SEND_HOUR_1 = 8   # ранковий дайджест
SEND_MINUTE_1 = 0

SEND_HOUR_2 = 19  # вечірній дайджест
SEND_MINUTE_2 = 0

# Тільки турецькі RSS-стрічки (політика + економіка)
RSS_FEEDS = [
    # Політика
    "https://t24.com.tr/rss/haberler",
    "https://www.cumhuriyet.com.tr/rss",
    "https://www.sozcu.com.tr/feeds-rss-category-gundem",
    "https://www.hurriyet.com.tr/rss/anasayfa",
    "https://www.haberturk.com/rss",
    "https://www.ntv.com.tr/gundem.rss",
    "https://www.cnnturk.com/feed/rss/turkiye/news",
    "https://www.sabah.com.tr/rss/anasayfa.xml",
    "https://www.sabah.com.tr/rss/gundem.xml",
    "https://www.aa.com.tr/tr/rss/default?cat=guncel",
    "https://www.ahaber.com.tr/rss/gundem.xml",
    "https://www.yenisafak.com/Rss",
    # Економіка
    "https://www.hurriyet.com.tr/rss/ekonomi",
    "https://www.haberturk.com/rss/ekonomi",
    "https://www.paraanaliz.com/rss",
    "https://www.doviz.com/rss",
]

DB_PATH = "news.db"
OPENAI_API_KEY = ""