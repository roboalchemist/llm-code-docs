# [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#load-and-search-hugging-face-datasets-with-qdrant) Load and Search Hugging Face Datasets with Qdrant

[Hugging Face](https://huggingface.co/) provides a platform for sharing and using ML models and
datasets. [Qdrant](https://huggingface.co/Qdrant) also publishes datasets along with the
embeddings that you can use to practice with Qdrant and build your applications based on semantic
search. **Please [let us know](https://qdrant.to/discord) if you’d like to see a specific dataset!**

## [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#arxiv-titles-instructorxl-embeddings) arxiv-titles-instructorxl-embeddings

[This dataset](https://huggingface.co/datasets/Qdrant/arxiv-titles-instructorxl-embeddings) contains
embeddings generated from the paper titles only. Each vector has a payload with the title used to
create it, along with the DOI (Digital Object Identifier).

```json
{
    "title": "Nash Social Welfare for Indivisible Items under Separable, Piecewise-Linear Concave Utilities",
    "DOI": "1612.05191"
}

```

You can find a detailed description of the dataset in the [Practice Datasets](https://qdrant.tech/documentation/datasets/#journal-article-titles)
section. If you prefer loading the dataset from a Qdrant snapshot, it also linked there.

Loading the dataset is as simple as using the `load_dataset` function from the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("Qdrant/arxiv-titles-instructorxl-embeddings")

```

The dataset contains 2,250,000 vectors. This is how you can check the list of the features in the dataset:

```python
dataset.features

```

### [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#streaming-the-dataset) Streaming the dataset

Dataset streaming lets you work with a dataset without downloading it. The data is streamed as
you iterate over the dataset. You can read more about it in the [Hugging Face\\
documentation](https://huggingface.co/docs/datasets/stream).

```python
from datasets import load_dataset

dataset = load_dataset(
    "Qdrant/arxiv-titles-instructorxl-embeddings", split="train", streaming=True
)

```

### [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#loading-the-dataset-into-qdrant) Loading the dataset into Qdrant

You can load the dataset into Qdrant using the [Python SDK](https://github.com/qdrant/qdrant-client).
The embeddings are already precomputed, so you can store them in a collection, that we’re going
to create in a second:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")

client.create_collection(
    collection_name="arxiv-titles-instructorxl-embeddings",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE,
    ),
)

```

It is always a good idea to use batching, while loading a large dataset, so let’s do that.
We are going to need a helper function to split the dataset into batches:

```python
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    while batch := list(islice(iterator, n)):
        yield batch

```

If you are a happy user of Python 3.12+, you can use the [`batched` function from the `itertools`](https://docs.python.org/3/library/itertools.html#itertools.batched) package instead.

No matter what Python version you are using, you can use the `upsert` method to load the dataset,
batch by batch, into Qdrant:

```python
batch_size = 100

for batch in batched(dataset, batch_size):
    ids = [point.pop("id") for point in batch]
    vectors = [point.pop("vector") for point in batch]

    client.upsert(
        collection_name="arxiv-titles-instructorxl-embeddings",
        points=models.Batch(
            ids=ids,
            vectors=vectors,
            payloads=batch,
        ),
    )

```

Your collection is ready to be used for search! Please [let us know using Discord](https://qdrant.to/discord)
if you would like to see more datasets published on Hugging Face hub.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/huggingface-datasets.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/huggingface-datasets.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-23-lllmstxt|>
## reranking-hybrid-search
- [Documentation](https://qdrant.tech/documentation/)
- [Advanced tutorials](https://qdrant.tech/documentation/advanced-tutorials/)
- Reranking in Hybrid Search