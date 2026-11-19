"""
Accessories Recommendation Engine — Selects best accessories within remaining budget.
Uses a greedy algorithm with priority-based selection.
"""

ACCESSORIES = [
    {"name": "Tempered Glass (Screen Guard)", "category": "Protection",  "price": 299,  "emoji": "🛡️"},
    {"name": "Shockproof Back Cover",          "category": "Protection",  "price": 349,  "emoji": "📱"},
    {"name": "Type-C Charging Cable (2m)",     "category": "Charging",    "price": 299,  "emoji": "🔌"},
    {"name": "Mobile Stand / Holder",          "category": "Comfort",     "price": 349,  "emoji": "🖥️"},
    {"name": "Pop Socket Grip",                "category": "Comfort",     "price": 199,  "emoji": "💫"},
    {"name": "Screen Cleaning Kit",            "category": "Maintenance", "price": 149,  "emoji": "🧹"},
    {"name": "OTG Adapter",                    "category": "Utility",     "price": 199,  "emoji": "🔧"},
    {"name": "Neck Strap / Lanyard",           "category": "Comfort",     "price": 199,  "emoji": "🎀"},
    {"name": "Earphones (Wired)",              "category": "Audio",       "price": 499,  "emoji": "🎧"},
    {"name": "Car Phone Mount",                "category": "Utility",     "price": 449,  "emoji": "🚗"},
    {"name": "20W Fast Charger",               "category": "Charging",    "price": 599,  "emoji": "⚡"},
    {"name": "5000mAh Power Bank",             "category": "Charging",    "price": 799,  "emoji": "🔋"},
    {"name": "TWS Wireless Earbuds",           "category": "Audio",       "price": 999,  "emoji": "🎵"},
    {"name": "10,000mAh Power Bank",           "category": "Charging",    "price": 999,  "emoji": "🔋"},
    {"name": "Bluetooth Speaker",              "category": "Audio",       "price": 1299, "emoji": "🔊"},
    {"name": "Wireless Charger 15W",           "category": "Charging",    "price": 1299, "emoji": "📡"},
]

PRIORITY_ORDER = [
    "Tempered Glass (Screen Guard)",
    "Shockproof Back Cover",
    "Type-C Charging Cable (2m)",
    "Mobile Stand / Holder",
    "Pop Socket Grip",
    "Screen Cleaning Kit",
    "OTG Adapter",
    "Neck Strap / Lanyard",
    "Earphones (Wired)",
    "Car Phone Mount",
    "20W Fast Charger",
    "5000mAh Power Bank",
    "TWS Wireless Earbuds",
    "10,000mAh Power Bank",
    "Bluetooth Speaker",
    "Wireless Charger 15W",
]


def get_accessories_recommendations(budget=0):
    """
    Select accessories that fit within the REMAINING budget.
    Uses greedy approach: pick priority items one by one until budget runs out.
    """
    if not budget or budget <= 0:
        return []

    sorted_acc = sorted(
        ACCESSORIES,
        key=lambda x: PRIORITY_ORDER.index(x['name'])
        if x['name'] in PRIORITY_ORDER else 99
    )

    selected = []
    spent    = 0

    for item in sorted_acc:
        if spent + item['price'] <= budget:
            selected.append(dict(item))
            spent += item['price']

    return selected
