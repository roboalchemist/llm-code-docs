# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/elastic-search.md

# Elasticsearch

Connect Elasticsearch to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), only Elastic Cloud instances are supported.

* For [Unstructured Ingest](/open-source/ingestion/overview), Elastic Cloud instances and self-manged Elasticsearch instances are supported.

* For Elastic Cloud, you will need an [Elastic Cloud service instance](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#hosted-elasticsearch-service).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/HEYIFC7uOus" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For self-managed Elasticsearch, you will need a [self-managed Elasticsearch instance](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#elasticsearch-deployment-options).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/9znbAkNG1Ok" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* You will need the name of the index on the instance. See [Create index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html) and [Get index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-index.html).

  The Elasticsearch index that you use must have a schema that is compatible with the schema of the documents
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
                  "type": "dense_vector",
                  "dims": 384,
                  "index": true,
                  "similarity": "cosine"
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

  * [An Introduction to Elasticsearch Mapping](https://www.elastic.co/blog/found-elasticsearch-mapping-introduction)
  * [Explicit mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/explicit-mapping.html)
  * [Dynamic field mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/dynamic-field-mapping.html)
  * [Unstructured document elements and metadata](/api-reference/partition/document-elements)

  <iframe width="560" height="315" src="https://www.youtube.com/embed/0f0tEcrvP8g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For Elastic Cloud, you will need the Elastic Cloud service instance's API key. If you are using Unstructured Ingest, you will also need the instance's Cloud ID. To get these, see your Elasticsearch Service web console.

* For self-managed Elasticsearch, you will need:

  * The self-managed instance's hostname and port number. See [Networking](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-network.html).
  * If you're using basic authentication to the self-managed instance, the user's name and password.
  * If you're using token-based authentication to the self-managed instance, the bearer token or API key for the instance. See [Token-based authentication services](https://www.elastic.co/guide/en/elasticsearch/reference/current/token-authentication-services.html) and [Create API key](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html).
  * If you're using certificate authentication to the self-managed instance, the path to the Certificate Authority (CA) file on the instance, and the certificate fingerprint. See [SSL certificate API](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-ssl.html) and [Where can I see my Certificate Fingerprint?](https://discuss.elastic.co/t/where-can-i-see-my-certificate-fingerprint/319335/3).

The Elasticsearch connector dependencies:

```bash CLI, Python theme={null}
pip install "unstructured-ingest[elasticsearch]"
```

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

The following environment variables:

* `ELASTICSEARCH_HOST` - The hostname and port number, defined as `<hostname>:<port-number>` and represented by `--hosts` (CLI) or `hosts` (Python).
* `ELASTICSEARCH_INDEX_NAME` - The name of the search index, represented by `--index-name` (CLI) or `index_name` (Python).

If you're using Elastic Cloud to connect to ElasticSearch:

* `ELASTIC_CLOUD_ID` - The instance's Cloud ID, represented by `--cloud-id` (CLI) or `cloud_id` (Python).
* `ELASTIC_CLOUD_API_KEY` - The corresponding Cloud API key value, represented by `--api-key-id` (CLI) or `api_key_id` (Python).

If you're using basic authentication to the instance:

* `ELASTICSEARCH_USERNAME` - The user's name, represented by `--username` (CLI) or `username` (Python).
* `ELASTICSEARCH_PASSWORD` - The user's password, represented by `--password` (CLI) or `password` (Python).

If you're using token-based authentication to the instance instead:

* `ELASTICSEARCH_BEARER_TOKEN` - The bearer token's value, represented by `--bearer-auth` (CLI) or `bearer_auth` (Python).
* `ELASTIC_CLOUD_API_KEY_ID` - The API key's value, represented by `--api-key` (CLI) or `api_key` (Python).

If you're using certificates:

* `ELASTICSEARCH_CA_CERTS` - The path to the Certificate Authority (CA) file, represented by `--ca-certs` (CLI) or `ca_certs` (Python).
* `ELASTICSEARCH_SSL_ASSERT_FINGERPRINT` - The certificate's fingerprint, represented by `--ssl-assert-fingerprint` or `ssl_assert_fingerprint` (Python).

Now call the Unstructured CLI or Python. The destination connector can be any of the ones supported. This example uses the local destination connector:

This example sends data to Unstructured for processing by default. To process files locally instead, see the instructions at the end of this page.

<CodeGroup>
  ```bash CLI theme={null}
  #!/usr/bin/env bash

  unstructured-ingest \
    elasticsearch \
      --metadata-exclude filename,file_directory,metadata.data_source.date_processed \
      --hosts $ELASTICSEARCH_HOST \
      --username $ELASTICSEARCH_USERNAME \
      --password $ELASTICSEARCH_PASSWORD \
      --index-name $ELASTICSEARCH_INDEX_NAME \
      --ca-certs $ELASTICSEARCH_CA_CERTS \
      --ssl-assert-fingerprint $ELASTICSEARCH_SSL_ASSERT_FINGERPRINT \
      --fields 'ethnicity, director, plot' \
      --output-dir $LOCAL_FILE_OUTPUT_DIR \
      --num-processes 2
      --partition-by-api \
      --api-key $UNSTRUCTURED_API_KEY \
      --partition-endpoint $UNSTRUCTURED_API_URL \
      --strategy hi_res
  ```

  ```python Python Ingest theme={null}
  import os

  from unstructured_ingest.pipeline.pipeline import Pipeline
  from unstructured_ingest.interfaces import ProcessorConfig

  from unstructured_ingest.processes.connectors.elasticsearch.elasticsearch import (
      ElasticsearchIndexerConfig,
      ElasticsearchDownloaderConfig,
      ElasticsearchConnectionConfig,
      ElasticsearchAccessConfig,
      ElasticsearchUploadStagerConfig,
      ElasticsearchUploaderConfig
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
          indexer_config=ElasticsearchIndexerConfig(index_name=os.getenv("ELASTICSEARCH_INDEX_NAME")),
          downloader_config=ElasticsearchDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_DOWNLOAD_DIR")),
          source_connection_config=ElasticsearchConnectionConfig(
              access_config=ElasticsearchAccessConfig(
                  password=os.getenv("ELASTICSEARCH_PASSWORD"),
                  ssl_assert_fingerprint=os.getenv("ELASTICSEARCH_SSL_ASSERT_FINGERPRINT")
              ),
              hosts=[os.getenv("ELASTICSEARCH_HOST")],
              username=os.getenv("ELASTICSEARCH_USERNAME"),
              ca_certs=os.getenv("ELASTICSEARCH_CA_CERTS")
          ),
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
          destination_connection_config=LocalConnectionConfig()
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
