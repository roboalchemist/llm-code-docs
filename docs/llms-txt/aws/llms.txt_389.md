# Source: https://docs.aws.amazon.com/firehose/latest/dev/llms.txt

# Amazon Data Firehose Developer Guide

> This is official Amazon Web Services (AWS) documentation for Amazon Data Firehose. Amazon Data Firehose is the easiest way to load streaming data into AWS. It can capture, transform, and load streaming data into Amazon Managed Service for Apache Flink, Amazon Simple Storage Service (Amazon S3), Amazon Redshift, and Amazon OpenSearch Service, enabling near real-time analytics with existing business intelligence tools and dashboards youâre already using today. Amazon Data Firehose is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. This guide provides a conceptual overview of Amazon Data Firehose and includes detailed instructions for using the service.

- [Complete prerequisites to set up Firehose](https://docs.aws.amazon.com/firehose/latest/dev/before-you-begin.html)
- [Test your Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/test-drive-firehose.html)
- [Quota](https://docs.aws.amazon.com/firehose/latest/dev/limits.html)
- [Document history](https://docs.aws.amazon.com/firehose/latest/dev/history.html)

## [What is Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/firehose/latest/dev/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Tutorial: Create a Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html)

- [Choose source and destination for your Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/create-name.html): Learn how to configure the source and destination for your Firehose stream.

### [Configure source settings](https://docs.aws.amazon.com/firehose/latest/dev/configure-source.html)

Learn how to configure the source to send data to your Firehose stream.

- [Configure source settings for Amazon MSK](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-msk.html): When you choose Amazon MSK to send information to a Firehose stream, you can choose between MSK provisioned and MSK-Serverless clusters.
- [Configure source settings for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-kinesis-streams.html): Configure the source settings for Amazon Kinesis Data Streams to send information to a Firehose stream as following.
- [(Optional) Configure record transformation and format conversion](https://docs.aws.amazon.com/firehose/latest/dev/create-transform.html): Learn how you can transform and convert your record data for record processing in a Firehose stream.
- [Configure destination settings](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html): Learn how to configure the destination settings for your Firehose stream based on different destinations.
- [Configure backup settings](https://docs.aws.amazon.com/firehose/latest/dev/create-configure-backup.html): Learn how to configure the S3 backup settings for your Firehose stream.
- [Configure advanced settings](https://docs.aws.amazon.com/firehose/latest/dev/create-configure-advanced.html): Learn how to log errors error and configure server side encryption, permissions, and tags for your Firehose stream.


## [Send data to a Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html)

### [Configure Kinesis agent to send data](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html)

Learn how to use Amazon Data Firehose agents to deliver your data in a reliable, timely, and simple manner to Firehose streams.

- [Manage AWS credentials](https://docs.aws.amazon.com/firehose/latest/dev/agent-credentials.html): Manage your AWS credentials using one of the following methods:
- [Create custom credential providers](https://docs.aws.amazon.com/firehose/latest/dev/custom-cred-provider.html): You can create a custom credentials provider and give its class name and jar path to the Kinesis agent in the following configuration settings: userDefinedCredentialsProvider.classname and userDefinedCredentialsProvider.location.
- [Download and install the Agent](https://docs.aws.amazon.com/firehose/latest/dev/download-install.html): First, connect to your instance.
- [Configure and start the Agent](https://docs.aws.amazon.com/firehose/latest/dev/config-start.html)
- [Specify agent configuration settings](https://docs.aws.amazon.com/firehose/latest/dev/agent-config-settings.html): The agent supports two mandatory configuration settings, filePattern and deliveryStream, plus optional configuration settings for additional features.
- [Configure multiple file directories and streams](https://docs.aws.amazon.com/firehose/latest/dev/sim-writes.html): By specifying multiple flow configuration settings, you can configure the agent to monitor multiple file directories and send data to multiple streams.
- [Pre-process data with Agents](https://docs.aws.amazon.com/firehose/latest/dev/pre-processing.html): The agent can pre-process the records parsed from monitored files before sending them to your Firehose stream.
- [Use common Agent CLI commands](https://docs.aws.amazon.com/firehose/latest/dev/cli-commands.html): The following table provides a set of common use cases and corresponding commands for working with the AWS Kinesis agent.
- [Troubleshoot issues when sending from Kinesis Agent](https://docs.aws.amazon.com/firehose/latest/dev/agent-faq.html): This table provides troubleshooting information and solutions for common issues faced when using the Amazon Kinesis Agent.
- [Send data with AWS SDK](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-sdk.html): Learn how to use AWS SDK to deliver your data in a reliable, timely, and simple manner to Firehose streams.

### [Send CloudWatch Logs to Firehose](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html)

Learn how to use CloudWatch Logs to deliver your data in a reliable, timely, and simple manner to Firehose streams.

- [Decompress CloudWatch Logs](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs-decompression.html): If you are using Firehose to deliver CloudWatch Logs and want to deliver decompressed data to your Firehose stream destination, use Firehose Data Format Conversion (Parquet, ORC) or Dynamic partitioning.
- [Extract message after decompression of CloudWatch Logs](https://docs.aws.amazon.com/firehose/latest/dev/Message_extraction.html): When you enable decompression, you have the option to also enable message extraction.
- [Enable decompression on a new Firehose stream from console](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs-decompression-enabling-console.html)
- [Enable decompression on an existing Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/enabling-decompression-existing-stream-console.html): This section provides instructions for enabling decompression on existing Firehose streams.
- [Disable decompression on Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs-decompression-disabling-console.html)
- [Troubleshoot decompression in Firehose](https://docs.aws.amazon.com/firehose/latest/dev/decomp-faq.html): The following table shows how Firehose handles errors during data decompression and processing, including delivering records to an error S3 bucket, logging errors, and emitting metrics.
- [Send CloudWatch Events to Firehose](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-events.html): Learn how to use CloudWatch Logs events to deliver your data in a reliable, timely, and simple manner to Firehose streams.
- [Configure AWS IoT to send data to Firehose](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-iot.html): Learn how to use AWS IoT events to deliver your data in a reliable, timely, and simple manner to Firehose streams.


## [Transform source data](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)

- [Required parameters for data transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation-status-model.html): All transformed records from Lambda must contain the following parameters, or Amazon Data Firehose rejects them and treats that as a data transformation failure.
- [Supported Lambda blueprints](https://docs.aws.amazon.com/firehose/latest/dev/lambda-blueprints.html): These blueprints demonstrate how you can create and use AWS Lambda functions to transform data in your Amazon Data Firehose data streams.
- [Handle failure in data transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation-failure-handling.html): If your Lambda function invocation fails because of a network timeout or because you've reached the Lambda invocation limit, Amazon Data Firehose retries the invocation three times by default.
- [Back up source records](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation-source-record-backup.html): Amazon Data Firehose can back up all untransformed records to your S3 bucket concurrently while delivering transformed records to the destination.


## [Partition streaming data](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)

- [Enable dynamic partitioning](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning-enable.html): Learn how to enable dynamic partitioning on a Firehose stream in Amazon Data Firehose.
- [Understand partitioning keys](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning-partitioning-keys.html): Upnderstand partitioning keys and how you can create them for Amazon Data Firehose.
- [Use Amazon S3 bucket prefix to deliver data](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning-s3bucketprefix.html): Understand how your partitioned data is delivered into the specified Amazon S3 prefixes.
- [Apply dynamic partitioning to aggregated data](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning-multirecord-deaggergation.html): Understand how to apply dynamic partitioning to aggregated data in Amazon Data Firehose.
- [Troubleshoot dynamic partitioning errors](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning-error-handling.html): Understand how to resolve errors related to dynamic partitioning in Amazon Data Firehose.
- [Buffer data for dynamic partitioning](https://docs.aws.amazon.com/firehose/latest/dev/buffering.html): Understand how Firehose internally buffers records that belong to a given partition.


## [Convert input data format](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)

- [Enable record format conversion](https://docs.aws.amazon.com/firehose/latest/dev/enable-record-format-conversion.html): Learn how you can enable record format conversion with Amazon Data Firehose console and API operations.
- [Handling errors for data format conversion](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion-error-handling.html): Learn how to resolve data format conversion errors in Amazon Data Firehose.


## [Understand data delivery](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html)

- [Understand delivery across AWS accounts and regions](https://docs.aws.amazon.com/firehose/latest/dev/across.html): Understand Amazon Data Firehose supports how data delivery to HTTP endpoint destinations across AWS accounts.
- [Understand HTTP endpoint delivery request and response specifications](https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html): Learn about specifications of the HTTP endpoint delivery request and response formats that Amazon Data Firehose uses.
- [Handle data delivery failures](https://docs.aws.amazon.com/firehose/latest/dev/retry.html): Understand how to resolve data delivery failures for different destinations with Amazon Data Firehose.

### [Configure Amazon S3 object name format](https://docs.aws.amazon.com/firehose/latest/dev/s3-object-name.html)

Understand how to configure S3 object key name and custom prefixes for Amazon S3 object for data delivery.

- [Understand custom prefixes for Amazon S3 objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html): Learn how to specify custom prefixes for data delivery to Amazon S3 and learn about different values you can use in Firehose namespaces.
- [Configure index rotation for OpenSearch Service](https://docs.aws.amazon.com/firehose/latest/dev/es-index-rotation.html): Learn how to set up index rotation for the OpenSearch Service destination in Amazon Data Firehose.
- [Pause and resume data delivery](https://docs.aws.amazon.com/firehose/latest/dev/pause-restart-stream.html): Learn how to temporarily pause and resume data delivery in Amazon Data Firehose.


## [Deliver data to Apache Iceberg Tables](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)

- [Considerations and limitations](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-considerations.html)
- [Prerequisites](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-prereq.html): Understand the prerequisites needed to use Apache Iceberg Tables and Amazon S3 Tables with Amazon Data Firehose.
- [Set up the Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-stream.html): Learn how to set up a Firehose stream and understand the prerequisites to use Apache Iceberg Tables as a destination.
- [Route incoming records to a single Iceberg table](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record.html): Learn how you can format input records to ingest data into Firehose for Apache Iceberg tables.
- [Route incoming records to different Iceberg tables](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record-different.html): Learn how you can route incoming records in a stream to different Iceberg tables based on the content of the record.
- [Monitor metrics](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-metric.html): Monitor CloudWatch metrics related to Apache Iceberg Tables as a destination.
- [Understand supported data types](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination-supp.html): Learn about all the primitive and complex data types that Firehose supports along with their examples.
- [Resources](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination-resources.html): Use the following resources to learn more:


## [Tag a Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging.html)

- [Understand tag basics](https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging-basics.html): You can use the Amazon Data Firehose API operations to complete the following tasks:
- [Track costs with tagging](https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging-billing.html): You can use tags to categorize and track your AWS costs.
- [Know tag restrictions](https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging-restrictions.html): The following restrictions apply to tags in Amazon Data Firehose.


## [Security](https://docs.aws.amazon.com/firehose/latest/dev/security.html)

- [Data Protection](https://docs.aws.amazon.com/firehose/latest/dev/encryption.html): Learn how to enable and disable server-side encryption when using Amazon Data Firehose.
- [Controlling access](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html): Control access to and from your Amazon Data Firehose resources by using IAM.

### [Authenticate with AWS Secrets Manager](https://docs.aws.amazon.com/firehose/latest/dev/using-secrets-manager.html)

Learn about using AWS Secrets Manager with Amazon Data Firehose to protect database credentials, API keys, and other secret information.

- [Understand secrets](https://docs.aws.amazon.com/firehose/latest/dev/secrets-manager-whats-secret.html): Learn what a secret contains in for different destinations in Amazon Data Firehose.
- [Create a secret](https://docs.aws.amazon.com/firehose/latest/dev/secrets-manager-create.html): How to use AWS Secrets Manager to create a secret and protect database credentials, API keys, and other secret information with Amazon Data Firehose.
- [Use the secret](https://docs.aws.amazon.com/firehose/latest/dev/secrets-manager-how.html): How Amazon Data Firehose uses AWS Secrets Manager to protect database credentials, API keys, and other secret information.
- [Rotate the secret](https://docs.aws.amazon.com/firehose/latest/dev/secrets-manager-rotate.html): How to rotate your AWS Secrets Manager secret and protect database credentials, API keys, and other secret information with Amazon Data Firehose.

### [Manage IAM roles through console](https://docs.aws.amazon.com/firehose/latest/dev/console-managed-roles.html)

Learn how to create and edit IAM roles in Amazon Data Firehose console.

- [Choose an existing IAM role](https://docs.aws.amazon.com/firehose/latest/dev/console-managed-iam-existing-roles.html): You can choose from an existing IAM role.
- [Create a new IAM role from console](https://docs.aws.amazon.com/firehose/latest/dev/console-managed-iam-create-new-roles.html): Alternatively, you could also use the Firehose console to create a new role on your behalf.
- [Edit IAM role from console](https://docs.aws.amazon.com/firehose/latest/dev/console-managed-iam-roles-edit.html): When you edit a Firehose stream, Firehose updates the corresponding permission policy accordingly to reflect the configuration and permission changes.
- [Compliance validation](https://docs.aws.amazon.com/firehose/latest/dev/compliance-validation.html): Learn what all AWS services are in scope of a specific compliance program and find resources for compliance with standards.
- [Resilience](https://docs.aws.amazon.com/firehose/latest/dev/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific Amazon Data Firehose features for data resiliency.

### [Understand infrastructure security](https://docs.aws.amazon.com/firehose/latest/dev/infrastructure-security.html)

Learn how Amazon Data Firehose isolates service traffic and how you can use AWS published API calls to access Firehose through the network.

- [Using Firehose with AWS PrivateLink](https://docs.aws.amazon.com/firehose/latest/dev/vpc.html): Learn how to use Amazon Data Firehose with AWS PrivateLink to keep traffic between your Amazon VPC and Amazon Data Firehose from leaving the Amazon network.
- [Implement security best practices](https://docs.aws.amazon.com/firehose/latest/dev/security-best-practices.html): Learn about security guidelines and considerations when you use Amazon Data Firehose and implement your own security policies.


## [Monitor Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/monitoring.html)

- [Implement best practices with CloudWatch Alarms](https://docs.aws.amazon.com/firehose/latest/dev/firehose-cloudwatch-metrics-best-practices.html): Learn the guidelines and best practices for CloudWatch Alarms in Amazon Data Firehose.
- [Monitoring with CloudWatch Metrics](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-metrics.html): Learn how to use CloudWatch Metrics to monitor Firehose streams in Amazon Data Firehose.
- [Access CloudWatch Metrics for Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/cloudwatch-metrics.html): Learn how you can monitor metrics for Amazon Data Firehose using the CloudWatch console, command line, or CloudWatch API.
- [Monitor with CloudWatch Logs](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-logs.html): Learn how to monitor Firehose stream in Amazon Data Firehose with CloudWatch logging.
- [Access CloudWatch logs for Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/accessing-firehose-data-delivery-logs.html): Learn how to access error logs for Amazon Data Firehose using the console or the CloudWatch console.
- [Monitor Agent Health](https://docs.aws.amazon.com/firehose/latest/dev/agent-health.html): Assess the health of Kinesis Agent by submitting data into Amazon Data Firehose and understand the rate at which the agent is submitting data.
- [Log Firehose API calls](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-using-cloudtrail.html): Learn how to use CloudTrail to capture all API calls for Amazon Data Firehose as events.


## [Code examples](https://docs.aws.amazon.com/firehose/latest/dev/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/firehose/latest/dev/service_code_examples_basics.html)

The following code examples show how to use the basics of Firehose with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/firehose/latest/dev/service_code_examples_actions.html)

The following code examples show how to use Firehose with AWS SDKs.

- [PutRecord](https://docs.aws.amazon.com/firehose/latest/dev/example_firehose_PutRecord_section.html): Use PutRecord with an AWS SDK or CLI
- [PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/dev/example_firehose_PutRecordBatch_section.html): Use PutRecordBatch with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/firehose/latest/dev/service_code_examples_scenarios.html)

The following code examples show how to use Firehose with AWS SDKs.

- [Put records to Firehose](https://docs.aws.amazon.com/firehose/latest/dev/example_firehose_Scenario_PutRecords_section.html): Use Amazon Data Firehose to process individual and batch records


## [Troubleshoot errors](https://docs.aws.amazon.com/firehose/latest/dev/troubleshooting.html)

- [Common issues](https://docs.aws.amazon.com/firehose/latest/dev/troubleshoot-common-issues.html): Learn what steps you can perform to fix issues when no data at destination or when Firehose stream is unavailable.
- [Troubleshooting Amazon S3](https://docs.aws.amazon.com/firehose/latest/dev/data-not-delivered-to-s3.html): Learn how to troubleshoot errors if data is not delivered to Amazon S3.
- [Troubleshooting Amazon Redshift](https://docs.aws.amazon.com/firehose/latest/dev/data-not-delivered-to-rs.html): Learn how to troubleshoot error and failures when delivering data to Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup.
- [Troubleshooting Amazon OpenSearch Service](https://docs.aws.amazon.com/firehose/latest/dev/data-not-delivered-to-es.html): Learn how to troubleshoot error and failures when delivering data to Amazon OpenSearch Service.
- [Troubleshooting Splunk](https://docs.aws.amazon.com/firehose/latest/dev/data-not-delivered-to-splunk.html): Learn how to troubleshoot error and failures while delivering data to to your Splunk endpoint.
- [Troubleshooting Snowflake](https://docs.aws.amazon.com/firehose/latest/dev/troubleshooting-snowflake.html): Learn how to troubleshoot error and failures while delivering data to to your Snowflake destination.
- [Troubleshooting Firehose endpoint reachability](https://docs.aws.amazon.com/firehose/latest/dev/endpoint-troubleshooting.html): Learn how to troubleshoot error and failures for endpoint reachability failures.
- [Troubleshooting HTTP Endpoints](https://docs.aws.amazon.com/firehose/latest/dev/http_troubleshooting.html): Get solutions to problems found while delivering data to generic HTTP endpoints from Firehose.
- [Troubleshooting MSK As Source](https://docs.aws.amazon.com/firehose/latest/dev/msk_troubleshooting.html): Learn how to resolve related to hose creation, backpressure, suspension and more while using MSK as a source.
