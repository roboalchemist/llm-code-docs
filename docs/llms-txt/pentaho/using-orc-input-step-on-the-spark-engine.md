# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-input/select-an-engine-orc-input-step/using-orc-input-step-on-the-spark-engine.md

# Using the ORC Input step on the Spark engine

You can set up the ORC Input step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to successfully process null values according to Spark's processing rules.

Because of Cloudera Distribution Spark (CDS) limitations, the step does not support AEL for reading Hive tables containing data files in the ORC format from Spark applications in YARN mode. As an alternative, you can use the Parquet data format for columnar data using Impala.
