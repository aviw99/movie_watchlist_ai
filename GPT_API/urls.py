from django.urls import path
from .views import recommendations_view, recommend_view

urlpatterns = [
    path('recommendations/', recommendations_view, name='recommendations'),
    path('get_recommendation', recommend_view, name='gpt_recommend'),
]