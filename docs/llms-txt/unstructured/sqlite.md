# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/sqlite.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/sqlite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SQLite

Batch process all your records to store structured outputs in a SQLite schema.

Insert query is currently limited to append.

The requirements are as follows.

* A SQLite instance. [Download and install SQLite](https://www.sqlitetutorial.net/download-install-sqlite/).
* A SQLite database. [Create a database](https://www.sqlite.org/quickstart.html).
* The path to the database's `.db` file.
* A table in the database. [Create a table](https://www.sqlite.org/cli.html).

  The table's schema must match the schema of the documents that Unstructured produces.
  Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  You can adapt the following table schema example for your own needs:

  ```sql SQLite theme={null}
  CREATE TABLE elements (
      id TEXT PRIMARY KEY,
      record_id TEXT,
      element_id TEXT,
      text TEXT,
      embeddings TEXT,
      parent_id TEXT,
      page_number INTEGER,
      is_continuation INTEGER,
      orig_elements TEXT,
      partitioner_type TEXT
  );
  ```

  See also:

  * [CREATE TABLE](https://www.sqlite.org/lang_createtable.html) for SQLite
  * [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `SQLITE_DB_PATH` - The path to the database's `.db` file, represented by `--database` (CLI) or `database` (Python).

Now call the Unstructured Ingest CLI or the Unstructured Ingest Python library. The source connector can be any of the ones supported. This example uses the local source connector:

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Specify which fields to output in the processed data. This can help prevent
  # database record insert issues, where a particular field in the processed data
  # does not match a column in the database table on insert.
  metadata_includes="id,element_id,text,embeddings,type,system,layout_width,\
  layout_height,points,url,version,date_created,date_modified,date_processed,\
  permissions_data,record_locator,category_depth,parent_id,attached_filename,\
  filetype,last_modified,file_directory,filename,languages,page_number,links,\
  page_name,link_urls,link_texts,sent_from,sent_to,subject,section,\
  header_footer_type,emphasized_text_contents,emphasized_text_tags,\
  text_as_html,regex_metadata,detection_class_prob"

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --num-processes 2 \
      --verbose \
      --strategy hi_res \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --metadata-include "$metadata_includes" \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    sqlite \
      --database-path $SQLITE_DB_PATH
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.sql.sqlite import (
      SQLiteConnectionConfig,
      SQLiteAccessConfig,
      SQLiteUploaderConfig,
      SQLiteUploadStagerConfig
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
      # Specify which fields to output in the processed data. This can help prevent
      # database record insert issues, where a particular field in the processed data
      # does not match a column in the database table on insert.
      metadata_includes = [
          "id", "element_id", "text", "embeddings", "type", "system", "layout_width",
          "layout_height", "points", "url", "version", "date_created", "date_modified",
          "date_processed", "permissions_data", "record_locator", "category_depth",
          "parent_id", "attached_filename", "filetype", "last_modified", "file_directory",
          "filename", "languages", "page_number", "links", "page_name", "link_urls",
          "link_texts", "sent_from", "sent_to", "subject", "section", "header_footer_type",
          "emphasized_text_contents", "emphasized_text_tags", "text_as_html", "regex_metadata",
          "detection_class_prob"
      ]

      Pipeline.from_configs(
          context=ProcessorConfig(),
          indexer_config=LocalIndexerConfig(input_path=os.getenv("LOCAL_FILE_INPUT_DIR")),
          downloader_config=LocalDownloaderConfig(),
          source_connection_config=LocalConnectionConfig(),
          partitioner_config=PartitionerConfig(
              partition_by_api=True,
              api_key=os.getenv("UNSTRUCTURED_API_KEY"),
              partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
              metadata_include=metadata_includes,
              additional_partition_args={
                  "split_pdf_page": True,
                  "split_pdf_allow_failed": True,
                  "split_pdf_concurrency_level": 15
              }
          ),
          chunker_config=ChunkerConfig(chunking_strategy="by_title"),
          embedder_config=EmbedderConfig(embedding_provider="huggingface"),
          destination_connection_config=SQLiteConnectionConfig(
              access_config=SQLiteAccessConfig(),
              database_path=os.getenv("SQLITE_DB_PATH")
          ),
          stager_config=SQLiteUploadStagerConfig(),
          uploader_config=SQLiteUploaderConfig()
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
