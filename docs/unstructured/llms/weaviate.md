# Source: https://docs.unstructured.io/ui/destinations/weaviate.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/weaviate.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/weaviate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

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
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
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

    If Unstructured creates a new collection and generates embeddings, you will not see an `embeddings` property in tools such as the Weaviate Cloud
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

If [auto-schema](https://docs.weaviate.io/weaviate/config-refs/collections#auto-schema) is enabled in Weaviate (which it is by default),
Weaviate can infer missing properties and add them to the collection definition at run time. However, it is a Weaviate best practice to manually define as much
of the data schema in advance as possible, since manual definition gives you the most control.

The minimum viable schema for Unstructured includes only the `element_id` and `record_id` properties. The `text` and `type` properties should also be included, but they are technically optional.
If you are using Unstructured to generate embeddings, you must

The following code example shows how to use the [weaviate-client](https://pypi.org/project/weaviate-client/) Python package to create a
collection in a Weaviate Cloud database cluster with this minimum viable schema, and to specify that Unstructured will generate the embeddings for this collection.
To connect to a locally hosted Weaviate instance instead, call [weaviate.connect\_to\_local](https://docs.weaviate.io/weaviate/connections/connect-local).
To connect to Embedded Weaviate instead, call [weaviate.connect\_to\_embedded](https://docs.weaviate.io/weaviate/connections/connect-embedded).

```python  theme={null}
import os
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes.config as wvc

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(api_key=os.getenv("WEAVIATE_API_KEY")),
)

collection = client.collections.create(
    name="MyCollection",
    properties=[
        wvc.Property(name="element_id", data_type=wvc.DataType.UUID),
        wvc.Property(name="record_id", data_type=wvc.DataType.TEXT),
        wvc.Property(name="text", data_type=wvc.DataType.TEXT),
        wvc.Property(name="type", data_type=wvc.DataType.TEXT),
    ],
    vectorizer_config=None, # Unstructured will generate the embeddings instead of Weaviate.
)

client.close()
```

For objects in the `metadata` field that Unstructured produces and that you want to store in a Weaviate collection, be sure to follow
Unstructured's `metadata` field naming convention. For example, if Unstructured produces a `metadata` field with the following
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

You could create corresponding properties in your collection's schema by using the following property names and data types:

```python  theme={null}
import os
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes.config as wvc

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(api_key=os.getenv("WEAVIATE_API_KEY")),
)

collection = client.collections.create(
    name="MyCollection",
    properties=[
        wvc.Property(name="element_id", data_type=wvc.DataType.UUID),
        wvc.Property(name="record_id", data_type=wvc.DataType.TEXT),
        wvc.Property(name="text", data_type=wvc.DataType.TEXT),
        wvc.Property(name="type", data_type=wvc.DataType.TEXT),
        wvc.Property(
            name="metadata",
            data_type=wvc.DataType.OBJECT,
            nested_properties=[
                wvc.Property(name="is_extracted", data_type=wvc.DataType.TEXT),
                wvc.Property(
                    name="coordinates",
                    data_type=wvc.DataType.OBJECT,
                    nested_properties=[
                        wvc.Property(name="points", data_type=wvc.DataType.TEXT),
                        wvc.Property(name="system", data_type=wvc.DataType.TEXT),
                        wvc.Property(name="layout_width", data_type=wvc.DataType.NUMBER),
                        wvc.Property(name="layout_height", data_type=wvc.DataType.NUMBER),
                    ],
                ),
                wvc.Property(name="filetype", data_type=wvc.DataType.TEXT),
                wvc.Property(name="languages", data_type=wvc.DataType.TEXT_ARRAY),
                wvc.Property(name="page_number", data_type=wvc.DataType.TEXT),
                wvc.Property(name="image_mime_type", data_type=wvc.DataType.TEXT),
                wvc.Property(name="filename", data_type=wvc.DataType.TEXT),
                wvc.Property(
                    name="data_source",
                    data_type=wvc.DataType.OBJECT,
                    nested_properties=[
                        wvc.Property(name="url", data_type=wvc.DataType.TEXT),
                        wvc.Property(name="record_locator", data_type=wvc.DataType.TEXT),
                    ],
                ),
                wvc.Property(
                    name="entities", 
                    data_type=wvc.DataType.OBJECT,
                    nested_properties=[
                        wvc.Property(
                            name="items", 
                            data_type=wvc.DataType.OBJECT_ARRAY,
                            nested_properties=[
                                wvc.Property(name="entity", data_type=wvc.DataType.TEXT),
                                wvc.Property(name="type", data_type=wvc.DataType.TEXT),
                            ],
                        ),
                        wvc.Property(
                            name="relationships", 
                            data_type=wvc.DataType.OBJECT_ARRAY,
                            nested_properties=[
                                wvc.Property(name="to", data_type=wvc.DataType.TEXT),
                                wvc.Property(name="from", data_type=wvc.DataType.TEXT),
                                wvc.Property(name="relationship", data_type=wvc.DataType.TEXT),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
    vectorizer_config=None, # Unstructured will generate the embeddings instead of Weaviate.
)

client.close()
```

Unstructured cannot provide a schema that is guaranteed to work in all
circumstances. This is because these schemas will vary based on your source files' types; how you
want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

See also:

* [Collection schema](https://weaviate.io/developers/weaviate/config-refs/schema)
* [Unstructured document elements and metadata](/api-reference/legacy-api/partition/document-elements)

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
