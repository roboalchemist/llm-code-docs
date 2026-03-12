# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/amazon-emr/use-hbase-with-ael-and-amazon-emr-ael-setup-specific-to-emr.md

# Use HBase with AEL and Amazon EMR

To use HBase with AEL and Amazon EMR, you must add the HBase libraries to the classpath.

Perform the following steps to add the HBase libraries:

1. Stop the AEL daemon.
2. From a command prompt (terminal window) on the cluster, run the following command:

   ```
   add SPARK_DIST_CLASSPATH=$(hbase classpath)
   ```
3. Start the AEL daemon.
