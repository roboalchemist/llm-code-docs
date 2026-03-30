# Convert movieId in ratings_df and movies_df to string
ratings_df['movieId'] = ratings_df['movieId'].astype(str)
movies_df['movieId'] = movies_df['movieId'].astype(str)

rating = ratings_df['rating']