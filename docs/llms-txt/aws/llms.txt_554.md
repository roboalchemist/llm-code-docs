# Source: https://docs.aws.amazon.com/managed-flink/latest/java/llms.txt

# Managed Service for Apache Flink Managed Service for Apache Flink Developer Guide

- [What is Managed Service for Apache Flink?](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
- [Training workshops, labs, and solution implementations](https://docs.aws.amazon.com/managed-flink/latest/java/examples-solutions.html)
- [Use practical utilities for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/utilities.html)
- [Managed Service for Apache Flink and Studio notebook quota](https://docs.aws.amazon.com/managed-flink/latest/java/limits.html)
- [Manage maintenance tasks for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/maintenance.html)
- [Achieve production readiness for your Managed Service for Apache Flink applications](https://docs.aws.amazon.com/managed-flink/latest/java/production-readiness.html)
- [Best practices](https://docs.aws.amazon.com/managed-flink/latest/java/best-practices.html)
- [Apache Flink stateful functions](https://docs.aws.amazon.com/managed-flink/latest/java/stateful-functions.html)
- [Document history](https://docs.aws.amazon.com/managed-flink/latest/java/doc-history.html)
- [API example code](https://docs.aws.amazon.com/managed-flink/latest/java/api-examples.html)
- [API Reference](https://docs.aws.amazon.com/managed-flink/latest/java/api-link.html)
- [Release versions](https://docs.aws.amazon.com/managed-flink/latest/java/release-versions.html)

## [How it works](https://docs.aws.amazon.com/managed-flink/latest/java/how-it-works.html)

### [Create an application](https://docs.aws.amazon.com/managed-flink/latest/java/how-creating-apps.html)

Explains the components and methods used to build a Managed Service for Apache Flink application.

- [Enable system rollbacks](https://docs.aws.amazon.com/managed-flink/latest/java/how-system-rollbacks.html): With system-rollback capability, you can achieve higher availability of your running Apache Flink application on Amazon Managed Service for Apache Flink.
- [Run an application](https://docs.aws.amazon.com/managed-flink/latest/java/how-running-apps.html): Explains details about running a Managed Service for Apache Flink application.
- [Application resources](https://docs.aws.amazon.com/managed-flink/latest/java/how-resources.html): This section describes the system resources that your application uses.
- [Pricing](https://docs.aws.amazon.com/managed-flink/latest/java/how-pricing.html): Managed Service for Apache Flink is now billed in one-second increments.

### [Review DataStream API components](https://docs.aws.amazon.com/managed-flink/latest/java/how-datastream.html)

Your Apache Flink application uses the Apache Flink DataStream API to transform data in a data stream.

### [Connectors](https://docs.aws.amazon.com/managed-flink/latest/java/how-connectors.html)

Use connectors in Managed Service for Apache Flink to move data in and out of applications with the DataStream API.

- [Add streaming data sources](https://docs.aws.amazon.com/managed-flink/latest/java/how-sources.html): Add sources to Managed Service for Apache Flink to provide streaming data for your application to analyze.
- [Write data using sinks](https://docs.aws.amazon.com/managed-flink/latest/java/how-sinks.html): Add sink configuration to a Managed Service for Apache Flink to persist data to an external destination.
- [Use Asynchronous I/O](https://docs.aws.amazon.com/managed-flink/latest/java/how-async.html): Work with Asynchronous I/O in Managed Service for Apache Flink.
- [Operators](https://docs.aws.amazon.com/managed-flink/latest/java/how-operators.html): Use Apache Flink operators in a Managed Service for Apache Flink application to transform incoming streaming data with the DataStream API.
- [Event tracking](https://docs.aws.amazon.com/managed-flink/latest/java/how-time.html): Work with timestamps in Managed Service for Apache Flink.

### [Table API components](https://docs.aws.amazon.com/managed-flink/latest/java/how-table.html)

Your Apache Flink application uses the Apache Flink Table API to interact with data in a stream using a relational model.

- [Table API connectors](https://docs.aws.amazon.com/managed-flink/latest/java/how-table-connectors.html): In the Apache Flink programming model, connectors are components that your application uses to read or write data from external sources, such as other AWS services.
- [Table API time attributes](https://docs.aws.amazon.com/managed-flink/latest/java/how-table-timeattributes.html): Each record in a data stream has several timestamps that define when events related to the record occurred:

### [Use Python](https://docs.aws.amazon.com/managed-flink/latest/java/how-python.html)

- [Program your Python application](https://docs.aws.amazon.com/managed-flink/latest/java/how-python-programming.html): You code your Managed Service for Apache Flink for Python application using the Apache Flink Python Table API.
- [Create your Python application](https://docs.aws.amazon.com/managed-flink/latest/java/how-python-creating.html)
- [Monitor your Python application](https://docs.aws.amazon.com/managed-flink/latest/java/how-python-monitoring.html): You use your application's CloudWatch log to monitor your Managed Service for Apache Flink Python application.
- [Use runtime properties](https://docs.aws.amazon.com/managed-flink/latest/java/how-properties.html): Work with Runtime Properties in Managed Service for Apache Flink.
- [Use Apache Flink connectors](https://docs.aws.amazon.com/managed-flink/latest/java/how-flink-connectors.html): Use connectors in Managed Service for Apache Flink to move data in and out of applications.
- [Implement fault tolerance](https://docs.aws.amazon.com/managed-flink/latest/java/how-fault.html): Use state, checkpoints, and snapshots in a Managed Service for Apache Flink to implement complex operations and fault tolerance.
- [Manage application backups using snapshots](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html): Use snapshots in a Managed Service for Apache Flink application to implement complex operations and fault tolerance.

### [Use in-place version upgrades for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/how-in-place-version-upgrades.html)

Use in-place version upgrades in Apache Flink to retain application traceability against a single ARN across Apache Flink versions.

- [Upgrade applications](https://docs.aws.amazon.com/managed-flink/latest/java/upgrading-applications.html): Before you begin, we recommend that you watch this video: In-Place Version Upgrades.
- [Upgrade to a new version](https://docs.aws.amazon.com/managed-flink/latest/java/upgrading-application-new-version.html): You can upgrade your Flink application by using the UpdateApplication action.
- [Roll back application upgrades](https://docs.aws.amazon.com/managed-flink/latest/java/rollback.html): If you have issues with your application or find inconsistencies in your application code between Flink versions, you can roll back using the AWS CLI, AWS CloudFormation, AWS SDK, or the AWS Management Console.
- [Best practices](https://docs.aws.amazon.com/managed-flink/latest/java/best-practices-recommendations.html)
- [Known issues](https://docs.aws.amazon.com/managed-flink/latest/java/precautions.html)

### [Implement application scaling](https://docs.aws.amazon.com/managed-flink/latest/java/how-scaling.html)

Use parallelism to implement application scaling in Managed Service for Apache Flink.

- [Use automatic scaling](https://docs.aws.amazon.com/managed-flink/latest/java/how-scaling-auto.html): Managed Service for Apache Flink elastically scales your applicationâs parallelism to accommodate the data throughput of your source and your operator complexity for most scenarios.

### [Add tags to applications](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging.html)

Explains how to tag applications with metadata.

- [Add tags when an application is created](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-create.html): You add tags when creating an application using the tags parameter of the CreateApplication action.
- [Add or update tags for an existing application](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-add.html): You add tags to an application using the TagResource action.
- [List tags for an application](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-list.html): To list existing tags, you use the ListTagsForResource action.
- [Remove tags from an application](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-remove.html): To remove tags from an application, you use the UntagResource action.
- [Use CloudFormation](https://docs.aws.amazon.com/managed-flink/latest/java/lambda-cfn-flink.html): The following exercise shows how to start a Flink application created with CloudFormation using a Lambda function in the same stack.
- [Use the Apache Flink Dashboard](https://docs.aws.amazon.com/managed-flink/latest/java/how-dashboard.html): Explains how to access and use the Apache Flink Dashboard with a Managed Service for Apache Flink.


## [Supported and deprecated versions](https://docs.aws.amazon.com/managed-flink/latest/java/release-version-list.html)

- [Amazon Managed Service for Apache Flink 1.20](https://docs.aws.amazon.com/managed-flink/latest/java/flink-1-20.html): Explains the Amazon Managed Service for Apache Flink 1.20 release.
- [Amazon Managed Service for Apache Flink 1.19](https://docs.aws.amazon.com/managed-flink/latest/java/flink-1-19.html): Explains the Amazon Managed Service for Apache Flink 1.19 release.
- [Amazon Managed Service for Apache Flink 1.18](https://docs.aws.amazon.com/managed-flink/latest/java/flink-1-18.html): Explains the Amazon Managed Service for Apache Flink 1.18 release.
- [Amazon Managed Service for Apache Flink 1.15](https://docs.aws.amazon.com/managed-flink/latest/java/flink-1-15-2.html): Explains the Amazon Managed Service for Apache Flink 1.15.2 release.
- [Earlier versions](https://docs.aws.amazon.com/managed-flink/latest/java/earlier.html): Learn about using earlier versions of Apache Flink in Managed Service for Apache Flink.


## [Use Studio notebooks with Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/how-notebook.html)

- [Use the correct Studio notebook Runtime version](https://docs.aws.amazon.com/managed-flink/latest/java/studio-notebook-versions.html): With Amazon Managed Service for Apache Flink Studio, you can query data streams in real time and build and run stream processing applications using standard SQL, Python, and Scala in an interactive notebook.
- [Create a Studio notebook](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-creating.html): A Studio notebook contains queries or programs written in SQL, Python, or Scala that runs on streaming data and returns analytic results.
- [Perform an interactive analysis of streaming data](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-interactive.html): You use a serverless notebook powered by Apache Zeppelin to interact with your streaming data.
- [Deploy as an application with durable state](https://docs.aws.amazon.com/managed-flink/latest/java/how-notebook-durable.html): You can build your code and export it to Amazon S3.
- [IAM permissions](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-iam.html): Managed Service for Apache Flink creates an IAM role for you when you create a Studio notebook through the AWS Management Console.
- [Use connectors and dependencies](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-connectors.html): Connectors enable you to read and write data across various technologies.
- [User-defined functions](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-udf.html): User-defined functions (UDFs) are extension points that allow you to call frequently-used logic or custom logic that can't be expressed otherwise in queries.
- [Enable checkpointing](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-checkpoint.html): You enable checkpointing by using environment settings.
- [Upgrade Studio Runtime](https://docs.aws.amazon.com/managed-flink/latest/java/upgrading-studio-runtime.html): This section contains information about how to upgrade your Studio notebook Runtime.

### [Work with AWS Glue](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-glue.html)

Your Studio notebook stores and gets information about its data sources and sinks from AWS Glue.

- [Table properties](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-glue-properties.html): In addition to data fields, your AWS Glue tables provide other information to your Studio notebook using table properties.

### [Examples and tutorials for Studio notebooks in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-examples.html)

### [Tutorial: Create a Studio notebook in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/example-notebook.html)

The following tutorial demonstrates how to create a Studio notebook that reads data from a Kinesis data stream or an Amazon MSK cluster.

- [Create a Studio notebook with Kinesis Data Streams](https://docs.aws.amazon.com/managed-flink/latest/java/example-notebook-streams.html): This tutorial describes how to create a Studio notebook that uses a Kinesis data stream as a source.
- [Create a Studio notebook with Amazon MSK](https://docs.aws.amazon.com/managed-flink/latest/java/example-notebook-msk.html): This tutorial describes how to create a Studio notebook that uses an Amazon MSK cluster as a source.
- [Clean up your application and dependent resources](https://docs.aws.amazon.com/managed-flink/latest/java/example-notebook-cleanup.html)
- [Tutorial: Deploy a Studio notebook as a Managed Service for Apache Flink application with durable state](https://docs.aws.amazon.com/managed-flink/latest/java/example-notebook-deploy.html): The following tutorial demonstrates how to deploy a Studio notebook as a Managed Service for Apache Flink application with durable state.
- [View example queries to analyza data in a Studio notebook](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-sql-examples.html): The following example queries demonstrate how to analyze data using window queries in a Studio notebook.
- [Troubleshoot Studio notebooks for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-troubleshooting.html): This section contains troubleshooting information for Studio notebooks.
- [Create custom IAM policies for Managed Service for Apache Flink Studio notebooks](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-appendix-iam.html): You normally use managed IAM policies to allow your application to access dependent resources.


## [Tutorial: Get started using the DataStream API in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html)

- [Set up an account](https://docs.aws.amazon.com/managed-flink/latest/java/setting-up.html): Before you use Managed Service for Apache Flink for the first time, complete the following tasks:
- [Set up the AWS CLI](https://docs.aws.amazon.com/managed-flink/latest/java/setup-awscli.html): In this step, you download and configure the AWS CLI to use with Managed Service for Apache Flink.
- [Create an application](https://docs.aws.amazon.com/managed-flink/latest/java/get-started-exercise.html): In this step, you create a Managed Service for Apache Flink application with Kinesis data streams as a source and a sink.
- [Clean up resources](https://docs.aws.amazon.com/managed-flink/latest/java/getting-started-cleanup.html): This section includes procedures for cleaning up AWS resources created in this Getting Started (DataStream API) tutorial.
- [Explore additional resources](https://docs.aws.amazon.com/managed-flink/latest/java/getting-started-next-steps.html): Now that you've created and run a basic Managed Service for Apache Flink application, see the following resources for more advanced Managed Service for Apache Flink solutions.


## [Tutorial: Get started using the TableAPI in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/gs-table.html)

- [Create an application](https://docs.aws.amazon.com/managed-flink/latest/java/gs-table-create.html): In this exercise, you create a Managed Service for Apache Flink application with Kinesis data streams as a source and sink.
- [Clean up resources](https://docs.aws.amazon.com/managed-flink/latest/java/gs-table-cleanup.html): This section includes procedures for cleaning up AWS resources created in the Getting Started (Table API) tutorial.
- [Explore additional resources](https://docs.aws.amazon.com/managed-flink/latest/java/gs-table-next-steps.html): Now that you've created and run a Managed Service for Apache Flink application that uses the Table API, see in the .


## [Tutorial: Get started using Python in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/gs-python.html)

- [Create an application](https://docs.aws.amazon.com/managed-flink/latest/java/gs-python-createapp.html): In this section, you create a Managed Service for Apache Flink application for Python application with a Kinesis stream as a source and a sink.
- [Clean up resources](https://docs.aws.amazon.com/managed-flink/latest/java/gs-python-cleanup.html): This section includes procedures for cleaning up AWS resources created in the Getting Started (Python) tutorial.


## [Tutorial: Get started using Scala in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/examples-gs-scala.html)

- [Create and run the application (console)](https://docs.aws.amazon.com/managed-flink/latest/java/gs-scala-7.html): Follow these steps to create, configure, update, and run the application using the console.
- [Create and run the application (CLI)](https://docs.aws.amazon.com/managed-flink/latest/java/examples-gs-scala-create-run-cli.html): In this section, you use the AWS Command Line Interface to create and run the Managed Service for Apache Flink application.
- [Clean up AWS resources](https://docs.aws.amazon.com/managed-flink/latest/java/examples-gs-scala-cleanup.html): This section includes procedures for cleaning up AWS resources created in the Tumbling Window tutorial.


## [Use Apache Beam with Managed Service for Apache Flink applications](https://docs.aws.amazon.com/managed-flink/latest/java/how-creating-apps-beam.html)

- [Creating an application using Apache Beam](https://docs.aws.amazon.com/managed-flink/latest/java/examples-beam.html): In this exercise, you create a Managed Service for Apache Flink application that transforms data using Apache Beam.


## [Examples for creating and working with Managed Service for Apache Flink applications](https://docs.aws.amazon.com/managed-flink/latest/java/examples-collapsibles.html)

- [Java examples for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/examples-new-java.html): The following examples demonstrate how to create applications written in Java.
- [Python examples for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/examples-new-python.html): The following examples demonstrate how to create applications written in Python.
- [Scala examples for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/examples-new-scala.html): The following examples demonstrate how to create applications using Scala with Apache Flink.


## [Security in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/security.html)

- [Data protection](https://docs.aws.amazon.com/managed-flink/latest/java/data-protection.html): Explains the permissions needed to enable Amazon Managed Service for Apache Flink access to streaming sources.

### [Key management in Amazon MSF](https://docs.aws.amazon.com/managed-flink/latest/java/key-management-flink.html)

In Amazon MSF, you can choose to use either AWS managed keys or your own customer managed keys (CMKs) to encrypt data.

- [Using customer managed keys](https://docs.aws.amazon.com/managed-flink/latest/java/use-cmk-flink.html): You need to consider the following factors when establishing, managing, and operating Amazon MSF applications subject to a CMK policy.
- [Managing CMK using console](https://docs.aws.amazon.com/managed-flink/latest/java/manage-cmk-console.html): This topic describes how to create and update your KMS CMKs using the AWS Management Console.
- [Managing CMK using APIs](https://docs.aws.amazon.com/managed-flink/latest/java/manage-cmk-api.html): This topic describes how to create, and update your KMS CMKs using Amazon MSF APIs.

### [Identity and Access Management for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/security-iam.html)

How to authenticate requests and manage access your Managed Service for Apache Flink resources.

- [How Amazon Managed Service for Apache Flink works with IAM](https://docs.aws.amazon.com/managed-flink/latest/java/security_iam_service-with-iam.html)
- [Identity-based policy examples](https://docs.aws.amazon.com/managed-flink/latest/java/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Managed Service for Apache Flink resources.
- [Troubleshooting](https://docs.aws.amazon.com/managed-flink/latest/java/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Managed Service for Apache Flink and IAM.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/managed-flink/latest/java/iam-cross-service-confused-deputy-prevention.html): In AWS, cross-service impersonation can occur when one service (the calling service) calls another service (the called service).
- [Compliance validation for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/akda-java-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience and disaster recovery in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific a Managed Service for Apache Flink features for data resiliency.
- [Infrastructure security in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/infrastructure-security.html): Learn how Managed Service for Apache Flink isolates service traffic.
- [Security best practices for Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/security-best-practices.html): Amazon Managed Service for Apache Flink provides a number of security features to consider as you develop and implement your own security policies.


## [Logging and monitoring in Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/monitoring-overview.html)

- [Logging in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/logging.html): Logging
- [Monitoring in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/monitoring.html): Monitoring
- [Set up application logging in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/cloudwatch-logs.html): Add a CloudWatch Logs option to your Managed Service for Apache Flink.
- [Analyze logs with CloudWatch Logs Insights](https://docs.aws.amazon.com/managed-flink/latest/java/cloudwatch-logs-reading.html): Use CloudWatch Logs Insights to monitor your Managed Service for Apache Flink application

### [Metrics and dimensions in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions.html)

Metrics and dimensions that Managed Service for Apache Flink reports to CloudWatch.

- [View CloudWatch metrics](https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions-viewing.html): You can view CloudWatch metrics for your application using the Amazon CloudWatch console or the AWS CLI.
- [Set CloudWatch metrics reporting levels](https://docs.aws.amazon.com/managed-flink/latest/java/cloudwatch-logs-levels.html): You can control the level of application metrics that your application creates.
- [Use custom metrics with Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/monitoring-metrics-custom.html): Describes how to create user-defined metrics with Managed Service for Apache Flink and CloudWatch Logs
- [Use CloudWatch Alarms with Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/monitoring-metrics-alarms.html): Describes recommendations for creating CloudWatch alarms with Managed Service for Apache Flink.
- [Write custom messages to CloudWatch Logs](https://docs.aws.amazon.com/managed-flink/latest/java/cloudwatch-logs-writing.html): Use the Apache log4j or slf4j library to write custom messages to Managed Service for Apache Flink application's CloudWatch log.
- [Log Managed Service for Apache Flink API calls with AWS CloudTrail](https://docs.aws.amazon.com/managed-flink/latest/java/logging-using-cloudtrail.html): Learn about logging Managed Service for Apache Flink with AWS CloudTrail.


## [Tune performance](https://docs.aws.amazon.com/managed-flink/latest/java/performance.html)

- [Troubleshoot performance issues](https://docs.aws.amazon.com/managed-flink/latest/java/performance-troubleshooting.html): This section contains a list of symptoms that you can check to diagnose and fix performance issues.
- [Use performance best practices](https://docs.aws.amazon.com/managed-flink/latest/java/performance-improving.html): This section describes special considerations for designing an application for performance.
- [Monitor performance](https://docs.aws.amazon.com/managed-flink/latest/java/performance-monitoring.html): This section describes tools for monitoring an application's performance.


## [Learn about Apache Flink settings](https://docs.aws.amazon.com/managed-flink/latest/java/reference-flink-settings.title.html)

- [Modifiable Flink configuration properties](https://docs.aws.amazon.com/managed-flink/latest/java/reference-modifiable-settings.html): Following are Flink configuration settings that you can modify using a support case.
- [View configured Flink properties](https://docs.aws.amazon.com/managed-flink/latest/java/viewing-modifiable-settings.html): You can view Apache Flink properties you have configured yourself or requested to be modified through a support case via the Apache Flink Dashboard and following these steps:


## [Configure MSF to access resources in an Amazon VPC](https://docs.aws.amazon.com/managed-flink/latest/java/vpc.html)

- [VPC application permissions](https://docs.aws.amazon.com/managed-flink/latest/java/vpc-permissions.html): This section describes the permission policies your application will need to work with your VPC.
- [Establish internet and service access for a VPC-connected Managed Service for Apache Flink application](https://docs.aws.amazon.com/managed-flink/latest/java/vpc-internet.html): By default, when you connect a Managed Service for Apache Flink application to a VPC in your account, it does not have access to the internet unless the VPC provides access.
- [Use the Managed Service for Apache Flink VPC API](https://docs.aws.amazon.com/managed-flink/latest/java/vpc-api.html): Use the following Managed Service for Apache Flink API operations to manage VPCs for your application.
- [Example: Use a VPC](https://docs.aws.amazon.com/managed-flink/latest/java/vpc-example.html): For a complete tutorial about how to access data from an Amazon MSK Cluster in a VPC, see .


## [Troubleshoot Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting.html)

### [Development troubleshooting](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-development.html)

This section contains information about diagnosing and fixing development issues with your Managed Service for Apache Flink application.

- [System rollback best practices](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-system-rollback.html): With automatic system rollback and operations visibility capabilities in Amazon Managed Service for Apache Flink, you can identify and resolve issues with your applications.
- [Hudi configuration best practices](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-hudi.html): To run Hudi connectors on Managed Service for Apache Flink we recommend the following configuration changes.
- [Apache Flink Flame Graphs](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-update-flamegraphs.html): Flame Graphs are enabled by default on applications in Managed Service for Apache Flink versions that support it.
- [Credential provider issue with EFO connector 1.15.2](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-credential-provider.html): There is a known issue with Kinesis Data Streams EFO connector versions up to 1.15.2 where the FlinkKinesisConsumer is not respecting Credential Provider configuration.
- [Applications with unsupported Kinesis connectors](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-unsupported-kinesis-connectors.html): Managed Service for Apache Flink for Apache Flink version 1.15 or later will automatically reject applications from starting or updating if they are using unsupported Kinesis Connector versions (pre-version 1.15.2) bundled into application JARs or archives (ZIP).
- [Compile error: "Could not resolve dependencies for project"](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-compile.html): In order to compile the Managed Service for Apache Flink sample applications, you must first download and compile the Apache Flink Kinesis connector and add it to your local Maven repository.
- [Invalid choice: "kinesisanalyticsv2"](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-cli-update.html): To use v2 of the Managed Service for Apache Flink API, you need the latest version of the AWS Command Line Interface (AWS CLI).
- [UpdateApplication action isn't reloading application code](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-update.html): The UpdateApplication action will not reload application code with the same file name if no S3 object version is specified.
- [S3 StreamingFileSink FileNotFoundExceptions](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-s3sink.html): Managed Service for Apache Flink applications can run into In-progress part file FileNotFoundException when starting from snapshots if an In-progress part file referred to by its savepoint is missing.
- [FlinkKafkaConsumer issue with stop with savepoint](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-FlinkKafkaConsumer.html): When using the legacy FlinkKafkaConsumer there is a possibility your application may get stuck in UPDATING, STOPPING or SCALING, if you have system snapshots enabled.

### [Flink 1.15 Async Sink Deadlock](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-async-deadlock.html)

There is a known issue with AWS connectors for Apache Flink implementing AsyncSink interface.

- [Update Java applications](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-async-deadlock-update-java-apps.html): Follow the procedures below to update Java applications:
- [Update Python applications](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-async-deadlock-update-python-apps.html): Python applications can use connectors in 2 different ways: packaging connectors and other Java dependencies as part of single uber-jar, or use connector jar directly.
- [Amazon Kinesis data streams source processing out of order during re-sharding](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-kinesis-data-streams-processing-out-of-order.html): The current FlinkKinesisConsumer implementation doesnât provide strong ordering guarantees between Kinesis shards.

### [Real-time vector embedding blueprints FAQ and troubleshooting](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-blueprints.html)

Review the following FAQ and troubleshooting sections to troubleshoot real-time vector embedding blueprint issues.

- [Real-time vector embedding blueprints - FAQ](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-blueprints-FAQ.html): Review the following FAQ about real-time vector embedding blueprints.
- [Real-time vector embedding blueprints - troubleshooting](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-blueprints-TS.html): Review the following troubleshooting topics about real-time vector embedding blueprints.

### [Runtime troubleshooting](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-runtime.html)

This section contains information about diagnosing and fixing runtime issues with your Managed Service for Apache Flink application.

- [Application issues](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-symptoms.html): This section contains solutions for error conditions that you may encounter with your Managed Service for Apache Flink application.
- [Application is restarting](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-rt-restarts.html): If your application is not healthy, its Apache Flink job continually fails and restarts.
- [Throughput is too slow](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-rt-throughput.html): If your application is not processing incoming streaming data quickly enough, it will perform poorly and become unstable.
- [Unbounded state growth](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-rt-stateleaks.html): If your application is not properly disposing of outdated state information, it will continually accumulate and lead to application performance or stability issues.
- [I/O bound operators](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-io-bound-operators.html): It's best to avoid dependencies to external systems on the data path.
- [Upstream or source throttling from a Kinesis data stream](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-source-throttling.html): Symptom: The application is encountering LimitExceededExceptions from their upstream source Kinesis data stream.
- [Checkpoints](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-checkpoints.html): Checkpoints are Flinkâs mechanism to ensure that the state of an application is fault tolerant.
- [Checkpointing is timing out](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-chk-timeout.html): If your application is not optimized or properly provisioned, checkpoints can fail.
- [Checkpoint failure for Apache Beam](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-chk-failure-beam.html): If your Beam application is configured with shutdownSourcesAfterIdleMs set to 0ms, checkpoints can fail to trigger because tasks are in "FINISHED" state.
- [Backpressure](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-backpressure.html): Flink uses backpressure to adapt the processing speed of individual operators.
- [Data skew](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-data-skew.html): A Flink application is executed on a cluster in a distributed fashion.
- [State skew](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-state-skew.html): For stateful operators, i.e., operators that maintain state for their business logic such as windows, data skew always leads to state skew.
- [Integrate with resources in different Regions](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-resources-in-different-regions.html): You can enable using StreamingFileSink to write to an Amazon S3 bucket in a different Region from your Managed Service for Apache Flink application via a setting required for cross Region replication in the Flink configuration.
