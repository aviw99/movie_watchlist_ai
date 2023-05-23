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
        api_url, description = generate_text(input_text)

        response = requests.get(api_url)
        try:
            api_data = response.json()
            movies = api_data['results'][:1]
            return render(request, 'recommendations.html', {'movies': movies, 'input_text': input_text, 'description': description})
        except KeyError:
            error_message = 'No movies found'
            print(error_message)
            return render(request, 'recommendations.html', {'error_message': error_message})
    else:
        return render(request, 'recommendations.html')


def generate_text(input_text):

    openai.api_key = ' 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'
    prompt = "Based on the following user input generate a url link for making API calls to the IMDB API" \
             "The url should be for movie recommendations or for tv show recommendations." \
             "If the user doesn't specify which, it should be for movies" \
             "Unless based on context it is clear they want a tv show" \
             "First you will determine if the user wants a movie or tv show" \
             "Then, based on their input, you will determine the most relevant titles" \
             "If the user inputs a specific title, don't include that title in your suggestion unless it's implied that"\
             "they want to view that title or something in it's franchise" \
             "They must be titles of existing movies or tv series" \
             "You will put those titles along with my IMDB API key into appropriate links which you will then output" \
             "Here is my IMDB API key 'k_kjg95dy6'" \
             "Use this link 'https://imdb-api.com/API/Search/[api key]/[title]'" \
             "Make sure to fix any spelling errors before generating the urls" \
             "In addition to the url, generate an extensive description" \
             "The description should include plot summary, actors, director, IMDB rating and public reception etc. of "\
             "the given title" \
             "Your output will be cleaned so that the url is saved to a variable" \
             "The rest of your output will be saved to a separate variable and displayed as the description" \
             "Use this format: Description: [description] [url]" \
             "Here's an example: Description: Seinfeld is an American sitcom about a group of friends living in " \
             "New York City. Follow Jerry Seinfeld, Elaine Benes, " \
             "George Costanza and Kramer as they explore the eccentricities of life. " \
             "https://imdb-api.com/en/API/Search/[api key]/seinfeld" \
             "The length of the description cannot exceed 100 - the length of the url" \
             f"User input: {input_text}"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=130
    )

    generated_text = response.choices[0].text.strip()
    api_url = re.findall(r'(https?://\S+)', generated_text)[0]
    description_start = 'Description:'
    description_end = api_url if api_url in generated_text else ''
    description = generated_text[generated_text.index(description_start) + len(description_start):generated_text.index(description_end)].strip()
    return api_url, description
