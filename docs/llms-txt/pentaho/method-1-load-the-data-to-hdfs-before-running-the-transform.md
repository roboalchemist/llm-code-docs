# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/table-input-step-fails/method-1-load-the-data-to-hdfs-before-running-the-transform.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/table-input-step-fails/method-1-load-the-data-to-hdfs-before-running-the-transform.md

# Method 1: Load the data to HDFS before running the transform

1. Run a different transformation using the Pentaho engine to move the data to the HDFS cluster.
2. Then use HDFS Input to run the transformation using the Spark engine.
