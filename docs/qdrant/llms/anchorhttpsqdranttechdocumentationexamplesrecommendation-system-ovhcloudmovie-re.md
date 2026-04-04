# [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#movie-recommendation-system) Movie Recommendation System

| Time: 120 min | Level: Advanced | Output: [GitHub](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-OVH.ipynb) |  |
| --- | --- | --- | --- |

In this tutorial, you will build a mechanism that recommends movies based on defined preferences. Vector databases like Qdrant are good for storing high-dimensional data, such as user and item embeddings. They can enable personalized recommendations by quickly retrieving similar entries based on advanced indexing techniques. In this specific case, we will use [sparse vectors](https://qdrant.tech/articles/sparse-vectors/) to create an efficient and accurate recommendation system.

**Privacy and Sovereignty:** Since preference data is proprietary, it should be stored in a secure and controlled environment. Our vector database can easily be hosted on [OVHcloud](https://ovhcloud.com/), our trusted [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) partner. This means that Qdrant can be run from your OVHcloud region, but the database itself can still be managed from within Qdrant Cloud’s interface. Both products have been tested for compatibility and scalability, and we recommend their [managed Kubernetes](https://www.ovhcloud.com/en/public-cloud/kubernetes/) service.

> To see the entire output, use our [notebook with complete instructions](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-OVH.ipynb).

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#components) Components

- **Dataset:** The [MovieLens dataset](https://grouplens.org/datasets/movielens/) contains a list of movies and ratings given by users.
- **Cloud:** [OVHcloud](https://ovhcloud.com/), with managed Kubernetes.
- **Vector DB:** [Qdrant Hybrid Cloud](https://hybrid-cloud.qdrant.tech/) running on [OVHcloud](https://ovhcloud.com/).

**Methodology:** We’re adopting a collaborative filtering approach to construct a recommendation system from the dataset provided. Collaborative filtering works on the premise that if two users share similar tastes, they’re likely to enjoy similar movies. Leveraging this concept, we’ll identify users whose ratings align closely with ours, and explore the movies they liked but we haven’t seen yet. To do this, we’ll represent each user’s ratings as a vector in a high-dimensional, sparse space. Using Qdrant, we’ll index these vectors and search for users whose ratings vectors closely match ours. Ultimately, we will see which movies were enjoyed by users similar to us.

![](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/architecture-diagram.png)

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#deploying-qdrant-hybrid-cloud-on-ovhcloud) Deploying Qdrant Hybrid Cloud on OVHcloud

[Service Managed Kubernetes](https://www.ovhcloud.com/en-in/public-cloud/kubernetes/), powered by OVH Public Cloud Instances, a leading European cloud provider. With OVHcloud Load Balancers and disks built in. OVHcloud Managed Kubernetes provides high availability, compliance, and CNCF conformance, allowing you to focus on your containerized software layers with total reversibility.

1. To start using managed Kubernetes on OVHcloud, follow the [platform-specific documentation](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#ovhcloud).
2. Once your Kubernetes clusters are up, [you can begin deploying Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/).

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#prerequisites) Prerequisites

Download and unzip the MovieLens dataset:

```shell
mkdir -p data
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip -d data

```

The necessary \* libraries are installed using `pip`, including `pandas` for data manipulation, `qdrant-client` for interfacing with Qdrant, and `*-dotenv` for managing environment variables.

```python
!pip install -U  \
    pandas  \
    qdrant-client \
    *-dotenv

```

The `.env` file is used to store sensitive information like the Qdrant host URL and API key securely.

```shell
QDRANT_HOST
QDRANT_API_KEY

```

Load all environment variables into the setup:

```python
import os
from dotenv import load_dotenv
load_dotenv('./.env')

```

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#implementation) Implementation

Load the data from the MovieLens dataset into pandas DataFrames to facilitate data manipulation and analysis.

```python
from qdrant_client import QdrantClient, models
import pandas as pd

```

Load user data:

```python
users = pd.read_csv(
    'data/ml-1m/users.dat',
    sep='::',
    names=['user_id', 'gender', 'age', 'occupation', 'zip'],
    engine='*'
)
users.head()

```

Add movies:

```python
movies = pd.read_csv(
    'data/ml-1m/movies.dat',
    sep='::',
    names=['movie_id', 'title', 'genres'],
    engine='*',
    encoding='latin-1'
)
movies.head()

```

Finally, add the ratings:

```python
ratings = pd.read_csv(
    'data/ml-1m/ratings.dat',
    sep='::',
    names=['user_id', 'movie_id', 'rating', 'timestamp'],
    engine='*'
)
ratings.head()

```

### [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#normalize-the-ratings) Normalize the ratings

Sparse vectors can use advantage of negative values, so we can normalize ratings to have a mean of 0 and a standard deviation of 1. This normalization ensures that ratings are consistent and centered around zero, enabling accurate similarity calculations. In this scenario we can take into account movies that we don’t like.

```python
ratings.rating = (ratings.rating - ratings.rating.mean()) / ratings.rating.std()

```

To get the results:

```python
ratings.head()

```

### [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#data-preparation) Data preparation

Now you will transform user ratings into sparse vectors, where each vector represents ratings for different movies. This step prepares the data for indexing in Qdrant.

First, create a collection with configured sparse vectors. For sparse vectors, you don’t need to specify the dimension, because it’s extracted from the data automatically.

```python
from collections import defaultdict

user_sparse_vectors = defaultdict(lambda: {"values": [], "indices": []})

for row in ratings.itertuples():
    user_sparse_vectors[row.user_id]["values"].append(row.rating)
    user_sparse_vectors[row.user_id]["indices"].append(row.movie_id)

```

Connect to Qdrant and create a collection called **movielens**:

```python
client = QdrantClient(
    url = os.getenv("QDRANT_HOST"),
    api_key = os.getenv("QDRANT_API_KEY")
)

client.create_collection(
    "movielens",
    vectors_config={},
    sparse_vectors_config={
        "ratings": models.SparseVectorParams()
    }
)

```

Upload user ratings to the **movielens** collection in Qdrant as sparse vectors, along with user metadata. This step populates the database with the necessary data for recommendation generation.

```python
def data_generator():
    for user in users.itertuples():
        yield models.PointStruct(
            id=user.user_id,
            vector={
                "ratings": user_sparse_vectors[user.user_id]
            },
            payload=user._asdict()
        )

client.upload_points(
    "movielens",
    data_generator()
)

```

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#recommendations) Recommendations

Personal movie ratings are specified, where positive ratings indicate likes and negative ratings indicate dislikes. These ratings serve as the basis for finding similar users with comparable tastes.

Personal ratings are converted into a sparse vector representation suitable for querying Qdrant. This vector represents the user’s preferences across different movies.

Let’s try to recommend something for ourselves:

```
1 = Like
-1 = dislike

```

```python