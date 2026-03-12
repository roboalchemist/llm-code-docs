# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21.md

# Using HBase steps with Amazon EMR 5.21

To use the HBase Input and HBase Output steps with EMR 5.21, you must add the following parameter:

```
spark.hadoop.validateOutputSpecs=false
```

You can use any of these methods to set the parameter:

* [Specify the parameter in the properties file](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-the-application.properties-file)
* [Specify the parameter in Transformation properties](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-the-transformations-properties-in-pdi)
* [Specify the parameter as an environment variable in PDI](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark/using-hbase-steps-with-amazon-emr-5.21/specify-the-parameter-in-environment-variables-in-pdi)

For more information about the properties file and processing Spark parameters, see the **Administer Pentaho Data Integration and Analytics** document.
