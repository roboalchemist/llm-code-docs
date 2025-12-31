# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/sftp.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/sftp.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/sftp.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/sftp.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/sftp.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/sftp.md

# SFTP

Batch process all your records to store structured outputs in SFTP.

The requirements are as follows.

* The SFTP server hostname, port, username, and password.

  SFTP servers are offered by several vendors. For example, the following video shows how to create and set up an SFTP server by using AWS Transfer Family:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/3_HHSnoFsoM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The directory path to start accessing data from, specified as `sftp://<path>/<to>/<directory>`.

See the [SFTP documentation](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol).

The SFTP connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[sftp]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `SFTP_HOST` - The SFTP hostname, represented by `--host` (CLI) or `host` (Python).
* `SFTP_PORT` - The SFTP port number, represented by `--port` (CLI) or `port` (Python).
* `SFTP_REMOTE_URL` - The directory path to start accessing data from, represented by `--remote-url` (CLI) or `remote_url` (Python).
* `SFTP_USERNAME` - The SFTP username, represented by `--username` (CLI) or `username` (Python).
* `SFTP_PASSWORD` - The SFTP password, represented by `--password` (CLI) or `password` (Python).

Now call the Unstructured Ingest CLI or the Unstructured Ingest Python library. The source connector can be any of the ones supported. This example uses the local source connector.

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --strategy hi_res \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
    sftp \
      --host $SFTP_HOST \
      --port $SFTP_PORT \
      --username $SFTP_USERNAME \
      --password $SFTP_PASSWORD \
      --remote-url $SFTP_REMOTE_URL
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.fsspec.sftp import (
      SftpConnectionConfig,
      SftpAccessConfig,
      SftpUploaderConfig
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
          destination_connection_config=SftpConnectionConfig(
              access_config=SftpAccessConfig(password=os.getenv("SFTP_PASSWORD")),
              host=os.getenv("SFTP_HOST"),
              port=os.getenv("SFTP_PORT"),
              username=os.getenv("SFTP_USERNAME")
          ),
          uploader_config=SftpUploaderConfig(remote_url=os.getenv("SFTP_REMOTE_URL"))
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
