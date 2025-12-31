# Source: https://docs.unstructured.io/ui/sources/opensearch.md

# Source: https://docs.unstructured.io/ui/destinations/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/opensearch.md

# Source: https://docs.unstructured.io/ui/sources/opensearch.md

# Source: https://docs.unstructured.io/ui/destinations/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/opensearch.md

# OpenSearch

Batch process all your records to store structured outputs in OpenSearch.

The requirements are as follows.

* An OpenSearch instance, such as an [AWS OpenSearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/setting-up.html) instance...

  <iframe width="560" height="315" src="https://www.youtube.com/embed/BNOYTbRbaFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  ...or a [local](https://opensearch.org/downloads.html) instance.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/Rew3_pNnYIs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  In all cases, the [OpenSearch version](https://github.com/opensearch-project/opensearch-py/blob/main/COMPATIBILITY.md) must be compatible with the client version of the [opensearch-py](https://github.com/opensearch-project/opensearch-py/blob/main/COMPATIBILITY.md) package on PyPI.

* The instance's hostname and port number. To learn how, see:

  * [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html) for AWS OpenSearch instances.
  * [Communicate with OpenSearch](https://opensearch.org/docs/latest/getting-started/communicate/) for local OpenSearch instances.

* The name of the search index on the instance. [Create an index](https://opensearch.org/docs/latest/api-reference/index-apis/create-index/).

  The OpenSearch index that you use must have a schema that is compatible with the schema of the documents
  that Unstructured produces for you. Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  You can adapt the following index schema example for your own needs:

  ```json  theme={null}
  {
      "settings": {
          "index": {
              "knn": true,
              "knn.algo_param.ef_search": 100
          }
      },
      "mappings": {
          "properties": {
              "record_id": {
                  "type": "text"
              },
              "element_id": {
                  "type": "keyword"
              },
              "text": {
                  "type": "text"
              },
              "embeddings": {
                  "type": "knn_vector",
                  "dimension": 384
              },
              "metadata": {
                  "type": "object",
                  "properties": {
                      "parent_id": {
                          "type": "text"
                      },
                      "page_number": {
                          "type": "integer"
                      },
                      "is_continuation": {
                         "type": "boolean"
                      },
                      "orig_elements": {
                         "type": "text"
                      },
                      "partitioner_type": {
                         "type": "text"
                      }
                  }
              }
          }
      }
  }
  ```

  See also:

  * [Mappings and field types](https://opensearch.org/docs/latest/field-types/)
  * [Explicit mapping](https://opensearch.org/docs/latest/field-types/#explicit-mapping)
  * [Dynamic mapping](https://opensearch.org/docs/latest/field-types/#dynamic-mapping)
  * [Unstructured document elements and metadata](/api-reference/partition/document-elements)

* If you're using basic authentication to the instance, the user's name and password.

* If you're using certificates for authentication instead:

  * The path to the Certificate Authority (CA) bundle, if you use intermediate CAs with your root CA.
  * The path to the combined private key and certificate file, or
  * The paths to the separate private key and certificate file.

  To learn more, see:

  * For AWS OpenSearch instances, see [Tutorial: Configure a domain with the internal user database and HTTP basic authentication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac-http-auth.html) and [Creating a custom endpoint for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/customendpoint.html).
  * For local OpenSearch instances, see [Authentication backends](https://opensearch.org/docs/latest/security/authentication-backends/authc-index/), [HTTP basic authentication](https://opensearch.org/docs/latest/security/authentication-backends/basic-authc/), and [Client certificate authentication](https://opensearch.org/docs/latest/security/authentication-backends/client-auth/).

The OpenSearch connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[opensearch]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `OPENSEARCH_HOST` - The hostname and port number, defined as `<hostname>:<port-number>` and represented by `--hosts` (CLI) or `hosts` (Python).
* `OPENSEARCH_INDEX_NAME` - The name of the search index, represented by `--index-name` (CLI) or `index_name` (Python).

If you're using basic authentication to the instance:

* `OPENSEARCH_USERNAME` - The user's name, represented by `--username` (CLI) or `username` (Python).
* `OPENSEARCH_PASSWORD` - The user's password, represented by `--password` (CLI) or `password` (Python).

If you're using certificates for authentication instead:

* `OPENSEARCH_CA_CERTS` - The path to the Certificate Authority (CA) bundle, if you use intermediate CAs with your root CA. This is represented by `--ca-certs` (CLI) or `ca_certs` (Python).
* `OPENSEARCH_CLIENT_CERT` - The path to the combined private key and certificate file, or the path to just the certificate file. This is represented by `--client-cert` (CLI) or `client_cert` (Python).
* `OPENSEARCH_CLIENT_KEY` - The path to the private key file, if `OPENSEARCH_CLIENT_CERT` refers to just the certificate file. This is represented by `--client-key` (CLI) or `client_key` (Python).

Additional related settings include:

* `--use-ssl` (CLI) or `use_ssl=True` (Python) to use SSL for the connection.
* `--verify-certs` (CLI) or `verify_certs=True` (Python) to verify SSL certificates.
* `--ssl-show-warn` (CLI) or `ssl_show_warn=True` (Python) to show a warning when verifying SSL certificates is disabled.

Now call the Unstructured CLI or Python. The source connector can be any of the ones supported. This example uses the local source connector:

This example sends files to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  # Chunking and embedding are optional.

  unstructured-ingest \
    local \
      --input-path $LOCAL_FILE_INPUT_DIR \
      --strategy hi_res \
      --chunking-strategy by_title \
      --embedding-provider huggingface \
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}" \
    opensearch \
      --hosts $OPENSEARCH_HOST \
      --username $OPENSEARCH_USERNAME \
      --password $OPENSEARCH_PASSWORD \
      --index-name $OPENSEARCH_INDEX_NAME
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.elasticsearch.opensearch import (
      OpenSearchConnectionConfig,
      OpenSearchAccessConfig,
      OpensearchUploadStagerConfig,
      OpensearchUploaderConfig
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
          destination_connection_config=OpenSearchConnectionConfig(
              access_config=OpenSearchAccessConfig(
                  password=os.getenv("OPENSEARCH_PASSWORD"),
                  use_ssl=True
              ),
              hosts=[os.getenv("OPENSEARCH_HOST")],
              username=os.getenv("OPENSEARCH_USERNAME")
          ),
          stager_config=OpensearchUploadStagerConfig(
              index_name=os.getenv("OPENSEARCH_INDEX_NAME")
          ),
          uploader_config=OpensearchUploaderConfig(
              index_name=os.getenv("OPENSEARCH_INDEX_NAME")
          )
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
