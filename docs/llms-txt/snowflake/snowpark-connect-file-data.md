# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-file-data.md

# Access to cloud service file data with Snowpark Connect for Spark

With Snowpark Connect for Spark, you can interact directly with external cloud storage systems such as Amazon S3, Google Cloud Storage, and Azure Blob.
You can read data from cloud storage into Snowflake, process the data, then write it back.

For example, you might want to use Snowpark Connect for Spark to perform the following tasks:

* Ingest raw data.

  Land files (for example, CSV, JSON, and Parquet) in S3, Google Cloud, or Azure before moving them into Snowflake.
* Export data for downstream use.

  Write processed Snowpark DataFrames back to cloud storage for ML training, sharing with external partners, or further Spark-based
  analytics.
* Create hybrid pipelines.

  Keep part of the pipeline in Snowflake while maintaining compatibility with existing data lakes.
* Comply with regulations or reduce costs.

  Store specific datasets externally due to regulations, governance, or budget constraints.

Use the steps listed in this topic to read from and write to files stored on these cloud service providers. You can access files using
either Snowflake external stages or direct access.

## Caveats

When using Snowpark Connect for Spark to work with cloud services, keep in mind the following caveats:

* Authentication—Snowpark Connect for Spark does not automatically manage cloud credentials. You must configure access keys (AWS), storage account
  keys or SAS tokens (Azure), or maintain external stages by yourself. Expired or missing credentials will result in read/write failures.
* Performance—Cloud I/O depends on network bandwidth and object store latency. Reading many small files can significantly impact performance.
* Format support—Ensure that the file formats you’re reading and writing are supported. Currently Snowpark Connect for Spark has parity with common
  formats, including TEXT, CSV, JSON, and Parquet. However, advanced features (such as Parquet partition discovery and JSON schema evolution)
  may differ from Spark.
* Permissions and policies—Writing to cloud buckets requires proper IAM/ACL policies. You might encounter an AccessDenied error if
  policies aren’t aligned between Snowflake roles and cloud credentials.

## Best Practices

To get the most reliable integration that performs well, follow these best practices:

* Use secure, temporary credentials and rotate credentials frequently.
* Partition and bucket data.

  When writing Parquet, partition on frequently filtered columns to reduce scan costs. Use fewer, larger files (for example, at 100MB to
  500MB each) instead of many small files.
* Validate schema on write.

  Always define the schema explicitly, especially for semi-structured formats such as JSON and CSV. This prevents drift between
  Snowflake and external data.
* Monitor costs.

  Consider consolidating files and filtering data before writing to reduce costs. Cloud provider costs are accrued per request and per byte scanned.
* Standardize API calls.

  Follow the documented guidance precisely when using functionality and parameters, avoiding ad-hoc variations. In this way, you can
  maintain compatibility, prevent regressions, and ensure expected behavior across different cloud providers.

## Access using Snowflake external stages

AWSAzureGoogle Cloud

1. [Configure secure access to Amazon S3](../../user-guide/data-load-s3-config.md) to create an external stage that points to your
   S3 location.
2. Read from your external stage.

   ```python
   # Read CSV
   spark.read.csv('@<your external stage name>/<file path>')
   spark.read.option("header", True).csv('@<your external stage name>/<file path>') # read with header in file

   # Write to CSV
   df.write.csv('@<your external stage name>/<file path>')
   df.write.option("header", True).csv('@<your external stage name>/<file path>') # write with header in file

   # Read Text
   spark.read.text('@<your external stage name>/<file path>')

   # Write to Text
   df.write.text('@<your external stage name>/<file path>')
   df.write.format("text").mode("overwrite").save('@<your external stage name>/<file path>')

   # Read Parquet
   spark.read.parquet('@<your external stage name>/<file path>')

   # Write to Parquet
   df.write.parquet('@<your external stage name>/<file path>')

   # Read JSON
   spark.read.json('@<your external stage name>/<file path>')

   # Write to JSON
   df.write.json('@<your external stage name>/<file path>')
   ```

3. [Configure secure access to Azure](../../user-guide/data-load-azure-create-stage.md) to create an external stage that points to your
   Azure container.
