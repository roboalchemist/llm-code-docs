# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer.md

# Kinesis consumer

The Kinesis consumer step gets and processes data records from Amazon Kinesis Data Streams (KDS). This step is useful for managing your Amazon KDS Applications. When you set up an Amazon KDS application in the Kinesis consumer step, the name property uniquely identifies the application that is associated with your AWS account and geographical region of the data stream. Then your consumer is ready to get and process data records from the indicated Kinesis data stream.

In the PDI Kinesis consumer step itself, you can define the location for processing, as well as the specific data formats to stream data and system metrics. You can set up this step to collect monitored events, track user consumption of data streams, and monitor alerts.

The Kinesis consumer step pulls [streaming data](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Streaming%20Analytics/Streaming%20analytics=GUID-27004CDD-BC78-457A-ABB5-1683D9AB3FBE=3=en=.md) from Amazon Kinesis Data Streams (KDS) through a PDI transformation. The parent Kinesis consumer step runs a child transformation that executes according to message batch size or duration, so you can process a continuous stream of records in near real-time. The child transformation must start with the [Get records from stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream) step.

Additionally, in the Kinesis consumer step, you can select a step in the child transformation to stream records back to the parent transformation. Records processed by a Kinesis consumer step in a parent transformation can then be passed downstream to any other steps included within the same parent transformation.

**Note:** Since the Kinesis consumer step continuously ingests streaming data, you may want to use the [Abort](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation to stop consuming records from Kinesis Data Streams for specific workflows. For example, you can run the parent transformation on a timed schedule, or abort the child transformation if sensor data exceeds a preset range.
