# Source: https://docs.unstructured.io/ui/destinations/milvus.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/milvus.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/milvus.md

# Source: https://docs.unstructured.io/ui/destinations/milvus.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/milvus.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/milvus.md

# Source: https://docs.unstructured.io/ui/destinations/milvus.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/milvus.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/milvus.md

# Milvus

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

Send processed data from Unstructured to Milvus.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), only Milvus cloud-based instances (such as Milvus on IBM watsonx.data, or Zilliz Cloud) are supported.

* For [Unstructured Ingest](/open-source/ingestion/overview), Milvus local and cloud-based instances are supported.

* For Milvus on IBM watsonx.data, you will need:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/hLCwoe2fCnc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * An [IBM Cloud account](https://cloud.ibm.com/registration).

  * An IBM watsonx.data [Lite plan](https://cloud.ibm.com/docs/watsonxdata?topic=watsonxdata-tutorial_prov_lite_1)
    or [Enterprise plan](https://cloud.ibm.com/docs/watsonxdata?topic=watsonxdata-getting-started_1) within your IBM Cloud account.

    * If you are provisoning a Lite plan, be sure to choose the **Generative AI** use case when prompted, as this is the only use case offered that includes Milvus.

  * A [Milvus service instance in IBM watsonx.data](https://cloud.ibm.com/docs/watsonxdata?topic=watsonxdata-adding-milvus-service).

    * If you are creating a Milvus service instance within a watsonx.data Lite plan, when you are prompted to choose a Milvus instance size, you can only select **Lite**. Because the Lite
      Milvus instance size is recommended only for 384 dimensions, you should also use an embedding model that uses 384 dimensions only.
    * If you are creating a Milvus service instance within a watsonx.data Enterprise plan, you can choose any available Milvus instance size. However, all Milvus instance sizes other than
      **Custom** are recommended only for 384 dimensions, which means you should use an embedding model that uses 384 dimensions only.
      The **Custom** Milvus instance size is recommended for any number of dimensions.

  * The URI of the instance, which takes the format of `https://`, followed by instance's **GRPC host**, followed by a colon and the **GRPC port**.
    This takes the format of `https://<host>:<port>`. To get this informatation, do the following:

    a. Sign in to your IBM Cloud account.<br />
    b. On the sidebar, click the **Resource list** icon. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the title bar.<br />
    c. Expand **Databases**, and then click the name of the target **watsonx.data** plan.<br />
    d. Click **Open web console**.<br />
    e. On the sidebar, click **Infrastructure manager**. If the sidebar is not visible, click the **Global navigation** icon to the far left of the title bar.<br />
    f. Click the target Milvus service instance.<br />
    g. On the **Details** tab, under **Type**, click **View connect details**.<br />
    h. Under **Service details**, expand **GRPC**, and note the value of **GRPC host** and **GRPC port**.<br />

  * The name of the [database](https://milvus.io/docs/manage_databases.md) in the instance.

  * The name of the [collection](https://milvus.io/docs/manage-collections.md) in the database. Note the collection requirements at the end of this section.

  * The username and password to access the instance.

    * The username for Milvus on IBM watsonx.data is always `ibmlhapikey`.
    * The password for Milvus on IBM watsonx.data is in the form of an IBM Cloud user API key. To create an IBM Cloud user API key:

      a. Sign in to your IBM Cloud account.<br />
      b. In the title bar, click **Manage** and then, under **Security and access**, click **Access (IAM)**.<br />
      c. On the sidebar, under **Manage identities**, click **API keys**. If the sidebar is not visible, click the **Navigation Menu** icon to the far left of the title bar.<br />
      d. Click **Create**.<br />
      e. Enter some **Name** for the API key.<br />
      f. Optionally, enter some **Description** for the API key.<br />
      g. For **Leaked action**, leave **Disable the leaked key** selected.<br />
      h. For **Session management**, leave **No** selected.<br />
      i. Click **Create**.<br />
      j. Click **Download** (or **Copy**), and then download the API key to a secure location (or paste the copied API key into a secure location). You won't be able to access this API key from this dialog again. If you lose this API key, you can create a new one (and you should then delete the old one).<br />

* For Zilliz Cloud, you will need:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/vwWudGvBEKQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  * A [Zilliz Cloud account](https://cloud.zilliz.com/signup).

  * A [Zilliz Cloud cluster](https://docs.zilliz.com/docs/create-cluster).

  * The URI of the cluster, also known as the cluster's *public endpoint*, which takes a format such as
    `https://<cluster-id>.<cluster-type>.<cloud-provider>-<region>.cloud.zilliz.com`. To get this public endpoint value, do the following:

    1. After you sign in to your Zilliz Cloud account, on the sidebar, in the list of available projects, select the project that contains the cluster.
    2. On the sidebar, click **Clusters**.
    3. Click the tile for the cluster.
    4. On the **Cluster Details** tab, on the **Connect** subtab, copy the **Public Endpoint** value.

  * The username and password to access the cluster, as follows:

    1. After you sign in to your Zilliz Cloud account, on the sidebar, in the list of available projects, select the project that contains the cluster.
    2. On the sidebar, click **Clusters**.
    3. Click the tile for the cluster.
    4. On the **Users** tab, copy the name of the user.
    5. Next to the user's name, under **Actions**, click the ellipsis (three dots) icon, and then click **Reset Password**.
    6. Enter a new password for the user, and then click **Confirm**. Copy this new password.

  * The name of the [database](https://docs.zilliz.com/docs/database#create-database) in the instance.

  * The name of the [collection](https://docs.zilliz.com/docs/manage-collections-console#create-collection) in the database.

    The collection must have a defined schema before Unstructured can write to the collection. The minimum viable
    schema for Unstructured contains only the fields `element_id`, `embeddings`, `record_id`, and `text`, as follows:

    | Field Name                       | Field Type        | Max Length | Dimension |
    | -------------------------------- | ----------------- | ---------- | --------- |
    | `element_id` (primary key field) | **VARCHAR**       | `200`      | --        |
    | `embeddings` (vector field)      | **FLOAT\_VECTOR** | --         | `384`     |
    | `record_id`                      | **VARCHAR**       | `200`      | --        |
    | `text`                           | **VARCHAR**       | `65536`    | --        |

    In the **Create Index** area for the collection, next to **Vector Fields**, click **Edit Index**. Make sure that for the
    `embeddings` field, the **Field Type** is set to **FLOAT\_VECTOR** and the **Metric Type** is set to **Cosine**.

    <Warning>
      The number of dimensions for the `embeddings` field must match the number of dimensions for the embedding model that you plan to use.
    </Warning>

* For Milvus local, you will need:

  * A [Milvus instance](https://milvus.io/docs/install-overview.md).
  * The [URI](https://milvus.io/api-reference/pymilvus/v2.4.x/MilvusClient/Client/MilvusClient.md) of the instance.
  * The name of the [database](https://milvus.io/docs/manage_databases.md) in the instance.
  * The name of the [collection](https://milvus.io/docs/manage-collections.md) in the database.
    Note the collection requirements at the end of this section.
  * The [username and password, or token](https://milvus.io/docs/authenticate.md) to access the instance.

All Milvus instances require the target collection to have a defined schema before Unstructured can write to the collection. The minimum viable
schema for Unstructured contains only the fields `element_id`, `embeddings`, `record_id`, and `text`, as follows.

This example code demonstrates the use of the
[Python SDK for Milvus](https://pypi.org/project/pymilvus/) to create a collection with this schema,
targeting Milvus on IBM watsonx.data. For the `MilvusClient` arguments to connect to other types of Milvus deployments, see your Milvus provider's documentation:

```python Python theme={null}
import os

from pymilvus import (
    MilvusClient,
    FieldSchema,
    DataType,
    CollectionSchema
)

DATABASE_NAME   = "default"
COLLECTION_NAME = "my_collection"

client = MilvusClient(
    uri="https://" +
        os.getenv("MILVUS_USER") + 
        ":" + 
        os.getenv("MILVUS_PASSWORD") + 
        "@" + 
        os.getenv("MILVUS_GRPC_HOST") + 
        ":" + 
        os.getenv("MILVUS_GRPC_PORT"),
    db_name=DATABASE_NAME
)

primary_key_field = FieldSchema(
    name="element_id",
    dtype=DataType.VARCHAR,
    is_primary=True,
    max_length=200
)

# IMPORTANT: The number of dimensions for the "embeddings" field
# must match the number of dimensions for the embedding model 
# that you plan to use.
embeddings_field = FieldSchema(
    name="embeddings",
    dtype=DataType.FLOAT_VECTOR,
    dim=384
)

record_id_field = FieldSchema(
    name="record_id",
    dtype=DataType.VARCHAR,
    max_length=200
)

text_field = FieldSchema(
    name="text",
    dtype=DataType.VARCHAR,
    max_length=65535
)

schema = CollectionSchema(
    fields=[
        primary_key_field, 
        embeddings_field,
        record_id_field, 
        text_field
    ]
)

client.create_collection(
    collection_name=COLLECTION_NAME",
    schema=schema,
    using=DATABASE_NAME
)

index_params = client.prepare_index_params()

index_params.add_index(
    field_name="embeddings",
    metric_type="COSINE",
    index_type="IVF_FLAT",
    params={"nlist": 1024}
)

client.create_index(
    collection_name=COLLECTION_NAME,
    index_params=index_params
)

client.load_collection(
    collection_name=COLLECTION_NAME
)
```

Other approaches, such as [creating collections instantly](https://milvus.io/docs/create-collection-instantly.md) or
[setting nullable and default fields](https://milvus.io/docs/nullable-and-default.md), have not
been fully evaluated by Unstructured and might produce unexpected results.

Unstructured cannot provide a schema that is guaranteed to work in all
circumstances. This is because these schemas will vary based on your source files' types; how you
want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

To create a Milvus destination connector, see the following examples.

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
                  type="milvus",
                  config={
                      "user": "<user>",
                      "uri": "<uri>",
                      "db_name": "<db-name>",
                      "password": "<password>",
                      "collection_name": "<collection-name>"
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
      "type": "milvus",
      "config": {
          "user": "<user>",
          "uri": "<uri>",
          "db_name": "<db-name>",
          "password": "<password>",
          "collection_name": "<collection-name>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<user>` (*required*) - The username to access the Milvus instance.
* `<uri>` (*required*) - The URI of the instance, for example: `https://12345.serverless.gcp-us-west1.cloud.zilliz.com.`
* `<db-name>` (*required*) - The name of the database in the instance.
* `<password>` (*required*) - The password corresponding to the username to access the instance.
* `<collection-name>` (*required*) - The name of the collection in the database.
