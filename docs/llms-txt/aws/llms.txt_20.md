# Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/llms.txt

# Amazon CloudWatch Logs User Guide

> Monitor and store your log files from AWS sources. You can then retrieve the associated log data from CloudWatch Logs.

- [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
- [Sending logs using HLC endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_HLC_Endpoint.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/sdk-general-information-section.html)
- [Troubleshoot with CloudWatch Logs Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html)
- [Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html)
- [Access logs with S3 Tables Integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/s3-tables-integration.html)
- [Filter pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html)
- [Streaming data to OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html)
- [Logging API and console operations with AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/logging_cw_api_calls_cwl.html)
- [Monitoring usage with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html)
- [Service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html)
- [Document history](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/DocumentHistory_cwl.html)
- [AWS Glossary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/glossary.html)

## [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

- [Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html): The terminology and concepts that are central to your understanding and use of CloudWatch Logs are described below.
- [Billing and costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsBillingDetails.html): For detailed information about how to analyze your costs and usage for CloudWatch Logs and CloudWatch, and for best practices about how to reduce your costs, see CloudWatch billing and cost.


## [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html)

- [Prerequisites](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/GettingSetup_cwl.html): Get started with Amazon CloudWatch Logs by ensuring that you have an AWS account and install the command line interface.
- [Using the unified CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/UseCloudWatchUnifiedAgent.html): How to use the unified CloudWatch agent to get started using CloudWatch Logs.

### [Using the previous CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/UsePreviousCloudWatchLogsAgent.html)

How to use the older CloudWatch Logs agent to get started using CloudWatch Logs.

- [Quick Start: Install the agent on a running EC2 Linux instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html): Install and configure the CloudWatch Logs agent on an existing EC2 instance.
- [Quick Start: Install the agent on an EC2 Linux instance at launch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/EC2NewInstanceCWL.html): Install and configure the CloudWatch Logs agent when launching a new EC2 instance.
- [Quick Start: Use CloudWatch Logs with Windows Server 2016 instances](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartWindows2016.html): Enable your Windows Server 2016 instances to send logs to CloudWatch Logs.
- [Quick Start: Use CloudWatch Logs with Windows Server 2012 and Windows Server 2008 instances](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartWindows20082012.html): Enable your Windows Server 2012 and Windows Server 2008 instances to send logs to CloudWatch Logs.
- [Report the CloudWatch Logs agent status](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ReportCWLAgentStatus.html): Determine the current status of the CloudWatch Logs agent.
- [Start the CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/StartTheCWLAgent.html): Start the CloudWatch Logs agent.
- [Stop the CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/StopTheCWLAgent.html): Stop the CloudWatch Logs agent.
- [CloudWatch Logs agent reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html): Describes the CloudWatch Logs agent.
- [Quick Start with CloudFormation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartCloudFormation.html): Use CloudFormation to provision CloudWatch Logs repeatedly across your web servers.


## [Log management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogManagement.html)

- [Data source discovery and management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-source-discovery-management.html): CloudWatch Logs automatically discovers and categorizes your log data by data source and type, making it easier to understand and manage your logs at scale.
- [Features enabled by data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/features-enabled-by-data-sources.html): Data sources enable advanced log processing and analytics capabilities through field discovery and consistent data structures.
- [Supported AWS services for data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/supported-aws-services-data-sources.html): The following table lists the AWS services that are automatically categorized by CloudWatch Logs as data sources:
- [Supported third-party sources for data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/supported-third-party-sources-data-sources.html): The following table lists the third-party sources that are automatically categorized by CloudWatch Logs as data sources when ingested through pipelines:


## [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)

### [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html)

The following sections list the commands supported in each query language.

### [CloudWatch Logs Insights query language (Logs Insights QL)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_LogsInsights.html)

This section includes full documentation of Logs Insights QL commands and functions.

### [CloudWatch Logs Insights language query syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)

This section provides details about the Logs Insights QL.

- [Logs Insights QL commands supported in log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Classes.html): All Logs Insights QL query commands are supported on log groups in the Standard log class.
- [anomaly](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Anomaly.html): Use anomaly to automatically identify unusual patterns and potential issues within your log data using machine learning.
- [display](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Display.html): Use display to show a specific field or fields in query results.
- [fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Fields.html): Use fields to show specific fields in query results.
- [filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Filter.html): Use filter to get log events that match one or more conditions.
- [filterIndex](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-FilterIndex.html): Use filterIndex to return indexed data only, by forcing a query to scan only log groups that are indexed on a field that you specify in the query.
- [SOURCE](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html): Including SOURCE in a query is a useful way to specify the log groups and/or data sources to include in a query when you are using the AWS CLI or API to create a query.
- [pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Pattern.html): Use pattern to automatically cluster your log data into patterns.
- [diff](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Diff.html): Compares the log events found in your requested time period with the log events from a previous time period of equal length.
- [parse](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Parse.html): Use parse to extract data from a log field and create an extracted field that you can process in your query. parse supports both glob mode using wildcards, and regular expressions.
- [sort](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Sort.html): Use sort to display log events in ascending (asc) or descending (desc) order by a specified field.
- [stats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Stats.html): Use stats to create visualizations of your log data such as bar charts, line charts, and stacked area charts.
- [limit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Limit.html): Use limit to specify the number of log events that you want your query to return.
- [dedup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Dedup.html): Use dedup to remove duplicate results based on specific values in fields that you specify.
- [unmask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Unmask.html): Use unmask to display all the content of a log event that has some content masked because of a data protection policy.
- [unnest](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Unnest.html): Use unnest to flatten a list taken as input to produce multiple records with a single record for each element in the list.
- [lookup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Lookup.html): Use lookup to enrich your query results with reference data from a lookup table.
- [Boolean, comparison, numeric, datetime, and other functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-operations-functions.html): CloudWatch Logs Insights supports many other operations and functions in queries, as explained in the following sections.
- [Fields that contain special characters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Guidelines.html): If a field contains non-alphanumeric characters other than the @ symbol or the period (.), you must surround the field with backtick characters (`).
- [Use aliases and comments in queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-alias.html): Create queries that contain aliases.

### [Get started with Logs Insights QL: Query tutorials](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Tutorials.html)

The following sections include sample query tutorials to help you get started with Logs Insights QL.

- [Tutorial: Run and modify a sample query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_RunSampleQuery.html): The following tutorial helps you get started with CloudWatch Logs Insights.
- [Tutorial: Run a query with an aggregation function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_AggregationQuery.html): You can use aggregation functions with the stats command and as arguments for other functions.
- [Tutorial: Run a query that produces a visualization grouped by log fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_VisualizationFieldQuery.html): When you run a query that uses the stats function to group the returned results by the values of one or more fields in the log entries, you can view the results as a bar chart, pie chart, line graph or stacked area graph.
- [Tutorial: Run a query that produces a time series visualization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_VisualizationQuery.html): When you run a query that uses the bin() function to group the returned results by a time period, you can view the results as a line graph, stacked area graph, pie chart, or bar chart.
- [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html): Lists useful examples of CloudWatch Logs Insights queries that illustrate the query syntax.
- [Compare (diff) with previous time ranges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Compare.html): Learn how to compare log events and patterns with those found in previous time periods in CloudWatch Logs.
- [Visualize log data in graphs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Insights-Visualizing-Log-Data.html): Explains how to find patterns in your CloudWatch Logs data with visualizations such as graphs.
- [OpenSearch Piped Processing Language (PPL)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_PPL.html): This section contains a basic introduction to querying CloudWatch Logs using OpenSearch PPL.
- [OpenSearch Structured Query Language (SQL)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_SQL.html): This section contains a basic introduction to querying CloudWatch Logs using OpenSearch SQL.
- [Use natural language to generate and update CloudWatch Logs Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html): Learn how to create queries using natural language .
- [Supported logs and discovered fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html): CloudWatch Logs Insights supports different log types.

### [Create field indexes to improve query performance and reduce scan volume](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html)

Learn how to create field indexes in log events to improve performance and reduce the scan volume of your CloudWatch Logs Insights queries.

- [Field index syntax and quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax.html): You create field indexes by creating field index policies.
- [Create an account-level field index policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-CreateAccountLevel.html): Use the steps in this section to create a field index policy that applies to all log groups in the account, or to multiple log groups that have log group names that start with the same string.
- [Create a log-group level field index policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-CreateLogGroupLevel.html): Use the steps in this section to create a field index policy that applies to a single log group.
- [Log group selection options when creating a query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Field-Indexing-Selection.html): This section explains the various ways that you can select log groups to include in a query.
- [Effects of deleting a field index policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Deletion.html): If you delete a field index policy that has been in effect for a time, the following happens:
- [Use facets to group and explore logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html): Learn how to use facets to interactively filter and group your data without running queries.
- [Pattern analysis](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Patterns.html): Learn how to find and analyze patterns in your log events in CloudWatch Logs.
- [Save and re-run queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Insights-Saving-Queries.html): Explains how to save queries and run saved queries in CloudWatch Logs Insights.
- [Add query to dashboard or export query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ExportQueryResults.html): How to add a CloudWatch Logs Insights query to a CloudWatch dashboard and how to export CloudWatch Logs Insights query results.
- [View running queries or query history](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-History.html): How to view CloudWatch Logs Insights query history and currently running queries.
- [Encrypt query results with AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Encrypt.html): Learn how to use a AWS KMS key to encrypt the results of your CloudWatch Logs Insights queries.
- [Generate a natural language summary from CloudWatch Logs Insights query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html): Learn how to generate an AI-powered natural language summary from CloudWatch Logs Insights query results.


## [Automating log analysis with scheduled queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ScheduledQueries.html)

- [Understanding scheduled queries concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-concepts.html): Before creating scheduled queries, understand these key concepts that affect how your queries run and where results are delivered.
- [Schedule expression reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-schedule-reference.html): Use these reference tables to construct schedule expressions for your scheduled queries.
- [Best practices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-best-practices.html): Follow these best practices to ensure reliable and efficient scheduled query operations:

### [Getting started with scheduled queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-getting-started.html)

When you create a scheduled query, you'll configure several key components that define how your query runs and where results are delivered.

- [Creating a scheduled query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/create-scheduled-query.html): Create a scheduled query that automatically runs CloudWatch Logs Insights queries and delivers results to your chosen destinations.
- [Viewing and managing scheduled queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-management.html): The following information is available for each query:
- [Viewing scheduled query execution history](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-execution-history.html): Use the execution history to monitor the performance of your scheduled queries and troubleshoot any issues with query execution or result delivery.
- [Updating a scheduled query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-updating.html): Modify your scheduled query configuration to change the query string, schedule, destinations, or execution role as your requirements evolve.
- [Configuring S3 destinations for scheduled queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-s3-destination.html): Configure Amazon S3 as a destination to store your scheduled query results as JSON files for long-term retention and analysis.
- [Troubleshooting scheduled queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-troubleshooting.html): Use these troubleshooting topics to resolve common issues with scheduled queries.


## [Log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html)

- [Using anomaly detection in CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Insights.html): In addition to creating log anomaly detectors for continuous monitoring, you can also use the anomaly command in CloudWatch Logs Insights queries to identify unusual patterns in your log data on-demand.
- [Enable anomaly detection on a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Enable.html): Use the following steps to use the CloudWatch console to create a log anomaly detector that scans a log group for anomalies.
- [View anomalies that have been found](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-View.html): After you create one or more log anomaly detectors, you can use the CloudWatch console to view the anomalies that they have found.
- [Create alarms on log anomaly detectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Alarms.html): You can create an alarm for a log anomaly detector in a log group.
- [Metrics published by log anomaly detectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Metrics.html): CloudWatch Logs publishes the AnomalyCount metric to CloudWatch metrics.
- [Encrypt an anomaly detector and its results with AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html): Anomaly detector data is always encrypted in CloudWatch Logs.


## [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)

- [Search log data using filter patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html): Search CloudWatch Logs data using filter patterns.
- [Protect log groups from deletion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protecting-log-groups-from-deletion.html): Enable deletion protection to prevent accidental deletion of important log groups.
- [Encrypt log data using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html): Enable AWS KMS encryption for CloudWatch Logs at the log group level.

### [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html)

Explains how to protect sensitive data that appears in log groups in CloudWatch Logs by masking it.

- [Understanding data protection policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-data-protection-policies.html): Learn about data protection policies in CloudWatch Logs.
- [IAM permissions required to create or work with a data protection policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-protection-policy-permissions.html): Learn what permissions you need to be able to create a data protection policy for a log group in CloudWatch Logs.
- [Create an account-wide data protection policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-accountlevel.html): Learn how to create a data protection policy to protect sensitive data in all CloudWatch Logs log groups in an AWS account.
- [Create a data protection policy for a single log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-start.html): Learn how to create a data protection policy to protect sensitive data in CloudWatch Logs log groups.
- [View unmasked data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-viewunmasked.html): Learn how to view data that has been protected by a data protection policy in CloudWatch Logs log groups.
- [Audit findings reports](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-audit-findings.html): Learn how to understand audit findings reports created with Amazon CloudWatch Logs data protection masking.

### [Types of data that you can protect](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html)

Learn about what types of sensitive data in log files you can protect with masking, in CloudWatch Logs.

### [CloudWatch Logs managed data identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-managed-data-identifiers.html)

This section contains information about the types of data that you can protect using managed data identifiers, and which countries and regions are relevant for each of those types of data.

- [Credentials](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-credentials.html): CloudWatch Logs data protection can find the following types of credentials.
- [Device identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-device.html): CloudWatch Logs data protection can find the following types of device identifiers.
- [Financial information](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-financial.html): CloudWatch Logs data protection can find the following types of financial information.
- [Protected health information (PHI)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-health.html): CloudWatch Logs data protection can find the following types of protected health information (PHI).
- [Personally identifiable information (PII)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-pii.html): CloudWatch Logs data protection can find the following types of personally identifiable information (PII).
- [Custom data identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html): Learn how to create custom data identifiers to use to specify types of custom data to mask in CloudWatch Logs.


## [Transform logs during ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html)

### [Create and manage log transformers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Create.html)

A log transformer includes one or more processors that are in a logical pipeline together.

- [Create an account-level transformer policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Transformer-CreateAccountLevel.html): Use the steps in this section to create a transformer policy that applies to all log groups in the account, or to multiple log groups that have log group names that start with the same string (prefix).
- [Edit or delete an account-level transformer policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Transformer-EditAccountLevel.html): Use the steps in this section to edit or delete an account-level transformer policy.
- [Create a log-group-level log transformer from scratch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-CreateNew.html): Use these steps to create a log-group-level transformer from scratch.
- [Create a log-group-level transformer by copying an existing one](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Copy.html): You can use the console to copy the JSON configuration of an existing transformer.
- [Edit a log-group-level transformer](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Edit.html): Use these steps to edit an existing log transformer.
- [Delete a log-group-level transformer](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Delete.html): Use these steps to delete a log transformer.
- [Configurable parser-type processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Configurable.html): This section contains information about the configurable data parser processors that you can use in a log event transformer.

### [Built-in processors for AWS vended logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-BuiltIn.html)

This section contains information about the built-in processors that you can use with AWS services that vend logs.

- [parseToOCSF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-parseToOCSF.html): The parseToOCSF processor converts logs into Open Cybersecurity Schema Framework (OCSF) events.
- [String mutate processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-StringMutate.html): This section contains information about the string mutate processors that you can use with a log event transformer.
- [JSON mutate processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-JSONMutate.html): This section contains information about the JSON mutate processors that you can use with a log event transformer.
- [Datatype converter processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Datatype.html): This section contains information about the datatype converter processors that you can use with a log event transformer.
- [Transformation metrics and errors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html): CloudWatch Logs publishes transformation metrics to CloudWatch.


## [Analyze with Amazon OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-OpenSearch-Dashboards.html)

- [Step 1: Create the integration with OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-Integrate.html): The first step is creating the integration with OpenSearch Service, which you need to do only once.
- [Step 2: Create vended logs dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-Create.html): After you have created the integration, you can create dashboards.
- [View, edit, or delete vended logs dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-Manage.html)
- [IAM policies for users](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html): CloudWatch Logs has created two IAM policies, CloudWatchOpenSearchDashboardsFullAccess and CloudWatchOpenSearchDashboardAccess.
- [Permissions that the integration needs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html): If you create an IAM role for the integration to use, instead of allowing CloudWatch Logs to create the role, it must include the following permissions and trust policy.


## [Metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)

- [Filter pattern syntax for metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntaxForMetricFilters.html): Match terms and extract values in log events using metric filters and filter patterns in CloudWatch Logs.

### [Creating metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringPolicyExamples.html)

Create metric filters based on examples to search log data using CloudWatch Logs.

- [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html): How to create a metric filter that publishes a metric to CloudWatch based on the contents of a log group.
- [Example: Count log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CountingLogEventsExample.html): CloudWatch Logs metric filter example that shows how to count log events.
- [Example: Count occurrences of a term](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CountOccurrencesExample.html): CloudWatch Logs metric filter example that shows how to count the occurrences of a word.
- [Example: Count HTTP 404 codes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Counting404Responses.html): CloudWatch Logs metric filter example that shows how to count HTTP 404 responses.
- [Example: Count HTTP 4xx codes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FindCountMetric.html): CloudWatch Logs metric filter example that shows how to count log events into a single metric.
- [Example: Extract fields from an Apache log and assign dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ExtractBytesExample.html): CloudWatch Logs metric filter example that shows how to extract the number of bytes transferred from an Apache log.
- [Listing metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ListingMetricFilters.html): List all CloudWatch Logs metric filters in a group.
- [Deleting a metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/DeletingMetricFilter.html): Delete a CloudWatch Logs metric filter.


## [Subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html)

- [Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/subscription-concepts.html): Each subscription filter is made up of the following key elements:
- [Log group-level subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html): Associate a subscription filter with a log group containing AWS CloudTrail events.
- [Account-level subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters-AccountLevel.html): Learn how to use account-level subscription filters in CloudWatch Logs.

### [Cross-account cross-Region subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.html)

Use CloudWatch Logs to share log data with cross-account subscriptions, using either Firehose or Amazon Kinesis.

### [Cross-account cross-Region log data sharing using Amazon Kinesis Data Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Kinesis.html)

Use CloudWatch Logs to share log data with cross-account subscriptions, using Amazon Kinesis Data Streams.

### [Setting up a new cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-New.html)

Use Amazon Kinesis Data Streams to create a new subscription for cross-account CloudWatch Logs data sharing.

- [Step 1: Create a destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateDestination.html): Use Amazon Kinesis Data Streams to create a destination for cross-account CloudWatch Logs data.
- [Step 2: (Only if using an organization) Create an IAM role](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilter-IAMrole.html): Create an IAM role if you're using AWS Organizations with your cross-account log subscription.
- [Step 3: Add/validate IAM permissions for the cross-account destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscription-Filter-CrossAccount-Permissions.html): Explains how to validate IAM permissions when you set up a cross-account subscription with Amazon Kinesis Data Streams.
- [Step 4: Create a subscription filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilter.html): Create a subscription filter so that cross-account users can send you their CloudWatch Logs events.
- [Validate the flow of log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ValidateLogEventFlow.html): Create a subscription filter so that cross-account users can send you their CloudWatch Logs events.
- [Modify destination membership at runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ModifyDestinationMembership.html): Add or remove users from a cross-account subscription destination used by CloudWatch Logs.

### [Updating an existing cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update.html)

How to update an existing subscription for cross-account CloudWatch Logs data sharing to use AWS Organizations.

- [Step 1: Update the subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update-filter.html)
- [Step 2: Update the existing destination access policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update-policy.html): After you have updated the subscription filters in all of the sender accounts, you can update the destination access policy in the recipient account.

### [Cross-account cross-Region log data sharing using Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose.html)

Use CloudWatch Logs to share log data with cross-account subscriptions, using Firehose.

- [Step 1: Create a Firehose delivery stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateFirehoseStream.html)
- [Step 2: Create a destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateFirehoseStreamDestination.html)
- [Step 3: Add/validate IAM permissions for the cross-account destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscription-Filter-CrossAccount-Permissions-Firehose.html): Explains how to validate IAM permissions when you set up a cross-account subscription with Amazon Kinesis.
- [Step 4: Create a subscription filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilterFirehose.html): Create a subscription filter so that cross-account users can send you their CloudWatch Logs events using Firehose.
- [Validating the flow of log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ValidateLogEventFlowFirehose.html): Create a subscription filter so that cross-account users can send you their CloudWatch Logs events to a Firehose delivery stream in another account..
- [Modifying destination membership at runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ModifyDestinationMembershipFirehose.html): Add or remove users from a cross-account subscription destination used by CloudWatch Logs.

### [Cross-account cross-Region account-level subscriptions using Amazon Kinesis Data Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Kinesis-Account.html)

Use CloudWatch Logs at the account level to share log data with cross-account subscriptions, using Amazon Kinesis Data Streams.

### [Setting up a new cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-New-Account.html)

Use Amazon Kinesis Data Streams to create a new subscription for cross-account CloudWatch Logs data sharing.

- [Step 1: Create a destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateDestination-Account.html): Use Amazon Kinesis Data Streams to create a destination for cross-account CloudWatch Logs data.
- [Step 2: (Only if using an organization) Create an IAM role](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilter-IAMrole-Account.html): Create an IAM role if you're using AWS Organizations with your cross-account log subscription.
- [Step 3: Create an account-level subscription filter policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilter-Account.html): Create an account-level subscription filter so that cross-account users can send you their CloudWatch Logs events.
- [Validate the flow of log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ValidateLogEventFlow-Account.html): Create an account-level subscription filter policy so that cross-account users can send you their CloudWatch Logs events.
- [Modify destination membership at runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ModifyDestinationMembership-Account.html): Add or remove users from a cross-account subscription destination used by CloudWatch Logs.

### [Updating an existing cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update-Account.html)

How to update an existing subscription for cross-account CloudWatch Logs data sharing to use AWS Organizations.

- [Step 1: Update the subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update-filter-Account.html)
- [Step 2: Update the existing destination access policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update-policy-Account.html): After you have updated the subscription filters in all of the sender accounts, you can update the destination access policy in the recipient account.

### [Cross-account cross-Region account-level subscriptions using Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose-Account.html)

Use CloudWatch Logs to share log data with cross-account subscriptions, using Firehose.

- [Step 1: Create a Firehose delivery stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateFirehoseStream-Account.html)
- [Step 2: Create a destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateFirehoseStreamDestination-Account.html)
- [Step 3: Create an account-level subscription filter policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilterFirehose-Account.html): Create a subscription filter policy so that cross-account users can send you CloudWatch Logs events from all of their log groups using Firehose.
- [Validating the flow of log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ValidateLogEventFlowFirehose-Account.html): Create a subscription filter so that cross-account users can send you their CloudWatch Logs events to a Firehose delivery stream in another account..
- [Modifying destination membership at runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ModifyDestinationMembershipFirehose-Account.html): Add or remove users from a cross-account subscription destination used by CloudWatch Logs.
- [Confused deputy prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-confused-deputy.html): How to guard against the confused deputy security problem in CloudWatch Logs subscriptions.
- [Log recursion prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html): Learn how to prevent infinite loops of log recursion when you set up subscription filters in CloudWatch Logs.


## [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

### [Logging that requires additional permissions [V1]](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions.html)

Explains the permissions necessary for some AWS services to send their logs to CloudWatch Logs, Amazon S3, and Firehose.

- [Logs sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-CWL.html)
- [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-S3.html): When you set logs to be sent to Amazon S3, AWS creates or changes the resource policies associated with the S3 bucket that is receiving the logs, if needed.
- [Logs sent to Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-Firehose.html): This section applies when the types of logs listed in the table in the preceding section are sent to Firehose:

### [Logging that requires additional permissions [V2]](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.html)

Explains the permissions necessary for some AWS services to send their logs to CloudWatch Logs, Amazon S3, Firehose, and X-Ray.

- [Logs sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-CloudWatchLogs.html): User permissions
- [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html): User permissions
- [Logs sent to Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.html): User permissions
- [Traces sent to X-Ray](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-XRayTraces.html): User permissions
- [Service-specific permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-service-specific.html): In addition to the destination-specific permissions listed in the previous sections, some services require explicit authorization that customers are allowed to send logs from their resources, as an additional layer of security.
- [Console-specific permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-console.html): In addition to the permissions listed in the previous sections, if you are setting up log delivery using the console instead of the APIs, you also need the following additional permissions:
- [Cross-account delivery example](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/vended-logs-crossaccount-example.html): In this example, two accounts are involved.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html)

- [Export log data to Amazon S3 using the console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasksConsole.html): Learn how to export logs to Amazon S3 using the AWS console.
- [Export log data to Amazon S3 using the AWS CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasks.html): Learn how to export logs to Amazon S3 using the AWS CLI.
- [Describe export tasks (CLI)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/DescribeExportTasks.html): After you create an export task, you can get the current status of the task.
- [Cancel an export task (CLI)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CancelExportTask.html): You can cancel an export task if it's in a PENDING or RUNNING state.


## [Code examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/service_code_examples_basics.html)

The following code examples show how to use the basics of CloudWatch Logs with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/service_code_examples_actions.html)

The following code examples show how to use CloudWatch Logs with AWS SDKs.

- [AssociateKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_AssociateKmsKey_section.html): Use AssociateKmsKey with an AWS SDK
- [CancelExportTask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CancelExportTask_section.html): Use CancelExportTask with an AWS SDK
- [CreateExportTask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateExportTask_section.html): Use CreateExportTask with an AWS SDK
- [CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogGroup_section.html): Use CreateLogGroup with an AWS SDK or CLI
- [CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogStream_section.html): Use CreateLogStream with an AWS SDK or CLI
- [DeleteLogGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DeleteLogGroup_section.html): Use DeleteLogGroup with an AWS SDK or CLI
- [DeleteSubscriptionFilter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DeleteSubscriptionFilter_section.html): Use DeleteSubscriptionFilter with an AWS SDK
- [DescribeExportTasks](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DescribeExportTasks_section.html): Use DescribeExportTasks with an AWS SDK
- [DescribeLogGroups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DescribeLogGroups_section.html): Use DescribeLogGroups with an AWS SDK or CLI
- [DescribeLogStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DescribeLogStreams_section.html): Use DescribeLogStreams with an AWS SDK or CLI
- [DescribeSubscriptionFilters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DescribeSubscriptionFilters_section.html): Use DescribeSubscriptionFilters with an AWS SDK
- [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_GetLogEvents_section.html): Use GetLogEvents with an AWS SDK or CLI
- [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_GetQueryResults_section.html): Use GetQueryResults with an AWS SDK
- [PutSubscriptionFilter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_PutSubscriptionFilter_section.html): Use PutSubscriptionFilter with an AWS SDK
- [StartLiveTail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartLiveTail_section.html): Use StartLiveTail with an AWS SDK
- [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartQuery_section.html): Use StartQuery with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/service_code_examples_scenarios.html)

The following code examples show how to use CloudWatch Logs with AWS SDKs.

- [Run a large query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_Scenario_BigQuery_section.html): Use CloudWatch Logs to run a large query
- [Use scheduled events to invoke a Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cross_LambdaScheduledEvents_section.html): Use scheduled events to invoke a Lambda function


## [Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/security.html)

- [Data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon CloudWatch Logs.

### [Identity and access management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/auth-and-access-control-cwl.html)

Control user access using IAM policies to specify which CloudWatch Logs actions a user in your AWS account can perform.

- [Overview of managing access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html): Describes how account administrators can manage access to resources by attaching permissions policies to IAM identities.

### [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html)

Provides examples of IAM identity-based policies for controlling access to Amazon CloudWatch Logs.

- [CloudWatch Logs permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html): Describes the Amazon CloudWatch Logs API operations and the corresponding actions you grant permissions to perform.
- [Using service-linked roles](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/using-service-linked-roles-cwl.html): How to use service-linked roles to give CloudWatch Logs access to resources in your AWS account.
- [Policy updates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cwl-slrpolicy-updates.html)
- [Compliance validation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon CloudWatch Logs features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/infrastructure-security.html): Learn how Amazon CloudWatch Logs isolates service traffic.
- [Interface VPC endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html): Explains how to use CloudWatch Logs with interface VPC endpoints.
