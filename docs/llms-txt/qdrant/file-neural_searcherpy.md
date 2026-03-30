# File: neural_searcher.py

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

```

The search function looks as simple as possible:

```python
    def search(self, text: str):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            top=5  # 5 the most closest results is enough
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads

```

With Qdrant it is also feasible to add some conditions to the search.
For example, if we wanted to search for startups in a certain city, the search query could look like this:

```python
from qdrant_client.models import Filter

    ...

    city_of_interest = "Berlin"

    # Define a filter for cities
    city_filter = Filter(**{
        "must": [{\
            "key": "city", # We store city information in a field of the same name\
            "match": { # This condition checks if payload field have requested value\
                "keyword": city_of_interest\
            }\
        }]
    })

    search_result = self.qdrant_client.search(
        collection_name=self.collection_name,
        query_vector=vector,
        query_filter=city_filter,
        top=5
    )
    ...

```

We now have a class for making neural search queries. Let’s wrap it up into a service.

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-5-deploy-as-a-service) Step 5: Deploy as a service

To build the service we will use the FastAPI framework.
It is super easy to use and requires minimal code writing.

To install it, use the command

```bash
pip install fastapi uvicorn

```

Our service will have only one API endpoint and will look like this:

```python