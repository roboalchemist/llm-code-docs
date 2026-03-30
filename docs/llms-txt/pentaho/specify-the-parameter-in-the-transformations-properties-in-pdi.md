# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-the-transformations-properties-in-pdi.md

# Specify the parameter in Transformation properties

Perform the following steps to specify the parameter in PDI using the **Transformation properties** dialog box.

1. Double-click anywhere on the transformation canvas.

   The **Transformation properties** dialog box appears.
2. Click the **Parameters** tab and enter the following information:
   1. In the **Parameter** column, type `spark.hadoop.validateOutputSpecs`.
   2. In the **Default Value** column, type `false`.
   3. (Optional) Add a descriptive note about why the parameter is included.
3. Click **OK** to activate the parameter.

   You can verify it is active in the transformation logging.

For more information about processing Spark parameters, see the **Administer Pentaho Data Integration and Analytics** document.
