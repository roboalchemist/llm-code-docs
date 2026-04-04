# Source: https://docs.confluent.io/cloud/current/get-started/index.md

<a id="cloud-quickstart"></a>

# Quick Start for Confluent Cloud

Confluent Cloud is a fully-managed, cloud-native data streaming platform powered by
Apache KafkaÂ®. This quick start guide will help you begin your data streaming journey
by showing you how to create a [cluster](../_glossary.md#term-Kafka-cluster), add a [topic](../_glossary.md#term-topic),
and produce data.

Considerations
: - This quick start gets you up and running with Confluent Cloud using a [Basic Kafka cluster](../clusters/cluster-types.md#basic-cluster).
  - The first section shows how to use Confluent Cloud to create topics, and [produce](../_glossary.md#term-producer) and [consume](../_glossary.md#term-consumer) data to and from the cluster.
  - The second section walks you through how to use Confluent Cloud for Apache FlinkÂ® to run queries on the data using SQL syntax.
  - The quick start workflows assume you already have a working Confluent Cloud environment, which includes a Stream Governance package. To learn more about Stream Governance packages, features, and environment setup workflows, see [Manage Stream Governance Packages in Confluent Cloud](../stream-governance/packages.md#stream-gov-packages).
  - Confluent Cloud has a web interface called the Cloud Console, a local command line interface, and REST APIs. Use the Cloud Console to manage cluster resources, settings, and billing. Use the Confluent CLI and REST APIs to create and manage topics and more.

Prerequisites
: - Access to [Confluent Cloud](https://www.confluent.io/confluent-cloud/).
    To get started for free, see [Deploy Free Clusters on Confluent Cloud](free-trial.md#free-trial).
  - Internet connectivity
  - Stream Governance package

<a id="cloud-qs-section1"></a>

## Section 1: Create a cluster and add a topic

Follow the steps in this section to set up a Kafka cluster on Confluent Cloud and
produce data to Kafka topics on the cluster.

<a id="cloud-create-kafka-cluster"></a>

### Step 1: Create a Kafka cluster in Confluent Cloud

In this step, you create and launch a basic Kafka cluster inside your default
environment.

### Cloud Console

1. Sign in to Confluent Cloud at [https://confluent.cloud](https://confluent.cloud).
2. Click **Add cluster**.
3. On the **Create cluster** page, for the **Basic** cluster, select **Begin configuration**.
   ![Screenshot of Confluent Cloud showing the Create cluster page](images/cloud-create-cluster.png)

   This example creates a **Basic** Kafka cluster, which supports single zone
   availability. For information about other cluster types,
   see [Kafka Cluster Types in Confluent Cloud](../clusters/cluster-types.md#cloud-cluster-types).
4. On the **Region/zones** page, choose a
   cloud provider, region, and select single availability zone.
   ![Screenshot of Confluent Cloud showing the Create Cluster workflow](images/cloud-pay-launch1.png)
5. Select **Continue**.

   #### NOTE
   If you havenât set up a payment method, you see the **Set payment page**. Enter
   payment method and select **Review**.
6. Specify a cluster name, review the configuration and cost information, and then select
   **Launch cluster**.
   ![Screenshot of Confluent Cloud showing the Create Cluster workflow](images/cloud-pay-launch-review.png)

Depending on the chosen cloud provider and other settings, it may take a few
minutes to provision your cluster, but after the cluster has provisioned,
the **Cluster Overview** page displays.

![Screenshot of Confluent Cloud showing Cluster Overview page](images/cloud-pay-launch-new-cluster.png)

Now you can get started configuring apps and data on your new cluster.

### Confluent CLI

1. Log in or sign up to Confluent Cloud:

   Log in:
   ```none
   confluent login
   ```
2. Create a Kafka cluster:
   ```none
   confluent kafka cluster create <name> [flags]
   ```

   For example:
   ```none
   confluent kafka cluster create quickstart_cluster --cloud "aws" --region "us-west-2"
   ```

### Confluent Cloud APIs

Create a Kafka cluster.

Request:

```bash
POST /cmk/v2/clusters
Host: api.confluent.cloud

{
   "spec": {
      "display_name": "quickstart_cluster",
      "availability": "SINGLE_ZONE",
      "cloud": "{provider}",
      "region": "{region}",
      "config": {
         "kind": "Basic"
      },
      "environment": {
         "id": "env-a12b34"
      }
   }
}
```

Response:

```bash
{
   "api_version": "cmk/v2",
   "id": "lkc-000000",
   "kind": "Cluster",
   "metadata": {
      "created_at": "2022-11-21T22:50:07.496522Z",
      "resource_name": "crn://confluent.cloud/organization=example1-org1-1111-2222-33aabbcc444dd55/environment=env-00000/cloud-cluster=lkc-000000/kafka=lkc-000000",
      "self": "https://api.confluent.cloud/cmk/v2/clusters/lkc-000000",
      "updated_at": "2022-11-21T22:50:07.497443Z"
   },
   "spec": {
      "api_endpoint": "https://pkac-{00000}.{region}.{provider}.confluent.cloud",
      "availability": "SINGLE_ZONE",
      "cloud": "{provider}",
      "config": {
            "kind": "Basic"
      },
      "display_name": "quickstart_cluster",
      "environment": {
            "api_version": "org/v2",
            "id": "env-a12b34",
            "kind": "Environment",
            "related": "https://api.confluent.cloud/org/v2/environments/env-a12b34",
            "resource_name": "crn://confluent.cloud/organization=example1-org1-1111-2222-33aabbcc444dd55/environment=env-a12b34}"
      ,
      "http_endpoint": "https://pkc-{00000}.{region}.{provider}.confluent.cloud:443",
      "kafka_bootstrap_endpoint": "SASL_SSL://pkc-{00000}.{region}.{provider}.confluent.cloud:9092",
      "region": "{region}"
   },
   "status": {
      "phase": "PROVISIONING"
   }
}
```

<a id="cloud-quick-create-topic"></a>

### Step 2: Create a Kafka topic

In this step, you create a `users` Kafka topic by using the Cloud Console.
A *topic* is a unit of organization for a cluster, and is essentially an
append-only log. For more information about topics, see
[What is Apache Kafka](https://developer.confluent.io/what-is-apache-kafka/).

### Cloud Console

1. From the navigation menu, click **Topics**, and then
   click **Create topic**.
   ![Create topic page Confluent Cloud](images/cloud-create-topic.png)
2. In the **Topic name** field, type âusersâ and then select **Create with defaults**.
   ![Topic page in Confluent Cloud showing a newly created topic](images/cloud-create-topic-2.png)

The `users` topic is created on the Kafka cluster and is available for use
by producers and consumers.

The success message may prompt you to take an action,
but you should continue with [Step 3: Create a sample producer](#cloud-create-producer).

### Confluent CLI

Create a topic:

```none
confluent kafka topic create <name> [flags]
```

For example:

```none
confluent kafka topic create users --cluster lkc-000000
```

### Confluent Cloud APIs

Create a topic:

Request:

```bash
POST /kafka/v3/clusters/{cluster_id}/topics
Host: pkc-{00000}.{region}.{provider}.confluent.cloud

{
   "topic_name": "users",
   "partitions_count": 6,
   "replication_factor": 3,
   "configs": [{
         "name": "cleanup.policy",
         "value": "delete"
      },
      {
         "name": "compression.type",
         "value": "gzip"
      }
   ]
}
```

Response:

```bash
{
   "kind": "KafkaTopic",
   "metadata": {
      "self": "https://pkc-{00000}.{region}.{provider}.confluent.cloud/kafka/v3/clusters/quickstart/topics/users",
      "resource_name": "crn:///kafka=quickstart/topic=users"
   },
   "cluster_id": "quickstart",
   "topic_name": "users",
   "is_internal": false,
   "replication_factor": 3,
   "partitions_count": 1,
   "partitions": {
      "related": "https://pkc-{00000}.{region}.{provider}.confluent.cloud/kafka/v3/clusters/cluster-1/topics/topic-X/partitions"
   },
   "configs": {
      "related": "https://pkc-{00000}.{region}.{provider}.confluent.cloud/kafka/v3/clusters/cluster-1/topics/topic-X/configs"
   },
   "partition_reassignments": {
      "related": "https://pkc-{00000}.{region}.{provider}.confluent.cloud/kafka/v3/clusters/cluster-1/topics/topic-X/partitions/-/reassignments"
   }
}
```

<a id="cloud-create-producer"></a>

### Step 3: Create a sample producer

You can produce example data to your Kafka cluster by using the
hosted [Datagen Source Connector for Confluent Cloud](../connectors/cc-datagen-source.md#cc-datagen-source).

### Cloud Console

1. From the navigation menu, select **Connectors**.

   To open Confluent Cloud at **Connectors**: [https://confluent.cloud/go/connectors](https://confluent.cloud/go/connectors).
2. In the **Search** box, type âdatagenâ.
3. From the search results, select the **Datagen Source** connector.
   ![Screenshot that shows searching for the datagen connector](images/cloud-search-datagen.png)
4. On the **Launch Sample Data** dialog, select the **Users** template, and click **Additional configuration**.
5. On the **Topic selection** dialog, select the âusersâ topic you created in
   the previous section and click **Continue**.
6. In the **Kafka credentials** dialog, select **My account**, and
   click **Generate API key & download**, then click **Continue**.

   This creates an API key and secret that allows the connector to access your cluster, and downloads the key
   and secret to your computer. The key and secret are required for the connector and also for the Confluent CLI and ksqlDB CLI to access your cluster.

   #### NOTE
   An API key and associated secret apply to the active Kafka cluster. If
   you add a new cluster, you must create a new API key for producers and
   consumers on the new Kafka cluster. For more information, see
   [Use API Keys to Authenticate to Confluent Cloud](../security/authenticate/workload-identities/service-accounts/api-keys/overview.md#cloud-api-keys).
7. On the **Configuration** page, select **JSON_SR** for the output record value
   format, **Users** for the template, and click **Continue**.
8. For **Connector sizing**, leave the slider at the default of **1** task and click **Continue**
9. On the **Review and launch** page, select the text in the **Connector name** box and
   replace it with âDatagenSourceConnector_usersâ.
10. Click **Continue** to start the connector.

    The status of your new connector should read **Provisioning**, which lasts for a few seconds.
    When the status changes to **Running**, your connector is producing data to the `users` topic.
    ![Screenshot of Confluent Cloud showing a running Datagen Source Connector](images/cloud-connectors-page.png)

### Confluent CLI

1. Create an API key:
   ```none
   confluent api-key create --resource <cluster_id> [flags]
   ```

   For example:
   ```none
   confluent api-key create --resource lkc-000000
   ```

   Example output:
   ```none
   +---------+------------------------------------------------------------------+
   | API Key | EXAMPLEERFBSSSLK                                                 |
   | Secret  | EXAMPLEEkYXOtOmn+En8397gCaeX05j0szygokwLRk1ypVby1UsgZpZLX7gJGR4G |
   +---------+------------------------------------------------------------------+
   ```

   It may take a couple of minutes for the API key to be ready. Save the API key and secret.
   The secret is not retrievable later.
2. Create a JSON file named `quick-start.json` and copy and paste the following configuration properties into the file:
   ```none
   {
      "name" : "DatagenSourceConnector_users",
      "connector.class": "DatagenSource",
      "kafka.auth.mode": "KAFKA_API_KEY",
      "kafka.api.key": "[Add your cluster API key here]",
      "kafka.api.secret" : "[Add your cluster API secret here]",
      "kafka.topic" : "users",
      "output.data.format" : "JSON_SR",
      "quickstart" : "USERS",
      "tasks.max" : "1"
   }
   ```
3. Replace `[Add your cluster API key here]` and `[Add your cluster API secret here]` with your API key and secret.
4. Create the sample producer:
   ```none
   confluent connect cluster create --config-file <file-name>.json --cluster <cluster_id>
   ```

   For example:
   ```none
   confluent connect cluster create --config-file quick-start.json --cluster lkc-000000
   ```

### Confluent Cloud APIs

Create a producer.

To create a producer with the Confluent Cloud APIs, you need two API keys:

- Cloud API key added to the header for authorization
- Kafka cluster API key added to the body for access to the cluster

Use the Confluent CLI or the Cloud Console to generate an API key for the Kafka cluster. For
more information, see [Authentication](/cloud/current/api.html#section/Authentication) in the API reference.

Request:

```bash
POST /connect/v1/environments/{environment_id}/clusters/{cluster_id}/connectors
Host: api.confluent.cloud

{
   "name": "DatagenSourceConnector_users",
   "config": {
      "name": "DatagenSourceConnector_users"
      "connector.class": "DatagenSource",
      "kafka.auth.mode": "KAFKA_API_KEY",
      "kafka.api.key": "[Add your cluster API key here]",
      "kafka.api.secret" : "[Add your cluster API secret here]",
      "kafka.topic" : "users",
      "output.data.format" : "JSON_SR",
      "quickstart" : "USERS",
      "tasks.max" : "1"
   }
}
```

Replace `[Add your cluster API key here]` and `[Add your cluster API secret here]` with your cluster API key and secret.

Response:

```bash
{
   "name": "DatagenSourceConnector_users",
   "type": "source",
   "config": {
      "cloud.environment": "prod",
      "cloud.provider": "{provider}",
      "connector.class": "DatagenSource",
      "kafka.api.key": "[Your cluster API key]",
      "kafka.api.secret": "[Your cluster API secret]",
      "kafka.auth.mode": "KAFKA_API_KEY",
      "kafka.endpoint": "SASL_SSL://pkc-{00000}.{region}.{provider}.confluent.cloud:9092",
      "kafka.region": "{region}",
      "kafka.topic": "users1",
      "name": "DatagenSourceConnector_users",
      "output.data.format": "JSON_SR",
      "quickstart": "USERS",
      "tasks.max": "1"
   },
   "tasks": []
}
```

### Step 4: View messages

Your new `users` topic is now receiving messages. Use Confluent Cloud Console to see
the data.

1. From the navigation menu, select **Topics** to show the list of topics in your
   cluster.
   ![Screenshot of Confluent Cloud showing the Topics page](images/cloud-topics-page.png)
2. Select the **users** topic.
3. In the **users** topic detail page, select the
   **Messages** tab to view the messages being produced to the topic.
   ![Confluent Cloud showing the Messages page](images/cloud-topic-message-search.png)

<a id="cloud-inspect-stream"></a>

### Step 5: Inspect the data stream

Use Stream Lineage to track data movement through your cluster.

1. Click **Stream Lineage** in the navigation menu.
2. Click the node labeled **DatagenSourceConnector_users**, which is the
   connector that you created in Step 3. The details overview shows
   graphs for total production and other data.
   ![Screenshot of Confluent Cloud showing details for a source connector](images/cloud-data-flow-2.png)
3. Dismiss this view and select the topic labeled **users**. Click the **Overview** tab to show graphs for total throughput and other data.
   Click the other tabs to view the schema associated with the topic (if there is one defined), along with metadata and messages.
   ![Screenshot of Confluent Cloud showing details for a topic](images/cloud-data-flow-4.png)
4. Click the arrow on the left border of the canvas to re-open the left-side navigation menu.

### Step 6: Delete resources (optional)

Skip this step if you plan to move on to [Section 2: Query streaming data with Flink SQL](#cloud-qs-section2) and learn
how to use Flink SQL statements to query your data.

If you donât plan to complete [Section 2](#cloud-qs-section2) and
youâre ready to quit the Quick Start, delete the resources you created
to avoid unexpected charges to your account.

### Cloud Console

- Delete the connector:
  1. From the navigation menu, select **Connectors**.
  2. Click **DatagenSourceConnector_users** and choose the **Settings** tab.
  3. Click **Delete connector**, enter the connector name (`DatagenSourceConnector_users`), and click
     **Confirm**.
- Delete the topic:
  1. From the navigation menu, click **Topics**, select the **users** topic, and then choose the **Configuration** tab.
  2. Click **Delete topic**, enter the topic name (`users`), and select **Continue**.
- Delete the cluster:
  1. From the navigation menu, select **Cluster Settings**.
  2. Click **Delete cluster**, enter the cluster name, and click **Continue**.

### Confluent CLI

1. Delete the connector:
   ```none
   confluent connect cluster delete <connector-id> [flags]
   ```

   For example:
   ```none
   confluent connect cluster delete lcc-aa1234 --cluster lkc-000000
   ```
2. Delete the topic:
   ```none
   confluent kafka topic delete <topic name> [flags]
   ```

   For example:
   ```none
   confluent kafka topic delete users --cluster lkc-000000
   ```
3. Delete the cluster.
   ```none
   confluent kafka cluster delete <id> [flags]
   ```

   For example (text you must enter is highlighted):
   ```none
   confluent kafka cluster delete lkc-123exa

   Are you sure you want to delete Kafka cluster "lkc-123exa"?
   To confirm, type "my-new-name". To cancel, press Ctrl-C:

   my-new-name

   Deleted Kafka cluster "lkc-123exa".
   ```

### Confluent Cloud APIs

Delete a producer.

Request:

```bash
DELETE /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}
Host: api.confluent.cloud
```

Delete a topic.

Request:

```bash
DELETE /kafka/v3/clusters/{kafka_cluster_id}/topics/{topic_name}
Host: pkc-{0000}.{region}.{provider}.confluent.cloud
```

Delete a cluster.

Request:

```bash
DELETE /cmk/v2/clusters/{id}?environment={environment_id}
Host: api.confluent.cloud
```

<a id="cloud-qs-section2"></a>

## Section 2: Query streaming data with Flink SQL

In [Section 1](#cloud-qs-section1), you installed a Datagen connector
to produce data to the `users` topic in your Confluent Cloud cluster.

In this section, you create a Flink workspace and write queries against the
`users` topic and other streaming data.

### Step 1: Create a Flink workspace

To write queries against streaming data in tables, create a new Flink workspace.

1. Navigate to the [Environments](https://confluent.cloud/environments) page,
   and in the navigation menu, click **Stream processing**.
2. In the dropdown, select the environment where you created the `users`
   topic and the Datagen Source connector.
3. Click **Create workspace**.

   A new workspace opens with an example query in the code editor, or *cell*.
   ![Flink workspace in Confluent Cloud](images/cloud-flink-workspace.png)

   Under the hood, Confluent Cloud for Apache Flink is creating a [compute pool](../flink/concepts/compute-pools.md#flink-sql-compute-pools),
   which represents the compute resources that are used to run your
   [SQL statements](../flink/concepts/statements.md#flink-sql-statements).

   It may take a minute or two for the compute pool to be provisioned. The
   status is displayed in the upper-right section of the workspace.

### Step 2: Run Flink SQL statements

When the compute pool status changes from **Provisioning** to **Running**,
itâs ready to run queries.

1. Click **Run** to submit the example query.

   The example statement is submitted, and information about the statement is
   displayed, including its status and a unique identifier. Click the
   **Statement name** link to open the statement details view, which displays
   the statement status and other information. Click **X** to dismiss the
   details view.

   After an initialization period, the query results display beneath the cell.

   Your output should resemble:
   ```none
   EXPR$0
   0
   1
   2
   ```
2. Clear the previous query from the cell and run the following query to
   inspect the `users` stream.

   Confluent Cloud for Apache Flink registers tables automatically on your Kafka topics, and your query
   runs against the `users` table with the streaming data from the underlying
   topic.
   ```sql
   SELECT * FROM users;
   ```

   Your output should resemble:
   ```none
   key             registertime  userid regionid gender
   x'557365725f34' 1502088104187 User_4 Region_1 MALE
   x'557365725f32' 1500243991207 User_2 Region_9 FEMALE
   x'557365725f32' 1497969328414 User_2 Region_9 OTHER
   ...
   ```
3. Click **Stop** to end the query.

   Data continues to flow from the Datagen connector into the `users` table
   even though the SELECT query is stopped.

### Step 3: Mask a field

With a Flink compute pool running, you can run sophisticated SQL queries on your
streaming data.

In this step, you run a Flink SQL statement to hide personal information in
the `users` stream and publish the scrubbed data to a new Kafka topic, named
`users_mask`.

1. Run the following statement to create a new Flink table based on the
   `users` table.
   ```sql
   CREATE TABLE users_mask LIKE users;
   ```
2. When the status of the previous statement is **Completed**, run the
   following statement to inspect the schema of the `users_mask` table.
   ```sql
   DESCRIBE users_mask;
   ```

   Your output should resemble:
   ```none
   +--------------+-----------+----------+------------+
   | Column Name  | Data Type | Nullable |   Extras   |
   +--------------+-----------+----------+------------+
   | key          | BYTES     | NULL     | BUCKET KEY |
   | registertime | BIGINT    | NULL     |            |
   | userid       | STRING    | NULL     |            |
   | regionid     | STRING    | NULL     |            |
   | gender       | STRING    | NULL     |            |
   +--------------+-----------+----------+------------+
   ```
3. Run the following statement to start a persistent query that uses the Flink
   [REGEXP_REPLACE](../flink/reference/functions/string-functions.md#flink-sql-regexp-replace-function) function to mask the value of
   the `gender` field and stream the results to the `users_mask` table.
   ```sql
   INSERT INTO users_mask SELECT
     `key`,
     registertime,
     userid,
     regionid,
     REGEXP_REPLACE(gender, '(\w)', '*') as gender
   FROM users;
   ```

   The [INSERT INTO FROM SELECT](../flink/reference/queries/insert-into-from-select.md#flink-sql-insert-into-from-select-statement)
   statement runs continuously until you stop it manually.

1. Click ![add-new-cell](flink/images/flink-add-code-editor.png) to create a new cell, and run the following statement
   to inspect the rows in the `users_mask` table.
   ```sql
   SELECT * FROM users_mask;
   ```

   Your output should resemble:
   ```none
   key             registertime  userid regionid gender
   x'557365725f34' 1488737391835 User_4 Region_5 *****
   x'557365725f34' 1499070045309 User_4 Region_5 *****
   x'557365725f32' 1505447077187 User_2 Region_7 *****
   x'557365725f34' 1505592707164 User_4 Region_2 *****
   ...
   ```
2. Click **Stop** to end the SELECT statement.

   The INSERT INTO statement that you started previously continues streaming
   data into the `users_mask` topic.

### Step 4: View the Stream Lineage

Your Flink SQL statements are resources in Confluent Cloud, like topics and
connectors, so you can view them in Stream Lineage.

1. In the navigation menu, find your environment and click to open it.

   The Kafka clusters in the environment are shown.
2. Click the cluster that has the `users_mask` topic.

   The Kafka topics in the cluster are shown.
3. Hover over the `users_mask` topic and click **View topic details**.
   ![Navigation view in a Flink workspace in Confluent Cloud](images/cloud-flink-workspace-navigator.png)
4. In the topic details pane, scroll to the **Stream Lineage** section and
   click **View full lineage**.
   ![Stream Lineage view of a Flink pipeline in Confluent Cloud](images/cloud-flink-stream-lineage.png)
5. Hover over the nodes in the Stream Lineage diagram to see details of the
   data flow.

### Step 5: Delete resources

When you are finished with the Quick Start, delete the resources you created
to avoid unexpected charges to your account.

### Cloud Console

- Delete the persistent query
  1. Navigate to your environmentâs details page and click **Flink**.
  2. In the statements list, find the statement that has a status of **Running**.
  3. In the **Actions** column, click **â¦** and select **Delete statement**.
  4. In the **Confirm statement deletion** dialog, copy and paste the statement
     name and click **Confirm**.
- Delete the connector:
  1. From the navigation menu, select **Connectors**.
  2. Click **DatagenSourceConnector_users** and choose the **Settings** tab.
  3. Click **Delete connector**, enter the connector name (`DatagenSourceConnector_users`), and click
     **Confirm**.
- Delete the topics:
  1. From the navigation menu, click **Topics**, select the **users** topic,
     and choose the **Configuration** tab.
  2. Click **Delete topic**, enter the topic name (`users`), and click
     **Continue**.
  3. Repeat these steps with the `users_mask` topic.

### Confluent CLI

1. Delete the connector:
   ```none
   confluent connect delete <connector-id> [flags]
   ```

   For example:
   ```none
   confluent connect delete lcc-aa1234 --cluster lkc-000000
   ```
2. Delete the topic:
   ```none
   confluent kafka topic delete <topic name> [flags]
   ```

   For example:
   ```none
   confluent kafka topic delete users --cluster lkc-000000
   ```

### Confluent Cloud APIs

Delete a producer.

Request:

```bash
DELETE /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}
Host: api.confluent.cloud
```

Delete a topic.

Request:

```bash
DELETE /kafka/v3/clusters/{kafka_cluster_id}/topics/{topic_name}
Host: pkc-{0000}.{region}.{provider}.confluent.cloud
```

<a id="qs-next-steps"></a>

## Related content

- [Stream Processing with Confluent Cloud for Apache Flink](../flink/overview.md#ccloud-flink)
- Learn about Connectors: [Connect External Systems to Confluent Cloud](../connectors/overview.md#kafka-connect-cloud)
- Learn about schema management in Confluent Cloud: [Quick Start for Schema Management on Confluent Cloud](schema-registry.md#cloud-sr-config)
- Learn how to [Connect Clients to Confluent Cloud](../cp-component/clients-cloud-config.md#cloud-connect-clients)
- [Configure Multi-Node Environment](/platform/current/kafka/multi-node.html)
- [Try out the Confluent Cloud Demos and Examples](/platform/current/tutorials/examples/ccloud/docs/ccloud-demos-overview.html)
- Learn about serverless infrastructure: [Cloud-Native Apache Kafka: Designing Cloud Systems for Speed and Scale](https://developer.confluent.io/learn/cloud-native-kafka/)
