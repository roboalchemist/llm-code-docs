# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page.md

# Adaptive Execution Layer

Pentaho uses an Adaptive Execution Layer (AEL) for running transformations with Spark. AEL adapts steps from the transformation you develop in PDI to use the native operator functions in Spark. This adaptation is necessary because the Spark engine runs big data transformations in the Hadoop cluster differently than the Pentaho engine. For example, the Spark engine may not require some fields in the PDI step, or it may require setting a precise value setting for an option. Also, null values must be adjusted because Spark processes null values differently than the Pentaho engine.

Some PDI steps commonly used in big data transformations are specifically coded to the Spark APIs for improved performance when using the Spark engine. To see whether the step you want to use has been optimized for distributed processing with Spark, refer the documentation for that step. You can also view the list of [Recommended PDI steps to use with Spark on AEL](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page/use-ael/recommended-pdi-steps-to-use-with-spark-on-ael-cp).

To decide whether the Spark engine or the Pentaho engine is the best choice for your transformation, you must know what cluster resources you have and the size of your data sets.
