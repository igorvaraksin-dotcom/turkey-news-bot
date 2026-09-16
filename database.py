import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            summary TEXT,
            link TEXT UNIQUE,
            source TEXT,
            published TEXT,
            category TEXT,
            processed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def save_news(news_list):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    for item in news_list:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO news (title, summary, link, source, published, category)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (item['title'], item['summary'], item['link'], item['source'], 
                  item['published'], item['category']))
        except:
            pass
    conn.commit()
    conn.close()

def get_unprocessed_news(limit=50):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, summary, link, source, category 
        FROM news 
        WHERE processed = 0 
        ORDER BY published DESC 
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{'title': r[0], 'summary': r[1], 'link': r[2], 'source': r[3], 'category': r[4]} for r in rows]

def mark_as_processed(news_list):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    for item in news_list:
        cursor.execute('UPDATE news SET processed = 1 WHERE link = ?', (item['link'],))
    conn.commit()
    conn.close()

def clear_old_news(days=7):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM news WHERE processed = 1")
    conn.commit()
    conn.close()
