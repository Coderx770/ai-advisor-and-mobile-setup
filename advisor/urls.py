"""
URL patterns for the advisor app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommendation/', views.recommendation_page, name='recommendation'),
    path('accessories/', views.accessories_page, name='accessories'),
    path('ai-agent/', views.ai_agent_page, name='ai_agent'),
    path('api/chat/', views.chat_api, name='chat_api'),
]
