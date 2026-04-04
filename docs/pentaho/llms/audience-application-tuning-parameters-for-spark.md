# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/audience-application-tuning-parameters-for-spark.md

# Audience and prerequisites

These setup tasks are intended for two different audiences. Application tuning tasks that use AEL properties are intended for cluster administrators who manage the cluster nodes and the applications on each node for the Spark engine. Alternately, application tuning tasks that use PDI transformation parameters are intended for ETL developers who have permissions to read, write, and execute commands on the Spark cluster.

To configure the application tuning parameters, you need the following information:

* The processing model for the Spark engine in PDI, as described in [Executing on the Spark engine](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/executing-on-the-spark-engine-about-spark-tuning).
* Available cluster resources.
* Size of the data.
* Amount of resources available to the Spark application during execution, including memory allotments and number of cores.
* Access to the YARN ResourceManager to monitor cluster resources.
* Access to the Spark execution resources on the Spark History Server.
