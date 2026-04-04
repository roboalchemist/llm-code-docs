# Convert results to scores and sort by score
movie_scores = results_to_scores(results)
top_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

```

Visualize results in Jupyter Notebook

Finally, we display the top 5 recommended movies along with their posters and titles.

```python