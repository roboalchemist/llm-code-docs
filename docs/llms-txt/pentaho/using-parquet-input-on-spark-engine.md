# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-input/select-an-engine-parquet-input/using-parquet-input-on-spark-engine.md

# Using Parquet Input on the Spark engine

You can set up the Parquet Input step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules.
