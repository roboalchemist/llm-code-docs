# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/set-up-the-application-properties-file.md

# Set up the application properties file

You must set up the `application.properties` file to permit Spark jobs on AEL to access the `hbase-site.xml` file from the HDFS cluster. This setup enables Spark jobs to connect to HBase from the Spark Executors. You must also specify the location of the vendor-specific JARs described below so they can be loaded on the classpath.

Perform the following steps to set up the `application.properties` file:

1. Navigate to the `design-tools/data-integration/adaptive-execution/config` folder and open the `application.properties` file with any text editor.
2. Set the value of the**hbaseConfDir** property to the location of your `hbase-site.xml` file.
3. Set the value of the **extraLib** property to the location of the vendor-specific JARs.

   The default value is ./extra.
4. Save and close the file.
