EXCLUDE_KEYWORDS = [
    'beşiktaş', 'galatasaray', 'fenerbahçe', 'trabzonspor',
    'tenis', 'futbol', 'basketbol', 'maç', 'gol', 'şampiyon',
    'sinema', 'dizi', 'magazin', 'ünlü', 'şarkıcı',
    'deprem', 'kaza', 'yangın', 'sel', 'intihar', 'cinayet',
    'hava durumu', 'meteoroloji', 'yemek', 'tarif'
]

def is_relevant(text):
    text_lower = text.lower()
    if any(kw in text_lower for kw in EXCLUDE_KEYWORDS):
        return False
    return True

def classify_category(text):
    text_lower = text.lower()
    economy_keywords = ['ekonomi', 'enflasyon', 'faiz', 'lira', 'dolar', 'euro', 'borsa', 'bank', 'merkez bankası', 'bütçe', 'işsizlik', 'maaş', 'zam']
    
    if any(kw in text_lower for kw in economy_keywords):
        return 'economy'
    return 'politics'

def filter_and_classify(news_list):
    filtered = []
    for item in news_list:
        combined_text = f"{item['title']} {item['summary']}"
        if not is_relevant(combined_text):
            continue
        item['category'] = classify_category(combined_text)
        filtered.append(item)
    return filtered
