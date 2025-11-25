# Source: https://docs.unstructured.io/ui/sources/couchbase.md

# Source: https://docs.unstructured.io/ui/destinations/couchbase.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/couchbase.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/couchbase.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/couchbase.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/couchbase.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/couchbase.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/couchbase.md

# Couchbase

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

Send processed data from Unstructured to Couchbase.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), only Couchbase Capella clusters are supported.
* For [Unstructured Ingest](/open-source/ingestion/overview), Couchbase Capella clusters and local Couchbase server deployments are supported.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9-RIBmIdi70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

For Couchbase Capella, you will need:

* A [Couchbase Capella account](https://docs.couchbase.com/cloud/get-started/create-account.html#sign-up-free-tier).
* A [Couchbase Capella cluster](https://docs.couchbase.com/cloud/get-started/create-account.html#getting-started).
* A [bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket),
  [scope](https://docs.couchbase.com/cloud/clusters/data-service/scopes-collections.html#create-scope),
  and [collection](https://docs.couchbase.com/cloud/clusters/data-service/scopes-collections.html#create-collection)
  on the cluster.
* The cluster's [public connection string](https://docs.couchbase.com/cloud/get-started/connect.html#connect-from-sdk-cbsh-cli-or-ide).
* The [cluster access name (username) and secret (password)](https://docs.couchbase.com/cloud/clusters/manage-database-users.html#create-database-credentials).
* [Incoming IP address allowance](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) for the cluster.

  To get Unstructured's IP address ranges, go to
  [https://assets.p6m.u10d.net/publicitems/ip-prefixes.json](https://assets.p6m.u10d.net/publicitems/ip-prefixes.json)
  and allow all of the `ip_prefix` fields' values that are listed.

  <Note>These IP address ranges are subject to change. You can always find the latest ones in the preceding file.</Note>

For a local Couchbase server, you will need:

* [Installation of a local Couchbase server](https://docs.couchbase.com/server/current/getting-started/start-here.html).
* [Connection details](https://docs.couchbase.com/server/current/guides/connect.html) to the local Couchbase server.

To learn more about how to set up a Couchbase cluster and play with data, refer to this [tutorial](https://developer.couchbase.com/tutorial-quickstart-flask-python).

To create a Couchbase destination connector, see the following examples.

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
                  type="couchbase",
                  config={
                      "username": "<username>",
                      "bucket": "<bucket>",
                      "connection_string": "<connection-string>",
                      "scope": "<scope>",
                      "collection": "<collection>",
                      "password": "<password>",
                      "batch_size": <batch-size>
                  }
              )
          )
      )

      print(response.destination_connector_information)
  # ...
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
      "type": "couchbase",
      "config": {
          "username": "<username>",
          "bucket": "<bucket>",
          "connection_string": "<connection-string>",
          "scope": "<scope>",
          "collection": "<collection>",
          "password": "<password>",
          "batch_size": <batch-size>
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<username>` (*required*) - The username for the Couchbase server.
* `<bucket>` (*required*) - The name of the bucket in the Couchbase server.
* `<connection-string>` (*required*) - The connection string for the Couchbase server.
* `<scope>` - The name of the scope in the bucket. The default is `_default` if not otherwise specified.
* `<collection>` - The name of the collection in the scope. The default is `_default` if not otherwise specified.
* `<password>` (*required*) - The password for the Couchbase server.
* `<batch-size>` - The maximum number of records to transmit per batch. The default is `50` if not otherwise specified.
* `<collection-id>` (source connector only) - The name of the collection field that contains the document ID. The default is `id` if not otherwise specified.

## Learn more

* <Icon icon="blog" />  [Couchbase Integration in Unstructured Platform](https://unstructured.io/blog/couchbase-integration-in-unstructured-platform)
