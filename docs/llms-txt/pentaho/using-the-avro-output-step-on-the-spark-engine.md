# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-output/using-the-avro-output-step-on-the-spark-engine.md

# Using the Avro Output step on the Spark engine

You can set up the **Avro Output** step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to successfully process null values according to Spark's processing rules.
