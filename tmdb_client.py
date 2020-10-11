import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjljYTA2OTUzZTMwNjBjYzE4ODY2MmRhNGNjNzU5YyIsInN1YiI6IjVmODIwMTMwMDI4NDIwMDAzODBmYjA0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RGx07Vgha4XDgPe4wEYtjTY3oKtoMjyLOl8tNksWyHQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"