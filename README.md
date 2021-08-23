# Movie List Idea

## How It Works

* Utilizing the TMDB API to gather info about movies from our movie list
    * **Discovery** - Gathering info about a movie that we query
        * **General Info** - Synopsis, Year, Tagline, Images
        * **Recommendations** - Who recommended (list of thumbs ups with names attached)
    * **Addition** - Adding the movie to the list


## Tools/Packages
* [TMDB API](https://developers.themoviedb.org/3/) - For general/streaming info
* [Rotten Tomatoes Client Library](https://pypi.org/project/rotten_tomatoes_client/) - For RT ratings


### API Examples
```
https://api.themoviedb.org/3/discover/movie?api_key=<<api_key>>&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&year=2020&with_watch_monetization_types=flatrate
```