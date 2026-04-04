# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/adaptive-execution-layer-di-perspective-in-pdi-client.md

# Adaptive Execution Layer

Pentaho uses the Adaptive Execution Layer (AEL) for running transformations with different engines. AEL adapts steps from the transformation you develop in PDI to native operators in the engine you select for your environment, such as AEL-Spark in a Hadoop cluster. The AEL-Spark engine is better suited for running big data transformations in a Hadoop cluster.

When you select the AEL-Spark engine for running your transformation, AEL matches steps in your transformation to the native operators in the Spark engine. For example, if your transformation contains a Hadoop File Input step, AEL uses an equivalent Spark operator. AEL builds a transformation definition for Spark, which moves execution directly to the cluster, leveraging Spark’s ability to coordinate large amount of data over multiple nodes.

AEL must be configured before using the Spark engine. Refer your Pentaho or IT administrator to the **Install Pentaho Data Integration and Analytics** document for more details. Once configured, you can select the Spark engine through run configurations. See [Run Configurations](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs) for more details.
