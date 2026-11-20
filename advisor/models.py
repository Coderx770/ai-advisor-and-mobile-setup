from django.db import models

class SearchHistory(models.Model):
    """Stores user search queries from the Recommendation page."""
    budget = models.IntegerField(help_text="User entered budget in INR")
    usage = models.CharField(max_length=50, default="gaming")
    processor = models.CharField(max_length=50, default="any")
    top_recommended_phone = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Search Query"
        verbose_name_plural = "User Search Queries"
        ordering = ['-created_at']

    def __str__(self):
        return f"₹{self.budget} ({self.usage}) - Top: {self.top_recommended_phone or 'None'}"


class UserSetup(models.Model):
    """Stores finalized phone and accessories selection."""
    mobile_name = models.CharField(max_length=150)
    mobile_price = models.IntegerField()
    total_budget = models.IntegerField()
    remaining_budget = models.IntegerField()
    total_spent = models.IntegerField(default=0)
    savings = models.IntegerField(default=0)
    accessories_list = models.TextField(blank=True, help_text="Comma-separated accessories")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mobile & Accessory Setup"
        verbose_name_plural = "User Saved Setups"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.mobile_name} (Total: ₹{self.total_budget}, Saved: ₹{self.savings})"


class ChatHistory(models.Model):
    """Stores AI Chatbot queries and responses."""
    user_message = models.TextField()
    bot_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chat Query"
        verbose_name_plural = "AI Chat History"
        ordering = ['-created_at']

    def __str__(self):
        return f"Q: {self.user_message[:40]}... [{self.created_at.strftime('%d-%m %H:%M')}]"
