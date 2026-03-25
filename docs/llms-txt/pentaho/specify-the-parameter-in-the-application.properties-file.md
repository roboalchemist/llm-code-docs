# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-the-application.properties-file.md

# Specify the parameter in the properties file

Perform the following steps to edit the `application.properties` file.

1. Navigate to the `design-tools/data-integration/adaptive-execution/config` folder and open the `application.properties` file with any text editor.
2. Find the section labeled as `#Base Configuration`.
3. Add the following parameter:

   `spark.hadoop.validateOutputSpecs=false`
4. Save and close the file.

For more information about the `application.properties` file, see the **Administer Pentaho Data Integration and Analytics** document.
