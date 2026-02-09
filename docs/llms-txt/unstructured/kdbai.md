# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/kdbai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# KDB.AI

Batch process all your records to store structured outputs in KDB.AI.

The requirements are as follows.

* A KDB.AI Cloud or server instance. [Sign Up for KDB.AI Cloud: Starter Edition](https://trykdb.kx.com/kdbai/signup/). [Set up KDB.AI Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html).
* The instance's endpoint URL. [Get the KDB.AI Cloud endpoint URL](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-cloud-setup.html#connect-to-your-database). [Get the KDB.AI Server endpoint URL](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html).
* An API key. [Create the API key](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-cloud-setup.html#create-an-api-key).
* The name of the target table to access. [Create the table](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html#create-a-new-table).

  KDB.AI requires the target table to have a defined schema before Unstructured can write to the table. The recommended table
  schema for Unstructured contains the fields `id`, `element_id`, `document`, `metadata`, and `embeddings`, as follows.
  This example code demonstrates the use of the [KDB.AI Client for Python](https://pypi.org/project/kdbai-client/) to create
  a table with this recommended schema, along with creating a vector index that contains 3072 dimensions:

  ```python Python theme={null}
  import kdbai_client as kdbai
  import os

  session = kdbai.Session(
      endpoint=os.getenv("KDBAI_ENDPOINT"),
      api_key=os.getenv("KDBAI_API_KEY")
  )

  db = session.database("default")

  schema = [
      {
          "name": "id",
          "type": "str"
      },
      {
          "name": "element_id",
          "type": "str"
      },
      {
          "name": "document",
          "type": "str"
      },
      {
          "name": "metadata", 
          "type": "general"
      },
      {
          "name": "embeddings",
          "type": "float32s"
      }
  ]

  indexes = [ 
      {
          "name": "vectorIndex",
          "type": "flat", 
          "params": {
              "dims": 3072,
              "metric": "CS"
          },
          "column": "embeddings"
      }
  ]

  table = db.create_table(
      table=os.getenv("KDBAI_TABLE"),
      schema=schema,
      indexes=indexes
  )

  print(f"The table named '{table.name}' now exists.")
  ```

The KDB.AI connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[kdbai]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `KDBAI_ENDPOINT` - The KDB.AI instance's endpoint URL, represented by `--endpoint` (CLI) or `endpoint` (Python).
* `KDBAI_API_KEY` - The KDB.AI API key, represented by `--api-key` (CLI) or `api_key` (Python).
* `KDBAI_TABLE` - The name of the target table, represented by `--table-name` (CLI) or `table_name` (Python).

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector:

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --strategy hi_res \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    kdbai \
      --endpoint $KDBAI_API_KEY \
      --api-key $KDBAI_API_KEY \
      --table-name $KDBAI_TABLE
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.kdbai import (
      KdbaiConnectionConfig,
      KdbaiAccessConfig,
      KdbaiUploadStagerConfig,
      KdbaiUploaderConfig
  )

  from unstructured_ingest.processes.connectors.local import (
      LocalIndexerConfig,
      LocalDownloaderConfig,
      LocalConnectionConfig
  )
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=LocalIndexerConfig(input_path=os.getenv("LOCAL_FILE_INPUT_DIR")),
          downloader_config=LocalDownloaderConfig(),
          source_connection_config=LocalConnectionConfig(),
          partitioner_config=PartitionerConfig(
              partition_by_api=True,
              api_key=os.getenv("UNSTRUCTURED_API_KEY"),
              partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
              strategy="hi_res",
              additional_partition_args={
                  "split_pdf_page": True,
                  "split_pdf_allow_failed": True,
                  "split_pdf_concurrency_level": 15
              }
          ),
          chunker_config=ChunkerConfig(chunking_strategy="by_title"),
          embedder_config=EmbedderConfig(embedding_provider="huggingface"),
          destination_connection_config=KdbaiConnectionConfig(
              access_config=KdbaiAccessConfig(
                  api_key=os.getenv("KDBAI_API_KEY")
              ),
              endpoint=os.getenv("KDBAI_ENDPOINT")
          ),
          stager_config=KdbaiUploadStagerConfig(),
          uploader_config=KdbaiUploaderConfig(table_name=os.getenv("KDBAI_TABLE"))
      ).run()
  ```
</CodeGroup>

For the Unstructured Ingest CLI and the Unstructured Ingest Python library, you can use the `--partition-by-api` option (CLI) or `partition_by_api` (Python) parameter to specify where files are processed:

* To do local file processing, omit `--partition-by-api` (CLI) or `partition_by_api` (Python), or explicitly specify `partition_by_api=False` (Python).

  Local file processing does not use an Unstructured API key or API URL, so you can also omit the following, if they appear:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`

* To send files to the legacy [Unstructured Partition Endpoint](/api-reference/legacy-api/partition/overview) for processing, specify `--partition-by-api` (CLI) or `partition_by_api=True` (Python).

  Unstructured also requires an Unstructured API key and API URL, by adding the following:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`, representing your API key and API URL, respectively.

  <Note>
    You must specify the API URL only if you are not using the default API URL for Unstructured Ingest, which applies to **Let's Go**, **Pay-As-You-Go**, and **Business SaaS** accounts.

    The default API URL for Unstructured Ingest is `https://api.unstructuredapp.io/general/v0/general`, which is the API URL for the legacy[Unstructured Partition Endpoint](/api-reference/legacy-api/partition/overview). However, you should always use the URL that was provided to you when your Unstructured account was created. If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

    If you do not have an API key, [get one now](/api-reference/legacy-api/partition/overview).

    If you are using a **Business** account, the process
    for generating Unstructured API keys, and the Unstructured API URL that you use, are different.
    For instructions, see your Unstructured account administrator, or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
  </Note>
