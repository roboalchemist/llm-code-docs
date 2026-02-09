# Source: https://docs.unstructured.io/ui/sources/elasticsearch.md

# Source: https://docs.unstructured.io/ui/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/elasticsearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Elasticsearch

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a destination connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key.

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the destination connector, add it along with a
  [source connector](/api-reference/workflow/sources/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to Elasticsearch.

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

To create an Elasticsearch destination connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateDestinationRequest
  from unstructured_client.models.shared import CreateDestinationConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.destinations.create_destination(
          request=CreateDestinationRequest(
              create_destination_connector=CreateDestinationConnector(
                  name="<name>",
                  type="elasticsearch",
                  config={
                      "hosts": ["<host-url>"],
                      "es_api_key": "<es-api-key>",
                      "index_name": "<index-name>"
                  }
              )
          )
      )

      print(response.destination_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/destinations" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "elasticsearch",
      "config": {
          "hosts": ["<host-url>"],
          "es_api_key": "<es-api-key>",
          "index_name": "<index-name>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `hosts` is a *required* array, with `<host-url>` specifying the URL of the Elastic Cloud instance to access, for example: `["https://<random-number>.<region>.<cloud-provider>.cloud.es.io"]`.
* `<es-api-key>` (*required*) - The Elastic Cloud API key for the target cluster.
* `<index-name>` (*required*) - The name of the target index in the cluster.

## Learn more

* <Icon icon="blog" />  [Finding Needles in a Haystack: PII Detection at Scale with Unstructured, Box, and Elasticsearch](https://unstructured.io/blog/finding-needles-in-a-haystack-pii-detection-at-scale-with-unstructured-box-and-elasticsearch)
