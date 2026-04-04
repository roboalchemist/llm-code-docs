# Source: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/llms.txt

# Amazon EMR Amazon EMR Serverless User Guide

> With Amazon EMR, you can run big data analytics applications on the Amazon Web Services Cloud using open source frameworks while letting Amazon EMR Serverless configure, optimize, secure, and manage clusters for you. Use this guide together with the Amazon EMR Serverless API Reference.

- [What is Amazon EMR Serverless?](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)
- [Prerequisites for getting started](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/setting-up.html)
- [Uploading data](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/upload-data.html)
- [Endpoints and quotas](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/endpoints-quotas.html)
- [Other considerations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/considerations.html)
- [Document history](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)

- [Getting started from the console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/gs-console.html): Getting started by creating an application in the EMR Serverless console, submitting a job run or interactive workload, and viewing the application and logs.
- [Getting started from the AWS CLI](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/gs-cli.html): Get started with EMR Serverless from the AWS CLI with commands to create an application, run jobs, check job run output, and delete your resources.


## [Interact with and configure an EMR Serverless application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/applications.html)

### [Using the EMR Studio console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/studio.html)

How to use the EMR Studio console to create an EMR Serverless application, list EMR Serverless applications, and manage your EMR Serverless applications.

- [List applications from the EMR Studio console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/studio-list-app.html): You can access all existing EMR Serverless applications from the List applications page.
- [Manage applications from the EMR Studio console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/studio-manage-app.html): You can perform the following actions on an application from either the List applications page or from a specific applicationâs Details page.
- [Using the AWS CLI](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/applications-cli.html): The various commands available to use with EMR Serverless applications on the AWS CLI.

### [Configuring an application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/application-capacity.html)

EMR Serverless options during application creation.

- [Application behavior](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/app-behavior.html): Understanding default application behavior, as well as maximum capacity and worker configurations for configuration of an application with EMR Serverless.
- [Pre-initialized capacity for working with an application in EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/pre-init-capacity.html): EMR Serverless provides an optional feature that keeps driver and workers pre-initialized.
- [Default app configuration](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/default-configs.html): Specify a common set of runtime and monitoring configurations at the application level for all EMR Serverless jobs submitted under the same application.
- [Customizing an image](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/application-custom-image.html): How to customize an EMR Serverless image on an application.
- [Configuring VPC access for EMR Serverless applications to connect to data](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/vpc-access.html): How to configure VPC access for your application.
- [Architecture options](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/architecture.html): The architecture determines the type of processors that your application uses.
- [Job concurrency and queuing](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/applications-concurrency-queuing.html): Job concurrency and queuing for an application.


## [Running jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs.html)

- [Job run states](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/job-states.html): The different possible states of a EMR Serverless job run.
- [Job run cancellation with grace period](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/job-cancellation-grace-period.html): In data processing systems, abrupt terminations can lead to resource waste, incomplete operations, and potential data inconsistencies.
- [Using the EMR Studio console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-studio.html): How to submit an EMR Serverless job in EMR Studio
- [Using the AWS CLI](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-cli.html): Commands for EMR Serverless job runs on the AWS CLI.
- [Execution IAM policy](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-cli-execution.html): You can specify an Execution IAM Policy, in addition to an Execution Role, when submitting job runs on EMR Serverless.
- [Using shuffle-optimized disks](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-shuffle-optimized-disks.html): With Amazon EMR use shuffle-optimized disks when you run Apache Spark or Hive jobs to improve performance for I/O-intensive workloads.
- [Using serverless storage](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-serverless-storage.html): [abstract text]

### [Streaming jobs for processing continuously streamed data](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-streaming.html)

A streaming job in EMR Serverless is a job mode that lets you analyze and process streaming data in near real-time, and automatically provides job-resiliency.

- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark-streaming-getting-started.html): Instructions for getting started streaming jobs with Amazon EMR Serverless applications.
- [Streaming connectors](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark-streaming-connectors.html): Supported streaming connectors for Amazon EMR Serverless are Amazon Kinesis Data Streams
- [Log management](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark-streaming-log-management.html): Streaming jobs support log rotation for Spark application logs and event logs, and log compaction for Spark event logs whenever managed logging is available.
- [Using Spark configurations when you run EMR Serverless jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark.html): How to use Spark-specific configurations when you run EMR Serverless jobs.
- [Using Hive configurations when you run EMR Serverless jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-hive.html): How to use Hive-specific job parameters, runtime roles, job driver parameters, configurations, and properties when you run EMR Serverless jobs.
- [Job resiliency](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-resiliency.html): How to enable and set the retry policy, as well as monitoring and logging jobs, and setting up batch jobs for job resiliency on EMR Serverless.

