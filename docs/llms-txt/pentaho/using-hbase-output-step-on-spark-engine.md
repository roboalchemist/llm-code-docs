# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-output/select-an-engine-hbase-output/using-hbase-output-step-on-spark-engine.md

# Using the HBase Output step on the Spark engine

You can set up the HBase Output step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules. For specific instructions on using this step with Spark, see [HBase setup for Spark](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark).
