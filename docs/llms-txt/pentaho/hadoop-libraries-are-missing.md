# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/hadoop-libraries-are-missing.md

# Hadoop libraries are missing

If you use the Spark libraries packaged with EMR, Cloudera, and Hortonworks’ distributions, you must add the Hadoop libraries to the classpath with the *SPARK\_DIST\_CLASSPATH* environment variable. These distributions are not packaged with the Hadoop libraries. For EMR, these libraries are required to access S3 resources.
