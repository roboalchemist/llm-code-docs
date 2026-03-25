# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/steps-cannot-run-in-parallel.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/steps-cannot-run-in-parallel.md

# Steps cannot run in parallel

If you are using the Spark engine to run a transformation with a step that cannot run in parallel, it generates errors in the log.

Some steps cannot run in parallel (on multiple nodes in a cluster), and will produce unexpected results. However, these steps can run as a coalesced dataset on a single node in a cluster. To enable a step to run as a coalesced dataset, add the step ID as a property value in the configuration file for using the Spark engine.
