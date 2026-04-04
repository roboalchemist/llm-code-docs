# Source: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/llms.txt

# Amazon Kinesis Data Analytics for SQL Applications Developer Guide SQL Developer Guide

> Scale elastically for real-time processing and analytics for streaming big data using Amazon Kinesis Data Analytics for SQL Applications

- [Amazon Kinesis Data Analytics for SQL Applications discontinuation](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/discontinuation.html)
- [What Is Amazon Kinesis Data Analytics for SQL Applications?](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html)
- [Limits](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html)
- [Best Practices](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/best-practices.html)
- [Troubleshooting](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/troubleshooting.html)
- [SQL Reference](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/analytics-kdg-sqlref.html)
- [Document History](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/glossary.html)

## [Migrating to Managed Service for Apache Flink](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/migrating-to-kda-studio-overview.html)


## [How It Works](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html)

### [Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html)

Configure a streaming source and a reference data source for a Kinesis Data Analytics application.

- [Working with JSONPath](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/about-json-path.html): Access JSON elements in Kinesis Data Analytics using JSONPath.
- [Mapping Streaming Source Elements to SQL Input Columns](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sch-mapping.html): Process and analyze streaming data in either JSON or CSV formats using standard SQL in Kinesis Data Analytics.
- [Using the Schema Discovery Feature on Streaming Data](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sch-dis.html): Use the discovery API to infer a schema on streaming data in Kinesis Data Analytics.
- [Using the Schema Discovery Feature on Static Data](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sch-dis-ref.html): Use schema discovery on a static file that contains a sample of the data in the expected format of your streaming or reference data in Kinesis Data Analytics.

### [Preprocessing Data Using a Lambda Function](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/lambda-preprocessing.html)

Use a Lambda function to preprocess data in your Amazon Kinesis data stream that needs format conversion, transformation, enrichment, or filtering.

- [Creating Lambda Functions for Preprocessing](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/lambda-preprocessing-functions.html): Create Lambda functions for preprocessing in Kinesis Data Analytics applications using Node.js, Java, Python, and .NET templates.
- [Parallelizing Input Streams for Increased Throughput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/input-parallelism.html)
- [Application Code](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html): Application code is a series of SQL statements that process input and produce output.

### [Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html)

Add output configuration to Kinesis Data Analytics applications to persist everything written to an in-application stream to an external destination.

### [Using a Lambda Function as Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output-lambda.html)

Overview of using Lambda functions as output, including permissions, metrics, templates, and how-to information.

- [Creating Lambda Functions for Application Destinations](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output-lambda-functions.html): Create Lambda functions as output in Kinesis Data Analytics applications using Node.js, Java, Python, and .NET templates.
- [Application Output Delivery Model](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/failover-checkpoint.html): Overview of how Kinesis Data Analytics handles the delivery of application output in the case of application failure.
- [Error Handling](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/error-handling.html): Amazon Kinesis Data Analytics returns API or SQL errors directly to you.
- [Auto Scaling Applications](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-autoscaling.html): Explains the process used by Kinesis Data Analytics to increase throughput by assigning more Kinesis Processing Units (KPUs).
- [Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html): Explains how to tag applications with metadata.


## [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html)

- [Step 1: Set Up an Account](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/setting-up.html): Before you use Amazon Kinesis Data Analytics for the first time, complete the following tasks:
- [Step 2: Set Up the AWS CLI](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/setup-awscli.html): Follow the steps to download and configure the AWS Command Line Interface (AWS CLI).

### [Step 3: Create Your Starter Analytics Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html)

By following the steps in this section, you can create your first Kinesis Data Analytics application using the console.

- [Step 3.1: Create an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-create-app.html): In this section, you create an Amazon Kinesis Data Analytics application.
- [Step 3.2: Configure Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-configure-input.html): Your application needs a streaming source.
- [Step 3.3: Add Real-Time Analytics (Add Application Code)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-add-realtime-analytics.html): You can write your own SQL queries against the in-application stream, but for the following step you use one of the templates that provides sample code.
- [Step 3.4: (Optional) Update the Application Code](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-update-appcode.html): In this step, you explore how to update the application code.

### [Step 4 (Optional) Edit the Schema and SQL Code Using the Console](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/console-feature-summary.html)

