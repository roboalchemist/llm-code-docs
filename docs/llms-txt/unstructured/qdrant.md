# Source: https://docs.unstructured.io/ui/destinations/qdrant.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/qdrant.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/qdrant.md

# Source: https://docs.unstructured.io/ui/destinations/qdrant.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/qdrant.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/qdrant.md

# Source: https://docs.unstructured.io/ui/destinations/qdrant.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/qdrant.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/qdrant.md

# Qdrant

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

Send processed data from Unstructured to Qdrant.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), only [Qdrant Cloud](https://qdrant.tech/documentation/cloud-intro/) is supported.
* For [Unstructured Ingest](/open-source/ingestion/overview), Qdrant Cloud,
  [Qdrant local](https://github.com/qdrant/qdrant), and [Qdrant client-server](https://qdrant.tech/documentation/quickstart/) are supported.

The following video shows how to set up Qdrant Cloud:

<iframe width="560" height="315" src="https://www.youtube.com/embed/730jcEAJUG8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For Qdrant local, the path to the local Qdrant installation, for example: `/qdrant/local`

* For Qdrant client-server, the Qdrant server URL, for example: `http://localhost:6333`

* For Qdrant Cloud:

  * A [Qdrant account](https://cloud.qdrant.io/login).

  * A [Qdrant cluster](https://qdrant.tech/documentation/cloud/create-cluster/).

  * The cluster's URL. To get this URL, do the following:

    1. Sign in to your Qdrant Cloud account.
    2. On the sidebar, under **Dashboard**, click **Clusters**.
    3. Click the cluster's name.
    4. Note the value of the **Endpoint** field, for example: `https://<random-guid>.<region-id>.<cloud-provider>.cloud.qdrant.io`.

  * A [Qdrant API key](https://qdrant.tech/documentation/cloud/authentication/#create-api-keys).

* The name of the target [collection](https://qdrant.tech/documentation/concepts/collections) on the Qdrant local installation,
  Qdrant server, or Qdrant Cloud cluster.

  Qdrant requires the target collection to exist before Unstructured can write to the collection.
  The following example code demonstrates the use of the [Python Qdrant Client](https://pypi.org/project/qdrant-client/) to create
  a collection on a Qdrant Cloud cluster, configuring the collection for vectors with 3072 dimensions:

  ```python Python theme={null}
  from qdrant_client import QdrantClient, models
  import os

  client = QdrantClient(
      url=os.getenv("QDRANT_URL"),
      api_key=os.getenv("QDRANT_API_KEY")
  )

  client.create_collection(
      collection_name=os.getenv("QDRANT_COLLECTION"),
      vectors_config=models.VectorParams(
          size=3072,
          distance=models.Distance.COSINE
      )
  )

  collection = client.get_collection(
                   collection_name=os.getenv("QDRANT_COLLECTION")
               )

  print(f"The collection named '{os.getenv("QDRANT_COLLECTION")}' exists and " +
        f"has a status of '{collection.status}'.")
  ```

To create a Qdrant destination connector, see the following examples.

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
                  type="qdrant-cloud",
                  config={
                      "url": "<url>",
                      "collection_name": "<collection-name>",
                      "batch_size": <batch-size>,
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
      "type": "qdrant-cloud",
      "config": {
          "url": "<url>",
          "collection_name": "<collection-name>",
          "batch_size": "<batch-size>",
          "api_key": "<api-key>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (required) - A unique name for this connector.
* `<url>` (required) - The Qdrant cluster's URL.
* `<collection-name>` (required) - The name of the target collection on the Qdrant cluster.
* `<batch-size>` - The maximum number of records to transmit at a time. The default is `50` if not otherwise specified.
* `<api-key>` (required) - The Qdrant API key.

## Learn more

* <Icon icon="blog" />  [Qdrant Integration in the Unstructured Platform](https://unstructured.io/blog/streamlining-rag-pipeline-development-qdrant-integration-in-the-unstructured-platform)
* <Icon icon="blog" />  [How to go from S3 to Qdrant with no code using Unstructured](https://unstructured.io/blog/how-to-go-from-s3-to-qdrant-with-no-code-using-unstructured)
