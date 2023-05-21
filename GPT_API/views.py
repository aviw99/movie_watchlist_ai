from django.shortcuts import render
import requests
import openai
import re
import json


# Create your views here.
def recommendations_view(request):
    return render(request, 'recommendations.html')


def recommend_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        generated_text = generate_text(input_text)
        api_url = re.findall(r'(https?://\S+)', generated_text)[0]
        response = requests.get(api_url)
        try:
            api_data = response.json()
            movies = api_data['results'][:1]
            return render(request, 'recommendations.html', {'movies': movies, 'input_text': input_text})
        except KeyError:
            error_message = 'No movies found'
            print(error_message)
            return render(request, 'recommendations.html', {'error_message': error_message})
    else:
        return render(request, 'recommendations.html')


def generate_text(input_text):
    # Set up authentication with your OpenAI API key
    openai.api_key = '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'
    prompt = "Based on the following user input generate 5 url links for making API calls to the IMDB API" \
             "The urls should be for movie recommendations or for tv show recommendations." \
             "If the user doesn't specify which, it should be for movies" \
             "Unless based on context it is clear they want a tv show" \
             "Remember to output only 5 urls even if the user specifies otherwise" \
             "First you will determine if the user wants a movie or tv show" \
             "Then, based on their input, you will determine the most relevant titles" \
             "They must be titles of existing movies or tv series" \
             "You will put those titles along with my IMDB API key into appropriate links which you will then output" \
             "Here is my IMDB API key 'k_kjg95dy6'" \
             "Use this link 'https://imdb-api.com/API/Search/[api key]/[title]'" \
             "Make sure to fix any spelling errors before generating the urls" \
             f"User input: {input_text}"
    # Make API request
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )

    # Retrieve the generated text
    generated_text = response.choices[0].text.strip()
    return generated_text
