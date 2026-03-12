# Source: https://code.kx.com/kdbai/latest/reference/index.html

Title: About indexes in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/index.html

Markdown Content:
_This page explains the types of vector indexes you can use in KDB.AI, including Flat, qFlat, IVF, IVFPQ, HNSW, AND qHNSW._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/supported-indexes.html).

To process data efficiently, vector databases rely on a critical component known as the **vector index**. A vector index is created by applying an algorithm to the [vector embeddings](https://kdb.ai/learning-hub/articles/vector-embeddings/) stored within the database. The algorithm maps these vectors to a specialized data structure, enabling rapid searches. Compared to raw embeddings, the index’s compact representation significantly reduces memory requirements and enhances accessibility.

Before delving into the technical details of creating indexes with KDB.AI, let's explore the key topics to understand:

*   [1. Why are vector indexes important?](https://code.kx.com/kdbai/latest/reference/index.html#1-why-are-vector-indexes-important)
*   [2. In-memory vs. on-disk](https://code.kx.com/kdbai/latest/reference/index.html#2-in-memory-vs-on-disk)
*   [3. Fundamental types of vector indexes](https://code.kx.com/kdbai/latest/reference/index.html#3-fundamental-types-of-vector-indexes)

1. Why are vector indexes important?
------------------------------------

Vector indexing is essential for efficient search and retrieval of high-dimensional vector data (for example, image features, text embeddings, or sensor readings), especially in generative AI applications.

Using vector indexes has the following benefits:

*   **High-dimensional data:** Traditional databases struggle with efficiently searching and retrieving data in such high-dimensional spaces due to the curse of dimensionality. Vector indexing addresses this challenge.
*   **Fast similarity searches:** Given a query vector, a vector index can quickly find the most similar vectors in the dataset. This is crucial for applications like recommendation systems, content-based search, and clustering.
*   **Nearest-neighbor queries:** Indexes find the closest vectors in a dataset. Nearest neighbor search is essential for tasks like finding similar images, detecting anomalies, or identifying related documents.
*   **Semantic context:** Vector embeddings (vector representations) capture the semantic meaning of objects. Indexes allow you to find specific data easily within large sets of vector representations. They bring context to generative AI models.
*   **Retrieval Augmented Generation (RAG):** In generative AI applications, context is crucial. Vector indexes play a critical role in RAG by efficiently searching and retrieving relevant objects from a dataset of vector embeddings.

2. In-memory vs. on-disk
------------------------

With KDB.AI you can choose between in-memory and on-disk indexes, depending on your application’s needs and available resources.

In-memory indexes On-disk indexes Trade-offs

**Storage location**: In-memory vector indexes reside entirely in RAM (main memory). All data structures related to indexing are stored in memory.

**Performance**: In-memory indexes offer fast query performance because they eliminate the need for disk input/output. Retrieving data from RAM is considerably quicker than accessing it from a disk.

**Suitable use cases**:

*   Small to medium datasets: In-memory indexes work well for datasets with up to around 10 million vectors (for example, 1024-dimensional vectors).
*   Real-time applications: Applications requiring low-latency responses, such as recommendation systems, real-time search, and similarity search, benefit from in-memory indexes.

**Limitations**:

*   Memory constraints: The primary limitation is the available RAM. Larger datasets may be too expensive to store entirely in memory.
*   Cost: RAM is more expensive than disk storage, so scaling up memory can be costly.

**Storage location**: On-disk vector indexes are stored on persistent storage, such as hard drives or SSDs. Data structures and index files reside on disk.

**Performance**: On-disk indexes involve disk input/output, which makes them slower than in-memory indexes. However, they allow virtually unlimited storage capacity.

**Suitable use cases**:

*   Large datasets: On-disk indexes are suitable for datasets with millions to billions of vectors.
*   Batch processing: Applications that perform batch processing or periodic indexing benefit from on-disk storage.

**Advantages**:

*   Scalability: Disk storage allows efficient handling of large-scale data.
*   Cost-effective: Disk storage is more cost-effective than expanding RAM.
*   Persistence: Data remains intact even after the system restarts.
*   Long-term storage: Useful for archiving historical data.

**Speed vs. capacity**: In-memory indexes prioritize speed, while on-disk indexes prioritize capacity.

**Cost vs. performance**: In-memory storage is faster but more expensive. On-disk is slower but cost-effective.

**Use-case specific**: Choose based on your specific use case, dataset size, and performance requirements.

3. Types of vector indexes
--------------------------

There are three main categories of vector indexes:

*   **Flat index**: This straightforward approach involves comparing vectors directly, making it suitable for smaller datasets.
*   **Graph index** (for example, HNSW): Graph-based methods organize vectors into a hierarchical graph structure, optimizing nearest neighbor searches.
*   **Inverted index** (for example, IVF, IVFPQ): Inverted indexes group vectors based on their content, improving search efficiency.

### 3.1 Flat index

A flat index (sometimes called brute-force) is an exact approach to vector indexing:

*   It doesn’t use any optimization or approximation techniques.
*   It stores all data points without any transformation or compression.
*   Vectors are placed directly in the index and referenced for efficient lookup.

The advantage of a flat index is that it guarantees 100% recall and precision. However, it can be slower and less efficient than other types of vector indexes.

In flat indexing, the index directly represents the vector embeddings without using pre-trained clusters or other modifications. The search process is exhaustive: it compares the query vector against every single vector embedding in the database, calculating distances for each pair. The k-Nearest Neighbors (kNN) search returns k embeddings based on these distances.

Example
For example, consider a scenario where you have a set of high-dimensional vectors (such as feature vectors representing images or documents), and you need to search for similar vectors efficiently. The flat index allows you to achieve precise results by directly comparing the vectors without any approximations. Keep in mind that while flat indexing provides accuracy, it may not be the most efficient solution for very large datasets due to its computational cost. In such cases, other indexing methods (such as quantized flat or Approximate Nearest Neighbor (ANN) algorithms) might be more suitable.

Flat indexing is useful in the following instances:

*   **Low-dimensional data**: For low-dimensional vectors (typically up to a few dozen dimensions), flat indexes can be sufficiently fast while maintaining high accuracy.
*   **Small-scale databases**: When the database contains a relatively small number of vectors, a flat index can provide quick retrieval times.
*   **Simple querying**: If your primary use case involves straightforward queries, a flat index performs competitively without the complexity of other indexes.
*   **Real-time data ingestion**: When continuously adding vectors to the database, flat indexing quickly generates new indexes with minimal computation.
*   **Low query volume**: If query rates are low, a flat index can handle them effectively.

Storage: Flat is stored in-memory. To store it on-disk, opt for qFlat.

[Learn how to use the Flat index](https://code.kx.com/kdbai/latest/use/supported-indexes.html#flat) and the [qFlat index](https://code.kx.com/kdbai/latest/use/supported-indexes.html#qflat).

### 3.2 Graph index - HNSW

Graph-based indexes build a graph structure to organize vectors. These indexes sacrifice some accuracy for improved search speed. Hierarchical Navigable Small Worlds (HNSW), for instance, navigates through the graph to find approximate nearest neighbors.

HNSW incorporates two fundamental techniques:

*   **Probability skip list**: Combines the benefits of a sorted array and a linked list. It builds several layers of linked lists, with each layer having links that skip intermediate nodes. Search starts at the highest layer with the longest skips and moves along the edges towards the right. If we overshoot our target, we drop to the previous node in the next level. HNSW inherits this layered format, with longer edges in higher layers for fast search and shorter edges in lower layers for accurate search.
*   **Navigable Small World Graphs (NSW)**: NSW graphs are a proximity graph with both long-range and short-range links. By building them, search times are reduced to logarithmic complexity.

HNSW is suitable for large-scale databases with moderate accuracy requirements. Storage: HNSW index is stored in-memory. To store it on-disk, opt for qHNSW.

[Learn how to use the HNSW index](https://code.kx.com/kdbai/latest/use/supported-indexes.html#hnsw) and the [qHNSW index](https://code.kx.com/kdbai/latest/use/supported-indexes.html#qHnsw).

### 3.3 Inverted index

An inverted index and a forward index are two fundamental data structures used in information retrieval systems, such as search engines. They store and retrieve documents or information efficiently.

While a forward index is a direct mapping from documents to the terms they contain, an inverted index is the opposite, mapping terms to the documents they appear in. When used for search queries, it allows to find all documents containing a given term quickly.

Inverted indexes, such as Inverted File (IVF) and Product Quantization (IVFPQ), divide the vector space into **cells** or **clusters**. These indexes trade off accuracy for even faster search times. IVFPQ, for example, quantizes vectors into subvectors and organizes them into inverted lists. Ideal for very large databases with lower accuracy needs.

As searches are performed against the most relevant clusters, they're faster but potentially less accurate compared to flat searches.

#### 3.3.1 IVF

An IVF index is an efficient data structure used for Approximate Nearest Neighbor (ANN) search. It helps narrow down the scope of vectors during search, significantly improving search speed. IVF maps contents (vectors) to their locations, making it easier to retrieve relevant information from large datasets.

[Learn how to use the IVF index.](https://code.kx.com/kdbai/latest/use/supported-indexes.html#ivf)

#### 3.3.2 IVFPQ

Inverted File Product Quantization (IVFPQ) combines the benefits of IVF and PQ. PQ is a technique for dimensionality reduction without losing essential information. Initially, IVF narrows down the search scope by using an inverted file index. Next, PQ further compresses the vectors, allowing efficient search with a reduced number of vectors.

Here’s how it works:

*   Divide a large, high-dimensional vector into equally sized chunks (subvectors).
*   For each subvector:

    *   Identify the nearest centroid (reproduction value) from a predefined set of centroids.
    *   Replace the subvector with a unique ID representing the chosen centroid.
    *   The result is a compressed representation of the original vector.

[Learn how to use the IVFPQ index.](https://code.kx.com/kdbai/latest/use/supported-indexes.html#ivfpq)

Summary
-------

This page has highlighted key aspects and mechanisms behind index creation, along with specific trade-offs, helping you make an informed decision on how and when to use each type.

Next steps
----------

*   To get more familiar with indexes, refer to our [Indexing basics](https://kdb.ai/learning-hub/articles/indexing-basics/) article published on the KDB.AI Learning Hub.
*   To index your vector embeddings, check out the [How to use an Index in KDB.AI](https://code.kx.com/kdbai/latest/use/supported-indexes.html) page.
