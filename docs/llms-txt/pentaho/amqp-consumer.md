# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer.md

# AMQP Consumer

The Advanced Message Queuing Protocol (AMQP) Consumer step receives [streaming data](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics) from an AMQP message producer through an AMQP 0-9-1 compatible broker. You can configure this step to use an existing AMQP message queue or create a new one.

You can also set up the AMQP Consumer step to continuously ingest streaming data from either an AMQP message or broker to collect messages about monitored events, track user consumption of data streams, or monitor alerts. The parent AMQP Consumer step runs a child (sub-transformation) that executes according to the message batch size or duration, letting you process a continuous stream of records in near real-time. The child transformation must start with the [Get records from stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream) step. Additionally, you can select a step in the child transformation to stream records back to the parent transformation, which passes the records downstream to any other steps included within the same parent transformation.

**Note:** Since the AMQP Consumer step continuously ingests streaming data, you may want to use the [Abort](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation to stop consuming records from AMQP for specific workflows. For example, you can run the parent transformation on a timed schedule, or abort the child transformation if sensor data exceeds a preset range.
