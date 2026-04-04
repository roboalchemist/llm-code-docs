# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/vectara.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Vectara

<NewDocument />

Batch process all your records to store structured outputs in Vectara.

The requirements are as follows.

* A [Vectara account](https://console.vectara.com/signup).
* The [customer ID](https://docs.vectara.com/docs/console-ui/vectara-console-overview#view-the-customer-id) for the account.
* The name and key for the target [corpus](https://docs.vectara.com/docs/console-ui/creating-a-corpus) in the account.
* The [OAuth authentication URL, client ID, and client secret](https://docs.vectara.com/docs/console-ui/app-clients) for accessing the target corpus.

The Vectara connector dependencies.

```bash  theme={null}
pip install "unstructured-ingest[vectara]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `VECTARA_CUSTOMER_ID` - The customer ID for the target Vectara account, represented by `--customer-id` (CLI) or `customer_id` (Python).
* `VECTARA_CORPUS_NAME` - The name of the target corpus in the account, represented by `--corpus-name` (CLI) or `corpus_name` (Python).
* `VECTARA_CORPUS_KEY` - The name of the corpus's key, represented by `--corpus-key` (CLI) or `corpus_key` (Python).
* `VECTARA_OAUTH_TOKEN_URL` - The OAuth token URL for getting and refreshing OAuth access tokens in the account, represented by `--token-url` (CLI) or `token_url` (Python).
* `VECTARA_OAUTH_CLIENT_ID` - A valid OAuth client ID in the account, represented by `--oauth-client-id` (CLI) or `oauth_client_id` (Python).
* `VECTARA_OAUTH_CLIENT_SECRET` - The OAuth client secret for the client ID, represented by `--oauth-client-secret` (CLI) or `oauth_client_secret` (Python).

Now call the Unstructured CLI or Python SDK. The source connector can be any of the ones supported.

This example uses the local source connector.

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding is optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    vectara \
      --customer-id $VECTARA_CUSTOMER_ID \
      --corpus-name $VECTARA_CORPUS_NAME \
      --corpus-key $VECTARA_CORPUS_KEY \
      --oauth-client-id $VECTARA_OAUTH_CLIENT_ID \
      --oauth-secret $VECTARA_OAUTH_CLIENT_SECRET \
      --token-url $VECTARA_OAUTH_TOKEN_URL
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.vectara import (
      VectaraAccessConfig,
      VectaraConnectionConfig,
      VectaraUploadStagerConfig,
      VectaraUploaderConfig
  )
  from unstructured_ingest.processes.connectors.local import (
      LocalIndexerConfig,
      LocalConnectionConfig,
      LocalDownloaderConfig
  )
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  # Chunking and embedding is optional.

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
          destination_connection_config=VectaraConnectionConfig(
              access_config=VectaraAccessConfig(
                  oauth_client_id=os.getenv("VECTARA_OAUTH_CLIENT_ID"),
                  oauth_secret=os.getenv("VECTARA_OAUTH_CLIENT_SECRET")
              ),
              customer_id=os.getenv("VECTARA_CUSTOMER_ID"),
              corpus_name=os.getenv("VECTARA_CORPUS_NAME"),
              corpus_key=os.getenv("VECTARA_CORPUS_KEY"),
              token_url=os.getenv("VECTARA_OAUTH_TOKEN_URL")
          ),
          stager_config=VectaraUploadStagerConfig(),
          uploader_config=VectaraUploaderConfig()
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
