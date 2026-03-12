# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-input/using-the-avro-input-step-on-the-spark-engine.md

# Using the Avro Input step on the Spark engine

You can set up the **Avro Input** step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to successfully process null values according to Spark's processing rules.

Additionally, when using the Avro Input step on an Amazon EMR cluster, you must copy the `spark-avro_2.11-2.4.2.jar` file from your *SPARK\_HOME* folder into the `extra` folder in your AEL `data-integration` setup location. The following is an example command to copy the file:

```
cp /usr/lib/spark/external/lib/spark-avro_2.11-2.4.2.jar <User>/data-integration/adaptive-execution/extra/
```
