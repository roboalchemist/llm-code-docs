# Define collection name
collection_name = "qdrant-agent"

storage_instance = QdrantStorage(
    vector_dim=embedding_instance.get_output_dim(),
    url_and_api_key=(
        qdrant_cloud_url,
        qdrant_api_key,
    ),
    collection_name=collection_name,
)

```

Make sure to update the `<your-qdrant-cloud-url>` and `<your-api-key>` fields.

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-4-scrape-and-process-data)**Step 4: Scrape and Process Data**

We’ll use CamelAI `VectorRetriever` library to help us to It processes content from a file or URL, divides it into chunks, and stores the embeddings in the specified Qdrant collection.

```python
from camel.retrievers import VectorRetriever

vector_retriever = VectorRetriever(embedding_model=embedding_instance,
                                   storage=storage_instance)

qdrant_urls = [\
    "https://qdrant.tech/documentation/overview",\
    "https://qdrant.tech/documentation/guides/installation",\
    "https://qdrant.tech/documentation/concepts/filtering",\
    "https://qdrant.tech/documentation/concepts/indexing",\
    "https://qdrant.tech/documentation/guides/distributed_deployment",\
    "https://qdrant.tech/documentation/guides/quantization"\
    # Add more URLs as needed\
]

for qdrant_url in qdrant_urls:
  vector_retriever.process(
      content=qdrant_url,
  )

```

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-5-setup-the-camel-ai-chatagent-instance)**Step 5: Setup the CAMEL-AI ChatAgent Instance**

Define the OpenAI model and create a CAMEL-AI ChatAgent instance.

```python
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent