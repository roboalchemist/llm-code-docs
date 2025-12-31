# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/chroma.md

# Chroma

Batch process all your records to store structured outputs in a Chroma account.

The requirements are as follows.

* A Chroma server. You can connect to a [hosted Chroma Cloud server](https://trychroma.com/signup) or [deploy your own server](https://docs.trychroma.com/deployment).
* The Chroma server's hostname or IP address, and the server's port number. For Chroma Cloud, the host is `api.trychroma.com`, and the port number is `8000`.
* If you are using local Chroma, the [path to the folder where you store your database](https://docs.trychroma.com/docs/run-chroma/persistent-client).
* The name of the tenant that you want to access on the server.
* The name of the database that you want to access in the tenant.
* The name of the collection that you want to access in the database.

The Chroma connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[chroma]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `CHROMA_HOST` - The , represented by `--host` (CLI) or `host` (Python). Chroma Cloud uses `api.trychroma.com`.
* `CHROMA_PORT` - The , represented by `--port` (CLI) or `port` (Python). Chroma Cloud uses port `8000`.
* `CHROMA_TENANT` - The name of the tenant that you want to access on the Chroma server, represented by `--tenant` (CLI) or `tenant` (Python).
* `CHROMA_DATABASE` - The name of the database that you want to access in the tenant, represented by `--database` (CLI) or `database` (Python).
* `CHROMA_COLLECTION` - The name of the collection that you want to access in the database, represented by `--collection-name` (CLI) or `collection_name` (Python).

Additional settings include:

* `--path` (CLI) or `path` (Python): The location where Chroma is persisted if you are not connecting through HTTP.
* `--settings` (CLI) or `settings` (Python): A dictionary of settings to communicate with the Chroma server, for example: `'{"persist_directory":"./chroma-persist"}'`.
* `--headers` (CLI) or `headers` (Python): A dictionary of headers to send to the Chroma server, for example: `'{"Authorization":"Basic()"}'`.
* `--ssl` (CLI) or `ssl` (Python): True to use SSL for the connection.

In order to use Chroma Cloud, you should have this configuration:

* `host=api.trychroma.com`
* `port=8000`
* Get your `tenant` ID from the [Chroma dashboard](https://trychroma.com).
* `headers={'x-chroma-token': 'YOUR_API_KEY'}`
* `ssl` should be enabled.

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector.

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --chunk-elements \
      --embedding-provider huggingface \
      --num-processes 2 \
      --verbose \
      --work-dir $WORK_DIR \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --strategy hi_res \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    chroma \
      --host $CHROMA_HOST \
      --port $CHROMA_PORT \
      --collection-name $CHROMA_COLLECTION \
      --tenant $CHROMA_TENANT \
      --database $CHROMA_DATABASE \
      --settings "{\"persist_directory\":\"./chroma-persist\"}" \
      --headers "{\"Authorization\":\"Basic()\"}" \
      --batch-size 80 \
      --ssl
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.chroma import (
      ChromaAccessConfig,
      ChromaConnectionConfig,
      ChromaUploadStagerConfig,
      ChromaUploaderConfig
  )
  from unstructured_ingest.processes.connectors.local import (
      LocalIndexerConfig,
      LocalConnectionConfig,
      LocalDownloaderConfig
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
              additional_partition_args={
                  "split_pdf_page": True,
                  "split_pdf_allow_failed": True,
                  "split_pdf_concurrency_level": 15
              }
          ),
          chunker_config=ChunkerConfig(chunking_strategy="by_title"),
          embedder_config=EmbedderConfig(embedding_provider="huggingface"),
          destination_connection_config=ChromaConnectionConfig(
              access_config=ChromaAccessConfig(
                  settings={"persist_directory":"./chroma-persist"},
                  headers={"Authorization":"Basic()"}
              ),
              host=os.getenv("CHROMA_HOST"),
              port=os.getenv("CHROMA_PORT"),
              tenant=os.getenv("CHROMA_TENANT"),
              database=os.getenv("CHROMA_DATABASE"),
              collection_name=os.getenv("CHROMA_COLLECTION")
          ),
          stager_config=ChromaUploadStagerConfig(),
          uploader_config=ChromaUploaderConfig()
      ).run()

  ```
</CodeGroup>

For the Unstructured Ingest CLI and the Unstructured Ingest Python library, you can use the `--partition-by-api` option (CLI) or `partition_by_api` (Python) parameter to specify where files are processed:

* To do local file processing, omit `--partition-by-api` (CLI) or `partition_by_api` (Python), or explicitly specify `partition_by_api=False` (Python).

  Local file processing does not use an Unstructured API key or API URL, so you can also omit the following, if they appear:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`

* To send files to the [Unstructured Partition Endpoint](/api-reference/partition/overview) for processing, specify `--partition-by-api` (CLI) or `partition_by_api=True` (Python).

  Unstructured also requires an Unstructured API key and API URL, by adding the following:

  * `--api-key $UNSTRUCTURED_API_KEY` (CLI) or `api_key=os.getenv("UNSTRUCTURED_API_KEY")` (Python)
  * `--partition-endpoint $UNSTRUCTURED_API_URL` (CLI) or `partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")` (Python)
  * The environment variables `UNSTRUCTURED_API_KEY` and `UNSTRUCTURED_API_URL`, representing your API key and API URL, respectively.

  <Note>
    You must specify the API URL only if you are not using the default API URL for Unstructured Ingest, which applies to **Let's Go**, **Pay-As-You-Go**, and **Business SaaS** accounts.

    The default API URL for Unstructured Ingest is `https://api.unstructuredapp.io/general/v0/general`, which is the API URL for the [Unstructured Partition Endpoint](/api-reference/partition/overview). However, you should always use the URL that was provided to you when your Unstructured account was created. If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

    If you do not have an API key, [get one now](/api-reference/partition/overview).

    If you are using a **Business** account, the process
    for generating Unstructured API keys, and the Unstructured API URL that you use, are different.
    For instructions, see your Unstructured account administrator, or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
  </Note>
