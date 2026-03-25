# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/set-up-the-vendor-specified-jars.md

# Set up the vendor-specified JARs

Each vendor has differences in their byte conversion for HBase, so you must use the JAR files for the Hadoop distribution you are using.

**Note:** Vendor-specific JARS for HBase are not shipped with Spark or HDFS.

Perform the following steps to set up the vendor-specific JARs:

1. Navigate to the `design-tools/data-integration/adaptive-execution/extra` directory and delete the three HBase JAR files.
2. Navigate to the `design-tools/data-integration/plugins/pentaho-big-data-plugin/hadoop-configurations` directory and locate your CDH or HDP distribution folder.
3. Locate the `lib/pmr` directory in your distribution folder.
4. Copy the six HBase files, along with the metrics-core file to the `design-tools/data-integration/adaptive-execution/extra` folder.
5. To complete your setup, you must restart the AEL daemon.

   See the **Administer Pentaho Data Integration and Analytics** document for instructions.
