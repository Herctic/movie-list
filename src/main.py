""" Main requests file

needs to be able to:
    * search and display search results
        * display anything that is obfuscated by tmdb's id system (just genres for now...)
    * send saved movies into the db
    * send ratings from individuals
    * gather rottentomatoes tomatometer and audience score
    * gather rogerebert ratings? (maybe not possible without an html scraper)

"""

import os
import requests
from dotenv import load_dotenv
from rotten_tomatoes_scraper.rt_scraper import MovieScraper

load_dotenv()
tmdb_key = os.environ['TMDB_KEY']

# getting tmdb config info for poster data
base_url = requests.get("https://api.themoviedb.org/3/configuration", {'api_key': tmdb_key}).json()['images']['base_url']
# print(base_url)
poster_size = 'w342'
poster_path = '/izrHg2UzxG3YXTBcKFaUbYp9LWA.jpg'
test_image = f'{base_url}{poster_size}{poster_path}'
# print(test_image)


def gather_ids():
    ''' used to gather genre ids
    only necessary when display on the frontend
    returns:
        genre_dict = {int(id): str(genre_name)}
    '''

    params = {
        'api_key': tmdb_key,
    }
    r = requests.get("https://api.themoviedb.org/3/genre/movie/list", params)

    genre_dict = {}
    for genre in r.json()['genres']:
        genre_dict[genre['id']] = genre['name']
    return genre_dict


def search_movies(query):
    ''' returns a list of movies that match the query
    returns:
        movie_list: [
            {
                "adult": false,
                "backdrop_path": "/xVHu86MkmtfsgKzLOaG7nCbeZpP.jpg",
                "genre_ids": [
                    53,
                    9648,
                    878,
                    27
                ],
                "id": 795518,
                "original_language": "en",
                "original_title": "Broadcast Signal Intrusion",
                "overview": "In the late 90s, a video...",
                "popularity": 4.851,
                "poster_path": "/472jgGaEB02ZQSWKqtl5DUqBJP7.jpg",
                "release_date": "2021-10-22",
                "title": "Broadcast Signal Intrusion",
                "video": false,
                "vote_average": 0,
                "vote_count": 0
            },
        ]
    '''
    
    params = {
        'api_key': tmdb_key,
        'query': str(query),
        'page': 1,
        'include_adult': False
    }
    r = requests.get("https://api.themoviedb.org/3/search/movie", params)
    return r.json().get('results', {'response': '400'})


def main():
    tmdb_url = 'https://api.themoviedb.org/3/'
    params = {
        'api_key': tmdb_key,
    }
    r = requests.get(f'{tmdb_url}', params)


if __name__ == '__main__':
    # main(gather_ids())
    print(search_movies('skyfall'))
