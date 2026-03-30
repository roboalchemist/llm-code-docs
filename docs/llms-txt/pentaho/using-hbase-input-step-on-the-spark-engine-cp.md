# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/select-an-engine-hbase-input/using-hbase-input-step-on-the-spark-engine-cp.md

# Using the HBase Input step on the Spark engine

You can set up the HBase Input step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules.

Before using the HBase Input step on the Spark engine, you must set up the `application.properties` file and vendor-specific JARs. See [HBase setup for Spark](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark) for instructions.
