# Convert results to scores and sort by score
def results_to_scores(results):
    movie_scores = defaultdict(lambda: 0)
    for result in results:
        for movie_id in result.payload["movie_id"]:
            movie_scores[movie_id] += result.score
    return movie_scores