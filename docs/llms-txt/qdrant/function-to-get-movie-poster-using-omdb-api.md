# Function to get movie poster using OMDB API
def get_movie_poster(imdb_id, api_key):
    url = f"https://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    data = requests.get(url).json()
    return data.get('Poster'), data

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#prepare-the-data) Prepare the data

Load the movie datasets. These include three main CSV files: user ratings, movie titles, and OMDB IDs.

```python