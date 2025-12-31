# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/lancedb.md

# LanceDB

Batch process all your records to store structured outputs in LanceDB.

The requirements are as follows.

* A [LanceDB open source software (OSS) installation](https://lancedb.github.io/lancedb/basic/#installation) on a local machine, a server, or a virtual machine.
  (LanceDB Cloud is not supported.)

* For LanceDB OSS with local data storage:

  * The local path to the folder where the LanceDB data is (or will be) stored.
    See [Connect to a database](https://lancedb.github.io/lancedb/basic/#connect-to-a-database) in the LanceDB documentation.
  * The name of the target [LanceDB table](https://lancedb.github.io/lancedb/basic/#create-an-empty-table) within the local data folder.

    <Note>
      Unstructured recommends that the target table have a field named `record_id` with a text string data type.
      Unstructured can use this field to do intelligent record overwrites. Without this field, duplicate records
      might be written to the table or, in some cases, the operation could fail altogether.
    </Note>

* For LanceDB OSS with data storage in an Amazon S3 bucket:

  * The URI for the target Amazon S3 bucket and any target folder path within that bucket. Use the format `s3://<bucket-name>[/<folder-name>]`.

  * The name of the target [LanceDB table](https://lancedb.github.io/lancedb/guides/storage/#object-stores) within the Amazon S3 bucket.

    <Note>
      Unstructured recommends that the target table have a field named `record_id` with a text string data type.
      Unstructured can use this field to do intelligent record overwrites. Without this field, duplicate records
      might be written to the table or, in some cases, the operation could fail altogether.
    </Note>

  * The AWS access key ID and AWS secret access key for the AWS IAM entity that has access to the Amazon S3 bucket.

  For more information, see [AWS S3](https://lancedb.github.io/lancedb/guides/storage/#aws-s3) in the LanceDB documentation, along with the following video:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/hyDHfhVVAhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For LanceDB OSS with data storage in an Azure Blob Storage account:

  * The name of the target Azure Blob Storage account.
    \= The URI for the target container within that Azure Blob Storage account and any target folder path within that container. Use the format `az://<container-name>[/<folder-name>]`.

  * The name of the target [LanceDB table](https://lancedb.github.io/lancedb/guides/storage/#object-stores) within the Azure Blob Storage account.

    <Note>
      Unstructured recommends that the target table have a field named `record_id` with a text string data type.
      Unstructured can use this field to do intelligent record overwrites. Without this field, duplicate records
      might be written to the table or, in some cases, the operation could fail altogether.
    </Note>

  * The access key for the Azure Blob Storage account.

  For more information, see [Azure Blob Storage](https://lancedb.github.io/lancedb/guides/storage/#azure-blob-storage) in the LanceDB documentation, along with the following video:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/Vl3KCphlh9Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For LanceDB OSS with data storage in a Google Cloud Storage bucket:

  * The URI for the target Google Cloud Storage bucket and any target folder path within that bucket. Use the format `gs://<bucket-name>[/<folder-name>]`.

  * The name of the target [LanceDB table](https://lancedb.github.io/lancedb/guides/storage/#object-stores) within the Google Cloud Storage bucket.

    <Note>
      Unstructured recommends that the target table have a field named `record_id` with a text string data type.
      Unstructured can use this field to do intelligent record overwrites. Without this field, duplicate records
      might be written to the table or, in some cases, the operation could fail altogether.
    </Note>

  * A single-line string that contains the contents of the downloaded service account key file for the Google Cloud service account that has access to the
    Google Cloud Storage bucket.

  For more information, see [Google Cloud Storage](https://lancedb.github.io/lancedb/guides/storage/#google-cloud-storage) in the LanceDB documentation, along with the following video:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/HYaALQ0F-L4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

The LanceDB connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[lancedb]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* For LanceDB OSS with local data storage:

  * `LANCEDB_URI` - The local path to the folder where the LanceDB data is stored, represented by `--uri` (CLI) or `uri` (Python).
  * `LANCEDB_TABLE` - The name of the target LanceDB table within the local data folder, represented by `--table-name` (CLI) or `table_name` (Python).

* For LanceDB OSS with data storage in an Amazon S3 bucket:

  * `LANCEDB_URI` - The URI for the target Amazon S3 bucket and any target folder path within that bucket. Use the format `s3://<bucket-name>[/<folder-name>]`. This is represented by `--uri` (CLI) or `uri` (Python).
  * `LANCEDB_TABLE` - The name of the target LanceDB table within the Amazon S3 bucket, rrepresented by `--table-name` (CLI) or `table_name` (Python).
  * `AWS_ACCESS_KEY_ID` - The AWS access key ID for the AWS IAM entity that has access to the Amazon S3 bucket, represented by `--aws-access-key-id` (CLI) or `aws_access_key_id` (Python).
  * `AWS_SECRET_ACCESS_KEY` - The AWS secret access key for the AWS IAM entity that has access to the Amazon S3 bucket, represented by `--aws-secret-access-key` (CLI) or `aws_secret_access_key` (Python).

* For LanceDB OSS with data storage in an Azure Blob Storage account:

  * `LANCEDB_URI` - The URI for the target container within that Azure Blob Storage account and any target folder path within that container. Use the format `az://<container-name>[/<folder-name>]`. This is represented by `--uri` (CLI) or `uri` (Python).
  * `LANCEDB_TABLE` - The name of the target LanceDB table within the Azure Blob Storage account, represented by `--table-name` (CLI) or `table_name` (Python).
  * `AZURE_STORAGE_ACCOUNT_NAME` - The name of the target Azure Blob Storage account, represented by `--azure-storage-account-name` (CLI) or `azure_storage_account_name` (Python).
  * `AZURE_STORAGE_ACCOUNT_KEY` - The access key for the Azure Blob Storage account, represented by `--azure-storage-account-key` (CLI) or `azure_storage_account_key` (Python).

* For LanceDB OSS with data storage in a Google Cloud Storage bucket:

  * `LANCEDB_URI` - The URI for the target Google Cloud Storage bucket and any target folder path within that bucket. Use the format `gs://<bucket-name>[/<folder-name>]`. This is represented by `--uri` (CLI) or `uri` (Python).
  * `LANCEDB_TABLE` - The name of the target LanceDB table within the Google Cloud Storage bucket, represented by `--table-name` (CLI) or `table_name` (Python).
  * `GCS_SERVICE_ACCOUNT_KEY` - A single-line string that contains the contents of the downloaded service account key file for the Google Cloud service account
    that has access to the Google Cloud Storage bucket, represented by `--google-service-account-key` (CLI) or `google_service_account_key` (Python).

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector:

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  # For LanceDB OSS with local data storage:
  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    lancedb-local \
      --uri $LANCEDB_URI \
      --table-name $LANCEDB_TABLE

  # For LanceDB OSS with data storage in an Amazon S3 bucket:
  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    lancedb-aws \
      --aws-access-key-id $AWS_ACCESS_KEY_ID \
      --aws-secret-access-key $AWS_SECRET_ACCESS_KEY \
      --uri $LANCEDB_URI \
      --table-name $LANCEDB_TABLE \
      --timeout 30s

  # For LanceDB OSS with data storage in an Azure Blob Storage account:
  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    lancedb-azure \
      --azure-storage-account-name $AZURE_STORAGE_ACCOUNT_NAME \
      --azure-storage-account-key $AZURE_STORAGE_ACCOUNT_KEY \
      --uri $LANCEDB_URI \
      --table-name $LANCEDB_TABLE \
      --timeout 30s

  # For LanceDB OSS with data storage in a Google Cloud Storage bucket:
  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    lancedb-gcs \
      --google-service-account-key $GCS_SERVICE_ACCOUNT_KEY \
      --uri $LANCEDB_URI \
      --table-name $LANCEDB_TABLE \
      --timeout 30s
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.local import (
      LocalIndexerConfig,
      LocalDownloaderConfig,
      LocalConnectionConfig
  )
  from unstructured_ingest.processes.partitioner import PartitionerConfig
  from unstructured_ingest.processes.chunker import ChunkerConfig
  from unstructured_ingest.processes.embedder import EmbedderConfig

  # For LanceDB OSS with local data storage:
  # from unstructured_ingest.processes.connectors.lancedb.local import (
  #     LanceDBLocalConnectionConfig,
  #     LanceDBLocalAccessConfig,
  #     LanceDBUploadStagerConfig,
  #     LanceDBUploaderConfig
  # )

  # For LanceDB OSS with data storage in an Amazon S3 bucket:
  from unstructured_ingest.processes.connectors.lancedb.aws import (
      LanceDBS3ConnectionConfig,
      LanceDBS3AccessConfig,
      LanceDBUploadStagerConfig,
      LanceDBUploaderConfig
  )

  # For LanceDB OSS with data storage in an Azure Blob Storage account:
  # from unstructured_ingest.processes.connectors.lancedb.azure import (
  #     LanceDBAzureConnectionConfig,
  #     LanceDBAzureAccessConfig,
  #     LanceDBUploadStagerConfig,
  #     LanceDBUploaderConfig
  # )

  # For LanceDB OSS with data storage in a Google Cloud Storage bucket:
  # from unstructured_ingest.processes.connectors.lancedb.gcp import (
  #     LanceDBGCSConnectionConfig,
  #     LanceDBGCSAccessConfig,
  #     LanceDBUploadStagerConfig,
  #     LanceDBUploaderConfig
  # )

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

          # For LanceDB OSS with local data storage:
          # destination_connection_config=LanceDBLocalConnectionConfig(
          #     access_config=LanceDBLocalAccessConfig(),
          #     uri=os.getenv("LANCEDB_URI")
          # ),

          # For LanceDB OSS with data storage in an Amazon S3 bucket:
          destination_connection_config=LanceDBS3ConnectionConfig(
              access_config=LanceDBS3AccessConfig(
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
              ),
              uri=os.getenv("LANCEDB_URI"),
              timeout="30s"
          ),

          # For LanceDB OSS with data storage in an Azure Blob Storage account:
          # destination_connection_config=LanceDBAzureConnectionConfig(
          #     access_config=LanceDBAzureAccessConfig(
          #         azure_storage_account_name=os.getenv("AZURE_STORAGE_ACCOUNT_NAME"),
          #         azure_storage_account_key=os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
          #     ),
          #     uri=os.getenv("LANCEDB_URI"),
          #     timeout="30s"
          # ),

          # For LanceDB OSS with data storage in a Google Cloud Storage bucket:
          # destination_connection_config=LanceDBGCSConnectionConfig(
          #     access_config=LanceDBGCSAccessConfig(
          #         google_service_account_key=os.getenv("GCS_SERVICE_ACCOUNT_KEY")
          #     ),
          #     uri=os.getenv("LANCEDB_URI"),
          #     timeout="30s"
          # ),

          stager_config=LanceDBUploadStagerConfig(),
          uploader_config=LanceDBUploaderConfig(table_name=os.getenv("LANCEDB_TABLE"))
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
