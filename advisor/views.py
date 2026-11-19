"""
Views for AI Advisor & Mobile Setup — Django version.
Same logic as Flask, converted to Django views.
"""
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .mobile_recommendation import get_mobile_recommendations
from .accessories import get_accessories_recommendations


def home(request):
    """Home page."""
    return render(request, 'advisor/index.html')


def recommendation_page(request):
    """
    Show BLANK form by default.
    Only show phone results AFTER user submits a budget.
    """
    has_searched = False
    budget       = ''
    usage        = 'gaming'
    processor    = 'any'
    mobiles      = []

    if request.method == 'POST':
        budget       = request.POST.get('budget', '').strip()
        usage        = request.POST.get('usage', 'gaming')
        processor    = request.POST.get('processor', 'any')
        has_searched = bool(budget)

    elif request.method == 'GET' and 'budget' in request.GET:
        budget       = request.GET.get('budget', '').strip()
        usage        = request.GET.get('usage', 'gaming')
        processor    = request.GET.get('processor', 'any')
        has_searched = bool(budget)

    if has_searched and budget:
        try:
            budget_val = float(budget)
            if budget_val > 0:
                mobiles = get_mobile_recommendations(
                    budget=budget_val,
                    usage=usage,
                    processor_pref=processor
                )
                return render(request, 'advisor/recommendation.html', {
                    'has_searched': True,
                    'mobiles': mobiles,
                    'budget': int(budget_val),
                    'usage': usage,
                    'processor': processor,
                })
        except (ValueError, TypeError):
            pass

    return render(request, 'advisor/recommendation.html', {
        'has_searched': False,
        'mobiles': [],
        'budget': '',
        'usage': usage,
        'processor': processor,
    })


def accessories_page(request):
    """Accessories recommendation based on remaining budget."""
    mobile_name  = request.GET.get('mobile_name', '')
    mobile_price = request.GET.get('mobile_price', 0)
    total_budget = request.GET.get('total_budget', 0)

    accessories  = []
    remaining    = 0
    total_spent  = 0
    summary      = {}

    try:
        mobile_price_val = float(mobile_price)
        total_budget_val = float(total_budget)
        remaining        = total_budget_val - mobile_price_val

        if remaining > 0:
            accessories = get_accessories_recommendations(budget=remaining)

        acc_total   = sum(a.get('price', 0) for a in accessories)
        total_spent = mobile_price_val + acc_total

        summary = {
            'mobile_price'      : int(mobile_price_val),
            'accessories_total' : int(acc_total),
            'total_spent'       : int(total_spent),
            'total_budget'      : int(total_budget_val),
            'savings'           : int(total_budget_val - total_spent),
        }
    except (ValueError, TypeError):
        pass

    return render(request, 'advisor/accessories.html', {
        'mobile_name'     : mobile_name,
        'mobile_price'    : mobile_price,
        'total_budget'    : total_budget,
        'remaining_budget': int(remaining),
        'accessories'     : accessories,
        'summary'         : summary,
        'total_spent'     : int(total_spent),
    })


def ai_agent_page(request):
    """AI Chatbot page."""
    return render(request, 'advisor/ai_agent.html')


@csrf_exempt
def chat_api(request):
    """Chat API endpoint for AI chatbot."""
    if request.method != 'POST':
        return JsonResponse({'reply': 'Send a POST request with your message.'})

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    message = data.get('message', '').strip().lower()

    if not message:
        return JsonResponse({'reply': 'Please ask me something! 😊'})

    reply = generate_reply(message)
    return JsonResponse({'reply': reply})


def generate_reply(msg):
    """Rule-based AI for mobile queries."""
    msg = msg.lower()

    if any(w in msg for w in ['budget', 'amount', 'price', 'cost', 'how much']):
        return ("Please tell me your budget — I will suggest the best phones in that range! 💰\n"
                "Example: 'Best phone under 15000', 'Gaming phone under ₹25k'")

    if any(w in msg for w in ['gaming', 'game', 'pubg', 'bgmi', 'cod', 'fps']):
        return ("🎮 Best Gaming Phones:\n"
                "• ₹15k – Poco M6 Pro 5G\n"
                "• ₹20k – iQOO Z9 Lite 5G\n"
                "• ₹25k – Poco X6 Pro 5G\n"
                "• ₹30k – iQOO Neo 9 Pro 5G\n"
                "Snapdragon 4 Gen 2 / Dimensity 8300 — best for gaming performance!")

    if any(w in msg for w in ['camera', 'photo', 'selfie', 'photography', 'portrait']):
        return ("📷 Best Camera Phones:\n"
                "• ₹15k – Redmi Note 13 5G (108MP)\n"
                "• ₹20k – Samsung Galaxy M35 (50MP OIS)\n"
                "• ₹30k – Vivo V30e (Sony IMX890)\n"
                "• ₹40k – Google Pixel 8a (AI Camera)")

    if any(w in msg for w in ['battery', 'charging', 'mah', 'backup', 'long lasting']):
        return ("🔋 Best Battery Phones:\n"
                "• ₹12k – Redmi 13C 5G (5000mAh)\n"
                "• ₹20k – Realme Narzo 70 Pro (5000mAh + 45W)\n"
                "• ₹25k – Samsung Galaxy A35 (5000mAh)\n"
                "• ₹35k – OnePlus Nord CE 4 (5500mAh + 100W)")

    if any(w in msg for w in ['5g', 'network', 'connectivity']):
        return ("📶 5G Phones available from just ₹10,999!\n"
                "• ₹11k – Redmi 13 5G\n"
                "• ₹15k – Poco M6 Pro 5G\n"
                "• ₹20k – Samsung Galaxy M35\n"
                "All support major 5G bands in India.")

    if any(w in msg for w in ['snapdragon', 'dimensity', 'processor', 'chip', 'exynos']):
        return ("⚡ Processor Comparison:\n"
                "• Snapdragon 4 Gen 2 — Best for gaming\n"
                "• Dimensity 7200 — Balanced performance\n"
                "• Snapdragon 695 — Budget 5G\n"
                "• Exynos 1380 — Good for everyday use\n"
                "Tell me your budget — I'll suggest the best processor for you!")

    if any(w in msg for w in ['accessories', 'cover', 'case', 'charger', 'earphone', 'setup']):
        return ("🛍️ Recommended Accessories:\n"
                "1. Tempered Glass – ₹299\n"
                "2. Shockproof Case – ₹399\n"
                "3. 65W GaN Fast Charger – ₹899\n"
                "4. TWS Earbuds – ₹999\n"
                "5. 10,000mAh Power Bank – ₹999")

    if any(w in msg for w in ['compare', 'vs', 'difference', 'better', 'which']):
        return ("📊 To compare phones, please tell me:\n"
                "• Your budget range\n"
                "• Primary use (gaming / camera / battery)\n"
                "I will pick the best option for you!")

    if any(w in msg for w in ['hello', 'hi', 'hey', 'good morning', 'good evening', 'greetings']):
        return ("Hello! 👋 I am your AI Mobile Advisor.\n"
                "Tell me your budget or ask me anything:\n"
                "• Best gaming phone under ₹20k?\n"
                "• Best camera phone under ₹25k?\n"
                "• 5G phone under ₹15k?")

    return ("Sorry, I could not understand that question. 🤔\n"
            "You can ask me:\n"
            "• 'Best phone under ₹20000'\n"
            "• 'Suggest a gaming phone'\n"
            "• 'Best camera phone under ₹25k'\n"
            "• 'Compare Snapdragon vs Dimensity'")
