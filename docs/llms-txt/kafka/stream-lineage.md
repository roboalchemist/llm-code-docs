# Source: https://docs.confluent.io/cloud/current/stream-governance/stream-lineage.md

<a id="cloud-stream-lineage"></a>

# Track Data with Stream Lineage on Confluent Cloud

To move forward with updates to mission-critical applications or answer
questions on important subjects like data regulation and compliance, teams need an
easy means of comprehending the big picture journey of data in motion.

Stream Lineage provides a graphical UI of event streams and data relationships with both
a birdâs eye view and drill-down magnification for answering questions like:

- Where did data come from?
- Where is it going?
- Where, when, and how was it transformed?

Answers to questions like these allow developers to trust the data theyâve found,
and gain the visibility needed to make sure their changes wonât cause any negative or
unexpected downstream impact. Developers can learn and make decisions quickly with
live metrics and metadata inspection embedded directly within lineage graphs.

#### NOTE
If you are working with secured data:

- The following tutorial assumes that you have [role-based access](../security/access-control/rbac/overview.md#cloud-rbac) to the clusters and topics you need.
- The tutorial assumes that you have role-based access to Stream Lineage. If you do not have this access, Stream Lineage will not show up as an option on any screen.
- Developer roles do not grant access to Stream Lineage. You can give developers
  access to Stream Lineage by granting them additional roles with appropriate scope for need-to-know; such as
  [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) role at the cluster level. To learn more, see [Access control (RBAC) for Stream Lineage](#stream-lineage-rbac) and [Role-based Access Control (RBAC) on Confluent Cloud](../security/access-control/rbac/overview.md#cloud-rbac).

<a id="stream-lineage-first-look"></a>

## First look

### What Stream Lineage shows

Stream Lineage in Confluent Cloud is represented visually to show the movement of data
from source to destination, and how it is transformed as it moves. The lineage
graph always shows the activity of producers and consumers of data for the last 10 minutes.

<a id="ways-to-view-stream-lineage"></a>

### How to access Stream Lineage views

There are multiple ways to get into the Stream Lineage view, as described in [Summary of navigation paths](#stream-lineage-nav-path-summary).
This example shows one path.

To view the Stream Lineage UIs:

1. Log on to Confluent Cloud using the Cloud Console.
2. Select an environment.
3. Select a cluster.
4. Select a topic.
5. Click **See in Stream Lineage** on the top right of the topic page.
6. The Stream Lineage for that topic is shown.

![image](images/dg-dl-overview.png)

The Stream Lineage shown in this example is the result of setting up a data pipeline based on several ksqlDB query streams.
If you havenât set up a data pipeline yet, your lineage view may only show a single, lonely event node.

To get an interesting lineage like the one shown above, take a spin through the [tutorial](#stream-lineage-tutorial) in the next section!

### View Stream Lineage for Confluent Platform with USM

After you [register a Confluent Platform cluster with Unified Stream Manager](../usm/register/overview.md#cloud-usm-register), you can view
its topic lineage directly in the Confluent Cloud Console. Stream Lineage visually represents your dataâs journey from
source to destination, including any transformations. The graph shows producer and consumer activity from the
last 10 minutes, offering a real-time view of your data streams.

To view the Stream Lineage for a Confluent Platform cluster with USM, follow these steps:

1. In the Confluent Cloud Console, select the environment that contains your Confluent Platform cluster.

1. From **Clusters** list, select your Confluent Platform cluster.
2. To open the lineage graph, choose one of the following options:
   - **For an overall cluster view**: Click **Stream Lineage** in the left menu.
   - **For a specific topicâs view**: Go to the topicâs details page and click the **Explore Stream Lineage** button.

This displays the complete Stream Lineage graph for your selection.

![image](images/usm-schema-lineage.png)

<a id="stream-lineage-nav-path-summary"></a>

### Summary of navigation paths

You can get into a Stream Lineage view from any of the following paths and resources on the Cloud Console:

- Select a topic from the topic list for a cluster (**Environments** > <cluster> > **Topics**). An embedded mini-view of the stream lineage for the selected topic is shown.
  From here, you can click **View full lineage** to open the complete lineage diagram.
  ![image](images/dg-dl-topic-mini-lineage-view.png)
- On the left menu from anywhere within a cluster on the Cloud Console, click **Stream Lineage**.
  ![image](images/dg-dl-left-menu-lineage.png)
- From a connector, click **See in Stream Lineage** on the top right of connector page.
  ![image](images/dg-dl-left-view-lineage-from-connector.png)

<a id="stream-lineage-tutorial"></a>

## Tutorial

In order to really see Stream Lineage in action, you need to configure topics,
producers, and consumers to create a data pipeline. Once you have events flowing
into your pipeline, you can use Stream Lineage to inspect where data is coming
from, what transformations are applied to it, and where itâs going.

### Select an environment, cluster, and Schema Registry

1. Add an environment or select an existing one.
2. [Add a cluster](../clusters/create-cluster.md#cloud-create-cluster) or select an existing one on which to run the demo.

   If you create a new cluster:
   - You must select a [cluster type](../clusters/cluster-types.md#cloud-cluster-types). You can choose any cluster type.
   - Choose a cloud provider and region.
   - Click **Continue** to review configuration and costs, usage limits, and uptime service level agreement (SLA)

   Then click **Launch Cluster**
3. The Schema Registry settings and information will be available on the Schema Registry tab for the environment.
   ![image](images/dg-dl-cluster-settings.png)
4. Generate and save the Schema Registry API key and secret for this Schema Registry. (Save the key to use later on step 10 of this procedure.)

If you need help with these initial steps, see [Quick Start for Confluent Cloud](../get-started/index.md#cloud-quickstart).

### Create the âstocksâ topic and generate data

1. Choose **Connectors** from the menu, and select the **Sample Data** (**Datagen**) source connector.
   ![image](images/dg-dl-datagen-connectors-choose.png)

   Select the **Stock trades** template and click **Additional configuration**.
   ![image](images/dg-dl-datagen-stock-trades-choose.png)
2. On **Topic selection** dialog, click **Add new topic**, and name the topic `stocks`.
   1. Accept the defaults for the other settings, and click **Create with defaults**. (It may take a moment to generate and appear in the list.)
   2. Select the `stocks` topic, and click **Continue**.
3. On the **Kafka credentials** dialog, choose **My account** to allow your connector to globally access everything that you have access to (as this is for development level testing, not for production).

   Download and save the key and secret, and click **Continue**.
4. On the **Configuration** dialog, choose the following options, then click **Continue**.
   - Output record format: **AVRO**
   - Schema: **Stock trades**
5. On the **Sizing** dialog, take the defaults, and click **Continue**.
6. On the **Review and launch** dialog, change the Connector name to **StockSource Connector**.
   ![image](images/dg-dl-datagen-setup-03.png)

   You have added the Connect **Datagen** source connector to generate sample data. The connector will use **AVRO** as the output record format, and start sending data to your target topic, `stocks`.
   ![image](images/dg-dl-sample-data.png)

### Create a ksqlDB app

1. Navigate to ksqlDB
2. Click **Create cluster**.
3. For âAccess controlâ, select either **My account**, then click **Continue**.
4. Provide a cluster name, such as `ksqlDB_stocks`, and accept the defaults for cluster size.
5. Click **Launch cluster**.

#### Verify your ksqlDB app is running

Return to the list of ksqlDB apps on the Cloud Console.

Your ksqlDB app should have completed Provisioning, and show a status of `Up`.

![image](images/dg-dl-ksql-app-up.png)

### Create persistent streams in ksqlDB to filter on stock prices

Navigate to the ksqlDB **Editor** and click into your ksqlDB app, `ksqlDB_stocks` (**ksqlDB_stocks** > **Editor**),  to create the following persistent streams.

Specify each query statement in the **Editor** and click **Run query** to start the query. You can click the **Streams** tab to view a list of running queries.

1. Create a stream for the `stocks` topic, then create a persistent stream that filters on stocks with price <= 100. This feed the results to the `stocks_under_100` topic.

   Youâll need to specify and run three separate queries for this step. You start by creating the `stocks` stream, then add the filters to find and list stocks under $100.
   After each of these, click **Run query**, then clear the editor to specify the next statement.
   ```bash
   CREATE STREAM stocks WITH (KAFKA_TOPIC = 'stocks', VALUE_FORMAT = 'AVRO');
   ```

   ```bash
   CREATE STREAM stocks_under_100 WITH (KAFKA_TOPIC='stocks_under_100', PARTITIONS=10, REPLICAS=3) AS SELECT * FROM stocks WHERE (price <= 100);
   ```

   ```bash
   SELECT * FROM stocks_under_100 EMIT CHANGES;
   ```

   - When you have these running, click the **Streams** tab. You should have two new streams, `STOCKS` and `STOCKS_UNDER_100`. (The last statement is a transient query on the stream, `STOCKS_UNDER_100`, to get some data onto the UI.)
   - Switch back to the Editor for the next step.
2. Create a persistent stream that filters on stocks to BUY, and feed the results to the `stocks_buy` topic.

   Youâll need to specify and run two separate queries for this step. After each of these, click **Run query**, then clear the editor to specify the next statement.
   ```bash
   CREATE STREAM stocks_buy WITH (KAFKA_TOPIC='stocks_buy', PARTITIONS=10, REPLICAS=3) AS SELECT * FROM stocks WHERE side='BUY';
   ```

   ```bash
   SELECT * FROM stocks_buy EMIT CHANGES;
   ```

   - Switch to the **Streams** tab to view your recent additions to the Streams list.
   - Click the Editor for the next step. (Switching back and forth will also give some time for the queries to start up.)
3. Create a persistent stream that filters on stocks to SELL.

   Youâll need to specify and run two separate queries for this step. After each of these, click **Run query**, then clear the editor to specify the next statement.
   ```bash
   CREATE STREAM stocks_sell WITH (KAFKA_TOPIC='stocks_sell', PARTITIONS=10, REPLICAS=3) AS SELECT * FROM stocks WHERE side='SELL';
   ```

   ```bash
   SELECT * FROM stocks_sell EMIT CHANGES;
   ```

When you have completed these steps, click the **ksqlDB** > **Streams** tab. You should have four persistent ksqlDB query streams
producing data to their associated topics:

- `STOCKS`
- `STOCKS_BUY`
- `STOCKS_SELL`
- `STOCKS_UNDER_100`

![image](images/dg-dl-ksqldb-streams-all.png)

The associated topics and schemas will be listed on those pages, respectively. Here is an example of the **Topics** page.

![image](images/dg-dl-topics.png)

### Consume events from the âstocksâ topic

Now, set up a consumer using the Confluent CLI to consume events from your `stocks` topic.

1. Log on using the Confluent CLI. (Provide username and password at prompts.)
   ```none
   confluent login --url https://confluent.cloud
   ```
2. List the environments to verify you are on the environment.
   ```none
   confluent environment list
   ```
3. If needed, re-select the environment youâve been using for this demo. (The active environment should have an asterisk beside it.):
   ```none
   confluent environment use <ENVIRONMENT_ID>
   ```
4. List the clusters to verify you are on the right cluster.
   ```none
   confluent kafka cluster list
   ```
5. If needed, re-select the cluster youâve been using for this demo. (The active cluster should have an asterisk beside it.)
   ```none
   confluent kafka cluster use <KAFKA_CLUSTER_ID>
   ```
6. Create Kafka API credentials for the consumer.

   Create an API key.
   ```bash
   confluent api-key create --resource <KAFKA_CLUSTER_ID>
   ```

   Use the API key.
   ```bash
   confluent api-key use <API_KEY> --resource <KAFKA_CLUSTER_ID>
   ```

   Alternatively, you can store the key.
   ```bash
   confluent api-key store --resource  <KAFKA_CLUSTER_ID>
   ```
7. Run a CLI consumer.
   ```bash
   confluent kafka topic consume stocks_buy --value-format avro --group buy_group
   ```
8. When prompted, provide the Schema Registry API key you generated in the first steps.

   You should see the consumer data being generated to the consumer at the command line, for example:
   ```bash
   My-MacBook-Pro:~ my$ confluent kafka topic consume stocks_buy --value-format avro --group buy_group
   Starting Kafka Consumer. ^C or ^D to exit
   {"SIDE":{"string":"BUY"},"QUANTITY":{"int":959},"SYMBOL":{"string":"ZVZZT"},"PRICE":{"int":704},"ACCOUNT":{"string":"XYZ789"},"USERID":{"string":"User_8"}}
   {"ACCOUNT":{"string":"ABC123"},"USERID":{"string":"User_1"},"SIDE":{"string":"BUY"},"QUANTITY":{"int":1838},"SYMBOL":{"string":"ZWZZT"},"PRICE":{"int":405}}
   {"QUANTITY":{"int":2163},"SYMBOL":{"string":"ZTEST"},"PRICE":{"int":78},"ACCOUNT":{"string":"ABC123"},"USERID":{"string":"User_8"},"SIDE":{"string":"BUY"}}
   {"PRICE":{"int":165},"ACCOUNT":{"string":"LMN456"},"USERID":{"string":"User_2"},"SIDE":{"string":"BUY"},"QUANTITY":{"int":4675},"SYMBOL":{"string":"ZJZZT"}}
   {"QUANTITY":{"int":1702},"SYMBOL":{"string":"ZJZZT"},"PRICE":{"int":82},"ACCOUNT":{"string":"XYZ789"},"USERID":{"string":"User_7"},"SIDE":{"string":"BUY"}}
   {"ACCOUNT":{"string":"LMN456"},"USERID":{"string":"User_9"},"SIDE":{"string":"BUY"},"QUANTITY":{"int":2982},"SYMBOL":{"string":"ZVV"},"PRICE":{"int":643}}
   {"SIDE":{"string":"BUY"},"QUANTITY":{"int":3687},"SYMBOL":{"string":"ZJZZT"},"PRICE":{"int":514},"ACCOUNT":{"string":"ABC123"},"USERID":{"string":"User_5"}}
   {"USERID":{"string":"User_5"},"SIDE":{"string":"BUY"},"QUANTITY":{"int":289},"SYMBOL":{"string":"ZJZZT"},"PRICE":{"int":465},"ACCOUNT":{"string":"XYZ789"}}
   ...
   ```

### Explore the data pipeline in Stream Lineage

<a id="stream-lineage-tour"></a>

#### Stream data quick tour

With the producers and consumers up and running, you can use Stream Lineage to visualize and explore the flow of data from the source connector
to the STOCKS topic, where queries filter the data on specified limits and generate lists to your three topics:
- `STOCKS_BUY`
- `STOCKS_SELL`
- `STOCKS_UNDER_100`

1. Search for `stocks` topic on the search box, then click `stocks` under **Topic** in that list.
   ![image](images/dg-dl-search-topic.png)
2. On the `stocks` topic page, in the embedded lineage view, click **View full lineage**.
   ![image](images/dg-dl-stocks-topic-stream-lineage-in-actions-menu.png)

   The Stream Lineage for the `stocks` topic is shown.
   ![image](images/dg-dl-overview.png)
3. Hover on a node for a high level description of the data source and throughput.
   - This example shows a ksqlDB query node
     ![image](images/dg-dl-on-query-hover.png)

     The thumbnail in this case shows:
     - Mode and type: persistent stream
     - Total number of bytes in and out of the flow for the last 10 minutes
     - Total number of messages in and out of the flow for the last 10 minutes
   - This example shows a topic node:
     ![image](images/dg-dl-on-topic-hover.png)

     The thumbnail in this case shows:
     - Topic name
     - [Schema format](/platform/current/schema-registry/serdes-develop/index.html) (can be Avro, Protobuf, or JSON schema)
     - Number of partitions for the topic
     - Total number of bytes into the topic during the last 10 minutes
     - Total number of messages received by the topic in the last 10 minutes
4. Click a node to inspect.
   ![image](images/dg-dl-on-topic-drilldown.png)
5. Return to the diagram, and hover on an edge to get a description of the flow between the given nodes.
   ![image](images/dg-dl-on-edge-hover.png)
6. Click the edge to inspect.
   ![image](images/dg-dl-on-edge-drilldown.png)

#### Tabs on node drilldown to inspect queries

The Stream Lineage inspect panel surfaces details and metrics about the queries based on the nodes you select.
The tabs available and details shown will vary, depending on the query. For example:

- **Overview tab** - Shows per topic throughput, along with bytes consumed and produced.
  ![image](images/dg-dl-topic-tabs-overview.png)
- **Messages tab** - Shows the list of messages the topic received.
  ![image](images/dg-dl-topic-tabs-messages.png)
- **Schema tab** - Shows a view-only copy of the schema for the topic. An editable version is available directly from the topic (see [Manage Schemas and Data Contracts in Confluent Cloud](../sr/schemas-manage.md#sr-prv)).
  ![image](images/dg-dl-topic-tabs-schema.png)
- **Query tab** - Shows a view-only copy of the persistent query that is sending results to the topic.
  (For details on stream processing, see [ksqlDB Stream Processing](../ksqldb/overview.md#ksqldb-cloud).)
  ![image](images/dg-dl-topic-tabs-query.png)

#### View and navigate options

From anywhere on the Stream Lineage view:

- Click the tab on the left side of the lineage view at any time to show/hide a navigation panel.
  ![image](images/dg-dl-left-nav.png)

From a drilldown on a ksqlDB query, within the lineage tabs:

- Click **View query** at the top of the tabs view to jump directly to the ksqlDB stream associated with the persistent ksqlDB query.
- Click the tab handle to the left of the tab view to expand the tab to full. Click again to collapse.
  ![image](images/dg-dl-stream-tabs-expand.png)

In addition to the above, the lineage view provides options to link directly
into topics, schemas, queries, and connectors at various point on the UIs.

#### Try this

- Click the **stocks** topic node, and scroll through the message throughput timelines on the **Overview** tab, then click **View topic** to go directly to the topic.
- Click the **stocks_buy** topic node, then click the **Schema** tab to view its associated schema.
- Click a query, such as **stocks_buy** query, and click the **Schema** tab. This shows you a menu style view of the same schema
  because the schema associated with the **stocks_buy** topic is coming from the **stocks_buy** query.
- To verify this, click **View query** to link to the **ksqlDB_stocks** query, then click the **Flow** tab under that app, and click **stocks_buy** on that diagram.
  (Note that you also can visualize a data flow particular to that query from directly within the ksqlDB app, but not the combined
  flows of all queries to all topics, as is shown on Stream Lineage.)

## Hide or show internal topics

From any Stream Lineage graph view, you have the option to hide or show internal (system) topics.
System topics are those that manage and track Confluent Cloud metadata, such as replication factors, partition counts,
and so forth. Typically, this system metadata is of less interest than data related your own topics,
and youâll want to hide it.

![image](images/dg-dl-hide-internal-topics.png)

## Browsing the diagram view

<a id="stream-lineage-point-in-time"></a>

### Set the diagram to a point in time (point in time lineage)

#### What is it?

Point-in-time lineage allows to visualize the flow of data at a point in time in
the past. The Essentials package only allow users to visualize the flow of data
from the past 10 minutes, but with point-in-time feature, only available on
Advanced package, a user can choose to see last 10 minutes, 30 minutes, 1 hour,
4 hours, 8 hours, 12 hours, 24 hours and 1 hour window on any of the last 7 days.

![Screenshot of point in time Stream Lineage for features page](images/dg-features-lineage-point-in-time.png)

#### Why is it important?

Sometimes the flow of data is not always continuous, might be that you ingest
data at a regular non real-time cadence, or some issue might interrupt the flow
of the data. In those cases looking at the last 10 minutes might not show
anything in Stream Lineage. Another important use case might be to troubleshoot
a potential data breach where you want to navigate to a point in time to
understand who were all the data consumers at that point.

This blog post explains the use of point-in-time lineage and the main use cases for Stream Lineage:
[How to Visualize Your Apache Kafka Data the Easy Way with Stream Lineage](https://www.confluent.io/blog/visualize-apache-kafka-data-easily-with-stream-lineage/)

#### How to use it

By default, graphs represent the last 10 minutes of data flowing through the system. You can navigate and search the graphs in this default time window,
or set a specific time window. These settings apply to all data on the cluster, whether that data is currently on-screen or not. (The example shows the time window re-set to âLast 24 hoursâ.)

![image](images/dg-dl-point-in-time.png)

Pre-set windows are available for:

- Last 10 minutes
- Last 30 minutes
- Last 1 hour
- Last 4 hours
- Last 8 hours
- Last 12 hours
- Last 24 hours (maximum size of a pre-set time window)

![image](images/dg-dl-point-in-time-windows.png)

You can also set a custom date and time window for your search, going back 7 days for a selected 1 hour block.

![image](images/dg-dl-custom-point-in-time.png)

The graphs, nodes, and available data will change depending on the selected time window.
For example, a custom setting to show data only from last Friday from 6:00-7:00 AM will not show
streams created later in the week. Similarly, the [graph search](#stream-graph-search)
is dependent on the time window setting, and will not find data that isnât available in the
current time window.

<a id="stream-graph-search"></a>

### Search the graph (Stream Lineage search)

#### What is it?

Lineage search enables searches within the lineage graph for particular entities
by partial or full names. The search finds topic names, connector names,
ksqlDB query names, consumer groups, and producer client IDs and spans
globally across the cluster, not just the on-screen nodes in the current diagram.

![Screenshot of Stream Lineage search for features page](images/dg-features-lineage-search.png)

#### Why is it important?

Many time customers have very complex streaming topologies with dozens if not
hundreds of applications, services, topics, queries, and so on. With this feature they
can easily isolate on the graph what they are interested in knowing more about.

#### How to use it

You can search the graph for partial or full names of entities. The search finds
topic names, connector names, ksqlDB query names, consumer groups, and
producer client IDs. The search spans globally across the cluster, not just
on-screen nodes in the current diagram.

Keep in mind that the search applies to data available across the cluster for the selected [time window](#stream-lineage-point-in-time).

![image](images/dg-dl-graph-search-00.png)

To execute a graph search, click into the Search bar and type a name (such as `buy` in this example).

![image](images/dg-dl-graph-search-01.png)

Next, select a search result by clicking it (for example `STOCKS_BUY`).

The drilldown for that entity is displayed.

![image](images/dg-dl-graph-search-02.png)

### Export a lineage diagram

To export the current diagram, click the Export icon ![image_export](images/dg-dl-export-icon.png) on the lower right tool panel.

![image](images/dg-dl-export-diagram.png)

### Reset the view

To reset the view to center on the entity that is the original focus of the diagram,
click the Reset icon ![image_reset_view](images/dg-dl-reset-view-icon.png) on the lower right tool panel.

![image](images/dg-dl-reset-view.png)

**Reset** view is only applicable when you launch the lineage diagram from within
an entity, such as a topic, ksqlDB table or stream, producer, consumer, and so forth.
It is not applicable if you launch the lineage diagram from the left menu or dashboard
because that is a global view, not centered on any specific node to begin with.

### Zoom in or out

Use the **+** and **-** buttons on the lower right tool panel to zoom in or zoom out on the lineage diagram.

![image](images/dg-dl-zoom-diagram.png)

### Traverse the Diagram

To explore the diagram, click, hold, and drag the cursor, or use analogous actions such
as three-finger drag on a Mac trackpad.

### All streams

Click **See all Streams** on the upper part of a diagram to view cards representing the data flows.

![image](images/dg-dl-all-streams-a.png)

The default view shows Stream 1.

![image](images/dg-dl-all-streams-1.png)

Click another card to focus in on a particular stream, for example Stream 2. The diagram
updates to show only the selected stream.

![image](images/dg-dl-all-streams-2.png)

## Understanding data nodes

Consumers and producers are automatically grouped; that is, a group of consumers or producers
is represented as a single node that expands upon drilldown to show the client IDs.

| Node                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![node-topic](images/dg-dl-node-Topic.png)         | A topic node shows:<br/><br/>- Topic name and link to the topic<br/>- Associated schemas (key and value)<br/>- Number of partitions<br/>- Total throughput as a time series line graph<br/>- Bytes consumed and produced per app, and per partition<br/>- Messages consumed and produced per query, which is ingress and egress for the stream                                                                                                                                                   |
| ![node-customApp](images/dg-dl-node-CustomApp.png) | A custom application node provides:<br/><br/>- Name of the application, and its status<br/>- Total throughput as a time series line graph<br/>- Bytes produced and consumed per topic<br/>- Drilldowns to show consumers and producers                                                                                                                                                                                                                                                           |
| ![node-query](images/dg-dl-node-Query.png)         | A ksqlDB query node shows:<br/><br/>- Query name and link to the query<br/>- Query type, status, and mode<br/>- Total throughput as a time series line graph<br/>- Bytes produced and consumed per topic<br/>- Drilldowns to show the ksqlDB app data                                                                                                                                                                                                                                            |
| ![node-kstream](images/dg-dl-node-KStream.png)     | A Kafka streams app includes:<br/><br/>- Application ID<br/>- Total throughput as a time series line graph<br/>- Bytes in and bytes out in the past 10 minutes<br/>- Messages in and messages out in the past 10 minutes                                                                                                                                                                                                                                                                         |
| ![node-connector](images/dg-dl-node-Connector.png) | A Kafka Connector node shows:<br/><br/>- Connector name and link to the connector<br/>- Type of connector (plugin type)<br/>- Message throughput and lag<br/>- Total production as a time series line graph<br/>- Bytes produced per topic as a time series line graph<br/>- Associated tasks and their statuses                                                                                                                                                                                 |
| ![node-cli](images/dg-dl-node-CLI.png)             | A CLI node shows monitoring data on producers and consumers running on the<br/>the Confluent CLI, producing to or reading from a topic on your Confluent Cloud cluster:<br/><br/>- For consumers, name or consumer group name, bytes in, number of messages read<br/>- For producers, client ID, bytes out, number of messages sent<br/>- Total and per topic number of bytes produced or consumed, as time series graphs<br/>- Drilldowns to show individual consumers, producers, and messages |

## Understanding node groups

In cases where you have a threshold number of nodes of the same type in a
workflow (24 or more like nodes), Stream Lineage collapses these into a single
node group to save screen real estate and improve navigation. This grouping is purely
for visual display of like nodes that are processing data to or from the same
connection point.

![image](images/dg-dl-super-node-overview.png)

To drill down on the individual nodes represented by a node group:

1. Click the composite node (node group) to display the individual nodes on the right.
   ![image](images/dg-dl-super-node-citibike.png)
2. Select a node from the list on the right to inspect details of that node.
   ![image](images/dg-dl-super-node-citibike-drilldown.png)

Automatic visual grouping of like nodes applies to any node type, but producers
and consumers are the most common as there is a tendency to employ large numbers
of these.

## Understanding edges

Edge thumbnails and drilldowns describe the flow between the given nodes. They show:

- The node where the data came from
- The node where the data is going to
- Bytes transferred
- Number of messages transferred

The relative thickness of an edge indicates the amount
of data that is moving through the connected nodes during the selected time range,
also known as throughput. Thicker edges have a higher throughput than thinner
edges. To get specific throughput numbers, use the drilldowns.

Hovering on an edge gives you the thumbnail.

![image](images/dg-dl-edge-summary.png)

Drilldown on an edge provides the tab view.

![image](images/dg-dl-edge-summary-tab.png)

<a id="stream-lineage-rbac"></a>

## Access control (RBAC) for Stream Lineage

If role-based access control (RBAC) is configured on your clusters, you must
make sure you have access to the appropriate resources, such as clusters,
topics, and features such as Stream Lineage views. This section provides a
summary of roles related to Stream Lineage access.

For details on how to manage RBAC for these resources, see [List the role bindings for a principal](../security/access-control/rbac/manage-role-bindings.md#manage-rbac-using-console), [Predefined RBAC Roles in Confluent Cloud](../security/access-control/rbac/predefined-rbac-roles.md#cloud-rbac-roles), and [List the role bindings for a principal](../security/access-control/rbac/manage-role-bindings.md#cloud-rbac-cli).

- The following roles have full access to Stream Lineage views:

  | Role                                                                                                 | View Scope                                                      | Admin Scope                                                                 |
  |------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------|
  | [OrganizationAdmin](../security/access-control/rbac/predefined-rbac-roles.md#organizationadmin-role) | All                                                             | All                                                                         |
  | [EnvironmentAdmin](../security/access-control/rbac/predefined-rbac-roles.md#environmentadmin-role)   | Organization, Support Plan, Users                               | All clusters in the environment, Schema Registry, Networking                |
  | [CloudClusterAdmin](../security/access-control/rbac/predefined-rbac-roles.md#cloudclusteradmin-role) | Organization, Environment, Support Plan, Users, Schema Registry | Specified Cluster, Topics, ksqlDB applications, Connectors, Schema Subjects |
  | [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role)                   | Organization, Environment, Cluster                              | N/A                                                                         |
  | [DataDiscovery](../security/access-control/rbac/predefined-rbac-roles.md#datadiscovery-role)         | Environment                                                     | N/A                                                                         |
  | [DataSteward](../security/access-control/rbac/predefined-rbac-roles.md#datasteward-role)             | Environment                                                     | N/A                                                                         |

#### NOTE
- Developer roles do not grant access to Stream Lineage. You can give developers
  access to Stream Lineage by granting them additional roles from the above table
  with appropriate scope for need-to-know; such as the [Operator](../security/access-control/rbac/predefined-rbac-roles.md#operator-role) role at the cluster level.
  To learn more, see [Access control (RBAC) for Stream Lineage](#stream-lineage-rbac) and [Role-based Access Control (RBAC) on Confluent Cloud](../security/access-control/rbac/overview.md#cloud-rbac).
- The DataSteward and DataDiscovery roles have access to view the lineage but cannot access the actual message contents.
- DataSteward and DataDiscovery do not have access to view details of a ksqlDB node.

To learn more, see [Role-based Access Control (RBAC) on Confluent Cloud](../security/access-control/rbac/overview.md#cloud-rbac).

<a id="stream-lineage-teardown"></a>

## Pause or teardown

When you are ready to quit the demo, donât forget to either pause or tear down resources so as not to incur unnecessary charges.
The extent to which you want to maintain your setup will depend on your use case. Here are some options.

### Pause data generation temporarily

If you want to keep your setup but minimize data traffic and cost when the system isnât in use, do the following.

1. Stop the consumer.

   On the Confluent CLI where the consumer is running, press Ctrl+C to stop consuming data.
2. Pause the <kconnect> Datagen âStockSourceâ  producers.

   On the Confluent Cloud Console, navigate to the Datagen **StockSource** connector, click it to drill down,
   and pause the connector.

   This will suspend data generation so that no messages are flowing through your cluster.
   ![image](images/dg-dl-stop-datagen-connector.png)

### Stop the queries and remove the cluster

To entirely tear down this instance, follow the âtemporary pauseâ steps above, but also perform the following tasks on the Confluent Cloud Console:

1. Navigate to ksqlDB, click **ksqlDB_stocks**, click the **Persistent queries** tab, and click **Terminate** on each query.
2. After you pause the <kconnect> Datagen âStockSourceâ, delete the connector.
3. At the Environment level, delete the cluster.

<a id="granular-ksqldb-and-acls"></a>

## Appendix A: Creating a ksqlDB app with granular access and assigning ACLs

As an alternative to creating the ksqlDB app with global access, you can create
the app with granular access, assign a service account to it, and then create
ACLs limited specifically to your ksqlDB app. There may be cases where you want to
limit access to the ksqlDB cluster to specific topics or actions.

1. Navigate to ksqlDB
2. Click **Create application myself**.
3. Select **Granular access** and click **Continue**.
4. Under **Create a service account**:
   - Select **Create a new one** (unless you already have an account you want to use).
   - Provide a new service account name and description, such as `stocks_trader` `ksqlDB_stocks`.
   - Check the box to add required ACLs when the ksqlDB app is created.
5. Provide access to the `stocks` topic (this should already be selected), and click **Continue**.
6. Create the ACLs for your ksqlDB app as follows (skip this step if you have done this previously for this app).
7. Log on to the Confluent Cloud by means of the Confluent CLI. (Provide username and password at prompts.)
   ```none
   confluent login --url https://confluent.cloud
   ```
8. List the environments to get the environment ID.
   ```none
   confluent environment list
   ```
9. Select the environment youâve been using for this demo.
   ```none
   confluent environment use <ENVIRONMENT_ID>
   ```
10. List the clusters to get the right cluster ID.
    ```none
    confluent kafka cluster list
    ```
11. Select the cluster youâve been using for this demo.
    ```none
    confluent kafka cluster use <KAFKA_CLUSTER_ID>
    ```
12. List the ksqlDB apps to get the ID for your app.
    ```none
    confluent ksql cluster list
    ```
13. Run this command to get the service account ID.
    ```none
    confluent ksql cluster configure-acls <KSQL_APP_ID> * --cluster <KAFKA_CLUSTER_ID> --dry-run
    ```
14. Copy the service account ID (after `User:<SERVICE_ACCOUNT_ID>` in the output).
15. Allow READ access to all topics on the ksql cluster for your service account ID.
    ```none
    confluent kafka acl create --allow  --service-account  <SERVICE_ACCOUNT_ID> --operations read --topic  '*'
    ```
16. Allow WRITE access to all topics on the ksql cluster for your service account ID.
    ```none
    confluent kafka acl create --allow --service-account <SERVICE_ACCOUNT_ID> --operations write --topic "*"
    ```
17. Allow CREATE access for all topics on the ksql cluster for your service account ID.
    ```none
    confluent kafka acl create --allow  --service-account  <SERVICE_ACCOUNT_ID> --operations create --topic  '*'
    ```

## Related content

- Confluent Developer Course: [Governing Data Streams](https://developer.confluent.io/learn-kafka/governing-data-streams/stream-lineage/)
