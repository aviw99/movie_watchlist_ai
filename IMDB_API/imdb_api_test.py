import requests
import json


def movie_test():
    new_url = "https://imdb-api.com/en/API/k_kjg95dy6/Search/Movie/Comedy/1/10"
    new_payload = {}
    new_headers = {}

    my_response = requests.get(new_url, headers=new_headers, data=new_payload)

    if my_response.status_code == 200:
        my_data = my_response.json()
        movie_data = []

        for item in my_data['items']:
            title_year = item['fullTitle']
            imdb_ranking = item['imDbRating']
            image = item['image']
            movie_data.append({'title/year': title_year, 'IMDB_ranking': imdb_ranking, 'image': image})
            print(title_year)
            # print(json.dumps(item, indent=4))
            # Process the data as per your requirements
    else:
        print("Error occurred:", my_response.status_code)


movie_test()

