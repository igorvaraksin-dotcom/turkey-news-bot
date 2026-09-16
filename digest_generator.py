from datetime import datetime
import requests

def translate_text(text, target_lang='uk'):
    if not text or len(text) < 10:
        return text
    
    target = 'uk' if target_lang == 'uk' else 'ru'
    
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
    categories = {'politics': [], 'economy': []}
    
    for item in news_list:
        cat = item['category']
        if cat in categories:
            categories[cat].append(item)
    
    today = datetime.now().strftime('%d %B %Y')
    title = f"🇹🇷 Новини Туреччини — {today}" if language == 'uk' else f"🇹🇷 Новости Турции — {today}"
    
    cat_names_uk = {'politics': '🔹 Політика', 'economy': '💰 Економіка'}
    cat_names_ru = {'politics': '🔹 Политика', 'economy': '💰 Экономика'}
    cat_names = cat_names_uk if language == 'uk' else cat_names_ru
    
    digest = f"*{title}*\n\n"
    
    for cat_key, cat_name in cat_names.items():
        items = categories[cat_key][:15]
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
