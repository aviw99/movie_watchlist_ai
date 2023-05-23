from django.shortcuts import render
import requests


# Create your views here.
def theaters_list_view(request):
    url = "https://imdb-api.com/en/API/InTheaters/k_kjg95dy6"
    response = requests.get(url)
    data = response.json()
    theaters = data['items']
    return render(request, 'theaters_list.html', {'theaters': theaters})


def movies_list_view(request):
    url = "https://imdb-api.com/en/API/Top250Movies/k_kjg95dy6"
    response = requests.get(url)
    data = response.json()
    movies = data['items']
    return render(request, 'movies_list.html', {'movies': movies})


def coming_soon_view(request):
    url = "https://imdb-api.com/en/API/ComingSoon/k_kjg95dy6"
    response = requests.get(url)
    data = response.json()
    soon = data['items']
    return render(request, 'coming_soon.html', {'soon': soon})


def shows_list_view(request):
    url = "https://imdb-api.com/en/API/Top250TVs/k_kjg95dy6"
    response = requests.get(url)
    data = response.json()
    shows = data['items']
    return render(request, 'shows_list.html', {'shows': shows})


def search_results_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        api_key = 'k_kjg95dy6'
        url = f'https://imdb-api.com/en/API/SearchAll/{api_key}/{search_query}'
        response = requests.get(url)
        data = response.json()
        search_results = data.get('results', [])

        return render(request, 'search_results.html', {'search_results': search_results})

    return render(request, 'search_results.html')


def my_movies_view(request):
    return render(request, 'my_movies.html')


def my_shows_view(request):
    return render(request, 'my_shows.html')