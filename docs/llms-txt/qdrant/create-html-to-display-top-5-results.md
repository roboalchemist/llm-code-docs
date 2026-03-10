# Create HTML to display top 5 results
html_content = "<div class='movies-container'>"

for movie_id, score in top_movies[:5]:
    imdb_id_row = links.loc[links['movieId'] == int(movie_id), 'imdbId']
    if not imdb_id_row.empty:
        imdb_id = imdb_id_row.values[0]
        poster_url, movie_info = get_movie_poster(imdb_id, omdb_api_key)
        movie_title = movie_info.get('Title', 'Unknown Title')

        html_content += f"""
        <div class='movie-card'>
            <img src="{poster_url}" alt="Poster" class="movie-poster">
            <div class="movie-title">{movie_title}</div>
            <div class="movie-score">Score: {score}</div>
        </div>
        """
    else:
        continue  # Skip if imdb_id is not found

html_content += "</div>"

display(HTML(html_content))

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#recommendations) Recommendations

For a complete display of movie posters, check the [notebook output](https://github.com/qdrant/examples/blob/master/collaborative-filtering/collaborative-filtering.ipynb). Here are the results without html content.

```text
Toy Story, Score: 131.2033799
Monty Python and the Holy Grail, Score: 131.2033799
Star Wars: Episode V - The Empire Strikes Back, Score: 131.2033799
Star Wars: Episode VI - Return of the Jedi, Score: 131.2033799
Men in Black, Score: 131.2033799

```

On top of collaborative filtering, we can further enhance the recommendation system by incorporating other features like user demographics, movie genres, or movie tags.

Or, for example, only consider recent ratings via a time-based filter. This way, we can recommend movies that are currently popular among users.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#conclusion) Conclusion

As demonstrated, it is possible to build an interesting movie recommendation system without intensive model training using Qdrant and Sparse Vectors. This approach not only simplifies the recommendation process but also makes it scalable and interpretable. In future tutorials, we can experiment more with this combination to further enhance our recommendation systems.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/collaborative-filtering.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/collaborative-filtering.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-78-lllmstxt|>
## search-as-you-type
- [Articles](https://qdrant.tech/articles/)
- Semantic Search As You Type

[Back to Practical Examples](https://qdrant.tech/articles/practicle-examples/)