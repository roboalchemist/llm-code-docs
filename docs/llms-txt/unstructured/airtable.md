# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/airtable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Airtable

Connect Airtable to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your data and store structured outputs locally on your filesystem.

The requirements are as follows.

* An [Airtable](https://www.airtable.com/) account. [Create a free Airtable account](https://airtable.com/signup).

* An Airtable personal access token. [Create a personal access token](https://support.airtable.com/docs/creating-and-using-api-keys-and-access-tokens).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/c3gvIWAAcTY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The ID of the Airtable base to access. [Create a base](https://www.airtable.com/guides/build/create-a-base). [Get a base's ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-url-ids).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/rU347YVMm2M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The ID of the table to access in the base. [Create a table](https://www.airtable.com/guides/build/create-a-table). [Get a table's ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-url-ids).

* The ID of the view to access in the table. [Create a view](https://www.airtable.com/guides/build/create-custom-views-of-data). [Get a view's ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-url-ids).

By default, Unstructured processes all tables from all bases within an Airtable organization. You can limit the
tables that Unstructured ingests data from within Airtable by specifying a list of Airtable paths.
An Airtable path uses the following structure: `base_id/table_id(optional)/view_id(optional)`

For example, given the following example Airtable URL:

```text  theme={null}
https://airtable.com/appr9nKeXLAtg6bgn/tblZ8uT1GY7NLbWit/viwDcpzf9dP0Gqz5J
```

* The base's ID is `appr9nKeXLAtg6bgn`. The base's path is `appr9nKeXLAtg6bgn`.
* The table's ID is `tblZ8uT1GY7NLbWit`. The table's path is `appr9nKeXLAtg6bgn/tblZ8uT1GY7NLbWit`.
* The view's ID is `viwDcpzf9dP0Gqz5J`. The view's path is `appr9nKeXLAtg6bgn/tblZ8uT1GY7NLbWit/viwDcpzf9dP0Gqz5J`.

You can call the Airtable API to get lists of available IDs for Airtable bases, tables, and views in bulk, as follows:

* [Base IDs](https://airtable.com/developers/web/api/list-bases)
* [Table and view IDs](https://airtable.com/developers/web/api/get-base-schema)
* [Base, table, and view IDs](https://pyairtable.readthedocs.io/en/latest/metadata.html)

The Airtable connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[airtable]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

These environment variables:

* `AIRTABLE_TOKEN` - The Airtable personal access token, represented by `--personal-access-token` (CLI) or `personal_access_token` (Python).
* `AIRTABLE_PATHS` - The list of Airtable paths to process, represented by `--list-of-paths` (CLI) or `list_of_paths` (Python).

Now call the Unstructured CLI or Python. The destination connector can be any of the ones supported. This example uses the local destination connector.

This example sends data to Unstructured for processing by default. To process data locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  unstructured-ingest \
    airtable \
      --personal-access-token $AIRTABLE_PERSONAL_ACCESS_TOKEN \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --num-processes 2 \
      --reprocess \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.airtable import (
      AirtableIndexerConfig,
      AirtableDownloaderConfig,
      AirtableConnectionConfig,
      AirtableAccessConfig
  )

  from unstructured_ingest.processes.connectors.local import LocalUploaderConfig
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig

  # Chunking is optional.

  if __name__ == "__main__":
      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=AirtableIndexerConfig(list_of_paths=[os.getenv("AIRTABLE_PATHS")]),
          downloader_config=AirtableDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")),
          source_connection_config=AirtableConnectionConfig(
              access_config=AirtableAccessConfig(
                  personal_access_token=os.getenv("AIRTABLE_TOKEN")
              )
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
