import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DIGEST_LANGUAGE = "uk"

RSS_FEEDS = [
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
    "https://www.hurriyet.com.tr/rss/ekonomi",
    "https://www.haberturk.com/rss/ekonomi",
    "https://www.paraanaliz.com/rss",
    "https://www.doviz.com/rss",
]

DB_PATH = "news.db"