Use features of the console that are discussed in the Kinesis Data Analytics Getting Started guide.

- [Working with the Schema Editor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/console-summary-edit-schema.html): The schema for an Amazon Kinesis Data Analytics application's input stream defines how data from the stream is made available to SQL queries in the application.
- [Working with the SQL Editor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/console-summary-sql-editor.html): Following, you can find information about sections of the SQL editor and how each works.


## [Streaming SQL Concepts](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/streaming-sql-concepts.html)

- [In-Application Streams and Pumps](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/streams-pumps.html): When you configure application input, you map a streaming source to an in-application stream that is created.
- [Timestamps and the ROWTIME Column](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/timestamps-rowtime-concepts.html): In-application streams include a special column called ROWTIME.
- [Continuous Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/continuous-queries-concepts.html): A query over a stream executes continuously over streaming data.

### [Windowed Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/windowed-sql.html)

SQL queries in your application code execute continuously over in-application streams.

- [Stagger Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/stagger-window-concepts.html): Using stagger windows is a windowing method that is suited for analyzing groups of data that arrive at inconsistent times.
- [Tumbling Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tumbling-window-concepts.html): When a windowed query processes each window in a non-overlapping manner, the window is referred to as a tumbling window.
- [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html): Instead of grouping records using GROUP BY, you can define a time-based or row-based window.
- [Stream Joins](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/stream-joins-concepts.html): You can have multiple in-application streams in your application.


## [Kinesis Data Analytics for SQL examples](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples.html)

### [Transforming Data](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming.html)

Examples of transforming data in Amazon Kinesis Data Analytics.

### [Transforming String Values](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings.html)

Examples of using SQL functions to transform strings in Amazon Kinesis Data Analytics

- [Extract a Portion of a String](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings-substring.html): Example of using the SUBSTRING function to transform a string in Kinesis Data Analytics.
- [Replace a Substring using Regex](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings-regexreplace.html): Example of using the REGEX_REPLACE function to transform a string in Kinesis Data Analytics.
- [Parse Logs with Regex](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings-regexlogparse.html): Example of using the REGEX_LOG_PARSE function to transform a string in Kinesis Data Analytics.
- [Parse Web Logs](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings-w3clogparse.html): Example of using the W3C_LOG_PARSE function to transform a string in Kinesis Data Analytics.
- [Split Strings into Multiple Fields](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-transforming-strings-variablecolumnlogparse.html): Example of using the VARIABLE_COLUMN_LOG_PARSE function to manipulate strings in Kinesis Data Analytics.
- [Transforming DateTime Values](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-string-datetime-manipulation.html): Example of using SQL functions to transform dates in Kinesis Data Analytics.

### [Transforming Multiple Data Types](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-tworecordtypes.html)

A common requirement in extract, transform, and load (ETL) applications is to process multiple record types on a streaming source.

- [Step 1: Prepare the Data](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tworecordtypes-prepare.html): Create and populate a streaming source for the Kinesis Data Analytics Transforming Multiple Data Types example.
- [Step 2: Create the Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tworecordtypes-create-app.html): In this section, you create an Kinesis Data Analytics application.

### [Windows and Aggregation](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window.html)

Examples of window and aggregation queries in Amazon Kinesis Data Analytics.

- [Stagger Window](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window-stagger.html): Example of a stagger window query in Kinesis Data Analytics.
- [Tumbling Window Using ROWTIME](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window-tumbling-rowtime.html): Example of a tumbling window using ROWTIME in Kinesis Data Analytics.
- [Tumbling Window Using an Event Timestamp](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window-tumbling-event.html): Example of a tumbling window using an event timestamp in Kinesis Data Analytics.
- [Most Frequently Occurring Values (TOP_K_ITEMS_TUMBLING)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window-topkitems.html): Example of finding the most frequently occurring values in a tumbling window query in Kinesis Data Analytics.
- [Aggregating Partial Results](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-window-partialresults.html): Example of aggregating partial results from a tumbling window query in Kinesis Data Analytics.

### [Joins](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-joins.html)

Examples of join queries in Amazon Kinesis Data Analytics

- [Example: Add Reference Data Source](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-add-reference-data.html): In this exercise, you add reference data to an existing Kinesis Data Analytics application.

### [Machine Learning](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-machine.html)

