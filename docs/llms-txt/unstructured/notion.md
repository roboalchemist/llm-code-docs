# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/notion.md

# Notion

Connect Notion to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* A Notion access token for an
  [internal integration](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up) or
  [public integration](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up).

* The IDs of any specific target Notion [databases](https://developers.notion.com/docs/working-with-databases). To get a database's ID:

  1. Open the database as a full page in Notion.

  2. Click **Share**, and then click **Copy link**.

  3. Paste the link in your text editor. The URL uses the following format:

     ```text  theme={null}
     https://www.notion.so/{workspace_name}/{database_id}?v={view_id}
     ```

  4. Find the part that corresponds to `{database_id}` in the URL you pasted. It is a 36-character string. This value is the database's ID.

     Note that if you receive a database ID by calling the Notion API, for example from the Notion search endpoint, it will contain hyphens in the UUIDv4 format. You may use either the hyphenated or un-hyphenated ID.

* The IDs of any specific target Notion [pages](https://developers.notion.com/docs/working-with-page-content). To get a page's ID:

  1. Open the page in Notion.
  2. Click **Share**, and then click **Copy link**.
  3. Paste the link in your text editor. The URL ends in a page ID. It should be a 32-character string.
  4. Format this value by inserting hyphens (`-`) in the following pattern: `8-4-4-4-12` (each number is the length of characters between the hyphens).

     Example: `1429989fe8ac4effbc8f57f56486db54` becomes `1429989f-e8ac-4eff-bc8f-57f56486db54`.

     This value is the page's ID.

The Notion connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[notion]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `NOTION_ACCESS_TOKEN` - The API key for the Notion integration, represented by `--notion-api-key` (CLI) or `notion_api_key` (Python).

Now call the Unstructured CLI or Python. The destination connector can be any of the ones supported. This example uses the local destination connector.

This example sends data to Unstructured for processing by default. To process data locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional. 

  unstructured-ingest \
    notion \
      --notion-api-key $NOTION_ACCESS_TOKEN \
      --page-ids 4b1a4fff-d740-4e59-aa9f-cc5c7c2b4789,47dcbd6d-13f1-4fc1-af7d-5fc147697c00 \
      --database-ids 1382c376-5a0a-8034-a3c3-d33402979df2,f2a60ad9-c466-4b06-859d-1ab176dea8c8 \
      --recursive \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.notion.connector import (
      NotionIndexerConfig,
      NotionDownloaderConfig,
      NotionConnectionConfig,
      NotionAccessConfig
  )

  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  from unstructured_ingest.processes.connectors.local import LocalUploaderConfig

  # Chunking and embedding are optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=NotionIndexerConfig(
              page_ids=[
                  "4b1a4fff-d740-4e59-aa9f-cc5c7c2b4789",
                  "47dcbd6d-13f1-4fc1-af7d-5fc147697c00"
              ],
              database_ids=[
                  "1382c376-5a0a-8034-a3c3-d33402979df2", 
                  "f2a60ad9-c466-4b06-859d-1ab176dea8c8"
              ],
              recursive=True
          ),
          downloader_config=NotionDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")),
          source_connection_config=NotionConnectionConfig(
              access_config=NotionAccessConfig(notion_api_key=os.getenv("NOTION_ACCESS_TOKEN"))
          ),
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
          uploader_config=LocalUploaderConfig(output_dir=os.getenv("LOCAL_FILE_OUTPUT_DIR"))
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
