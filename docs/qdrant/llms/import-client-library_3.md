# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

qdrant_client = QdrantClient(host='localhost', port=6333)

```

Qdrant allows you to combine vectors of the same purpose into collections.
Many independent vector collections can exist on one service at the same time.

Let’s create a new collection for our startup vectors.

```python
if not qdrant_client.collection_exists('startups'):
    qdrant_client.create_collection(
        collection_name='startups',
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

```

The `vector_size` parameter is very important.
It tells the service the size of the vectors in that collection.
All vectors in a collection must have the same size, otherwise, it is impossible to calculate the distance between them.
`384` is the output dimensionality of the encoder we are using.

The `distance` parameter allows specifying the function used to measure the distance between two points.

The Qdrant client library defines a special function that allows you to load datasets into the service.
However, since there may be too much data to fit a single computer memory, the function takes an iterator over the data as input.

Let’s create an iterator over the startup data and vectors.

```python
import numpy as np
import json

fd = open('./startups.json')