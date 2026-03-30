# 1. Connect to Qdrant server
client = QdrantClient("http://localhost:6333")

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#1-encode-documents) 1\. Encode Documents

Next, encode your documents:

```python
from fastembed import TextEmbedding, LateInteractionTextEmbedding