### [Metastore configuration for EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/metastore-config.html)

Store structural information about tables, schemas, partition names, and data types by configuring AWS Glue Data Catalog metastore or using a Hive metastore.

- [Using an external Hive metastore](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/external-metastore.html): You can configure your EMR Serverless Spark and Hive jobs to connect to an external Hive metastore, such as Amazon Aurora or Amazon RDS for MySQL.
- [Working with AWS Glue multi-catalog hierarchy on EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/external-metastore-glue-multi.html): You can configure your EMR Serverless applications to work with the AWS Glue multi-catalog hierarchy.
- [Considerations when using an external metastore](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/external-metastore-considerations.html)
- [Cross-account S3 access](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-s3-access.html): How to set up cross-account S3 access for Amazon EMR Serverless to access Amazon S3 data using a bucket policy, assumed role, or multiple assumed roles.
- [Troubleshooting errors](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-troubleshoot.html): How to troubleshoot errors to diagnose and fix common issues that occur when running EMR Serverless jobs.
- [Job Level Cost Allocation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-job-level-cost-allocation.html): How to enable and configure job-level cost allocation for granular billing attribution in EMR Serverless.


## [Running interactive workloads](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads.html)

- [Running interactive workloads through Apache Livy endpoint](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads-livy-endpoints.html): Create and enable an Apache Livy endpoint and an EMR Serverless application to run interactive workloads through your self-hosted notebooks or a custom client.


## [Logging and monitoring](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging-monitoring.html)

- [Storing logs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html): How to set up logging for EMR Serverless jobs runs.
- [Rotating logs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/rotating-logs.html): EMR Serverless can rotate Spark application logs and event logs.
- [Encrypting logs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-log-encryption.html): How to encrypt EMR Serverless logs with managed storage, with Amazon S3 buckets, and with Amazon CloudWatch.
- [Configuring Log4j2](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/log4j2.html): Configure custom Log4j2 logging properties for EMR Serverless jobs.

### [Monitoring](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/metrics.html)

How to monitor applications and jobs.

- [Applications and jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/app-job-metrics.html): With Amazon CloudWatch metrics for EMR Serverless, you can receive 1-minute CloudWatch metrics and access CloudWatch dashboards to access near-real-time operations and performance of your EMR Serverless applications.
- [Spark engine metrics](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/monitor-with-prometheus.html): You can use EMR Serverless with Amazon Managed Service for Prometheus to collect Apache Spark metrics for EMR Serverless jobs and applications.
- [Usage metrics](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/monitoring-usage.html): Use Amazon CloudWatch usage metrics to provide visibility into the resources that your Amazon EMR Serverless account uses.
- [Automating with EventBridge](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-eventbridge.html): Use Amazon EventBridge to automate your AWS services and respond automatically to system events, such as application availability issues or resource changes.


## [Tagging resources](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tagging.html)

- [What is a tag?](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tag-basics.html): A tag is a label that you assign to an AWS resource.
- [Tagging resources](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tagging-resources.html): You can tag new or existing applications and job runs.
- [Tagging limitations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tagging-restrictions.html): The basic tagging limitations for keys and values including minimum and maximum length, allowed characters, case sensitivity and maximum number of tags.
- [Working with tags](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-tags.html): Use the following AWS CLI commands or Amazon EMR Serverless API operations to add, update, list, and delete the tags for your resources.


## [Tutorials](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tutorials.html)

- [Using Java 17](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-java-runtime.html): Configure EMR Serverless Spark jobs to use Java 17 runtime.
- [Using Hudi](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-hudi.html): This section describes using Apache Hudi with EMR Serverless applications.
- [Using Iceberg](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-iceberg.html): This section describes how to use Apache Iceberg with EMR Serverless applications.
- [Using Python libraries](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-python-libraries.html): When you run PySpark jobs on Amazon EMR Serverless applications, package various Python libraries as dependencies.
- [Using different Python versions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-python.html): In addition to the use case in , you can also use Python virtual environments to work with different Python versions than the version packaged in the Amazon EMR release for your Amazon EMR Serverless application.
- [Using Delta Lake OSS](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-delta-lake.html)
- [Submitting jobs from Airflow](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-airflow.html): The Amazon Provider in Apache Airflow provides EMR Serverless operators.
- [Using Hive user-defined functions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-hive-udf.html): Hive user-defined functions (UDFs) let you create custom functions to process records or groups of records.

