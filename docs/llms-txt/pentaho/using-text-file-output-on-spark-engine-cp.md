# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp/select-an-engine-text-file-output/using-text-file-output-on-spark-engine-cp.md

# Using the Text File Output step on the Spark engine

You can set up the Text file output step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules.

**Note:** If you are using this step to write data to [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html), specify the URI of the S3 system through the **Filename** option in the **File** tab. For details, see the [File tab](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/File%20tab%20\(Text%20File%20Output\)%20\(Spark\).md).
