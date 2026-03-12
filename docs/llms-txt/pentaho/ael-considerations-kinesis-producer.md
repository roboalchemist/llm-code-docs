# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer/ael-considerations-kinesis-producer.md

# AEL considerations

When using the Kinesis Producer step with the [Adaptive Execution Layer](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page), the following may affect performance and results.

* When running the Kinesis Consumer step on AEL Spark, use HDP 3.x. Earlier versions of HDP are not supported.
