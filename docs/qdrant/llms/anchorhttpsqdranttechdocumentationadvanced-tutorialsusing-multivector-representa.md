# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#how-to-effectively-use-multivector-representations-in-qdrant-for-reranking) How to Effectively Use Multivector Representations in Qdrant for Reranking

Multivector Representations are one of the most powerful features of Qdrant. However, most people don’t use them effectively, resulting in massive RAM overhead, slow inserts, and wasted compute.

In this tutorial, you’ll discover how to effectively use multivector representations in Qdrant.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#what-are-multivector-representations) What are Multivector Representations?

In most vector engines, each document is represented by a single vector - an approach that works well for short texts but often struggles with longer documents. Single vector representations perform pooling of the token-level embeddings, which obviously leads to losing some information.

Multivector representations offer a more fine-grained alternative where a single document is represented using multiple vectors, often at the token or phrase level. This enables more precise matching between specific query terms and relevant parts of the document. Matching is especially effective in Late Interaction models like [ColBERT](https://qdrant.tech/documentation/fastembed/fastembed-colbert/), which retain token-level embeddings and perform interaction during query time leading to relevance scoring.

![Multivector Representations](https://qdrant.tech/documentation/advanced-tutorials/multivectors.png)

As you will see later in the tutorial, Qdrant supports multivectors and thus late interaction models natively.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#why-token-level-vectors-are-useful) Why Token-level Vectors are Useful

With token-level vectors, models like ColBERT can match specific query tokens to the most relevant parts of a document, enabling high-accuracy retrieval through Late Interaction.

In late interaction, each document is converted into multiple token-level vectors instead of a single vector. The query is also tokenized and embedded into various vectors. Then, the query and document vectors are matched using a similarity function: MaxSim. You can see how it is calculated [here](https://qdrant.tech/documentation/concepts/vectors/#multivectors).

In traditional retrieval, the query and document are converted into single embeddings, after which similarity is computed. This is an early interaction because the information is compressed before retrieval.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#what-is-rescoring-and-why-is-it-used) What is Rescoring, and Why is it Used?

Rescoring is two-fold:

- Retrieve relevant documents using a fast model.
- Rerank them using a more accurate but slower model such as ColBERT.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#why-indexing-every-vector-by-default-is-a-problem) Why Indexing Every Vector by Default is a Problem

In multivector representations (such as those used by Late Interaction models like ColBERT), a single logical document results in hundreds of token-level vectors. Indexing each of these vectors individually with HNSW in Qdrant can lead to:

- High RAM usage
- Slow insert times due to the complexity of maintaining the HNSW graph

However, because multivectors are typically used in the reranking stage (after a first-pass retrieval using dense vectors), there’s often no need to index these token-level vectors with HNSW.

Instead, they can be stored as multi-vector fields (without HNSW indexing) and used at query-time for reranking, which reduces resource overhead and improves performance.

For more on this, check out Qdrant’s detailed breakdown in our [Scaling PDF Retrieval with Qdrant tutorial](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/#math-behind-the-scaling).

With Qdrant, you have full control of how indexing works. You can disable indexing by setting the HNSW `m` parameter to `0`:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")
collection_name = "dense_multivector_demo"
client.create_collection(
    collection_name=collection_name,
    vectors_config={
        "dense": models.VectorParams(
            size=384,
            distance=models.Distance.COSINE
            # Leave HNSW indexing ON for dense
        ),
        "colbert": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
            hnsw_config=models.HnswConfigDiff(m=0)  # Disable HNSW for reranking
        )
    }
)

```

By disabling HNSW on multivectors, you:

- Save compute.
- Reduce memory usage.
- Speed up vector uploads.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#how-to-generate-multivectors-using-fastembed) How to Generate Multivectors Using FastEmbed

Let’s demonstrate how to effectively use multivectors using [FastEmbed](https://github.com/qdrant/fastembed), which wraps ColBERT into a simple API.

Install FastEmbed and Qdrant:

```bash
pip install qdrant-client[fastembed]>=1.14.2

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#step-by-step-colbert--qdrant-setup) Step-by-Step: ColBERT + Qdrant Setup

Ensure that Qdrant is running and create a client:

```python
from qdrant_client import QdrantClient, models