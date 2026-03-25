# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally/determining-spark-resource-requirements.md

# Determining Spark resource requirements

To tune your Spark application, start by knowing your cluster size and the allowable percentage of cluster resources that a KTR can consume while running, as established by the cluster administrator. With that limitation in mind, you can maximize the number of executors, while providing each with adequate resources to do processing. As a best practice, reserve the following cluster resources when estimating the Spark application settings:

* 1 core per node.
* 1 GB RAM per node.
* 1 executor per cluster for the application manager.
* 10 percent memory overhead per executor.

**Note:** The example below is provided only as a reference. Your cluster size and job requirement will differ.
