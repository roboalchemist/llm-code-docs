# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/cannot-read-footer-in-a-spark-file-ael-troubleshooting.md

# Cannot read footer in a Spark file

You might receive a “Could not read footer for file” error message from Spark when trying to access your data file while running on the Spark engine. This error occurs when Spark does not have an option for reading footer information from an input file. See <https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameWriter.html#csv-java.lang.String-> for more information.

Perform the following steps to work around this issue:

1. Create a new PDI transformation containing either the Hadoop File Input and Hadoop File Output steps or the Text File Input and Text File Output steps.
2. Use the footer option in the **Content** tab of the Hadoop File Input or Text File Input step to specify your footer data. See the **Pentaho Data Integration** document for details on the **Content** tab.
3. Verify the **Footer** option in the **Content** tab of the Hadoop File Output or Text File Output step has been cleared so the data is not written out as a footer. See the **Pentaho Data Integration** document for details on the **Content** tab.
4. Save the transformation and run it on the Pentaho engine. See the **Pentaho Data Integration** document for instructions

You can now read the file resulting from the output step in either Spark or AEL.
