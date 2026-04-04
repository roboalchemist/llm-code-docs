# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer.md

# Kafka consumer

The PDI client pulls [streaming data](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Streaming%20Analytics/Streaming%20analytics=GUID-27004CDD-BC78-457A-ABB5-1683D9AB3FBE=3=en=.md) from Kafka through a Kafka transformation. The parent Kafka Consumer step runs a child (sub-transformation) that executes according to message batch size or duration, letting you process a continuous stream of records in near real-time. The child transformation must start with the [Get records from stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream) step.

You can configure the Kafka Consumer step to continuously ingest streaming data from your Kafka server. Depending on your setup, you can execute the transformation within PDI.

In the Kafka Consumer step itself, you can define the number of messages to accept for processing, as well as the specific data formats to stream activity data and system metrics. You can set up this step to collect monitored events, track user consumption of data streams, and monitor alerts.

Additionally, from the Kafka Consumer step, you can select a step in the child transformation to stream records back to the parent transformation. This allows records processed by a Kafka Consumer step in a parent transformation to be passed downstream to any other steps included within the same parent transformation.

Kafka records are stored within topics, and consist of a category to which the records are published. Topics are divided into a set of logs known as partitions. Kafka scales topic consumption by distributing partitions among a consumer group. A consumer group is a set of consumers sharing a common group identifier.

Before using the Kafka Consumer step, you must configure a named connection for your distribution. For information on named connections, see [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article).

**Note:** Since the Kafka Consumer step continuously ingests streaming data, you may want to use the [Abort](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation to stop consuming records from Kafka for specific workflows. For example, you can run the parent transformation on a timed schedule, or abort the child transformation if sensor data exceeds a preset range.

You can stop the consumer ingestion by entering a stop date in the **Offset Settings** tab. You can also use SSL and SASL secure connections by providing the configuration information explained in the **Options** tab topic.
