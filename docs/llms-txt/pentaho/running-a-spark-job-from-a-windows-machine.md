# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/spark-submit/troubleshooting-your-configuration/running-a-spark-job-from-a-windows-machine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/spark-submit/troubleshooting-your-configuration/running-a-spark-job-from-a-windows-machine.md

# Running a Spark job from a Windows machine

The following errors may occur when running a Spark Submit job from a Windows machine:

* `ERROR yarn.ApplicationMaster: Uncaught exception: org.apache.spark.SparkException: Failed to connect to driver! - JobTracker's log`
* `Stack trace: ExitCodeException exitCode=10 - Spoon log`

To resolve these errors, create a new rule in the Windows firewall settings to enable inbound connections from the cluster.
