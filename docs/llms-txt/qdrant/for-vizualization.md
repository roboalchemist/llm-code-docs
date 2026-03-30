# For vizualization
import seaborn as sns

```

Establish connection to Qdrant:

```python
client = QdrantClient("http://localhost:6333")

```

After this is done, we can compute the distance matrix:

```python