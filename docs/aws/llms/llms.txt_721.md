# Source: https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/llms.txt

# The lakehouse architecture of Amazon SageMaker User Guide

> Unify data access across Amazon S3 data lakes, Amazon Redshift data warehouses, and third-party and federated data sources with the lakehouse architecture of Amazon SageMaker

- [Document history](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/doc-history.html)

## [What is the lakehouse architecture of Amazon SageMaker?](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.html)

- [Key components](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-components.html): Learn about the lakehouse architecture of Amazon SageMaker key components such as catalogs, databases, tables/views, and storage.
- [How it works](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-how.html): Learn how the lakehouse architecture works.
- [Data connections](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.html): Learn about data connections in the lakehouse architecture.
- [Support for the Apache Iceberg open standard](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-iceberg.html): The lakehouse architecture provides support for Apache Iceberg, enabling organizations to unify data across Amazon S3 data lakes and Amazon Redshift data warehouses while building powerful analytics and AI/ML applications on a unified data layer.


## [Getting started](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-get-started.html)

### [Adding data sources](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-add-data.html)

Learn about adding data sources in lakehouse architecture.

- [Create new connection](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-create-connection.html): Learn how to create connections in lakehouse architecture.
- [Upload data](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-upload-data.html): Learn how to upload data in the lakehouse architecture.
- [Create a catalog](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-create-catalog.html): Learn how to create a catalog in the lakehouse architecture.
- [Add existing databases and catalogs](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-add-catalog.html): Learn how to add existing databases and catalogs using AWS Lake Formation permissions in the lakehouse architecture.
- [Creating AWS Glue databases via Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-add-new-database.html): Learn how to create new AWS Glue databases via Amazon SageMaker Unified Studio.
- [Deleting AWS Glue databases via Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-delete-new-database.html): Learn how to delete databases.
- [Amazon S3 tables integration](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-s3-tables-integration.html): Learn how to integrate Amazon S3 tables.
- [Publishing data](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-publish.html): After you have added data in the lakehouse architecture, you can publish the data to share it with other users in the lakehouse architecture.


## [Onboarding data](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/onboarding-data-sagemaker-lakehouse.html)

- [Prerequisites](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/prerequisites-s3-tables.html): Review the requirements and setup steps needed before onboarding data into the lakehouse architecture.
- [Working with Amazon S3 Tables](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/s3-tables-integration.html): Analyze the data in the lakehouse architecture of Amazon SageMaker with Amazon S3 Tables.

### [Amazon Redshift Managed Storage](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/rms-integration.html)

Learn how to integrate Amazon Redshift Managed Storage with the lakehouse architecture of Amazon SageMaker for unified data warehouse and data lake querying.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/redshift-managed-catalog-prereqs.html): This section covers the prerequisites needed to manage Amazon Redshift managed storage catalogs within the AWS Glue Data Catalog using Lake Formation permissions.
- [Amazon S3 data lakes](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/s3-data-lakes.html): Discover how to leverage Amazon S3 as the foundational storage layer for scalable, durable data lake capabilities in the lakehouse architecture.
- [Federated catalogs](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/federated-catalogs.html): Explore how to establish secure federated catalogs to external data sources for unified querying without data duplication.


## [Share your data](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/sharing-data-smlh.html)

### [Configure cross-account access with Redshift](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/configure-cross-account-access.html)

Set up secure cross-account access for multi-catalog tables and run join queries using Spark.

- [Configure account A](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/producer-account-setup.html): Configure account A for secure cross-account data sharing workflows.
- [Configure account B](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/consumer-account-setup.html): Configure account B for cross-account data sharing by accepting AWS RAM shares, creating resource links to shared catalogs and tables, and setting up permissions for AWS Glue execution roles.
- [Run a PySpark job in AWS Glue 5.0](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/run-pyspark-job.html): Execute a cross-account join query using AWS Glue 5.0 Spark.