Examples of machine learning queries in Amazon Kinesis Data Analytics

### [Detecting Anomalies](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-detection.html)

Example that demonstrates how to assign anomaly scores to records on an application's streaming source in Kinesis Data Analytics.

- [Step 1: Prepare](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-prepare.html): Before you create an Amazon Kinesis Data Analytics application for this exercise, you must create two Kinesis data streams.
- [Step 2: Create an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anom-score-create-app.html): In this section, you create an Amazon Kinesis Data Analytics application as follows:
- [Step 3: Configure Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-create-ka-app-config-destination.html): After completing , you have application code that is reading heart rate data from a streaming source and assigning an anomaly score to each.
- [Step 4: Verify Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-verify-output.html): After configuring the application output in , use the following AWS CLI commands to read records in the destination stream that is written by the application:

### [Example: Detect Anomalies and Get an Explanation](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-detection-with-explanation.html)

Amazon Kinesis Data Analytics provides the RANDOM_CUT_FOREST_WITH_EXPLANATION function, which assigns an anomaly score to each record based on values in the numeric columns.

- [Step 1: Prepare the Data](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-with-ex-prepare.html): Before you create an Amazon Kinesis Data Analytics application for this example, you create a Kinesis data stream to use as the streaming source for your application.
- [Step 2: Create an Analytics Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anom-with-exp-create-app.html): In this section, you create an Amazon Kinesis Data Analytics application and configure it to use the Kinesis data stream that you created as the streaming source in .
- [Step 3: Examine the Results](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examine-results-with-exp.html): When you run the SQL code for this example, you first see rows with an anomaly score equal to zero.

### [Example: Detect Hotspots](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-detection.html)

Tutorial for using the HOTSPOTS function in Kinesis Data Analytics to locate hotspots on an application's streaming source.

- [Step 1: Create Streams](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-prepare.html): Hotspots example step 1: Prepare two Kinesis data streams for the source and destination for your application.
- [Step 2: Create an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspot-create-app.html): Hotspots example step 2: Create a Kinesis Data Analytics application.
- [Step 3: Configure Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-create-ka-app-config-destination.html): Hotspots example step 3: Configure the Kinesis Data Analytics application output.
- [Step 4: Verify Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-verify-output.html): Hotspots example step 4: Set up a web application to display the hotspot information in a Scalable Vector Graphics control.

### [Alerts and Errors](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples-alerts.html)

Examples of alerts and error queries in Amazon Kinesis Data Analytics

- [Simple Alerts](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-simple-alerts.html): Kinesis Data Analytics example application showing how to create simple alerts.
- [Throttled Alerts](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-throttled-alerts.html): Kinesis Data Analytics example application showing how to create throttled alerts.
- [In-Application Error Stream](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-explore-error-stream.html): Kinesis Data Analytics example application demonstrating exploring an in-application error stream.
- [Solution Accelerators](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/examples_solution.html): Solution accelerators that are available in Amazon Kinesis Data Analytics.


## [Security](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/security.html)

- [Data Protection](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/data-protection.html): Explains how Amazon Kinesis Data Analytics for SQL Applications protects sensitive data.

### [Identity and Access Management](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/iam-role.html)

Explains the permissions needed to enable Amazon Kinesis Data Analytics access to streaming sources.

- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/iam-cross-service-confused-deputy-prevention.html): In AWS, cross-service impersonation can occur when one service (the calling service) calls another service (the called service).

### [Authentication and Access Control](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/authentication-and-access-control.html)

How to authenticate requests and manage permissions to access your for SQL Applications resources through the API.

- [Overview of Managing Access](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/access-control-overview.html): Provides an overview of managing access permissions to your resources.
- [Using Identity-Based Policies (IAM Policies)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/using-identity-based-policies.html): Provides an overview of using identity-based (IAM) policies to control access to your resources.
- [API Permissions Reference](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/api-permissions-reference.html): Provides a complete list of the required API permissions you can use to control access to your resources.
- [Monitoring](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/security-monitoring.html): Learn how to monitor your delivery streams in Amazon Kinesis Data Analytics.
- [Compliance Validation](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/akda-java-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific Kinesis Data Analytics features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/infrastructure-security.html): Learn how Amazon Kinesis Data Analytics isolates service traffic.
- [Security Best Practices](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/security-best-practices.html): Amazon Kinesis Data Analytics provides a number of security features to consider as you develop and implement your own security policies.


