# Define your API key and other payload data
api_key = "your_api_key"
payload = { ...
}

token = jwt.encode(payload, api_key, algorithm="HS256")
print(token)

```

Once you have generated the token, you should include it in the subsequent requests. You can do so by providing it as a bearer token in the Authorization header, or in the API Key header of your requests.

Below is an example of how to do so using QdrantClient in Python:

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "http://localhost:6333",
    api_key="<JWT>", # the token goes here
)