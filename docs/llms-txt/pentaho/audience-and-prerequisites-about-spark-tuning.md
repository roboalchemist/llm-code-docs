# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/audience-and-prerequisites-about-spark-tuning.md

# Audience and prerequisites

Spark tuning features are intended for ETL developers who have a solid understanding of PDI, Spark, and your system's cluster resources. For effective Spark tuning, you need to know how a transformation uses your resources, including both your environment and data size. PDI steps vary in their resource requirements, so you should tune the Spark engine to meet the needs of each transformation.

To use the Spark tuning features, you need access to the following information:

* Cluster resources
* Amount of resources available to the Spark engine during execution, including memory allotments and number of cores.
* Size of data.

You may want to consult your cluster administrator, who can perform the following tasks:

* Monitor cluster resources on the YARN Resource Manager.
* Manage Spark execution resources on the Spark History Server.
