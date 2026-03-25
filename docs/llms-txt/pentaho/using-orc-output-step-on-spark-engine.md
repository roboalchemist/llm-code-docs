# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-output/select-an-engine-orc-output-step/using-orc-output-step-on-spark-engine.md

# Using the ORC Output step on the Spark engine

You can set up the ORC Output step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules.

Because of Cloudera Distribution Spark (CDS) limitations, the step does not support the [Adaptive Execution Layer](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page) for writing Hive tables containing data files in the ORC format from Spark applications in YARN mode. As an alternative, you can use the Parquet data format for columnar data using Impala.
