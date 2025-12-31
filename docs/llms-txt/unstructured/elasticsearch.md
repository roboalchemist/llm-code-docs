# Source: https://docs.unstructured.io/ui/sources/elasticsearch.md

# Source: https://docs.unstructured.io/ui/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/ui/sources/elasticsearch.md

# Source: https://docs.unstructured.io/ui/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/ui/sources/elasticsearch.md

# Source: https://docs.unstructured.io/ui/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/elasticsearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/elasticsearch.md

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
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
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
