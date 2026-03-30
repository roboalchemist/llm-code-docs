# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient("http://localhost:6333")

```

3. Related vectors need to be added to a collection. Create a new collection for your startup vectors.

```python
if not client.collection_exists("startups"):
    client.create_collection(
        collection_name="startups",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

```

4. Create an iterator over the startup data and vectors.

The Qdrant client library defines a special function that allows you to load datasets into the service.
However, since there may be too much data to fit a single computer memory, the function takes an iterator over the data as input.

```python
fd = open("./startups_demo.json")