### [Using custom images](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-custom-images.html)

- [Licensing information for using custom images](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/concepts-licensing-images.html): You can build custom images with EMR Serverless to perform specific tasks or to use specific versions of a software package.

### [Using Spark on Amazon Redshift](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-spark-redshift.html)

With Amazon EMR release 6.9.0 and later, every release image includes a connector between Apache Spark and Amazon Redshift.

- [Launch a Spark application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-spark-redshift-launch.html): To use the integration with EMR Serverless 6.9.0, pass the required Spark-Redshift dependencies with your Spark job.
- [Authenticate to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-spark-redshift-auth.html)
- [Read and write to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-spark-redshift-readwrite.html): The following code examples use PySpark to read and write sample data from and to an Amazon Redshift database with a data source API and with SparkSQL.
- [Considerations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-spark-redshift-considerations.html)

### [Connecting to DynamoDB](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-ddb-connector.html)

In this tutorial, you upload a subset of data from the United States Board on Geographic Names to an Amazon S3 bucket and then use Hive or Spark on Amazon EMR Serverless to copy the data to an Amazon DynamoDB table for querying.

- [Setting up cross-account access](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-ddb-connector-xaccount.html): To set up cross-account access for EMR Serverless, complete the following steps.
- [Considerations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-ddb-connector-considerations.html): Note these behaviors and limitations when you use the DynamoDB connector with Apache Spark or Apache Hive.


## [Security](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security.html)

- [Security best practices](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-best-practices.html): How to configure security features to protect your data on EMR Serverless.
- [Data protection](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/data-protection.html): How to protect data in your EMR Serverless application.

### [Identity and Access Management (IAM)](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security_iam_service-with-iam.html)

How to authenticate requests and manage access to your EMR Serverless resources.

- [How EMR Serverless works with IAM](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-serverless.html): How to set up IAM when using EMR Serverless.
- [Using service-linked roles](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-service-linked-roles.html): How to use service-linked roles to give EMR Serverless access to resources in your AWS account.
- [Job runtime roles for Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.html): How to set up job runtime roles.
- [User access policies](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-user-access-policies.html): How to configure IAM policies for full and read-only access.
- [Policies for tag-based access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-TBAC.html): How to set up EMR Serverless policies for tag-based access control.
- [Identity-based policies](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-id-based-policy-examples.html): How to set up identity-based policies for EMR Serverless.
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon EMR Serverless and IAM.

### [Trusted Identity Propagation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.html)

Trusted Identity Propagation

- [Getting started with Trusted-Identity Propagation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-getting-started.html): This section helps you configure EMR-Serverless application with Apache Livy Endpoint to integrate with AWS IAM Identity Center and enable Trusted identity propagation.
- [Trusted Identity Propagation for interactive workloads](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-interactive-workloads.html): The steps to propagate identity to interactive workloads through an Apache Livy endpoint depend on whether your users interact with AWS managed development environment like Amazon SageMaker AI or your own self-hosted Notebook environment as client-facing application.
- [User background sessions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-user-background.html): User background sessions enable long-running analytics and machine learning flows to continue even after the user has logged off from their notebook interface.
- [Considerations for EMR Serverless Trusted-Identity-Propagation integration](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-considerations-limitations.html): Consider the following when you use IAM Identity Center Trusted-Identity-Propagation with EMR Serverelss Application:

### [Using Lake Formation with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-section.html)

You can configure EMR Serverless applications to use Lake Formation with either full table access or fine-grained access control.

- [Lake Formation full table access for EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.html): Learn how to use AWS Lake Formation with full table permissions in Amazon EMR releases 7.8.0 and higher without fine-grained access control limitations.

### [Lake Formation for FGAC](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.html)

You can use Lake Formation with Amazon EMR Serverless to apply fine grained access controls on Data Catalog tables.

