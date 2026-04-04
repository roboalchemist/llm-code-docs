# Source: https://docs.lancedb.com/integrations/ai/llamaIndex.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LlamaIndex

export const PyFrameworksLlamaindexQuickStart = "import logging\nimport sys\nimport textwrap\n\nimport openai\n\n# Uncomment to see debug logs\n# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)\n# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))\nfrom llama_index.core import (\n    Document,\n    SimpleDirectoryReader,\n    StorageContext,\n    VectorStoreIndex,\n)\nfrom llama_index.vector_stores.lancedb import LanceDBVectorStore\n\nopenai.api_key = \"sk-...\"\n\ndocuments = SimpleDirectoryReader(\"./data/your-data-dir/\").load_data()\nprint(\"Document ID:\", documents[0].doc_id, \"Document Hash:\", documents[0].hash)\n\n## For LanceDB cloud :\n# vector_store = LanceDBVectorStore(\n#     uri=\"db://db_name\", # your remote DB URI\n#     api_key=\"sk_..\", # lancedb cloud api key\n#     region=\"your-region\" # the region you configured\n#     ...\n# )\n\nvector_store = LanceDBVectorStore(\n    uri=\"./lancedb\", mode=\"overwrite\", query_type=\"vector\"\n)\nstorage_context = StorageContext.from_defaults(vector_store=vector_store)\n\nindex = VectorStoreIndex.from_documents(documents, storage_context=storage_context)\nlance_filter = \"metadata.file_name = 'paul_graham_essay.txt' \"\nretriever = index.as_retriever(vector_store_kwargs={\"where\": lance_filter})\nresponse = retriever.retrieve(\"What did the author do growing up?\")\n";

export const PyFrameworksLlamaindexHybridSearch = "from lancedb.rerankers import ColbertReranker\n\nreranker = ColbertReranker()\nvector_store._add_reranker(reranker)\n\nquery_engine = index.as_query_engine(\n    filters=query_filters,\n    vector_store_kwargs={\n        \"query_type\": \"hybrid\",\n    },\n)\n\nresponse = query_engine.query(\"How much did Viaweb charge per month?\")\n";

export const PyFrameworksLlamaindexFiltering = "from llama_index.core.vector_stores import (\n    FilterCondition,\n    FilterOperator,\n    MetadataFilter,\n    MetadataFilters,\n)\n\nquery_filters = MetadataFilters(\n    filters=[\n        MetadataFilter(\n            key=\"creation_date\", operator=FilterOperator.EQ, value=\"2024-05-23\"\n        ),\n        MetadataFilter(key=\"file_size\", value=75040, operator=FilterOperator.GT),\n    ],\n    condition=FilterCondition.AND,\n)\n";

export const PyFrameworksLlamaindexAddReranker = "from lancedb.rerankers import ColbertReranker\n\nreranker = ColbertReranker()\nvector_store._add_reranker(reranker)\n";

## Quickstart

LlamaIndex is a well-known framework for building LLM-powered agents over your data with LLMs and workflows.
You can build your LlamaIndex pipeline and persist your metadata and embeddings in LanceDB via the `LanceDBVectorStore` class.

First, install the LlamaIndex-LanceDB integration.

<CodeBlock filename="bash" language="bash" icon="terminal">
  pip install llama-index-vector-stores-LanceDB
</CodeBlock>

Run the below script as an example.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksLlamaindexQuickStart}
</CodeBlock>

The vector store connector will open an existing LanceDB directory or create the directory if it does not exist.

### Filtering

For metadata filtering, you can use a Lance SQL-like string filter as demonstrated in the example above. Additionally, you can also filter using the `MetadataFilters` class from LlamaIndex:

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksLlamaindexFiltering}
</CodeBlock>

### Hybrid Search

For complete documentation, refer [here](https://lancedb.github.io/lancedb/hybrid_search/hybrid_search/). This example uses the `colbert` reranker. Make sure to install necessary dependencies for the reranker you choose.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksLlamaindexHybridSearch}
</CodeBlock>

In the snippet above, you can change/specify `query_type` when creating the engine/retriever
to use different search strategies, such as vector search or FTS.

## API reference

<Card title="LlamaIndex Vector Stores API reference" href="https://developers.llamaindex.ai/python/framework-api-reference/storage/vector_store/lancedb/">
  See the official LlamaIndex Vector Stores API reference for more details.
</Card>
