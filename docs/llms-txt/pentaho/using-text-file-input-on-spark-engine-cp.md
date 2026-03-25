# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/select-an-engine-text-file-input/using-text-file-input-on-spark-engine-cp.md

# Using the Text File Input step on the Spark engine

You can set up the Text file input step to run on the Spark engine. Spark processes null values differently than the Pentaho engine, so you may need to adjust your transformation to process null values following Spark's processing rules.

**Note:** If you are using this step to extract data from [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html), browse to the URI of the S3 system or specify the **Uri field** option in the **Additional output fields** tab. S3 and S3n are supported.

If you are running your transformation on the Spark engine, use the following instructions to set up the Text File Input step.
