# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/jms-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-consumer.md

# JMS Consumer

Use the JMS Consumer step to receive [streaming data](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics) from the Apache ActiveMQ Java Messaging Service (JMS) server or the IBM MQ® middleware.

The parent JMS Consumer step runs a child (sub-transformation) that executes according to the message batch size or duration, letting you process a continuous stream of records in near real-time. The child transformation must start with the [Get records from stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream) step. You can configure the JMS Consumer step to continuously ingest streaming data from your JMS server.

In the JMS Consumer step itself, you can define the number of messages to accept for processing, as well as the specific data formats to stream activity data and system metrics. You can set up this step to collect monitored events, track user consumption of data streams, and monitor alerts. Additionally, you can select a step in the child transformation to stream records back to the parent transformation, which passes records downstream to any other steps included within the same parent transformation.

**Note:** Since the JMS Consumer step continuously ingests streaming data, you may want to use the [Abort](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation to stop consuming records from JMS for specific workflows. For example, you can run the parent transformation on a timed schedule, or abort the child transformation if sensor data exceeds a preset range.
