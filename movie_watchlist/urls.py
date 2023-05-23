from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('IMDB_API.urls')),
    path('home/', include('HOME.urls')),
    path('recommend/', include('GPT_API.urls')),
    path('accounts/', include('accounts.urls')),
]
