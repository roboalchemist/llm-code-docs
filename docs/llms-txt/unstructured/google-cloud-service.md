# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/google-cloud-service.md

# Google Cloud Storage

Batch process all your records to store structured outputs in Google Cloud Service.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R57duYCxLi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A Google Cloud service account. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create#console).

* A service account key for the service account. See [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in
  [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

  To ensure maximum compatibility across Unstructured service offerings, you should give the service account key information to Unstructured as
  a single-line string that contains the contents of the downloaded service account key file (and not the service account key file itself).
  To print this single-line string without line breaks, suitable for copying, you can run one of the following commands from your Terminal or Command Prompt.
  In this command, replace `<path-to-downloaded-key-file>` with the path to the service account key file that you downloaded by following the preceding instructions.

  * For macOS or Linux:
    ```text  theme={null}
    tr -d '\n' < <path-to-downloaded-key-file>
    ```
  * For Windows:
    ```text  theme={null}
    (Get-Content -Path "<path-to-downloaded-key-file>" -Raw).Replace("`r`n", "").Replace("`n", "")
    ```

* The URI for a Google Cloud Storage bucket. This URI consists of the target bucket name, plus any target folder within the bucket, expressed as `gs://<bucket-name>[/folder-name]`. [Create a bucket](https://cloud.google.com/storage/docs/creating-buckets#console).

  This bucket must have, at minimum, one of the following roles applied to the target Google Cloud service account:

  * `Storage Object Viewer` for bucket read access.
  * `Storage Object User` for bucket write access.
  * The `Storage Object Admin` role provides read and write access, plus access to additional bucket operations.

  To apply one of these roles to a service account for a bucket, see [Add a principal to a bucket-level policy](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add)
  in [Set and manage IAM policies on buckets](https://cloud.google.com/storage/docs/access-control/using-iam-permissions).

The Google Cloud Storage connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[gcs]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `GCS_SERVICE_ACCOUNT_KEY` - The Google Cloud service account key for Google Cloud Storage, represented by `--service-account-key` (CLI) or `service_account_key` (Python).
* `GCS_REMOTE_URL` - The Google Cloud Storage bucket URL, represented by `--remote-url` (CLI) or `remote_url` (Python).

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector:

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --strategy hi_res \
      --chunk-elements \
      --embedding-provider huggingface \
      --num-processes 2 \
      --verbose \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
    gcs \
      --service-account-key $GCS_SERVICE_ACCOUNT_KEY \
      --remote-url $GCS_REMOTE_URL
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.fsspec.gcs import (
      GcsConnectionConfig,
      GcsAccessConfig,
      GcsUploaderConfig
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
          destination_connection_config=GcsConnectionConfig(
              access_config=GcsAccessConfig(
                  service_account_key=os.getenv("GCS_SERVICE_ACCOUNT_KEY")
              )
          ),
          uploader_config=GcsUploaderConfig(remote_url=os.getenv("GCS_REMOTE_URL"))
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