- [Debugging jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable-debugging.html)
- [Working with Glue Data Catalog views](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/SECTION-jobs-glue-data-catalog-views.html): You can create and manage views in the AWS Glue Data Catalog for use with EMR Serverless.
- [Open-table format support](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable-open-table-format-support.html): EMR Serverless supports SELECT queries on Apache Hive, Apache Iceberg, Delta Lake (7.6.0+), and Apache Hudi (7.6.0+).
- [Considerations and limitations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.html)
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-troubleshooting.html): See the following sections for troubleshooting solutions.
- [Spark native fine-grained access control alllowlisted PySpark API](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/clean-rooms-spark-fgac-pyspark-api-allowlist.html): Reference document and searchable list for supported PySpark function use within Amazon EMR Spark FGAC
- [Inter-worker encryption](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interworker-encryption.html): With Amazon EMR versions 6.15.0 and higher, enable mutual-TLS encrypted communication between workers in your Spark job runs.
- [Disk Encryption with KMS CMK](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/disk-encryption-cmk.html): EMR Serverless encrypts all disks attached to workers by default using service-owned encryption keys.
- [Secrets Manager for data protection](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/secrets-manager.html): Learn about using AWS Secrets Manager with EMR Serverless to protect database credentials, API keys, and other secret information.
- [S3 Access Grants for data access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/access-grants.html): Launch an EMR Serverless application with S3 Access Grants for data access management.
- [CloudTrail for logging](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging-using-cloudtrail.html): Learn about logging Amazon EMR Serverless with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EMR Serverless features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/infrastructure-security.html): Learn how Amazon EMR Serverless isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/configuration-vulnerability.html): How AWS handles security configuration and vulnerability analysis.


## [Release versions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-versions.html)

- [AWS runtime for Apache Spark (emr-spark-8.0-preview)](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-emr-spark-8.0-preview.html): The following table lists the application versions available with AWS runtime for Apache Spark (emr-spark-8.0-preview).
- [EMR Serverless 7.12.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-7120.html): The following table lists the application versions available with EMR Serverless 7.12.0.
- [EMR Serverless 7.11.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-7110.html): The following table lists the application versions available with EMR Serverless 7.11.0.
- [EMR Serverless 7.10.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-7100.html): The following table lists the application versions available with EMR Serverless 7.10.0.
- [EMR Serverless 7.9.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-790.html): The following table lists the application versions available with EMR Serverless 7.9.0.
- [EMR Serverless 7.8.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-780.html): The following table lists the application versions available with EMR Serverless 7.8.0.
- [EMR Serverless 7.7.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-770.html): The following table lists the application versions available with EMR Serverless 7.7.0.
- [EMR Serverless 7.6.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-760.html): The following table lists the application versions available with EMR Serverless 7.6.0.
- [EMR Serverless 7.5.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-750.html): The following table lists the application versions available with EMR Serverless 7.5.0.
- [EMR Serverless 7.4.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-740.html): The following table lists the application versions available with EMR Serverless 7.4.0.
- [EMR Serverless 7.3.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-730.html): The following table lists the application versions available with EMR Serverless 7.3.0.
- [EMR Serverless 7.2.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-720.html): The following table lists the application versions available with EMR Serverless 7.2.0.
- [EMR Serverless 7.1.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-710.html): The following table lists the application versions available with EMR Serverless 7.1.0.
- [EMR Serverless 7.0.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-700.html): The following table lists the application versions available with EMR Serverless 7.0.0.
- [EMR Serverless 6.15.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6150.html): The following table lists the application versions available with EMR Serverless 6.15.0.
- [EMR Serverless 6.14.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6140.html): The following table lists the application versions available with EMR Serverless 6.14.0.
- [EMR Serverless 6.13.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6130.html): The following table lists the application versions available with EMR Serverless 6.13.0.
- [EMR Serverless 6.12.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6120.html): The following table lists the application versions available with EMR Serverless 6.12.0.
- [EMR Serverless 6.11.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6110.html): The following table lists the application versions available with EMR Serverless 6.11.0.
- [EMR Serverless 6.10.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6100.html): The following table lists the application versions available with EMR Serverless 6.10.0.
- [EMR Serverless 6.9.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-690.html): The following table lists the application versions available with EMR Serverless 6.9.0.
- [EMR Serverless 6.8.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-680.html): The following table lists the application versions available with EMR Serverless 6.8.0.
- [EMR Serverless 6.7.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-670.html): The following table lists the application versions available with EMR Serverless 6.7.0.
- [EMR Serverless 6.6.0](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-660.html): The following table lists the application versions available with EMR Serverless 6.6.0.
