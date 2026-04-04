# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/singlestore.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/singlestore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SingleStore

Batch process all your records to store structured outputs in a SingleStore account.

The requirements are as follows.

* A SingleStore deployment, database, and table. [Learn how](https://www.singlestore.com/blog/how-to-get-started-with-singlestore/).
* The hostname for the SingleStore deployment.
* The port for the host.
* The username for the deployment.
* The password for the user.
* The name of the database in the deployment.
* The name of the table in the database.

To get the values for the hostname, port, username, and password:

1. In your SingleStore account's dashboard sidebar, click **Deployments**.
2. From the drop-down list at the top of the **Deployments** page, select your deployment.
3. On the **Overview** tab, in the **Compute** area, in the **Connect** drop-down list for your deployment, select
   **Your App**.
4. If a **Create User** dialog box appears, note the **User** name and **Password** values.
5. In the **Connect to Workspace** pane's **Your App** tab, note the string in the following format:

```
<user-name>:<password>@<host>:<port>
```

* `<user-name>` is the username.
* `<password>` is the user's password.
* `<host>` is the workspace's hostname.
* `<post>` is the host's port.

To get the values for the database and table names:

1. In your SingleStore dashboard's sidebar, click **Deployments**.
2. From the drop-down list at the top of the **Deployments** page, select your deployment.
3. On the **Databases** tab, note **Name** of your database.
4. Click the database and, on the **Tables** tab, note the name of your table.

The SingleStore connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[singlestore]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

These environment variables:

* `SINGLESTORE_HOST` - The hostname for the SingleStore deployment, represented by `--host` (CLI) or `host` (Python).
* `SINGLESTORE_PORT` - The port for the host, represented by `--port` (CLI) or `port` (Python).
* `SINGLESTORE_USER` - The username for the deployment, represented by `--user` (CLI) or `user` (Python).
* `SINGLESTORE_PASSWORD` - The password for the user, represented by `--password` (CLI) or `password` (Python).
* `SINGLESTORE_DB` - The name of the database in the deployment, represented by `--database` (CLI) or `database` (Python).
* `SINGLESTORE_TABLE` - The name of the table in the database, represented by `--table-name` (CLI) or `table_name` (Python).

The table's schema must match the schema of the documents that Unstructured produces.

During insertion, JSON objects are flattened, and underscores are placed between nested object names.
For example, the following JSON object matches a column in the table named `data_source_date_created`:

```json  theme={null}
{
    "...": "...",
    "data_source": {
        "date_created": "1719963233.949"
    },
    "...": "..."
}
```

The `metadata` object itself is also flattened in a similar way. However, for nested objects in `metadata`,
the column in the table does not start with `metadata_`. For example, the following JSON object matches a
column in the table named `last_modified`:

```json  theme={null}
{
    "...": "...",
    "metadata": {
        "...": "...",
        "last_modified": "2022-12-16T17:04:16-05:00",
        "...": "..."
    },
    "...": "..."
}
```

Unstructured cannot provide a table schema that is guaranteed to work in all
circumstances. This is because these schemas will vary based on your source files' types; how you
want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

You can adapt the following table schema example for your own needs:

```sql  theme={null}
CREATE TABLE elements (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    record_id TEXT,
    element_id TEXT,
    text TEXT,
    embeddings Vector(384),
    parent_id TEXT,
    page_number TEXT,
    is_continuation BOOLEAN,
    orig_elements TEXT,
    partitioner_type TEXT
);
```

See also:

* [CREATE TABLE](https://docs.singlestore.com/cloud/reference/sql-reference/data-definition-language-ddl/create-table/)
  in the SingleStore documentation
* [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

Now call the Unstructured Ingest CLI or the Unstructured Ingest Python library. The source connector can be any of the ones supported. This example uses the local source connector.

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --partition-by-api \
      --strategy hi_res \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    singlestore \
      --host $SINGLESTORE_HOST \
      --port $SINGLESTORE_PORT \
      --user $SINGLESTORE_USER \
      --password $SINGLESTORE_PASSWORD \
      --database $SINGLESTORE_DB \
      --table-name $SINGLESTORE_TABLE
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
  from unstructured_ingest.processes.connectors.singlestore import (
      SingleStoreConnectionConfig,
      SingleStoreAccessConfig,
      SingleStoreUploadStagerConfig,
      SingleStoreUploaderConfig
  )

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
          destination_connection_config=SingleStoreConnectionConfig(
              host=os.getenv("SINGLESTORE_HOST"),
              port=os.getenv("SINGLESTORE_PORT"),
              user=os.getenv("SINGLESTORE_USER"),
              database=os.getenv("SINGLESTORE_DB"),
              access_config=SingleStoreAccessConfig(
                  password=os.getenv("SINGLESTORE_PASSWORD")
              )
          ),
          stager_config=SingleStoreUploadStagerConfig(drop_empty_cols=True),
          uploader_config=SingleStoreUploaderConfig(table_name=os.getenv("SINGLESTORE_TABLE"))
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
