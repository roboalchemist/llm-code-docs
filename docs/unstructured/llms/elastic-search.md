# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/elastic-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Elasticsearch

Connect Elasticsearch to your preprocessing pipeline, and use the Unstructured Ingest CLI or the Unstructured Ingest Python library to batch process all your documents and store structured outputs locally on your filesystem.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), only Elastic Cloud instances are supported.

* For [Unstructured Ingest](/open-source/ingestion/overview), Elastic Cloud instances and self-manged Elasticsearch instances are supported.

* For Elastic Cloud, you will need an [Elastic Cloud service instance](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#hosted-elasticsearch-service).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/HEYIFC7uOus" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For self-managed Elasticsearch, you will need a [self-managed Elasticsearch instance](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#elasticsearch-deployment-options).

  <iframe width="560" height="315" src="https://www.youtube.com/embed/9znbAkNG1Ok" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* You will need the name of the index on the instance.

  For the destination connector, if you need to create an index, you can use for example the following `curl` command. Replace the following placeholders:

  * Replace `<host>:<port>` with the instance's host identifier and port number.
  * Replace one of the following, and remove the other:

    * For an instance's user and password combination, replace `<username>` with your Elasticsearch or Elastic Cloud instance's user name, replace `<password>` with your password, and then remove `--user "Authorization: ApiKey <your-api-key>"`.
    * For an Elastic Cloud API key, replace `<your-api-key>` with your Elastic Cloud API key, and then remove `--user "<username>:<password>"`.
  * Replace `<index-name>` with the name of the new index on the instance.
  * Replace `<index-schema>` with the schema for the index. A schema is optional; see the explanation
    following this `curl` command for more information.

  ```bash  theme={null}
  curl --request PUT "<host>:<port>/<index-name>" \
  --user "<username>:<password>" \
  --user "Authorization: ApiKey <your-api-key>" \
  [--header "Content-Type: application/json" \
  --data '<index-schema>']
  ```

  To learn more, see [Create index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html) and [Get index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-index.html).

  For the destination connector, the index does not need to contain a schema beforehand. If Unstructured encounters an index without a schema,
  Unstructured will automatically create a compatible schema for you before inserting items into the index. Nonetheless,
  to reduce possible schema compatibility issues, Unstructured recommends that you create a schema that is compatible with Unstructured's schema.
  Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  For objects in the `metadata` field that Unstructured produces and that you want to store in an Elasticsearch or Elastic Cloud index, you must create fields in your index's schema that
  follows Unstructured's `metadata` field naming convention. For example, if Unstructured produces a `metadata` field with the following
  child objects:

  ```json  theme={null}
  "metadata": {
    "is_extracted": "true",
    "coordinates": {
      "points": [
        [
          134.20055555555555,
          241.36027777777795
        ],
        [
          134.20055555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          241.36027777777795
        ]
      ],
      "system": "PixelSpace",
      "layout_width": 1654,
      "layout_height": 2339
    },
    "filetype": "application/pdf",
    "languages": [
      "eng"
    ],
    "page_number": 1,
    "image_mime_type": "image/jpeg",
    "filename": "realestate.pdf",
    "data_source": {
      "url": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf",
      "record_locator": {
        "protocol": "file",
        "remote_file_path": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf"
      }
    },
    "entities": {
      "items": [
        {
          "entity": "HOME FOR FUTURE",
          "type": "ORGANIZATION"
        },
        {
          "entity": "221 Queen Street, Melbourne VIC 3000",
          "type": "LOCATION"
        }
      ],
      "relationships": [
        {
          "from": "HOME FOR FUTURE",
          "relationship": "based_in",
          "to": "221 Queen Street, Melbourne VIC 3000"
        }
      ]
    }
  }
  ```

  You can adapt the following index schema example for your own needs. Note that outside of `metadata`, the following fields are
  required by Unstructured whenever you create your own index schema:

  * `element_id`
  * `record_id`, which is required by Unstructured for intelligent record updates.
  * `type`, which is not required, but highly recommended.
  * `text`
  * `embeddings` if embeddings are generated; make sure to set `dims` to the same number of dimensions as the embedding model generates.

  ```json  theme={null}
  {
    "mappings": {
      "properties": {
        "element_id": {
          "type": "keyword"
        },
        "record_id": {
          "type": "text"
        },
        "text": {
          "type": "text"
        },
        "type": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "embeddings": {
          "type": "dense_vector",
          "dims": 1536,
          "index": true,
          "similarity": "cosine"
        },
        "metadata": {
          "properties": {
            "is_extracted": {
              "type": "boolean"
            },
            "coordinates-points": {
              "type": "float"
            },
            "coordinates-system": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "coordinates-layout_width": {
              "type": "long"
            },
            "coordinates-layout_height": {
              "type": "long"
            },
            "filetype": {
              "type": "keyword"
            },
            "languages": {
              "type": "keyword"
            },
            "page_number": {
              "type": "integer"
            },
            "image_mime_type": {
              "type": "keyword"
            },
            "filename": {
              "type": "keyword"
            },
            "data_source-url": {
              "type": "keyword"
            },
            "data_source-record_locator-protocol": {
              "type": "keyword"
            },
            "data_source-record_locator-remote_file_path": {
              "type": "keyword"
            },
            "entities-items": {
              "properties": {
                "entity": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "type": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            },
            "entities-relationships": {
              "properties": {
                "from": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "relationship": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "to": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
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
  * [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

  <iframe width="560" height="315" src="https://www.youtube.com/embed/0f0tEcrvP8g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For Elastic Cloud, you will need the Elastic Cloud service instance's API key. If you are using Unstructured Ingest, you will also need the instance's Cloud ID. To get these, see your Elasticsearch Service web console or [Elastic Cloud API keys](https://www.elastic.co/docs/deploy-manage/api-keys/elastic-cloud-api-keys).

  <Note>
    When generating an Elastic Cloud service instance's API key through the Elasticsearch Service web console, be sure after you click **Create API key** to select **Encoded** to get the API key's value.
    (The **Encoded** API key value is the Base64 encoding of the UTF-8 representation of the API key's ID and key value joined by a colon \[:].)
  </Note>

* For self-managed Elasticsearch, you will need:

  * The self-managed instance's hostname and port number. See [Networking](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-network.html).

  * If you're using basic authentication to the self-managed instance, the user's name and password.

  * If you're using token-based authentication to the self-managed instance, the bearer token or API key for the instance. See [Token-based authentication services](https://www.elastic.co/guide/en/elasticsearch/reference/current/token-authentication-services.html) and [Create API key](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html).

    <Note>
      When generating an API key for a self-managed Elasticsearch instance by calling [POST /\_security/api\_key](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key), be sure to use
      the `encoded` value in the response payload. (This `encoded` value is the Base64 encoding of the UTF-8 representation of the payload's `id` and `api_key` values joined by a colon \[:]). Do not use the `api_key` value by itself.
    </Note>

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
