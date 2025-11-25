# Source: https://docs.unstructured.io/ui/destinations/weaviate.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/weaviate.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/weaviate.md

# Weaviate

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

Send processed data from Unstructured to Weaviate.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview): only [Weaviate Cloud](https://weaviate.io/developers/wcs) clusters are supported.
* For [Unstructured Ingest](/open-source/ingestion/overview): Weaviate Cloud clusters,
  [Weaviate installed locally](https://weaviate.io/developers/weaviate/quickstart/local),
  and [Embedded Weaviate](https://weaviate.io/developers/weaviate/installation/embedded) are supported.
* For Weaviate installed locally, you will need the name of the target collection on the local instance.
* For Embedded Weaviate, you will need the instance's connection URL and the name of the target collection on the instance.
* For Weaviate Cloud, you will need:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/FvhJDUZM078" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * A Weaviate database instance. The following information assumes that you have a Weaviate Cloud (WCD) account with a Weaviate database cluster in that account.
    [Create a WCD account](https://weaviate.io/developers/wcs/quickstart#create-a-wcd-account). [Create a database cluster](https://weaviate.io/developers/wcs/quickstart#create-a-weaviate-cluster). For other database options, [learn more](https://weaviate.io/developers/weaviate/installation).
  * The URL and API key for the database cluster. [Get the URL and API key](https://weaviate.io/developers/wcs/quickstart#explore-the-details-panel).
  * The name of the target collection in the database. [Create a collection](https://weaviate.io/developers/wcs/tools/collections-tool).

    An existing collection is not required. At runtime, the collection behavior is as follows:

    For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview):

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your Weaviate cluster. If Unstructured generates embeddings,
      the new collection's name will be `U<short-workflow-id>_<short-embedding-model-name>_<number-of-dimensions>`.
      If Unstructured does not generate embeddings, the new collection's name will be `U<short-workflow-id`.

    For [Unstructured Ingest](/open-source/ingestion/overview):

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your Weaviate cluster. The new collection's name will be `Unstructuredautocreated`.

    If Unstructured creates a new collection and generates embeddings, you will not see an embeddings property in tools such as the Weaviate Cloud
    **Collections** user interface. To view the generated embeddings, you can run a Weaviate GraphQL query such as the following. In this query, replace `<collection-name>` with
    the name of the new collection, and replace `<property-name>` with the name of each additional available property that
    you want to return results for, such as `text`, `type`, `element_id`, `record_id`, and so on. The embeddings will be
    returned in the `vector` property.

    ```text  theme={null}
    {
      Get {
        <collection-name> {
          _additional {
            vector
          }
          <property-name>
          <property-name>
        }
      }
    }
    ```

Weaviate requires an existing collection to have a data schema before you add data. At minimum, this schema must contain the `record_id` property, as follows:

```json  theme={null}
{
    "class": "Elements",
    "properties": [
        {
            "name": "record_id",
            "dataType": ["text"]
        }
    ]
}
```

Weaviate generates any additional properties based on the incoming data.

If you have specific schema requirements, you can define the schema manually.
Unstructured cannot provide a schema that is guaranteed to work for everyone in all circumstances.
This is because these schemas will vary based on
your source files' types; how you want Unstructured to partition, chunk, and generate embeddings;
any custom post-processing code that you run; and other factors.

You can adapt the following collection schema example for your own specific schema requirements:

```json  theme={null}
{
    "class": "Elements",
    "properties": [
        {
            "name": "record_id",
            "dataType": ["text"]
        },
        {
            "name": "element_id",
            "dataType": ["text"]
        },
        {
            "name": "text",
            "dataType": ["text"]
        },
        {
            "name": "embeddings",
            "dataType": ["number[]"]
        },
        {
            "name": "metadata",
            "dataType": ["object"],
            "nestedProperties": [
                {
                    "name": "parent_id",
                    "dataType": ["text"]
                },
                {
                    "name": "page_number",
                    "dataType": ["text"]
                },
                {
                    "name": "is_continuation",
                    "dataType": ["boolean"]
                },
                {
                    "name": "orig_elements",
                    "dataType": ["text"]
                },
                {
                    "name": "partitioner_type",
                    "dataType": ["text"]
                }
            ]
        }
    ]
}
```

See also :

* [Collection schema](https://weaviate.io/developers/weaviate/config-refs/schema)
* [Unstructured document elements and metadata](/api-reference/partition/document-elements)

To create a Weaviate destination connector, see the following examples.

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
                  type="weaviate-cloud",
                  config={
                      "cluster_url": "<host-url>",
                      "collection": "<class-name>",
                      "api_key": "<api-key>"
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
      "type": "weaviate",
      "config": {
          "host_url": "<host-url>",
          "class_name": "<class-name>",
          "api_key": "<api-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<host-url>` (*required*) - The URL of the Weaviate database cluster.
* `<class-name>` - The name of the target collection within the cluster. If no value is provided, see the beginning of this article
  for the behavior at run time.
* `<api-key>` (*required*) - The API key provided by Weaviate to access the cluster.
