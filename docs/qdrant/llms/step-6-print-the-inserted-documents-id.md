# Step 6: Print the Inserted Document's ID
print("Inserted document ID:", result.inserted_id)

```

`project_root_folder/utils/app_utils.py`

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333", api_key="<YOUR_KEY>")
dimension_dict = {"snowflake/snowflake-arctic-embed-s": 384}

def create_qdrant_collection(collection_name: str, embed_model: str):

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=dimension_dict.get(embed_model), distance=models.Distance.COSINE)
        )

```

Before we run the application, below is the state of MongoDB and Qdrant databases.

![3.webp](https://qdrant.tech/documentation/examples/data-streaming-kafka-qdrant/3.webp)

Figure 3: Initial state: no collection named `test` & `no data` in the `docs` collection of MongodDB.

Once you run the code the data goes into Mongodb and the CDC gets triggered and eventually Qdrant will receive this data.

![4.webp](https://qdrant.tech/documentation/examples/data-streaming-kafka-qdrant/4.webp)

Figure 4: The test Qdrant collection is created automatically.

![5.webp](https://qdrant.tech/documentation/examples/data-streaming-kafka-qdrant/5.webp)

Figure 5: Data is inserted into both MongoDB and Qdrant.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#conclusion) Conclusion:

In conclusion, the integration of **Kafka** with **Qdrant** using the **Qdrant Sink Connector** provides a seamless and efficient solution for real-time data streaming and processing. This setup not only enhances the capabilities of your data pipeline but also ensures that high-dimensional vector data is continuously indexed and readily available for similarity searches. By following the installation and setup guide, you can easily establish a robust data flow from your **source systems** like **MongoDB** and **Azure Blob Storage**, through **Kafka**, and into **Qdrant**. This architecture empowers modern applications to leverage real-time data insights and advanced search capabilities, paving the way for innovative data-driven solutions.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/data-streaming-kafka-qdrant.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/data-streaming-kafka-qdrant.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-47-lllmstxt|>
## fastembed-splade
- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- Working with SPLADE