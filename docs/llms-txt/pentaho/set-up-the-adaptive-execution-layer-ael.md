# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael.md

# Set up the Adaptive Execution Layer (AEL)

Pentaho uses the Adaptive Execution Layer for running transformations on the Spark Distributive Compute Engine. AEL adapts steps from a transformation developed in PDI to Spark-native operators. The AEL daemon builds a transformation definition in Spark, which moves execution directly to the cluster.

Your installation of Pentaho includes the AEL daemon which you can set up for production to run on your clusters. After you configure the AEL daemon, the PDI client communicates with both your Spark cluster and the AEL daemon, which lives on a node of your cluster to launch and run transformations.

Before you can select the Spark engine through run configurations, you will need to configure AEL for your system and your workflow. Depending on your deployment, you may need to perform additional configuration tasks, such as setting up AEL in a secure cluster.

AEL runs PDI transformations in Spark-centric manner, which is documented for each step using the Spark engine.

See the **Administer Pentaho Data Integration and Analytics** and **Pentaho Data Integration** documents for further infotmation on AEL, Spark engine run configurations, and related transformation steps.
