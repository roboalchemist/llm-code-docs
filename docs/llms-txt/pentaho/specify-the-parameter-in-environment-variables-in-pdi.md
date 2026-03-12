# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-environment-variables-in-pdi.md

# Specify the parameter as an environment variable in PDI

Perform the following steps to specify the parameter in PDI using an environment variable.

1. From the **Edit** menu, select **Set Environment Variables**.

   The **Set Environment Variables** table appears.
2. Enter the following information:
   1. In the **Name** column, type `spark.hadoop.validateOutputSpecs`.
   2. In the **Value** column, type `false`.
3. Click **OK** to activate the parameter.

   You can verify it is active in the transformation logging.

For more information about processing Spark parameters, see the **Administer Pentaho Data Integration and Analytics** document.
