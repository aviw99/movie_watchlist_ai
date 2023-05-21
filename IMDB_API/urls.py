from django.urls import path
from .views import movies_list_view, shows_list_view, theaters_list_view, coming_soon_view, search_results_view,\
    my_movies_view, my_shows_view

urlpatterns = [
    path('theaters/', theaters_list_view, name='theaters'),
    path('movies/', movies_list_view, name='movies'),
    path('coming_soon/', coming_soon_view, name='soon'),
    path('shows/', shows_list_view, name='shows'),
    path('my_movies/', my_movies_view, name='my-movies'),
    path('my_shows/', my_shows_view, name='my-shows'),
    path('search_results/', search_results_view, name='search'),
]