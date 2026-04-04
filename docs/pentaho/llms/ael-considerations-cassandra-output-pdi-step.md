# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/cassandra-output/ael-considerations-cassandra-output-pdi-step.md

# AEL Considerations

When using the Cassandra Output step with the [Adaptive Execution Layer](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page), the following factor affects performance and results:

* Spark processes null values differently than the Pentaho engine. You will need to adjust your transformation to successfully process null values according to Spark's processing rules.
