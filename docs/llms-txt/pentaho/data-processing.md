# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/streaming-analytics/data-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/streaming-analytics/data-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics/data-processing.md

# Data processing

Once the data stream is ingested through windowing, you can process these windows in your child transformation. Use the child transformation to adjust the data and handle event alerts as needed. After processing, you can either load the windowed data into various outputs or publish it back into the data message stream. You can publish data back into the message stream by using the following producer steps for your specified target:

* [AMQP Producer](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-producer): Advanced Message Queuing Protocol brokers
* [JMS Producer](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-producer): Apache ActiveMQ Java Messaging Service server or the IBM MQ middleware
* [Kafka Producer](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-producer): Kafka server
* [Kinesis Producer](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer): Support for pushing data to a specific region and stream located within the Amazon Kinesis Data Streams service
* [MQTT Producer](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-producer): Message Queuing Telemetry Transport broker or clients

You can also use the data streaming window to capture data for analysis. Streaming Pentaho data services can be created from output steps in the child transformation. You can use CTools to create dashboards using these services as data sources. See **Pentaho CTools** for more information.

Once started, streaming data transformations run continuously. You can stop these transformations using the following tools:

* The stop option in the PDI client.
* The [Abort](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation.
* Restarting the Pentaho or Spark execution engine.

**CAUTION:**

Stopping or aborting a continuous transformation may cause data loss. Changing the flow of a data stream affects the data that is ingested and processed. Please plan accordingly. If you are working with a Kafka server, you have the option to control when an offset is committed to your window. Use this option to retain the data if the message flow is interrupted.