## [Monitoring](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/monitoring-overview.html)

- [Monitoring Tools](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/monitoring-automated-manual.html): Configure AWS tools to monitor .

### [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/monitoring-cloudwatch.html)

You can monitor applications using Amazon CloudWatch.

- [Metrics and Dimensions](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/monitoring-metrics.html): The AWS/KinesisAnalytics namespace includes the following metrics.
- [Viewing Metrics and Dimensions](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/metrics-dimensions.html): When your application processes data streams, sends the following metrics and dimensions to CloudWatch.
- [Alarms](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/creating-alarms.html): You can create an Amazon CloudWatch alarm that sends an Amazon SNS message when the alarm changes state.
- [Logs](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html): If an application is misconfigured, it can transition to a running state during application start.
- [Using AWS CloudTrail](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/logging-using-cloudtrail.html): Learn about logging with AWS CloudTrail.


## [API Reference](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Operations.html)

The following actions are supported:

- [AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationCloudWatchLoggingOption.html)
- [AddApplicationInput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationInput.html)
- [AddApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationInputProcessingConfiguration.html)
- [AddApplicationOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationOutput.html)
- [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html)
- [CreateApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html)
- [DeleteApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplication.html)
- [DeleteApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationCloudWatchLoggingOption.html)
- [DeleteApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationInputProcessingConfiguration.html)
- [DeleteApplicationOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationOutput.html)
- [DeleteApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationReferenceDataSource.html)
- [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html)
- [DiscoverInputSchema](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DiscoverInputSchema.html)
- [ListApplications](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html)
- [ListTagsForResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListTagsForResource.html): Retrieves the list of key-value tags assigned to the application.
- [StartApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StartApplication.html)
- [StopApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StopApplication.html)
- [TagResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_TagResource.html): Adds one or more key-value tags to a Kinesis Analytics application.
- [UntagResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_UntagResource.html): Removes one or more tags from a Kinesis Analytics application.
- [UpdateApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_UpdateApplication.html)

### [Data Types](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Types.html)

The following data types are supported:

