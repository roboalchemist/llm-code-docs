# Initialize the client
client = QdrantClient(":memory:")  # or QdrantClient(path="path/to/db")

```

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-3-preparing-documents-metadata-and-ids) Step 3: Preparing Documents, Metadata, and IDs

Once the client is initialized, prepare the text documents you wish to embed, along with any associated metadata and unique IDs:

```python
docs = [\
    "Qdrant has Langchain integrations",\
    "Qdrant also has Llama Index integrations"\
]
metadata = [\
    {"source": "Langchain-docs"},\
    {"source": "LlamaIndex-docs"},\
]
ids = [42, 2]

```

Note that the add method we’ll use is overloaded: If you skip the ids, we’ll generate those for you. metadata is obviously optional. So, you can simply use this too:

```python
docs = [\
    "Qdrant has Langchain integrations",\
    "Qdrant also has Llama Index integrations"\
]

```

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-4-adding-documents-to-a-collection) Step 4: Adding Documents to a Collection

With your documents, metadata, and IDs ready, you can proceed to add these to a specified collection within Qdrant using the add method:

```python
client.add(
    collection_name="demo_collection",
    documents=docs,
    metadata=metadata,
    ids=ids
)

```

Inside this function, Qdrant Client uses FastEmbed to make the text embedding, generate ids if they’re missing, and then add them to the index with metadata. This uses the DefaultEmbedding model: [BAAI/bge-small-en-v1.5](https://huggingface.co/baai/bge-small-en-v1.5)

![INDEX TIME: Sequence Diagram for Qdrant and FastEmbed](https://qdrant.tech/articles_data/fastembed/generate-embeddings-from-docs.png)

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-5-performing-queries) Step 5: Performing Queries

Finally, you can perform queries on your stored documents. Qdrant offers a robust querying capability, and the query results can be easily retrieved as follows:

```python
search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(search_result)

```

Behind the scenes, we first convert the query\_text to the embedding and use that to query the vector index.

![QUERY TIME: Sequence Diagram for Qdrant and FastEmbed integration](https://qdrant.tech/articles_data/fastembed/generate-embeddings-query.png)

By following these steps, you effectively utilize the combined capabilities of FastEmbed and Qdrant, thereby streamlining your embedding generation and retrieval tasks.

Qdrant is designed to handle large-scale datasets with billions of data points. Its architecture employs techniques like [binary quantization](https://qdrant.tech/articles/binary-quantization/) and [scalar quantization](https://qdrant.tech/articles/scalar-quantization/) for efficient storage and retrieval. When you inject FastEmbed’s CPU-first design and lightweight nature into this equation, you end up with a system that can scale seamlessly while maintaining low latency.

## [Anchor](https://qdrant.tech/articles/fastembed/\#summary) Summary

If you’re curious about how FastEmbed and Qdrant can make your search tasks a breeze, why not take it for a spin? You get a real feel for what it can do. Here are two easy ways to get started:

1. **Cloud**: Get started with a free plan on the [Qdrant Cloud](https://qdrant.to/cloud?utm_source=qdrant&utm_medium=website&utm_campaign=fastembed&utm_content=article).

2. **Docker Container**: If you’re the DIY type, you can set everything up on your own machine. Here’s a quick guide to help you out: [Quick Start with Docker](https://qdrant.tech/documentation/quick-start/?utm_source=qdrant&utm_medium=website&utm_campaign=fastembed&utm_content=article).


So, go ahead, take it for a test drive. We’re excited to hear what you think!

Lastly, If you find FastEmbed useful and want to keep up with what we’re doing, giving our GitHub repo a star would mean a lot to us. Here’s the link to [star the repository](https://github.com/qdrant/fastembed).

If you ever have questions about FastEmbed, please ask them on the Qdrant Discord: [https://discord.gg/Qy6HCJK9Dc](https://discord.gg/Qy6HCJK9Dc)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/fastembed.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/fastembed.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-112-lllmstxt|>
## usage-statistics
- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Usage Statistics