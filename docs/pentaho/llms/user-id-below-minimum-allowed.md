# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/user-id-below-minimum-allowed.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/user-id-below-minimum-allowed.md

# User ID below minimum allowed

If you are [using the Spark engine in a secured cluster](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael) and an error about minimum user ID occurs, the user ID of the proxy user is below the minimum user ID required by the cluster. See [Cloudera documentation](https://www.cloudera.com/documentation/enterprise/5-5-x/topics/cm_sg_s7_prepare_cluster.html#xd_583c10bfdbd326ba--6eed2fb8-14349d04bee--76df) for details.

To resolve, change the ID of the proxy user to be higher than the minimum user ID specified for the cluster.
