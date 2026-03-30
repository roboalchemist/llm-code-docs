# Create the new dataframe with the vectorized data
embeddings_df = spark.createDataFrame(data=embeddings, schema=schema)

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#uploading-the-data-to-qdrant) Uploading the data to Qdrant

- **Create a Qdrant collection:**


  - [Follow the documentation](https://qdrant.tech/documentation/concepts/collections/#create-a-collection) to create a collection with the appropriate configurations. Here’s an example request to support both dense and sparse vectors:

```json
PUT /collections/{collection_name}
{
  "vectors": {
    "dense": {
      "size": 384,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "sparse": {}
  }
}

```

- **Upload the dataframe to Qdrant:**


```python
options = {
    "qdrant_url": "<QDRANT_GRPC_URL>",
    "api_key": "<QDRANT_API_KEY>",
    "collection_name": "<QDRANT_COLLECTION_NAME>",
    "vector_fields": "dense_vector",
    "vector_names": "dense",
    "sparse_vector_value_fields": "sparse_vector_values",
    "sparse_vector_index_fields": "sparse_vector_indices",
    "sparse_vector_names": "sparse",
    "schema": embeddings_df.schema.json(),
}

embeddings_df.write.format("io.qdrant.spark.Qdrant").options(**options).mode(
    "append"
).save()

```

Ensure to replace the placeholder values ( `<QDRANT_GRPC_URL>`, `<QDRANT_API_KEY>`, `<QDRANT_COLLECTION_NAME>`) with your actual values. If the `id_field` option is not specified, Qdrant Spark connector generates random UUIDs for each point.

The command output you should see is similar to:

```console
Command took 40.37 seconds -- by xxxxx90@xxxxxx.com at 4/17/2024, 12:13:28 PM on fastembed

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#conclusion) Conclusion

That wraps up our tutorial! Feel free to explore more functionalities and experiments with different models, parameters, and features available in Databricks, Spark, and Qdrant.

Happy data engineering!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/databricks.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/databricks.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-144-lllmstxt|>
## agentic-rag
- [Articles](https://qdrant.tech/articles/)
- What is Agentic RAG? Building Agents with Qdrant

[Back to RAG & GenAI](https://qdrant.tech/articles/rag-and-genai/)