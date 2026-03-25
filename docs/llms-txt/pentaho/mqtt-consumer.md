# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer.md

# MQTT Consumer

The PDI client can pull [streaming data](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Streaming%20Analytics/Streaming%20analytics=GUID-27004CDD-BC78-457A-ABB5-1683D9AB3FBE=3=en=.md) from an MQTT broker or clients through an MQTT transformation. The parent MQTT Consumer step runs a child transformation that executes according to the message batch size or duration, allowing you to process a continuous stream of records in near real-time. The child transformation must start with the [Get records from stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream) step.

Additionally, from the MQTT Consumer step, you can select a step in the child transformation to stream records back to the parent transformation. This capability allows records processed by an MQTT Consumer step in a parent transformation to be passed downstream to any other steps included within the same parent transformation.
