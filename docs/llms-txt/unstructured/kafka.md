# Source: https://docs.unstructured.io/ui/sources/kafka.md

# Source: https://docs.unstructured.io/ui/destinations/kafka.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/kafka.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/kafka.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/kafka.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/kafka.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/kafka.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/kafka.md

# Kafka

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

Send processed data from Unstructured to Kafka.

The requirements are as follows.

* A Kafka cluster in [Confluent Cloud](https://www.confluent.io/confluent-cloud).
  ([Create a cluster](https://docs.confluent.io/cloud/current/clusters/create-cluster.html#create-ak-clusters).)

  The following video shows how to set up a Kafka cluster in Confluent Cloud:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/zcKJ96J4Xvk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The [hostname and port number](https://docs.confluent.io/cloud/current/clusters/create-cluster.html#view-a-ak-cluster) of the bootstrap Kafka cluster to connect to..

* The name of the topic to read messages from or write messages to on the cluster.
  [Create a topic](https://docs.confluent.io/cloud/current/client-apps/topics/index.html#create-topics).
  [Access available topics](https://docs.confluent.io/cloud/current/client-apps/topics/index.html#create-topics).

* For authentication, an [API key and secret](https://docs.confluent.io/cloud/current/security/authenticate/workload-identities/service-accounts/api-keys/manage-api-keys.html#add-an-api-key).

To create a Kafka destination connector, see the following examples.

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
                  type="kafka-cloud",
                  config={
                      "bootstrap_servers": "<bootstrap-server>",
                      "port": <port>,
                      "group_id": "<group-id>",
                      "kafka_api_key": "<kafka-api-key>",
                      "secret": "<secret>",
                      "topic": "<topic>",
                      "batch_size": <batch-size>
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
      "type": "kafka-cloud",
      "config": {
          "bootstrap_server": "<bootstrap-server>",
          "port": <port>,
          "group_id": "<group-id>",
          "kafka_api_key": "<kafka-api-key>",
          "secret": "<secret>",
          "topic": "<topic>",
          "num_messages_to_consume": <num-messages-to-consume>
      },
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<bootstrap-server>` - The hostname of the bootstrap Kafka cluster to connect to.
* `<port>` - The port number of the bootstrap Kafka cluster to connect to. The default is `9092` if not otherwise specified.
* `<group-id>` - The ID of the consumer group. A consumer group is a way to allow a pool of consumers to divide the consumption of data over topics and partitions. The default is `default_group_id` if not otherwise specified.
* `<kafka-api-key>` - For authentication, the API key for access to the cluster.
* `<secret>` - For authentication, the secret for access to the cluster.
* `<topic>` - The name of the topic to read messages from or write messages to on the cluster.
* `<batch-size>` (destination connector only) - The maximum number of messages to send in a single batch. The default is `100` if not otherwise specified.
* `<num-messages-to-consume>` (source connector only) - The maximum number of messages that the consumer will try to consume. The default is `100` if not otherwise specified.

## Learn more

* <Icon icon="blog" />  [Unstructured Platform Now Integrates with Apache Kafka in Confluent Cloud](https://unstructured.io/blog/unstructured-platform-now-integrates-with-apache-kafka-in-confluent-cloud)
