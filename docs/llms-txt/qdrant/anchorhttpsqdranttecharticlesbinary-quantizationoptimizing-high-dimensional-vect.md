# [Anchor](https://qdrant.tech/articles/binary-quantization/\#optimizing-high-dimensional-vectors-with-binary-quantization) Optimizing High-Dimensional Vectors with Binary Quantization

Qdrant is built to handle typical scaling challenges: high throughput, low latency and efficient indexing. **Binary quantization (BQ)** is our latest attempt to give our customers the edge they need to scale efficiently. This feature is particularly excellent for collections with large vector lengths and a large number of points.

Our results are dramatic: Using BQ will reduce your memory consumption and improve retrieval speeds by up to 40x.

As is the case with other quantization methods, these benefits come at the cost of recall degradation. However, our implementation lets you balance the tradeoff between speed and recall accuracy at time of search, rather than time of index creation.

The rest of this article will cover:

1. The importance of binary quantization
2. Basic implementation using our Python client
3. Benchmark analysis and usage recommendations

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#what-is-binary-quantization) What is Binary Quantization?

Binary quantization (BQ) converts any vector embedding of floating point numbers into a vector of binary or boolean values. This feature is an extension of our past work on [scalar quantization](https://qdrant.tech/articles/scalar-quantization/) where we convert `float32` to `uint8` and then leverage a specific SIMD CPU instruction to perform fast vector comparison.

![What is binary quantization](https://qdrant.tech/articles_data/binary-quantization/bq-2.png)

**This binarization function is how we convert a range to binary values. All numbers greater than zero are marked as 1. If it’s zero or less, they become 0.**

The benefit of reducing the vector embeddings to binary values is that boolean operations are very fast and need significantly less CPU instructions. In exchange for reducing our 32 bit embeddings to 1 bit embeddings we can see up to a 40x retrieval speed up gain!

One of the reasons vector search still works with such a high compression rate is that these large vectors are over-parameterized for retrieval. This is because they are designed for ranking, clustering, and similar use cases, which typically need more information encoded in the vector.

For example, The 1536 dimension OpenAI embedding is worse than Open Source counterparts of 384 dimension at retrieval and ranking. Specifically, it scores 49.25 on the same [Embedding Retrieval Benchmark](https://huggingface.co/spaces/mteb/leaderboard) where the Open Source `bge-small` scores 51.82. This 2.57 points difference adds up quite soon.

Our implementation of quantization achieves a good balance between full, large vectors at ranking time and binary vectors at search and retrieval time. It also has the ability for you to adjust this balance depending on your use case.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#faster-search-and-retrieval) Faster search and retrieval

Unlike product quantization, binary quantization does not rely on reducing the search space for each probe. Instead, we build a binary index that helps us achieve large increases in search speed.

![Speed by quantization method](https://qdrant.tech/articles_data/binary-quantization/bq-3.png)

HNSW is the approximate nearest neighbor search. This means our accuracy improves up to a point of diminishing returns, as we check the index for more similar candidates. In the context of binary quantization, this is referred to as the **oversampling rate**.

For example, if `oversampling=2.0` and the `limit=100`, then 200 vectors will first be selected using a quantized index. For those 200 vectors, the full 32 bit vector will be used with their HNSW index to a much more accurate 100 item result set. As opposed to doing a full HNSW search, we oversample a preliminary search and then only do the full search on this much smaller set of vectors.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#improved-storage-efficiency) Improved storage efficiency

The following diagram shows the binarization function, whereby we reduce 32 bits storage to 1 bit information.

Text embeddings can be over 1024 elements of floating point 32 bit numbers. For example, remember that OpenAI embeddings are 1536 element vectors. This means each vector is 6kB for just storing the vector.

![Improved storage efficiency](https://qdrant.tech/articles_data/binary-quantization/bq-4.png)

In addition to storing the vector, we also need to maintain an index for faster search and retrieval. Qdrant’s formula to estimate overall memory consumption is:

`memory_size = 1.5 * number_of_vectors * vector_dimension * 4 bytes`

For 100K OpenAI Embedding ( `ada-002`) vectors we would need 900 Megabytes of RAM and disk space. This consumption can start to add up rapidly as you create multiple collections or add more items to the database.

**With binary quantization, those same 100K OpenAI vectors only require 128 MB of RAM.** We benchmarked this result using methods similar to those covered in our [Scalar Quantization memory estimation](https://qdrant.tech/articles/scalar-quantization/#benchmarks).

This reduction in RAM usage is achieved through the compression that happens in the binary conversion. HNSW and quantized vectors will live in RAM for quick access, while original vectors can be offloaded to disk only. For searching, quantized HNSW will provide oversampled candidates, then they will be re-evaluated using their disk-stored original vectors to refine the final results. All of this happens under the hood without any additional intervention on your part.

### [Anchor](https://qdrant.tech/articles/binary-quantization/\#when-should-you-not-use-bq) When should you not use BQ?

Since this method exploits the over-parameterization of embedding, you can expect poorer results for small embeddings i.e. less than 1024 dimensions. With the smaller number of elements, there is not enough information maintained in the binary vector to achieve good results.

You will still get faster boolean operations and reduced RAM usage, but the accuracy degradation might be too high.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#sample-implementation) Sample implementation

Now that we have introduced you to binary quantization, let’s try our a basic implementation. In this example, we will be using OpenAI and Cohere with Qdrant.

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#create-a-collection-with-binary-quantization-enabled) Create a collection with Binary Quantization enabled

Here is what you should do at indexing time when you create the collection:

1. We store all the “full” vectors on disk.
2. Then we set the binary embeddings to be in RAM.

By default, both the full vectors and BQ get stored in RAM. We move the full vectors to disk because this saves us memory and allows us to store more vectors in RAM. By doing this, we explicitly move the binary vectors to memory by setting `always_ram=True`.

```python
from qdrant_client import QdrantClient

#collect to our Qdrant Server
client = QdrantClient(
    url="http://localhost:6333",
    prefer_grpc=True,
)

#Create the collection to hold our embeddings