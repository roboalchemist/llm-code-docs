# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#use-collaborative-filtering-to-build-a-movie-recommendation-system-with-qdrant) Use Collaborative Filtering to Build a Movie Recommendation System with Qdrant

| Time: 45 min | Level: Intermediate | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/master/collaborative-filtering/collaborative-filtering.ipynb) |  |
| --- | --- | --- | --- |

Every time Spotify recommends the next song from a band you’ve never heard of, it uses a recommendation algorithm based on other users’ interactions with that song. This type of algorithm is known as **collaborative filtering**.

Unlike content-based recommendations, collaborative filtering excels when the objects’ semantics are loosely or unrelated to users’ preferences. This adaptability is what makes it so fascinating. Movie, music, or book recommendations are good examples of such use cases. After all, we rarely choose which book to read purely based on the plot twists.

The traditional way to build a collaborative filtering engine involves training a model that converts the sparse matrix of user-to-item relations into a compressed, dense representation of user and item vectors. Some of the most commonly referenced algorithms for this purpose include [SVD (Singular Value Decomposition)](https://en.wikipedia.org/wiki/Singular_value_decomposition) and [Factorization Machines](https://en.wikipedia.org/wiki/Matrix_factorization_%28recommender_systems%29). However, the model training approach requires significant resource investments. Model training necessitates data, regular re-training, and a mature infrastructure.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#methodology) Methodology

Fortunately, there is a way to build collaborative filtering systems without any model training. You can obtain interpretable recommendations and have a scalable system using a technique based on similarity search. Let’s explore how this works with an example of building a movie recommendation system.

Recommendation system with Qdrant and sparse vectors (Collaborative Filtering) - YouTube

[Photo image of Qdrant - Vector Database & Search Engine](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA?embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

Qdrant - Vector Database & Search Engine

8.12K subscribers

[Recommendation system with Qdrant and sparse vectors (Collaborative Filtering)](https://www.youtube.com/watch?v=9B7RrmQCQeQ)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=9B7RrmQCQeQ&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

0:00

0:00 / 3:55
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=9B7RrmQCQeQ "Watch on YouTube")

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#implementation) Implementation

To implement this, you will use a simple yet powerful resource: [Qdrant with Sparse Vectors](https://qdrant.tech/articles/sparse-vectors/).

Notebook: [You can try this code here](https://githubtocolab.com/qdrant/examples/blob/master/collaborative-filtering/collaborative-filtering.ipynb)

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#setup) Setup

You have to first import the necessary libraries and define the environment.

```python
import os
import pandas as pd
import requests
from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct, SparseVector, NamedSparseVector
from collections import defaultdict