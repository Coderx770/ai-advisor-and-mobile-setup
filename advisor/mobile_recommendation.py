"""
Mobile Recommendation Engine — Scores and ranks phones within user's budget.
Uses a scoring algorithm based on budget fit, usage match, and specifications.
"""

PHONES = [
    # ── Under ₹15,000 ──────────────────────────────────────────
    {"name": "Redmi 13 5G", "brand": "Xiaomi", "price": 10999, "processor": "Snapdragon 4 Gen 2", "processor_type": "snapdragon", "ram": 4, "storage": 128, "battery": 5000, "camera": 50, "display": "6.79\" HD+ 90Hz", "usage_tags": ["general", "battery", "5g"]},
    {"name": "Poco M6 5G", "brand": "Poco", "price": 11999, "processor": "Snapdragon 4 Gen 2", "processor_type": "snapdragon", "ram": 6, "storage": 128, "battery": 5000, "camera": 50, "display": "6.74\" HD+ 90Hz", "usage_tags": ["gaming", "general"]},
    {"name": "Realme Narzo 70x 5G", "brand": "Realme", "price": 12999, "processor": "Dimensity 6100+", "processor_type": "dimensity", "ram": 6, "storage": 128, "battery": 5000, "camera": 50, "display": "6.67\" FHD+ 120Hz", "usage_tags": ["gaming", "battery"]},
    {"name": "Redmi Note 13 5G", "brand": "Xiaomi", "price": 14999, "processor": "Snapdragon 4 Gen 2", "processor_type": "snapdragon", "ram": 6, "storage": 128, "battery": 5000, "camera": 108, "display": "6.67\" FHD+ 120Hz AMOLED", "usage_tags": ["camera", "gaming", "general"]},

    # ── ₹15,000–₹20,000 ────────────────────────────────────────
    {"name": "Poco X6 Neo 5G", "brand": "Poco", "price": 16999, "processor": "Dimensity 6080", "processor_type": "dimensity", "ram": 8, "storage": 256, "battery": 5000, "camera": 108, "display": "6.67\" FHD+ 120Hz AMOLED", "usage_tags": ["camera", "gaming"]},
    {"name": "Samsung Galaxy M35", "brand": "Samsung", "price": 17999, "processor": "Exynos 1380", "processor_type": "exynos", "ram": 6, "storage": 128, "battery": 6000, "camera": 50, "display": "6.7\" FHD+ 120Hz AMOLED", "usage_tags": ["battery", "camera", "business"]},
    {"name": "iQOO Z9 Lite 5G", "brand": "iQOO", "price": 17999, "processor": "Snapdragon 4 Gen 2", "processor_type": "snapdragon", "ram": 8, "storage": 128, "battery": 5000, "camera": 50, "display": "6.72\" FHD+ 120Hz AMOLED", "usage_tags": ["gaming", "general"]},
    {"name": "Realme P1 Pro 5G", "brand": "Realme", "price": 19999, "processor": "Snapdragon 6 Gen 1", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5000, "camera": 50, "display": "6.7\" FHD+ 120Hz AMOLED", "usage_tags": ["gaming", "camera"]},

    # ── ₹20,000–₹30,000 ────────────────────────────────────────
    {"name": "OnePlus Nord CE 4 Lite", "brand": "OnePlus", "price": 19999, "processor": "Snapdragon 695", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5500, "camera": 50, "display": "6.67\" FHD+ 120Hz", "usage_tags": ["battery", "general", "business"]},
    {"name": "Poco X6 Pro 5G", "brand": "Poco", "price": 22999, "processor": "Dimensity 8300", "processor_type": "dimensity", "ram": 8, "storage": 256, "battery": 5000, "camera": 64, "display": "6.67\" FHD+ 120Hz AMOLED", "usage_tags": ["gaming", "camera"]},
    {"name": "iQOO Z9s Pro 5G", "brand": "iQOO", "price": 24999, "processor": "Snapdragon 7s Gen 3", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5000, "camera": 50, "display": "6.77\" FHD+ 144Hz AMOLED", "usage_tags": ["gaming", "camera"]},
    {"name": "Samsung Galaxy A55", "brand": "Samsung", "price": 26999, "processor": "Exynos 1480", "processor_type": "exynos", "ram": 8, "storage": 128, "battery": 5000, "camera": 50, "display": "6.6\" FHD+ 120Hz AMOLED", "usage_tags": ["camera", "business", "general"]},
    {"name": "Nothing Phone 2a", "brand": "Nothing", "price": 23999, "processor": "Dimensity 7200 Pro", "processor_type": "dimensity", "ram": 8, "storage": 256, "battery": 5000, "camera": 50, "display": "6.7\" FHD+ 120Hz AMOLED", "usage_tags": ["general", "camera"]},

    # ── ₹30,000–₹50,000 ────────────────────────────────────────
    {"name": "OnePlus Nord 4", "brand": "OnePlus", "price": 29999, "processor": "Snapdragon 7+ Gen 3", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5500, "camera": 50, "display": "6.74\" FHD+ 120Hz AMOLED", "usage_tags": ["gaming", "battery", "business"]},
    {"name": "iQOO Neo 9 Pro", "brand": "iQOO", "price": 33999, "processor": "Snapdragon 8 Gen 2", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5160, "camera": 50, "display": "6.78\" FHD+ 144Hz AMOLED", "usage_tags": ["gaming", "camera"]},
    {"name": "Google Pixel 8a", "brand": "Google", "price": 39999, "processor": "Google Tensor G3", "processor_type": "other", "ram": 8, "storage": 128, "battery": 4492, "camera": 64, "display": "6.1\" FHD+ 120Hz OLED", "usage_tags": ["camera", "business", "general"]},
    {"name": "Vivo V30 Pro", "brand": "Vivo", "price": 37999, "processor": "Snapdragon 7 Gen 3", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5000, "camera": 50, "display": "6.78\" FHD+ 120Hz AMOLED", "usage_tags": ["camera", "business"]},
    {"name": "Samsung Galaxy S23 FE", "brand": "Samsung", "price": 34999, "processor": "Snapdragon 8 Gen 1", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 4500, "camera": 50, "display": "6.4\" FHD+ 120Hz OLED", "usage_tags": ["gaming", "camera", "business"]},

    # ── ₹50,000+ ───────────────────────────────────────────────
    {"name": "OnePlus 12R", "brand": "OnePlus", "price": 39999, "processor": "Snapdragon 8 Gen 2", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 5500, "camera": 50, "display": "6.78\" QHD+ 120Hz AMOLED", "usage_tags": ["gaming", "battery"]},
    {"name": "iQOO 12", "brand": "iQOO", "price": 52999, "processor": "Snapdragon 8 Gen 3", "processor_type": "snapdragon", "ram": 12, "storage": 256, "battery": 5000, "camera": 50, "display": "6.78\" QHD+ 144Hz AMOLED", "usage_tags": ["gaming", "camera"]},
    {"name": "Samsung Galaxy S24", "brand": "Samsung", "price": 64999, "processor": "Snapdragon 8 Gen 3", "processor_type": "snapdragon", "ram": 8, "storage": 256, "battery": 4000, "camera": 50, "display": "6.2\" FHD+ 120Hz OLED", "usage_tags": ["camera", "business", "gaming"]},
    {"name": "OnePlus 12", "brand": "OnePlus", "price": 64999, "processor": "Snapdragon 8 Gen 3", "processor_type": "snapdragon", "ram": 12, "storage": 256, "battery": 5400, "camera": 50, "display": "6.82\" QHD+ 120Hz AMOLED", "usage_tags": ["gaming", "battery", "camera"]},
]


def score_mobile(phone, budget, usage, processor_pref):
    """Score a phone based on budget, usage, and processor preference."""
    # STRICT: Phone over budget = REJECTED
    if phone['price'] > budget:
        return -999999

    score = 0

    # Budget utilization (higher is better, up to 100% of budget)
    utilization = phone['price'] / budget
    score += utilization * 50

    # Usage match
    if usage in phone.get('usage_tags', []):
        score += 30

    # Processor match
    if processor_pref != 'any' and phone['processor_type'] == processor_pref:
        score += 20

    # Specs bonus
    score += min(phone['ram'], 12) * 1.5
    score += min(phone['storage'], 256) * 0.05
    score += min(phone['battery'], 6000) / 1000 * 2
    score += min(phone['camera'], 108) * 0.1

    return score


def get_mobile_recommendations(budget=None, usage='general', processor_pref='any', top_n=6):
    """Return top N phones within budget, ranked by score."""
    if not budget or budget <= 0:
        return []

    scored = []
    for phone in PHONES:
        s = score_mobile(phone, budget, usage, processor_pref)
        if s > -999999:
            p = dict(phone)
            p['score'] = round(s, 1)
            scored.append(p)

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_n]
