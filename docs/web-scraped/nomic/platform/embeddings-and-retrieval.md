# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/

Nomic Atlas provides embedding and retrieval capabilities that power semantic search, RAG applications, clustering analysis, and multimodal data processing to help you work with unstructured data.

### Generate Embeddings

Generate embeddings locally or over the Nomic API

### Building RAG Applications with Atlas

Use Nomic embeddings over Atlas API for your RAG retrieval

### Text Embedding

Read more about text embedding models available in Atlas

### Image Embedding

Read more about image embedding models available in Atlas

## What are Embeddings?​

Embeddings are dense vector representations of data (like text or images) that capture semantic meaning in a way that computers can process.

Atlas supports both text embeddings and image embeddings through state-of-the-art models like nomic-embed-text-v1.5 and nomic-embed-vision-v1.5.

```
nomic-embed-text-v1.5
```

```
nomic-embed-vision-v1.5
```

## Getting Started​

The simplest way to start using embeddings in Atlas is through our Python client:

```
from nomic import embed# Generate text embeddingstext_output = embed.text(    texts=['Your text here'],    model='nomic-embed-text-v1.5',    task_type='search_document')# Generate image embeddingsimage_output = embed.image(    images=['path/to/image.jpg'],    model='nomic-embed-vision-v1.5')
```

## Supported Tasks​

- Vector Search: Build efficient semantic search systems
- RAG Applications: Power retrieval for AI applications
- Clustering: Organize and understand data relationships
- Classification: Train models for categorization tasks
## Embeddings in Atlas​

When an unstructured dataset is uploaded to Atlas, an embedding is associated with each datapoint using a Nomic Embedding Model.

In Atlas, embeddings serve two key purposes:

- Data Maps: Embeddings determine the layout of Atlas maps, as detailed in our technical report. This projection preserves semantic relationships, ensuring similar items appear closer together in the map interface.
Data Maps: Embeddings determine the layout of Atlas maps, as detailed in our technical report. This projection preserves semantic relationships, ensuring similar items appear closer together in the map interface.

- Vector Search: The vector search bar in Atlas uses embeddings to find semantically related content, going beyond simple keyword matching to find data on the map that corresponds with the meaning of your queries.
Vector Search: The vector search bar in Atlas uses embeddings to find semantically related content, going beyond simple keyword matching to find data on the map that corresponds with the meaning of your queries.

In addition to underlying the capabilities of Atlas, embeddings are available for inference using the Nomic API.

### Dimensionality Reduction​

All embeddings stored in Atlas are projected into a 2D coordinate representation, which forms the layout you see in Atlas Data Maps. These projections are generated using dimensionality reduction models.

You can read more about how this looks for different models in a our blog post on dimensionality reduction.

## Next Steps​

- Learn more about Text Embeddings
Learn more about Text Embeddings

- Explore Image Embeddings
Explore Image Embeddings

- See how to implement RAG with Atlas
See how to implement RAG with Atlas

- Review our API Reference for detailed documentation
Review our API Reference for detailed documentation

- What are Embeddings?
- Getting Started
- Supported Tasks
- Embeddings in AtlasDimensionality Reduction
- Dimensionality Reduction
- Next Steps
