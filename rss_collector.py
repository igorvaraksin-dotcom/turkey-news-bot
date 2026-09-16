import feedparser
from datetime import datetime, timedelta
import config
import re

def fetch_rss_feeds():
    news = []
    cutoff = datetime.now() - timedelta(hours=26)
    
    for feed_url in config.RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            source = feed.feed.get('title', feed_url)
            
            for entry in feed.entries[:50]:
                published = datetime.now()
                
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    try:
                        published = datetime(*entry.published_parsed[:6])
                    except:
                        pass
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    try:
                        published = datetime(*entry.updated_parsed[:6])
                    except:
                        pass
                
                title = entry.get('title', 'Без назви')
                summary = entry.get('summary', entry.get('description', ''))
                summary = re.sub('<.*?>', '', summary)
                link = entry.get('link', '')
                
                news.append({
                    'title': title,
                    'summary': summary[:500],
                    'link': link,
                    'source': source,
                    'published': published.isoformat(),
                    'category': 'uncategorized'
                })
        except Exception as e:
            print(f"Помилка завантаження {feed_url}: {e}")
    
    return news