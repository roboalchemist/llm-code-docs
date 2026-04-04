# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/vector-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vector Index

> The Vector index enables efficient vector similarity searches, supporting high-dimensional data queries for applications like recommendation systems and anomaly detection.

## Overview and Purpose

A vector index is a specialized data structure that enables efficient similarity searches across high-dimensional vector embeddings. It transforms complex similarity computations from exhaustive comparisons to approximate nearest neighbor searches, dramatically improving query performance.

In StarTree Cloud (powered by Apache Pinot), vector indexing supports storing and querying embedding vectors generated from machine learning models for use cases like semantic search, recommendation systems, and AI-powered analytics.

Vector indexes are particularly valuable for:

* Semantic search applications using text embeddings
* Image similarity search using visual embeddings
* Recommendation engines based on user or item embeddings
* Anomaly detection using vector representations
* Any query pattern involving similarity comparisons between high-dimensional vectors

<Info>
  Without a vector index, finding similar vectors would require computing distances between the query vector and every vector in the database, which becomes prohibitively expensive as data volume grows.
</Info>

## How the Index Works

### Core Concepts

Traditional database indexes are designed for exact matches or range queries. However, vector similarity search requires finding the "most similar" items in high-dimensional space, which is fundamentally different.

The vector index in StarTree Cloud:

1. **HNSW Implementation**: Uses Hierarchical Navigable Small World (HNSW) algorithm for efficient approximate nearest neighbor (ANN) search.
2. **Graph-Based Navigation**: Creates a navigable graph structure where similar vectors are connected, enabling efficient traversal to find nearest neighbors.
3. **Multi-Layer Structure**: Organizes vectors in a hierarchical structure that allows for quick pruning of the search space.
4. **Approximate Results**: Trades off perfect accuracy for dramatic speed improvements, finding the most similar vectors with high probability.

### Example Illustration

For a set of product embeddings representing semantic meaning:

1. A traditional approach would compute the distance between a query vector and every product vector in the database.
2. With a vector index, the system:
   * Starts at an entry point in the graph
   * Navigates through connections to increasingly similar vectors
   * Quickly narrows down to a small subset of candidate vectors
   * Returns the most similar vectors without exhaustive comparison

This approach can reduce search time from linear (O(n)) to logarithmic (O(log n)) complexity, enabling real-time similarity search even with millions of vectors.

## Configuration

### Enabling Vector Index

To enable a vector index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```
{
  "fieldConfigList": [
    {
      "name": "embedding",
      "encodingType": "RAW",
      "indexes": {
        "vector": {
          "vectorIndexType": "HNSW",
          "vectorDimension": 1536,
          "vectorDistanceFunction": "COSINE",
          "version": 1
        }
      }
    }
  ]
}
```

### Alternative Configuration (Legacy Method)

You can also use the older configuration format:

```
{
  "fieldConfigList": [
    {
      "name": "embedding",
      "encodingType": "RAW",
      "indexType": "VECTOR",
      "properties": {
        "vectorIndexType": "HNSW",
        "vectorDimension": 1536,
        "vectorDistanceFunction": "COSINE",
        "version": 1
      }
    }
  ]
}
```

### Important Configuration Parameters

1. **vectorIndexType**: Specifies the algorithm used for vector indexing.
   * Currently, only "HNSW" (Hierarchical Navigable Small World) is supported.
2. **vectorDimension**: Defines the number of dimensions in the vector.
   * This must match the dimension of your embeddings (e.g., 1536 for OpenAI models, 768 for BERT base).
3. **vectorDistanceFunction**: Specifies the distance metric for similarity computation.
   * **COSINE**: Measures the angle between vectors (ideal for normalized vectors where orientation matters more than magnitude).
   * **INNER\_PRODUCT**: Computes the dot product (best when vectors are normalized and higher scores indicate greater similarity).
   * **L2**: Measures Euclidean distance (suitable for spatial closeness in high-dimensional space).
   * **L1**: Measures Manhattan distance (sum of absolute differences of coordinates).
4. **version**: Specifies the version of the vector index implementation.
5. **Data Type Requirements**, The column must be:
   * A multi-valued FLOAT array (set `singleValueField: false` in schema)
   * RAW encoded (set `encodingType: "RAW"` in the configuration)

Built with [Mintlify](https://mintlify.com).
