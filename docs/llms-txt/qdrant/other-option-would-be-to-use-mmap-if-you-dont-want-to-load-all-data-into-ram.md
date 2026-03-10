# Other option would be to use Mmap, if you don't want to load all data into RAM
vectors = np.load("./startup_vectors.npy")

```

5. Upload the data

```python
client.upload_collection(
    collection_name="startups",
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256,  # How many vectors will be uploaded in a single request?
)

```

Vectors are now uploaded to Qdrant.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#build-the-search-api) Build the search API

Now that all the preparations are complete, let’s start building a neural search class.

In order to process incoming requests, neural search will need 2 things: 1) a model to convert the query into a vector and 2) the Qdrant client to perform search queries.

1. Create a file named `neural_searcher.py` and specify the following.

```python
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class NeuralSearcher:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        # initialize Qdrant client
        self.qdrant_client = QdrantClient("http://localhost:6333")

```

2. Write the search function.

```python
def search(self, text: str):
    # Convert text query into vector
    vector = self.model.encode(text).tolist()

    # Use `vector` for search for closest vectors in the collection
    search_result = self.qdrant_client.query_points(
        collection_name=self.collection_name,
        query=vector,
        query_filter=None,  # If you don't want any filters for now
        limit=5,  # 5 the most closest results is enough
    ).points
    # `search_result` contains found vector ids with similarity scores along with the stored payload
    # In this function you are interested in payload only
    payloads = [hit.payload for hit in search_result]
    return payloads

```

3. Add search filters.

With Qdrant it is also feasible to add some conditions to the search.
For example, if you wanted to search for startups in a certain city, the search query could look like this:

```python
from qdrant_client.models import Filter

    ...

    city_of_interest = "Berlin"

    # Define a filter for cities
    city_filter = Filter(**{
        "must": [{\
            "key": "city", # Store city information in a field of the same name\
            "match": { # This condition checks if payload field has the requested value\
                "value": city_of_interest\
            }\
        }]
    })

    search_result = self.qdrant_client.query_points(
        collection_name=self.collection_name,
        query=vector,
        query_filter=city_filter,
        limit=5
    ).points
    ...

```

You have now created a class for neural search queries. Now wrap it up into a service.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#deploy-the-search-with-fastapi) Deploy the search with FastAPI

To build the service you will use the FastAPI framework.

1. Install FastAPI.

To install it, use the command

```bash
pip install fastapi uvicorn

```

2. Implement the service.

Create a file named `service.py` and specify the following.

The service will have only one API endpoint and will look like this:

```python
from fastapi import FastAPI