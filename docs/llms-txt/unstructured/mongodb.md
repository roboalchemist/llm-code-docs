# Source: https://docs.unstructured.io/ui/sources/mongodb.md

# Source: https://docs.unstructured.io/ui/destinations/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/mongodb.md

# Source: https://docs.unstructured.io/ui/sources/mongodb.md

# Source: https://docs.unstructured.io/ui/destinations/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/mongodb.md

# Source: https://docs.unstructured.io/ui/sources/mongodb.md

# Source: https://docs.unstructured.io/ui/destinations/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/mongodb.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/mongodb.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/mongodb.md

# MongoDB

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

Send processed data from Unstructured to MongoDB.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8YBVHt5spIQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

The MongoDB requirements for a MongoDB Atlas deployment include:

<Warning>
  For MongoDB Atlas, SCRAM-SHA-1 is not supported for authentication. This means that cluster types that only
  include SCRAM-SHA-1, such as **Free**, **M0**, **Flex**, and **Serverless**, are **not** supported.
  Unstructured only supports SCRAM-SHA-256 for MongoDB Atlas, which is cryptographically stronger than SCRAM-SHA-1.

  If you try to test or use a connector that refers to a cluster type that only includes SCRAM-SHA-1, the
  operation will fail, and you will get an error message similar to the following:
  `[digital envelope routines] unsupported`.
</Warning>

* A MongoDB Atlas account. [Create an account](https://www.mongodb.com/cloud/atlas/register).

* A MongoDB Atlas cluster. [Create a cluster](https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/). Be sure to **not**
  select a cluster type that only includes SCRAM-SHA-1, such as **Free**, **M0**, **Flex**, or **Serverless**.

* The cluster must be reachable from your application environment, for example by adding IP addresses to your IP access list. [Learn more](https://www.mongodb.com/docs/atlas/setup-cluster-security/#network-and-firewall-requirements).

* The cluster must be configured to allow IP address. [Learn how](https://www.mongodb.com/docs/atlas/security/ip-access-list/#add-ip-access-list-entries).

  To get Unstructured's IP address ranges, go to
  [https://assets.p6m.u10d.net/publicitems/ip-prefixes.json](https://assets.p6m.u10d.net/publicitems/ip-prefixes.json)
  and allow all of the `ip_prefix` fields' values that are listed.

  <Note>These IP address ranges are subject to change. You can always find the latest ones in the preceding file.</Note>

* The cluster must have at least one database. [Create a database](https://www.mongodb.com/docs/compass/current/databases/#create-a-database).

* The database must have at least one user, and that user must have sufficient access to the database. [Create a database user](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/#add-database-users). [Give the user database access](https://www.mongodb.com/docs/manual/core/authorization/).

* The database must have at least one collection. [Create a collection](https://www.mongodb.com/docs/compass/current/collections/#create-a-collection).

  <Note>
    For the destination connector, Unstructured recommends that all documents in the target collection have a field
    named `record_id` with a `String` data type.
    Unstructured can use this field to do intelligent document overwrites. Without this field, duplicate documents
    might be written to the collection or, in some cases, the operation could fail altogether.
  </Note>

* The connection string for the cluster. For MongoDB Atlas, this connection string must include the protocol, username, password, host, and cluster name. For example:

  ```text  theme={null}
  mongodb+srv://<db_user>:<db_password>@<host>/?retryWrites=true&w=majority&appName=<cluster>
  ```

  To get the connection string in MongoDB Atlas, do the following:

  1. Log in to your MongoDB Atlas console.
  2. In the sidebar, under **Databases**, click **Clusters**.
  3. Click on the cluster you want to connect to.
  4. Click **Connect**.
  5. Click **Drivers**.
  6. Under **Add your connection string into your application code**, copy the connection string.
     You can then close the **Connect** dialog in MongoDB Atlas.

     Before you use this connection string, be sure to fill in any placeholders in the string, such as your MongoDB Atlas database user's password value.

  [Learn more](https://www.mongodb.com/resources/products/fundamentals/mongodb-connection-string).

To create a MongoDB destination connector, see the following examples.

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
                  type="mongodb",
                  config={
                      "database": "<database>",
                      "collection": "<collection>",
                      "uri": "<uri>"
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
      "type": "mongodb",
      "config": {
          "database": "<database>",
          "collection": "<collection>",
          "uri": "<uri>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<database>` (*required*) - The name of the database on the target MongoDB instance.
* `<collection>` (*required*) - The name of the collection within the database.
* `<uri>` (*required*) - The instance connection string.

## Learn more

* <Icon icon="blog" />  [How to go from S3 to MongoDB with no code using Unstructured](https://unstructured.io/blog/how-to-go-from-s3-to-mongodb-with-no-code-using-unstructured)
