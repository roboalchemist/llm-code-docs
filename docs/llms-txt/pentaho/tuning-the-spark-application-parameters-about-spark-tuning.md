# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/tuning-the-spark-application-parameters-about-spark-tuning.md

# Tuning the Spark application parameters

Spark transformations are lazy loaded. They are only loaded into a process when they are needed, which are triggered by actions. Some examples of these actions are count, collect, take, and save.

Spark views PDI transformations as applications. If you execute a PDI transformation on a Spark engine, the PDI transformation appears in Spark as an application on your cluster.