4. Read from your external stage.

   ```python
   # Read CSV
   spark.read.csv('@<your external stage name>/<file path>')
   spark.read.option("header", True).csv('@<your external stage name>/<file path>')
   # read with header in file

   # Write to CSV
   df.write.csv('@<your external stage name>/<file path>')
   df.write.option("header", True).csv('@<your external stage name>/<file path>') # write with header in file

   # Read Text
   spark.read.text('@<your external stage name>/<file path>')

   # Write to Text
   df.write.text('@<your external stage name>/<file path>')
   df.write.format("text").mode("overwrite").save('@<your external stage name>/<file path>')

   # Read Parquet
   spark.read.parquet('@<your external stage name>/<file path>')

   # Write to Parquet
   df.write.parquet('@<your external stage name>/<file path>')

   # Read JSON
   spark.read.json('@<your external stage name>/<file path>')

   # Write to JSON
   df.write.json('@<your external stage name>/<file path>')
   ```

5. [Configure secure access to Google Cloud](../../user-guide/data-load-gcs-config.md) to create an external stage that points to your
   Google Cloud Storage bucket.
6. Read from your external stage.

   ```python
   # Read CSV
   spark.read.csv('@<your external stage name>/<file path>')
   spark.read.option("header", True).csv('@<your external stage name>/<file path>') # read with header in file

   # Write to CSV
   df.write.csv('@<your external stage name>/<file path>')
   df.write.option("header", True).csv('@<your external stage name>/<file path>') # write with header in file

   # Read Text
   spark.read.text('@<your external stage name>/<file path>')

   # Write to Text
   df.write.text('@<your external stage name>/<file path>')
   df.write.format("text").mode("overwrite").save('@<your external stage name>/<file path>')

   # Read Parquet
   spark.read.parquet('@<your external stage name>/<file path>')

   # Write to Parquet
   df.write.parquet('@<your external stage name>/<file path>')

   # Read JSON
   spark.read.json('@<your external stage name>/<file path>')

   # Write to JSON
   df.write.json('@<your external stage name>/<file path>')
   ```

## Access using direct access

You can access files directly on cloud service providers using the steps and code described here.

AWSAzure

1. Set the Spark configuration with AWS credentials.

   ```python
   # For S3 related access with public/private buckets, please add these config change
   spark.conf.set("spark.hadoop.fs.s3a.connection.ssl.enabled","false")
   spark.conf.set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
   spark.conf.set("spark.jars.packages","org.apache.hadoop:hadoop-aws:3.3.2")

   # For private S3 access, please also provide credentials
   spark.conf.set("spark.hadoop.fs.s3a.access.key","<AWS_ACCESS_KEY_ID>")
   spark.conf.set("spark.hadoop.fs.s3a.secret.key","<AWS_SECRET_ACCESS_KEY>")
   spark.conf.set("spark.hadoop.fs.s3a.session.token","<AWS_SESSION_TOKEN>")
   ```

2. Read and write directly with S3.

   ```python
   # Read CSV
   spark.read.csv('s3a://<bucket name>/<file path>')
   spark.read.option("header", True).csv('s3a://<bucket name>/<file path>') # read with header in file

   # Write to CSV
   df.write.csv('s3a://<bucket name>/<file path>')
   df.write.option("header", True).csv('s3a://<bucket name>/<file path>') # write with header in file

   # Read Text
   spark.read.text('s3a://<bucket name>/<file path>')

   # Write to Text
   df.write.text('s3a://<bucket name>/<file path>')
   df.write.format("text").mode("overwrite").save('s3a://<bucket name>/<file path>')

   # Read Parquet
   spark.read.parquet('s3a://<bucket name>/<file path>')

   # Write to Parquet
   df.write.parquet('s3a://<bucket name>/<file path>')

   # Read JSON
   spark.read.json('s3a://<bucket name>/<file path>')

   # Write to JSON
   df.write.json('s3a://<bucket name>/<file path>')
   ```

3. Set the Spark configuration with Azure credentials.

   ```python
   # For private Azure access, please also provide blob SAS token
   #   * Make sure all required permissions are in place before proceeding
   spark.conf.set("fs.azure.sas.fixed.token.<storage-account>.dfs.core.windows.net","<Shared Access Token>")
   ```
4. Read and write directly with Azure.

   ```python
   # Read CSV
   spark.read.csv('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')
   spark.read.option("header", True).csv('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>') # read with header in file

   # Write to CSV
   df.write.csv('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')
   df.write.option("header", True).csv('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>') # write with header in file

   # Read Text
   spark.read.text('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')

   # Write to Text
   df.write.text('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')
   df.write.format("text").mode("overwrite").save('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')

   # Read Parquet
   spark.read.parquet('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')

   # Write to Parquet
   df.write.parquet('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')

   # Read JSON
   spark.read.json('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')

   # Write to JSON
   df.write.json('wasbs://<container name>@<storage account name>.blob.core.windows.net/<bucket name>/<file path>')
   ```