- [ApplicationDetail](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ApplicationDetail.html)
- [ApplicationSummary](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ApplicationSummary.html)
- [ApplicationUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ApplicationUpdate.html): Describes updates to apply to an existing Amazon Kinesis Analytics application.
- [CloudWatchLoggingOption](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CloudWatchLoggingOption.html): Provides a description of CloudWatch logging options, including the log stream Amazon Resource Name (ARN) and the role ARN.
- [CloudWatchLoggingOptionDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CloudWatchLoggingOptionDescription.html): Description of the CloudWatch logging option.
- [CloudWatchLoggingOptionUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CloudWatchLoggingOptionUpdate.html): Describes CloudWatch logging option updates.
- [CSVMappingParameters](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CSVMappingParameters.html): Provides additional mapping information when the record format uses delimiters, such as CSV.
- [DestinationSchema](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DestinationSchema.html): Describes the data format when records are written to the destination.
- [Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html): When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.
- [InputConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputConfiguration.html): When you start your application, you provide this configuration, which identifies the input source and the point in the input source at which you want the application to start processing records.
- [InputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputDescription.html): Describes the application input configuration.
- [InputLambdaProcessor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html): An object that contains the Amazon Resource Name (ARN) of the AWS Lambda function that is used to preprocess records in the stream, and the ARN of the IAM role that is used to access the AWS Lambda function.
- [InputLambdaProcessorDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html): An object that contains the Amazon Resource Name (ARN) of the AWS Lambda function that is used to preprocess records in the stream, and the ARN of the IAM role that is used to access the AWS Lambda expression.
- [InputLambdaProcessorUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorUpdate.html): Represents an update to the InputLambdaProcessor that is used to preprocess the records in the stream.
- [InputParallelism](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputParallelism.html): Describes the number of in-application streams to create for a given streaming source.
- [InputParallelismUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputParallelismUpdate.html): Provides updates to the parallelism count.
- [InputProcessingConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html): Provides a description of a processor that is used to preprocess the records in the stream before being processed by your application code.
- [InputProcessingConfigurationDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfigurationDescription.html): Provides configuration information about an input processor.
- [InputProcessingConfigurationUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfigurationUpdate.html): Describes updates to an InputProcessingConfiguration.
- [InputSchemaUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputSchemaUpdate.html): Describes updates for the application's input schema.
- [InputStartingPositionConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputStartingPositionConfiguration.html): Describes the point at which the application reads from the streaming source.
- [InputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputUpdate.html): Describes updates to a specific input configuration (identified by the InputId of an application).
- [JSONMappingParameters](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_JSONMappingParameters.html): Provides additional mapping information when JSON is the record format on the streaming source.
- [KinesisFirehoseInput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseInput.html): Identifies an Amazon Kinesis Firehose delivery stream as the streaming source.
- [KinesisFirehoseInputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseInputDescription.html): Describes the Amazon Kinesis Firehose delivery stream that is configured as the streaming source in the application input configuration.
- [KinesisFirehoseInputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseInputUpdate.html): When updating application input configuration, provides information about an Amazon Kinesis Firehose delivery stream as the streaming source.
- [KinesisFirehoseOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseOutput.html): When configuring application output, identifies an Amazon Kinesis Firehose delivery stream as the destination.
- [KinesisFirehoseOutputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseOutputDescription.html): For an application output, describes the Amazon Kinesis Firehose delivery stream configured as its destination.
- [KinesisFirehoseOutputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisFirehoseOutputUpdate.html): When updating an output configuration using the UpdateApplication operation, provides information about an Amazon Kinesis Firehose delivery stream configured as the destination.
- [KinesisStreamsInput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsInput.html): Identifies an Amazon Kinesis stream as the streaming source.
- [KinesisStreamsInputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsInputDescription.html): Describes the Amazon Kinesis stream that is configured as the streaming source in the application input configuration.
- [KinesisStreamsInputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsInputUpdate.html): When updating application input configuration, provides information about an Amazon Kinesis stream as the streaming source.
- [KinesisStreamsOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsOutput.html): When configuring application output, identifies an Amazon Kinesis stream as the destination.
- [KinesisStreamsOutputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsOutputDescription.html): For an application output, describes the Amazon Kinesis stream configured as its destination.
- [KinesisStreamsOutputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_KinesisStreamsOutputUpdate.html): When updating an output configuration using the UpdateApplication operation, provides information about an Amazon Kinesis stream configured as the destination.
- [LambdaOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_LambdaOutput.html): When configuring application output, identifies an AWS Lambda function as the destination.
- [LambdaOutputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_LambdaOutputDescription.html): For an application output, describes the AWS Lambda function configured as its destination.
- [LambdaOutputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_LambdaOutputUpdate.html): When updating an output configuration using the UpdateApplication operation, provides information about an AWS Lambda function configured as the destination.
- [MappingParameters](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_MappingParameters.html): When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
- [Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Output.html): Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written.
- [OutputDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_OutputDescription.html): Describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written.
- [OutputUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_OutputUpdate.html): Describes updates to the output configuration identified by the OutputId.
- [RecordColumn](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordColumn.html): Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
- [RecordFormat](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html): Describes the record format and relevant mapping information that should be applied to schematize the records on the stream.
- [ReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ReferenceDataSource.html): Describes the reference data source by providing the source information (S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.
- [ReferenceDataSourceDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ReferenceDataSourceDescription.html): Describes the reference data source configured for an application.
- [ReferenceDataSourceUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ReferenceDataSourceUpdate.html): When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.
- [S3Configuration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_S3Configuration.html): Provides a description of an Amazon S3 data source, including the Amazon Resource Name (ARN) of the S3 bucket, the ARN of the IAM role that is used to access the bucket, and the name of the Amazon S3 object that contains the data.
- [S3ReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_S3ReferenceDataSource.html): Identifies the S3 bucket and object that contains the reference data.
- [S3ReferenceDataSourceDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_S3ReferenceDataSourceDescription.html): Provides the bucket name and object key name that stores the reference data.
- [S3ReferenceDataSourceUpdate](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_S3ReferenceDataSourceUpdate.html): Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.
- [SourceSchema](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_SourceSchema.html): Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
- [Tag](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Tag.html): A key-value pair (the value is optional) that you can define and assign to AWS resources.
