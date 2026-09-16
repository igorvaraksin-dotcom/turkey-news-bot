import config
from datetime import datetime
import requests

def translate_text(text, target_lang='uk'):
    """Переклад через Google Translate"""
    if not text or len(text) < 10:
        return text
    
    lang_map = {'uk': 'uk', 'ru': 'ru', 'tr': 'tr', 'en': 'en'}
    target = lang_map.get(target_lang, 'uk')
    
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target}&dt=t&q={text[:500]}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            translated = ''.join([s[0] for s in result[0] if s[0]])
            return translated.strip() if translated else text
    except:
        pass
    
    return text

def generate_digest(news_list, language='uk'):
    categories = {
        'politics': [],
        'economy': []
    }
    
    for item in news_list:
        cat = item['category']
        if cat in categories:
            categories[cat].append(item)
    
    today = datetime.now().strftime('%d %B %Y')
    
    if language == 'uk':
        title = f"🇹🇷 Новини Туреччини — {today}"
        cat_names = {
            'politics': '🔹 Політика',
            'economy': '💰 Економіка'
        }
    elif language == 'ru':
        title = f"🇹🇷 Новости Турции — {today}"
        cat_names = {
            'politics': '🔹 Политика',
            'economy': '💰 Экономика'
        }
    elif language == 'tr':
        title = f"🇹🇷 Türkiye Haberleri — {today}"
        cat_names = {
            'politics': '🔹 Politika',
            'economy': '💰 Ekonomi'
        }
    else:
        title = f"🇹🇷 Turkey News — {today}"
        cat_names = {
            'politics': '🔹 Politics',
            'economy': '💰 Economy'
        }
    
    digest = f"*{title}*\n\n"
    
    for cat_key, cat_name in cat_names.items():
        items = categories[cat_key][:15]  # до 15 новин на категорію
        if items:
            digest += f"{cat_name}\n"
            for item in items:
                translated_title = translate_text(item['title'], language)
                short_title = translated_title[:140]
                source_short = item['source'][:25]
                digest += f"• {short_title} [{source_short}]\n"
                digest += f"  {item['link']}\n\n"
            digest += "\n"
    
    return digest