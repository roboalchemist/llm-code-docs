# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp.md

# About Spark tuning in PDI

Spark tuning is the customization of PDI transformation and step parameters to improve the performance of your PDI transformation executed on the Spark engine. These Spark parameters include both the transformation parameters, which we call **application tuning parameters** when working with PDI transformations on Spark, and step-level parameters, which we call **Spark tuning options**. Together, the application tuning parameters and the Spark tuning options control memory storage and the number of partitions which are critical to optimizing the execution of your transformation.
