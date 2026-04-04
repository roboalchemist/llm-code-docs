# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/duckdb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# DuckDB

Batch process all your records to store structured outputs in a DuckDB installation.

The requirements are as follows.

* A [DuckDB installation](https://duckdb.org/docs/installation).

* A [persistent database](https://duckdb.org/docs/connect/overview.html#persistent-database), for example by running the
  [DuckDB CLI](https://duckdb.org/docs/api/cli) command `duckdb <my-database-filename>.db` or
  `duckdb <my-database-filename>.duckdb`, replacing `<my-database-filename>` with the name of the target file.

* The path to the target persistent database file.

* A schema in the target database.

  * [Create a schema](https://duckdb.org/docs/sql/statements/create_schema.html).
  * You can list available schemas and their parent catalogs by running the following DuckDB CLI command:

    ```sql  theme={null}
    SELECT * FROM information_schema.schemata;
    ```

  The DuckDB connector uses the default schema name of `main` if not otherwise specified.

* A table in the target schema.

  * [Create a table](https://duckdb.org/docs/sql/statements/create_table).
  * You can list available tables in a schema by running the following DuckDB CLI commands, replacing the target catalog and schema names:

    ```sql  theme={null}
    USE <catalog_name>.<schema_name>;
    SHOW TABLES;
    ```

  The DuckDB connector uses the default table name of `elements` if not otherwise specified.

  For maximum compatibility, Unstructured recommends the following table schema:

  ```sql  theme={null}
  CREATE TABLE elements (
      id VARCHAR,
      element_id VARCHAR,
      text TEXT,
      embeddings FLOAT[],
      type VARCHAR,
      system VARCHAR,
      layout_width DECIMAL,
      layout_height DECIMAL,
      points TEXT,
      url TEXT,
      version VARCHAR,
      date_created INTEGER,
      date_modified INTEGER,
      date_processed DOUBLE,
      permissions_data TEXT,
      record_locator TEXT,
      category_depth INTEGER,
      parent_id VARCHAR,
      attached_filename VARCHAR,
      filetype VARCHAR,
      last_modified TIMESTAMP,
      file_directory VARCHAR,
      filename VARCHAR,
      languages VARCHAR[],
      page_number VARCHAR,
      links TEXT,
      page_name VARCHAR,
      link_urls VARCHAR[],
      link_texts VARCHAR[],
      sent_from VARCHAR[],
      sent_to VARCHAR[],
      subject VARCHAR,
      section VARCHAR,
      header_footer_type VARCHAR,
      emphasized_text_contents VARCHAR[],
      emphasized_text_tags VARCHAR[],
      text_as_html TEXT,
      regex_metadata TEXT,
      detection_class_prob DECIMAL,
      partitioner_type VARCHAR
  );
  ```

  You can list the schema of a table by running the following DuckDB CLI commands, replacing the target catalog, schema, and table names:

  ```sql  theme={null}
  USE <catalog_name>.<schema_name>;
  DESCRIBE TABLE <table_name>;
  ```

The DuckDB connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[duckdb]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `DUCKDB_DATABASE` - The path to the target DuckDB persistent database file with the extension `.db` or `.duckdb`, represented by `--database` (CLI) or `database` (Python).
* `DUCKDB_DB_SCHEMA` - The name of the target schema in the database, represented by `--db-schema` (CLI) or `db_schema` (Python).
* `DUCKDB_TABLE` - The name of the target table in the schema, represented by `--table` (CLI) or `table` (Python).

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector.

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
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    duckdb \
      --database $DUCKDB_DATABASE \
      --db-schema $DUCKDB_DB_SCHEMA \
      --table $DUCKDB_TABLE
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.duckdb.duckdb import (
      DuckDBAccessConfig,
      DuckDBConnectionConfig,
      DuckDBUploadStagerConfig,
      DuckDBUploaderConfig
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
          destination_connection_config=DuckDBConnectionConfig(
              access_config=DuckDBAccessConfig(),
              database=os.getenv("DUCKDB_DATABASE"),
              db_schema=os.getenv("DUCKDB_DB_SCHEMA"),
              table=os.getenv("DUCKDB_TABLE")
          ),
          stager_config=DuckDBUploadStagerConfig(),
          uploader_config=DuckDBUploaderConfig(batch_size=50)
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
