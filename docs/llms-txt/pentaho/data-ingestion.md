# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/streaming-analytics/data-ingestion.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/streaming-analytics/data-ingestion.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics/data-ingestion.md

# Data ingestion

Data is ingested into PDI by pulling messages from a stream into a transformation through a specified window. A consumer step in a parent transformation pulls the data into PDI, then runs a child sub-transformation, which executes according to the window parameters. The window creates a continuous stream of records in near real-time.

In the consumer step itself, you can define the number of messages to accept for processing, as well as the specific data formats to stream data. You can set up this step to collect events, monitor alerts, and track user consumption of data streams. Additionally, you can select a step in the child transformation to stream records back to the parent transformation, which passes records downstream to any other steps included within the same parent transformation.

The following consumer steps ingest streaming data into PDI from the specified sources:

* [**AMQP Consumer**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer)

  Advanced Message Queuing Protocol brokers
* [**JMS Consumer**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-consumer)

  Apache ActiveMQ Java Messaging Service server or IBM MQ middleware
* [**Kafka Consumer**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer)

  Kafka server
* [**Kinesis Consumer**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer)

  Amazon Kinesis Data Streams service
* [**MQTT Consumer**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer)

  Message Queuing Telemetry Transport broker or clients

In PDI, the data stream window is defined by either duration (in milliseconds) or number of rows. The window of data is created when either the duration or number of rows occur. For example, if the duration is set to `1000` milliseconds and the number of rows is 1000, windows of data are created whenever time intervals of 1000 milliseconds are reached or 1000 rows have been received. If you set either duration or number of rows to `0` (zero), PDI will ignore that parameter. For example, if duration is set to `1000` milliseconds and the number of rows is zero, windows are created only every 1000 milliseconds.

You can specify the maximum number of these batches used to collect records at the same time. However, you should only specify a maximum number of these concurrent batches when your consumer step cannot keep pace with the speed at which the data is streaming. Your computing environment must have adequate CPU and memory for this implementation. An error will occur if your environment cannot handle the maximum number of concurrent batches specified.

Depending on your setup, you can run the transformation within PDI or using Spark within the Adaptive Execution Layer (AEL) as the execution engine, which is set in the [Run Options](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation) dialog box. The Spark engine executes the child transformation by duration only, and not by the number of rows.

**Note:** If you use the Spark engine on streaming data, your transformation will use the native Spark Streaming. PDI will not report the execution results. This information will appear in Spark on your cluster.

Before using a consumer step with big data, you must set up Pentaho to connect to a cluster. See [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article) for instructions.
