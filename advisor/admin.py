from django.contrib import admin
from .models import SearchHistory, UserSetup, ChatHistory

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'budget', 'usage', 'processor', 'top_recommended_phone', 'created_at')
    list_filter = ('usage', 'processor', 'created_at')
    search_fields = ('top_recommended_phone', 'budget')

@admin.register(UserSetup)
class UserSetupAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile_name', 'mobile_price', 'total_budget', 'total_spent', 'savings', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('mobile_name',)

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_message', 'created_at')
    search_fields = ('user_message', 'bot_reply')
