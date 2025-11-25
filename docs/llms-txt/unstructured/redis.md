# Source: https://docs.unstructured.io/ui/destinations/redis.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/redis.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/redis.md

# Redis

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

Send processed data from Unstructured to Redis.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_zpzzr2VtoM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [Redis](https://redis.io) database, for example in [Redis Cloud](https://redis.io/cloud/).
* The target database's hostname and port number. [Create a database in Redis Cloud](https://redis.io/docs/latest/operate/rc/rc-quickstart/#create-an-account).
* The username and password for the target database. [Get the username and password in Redis Cloud](https://redis.io/docs/latest/operate/rc/rc-quickstart/#connect-to-a-database).
* The database number for the target database. Redis databases are typically numbered from 0 to 15, with the default database number typically being 0.

To create a Redis destination connector, see the following examples.

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
                  type="redis",
                  config={
                      "database": "<database>",
                      "ssl": <True|False>,
                      "batch_size": <batch-size>,
                      "key_prefix": "<key-prefix>",

                      # For URI authentication, include only "uri" key:
                      # "uri": "<uri>",

                      # For password authentication, include these keys instead:
                      # "host": "<host>",
                      # "port": <port>,
                      # "username": "<username>",
                      # "password": "<password>"
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
      "type": "redis",
      "config": {
          "database": <database>,
          "ssl": <true|false>,
          "batch_size": <batch-size>,
          "key_prefix": "<key-prefix>",

          # For URI authentication:
          "uri": "<uri>"
        
          # For password authentication:
          "host": "<host>",
          "port": <port>,
          "username": "<username>",
          "password": "<password>"   
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (required) - A unique name for this connector.
* `<uri>` For URI authentication, the connection URI for the target database user and password, hostname, and port number. Use the format of `redis://<username>:<password>@<hostname>:<port-number>`. If SSL encryption is enabled for the database, use `rediss://` instead of `redis://`.
* `<host>` (*required* for password authentication): The target database's hostname.
* `<port>`: For password authentication, the database's port number. The default is `6379` unless otherwise specified.
* `<username>` (*required* for password authentication): The name of the database user (not the logged in user).
* `<password>` (*required* for password authentication): The database user's password.
* `<database>`: The number (index) for the target database. The default is `0` unless otherwise specified.
* For `ssl`, `true` to enable SSL encryption for the connection. Set to `true` only if SSL is already set up and enabled for the target database. The default is `true` unless otherwise specified.
* `<key-prefix>`: A string to prepend to each element's `element_id`. This is useful for distinguishing between different data sets in the same Redis instance. The default is an empty string.
* `<batch-size>`: The maximum number of records to upload in a single batch. The default is `100` unless otherwise specified.

## Learn more

* <Icon icon="blog" />  [Redis Support in Unstructured Platform: Supercharging Your RAG Pipeline](https://unstructured.io/blog/redis-support-in-unstructured-platform-supercharging-your-rag-pipeline)
* <Icon icon="blog" />  [Getting Started with Unstructured and Redis](https://unstructured.io/blog/getting-started-with-unstructured-and-redis)
