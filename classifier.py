import config

# Слова для виключення (спорт, розваги, пригоди, землетруси тощо)
EXCLUDE_KEYWORDS = [
    # Спорт
    'beşiktaş', 'galatasaray', 'fenerbahçe', 'trabzonspor', 'başakşehir',
    'tennis', 'tenis', 'futbol', 'basketbol', 'voleybol', 'maç', 'gol',
    'şampiyon', 'lig', 'kupa', 'transfer', 'oyuncu', 'antrenör', 'derbi',
    # Розваги
    'sinema', 'dizi', 'magazin', 'ünlü', 'şarkıcı', 'oyuncu', 'konser', 'festival',
    # Пригоди/катастрофи
    'deprem', 'zelzele', 'afet', 'kaza', 'yangın', 'sel', 'toprak kayması',
    'çökme', 'patlama', 'trafik kazası', 'intihar', 'cinayet', 'hırsızlık',
    'dolandırıcı', 'kayıp', 'arama kurtarma',
    # Погода
    'hava durumu', 'meteoroloji', 'sıcaklık', 'yağmur', 'kar', 'fırtına',
    # Інше
    'yemek', 'tarif', 'restoran', 'kafe', 'sağlık', 'hastane', 'doktor', 'aşı'
]

def is_relevant(text, language='uk'):
    text_lower = text.lower()
    
    # Виключаємо спорт, розваги, пригоди тощо
    if any(kw in text_lower for kw in EXCLUDE_KEYWORDS):
        return False
    
    return True

def classify_category(text):
    text_lower = text.lower()
    
    # Економіка (пріоритет)
    economy_keywords = [
        'ekonomi', 'economy', 'ekonomi', 'enflasyon', 'inflation', 'faiz', 'interest rate',
        'lira', 'tl ', 'dolar', 'euro', 'borsa', 'hisse', 'bank', 'banka',
        'merkez bankası', 'central bank', 'bütçe', 'budget', 'vergi', 'tax',
        'işsizlik', 'unemployment', 'büyüme', 'growth', 'gdp', 'gsyh',
        'ticaret', 'trade', 'ihracat', 'export', 'ithalat', 'import',
        'yatırım', 'investment', 'şirket', 'company', 'fabrika', 'factory',
        'ücret', 'wage', 'maaş', 'salary', 'zam', 'raise', 'emekli', 'pension'
    ]
    
    if any(kw in text_lower for kw in economy_keywords):
        return 'economy'
    
    # Політика (за замовчуванням)
    return 'politics'

def filter_and_classify(news_list, language='uk'):
    filtered = []
    for item in news_list:
        combined_text = f"{item['title']} {item['summary']}"
        
        # Фільтруємо непотрібні теми
        if not is_relevant(combined_text, language):
            continue
        
        item['category'] = classify_category(combined_text)
        filtered.append(item)
    
    return filtered