# Set Qdrant Client
qdrant_client = QdrantClient(
    os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#define-output) Define output

Here, you will configure the recommendation engine to retrieve movie posters as output.

```python