# Source: https://code.kx.com/kdbai/latest/integrations/unstructured-io.html

Title: KDB.AI Unstructured - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/integrations/unstructured-io.html

Markdown Content:
_This page explains how to integrate KDB.AI with Unstructured._

Disclaimer: This integration is currently live only for the [Python API](https://code.kx.com/kdbai/latest/reference/python-client.html). [REST API](https://code.kx.com/kdbai/latest/reference/rest-api.html) is next.

[Unstructured](http://unstructured.io/) is a platform that focuses on optimizing data workflows for Large Language Models (LLMs). It provides modular functions and pre-built connectors that work seamlessly together. The goal is to efficiently transform unstructured data into structured formats, making it suitable for LLMs and other AI applications. Unstructured makes it easy to extract and transform complex data from various formats like plain text (TXT, XML), documents (CSV, HTML, PDF, and PPTX) and images (PNG, JPG).

This integration guide helps you integrate KDB.AI with Unstructured to achieve the following:

*   Process and analyze unstructured data effectively, achieving effortless document extraction.
*   Enable quick similarity searches for Generative AI and LLMs, improving recommendation systems and chatbots by seamlessly handling both structured and unstructured data.

Key features of the Unstructured Ingest Library
*   **Customization**: Allows to set up data sources, configure ingestion, and set destination targets.
*   **Data Ingestion**: Facilitates ingestion from APIs, databases, files, and streaming services.
*   **Fault Tolerance**: Provides ways to manage errors and retries in the data ingestion process.
*   **Logging**: Offers extensive logging and monitoring features to oversee the data ingestion.
*   **Partitioning**: Efficiently splits data files to retrieve relevant text outputs.
*   **Scalability**: Can be extended horizontally to support large enterprise-level data volumes.

Getting started
---------------

Before you begin, make sure you have the following:

*   Installed [Python 3](https://www.python.org/downloads) (versions 3.9 to 3.13), [Pip](https://pip.pypa.io/en/stable/installation/), and [Git](https://git-scm.com/downloads)
*   Active KDB.AI [Server](https://kx.com/kdb-ai-server-download) license
*   Basic knowledge of working with [vector databases](https://kdb.ai/learning-hub/articles/vector-database-101/) and [embedding models](https://kdb.ai/learning-hub/articles/vector-embeddings/)
*   Necessary configurations for interacting with KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   The name of the target table. [Create the table.](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html#create-a-new-table)

Environment variables you will need

KDB.AI Unstructured

*   `KDBAI_ENDPOINT` - The endpoint URL for your KDB.AI instance, represented by `--endpoint` (CLI) or `endpoint` (Python).
*   `KDBAI_API_KEY` - The KDB.AI API key, represented by `--api-key` (CLI) or `api_key` (Python).
*   `KDBAI_TABLE` - The name of the target table, represented by `--table-name` (CLI) or `table_name` (Python).

Use the Unstructured API to ingest data
---------------------------------------

Now you can batch process files using the `unstructured-ingest` library. This tool stores structured outputs locally and uploads them to a table in your KDB.AI database.

First, install the KDB.AI and Unstructured dependencies which include the ingest code and the command-line interface (CLI):

```
pip install "unstructured-ingest[kdbai]"
```

 To view a full list of options accepted by CLI, run: 

```
unstructured-ingest <upstream connector> kdbai --help
```

For further details, go through this quick Unstructured [installation guide](https://docs.unstructured.io/welcome). Check out two practical examples below, based on a [1-page book sample](https://github.com/Unstructured-IO/unstructured/blob/main/example-docs/pdf/DA-1p.pdf).

Example: Use KDB.AI and Unstructured to ingest data

Python Shell

```
# Before calling the API, ensure that the sdk is installed.
# See https://docs.unstructured.io/api-reference/api-services/sdk for more details
# This sample requires the following packages
# pip install unstructured
# pip install unstructured-ingest
# pip install "unstructured-ingest[kdbai]"
# pip install "unstructured[pdf]"
# pip install unstructured-client
# pip install "unstructured[embed-huggingface]"
import os
import kdbai_client as kdbai
from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.processes.connectors.kdbai import (
    KdbaiConnectionConfig,
    KdbaiAccessConfig,
    KdbaiUploadStagerConfig,
    KdbaiUploaderConfig
)
from unstructured_ingest.v2.processes.connectors.local import (
    LocalIndexerConfig,
    LocalDownloaderConfig,
    LocalConnectionConfig
)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
from unstructured_ingest.v2.processes.chunker import ChunkerConfig
from unstructured_ingest.v2.processes.embedder import EmbedderConfig
from unstructured import embed
# KDB.AI server information
# Set up a local server by following these steps: https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html
# We are using a local server in this example
KDBAI_ENDPOINT='http://localhost:8082'
KDBAI_API_KEY=''
# Create new KDB.AI session
session=kdbai.Session(endpoint=KDBAI_ENDPOINT, api_key=KDBAI_API_KEY)
# Create a table to store our embeddings called pdf_data
KDBAI_TABLE='pdf_data_python'
db = session.database("default")
# If we're re-running this, we need to first remove the old pdf_data table
for t in db.tables:
    if t.name == KDBAI_TABLE:
        t.drop() 
# Schema for our new table
schema = [
        {"name": "id", "type": "str"},
        {"name": "element_id", "type": "str"},
        {"name": "document", "type": "str"},
        {"name": "metadata", "type": "general"},
        {'name': 'embeddings', 'type': 'float32s'},
        ]
INDEX_HNSW = {"name": "hnsw",
            "column": "embeddings",
            "type": "hnsw",
            "params": {
                "dims": 384,
                "metric": "L2",
                "efConstruction": 8,
                "M": 8,
            },
            }
# Create the pdf_data table
table=db.create_table(KDBAI_TABLE, schema, indexes=[INDEX_HNSW])
# Check if table was created
print(db.tables)
# If you want to send files to Unstructured API services for processing, specify partition_by_api=True
# You will need an Unstructured service API and key. 
# Follow these steps to create them: https://docs.unstructured.io/api-reference/api-services/saas-api-development-guide#get-started
UNSTRUCTURED_API_URL="YOUR_UNSTRUCTURED_API_URL"
UNSTRUCTURED_API_KEY="YOUR_UNSTRUCTURED_API_KEY"
# We are processing a pdf file so need to provide its path
# This file is located in the Unstructured repo - example-docs/pdf/DA-1p.pdf
PATH_TO_SAMPLE_PDF_FILE=os.path.expanduser("~/pdfs/DA-1p.pdf")
Pipeline.from_configs(
    context=ProcessorConfig(),
    indexer_config=LocalIndexerConfig(input_path=PATH_TO_SAMPLE_PDF_FILE),
    downloader_config=LocalDownloaderConfig(),
    source_connection_config=LocalConnectionConfig(),
    partitioner_config=PartitionerConfig(
        partition_by_api=False, # local file processing
        #partition_by_api=True, # Unstructured service file processing
        api_key=UNSTRUCTURED_API_KEY,
        partition_endpoint=UNSTRUCTURED_API_URL,
        strategy="hi_res",
        additional_partition_args={
            "split_pdf_page": True,
            "split_pdf_allow_failed": True,
            "split_pdf_concurrency_level": 15
        }
    ),
    chunker_config=ChunkerConfig(chunking_strategy="by_title"),
    embedder_config=EmbedderConfig(embedding_provider="langchain-huggingface"),
    destination_connection_config=KdbaiConnectionConfig(
        access_config=KdbaiAccessConfig(
            api_key=KDBAI_API_KEY
        ),
        endpoint=KDBAI_ENDPOINT
    ),
    stager_config=KdbaiUploadStagerConfig(),
    uploader_config=KdbaiUploaderConfig(table_name=KDBAI_TABLE)
).run()
# Do a simple query so we can see the data in our table
pdf_data=db.table(KDBAI_TABLE).query()
print(pdf_data)
# Finally drop the pdf_data table
db.table(KDBAI_TABLE).drop()
```

```
#!/usr/bin/env bash
# KDB.AI server information
# Set up a local server by following these steps: https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html
# We are using a local server in this example
KDBAI_ENDPOINT='http://localhost:8082'
KDBAI_API_KEY=''
# Check if service is ready
curl -H "X-Api-Key: $KDBAI_API_KEY" $KDBAI_ENDPOINT/api/v2/ready
# Create a table to store our embeddings called pdf_data
KDBAI_TABLE='pdf_data'
curl -X "DELETE" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_API_KEY" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables/$KDBAI_TABLE
# Create a table.json containing the following schema
: <<'SCHEMA_EXAMPLE'
{
    "table": "pdf_data",
    "schema": [
        {"name": "id", "type": "symbol"},
        {"name": "element_id", "type": "symbol"},
        {"name": "document", "type": "symbol"},
        {"name": "metadata", "type": " "},
        {"name": "embeddings", "type": "floats"}
    ],
    "indexes": [ 
        {"name": "vectorIndex", "type": "hnsw", 
        "params": {"dims": 384, "metric": "L2", "efConstruction": 8,"M": 8},
        "column": "embeddings"}
    ]
}
SCHEMA_EXAMPLE
# Create the table using file table.json
curl -X "POST" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_API_KEY" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables -d @table.json
# Check if table was created
curl -X "GET" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_API_KEY" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables
# If you want to send files to Unstructured API services for processing, specify partition_by_api=True
# You will need an Unstructured service API and key. 
# Follow these steps to create them: https://docs.unstructured.io/api-reference/api-services/saas-api-development-guide#get-started
UNSTRUCTURED_API_URL="YOUR_UNSTRUCTURED_API_URL"
UNSTRUCTURED_API_KEY="YOUR_UNSTRUCTURED_API_KEY"
# We are processing a pdf file so need to provide its path
# This file is located in the Unstructured repo - example-docs/pdf/DA-1p.pdf
PATH_TO_SAMPLE_PDF_FILE='./DA-1p.pdf'
# For Unstructured service file processing, add this line
#    --partition-by-api \
# Local file processing
unstructured-ingest \
local \
    --input-path "$PATH_TO_SAMPLE_PDF_FILE" \
    --partition-by-api \
    --embedding-provider langchain-huggingface \
    --chunking-strategy by_title \
    --api-key $UNSTRUCTURED_API_KEY \
    --partition-endpoint $UNSTRUCTURED_API_URL \
    --strategy hi_res \
    --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
kdbai --table-name=$KDBAI_TABLE --endpoint $KDBAI_ENDPOINT --api-key ""
# Do a simple query so we can see the data in our table
PDF_DATA=$(curl -H 'Content-Type: application/json' $KDBAI_ENDPOINT/api/v2/databases/default/tables/${KDBAI_TABLE}/query -d '{"filter" : []}')
echo $PDF_DATA
# Finally drop the pdf_data table
curl -X "DELETE" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables/$KDBAI_TABLE
```

If you need help with the integration, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai)

Summary
-------

Integrating KDB.AI with Unstructured.io enhances data processing, improves AI applications, and facilitates efficient handling of both structured and unstructured data.

Now that you have successfully configured the integration you can execute the following:

*   **Retrieval Augmented Generation (RAG)**: Create retrieval-based models that combine pre-trained LLMs with a retrieval mechanism for more relevant, context-aware text generation.
*   **Traditional ETL (Extract, Transform, Load)**: Simplify the extraction, transformation, and loading of unstructured data into structured formats.

Next steps
----------

Whether you’re analyzing customer feedback in real-time or extracting insights from large document repositories, we recommend the following:

*   Run the [RAG with Unstructured, LangChain, & KDB.AI](https://github.com/KxSystems/kdbai-samples/blob/main/unstructured_io_RAG/Table_RAG_Unstructured_KDBAI_LangChain_RAG.ipynb) notebook in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/unstructured_io_RAG/Table_RAG_Unstructured_KDBAI_LangChain_RAG.ipynb).
*   Check out our [KDB.AI for Q&A with ChatGPT Retrieval Plugin](https://github.com/KxSystems/chatgpt-retrieval-plugin/blob/KDB.AI/examples/providers/kdbai/ChatGPT_QA_Demo.ipynb) notebook.
*   Watch a [YouTube video demonstrating the integration of a custom GPT with KDB.AI](https://www.youtube.com/watch?v=8IsVeTYh-MY).
*   Go through the advanced RAG samples in the [KX GitHub repository](https://github.com/KxSystems/kdbai-samples/tree/main/LlamaIndex_advanced_RAG). 
*   Try the advanced RAG with temporal filters [Sample notebook](https://github.com/KxSystems/kdbai-samples/blob/main/LlamaIndex_advanced_RAG/KDBAI_Advanced_RAG_Demo.ipynb) that you can run [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/LlamaIndex_advanced_RAG/KDBAI_Advanced_RAG_Demo.ipynb).
