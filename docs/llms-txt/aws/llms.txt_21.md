# Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/llms.txt

# Amazon CloudWatch User Guide

> Monitor your AWS services, collect and track metrics from AWS services and your own applications, and set alarms based on data from those metrics.

- [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Getting set up](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html)
- [Analyzing, optimizing, and reducing CloudWatch costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_billing.html)
- [Services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)
- [FAQs on CloudWatch supported protocols](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-protocols-faq.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sdk-general-information-section.html)
- [Logging API and console operations with AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/logging_cw_api_calls.html)
- [Tagging your CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)
- [Grafana integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Grafana-support.html)
- [Service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html)
- [Document history](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/DocumentHistory.html)

## [Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)

### [Getting started with automatic dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html)

Helps customers quickly get productive using Amazon CloudWatch, using the overview and automatic dashboards.

- [Viewing the cross-service dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.html): View the CloudWatch Cross-service dashboard to see key metrics from all AWS services.
- [Removing a service from appearing in the cross-service dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Remove_service_from_Cross_Service_Dashboard.html): Steps to remove a service's metrics from appearing in the CloudWatch cross-service dashboard.
- [Viewing a dashboard for a single service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Focus_Service.html): Learn how to drill down for more information about a particular AWS service using the CloudWatch home page.
- [Viewing a dashboard for a resource group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Resource_Group.html): Steps to focus your CloudWatch view on metrics and alarms from a single resource group.
- [Creating a customized dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html): Learn how to create a CloudWatch dashboard to track metrics for your AWS resources.
- [Creating a cross-account cross-Region dashboard with the console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_xaxr_dashboard.html): Learn how to create a cross-account, cross-Region dashboard using the AWS Management Console.
- [Adding an alarm from a different account to a cross-account dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-alarm-xaxr-dashboard.html): Steps to add an alarm from a different account to a cross-account cross-Region dashboard.

### [Creating dashboards with variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html)

Explains how to use dashboard variables to create dynamic Amazon CloudWatch dashboards.

- [Copying a variable to another dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables_copy.html): Demonstrates how to copy an Amazon CloudWatch dashboard variable to other dashboards.
- [Tutorial: Using a regular expression pattern to switch between Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables_pattern.html): Demonstrates how to use a pattern variable to create a flexible Amazon CloudWatch dashboard.
- [Tutorial: Creating dashboard with the Lambda function name as a variable](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables_property.html): Demonstrates how to use a property variable to create a flexible Amazon CloudWatch dashboard.

### [Using widgets on dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html)

Steps for adding, removing, and editing graphs and other widgets in a CloudWatch dashboard.

- [Adding a graph widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_graph_dashboard.html): How to add graphs to a CloudWatch dashboard.
- [Removing a graph widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_graph_dashboard.html): How to remove graphs from a CloudWatch dashboard.
- [Graph metrics manually on a dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_old_metrics_to_graph.html): Steps to add metrics that haven't published data in 14 days to a CloudWatch graph.
- [Editing a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/edit_graph_dashboard.html): How to edit graph data on a CloudWatch dashboard.
- [Renaming a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/rename_graph_dashboard.html): Change the name of a graph on a CloudWatch dashboard.
- [Moving a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/move_graph_dashboard.html): Steps to move or resize graphs on a CloudWatch dashboard.
- [Add a metrics explorer widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_metrics_explorer_dashboard.html): Steps to add a metrics explorer widget on a CloudWatch dashboard.
- [Adding a line graph widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_line_dashboard.html): Steps to add a line graph widget to a CloudWatch dashboard.
- [Removing a line graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_line_dashboard.html): Steps to remove a line graph widget from a CloudWatch dashboard.
- [Adding a number widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_number_dashboard.html): Steps to add a widget to display a number on a CloudWatch dashboard.
- [Removing a number widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_number_dashboard.html): Steps to remove a widget to display a number from a CloudWatch dashboard.
- [Adding a gauge widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_gauge_dashboard.html): Steps to add a gauge widget to a CloudWatch dashboard.
- [Removing a gauge widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_gauge_dashboard.html): Steps to remove a gauge widget from a CloudWatch dashboard.

### [Using a custom widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.html)

Learn about custom widgets on a CloudWatch dashboard, including security considerations, interactivity options, and sample custom widget code.

- [Details about custom widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_about.html): Information about custom CloudWatch widgets, including how they work, how they are styled, and sample code.
- [Security and JavaScript](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_security.html): Information about why JavaScript is not allowed in returned HTML of custom CloudWatch widgets.
- [Interactivity in custom widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_interactivity.html): Information about ways to include interactivity in custom CloudWatch widgets, including example code.
- [Creating a custom widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_create.html): Steps to create a custom widget for a CloudWatch dashboard.
- [Sample custom widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_samples.html): Access sample custom widgets.
- [Adding a text widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_text_dashboard.html): Steps to add a text widget to a CloudWatch dashboard.
- [Editing a text widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/edit_text_dashboard.html): Steps to change the text in a text widget on a CloudWatch dashboard.
- [Removing a text widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_text_dashboard.html): Steps to remove a text widget from a CloudWatch dashboard.
- [Adding an alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_alarm_dashboard.html): Steps to add an alarm, including its graph, to a CloudWatch dashboard.
- [Adding an alarm status widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_alarm_widget_dashboard.html): Steps to add an alarm status widget to a CloudWatch dashboard.
- [Removing an alert widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_alarm_dashboard.html): Steps to remove an alarm widget from a CloudWatch dashboard.

### [Using a data table widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_remove_table_dashboard.html)

Information about a data table widget in a CloudWatch dashboard, including details of the types of data available to display in data tables.

- [Adding a data table widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_table_dashboard.html): Steps to add a data table widget to a CloudWatch dashboard.
- [Removing a data table widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/remove_table_dashboard.html): Steps to remove a data table widget from a CloudWatch dashboard.
- [Linking graphs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/link_graphs_dashboard.html): Steps to link graphs on a CloudWatch dashboard so that changes in time are reflected on all graphs.
- [Unlinking graphs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/unlink_graphs_dashboard.html): Steps to unlink graphs on a CloudWatch dashboard.

### [Sharing dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.html)

Learn about details of sharing your CloudWatch dashboards with people who don't have access to your AWS account, including information about pricing and permissions.

- [Sharing one dashboard with specific users](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-email-addresses.html): Steps to share your CloudWatch dashboards with specific users that you choose.
- [Sharing a dashboard publicly](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-public.html): Steps to share your CloudWatch dashboards publicly.
- [Sharing all dashboards using SSO](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-sso.html): Steps to share all of your CloudWatch dashboards with users by using single sign-on (SSO).
- [Setting up SSO](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboards-setup-SSO.html): Steps to set up single sign-on (SSO) to enable CloudWatch dashboard sharing.
- [Seeing how many of your dashboards are shared](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-how-many.html): Steps how to see how many of your CloudWatch dashboards are currently being shared.
- [Seeing which dashboards are shared](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-list.html): Steps to see which of your CloudWatch dashboards are currently being shared.
- [Stopping dashboard sharing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-stop.html): Steps to stop sharing a CloudWatch dashboard.
- [Reviewing and changing shared dashboard permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-review-permissions.html): Steps to review and change the permission scope of shared CloudWatch dashboards.

### [Using live data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-live-data.html)

Get information about whether to use live, unaggregated CloudWatch data on a single widget or your entire CloudWatch dashboard.

- [Using live data for a dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/live_data_dashboard.html): Steps to use live data for all widgets on a CloudWatch dashboard.
- [Using live data for a widget](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/live_data_widget.html): Steps to use live data for a widget on a CloudWatch dashboard.
- [Viewing an animated dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-animated-dashboard.html): How to view an animated CloudWatch dashboard to see CloudWatch metrics over time.
- [Add a dashboard to your favorites list](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add-dashboard-to-favorites.html): Learn how to add CloudWatch dashboards, alarms, and log groups to your favorites list.
- [Changing the period override setting or refresh interval](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/change_dashboard_refresh_interval.html): Steps to change how often data on a CloudWatch dashboard is refreshed or how the periods of graphs are retained or overridden.
- [Changing the time range or time zone format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/change_dashboard_time_format.html): Steps to change the time range and time zone format to display data on a CloudWatch dashboard.


## [Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

- [Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html): Describes the fundamentals, concepts, and terminology you need to know for working with Amazon CloudWatch metrics.
- [Basic and detailed monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html): Explains the difference between basic monitoring and detailed monitoring in CloudWatch, and lists the AWS services that offer detailed monitoring.

### [Query metrics with CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html)

Query your Amazon CloudWatch metrics with CloudWatch Metrics Insights, a powerful SQL query engine.

- [Building queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-buildquery.html): How to create a query in CloudWatch Metrics Insights.

### [Query components and syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage.html)

Explains the query language used in CloudWatch Metrics Insights.

- [Reserved keywords](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-reserved-keywords.html): Lists the reserved keywords that must have special syntax to be used in CloudWatch Metrics Insights queries.

### [Alarms on queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-alarms.html)

Describes CloudWatch alarms based on CloudWatch Metrics Insights queries.

- [Creating a Metrics Insights alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-alarm-create.html): Steps to create an CloudWatch alarm based on a Metrics Insights query.
- [Use Metrics Insights queries with metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-math.html): Explains how CloudWatch Metrics Insights and metric match can interoperate.
- [Use natural language to generate and update CloudWatch Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-query-assist.html): Learn how to create queries using natural language.
- [SQL inference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-inference.html): Explains the SQL inferences used in CloudWatch Metrics Insights.
- [Metrics Insights quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-limits.html): Explains the terminology used in CloudWatch Metrics Insights.
- [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-queryexamples.html): Sample queries that provide examples of useful queries in CloudWatch Metrics Insights.
- [Metrics Insights glossary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-glossary.html): Explains the terminology used in CloudWatch Metrics Insights.
- [Troubleshooting Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-troubleshooting.html): Troubleshooting tips for CloudWatch Metrics Insights.
- [Use metrics explorer to monitor resources by their tags and properties](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metrics-Explorer.html): Visualize your resources by their tags and properties by using CloudWatch metrics explorer.

### [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)

Use metric streams to stream CloudWatch metrics to a destination of your choice.

### [Set up a metric stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup.html)

Explains how to set up CloudWatch metric streams in the console and in the CLI.

- [Custom setup with Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup-datalake.html): Explains how to set up a CloudWatch metric stream to another AWS service using Firehose
- [Use Quick Amazon S3 setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup-Quick-S3.html): Explains how to set up a CloudWatch metric stream to Amazon S3 using Quick S3 Setup.
- [Quick partner setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-QuickPartner.html): Explains how to set up a CloudWatch metric stream to a third-party solution using the CloudWatch quick partner setup.
- [Statistics that can be streamed](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-statistics.html): Explains which CloudWatch statistics are included by default in a metric stream, and which statistics you can add to the stream for additional charges.
- [Metric stream operation and maintenance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-operation.html): How to operate and maintain your CloudWatch metric stream after it's set up.
- [Monitoring your metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-monitoring.html): Descriptions of metrics emitted by CloudWatch metric streams.
- [Trust between CloudWatch and Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-trustpolicy.html): Learn about setting up an IAM role for a trust relationship between the Firehose delivery stream and CloudWatch.
- [JSON output format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-json.html): Learn about the CloudWatch metric stream output in JSON format.

### [OpenTelemetry 1.0.0 output format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry-100.html)

Learn about the CloudWatch metric output stream in OpenTelemetry 1.0.0 format.

- [Translations with OpenTelemetry 1.0.0 format in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry-translation-100.html): Learn about how CloudWatch transforms some CloudWatch data for OpenTelemetry format.
- [How to parse OpenTelemetry 1.0.0 messages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry-parse-100.html): This section provides information to help you parse OpenTelemetry 1.0.0 messages, including code examples.

### [OpenTelemetry 0.7.0 output format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry.html)

Learn about the CloudWatch metric output stream in OpenTelemetry 0.7.0 format.

- [Translations with OpenTelemetry 0.7.0 format in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry-translation.html): Learn about how CloudWatch transforms some CloudWatch data for OpenTelemetry format.
- [How to parse OpenTelemetry 0.7.0 messages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats-opentelemetry-parse.html): This section provides information to help you parse OpenTelemetry 0.7.0 messages, including code examples.
- [Troubleshooting metric streams in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-troubleshoot.html): Learn about strategies to address issues that may occur when using CloudWatch metric streams.

### [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html)

Learn how to view the available metrics by category for the AWS services that you are using.

- [Search for available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/finding_metrics_with_cloudwatch.html): Search for available metrics in CloudWatch within all of the metrics in your account using targeted search terms.

### [Graphing metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_metrics.html)

Walks through how to graph metric data using the CloudWatch console.

- [Graph a metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_a_metric.html): Walks through how to select a metric and create a graph of the metric data in CloudWatch.
- [Merge two graphs into one](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/merge_graphs.html): Walks through how to merge two CloudWatch metrics graphs into one graph.
- [Use dynamic labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html): Explains how using dynamic labels can help make graphs clearer.
- [Modify the time range or time zone format for a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/modify_graph_date_time.html): Walks through how to modify the date, time, and time zone on a CloudWatch metrics graph.
- [Zooming in on a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/zoom-graph.html): Learn how to zoom in on a CloudWatch graph.
- [Modify the y-axis for a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/switch_graph_axes.html): Walks through how to customize the y-axis for a CloudWatch graph and switch between axes.
- [Create an alarm from a metric on a graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_alarm_metric_graph.html): Learn how to graph a metric and create an alarm from the metric in CloudWatch.
- [Using outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html): Explains how CloudWatch outlier detection works and how to use it with alarms and graphs of metrics.
- [Using math expressions with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html): Steps to use math expressions with CloudWatch metrics to create new time series.

### [Use search expressions in graphs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-search-expressions.html)

Use search expressions to create a CloudWatch graph that displays multiple related metrics and to create dynamic graphs.

- [Search expression syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/search-expression-syntax.html): Explains the syntax rules for search expressions in a CloudWatch graph.
- [Search expression examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/search-expression-examples.html): Lists examples of valid search expressions in a CloudWatch graph.
- [Creating a graph with a search expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-search-expression.html): How to create a CloudWatch Graph with a search expression

### [Get statistics for a metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/getting-metric-statistics.html)

Walks through common scenarios for getting statistics for a metric.

- [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html): The definitions of Amazon CloudWatch statistics, including trimmed mean, winsorized mean, trimmed count, percentile rank, trimmed sum, average, sum, min, max, and samplecount.
- [Get statistics for a specific resource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SingleMetricPerInstance.html): Walks through how to get statistics for a specific Amazon EC2 instance.
- [Aggregate statistics across resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GetSingleMetricAllDimensions.html): Walks through how to aggregate statistics across instances where you have enabled detailed monitoring.
- [Aggregate statistics by Auto Scaling group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GetMetricAutoScalingGroup.html): Walks through how to aggregate statistics across an Auto Scaling group.
- [Aggregating statistics by AMI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SingleMetricPerAMI.html): Walks through how to aggregate statistics according to a specified AMI ID.
- [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html): Walks through how to publish your own custom metrics in CloudWatch.


## [Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)

### [Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-concepts.html)

Learn about key concepts for CloudWatch alarms including evaluation, data queries, actions, and suppression.

- [Alarm data queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-data-queries.html): Configure data sources for CloudWatch alarms including metrics, metric math, composite alarms, and logs.

### [Alarm evaluation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation.html)

Understand how CloudWatch evaluates alarms including states, conditions, thresholds, and evaluation windows.

- [Configuring how alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html): Sometimes, not every expected data point for a metric gets reported to CloudWatch.
- [How partial data is handled](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-alarms-partial-data.html): Learn about how CloudWatch evaluates metrics matched by a Metrics Insights query.
- [Percentile-based alarms and low data samples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/percentiles-with-low-samples.html): When you set a percentile as the statistic for an alarm, you can specify what to do when there is not enough data for a good statistical assessment.

### [Composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-combining.html)

Explains how composite alarms work in CloudWatch, along with their benefits.

- [Alarm suppression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-suppression.html): Temporarily suppress alarm notifications during maintenance windows or known issues.
- [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-actions.html): Configure actions that CloudWatch alarms trigger when changing state.

### [Alarm Mute Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-mute-rules.html)

Learn how to automatically mute alarm actions during predefined time windows.

- [How alarm mute rules work](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-mute-rules-behaviour.html): The following scenarios illustrate how alarm mute rules affect the targeted alarms and how the alarm actions are muted or executed.
- [Limits](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-limits.html)

### [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-getting-started.html)

Step-by-step examples for creating different types of CloudWatch alarms.

### [Create alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-Alarms.html)

Learn how to create different types of CloudWatch alarms.

- [Create an alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html): Create an CloudWatch alarm based on a static threshold.
- [Create an alarm based on a metric math expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html): Create a CloudWatch alarm that is based on the result of a metric math expression.
- [Create an alarm based on outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html): Create an CloudWatch alarm based on outlier detection models.
- [Create a multi time series alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/multi-time-series-alarm.html): Walks through how to create an alarm that monitors metrics across a fleet of resources.
- [Create an alarm based on a connected data source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_MultiSource_Alarm.html): Learn how to create a CloudWatch alarm that watches data from a data source that is not CloudWatch.
- [Alarming on logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html): Explains how to create a CloudWatch alarm that watches logs.
- [Create a composite alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html): Learn how to create a composite alarm with the following procedure.

### [Acting on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Acting_Alarm_Changes.html)

Explains how CloudWatch can notify users when alarms change state or change configuration, and how actions are handled for different alarm types.

- [Notifying users on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html): Explains how CloudWatch can notify users when alarms change state or change configuration.
- [Invoke a Lambda function from an alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-actions-Lambda.html): CloudWatch alarms guarantees an asynchronous invocation of the Lambda function for a given state change, except in the following cases:
- [Start a CloudWatch investigations from an alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Start-Investigation-Alarm.html): Start a CloudWatch investigations from an alarm, or from any point in the last two weeks of a CloudWatch alarm's history.
- [Stop, terminate, reboot, or recover an EC2 instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingAlarmActions.html): Stop, terminate, reboot, or recover your Amazon EC2 instances.
- [Alarm events and EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-eventbridge.html): Explains how CloudWatch sends events to EventBridge and CloudWatch Events for alarm state changes.
- [Configure alarm mute rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-mute-rules-configure.html): Learn how to create and configure alarm mute rules to automatically mute alarm actions during specific time windows.

### [Managing alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Manage-CloudWatch-Alarm.html)

Learn how to edit, delete, hide, and tag CloudWatch alarms.

- [Editing or deleting a CloudWatch alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Edit-CloudWatch-Alarm.html): Edit or delete an existing CloudWatch alarm.
- [Hide Auto Scaling alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/hide-autoscaling-alarms.html): When you view your alarms in the AWS Management Console, you can hide the alarms related to both Amazon EC2 Auto Scaling and Application Auto Scaling.
- [Alarms and tagging](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_alarms_and_tagging.html): Explains details about how tagging works with CloudWatch alarms
- [Viewing and managing muted alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing-managing-muted-alarms.html): View and manage alarms that are currently muted by alarm mute rules.

### [Alarm recommendations for AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html)

Explains the alarms that CloudWatch recommends as best-practice alarms to use for other AWS services.

- [Recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html): Lists the metrics that AWS recommends that you set alarms on to monitor your AWS infrastructure.

### [Alarm use cases and examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-Use-Cases.html)

Provides examples and tutorials for common CloudWatch alarm uses cases.

- [Create a billing alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html): Walks through how to monitor your estimated charges using CloudWatch.
- [Create a CPU usage alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_AlarmAtThresholdEC2.html): Walks through how to create an CloudWatch alarm that sends a notification based on CPU usage.
- [Create a load balancer latency alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_AlarmAtThresholdELB.html): Walks through how to create a load balancer alarm based on excess latency.
- [Create a storage throughput alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_AlarmAtThresholdEBS.html): Walks through how to create a storage throughput alarm based on Amazon EBS that exceeds 100-MB throughput.
- [Create an alarm on Performance Insights counter metrics from an AWS database](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.html): Walks through how to create an alarm based on Performance Insights metrics that you retrieve from Amazon RDS or Amazon DocumentDB.


## [Resource tags for telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-tags-for-telemetry.html)

- [Enable resource tags on telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EnableResourceTagsOnTelemetry.html): Use the CloudWatch console to enable resource tags for telemetry for your AWS account.
- [Using resource tags for telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html): Create tag-based Metrics Insights queries and alarms to monitor your AWS infrastructure by tags.
- [Disable resource tags on telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/DisableResourceTagsOnTelemetry.html): Turn off resource tags for telemetry when you no longer need the feature.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ResourceTagsTelemetryTroubleshooting.html): Common issues and solutions when working with resource tags for telemetry.


## [Audit and turn on AWS telemetry related configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html)

- [Turning on telemetry auditing and configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html): Learn how to enable and configure telemetry for your AWS account or organization using the CloudWatch console to discover resources and set up telemetry collection.
- [Viewing resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-view-resources.html): The Telemetry configuration and auditing experience displays AWS resources in two places: As an overview, on the Telemetry config page and in detail, on the Discovered data sources page.
- [Working with telemetry enablement rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-rules.html): Learn how to create and manage telemetry rules to standardize telemetry collection across your AWS resources.
- [Turning off telemetry configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-off.html): When you no longer need telemetry configuration, you can turn it off.


## [Infrastructure monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Insights-Sections.html)

### [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)

How to use Container Insights to collect metrics and logs from your containers.

- [Container Insights with enhanced observability for Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-detailed-ecs-metrics.html): How to use Container Insights with enhanced observability for Amazon ECS.
- [Container Insights with enhanced observability for Amazon EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-detailed-metrics.html): How to use Container Insights to with enhanced observability for Amazon EKS.

### [Setting up Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights.html)

How to install and set up CloudWatch Container Insights.

### [Setting up Container Insights on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html)

How to install and set up CloudWatch Container Insights on Amazon ECS.

- [Setting up Container Insights on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html): How to install and set up CloudWatch Container Insights on Amazon ECS.
- [Setting up Container Insights on Amazon ECS using AWS Distro for OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-adot.html): How to use AWS Distro for OpenTelemetry to set up CloudWatch Container Insights on Amazon ECS.
- [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-instancelevel.html): How to use the CloudWatch agent as a daemon service to collect instance-level metrics on your Amazon ECS clusters that are hosted on EC2 instances.
- [Deploying the AWS Distro for OpenTelemetry to collect EC2 instance-level metrics on Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-OTEL.html): How to use the AWS Distro for OpenTelemetry to collect instance-level metrics on your Amazon ECS clusters that are hosted on EC2 instances.
- [Set up FireLens to send logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-logs.html): How to use FireLens on Amazon ECS to send logs to CloudWatch Logs.

### [Setting up Container Insights on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html)

How to install and set up CloudWatch Container Insights on Amazon EKS or Kubernetes.

- [Verifying prerequisites](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-prerequisites.html): Information to verify about your Amazon EKS or Kubernetes configuration before installing Container Insights.

### [Using Container Insights enhanced observability enabled](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-agent.html)

Information on installing and setting up the CloudWatch Observability EKS add-on.

- [Quick start with the Amazon CloudWatch Observability EKS add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.html): Learn how to install the Amazon CloudWatch Observability EKS add-on, which you can use to enable CloudWatch Application Signals and CloudWatch Container Insights with enahanced observability for Amazon EKS.
- [Quick Start setup for Container Insights on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-quickstart.html): Information about setting up Container Insights in CloudWatch for Amazon EKS and Kubernetes quickly.
- [Setting up the CloudWatch agent to collect cluster metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-metrics.html): Information about setting up the CloudWatch Observability EKS add-on.
- [Using AWS Distro for OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-otel.html): Information about setting up Container Insights in CloudWatch to collect metrics from Amazon EKS clusters.

### [Send logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html)

How to set up CloudWatch Container Insights to send logs from containers to Amazon CloudWatch Logs.

- [Set up Fluent Bit as a DaemonSet to send logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs-FluentBit.html): Information about setting up Fluent bit to send logs to CloudWatch.
- [(Optional) Set up Amazon EKS control plane logging](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-control-plane-logging.html): Information about setting up optional Amazon EKS control plane logging in CloudWatch.
- [(Optional) Enable the Use_Kubelet feature for large clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-use-kubelet.html): Informating about enabling the Use_Kubelet feature for the FluentBit Kubernetes plugin in CloudWatch.

### [Updating or deleting Container Insights on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-update-delete.html)

Instructions for updating or deleting Container Insights.

- [Upgrading to Container Insights with enhanced observability for Amazon EKS in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-upgrade-enhanced.html): Information about upgrading or installing Container Insights on an Amazon EKS cluster using the Amazon CloudWatch Observability EKS add-on.
- [Updating the CloudWatch agent container image](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-update-image.html): Steps to update the CloudWatch agent container image to the latest version.
- [Deleting the CloudWatch agent and Fluent Bit for Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-delete-agent.html): Information about removing the CloudWatch agent for Container Insights.
- [Setting up Container Insights on RedHat OpenShift on AWS (ROSA)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-RedHatOpenShift.html): How to install and set up CloudWatch Container Insights on RedHat OpenShift on AWS (ROSA).
- [Viewing Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-view-metrics.html): Steps to view Container Insights metrics in the CloudWatch console.

### [Metrics collected by Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics.html)

Information about the metrics collected in CloudWatch by Container Insights.

- [Amazon ECS Container Insights with enhanced observability metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.html): Information about metrics and dimensions collected by Container Insights in CloudWatch from Amazon ECS.
- [Amazon ECS Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html): Information about metrics and dimensions collected by Container Insights in CloudWatch from Amazon ECS.

### [Amazon EKS and Kubernetes Container Insights with enhanced observability metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-enhanced-EKS.html)

Information about metrics and dimensions collected by Container Insights in CloudWatch for Amazon EKS and Kubernetes.

- [Amazon EKS and Kubernetes Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.html): Information about metrics and dimensions collected by Container Insights in CloudWatch for Amazon EKS and Kubernetes.

### [Performance log reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-reference.html)

Information about Container Insights performance logs events and collecting metrics in CloudWatch.

- [Performance log events for Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-reference-performance-logs-ECS.html): Information about performance events collected from Amazon ECS by container insights.
- [Performance log events for Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-reference-performance-logs-EKS.html): Information about performance events collected by Container Insights from Amazon EKS and Kubernetes clusters.
- [Relevant fields in performance log events for Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-reference-performance-entries-EKS.html): Information about performance log events generated by Amazon EKS and Kubernetes in Container Insights.

### [Container Insights Prometheus metrics monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus.html)

Explains how to use CloudWatch Container Insights to collect Prometheus metrics.

### [Set up and configure on Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-ECS.html)

Explains how to set up CloudWatch Container Insights to collect Prometheus metrics on Amazon ECS .

- [Set up on Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-install-ECS.html): Explains how to set up CloudWatch Container Insights to collect Prometheus metrics on Amazon ECS .

### [Scraping additional Prometheus sources and importing those metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure-ECS.html)

Explains how to import more Prometheus metrics and scrape more Prometheus sources in CloudWatch Container Insights

- [Detailed guide for autodiscovery on Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-autodiscovery-ecs.html): Information about setting up autodiscovery with Prometheus.

### [(Optional) Set up sample containerized Amazon ECS workloads for Prometheus metric testing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-ECS.html)

Information on setting up sample containerized Amazon ECS workloads against which to test Prometheus metrics collection.

- [Sample App Mesh workload for Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-ECS-appmesh.html): Information about collecting metrics from a sample Prometheus workload for Amazon ECS.
- [Sample Java/JMX workload for Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-ECS-javajmx.html): Information about setting up a sample workload to expose JMX mBeans as Prometheus metrics.
- [Sample NGINX workload for Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-nginx-ecs.html): Information about setting up NGNIX data as Prometheus metrics.
- [Sample NGINX Plus workload for Amazon ECS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-nginx-plus-ecs.html): Information about setting up a sample NGNIX Plus workload for Amazon ECS clusters.
- [Tutorial for adding a new Prometheus scrape target: Memcached on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-memcached-ecs.html): Information about setting up Prometheus to scrape memcashed on Amazon ECS.
- [Tutorial for scraping Redis OSS Prometheus metrics on Amazon ECS Fargate](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-redis-ecs.html): Information about setting up to screape Redis OSS Prometheus metrics on Amazon ECS Fargate.

### [Set up and configure on Amazon EKS and Kubernetes clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-install-EKS.html)

Explains how to set up CloudWatch Container Insights to collect Prometheus metrics on Amazon ECS .

### [Set up on Amazon EKS and Kubernetes clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup.html)

Explains how to set up CloudWatch Container Insights to collect Prometheus metrics on Amazon EKS and Kubernetes clusters.

- [Scraping additional Prometheus sources and importing those metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.html): Explains how to import more Prometheus metrics and scrape more Prometheus sources in CloudWatch Container Insights

### [(Optional) Set up sample containerized Amazon EKS workloads for Prometheus metric testing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads.html)

Information on installing and setting up sample containerized Amazon EKS workloads against which to test Prometheus metrics.

### [Set up AWS App Mesh sample workload for Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-appmesh.html)

Setting up Prometheus support in CloudWatch Container Insights for AWS App Mesh.

- [Set up AWS App Mesh sample workload on an Amazon EKS cluster with the EC2 launch type or a Kubernetes cluster](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-appmesh-EKS.html): Information about setting up an AWS App Mesh sample workload on an Amazon EKS cluster.
- [Set up AWS App Mesh sample workload on an Amazon EKS cluster with the Fargate launch type](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-appmesh-Fargate.html): Information about setting up an AWS App Mesh sample workload with the Fargate launch type.
- [Set up NGINX with sample traffic on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-nginx.html): Information about setting up NGINX to produce sample traffic.
- [Set up memcached with a metric exporter on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-memcached.html): Information about setting up memcached to export metrics on Amazon EKS.
- [Set up Java/JMX sample workload on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-javajmx.html): Information about setting up a JAVA/JMX sample workload on Amazon EKS and Kubernetes.
- [Set up HAProxy with a metric exporter on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-haproxy.html): Information about setting up HAProxy to export metrics to CloudWatch.
- [Tutorial for adding a new Prometheus scrape target: Redis OSS on Amazon EKS and Kubernetes clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-redis-eks.html): Information about scraping Prometheus metrics from a Resis OSS application on Amazon EKS and Kubernetes.
- [Prometheus metric type conversion by the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-metrics-conversion.html): Information about the Prometheus metric types supported by CloudWatch.
- [Prometheus metrics collected by the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-metrics.html): Information about Prometheus metrics automatically collected by CloudWatch.
- [Viewing your Prometheus metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-viewmetrics.html): Steps to view Prometheus metrics in the CloudWatch console.

### [Prometheus metrics troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-troubleshooting.html)

Information for resolving issues with Prometheus metrics.

- [Prometheus metrics troubleshooting on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-troubleshooting-ECS.html): Information about issues and resolutions for Prometheus metrics on Amazon ECS in CloudWatch.
- [Prometheus metrics troubleshooting on Amazon EKS and Kubernetes clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-troubleshooting-EKS.html): Information about issues and resolutions for Amazon EKS and Kubernetes in CloudWatch.
- [Integration with Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-appinsights.html): Information about how Container Insights integrates with Application Insights in CloudWatch.
- [Viewing Amazon ECS lifecycle events within Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-ECS-lifecycle-events.html): Steps to view Amazon ECS lifecycle events in Container Insights in CloudWatch.
- [Troubleshooting Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-troubleshooting.html): Information about issues with CloudWatch Container Insights and resolutions.
- [Building your own CloudWatch agent Docker image](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-build-docker-image.html): Information about creating a Docker image for CloudWatch for your environment.
- [Deploying other CloudWatch agent features in your containers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-other-agent-features.html): Information about other CloudWatch monitoring features you can include in your containers.

### [Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html)

Learn how to use CloudWatch Lambda Insights to collect CloudWatch metrics related to your Lambda functions.

### [Get started with Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started.html)

Learn how to deploy CloudWatch Lambda Insights to collect CloudWatch metrics related to your Lambda functions.

### [Available versions of the Lambda Insights extension](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-extension-versions.html)

Information about versions of the CloudWatch Lambda Insights extension, including ARNs for use in AWS Regions.

- [x86-64 platforms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-extension-versionsx86-64.html): Information about the versions of CloudWatch Lambda Insights for x86-64 platforms, including ARNs for use in AWS Regions.
- [ARM64 platforms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-extension-versionsARM.html): Information about the versions of the CloudWatch Lambda Insights extension for ARM64 platforms, including the ARNs to use them in AWS Regions.
- [Using the console to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-console.html): Steps to enable Lambda Insights through the AWS Lambda console.
- [Use the AWS CLI to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-cli.html): Steps to use enable CloudWatch Lambda Insights through the AWS CLI.
- [Use the AWS SAM CLI to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-SAM-CLI.html): Steps to enable CloudWatch Lambda Insights through the AWS SAM CLI.
- [Use CloudFormation to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-cloudformation.html): Steps to enable CloudWatch Lambda Insights through CloudFormation.
- [Use the AWS CDK to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-clouddevelopmentkit.html): Steps to enable CloudWatch Lambda Insights through the AWS CDK.
- [Use Serverless Framework to enable Lambda Insights on an existing Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-serverless.html): Use these steps to use Serverless Framework to enable Lambda Insights on a Lambda function.
- [Enable Lambda Insights on a Lambda container image deployment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html): Use these steps to use enable Lambda Insights on a Lambda function that is deployed as a container image, such as using Amazon ECR.
- [Update the Lambda Insights extension version on a function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Update-Extension.html): Use these steps to use update the Lambda Insights extension version that you are using with an existing Lambda function
- [Viewing your Lambda Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-view-metrics.html): Steps to view CloudWatch Lambda Insights in the console.
- [Integration with Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/lambda-insights-appinsights.html): Information about how CloudWatch Lambda Insights integrates with Application Insights.

### [Metrics collected by Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-metrics.html)

Information about the types of metrics collected by CloudWatch about Lambda functions.

- [Lambda Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-metrics-lambda-functions.html): Metrics collected by CloudWatch Lambda Insights for standard Lambda functions.
- [Managed Instances Lambda Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-metrics-managed-instances.html): Metrics collected by CloudWatch Lambda Insights for Lambda functions running on Managed Instances.
- [Troubleshooting and known issues](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Troubleshooting.html): Information about issues with CloudWatch Lambda Insights and their resolutions.
- [Example telemetry event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-example-event.html): Information about the format of a CloudWatch Lambda Insights log event and methods to analyze log events.

### [Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html)

Monitor and troubleshoot Amazon RDS and Amazon Aurora MySQL and Amazon Aurora PostgreSQL databases at scale with CloudWatch Database Insights.

- [Get started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Get-Started.html): Get started with Database Insights.
- [Cross-account cross-region monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Cross-Account-Cross-Region.html): CloudWatch Database Insights allows you to monitor your Amazon Aurora and RDS databases across accounts and regions at scale.

### [Viewing the Fleet Health Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Fleet-Health-Dashboard.html)

Monitor and troubleshoot issues for your databases with the Fleet Health Dashboard.

- [Create a fleet health view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-fleet-views-create.html): Create and save fleet health views for groups of databases you choose.
- [Edit a fleet health view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-fleet-views-edit.html): Edit the name and filters for your fleet health views.
- [Delete a fleet health view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-fleet-views-delete.html): Delete fleet health views.

### [Viewing the Database Instance Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Database-Instance-Dashboard.html)

Monitor and troubleshoot issues for your DB instance with the Database Instance Dashboard.

- [Analyzing lock trees](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Lock-Analysis.html): Analyze lock trees for Amazon Aurora PostgreSQL and Amazon RDS for PostgreSQL databases with CloudWatch Database Insights.
- [Analyzing execution plans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Execution-Plans.html): Analyze execution plans with CloudWatch Database Insights.
- [Monitoring Aurora Limitless databases with Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/database-insights-limitless.html): Monitor and analyze database load across Aurora Limitless shard groups and instances.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Troubleshooting.html): Troubleshoot issues for CloudWatch Database Insights.

### [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)

Learn how to use CloudWatch Contributor Insights to create time series showing the top-N talkers that are contributing to your CloudWatch metrics and logs, and find the number of contributors.

- [Create a Contributor Insights rule in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html): Steps to create a CloudWatch Contributor Insights rule to analyze log data.
- [Contributor Insights rule syntax in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html): Information about how to construct a CloudWatch Contributor Insights rule.
- [Example rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-Rule-Examples.html): Examples of CloudWatch Contributor Insights rules, including sample code.
- [Viewing Contributor Insights reports in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-ViewReports.html): Steps to view CloudWatch Contributor Insights reports in the console.
- [Graphing metrics generated by rules in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-GraphReportData.html): Information about adding data from a Contributer Insights report a graph in the CloudWatch console.
- [Using Contributor Insights built-in rules in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-BuiltInRules.html): Information about analyzing metrics of other AWS services in CloudWatch Contributor Insights.

### [CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html)

Learn how to detect and troubleshoot common application problems using CloudWatch Application Insights, which provides automated dashboards and insights to help reduce mean time to resolution (MTTR) for your applications and AWS resources.

- [What is Amazon CloudWatch Application Insights?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-what-is.html): Learn how to monitor, detect problems, and troubleshoot applications using CloudWatch Application Insights for AWS services and technology stacks like EC2, RDS, SQL Server, Java, and SAP.

### [How Application Insights works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-how-works.html)

Discover how CloudWatch Application Insights components monitor your applications by analyzing data sources, detecting issues through intelligent algorithms, and generating CloudWatch Events for notifications, enabling proactive troubleshooting and maximizing application performance.

- [SSM packages used by Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-ssm-packages.html): Learn how to install and configure AWS-provided Prometheus exporters for Java, SAP HANA, SAP NetWeaver, SQL Server, and High Availability (HA) clusters to monitor application and database metrics using AWS Systems Manager Distributor.
- [SSM documents used by Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-ssm-documents.html): Learn how CloudWatch Application Insights uses AWS Systems Manager Documents to automate monitoring tasks on managed instances for application performance visibility.

### [Prerequisites, IAM policies, and permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-accessing.html)

Learn how to access CloudWatch Application Insights by verifying prerequisites, configuring IAM policies, and attaching necessary permissions for account-based application onboarding.

- [Prequisites](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-prereqs.html): Discover prerequisites to configure applications for monitoring with CloudWatch Application Insights, including enabling AWS Systems Manager Agent, attaching EC2 instance roles, creating resource groups, setting IAM permissions, using service-linked roles, supporting Performance Counter metrics on EC2 Windows instances, and installing CloudWatch agent.
- [IAM policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-iam.html): Discover how to create an IAM policy and attach it to your user, group, or role to use CloudWatch Application Insights, enabling management of permissions for this AWS service.
- [Permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-account-based-onboarding-permissions.html): Learn how to configure IAM role permissions for account-based application onboarding in CloudWatch Application Insights to discover all resources in your AWS account.

### [Set up application for monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up.html)

Discover how to set up and configure CloudWatch Application Insights for monitoring your applications using the AWS Management Console, AWS CLI, or PowerShell.

- [Console steps](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up-console.html): Learn how to set up and configure application monitoring with CloudWatch Application Insights from the CloudWatch console, including adding applications, enabling container monitoring for Amazon ECS and EKS resources, and disabling component monitoring.
- [Command line steps](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up-command.html): Learn how to set up, configure, and manage application monitoring using the command line for CloudWatch Application Insights.
- [Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-cloudwatch-events.html): Learn about CloudWatch Events which are emitted when CloudWatch Application Insights detects a new problem or a problem is updated.
- [Notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-problem-notifications.html): Learn how to receive notifications for detected problems using CloudWatch events, Amazon SNS notifications, and Systems Manager OpsCenter.
- [Application Insights cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-cross-account.html): Learn how to monitor and troubleshoot applications spanning multiple AWS accounts within a AWS Region using CloudWatch Application Insights cross-account observability.

### [Work with component configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config.html)

Discover how to configure components for Amazon CloudWatch with JSON files, including template fragments, configuration sections, and examples for relevant services.

- [Template fragment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-json.html): Discover how the component configuration template fragment in JSON format works to define monitoring and observability settings for AWS resources like EC2 instances, volumes, and services like CloudWatch alarms, logs, metrics, processes, and events.
- [Sections](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-sections.html): Discover how CloudWatch Application Insights component configurations work to monitor your resources and applications.

### [Example configurations for relevant services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples.html)

Discover how Amazon CloudWatch components work to monitor and observe AWS resources and applications with configuration examples for services like Amazon EC2, Amazon ECS, Amazon RDS, Amazon S3, AWS Lambda, and more.

- [Amazon DynamoDB table](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-dynamo.html): Discover an example JSON configuration for monitoring Amazon DynamoDB table metrics with Amazon CloudWatch, including settings for alarms and logs.
- [Amazon EC2 Auto Scaling (ASG)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-asg.html): Discover how the Amazon CloudWatch component configuration works for Amazon EC2 Auto Scaling (ASG) to monitor metrics, logs, processes, and events for instances and volumes.
- [Amazon EKS cluster](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-eks-cluster.html): Discover how Amazon EKS cluster component configuration examples illustrate enabling monitoring for key metrics and logs on Kubernetes clusters, EC2 instances, AutoScaling groups, and EBS volumes.
- [Amazon Elastic Compute Cloud (EC2) instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-ec2.html): Discover how CloudWatch Application Insights configures components like Amazon EC2 instances to monitor logs, metrics, alarms, and sub-components for optimal application performance.
- [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-ecs.html): Learn how to configure and monitor Amazon ECS with CloudWatch, including alarms for metrics like CPU, memory, network, tasks, and storage, along with log monitoring for ECS task definitions, load balancers, EC2 instances, volumes, processes, and Windows events.
- [Amazon ECS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-ecs-service.html): Discover how to configure Amazon CloudWatch metrics and logs for Amazon ECS services, load balancers, EC2 instances, and volumes to monitor critical performance metrics and events.
- [Amazon ECS tasks](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-ecs-task.html): Learn how to configure Amazon CloudWatch agent to monitor Amazon ECS tasks, including application logs and process metrics like CPU and memory usage.
- [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-efs.html): Discover how Amazon CloudWatch monitors Amazon Elastic File System performance with comprehensive metrics and logs for resource utilization and file system health.
- [Amazon FSx](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-fsx.html): Discover how the Amazon FSx component configuration example shows metrics to monitor for alarms, including data read/write bytes and operations, metadata operations, and free storage capacity.
- [Amazon Relational Database Service (RDS) Aurora MySQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-rds-aurora.html): Discover how the Aurora MySQL-Compatible Edition component configuration example facilitates monitoring CPU utilization, commit latency, and MySQL log types for efficient database management and performance optimization.
- [Amazon Relational Database Service (RDS) instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-rds.html): Discover how to configure Amazon CloudWatch components for an Amazon Relational Database Service instance with example JSON code.
- [Amazon RouteÂ 53 health check](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-health-check.html): Discover how Amazon RouteÂ 53 Public Data Plane health check components work to monitor key metrics for DNS health and performance.
- [Amazon RouteÂ 53 hosted zone](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-hosted-zone.html): Discover how the Amazon RouteÂ 53 Public Data Plane hosted zone component configuration works to monitor DNS queries, DNSSEC key management, and enable public query logging.
- [Amazon RouteÂ 53 Resolver endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-resolver-endpoint.html): Learn how to monitor Amazon RouteÂ 53 Resolver endpoints with CloudWatch metrics like EndpointHealthyENICount, EndpointUnHealthyENICount, InboundQueryVolume, OutboundQueryVolume, and OutboundQueryAggregateVolume.
- [Amazon RouteÂ 53 Resolver query logging configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-resolver-query-logging.html): Learn how to configure Amazon RouteÂ 53 Resolver query logging to monitor DNS queries for operational insights and security analysis with CloudWatch logs.
- [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-s3.html): Discover how to monitor Amazon S3 bucket metrics like replication latency, 5xx errors, and bytes downloaded using Amazon CloudWatch component configurations.
- [Amazon Simple Queue Service (SQS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sqs.html): Learn how to configure Amazon CloudWatch to monitor key metrics for Amazon Simple Queue Service and set alarms for anomalous behavior using the provided JSON example.
- [Amazon SNS topic](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sns.html): Discover how to monitor key metrics for Amazon SNS topics with CloudWatch to ensure reliable message delivery.
- [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-vpc.html): Discover how Amazon Virtual Private Cloud component configuration examples work to monitor critical metrics like network address usage and VPC firewall query volume.
- [Amazon VPC Network Address Translation (NAT) gateways](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-nat-gateway.html): Discover how to monitor key metrics for Amazon Virtual Private Cloud Network Address Translation (NAT) gateways with Amazon CloudWatch to ensure optimal performance and resource utilization.
- [API Gateway REST API stages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-api-gateway.html): Learn how to configure Amazon CloudWatch logging and monitoring for Amazon API Gateway REST API stages to track errors and execution access.
- [Application Elastic Load Balancing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-application-elb.html): Discover how to configure CloudWatch components for Elastic Load Balancing, including alarms, metrics for load balancers, EC2 instances, and volumes, logs, and Windows events.
- [AWS Lambda Function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-lambda.html): Learn how to monitor AWS Lambda Function metrics and logs with CloudWatch to track errors, throttles, iterator age, and duration.
- [AWS Network Firewall rule group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-firewall-rule-group.html): Learn how to configure AWS Network Firewall rule groups for firewall metrics monitoring and set alarms using CloudWatch.
- [AWS Network Firewall rule group association](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-firewall-rule-group-assoc.html): Learn how to configure AWS Network Firewall rule group association to monitor firewall rule group query volume with CloudWatch alarms and metrics.
- [AWS Step Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-step-functions.html): Discover how AWS Step Functions component metrics and logs work to monitor execution failures, Lambda function failures, and provisioned refill rates.
- [Customer-grouped Amazon EC2 instances](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-grouped-ec2.html): Learn how to configure Amazon CloudWatch components for customer-grouped Amazon EC2 instances and volumes to monitor alarms, logs, processes, and Windows events.
- [Elastic Load Balancing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-elb.html): Learn how to configure CloudWatch components to monitor Elastic Load Balancing including metrics, logs, processes, and events for EC2 instances, volumes, and application load balancers.
- [Java](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-java.html): Learn how to configure CloudWatch Application Insights components for Java applications to monitor metrics like thread count, heap memory usage, and more with Prometheus JMX exporter.
- [Kubernetes on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-kubernetes-ec2.html): Discover how to monitor and manage Kubernetes clusters on Amazon EC2 instances with Amazon CloudWatch, including metrics for nodes, pods, CPU, memory, network, file systems, processes, and EC2 instances and volumes.
- [RDS MariaDB and RDS MySQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-mysql.html): Learn how to configure Amazon CloudWatch to monitor RDS MariaDB and RDS MySQL databases, including CPU utilization metrics and MySQL log file types.
- [RDS Oracle](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-oracle.html): Discover how to monitor Amazon RDS Oracle instances using CloudWatch by configuring alarms for CPU utilization and enabling log monitoring for Oracle alerts.
- [RDS PostgreSQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-rds-postgre-sql.html): Learn how to monitor Amazon RDS PostgreSQL databases using CloudWatch with CPU utilization metrics and PostgreSQL log monitoring for comprehensive insights.
- [SAP ASE on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sap-ase.html): Learn how to configure Amazon CloudWatch to monitor SAP ASE database instances on Amazon EC2 using metrics, logs, and a SAP ASE Prometheus exporter.
- [SAP ASE High Availability on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sap-ase-ha.html): Discover how to configure Amazon CloudWatch to monitor SAP ASE High Availability on Amazon EC2, including alarm metrics, log files, and the SAP ASE Prometheus exporter for comprehensive monitoring.
- [SAP HANA on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-hana.html): Learn how to configure Amazon CloudWatch to monitor SAP HANA on Amazon EC2 instances, including metrics, logs, and Prometheus exporter settings for optimal monitoring and alerting.
- [SAP HANA High Availability on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-hana-ha.html): Learn how to configure Amazon CloudWatch to monitor SAP HANA High Availability on Amazon EC2, including specific metrics, logs, HANA Prometheus exporter, and HA cluster Prometheus exporter settings.
- [SAP NetWeaver on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-netweaver.html): Discover how to configure Amazon CloudWatch to monitor SAP NetWeaver on Amazon EC2 instances, including metrics, logs, and Prometheus exporter settings for tracking performance, availability, and system health.
- [SAP NetWeaver High Availability on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-netweaver-ha.html): Discover how to configure Amazon CloudWatch monitoring for SAP NetWeaver High Availability on Amazon EC2, including metrics, logs, and Prometheus exporters for HA clusters and NetWeaver instances.
- [SQL Always On Availability Group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sql.html): Discover how the AWS Management Console component configuration example monitors SQL Server Always On Availability Group metrics, logs, and Windows events for instance and volume resources using Amazon CloudWatch.
- [SQL failover cluster instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-sql-failover-cluster.html): Discover how to monitor SQL failover cluster instances with Amazon CloudWatch through JSON component configurations that specify custom metrics, Windows events, and logs to capture critical performance and health data.
- [Use CloudFormation templates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-cloudformation.html): Learn how to create and configure CloudWatch Application Insights monitoring using CloudFormation templates for applications, resources, and components.
- [Tutorial: Set up monitoring for SAP ASE](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-tutorial-sap-ase.html): Use CloudWatch Application Insights to automatically monitor and troubleshoot SAP ASE databases running on AWS, with automatic dashboards, alarms, and log analysis.
- [Tutorial: Set up monitoring for SAP HANA](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-tutorial-sap-hana.html): Learn how to set up monitoring for your SAP HANA databases using CloudWatch Application Insights to visualize problems, accelerate troubleshooting, and facilitate mean time to resolution (MTTR).
- [Tutorial: Set up monitoring for SAP NetWeaver](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-tutorial-sap-netweaver.html): Learn how to set up monitoring for SAP NetWeaver using CloudWatch Application Insights to visualize issues, accelerate troubleshooting, and reduce mean time to resolution (MTTR).
- [View and troubleshoot Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-troubleshooting.html): Discover how CloudWatch Application Insights troubleshooting works to identify and resolve problems detected for monitored applications.

### [Supported logs and metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-logs-and-metrics.html)

Learn how to use Amazon CloudWatch Application Insights to monitor logs and metrics for your applications running on AWS services like EC2, RDS, Lambda, DynamoDB, and more, including infrastructure metrics, application logs, and performance counters.

- [Amazon Elastic Compute Cloud (EC2)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-ec2.html): Discover how Amazon EC2 metrics provide visibility into the performance and health of your Amazon Elastic Compute Cloud instances with CloudWatch Application Insights, including built-in metrics, CloudWatch agent metrics for Windows and Linux servers, and process-level metrics.
- [Elastic Block Store (EBS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-ebs.html): Discover how to monitor Amazon Elastic Block Store volume performance with Amazon CloudWatch Application Insights metrics like read/write operations, throughput, and queue length.
- [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-efs.html): Discover key Amazon Elastic File System metrics monitored by Amazon CloudWatch Application Insights for optimizing performance and monitoring file system health.
- [Elastic Load Balancer (ELB)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-elb.html): Learn how to monitor and analyze key metrics for Elastic Load Balancing with Amazon CloudWatch Application Insights, including connection counts, consumed LCUs, HTTP error codes, and host health.
- [Application ELB](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-app-elb.html): Learn how to monitor Elastic Load Balancing metrics with Amazon CloudWatch Application Insights to gain insights into load balancer performance and health.
- [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-as.html): Learn how to monitor Amazon EC2 Auto Scaling groups with Amazon CloudWatch Application Insights metrics for CPU, disk, network, and status checks.
- [Amazon Simple Queue Server (SQS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-sqs.html): Learn how to monitor and optimize Amazon Simple Queue Service performance using Amazon CloudWatch Application Insights metrics for queue depth, message age, and throughput.
- [Amazon Relational Database Service (RDS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-rds.html): Discover the Amazon RDS metrics supported by Amazon CloudWatch Application Insights for monitoring database instances and clusters, including performance, storage, and connectivity metrics.
- [AWS Lambda function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-lambda.html): Discover how to monitor Lambda function metrics using Amazon CloudWatch Application Insights to gain visibility into errors, duration, throttles, and more.
- [Amazon DynamoDB table](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-dyanamodb.html): Discover Amazon CloudWatch Application Insights metrics for monitoring Amazon DynamoDB table performance, including system and user errors, read/write capacity consumption, throttling, time-to-live item deletions, and replication health.
- [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-s3.html): Learn how to monitor Amazon S3 bucket metrics using Amazon CloudWatch Application Insights, including replication latency, error rates, request types, and data transfer metrics for optimizing performance and cost.
- [AWS Step Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-step-functions.html): Discover how Amazon CloudWatch Application Insights monitors AWS Step Functions metrics to track execution, activities, Lambda functions, service integrations, and API usage.
- [API Gateway REST API stages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-api-gateway.html): Discover how to monitor API Gateway REST API stages with Amazon CloudWatch Application Insights metrics like error rates, latency, and cache performance for effective API management.
- [SAP HANA](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-sap-hana.html): Learn how to monitor SAP HANA performance with Amazon CloudWatch Application Insights by viewing key metrics like service status, alerts, memory usage, CPU utilization, connections, transactions, and backups.
- [SAP ASE](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-sap-ase.html): Discover how Amazon CloudWatch Application Insights provides key SAP ASE database metrics to monitor performance, availability, cache usage, database space, transaction logs, and job failures for optimal database management.
- [SAP ASE High Availability on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-sap-ase-ha.html): Discover how Amazon CloudWatch Application Insights monitors SAP ASE high availability on Amazon EC2 with metrics for replication state, mode, and latency.
- [SAP NetWeaver](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-sap-netweaver.html): Learn how to monitor key SAP NetWeaver metrics with Amazon CloudWatch Application Insights, including response times, alerts, queue status, enqueue statistics, and high availability checks for optimal performance and availability.
- [HA Cluster](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-ha-cluster.html): Discover how to monitor high availability cluster metrics with Amazon CloudWatch Application Insights to ensure the health and reliability of your mission-critical systems.
- [Java](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-java.html): Discover how Java application metrics work with Amazon CloudWatch Application Insights to monitor memory usage, operating system resources, thread counts, class loading, and garbage collection times.
- [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-ecs.html): Discover key Amazon Elastic Container Service metrics available in Amazon CloudWatch Application Insights, including built-in metrics, Container Insights metrics, and Java JMX Prometheus metrics for monitoring ECS workloads.
- [Kubernetes on AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-kubernetes.html): Learn how to monitor Kubernetes clusters on AWS with Amazon CloudWatch Application Insights Container Insights metrics and Prometheus JMX metrics for Java applications.
- [Amazon FSx](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-fsx.html): Discover how Amazon FSx file system metrics work to monitor performance and capacity utilization with Amazon CloudWatch Application Insights.
- [Amazon VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-vpc.html): Discover how to monitor Amazon VPC usage and firewall activity with Amazon CloudWatch Application Insights metrics for NetworkAddressUsage, NetworkAddressUsagePeered, and VPCFirewallQueryVolume.
- [Amazon VPC NAT gateways](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-nat-gateways.html): Discover how Amazon CloudWatch Application Insights monitors Amazon VPC NAT gateway metrics for error port allocation and idle timeout count.
- [Amazon RouteÂ 53 health check](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-health-check.html): Discover how Amazon Route 53 health checks work to monitor the health and performance of your web applications and resources with CloudWatch Application Insights metrics.
- [Amazon RouteÂ 53 hosted zone](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-hosted-zone.html): CloudWatch Application Insights supports the following metrics:
- [Amazon RouteÂ 53 Resolver endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-resolver-endpoint.html): CloudWatch Application Insights supports the following metrics:
- [AWS Network Firewall rule group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-firewall-rule-group.html): CloudWatch Application Insights supports the following metrics:
- [AWS Network Firewall rule group association](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-firewall-rule-group-assoc.html): CloudWatch Application Insights supports the following metrics:
- [Metrics with data points requirements](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-metrics-datapoint-requirements.html): For metrics without an obvious default threshold to alarm on, Application Insights waits until the metric has enough data points to predict a reasonable threshold to alarm on.
- [Recommended metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/application-insights-recommended-metrics.html): The following table lists the recommended metrics for each component type.
- [Performance Counter metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/application-insights-performance-counter.html): Performance Counter metrics are recommended for instances only when the corresponding Performance Counter sets are installed on the Windows instances.
- [Using the resource health view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_resource_health.html): Explains how to use the resource health view in the CloudWatch console.


## [Application performance monitoring (APM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html)

### [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html)

Includes sections about CloudWatch features such as Application Signals, Synthetics, and CloudWatch RUM.

- [Permissions required for Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application_Signals_Permissions.html): Learn about the IAM permissions required to be able to enable and manage CloudWatch Application Signals.
- [Supported systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-supportmatrix.html): Explains compatibility issues to consider before installing CloudWatch Application Signals, including OpenTelemetry and Java compatibility.
- [Supported instrumentation setups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Getting-Started-App-Signals.html): Explains how to enable CloudWatch Application Signals on different instrumentation setups
- [Enable Application Signals in your account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html): Explains how to enable Application Signals in your account.
- [(Optional) Try out Application Signals with a sample app](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-EKS-sample.html): Explains how to try out Application Signals by creating a new Amazon EKS cluster to install it in, and install a sample app.
- [Enable your applications on Amazon EKS clusters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-EKS.html): Explains how to enable Application Signals on Amazon EKS clusters.
- [Enable your applications on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-EC2Main.html): Explains how to enable Application Signals on platforms such as Amazon EC2.

### [Enable your applications on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-ECSMain.html)

Explains how to enable Application Signals on platforms such as Amazon ECS, using a custom setup.

- [Deploy using the sidecar strategy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-ECS-Sidecar.html)
- [Deploy using the daemon strategy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-ECS-Daemon.html)
- [Enable Application Signals on Amazon ECS using AWS CDK](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-EKS-CDK.html): Explains how to enable Application Signals on platforms such as Amazon ECS using AWS CDK
- [Enable your applications on Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-KubernetesMain.html): Explains how to enable Application Signals on platforms such as Kubernetes, using a custom setup.
- [Enable your applications on Lambda](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.html): Explains how to enable Application Signals on platforms such as Lambda using a custom setup.
- [Troubleshooting your Application Signals installation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-Troubleshoot.html): Explains how to troubleshoot your installation of CloudWatch Application Signals.

### [(Optional) Configuring Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Configure.html)

Explains how to configure CloudWatch Application Signals afer you have enabled it.

- [Trace sampling rate](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-SampleRate.html): By default, when you enable Application Signals X-Ray centralized sampling is enabled using the default sampling rate settings of reservoir=1/s and fixed_rate=5%.
- [Enable trace to log correlation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-TraceLogCorrelation.html): You can enable trace to log correlation in Application Signals.
- [Enable metric to log correlation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-MetricLogCorrelation.html): If you publish application logs to log groups in CloudWatch Logs, you can enable metric to application log correlation in Application Signals.
- [Manage high-cardinality operations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-Cardinality.html): Application Signals includes settings in the CloudWatch agent that you can use to manage the cardinality of your operations and manage the metric exportation to optimize costs.

### [Monitor your application's operational health](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services.html)

Use the Services, Service detail, and Application Map pages in CloudWatch Application Signals to monitor the operational health of your applications.

- [View your services with the Services page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-page.html): Use the Services page in CloudWatch Application Signals to monitor and troubleshoot your application services.
- [View detailed service information](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceDetail.html): How to use the service detail page in CloudWatch Application Signals to monitor and troubleshoot a specific service.
- [View your application topology with the application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html): Learn how to use the application map in CloudWatch Application Signals to understand your application topology and monitor and troubleshoot the operational health of your services.
- [Application observability for AWS Action](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Service-Application-Observability-for-AWS-GitHub-Action.html): This action provides an end-to-end application observability investigation workflow that connects your source code and live production telemetry data to AI agent.
- [Example: Resolve an operational health issue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-example-scenario.html): An example of using Application Signals to identify and resolve an operational health issue.
- [Example: Troubleshoot applications interacting with Amazon Bedrock](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.html): An example of using Application Signals to troubleshoot generative AI applications interacting with Amazon Bedrock.
- [Metrics collected by Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AppSignals-MetricsCollected.html): Learn about the standard application metrics and runtime metrics that CloudWatch Signals collects.
- [Custom metrics with Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AppSignals-CustomMetrics.html): Learn how to add custom metrics to your applications monitored by Application Signals.
- [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html): Explains how to work with service level objectives (SLOs) in CloudWatch.

### [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html)

Provides an overview of Transaction Search.

### [Enable transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html)

You can enable through the console or by using an API.

- [Using Transaction Search with CloudFormation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-Cloudformation.html): How to use Transaction Search with CloudFormation

### [Spans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-ingesting-span-log-groups.html)

Describes which CloudWatch Logs features are available for ingested spans.

- [Searching and analyzing spans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-search-analyze-spans.html): Describes how to search and analyze spans.
- [Ingesting spans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-ingesting-spans.html): Provides an overview of ingesting spans for complete visibility.
- [Monitoring spans across accounts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-cross-account-observability.html): Provides an overview of how to monitor spans across multiple accounts.
- [Adding custom attributes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-add-custom-attributes.html): Describes how to add custom attributes.
- [Troubleshooting application issues](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-troubleshooting.html): Describes how to troubleshoot issues related to Transaction Search.

### [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)

Explains how to use Synthetic Monitoring to create and manage canaries in Synthetics and the X-Ray Trace Map.

### [Required roles and permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles.html)

Explains the roles and permissions that are required for both canaries and the users who work with them, in CloudWatch Synthetics.

- [Required roles and permissions for users who manage CloudWatch canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_UserPermissions.html): Information about IAM policies required to view canary details and results of canary runs.
- [Required roles and permissions for canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_CanaryPermissions.html): Information about the IAM trust policy statement required for canaries.
- [Limiting a user to viewing specific canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html): Example IAM policies to limit user roles that can view information about canaries.

### [Creating a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Create.html)

Explains how to create canaries in Synthetics.

### [Using canary blueprints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints.html)

Explains the details and use of each type of canary blueprint in Amazon CloudWatch Synthetics.

- [Creating multi checks blueprint canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_MultiCheck_Blueprint.html): Learn how to create and configure multi-check blueprint canaries in Amazon CloudWatch Synthetics.
- [Using the CloudWatch Synthetics Recorder for Google Chrome](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Recorder.html): Explains how to download and use the CloudWatch Synthetics canary recorder extension for Google Chrome.

### [Synthetics runtime versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html)

Explains the versions of CloudWatch Synthetics runtimes, libraries, and configuration information.

- [Runtime versions using Java](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_Java.html): Describes the versions of canary runtimes, libraries, and configuration information for Java
- [Runtime versions using Node.js and Playwright](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_playwright.html): Describes the versions of canary runtimes, libraries, and configuration information for Node.js using Playwright.
- [Runtime versions using Node.js and Puppeteer](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html): Explains the versions of canary runtimes, libraries, and configuration information.
- [Runtime versions using Python and Selenium Webdriver](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html): Explains the versions of canary runtimes, libraries, and configuration information.
- [Runtime versions using Node.js](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_Nodejs.html): Explains the versions of canary runtimes, libraries, and configuration information.
- [Runtime versions support policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Runtime_Support_Policy.html): Explains the versions of CloudWatch Synthetics runtimes, libraries, and configuration information.
- [Runtime versions update](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Runtime_Version_Update.html): Explains the processes of CloudWatch Synthetics runtimes upgrade.

### [Writing a canary script](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html)

Describes how to write a CloudWatch Synthetics canary script from scratch, how to change an existing script to be a canary, and how to integrate other AWS services with your canary.

- [Writing a canary script using the Java runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Synthetics_WritingCanary_Java.html): Describes how to package Java canaries, how to change an existing Java script to be a canary.
- [Writing a Node.js canary script using the Playwright runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Synthetics_WritingCanary_Nodejs_Playwright.html): Describes how to package Playwright Node.Js canaries, how to change an existing Playwright script to be a canary.
- [Writing a Node.js canary script using the Puppeteer runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Nodejs_Pup.html): Explains how to write a CloudWatch Synthetics Node.js canary script from scratch, how to change an existing script to be a canary, and how to integrate other AWS services with your canary.
- [Writing a Python canary script](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Python.html): Explains how to write a CloudWatch Synthetics Python canary script from scratch, how to change an existing script to be a canary, and how to integrate other AWS services with your canary.
- [Writing a JSON configuration for Node.js multi Checks blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_WritingCanary_Multichecks.html): Explains how to write a CloudWatch Synthetics JSON configuration script for Node.js multi checks blueprint

### [Library functions available for canary scripts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Function_Library.html)

Explains the built-in functions included in CloudWatch Synthetics that you can use to write your own canary scripts.

- [Library functions available for Node.js canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Library_function_Nodejs.html): Explains the built-in functions included in CloudWatch Synthetics that you can use to write your own canary scripts in Node.js.
- [Library functions available for Java canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Java.html): Describes functions that are included in CloudWatch Synthetics that you can use to write your own canary scripts in Java.
- [Library functions available for Node.js canary scripts using Playwright](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Nodejs_Playwright.html): Describes functions that are included in CloudWatch Synthetics that you can use to write your own canary scripts in Node.js by using the Playwright runtime.
- [Library functions available for Node.js canary scripts using Puppeteer](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library_Nodejs.html): Explains the built-in functions included in CloudWatch Synthetics that you can use to write your own canary scripts in Node.js.
- [Library functions available for Python canary scripts using Selenium](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library_Python.html): Explains the built-in functions included in CloudWatch Synthetics that you can use to write your own canary scripts in Python.
- [Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html): Explains how to use cron to create detailed schedules for your CloudWatch Synthetics canary runs.
- [Configuring your canary to retry automatically](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_autoretry.html): Explains how to configure your canaries to automatically attempt additional runs when the schedule dry run fails.
- [Using dependencies with CloudWatch Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_dependencies.html): This section explains how to use Dependencies in CloudWatch Synthetics canaries.
- [Groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Groups.html): Explains how to create canary groups and their benefits for management, automation, and monitoring.
- [Test a canary locally](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Debug_Locally.html): Explains how to debug a canary locally within the Visual Studio Code editor.
- [Troubleshooting a failed canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Troubleshoot.html): Provides troubleshooting tips if your CloudWatch Synthetics canary fails.
- [Sample code for canary scripts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Samples.html): Provides some code samples useful for writing CloudWatch Synthetics canary scripts.
- [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html): Explains how canaries work with X-Ray tracing.
- [Running a canary on a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html): Explains how to run a canary on a virtual private cloud (VPC).
- [Encrypting canary artifacts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html): Explains the options for encrypting canary artifacts in CloudWatch Synthetics.
- [Viewing canary statistics and details](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Details.html): Explains how to view the details and statistics for your canaries in Synthetics and the X-Ray Trace Map.
- [CloudWatch metrics published by canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_metrics.html): Explains how to view the CloudWatch metrics that are published by canaries in CloudWatch Synthetics.
- [Edit or delete a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html): Explains extra steps that you should take when you delete a canary in CloudWatch.
- [Start, stop, delete, or update runtime for multiple canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_multi-action.html): Explains how to start, stop, delete, or update the runtime of multiple Amazon CloudWatch canaries with one action.
- [Monitoring canary events with Amazon EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitoring-events-eventbridge.html): Learn how to use Amazon EventBridge to monitor your canary status changes and the results of canary runs.
- [Performing safe canary updates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/performing-safe-canary-upgrades.html): CloudWatch synthetics safe canary updates allows you to test the updates on your existing canaries before applying the changes.

### [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)

Learn how to collect performance data for your web application from real user sessions, using CloudWatch RUM.

- [Set up a mobile application to use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-web-mobile.html): Learn how to collect performance data for your mobile applications from real user sessions, using CloudWatch RUM.
- [IAM policies to use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-permissions.html): Lists the IAM policies needed to manage CloudWatch RUM.

### [Set up a web application to use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started.html)

How to configure a web application to use CloudWatch RUM.

- [Authorize your web application to send data to AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html): Steps to set up authorization for your web application to send data to AWS.
- [Creating an app monitor for a web application](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-create-app-monitor.html): Steps to create an app monitor for using CloudWatch RUM with your application.
- [Modifying the code snippet (optional)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-modify-snippet.html): Information about modifications you can make to the app monitor code snippet, including example code.
- [Inserting the app monitor code snippet](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-insert-code-snippet.html): Steps describing how to insert the app monitor code snippet into your application, including example code.
- [Testing your app monitor setup by generating user events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-generate-data.html): Information about how to test your CloudWatch RUM app monitor setup including recommneded types of user events.
- [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html): You can attach a resource policy to a CloudWatch RUM app monitor.
- [Configuring the CloudWatch RUM web client](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-configure-client.html): Information about how to configure the CloudWatch RUM web client, including example code.
- [Enabling unminification of JavaScript error stack traces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-JavaScriptStackTraceSourceMaps.html): TBD
- [Regionalization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-Regionalization.html): Learn about strategies for using CloudWatch RUM with applications that span multiple AWS Regions.
- [Use page groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-page-groups.html): Learn how to use page groups in CloudWatch RUM to aggregate analytics for groups of pages.
- [Specify custom metadata](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-metadata.html): Explains how to specify custom attributes in the metadata that the CloudWatch RUM web client collects.
- [Send custom events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html): Learn how to record and send custom events to CloudWatch RUM.
- [Viewing the CloudWatch RUM dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-view-data.html): Learn about the different views and information available in the CloudWatch RUM dashboard for web and mobile applications.

### [CloudWatch metrics that you can collect with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html)

Information about metrics you can collect with CloudWatch RUM, including the metric name, the unit provided by the metric, and a description of the metric.

- [Custom metrics and extended metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-and-extended-metrics.html): Learn how to send CloudWatch RUM custom metrics and metrics with fine-grained dimensions to CloudWatch.
- [Data protection and data privacy with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-privacy.html): Explains how to protect your sensitive information when using CloudWatch RUM, and how to choose to use web cookies with CloudWatch RUM.

### [Information collected by the CloudWatch RUM web client](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-datacollected.html)

Lists all the types of data collected by CloudWatch RUM.

- [Route change timing for single-page applications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-route-change-timing.html): Information about how CloudWatch RUM measures load times for single-page applications.

### [Manage your applications that use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-manage.html)

How to manage the applications that you are using with CloudWatch RUM.

- [How do I find a code snippet that I've already generated?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html): Steps to find the app monitoring code snipet in the CloudWatch console after you generated it.
- [Editing your CloudWatch RUM app monitor settings](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-edit-application.html): Steps to edit the CloudWatch RUM app monitor settings for one of your applications.
- [Stopping or deleting an app monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-delete-appmonitor.html): Steps to stop using CloudWatch RUM app monitoring with your application.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-troubleshooting.html): How to troubleshoot issues with CloudWatch RUM.


## [Generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)

- [Model Invocations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/model-invocations.html): CloudWatch generative AI observability allows you to monitor Model Invocations performance.

### [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AgentCore-Agents.html)

CloudWatch provides curated observability views for Amazon Bedrock AgentCore.

### [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AgentCore-GettingStarted.html)

Amazon Bedrock AgentCore provides built-in metrics, logs, and traces to monitor the performance of your AgentCore modular services.

- [View observability data in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/view-observability-data-cloudwatch.html): After you enable observability for your agentic resources, you can view the collected data in CloudWatch.
- [Protect sensitive data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/mask-sensitive-data.html): Amazon CloudWatch Logs uses data protection policies to identify sensitive data and define actions to protect that data.

### [Agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Agents.html)

You can use Agents to monitor agent performance, track their decision-making processes, analyze conversation flows, and troubleshoot issues through comprehensive metrics and tracing.

### [Agent view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/agent-view.html)

The Agent view provides a curated dashboard for your account's agents.

- [Agent details - Sessions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-sessions-view.html): An Agent can have several Sessions.
- [Agent details - Traces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-traces-view.html): Each agent might have multiple traces.
- [Agent details - Evaluations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-traces-evaluations.html): Evaluations provides continuous quality monitoring metrics for your AI agents.
- [Session view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/session-view.html): The Sessions view shows the list of all the sessions associated with all agents in your account.
- [Traces view](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/traces-view.html): Trace view lists all traces from your agents in this account.
- [Memory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Memory.html): Understand how your agents store, retrieve, and use contextual information to provide personalized experiences.
- [Built-in tools](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Built-in-tools.html): Use CloudWatch to gain visibility into how your agents use built-in tools like Code interpreter tool and Browser use tool to complete tasks.

### [Gateways](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Gateways.html)

Monitor how your agents discover and interact with external tools and services through AgentCore Gateway.

- [Gateway details - Overview](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/gateways-overview.html): The Overview tab provides insights derived from sampled spans after transaction search is enabled.
- [Gateway details - Traces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/gateways-traces.html): The Traces tab displays all of the sampled traces for the selected gateway.
- [Identity](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Identity.html): Track identity and access management operations to ensure secure and compliant agent behavior.


## [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html)

- [Methods to create an investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/creation-methods.html): You can create investigations in the following ways:
- [Understanding hypothesis visualizations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-HypothesisVisualization.html): When CloudWatch investigations generates hypotheses that include multiple resources, the investigation view provides a visual representation of the causal relationships between those resources.
- [How CloudWatch investigations finds data for suggestions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-usage-considerations.html): CloudWatch investigations uses a wide range of data sources to determine dependency relationships and plan analysis paths, including telemetry data configurations, service configurations, and observed relationships.
- [Costs associated with CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/investigations-costs.html): CloudWatch investigations might incur AWS service usage including telemetry and resource queries and other API usage.
- [Insights that CloudWatch investigations can surface in investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-SuggestionTypes.html): CloudWatch investigations can surface the following types of items and add them to the Suggestions tab of an investigation.
- [AWS services where investigations are supported](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Services.html): You can launch investigations from telemetry data (such as CloudWatch metrics, alarms, and logs), review generated anomaly signals, and explore hypotheses on investigations.
- [Conduct an CloudWatch investigation without additional configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Ephemeral.html): You can conduct a CloudWatch investigations AI-powered root cause analysis without any additional configuration of your AWS account using the Investigations feature available in Operational troubleshooting.

### [Configure CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-GetStarted.html)

Configuring CloudWatch investigations creates an investigation group that CloudWatch investigations will use to access telemetry and aggregate data related to the investigation.

- [See a sample investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-sample.html): If you'd like to see an investigation in action before you configure an investigation group for your account, you can walk through a sample investigation.
- [Set up an investigation group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-GetStarted-Group.html): To set up CloudWatch investigations in your account for use with an enhanced investigation, you create an investigation group.

### [Configure alarms to create investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-configure-alarms.html)

You can configure an existing CloudWatch alarm to automatically create investigations in CloudWatch investigations.

- [Configure an alarm to create investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-configure-alarm-procedures.html): After you have an investigation group set up in your account, you can configure existing CloudWatch alarms to automatically create investigations when they enter the ALARM state.
- [Integration with Amazon EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EKS-Integration.html): CloudWatch investigations investigation groups can utilize information directly from your Amazon EKS cluster.
- [(Recommended) Best practices to enhance investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-RecommendedServices.html): As a best practice, we recommend that you enable several AWS services and features in your account that can help CloudWatch investigations discover more information in your topology and make better suggestions during investigations.

### [Investigate operational issues in your environment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Investigate.html)

You can create investigations in several ways depending on your workflow and the source of the issue you're investigating.

- [Create an investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-CreateInvestigation.html): You can start an investigation from several AWS consoles, including (but not limited to) CloudWatch alarm pages, CloudWatch metric pages, and Lambda monitoring pages.
- [Create an investigation from a CloudWatch Application Signals Service Level Objective (SLO)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-CreateInvestigation-SLO.html): You can start an investigation from a CloudWatch Application Signals Service Level Objective (SLO) metric.
- [View and continue an open investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Continue.html): Use the steps in this section to view and continue and existing investigation
- [Reviewing and executing suggested runbook remediations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/suggested-investigation-actions.html): When you add a hypothesis to the Feed area of an active investigation, CloudWatch investigations might display Show suggested actions.
- [Manage your current investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Manage.html): You can view a list of your current investigations, end active investigations, re-open archived investigations, rename, and delete investigations.
- [Restart an archived investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Restart.html): You can restart archived investigations.
- [Cross-account investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-cross-account.html): Cross-account CloudWatch investigations enables you to investigate application issues that span multiple AWS accounts from a centralized monitoring account.

### [Generate incident reports](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Incident-Reports.html)

Incident reports help you more quickly and easily write a report about your incident investigation.

- [Understanding AI-derived facts in incident reports](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-IncidentReports-ai-facts.html): AI-derived facts form the foundation of CloudWatch investigations incident reports, representing information that the AI system considers objectively true or highly probable based on comprehensive analysis of your AWS environment.
- [Incident report terminology](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-IncidentReports-terms.html): The following terms are used in CloudWatch investigations incident reports:
- [Generate a report from an investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-IncidentReports-Generate.html): You can generate incident reports from in-progress or completed investigations.
- [Using 5 Whys analysis in incident reports](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/incident-report-5whys.html): When generating incident reports, CloudWatch investigations can perform a 5 Whys root cause analysis to systematically identify the underlying causes of operational issues.
- [Integrations with other systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Integrations.html): Learn about other AWS services that are integrated with CloudWatch investigations.
- [Security in CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html): This section includes topics about how CloudWatch investigations integrate with AWS security and permissions features.
- [CloudWatch investigations data retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Retention.html): The retention period that you set for an investigation group determines how long that investigation data is kept.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Troubleshooting.html): Learn how to troubleshoot commons issues with CloudWatch investigations.


## [OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html)

- [OTLP Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html): Includes information about OpenTelemetry Protocol endpoints.

### [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html)

Includes sections on how to get started with OpenTelemetry.

- [OpenTelemetry Collector Contrib](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPSimplesetup.html): Includes section on how to get started with OpenTelemetry using the simple setup.
- [Build your own custom OpenTelemetry Collector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPAdvancedsetup.html): Includes section on how to get to build your own custom OpenTelemetry Collector
- [Exporting collector-less telemetry using AWS Distro for OpenTelemetry (ADOT) SDK](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-UsingADOT.html): Includes section on how you can use the option to go collector-less using AWS Distro for OpenTelemetry to send traces and logs directly to the OTLP endpoints.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPTroubleshooting.html): Includes information about troubleshooting OpenTelemetry issues.


## [Network Monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Network-Monitoring-Sections.html)

### [Using Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html)

Learn about Network Flow Monitor, a service that provides visibility into the performance of the network connecting your AWS hosted applications to your on-premises destinations.

### [What is Network Flow Monitor?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-What-is-NetworkFlowMonitor.html)

Summary information about Network Flow Monitor including Region support and pricing.

- [Supported AWS Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-Regions.html): Learn about the Regions supported by Network Flow Monitor.
- [Components](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html): Learn about components and features in Network Flow Monitor.
- [How it works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-inside-network-flow-monitor.html): Learn about how Network Flow Monitor works.
- [Pricing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.pricing.html): Network Flow Monitor pricing information.
- [Get started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-get-started.html): Learn about getting started with Network Flow Monitor.
- [API operations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-API-operations.html): The following table lists Network Flow Monitor API operations that you can use with Network Flow Monitor.
- [Examples with the CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NFM-get-started-CLI.html): Examples of using the AWS CLI to complete common tasks with Network Flow Monitor.

### [Work with EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-work-with-eks.html)

Using Network Flow Monitor, you can collect performance metrics for workloads that use Amazon Elastic Kubernetes Service (Amazon EKS).

### [Install agents for EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.html)

Learn about installing the Network Flow Monitor Agent add-on for Amazon EKS.

- [Configure for third party tools](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party.html): Learn about configuring the Network Flow Monitor EKS add-on to integrate with third party monitoring tools.
- [Additional metadata for EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-work-with-eks.performance-metadata.html): When Network Flow Monitor gathers performance metrics for network flows between Amazon EKS components, it includes additional metadata information about the network path, to help you better understand how the network paths for your workload are performing.

### [Install EC2 agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents.html)

Configure Network Flow Monitor in the AWS Management Console.

- [Supported Linux versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-versions.html): Learn about requirements for Network Flow Monitor agents.

### [EC2 instance agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-ec2.html)

Learn about methods for installing agents for EC2 instances in Network Flow Monitor.

- [Configure permissions for agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-ec2-permissions.html): To enable agents to send metrics to the Network Flow Monitor ingestion backend, the EC2 instances that the agents run in must use a role that has a policy attached with the correct permissions.
- [EC2 instance agents with SSM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-ec2-install-ssm.html): Learn about installing agents for EC2 instances in Network Flow Monitor by using SSM.
- [Download and install the agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline.html): Explains how to download and configure the Network Flow Monitor agent.

### [Self-managed Kubernetes agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.html)

Learn about installing agents for Kubernetes instances in Network Flow Monitor.

- [Before you begin](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin.html): Before you start the installation process, follow the steps in this section to make sure that your environment is set up to successfully install agents on the right Kubernetes clusters.
- [Download Helm charts and install agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-install-agents.html): You can download the Network Flow Monitor agent Helm charts from the AWS public repository by using the following command.
- [Configure permissions for agents to deliver metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-permissions.html): After you install agents for Network Flow Monitor, you must enable the agents to send network metrics to the Network Flow Monitor ingestion APIs.

### [Initialize Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-begin.html)

Before you can view performance metrics for network flows, you must initialize Network Flow Monitor, which grants required permissions and creates an initial topology for your account or accounts.

- [Single account monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-single-account.html): Initialize Network Flow Monitor for single account monitoring.
- [Multi-account monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-multi-account.html): Initialize Network Flow Monitor with AWS Organizations and add accounts, for multi-account monitoring.

### [Monitor network flows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure.html)

Learn about analyzing network flows and creating monitors to track them in Network Flow Monitor.

- [Evaluate network flows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html): Evaluate network flows in Network Flow Monitor in the AWS Management Console.

### [Create and work with monitors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors.html)

Create monitors in Network Flow Monitor in the AWS Management Console.

- [Create a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-create.html): Create monitors in Network Flow Monitor in the AWS Management Console.
- [Edit a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-edit.html): Information about how to edit a monitor in Network Flow Monitor.
- [Delete a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-delete.html): Information about how to delete a monitor in Network Flow Monitor.
- [Monitor and analyze](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-monitor-and-analyze.html): Information about how to monitor and analyze network flows using Network Flow Monitor performance metrics.
- [Delete scope](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-disable.html): Information about how to delete your scope in Network Flow Monitor.
- [View CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-cw-metrics.html): Information about viewing metrics for Network Flow Monitor.
- [Create alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-create-alarm.html): Information about creating alarms with Network Flow Monitor.
- [CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-monitoring-overview.html): Monitor Network Flow Monitor with CloudTrail to help maintain reliability, availability, and performance.
- [Troubleshoot issues](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-troubleshooting.html): Information about troubleshooting issues in Network Flow Monitor, such as installing agents.

### [Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-security-nfw.html)

Configure Network Flow Monitor to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Network Flow Monitor resources.

- [Data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-protection-nfw.html): Learn how the AWS shared responsibility model applies to data protection in Network Flow Monitor.
- [Infrastructure Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/infrastructure-security-nfw.html): Learn how Network Flow Monitor isolates service traffic.

### [Identity and Access Management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-security-iam.html)

How to authenticate requests and manage access to your Network Flow Monitor resources.

- [How Network Flow Monitor works with IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_service-with-iam-network-flow-monitor.html): Learn about IAM security for Network Flow Monitor.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam-awsmanpol-network-flow-monitor.html): Learn about AWS managed policies for Network Flow Monitor and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-service-linked-roles-network-flow-monitor.html): How service-linked roles give Network Flow Monitor access to resources in your AWS account.

### [Using Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)

Continuously monitor internet performance and availability between your AWS applications and end users, and detect health events.

### [What is Internet Monitor?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.what-is-cwim.html)

Internet Monitor supported AWS Regions.

- [Supported Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.Regions.html): Internet Monitor supported AWS Regions.
- [Components](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html): Components and terms for Internet Monitor.
- [How it works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html): Information about how Internet Monitor works to measure connectivity data and more.
- [Use cases](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-use-cases.html): Internet Monitor use cases.
- [Internet weather map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.outage-map.html): About the global internet weather map in Internet Monitor.
- [Cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html): With Internet Monitor cross-account observability, you can monitor your applications that span multiple AWS accounts within a single AWS Region.
- [Pricing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.pricing.html): Internet Monitor pricing information.
- [Getting started](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.html): Get started by creating a monitor in Internet Monitor in the AWS Management Console.

### [Configure a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-working-with.html)

Create and configure a monitor in Internet Monitor in the AWS Management Console.

- [Create a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-working-with.create.html): Create a monitor in Internet Monitor in the AWS Management Console.
- [Add resources to your monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMMonitorResources.html): When you create a monitor, you must associate your application's resources with it: Amazon Virtual Private Clouds (VPCs), Network Load Balancers, Amazon CloudFront distributions, Network Load Balancers (NLBs), or Amazon WorkSpaces directories.
- [Set your application traffic percentage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html): The coverage that you choose for the percentage of application traffic to monitor determines how many city-networks (client locations and ASNs, typically internet service providers) for your application are monitored, up to an optional city-networks maximum limit that you can also set.
- [Use a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMWhyCreateMonitor.html): There are several ways to use an Internet Monitor monitor after you create it: for example, you can view information in the CloudWatch dashboard, get information by using the AWS Command Line Interface, and set health alerts.
- [Edit a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.edit-monitor.html): Using the Action menu, you can edit a monitor in Amazon CloudWatch Internet Monitor after you create it.
- [Delete a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.delete-monitor.html): Information about how to delete a monitor in Amazon CloudWatch Internet Monitor.

### [Advanced options](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.advanced-options.html)

Information about how to configure advanced options for Internet Monitor.

- [Choose a city-networks limit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html): In addition to setting a traffic percentage for your monitor in Internet Monitor, you can also set a maximum limit for the number of city-networks monitored.
- [Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.change-threshold.html): Information about how to configure health event thresholds for Internet Monitor.
- [Publish internet measurements to S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.Publish-to-S3.html): You can choose to have Internet Monitor publish internet measurements to Amazon S3 for your internet-facing traffic to the monitored city-networks (client locations and ASNs, typically internet service providers) in your monitor, up to the 500,000 city-networks service limit.
- [Examples with the CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started-CLI.html): Examples of using the AWS CLI to complete common tasks with Internet Monitor.

### [Internet Monitor dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-monitor-and-optimize.html)

Using the Internet Monitor dashboard in the AWS Management Console, you can visualize data and get insights and suggestions about your AWS application's internet traffic, and configure options for your monitor.

- [Track real-time performance and availability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html): The Overview page in the Internet Monitor console shows you a high-level view of performance and availability for the traffic that your monitor tracks, and a timeline of when health events have impacted your monitored traffic.
- [View health events and metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-Health-events.html): The Health events page in the Internet Monitor console provides a map of health events that impact the client locations and ASNs for your application.
- [Analyze historical data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-historical-explorer.html): On the Analyze page in the Internet Monitor console, you can view your application's the top client locations for the traffic that you monitor, by traffic volume.
- [Get suggestions to optimize application performance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-insights.html): Use the Optimize page in the Internet Monitor console to get suggestions for how to optimize application performance for your clients.
- [Your monitor details](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-configure.html): Description of the Configure page in the Internet Monitor console.

### [Explore data using tools](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools.html)

Learn how you can query and explore your Internet Monitor information by using CloudWatch tools and the Internet Monitor query interface.

- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-logs-insights.html): You can use CloudWatch Logs Insights queries to filter a subset of logs for a specific city or geography (client location), client ASN (ISP), and AWS source location.
- [CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-contributor-insights.html): CloudWatch Contributor Insights can help you identify top client locations and ASNs (typically, internet service providers or ISPs) for your AWS application.
- [CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-metrics-dashboard.html): You can view or set alarms on Internet Monitor metrics by using CloudWatch alarms and CloudWatch Metrics in the CloudWatch console.
- [Athena with S3 logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools.S3_athena.html): You can use Amazon Athena to query and view the internet measurements that Internet Monitor publishes to an Amazon S3 bucket.
- [Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html): An option for understanding more about internet traffic for your AWS application is to use the Internet Monitor query interface.

### [Add a monitor with another AWS service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-integrations.html)

Add a monitor for Internet Monitor when you create or work with other AWS services.

- [Add monitor when you create an NLB](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.nlb-monitor.html): When you create a Network Load Balancer in the AWS Management Console, you can optionally choose to also set up monitoring for traffic to and from the Network Load Balancer using a monitor in Internet Monitor.
- [Add monitor when you create a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.vpc-monitor.html): When you create a Amazon Virtual Private Cloud VPC in the AWS Management Console, you can optionally choose to also set up monitoring for it in Internet Monitor.
- [Add monitor from the CloudFront console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.cf-monitor.html): On the metrics dashboard for a distribution in Amazon CloudFront console, you can set up additional monitoring for a distribution in Internet Monitor.
- [Create alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-create-alarm.html): Information about creating alarms with Internet Monitor.
- [EventBridge integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-EventBridge-integration.html): Information about how to use Internet Monitor with Amazon EventBridge.
- [Logs and metrics access errors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-troubleshooting.html): To support some features, Internet Monitor must interact with certain Amazon CloudWatch resources, including logs and metrics.
- [Data protection and data privacy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-privacy.html): The AWS shared responsibility model applies to data protection and data privacy in Internet Monitor.

### [Identity and Access Management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam.html)

How to authenticate requests and manage access to your Internet Monitor resources.

- [Upgrade IAM policies to IPv6](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_cwim_security-ipv6-upgrade.html): Upgrading your IAM policies to include IPv6 if you use dual-stack.
- [How Internet Monitor works with IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_service-with-iam-cwim.html): Before you use IAM to manage access to Internet Monitor, learn what IAM features are available to use with Internet Monitor.
- [Confused deputy prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam-cwim-confused-deputy.html): Confused deputy prevention when using multiple AWS services.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-permissions.html): Learn about AWS managed policies for Internet Monitor and recent changes to those policies.
- [Service-linked role](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-service-linked-roles-CWIM.html): How a service-linked role gives Internet Monitor access to resources in your AWS account.

### [Using Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html)

Learn about Network Synthetic Monitor, a service that provides visibility into the performance of the network connecting your AWS hosted applications to your on-premises destinations.

- [How Network Synthetic Monitor works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html): Network Synthetic Monitor is fully managed by AWS, and doesn't require separate agents on monitored resources.
- [Supported AWS Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-regions.html): The AWS Regions where Network Synthetic Monitor is supported are listed in this section.
- [Pricing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pricing-nw.html): Learn about pricing for Network Synthetic Monitor.
- [API operations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Synthetics-API-reference.html): The following table lists Network Synthetic Monitor API operations that you can use with Amazon CloudWatch.

### [Working with monitors and probes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-working-with.html)

Learn about working with Network Synthetic Monitor.

- [Create a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/getting-started-nw.html): Create a monitor in Network Synthetic Monitor to meet your security and compliance objectives.
- [Edit a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-edit.html): Learn how to edit Network Synthetic Monitor information.
- [Delete a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-delete.html): Learn how to delete a Network Synthetic Monitor.
- [Activate or deactivate a probe](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-probe-status.html): Learn how to activate or deactivate a Network Synthetic Monitor probe.
- [Add a probe to a monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-add-probe.html): Learn how to add a Network Synthetic Monitor probe to a monitor.
- [Edit a probe](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-probe-edit.html): Learn how to edit a Network Synthetic Monitor probe.
- [Delete a probe](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-probe-delete.html): Learn how to delete a Network Synthetic Monitor probe.
- [Tag or untag resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-tags-cli.html): You can work with resource tags in Network Synthetic Monitor, to add or remove tags.

### [Network Synthetic Monitor dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-dashboards.html)

Learn about the Network Synthetic Monitor dashboard.

- [Monitor dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-db.html): Learn about monitor dashboards in Network Synthetic Monitor.
- [Probe dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-probe-db.html): Learn about the Network Synthetic Monitor probe dashboards.
- [Specify metrics time frame](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-time-frame.html): Metrics and events on the dashboards in Network Synthetic Monitor use a default time of two hours, calculated from the current time, but you can set a custom metrics default time frame to use.
- [Probe alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cw-nwm-create-alarm.html): Learn about creating alarms with Network Synthetic Monitor.

### [Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-nw.html)

Configure Network Synthetic Monitor to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Network Synthetic Monitor resources.

- [Data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-protection-nw.html): Learn how the AWS shared responsibility model applies to data protection in Network Synthetic Monitor.
- [Infrastructure Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/infrastructure-security-nw.html): Learn how Network Synthetic Monitor isolates service traffic.

### [Identify and access management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/networkmonitoring-iam.html)

AWS Identity and Access Management is a service that helps an administrator securely control access to resources. uses service-linked roles for the permissions that it requires to call other AWS services on your behalf.

- [How Network Synthetic Monitor works with IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_service-with-iam-nw.html): Before you use IAM to manage access to Network Synthetic Monitor, learn what IAM features are available to use with Network Synthetic Monitor.

### [Identity-based policy examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_id-based-policy-examples-nw.html)

By default, users and roles don't have permission to create or modify Network Synthetic Monitor resources.

- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_troubleshoot-nw.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Network Synthetic Monitor and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam-awsmanpol-nw.html): Learn about AWS managed policies for creating and working with CloudWatch network monitors.
- [IAM permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NW-permissions.html): Describes the IAM permissions required to view and create monitors in Network Synthetic Monitor.
- [Service-linked roles](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitoring-using-service-linked-roles-nw.html): How service-linked roles are used by Network Synthetic Monitor,


## [CloudWatch observability solutions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Monitoring-Solutions.html)

- [JVM workload on EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-JVM-On-EC2.html): Explains the solution and best practices for monitoring Java Virtual Machine (JVM) on EC2.
- [NGINX workload on EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-NGINX-On-EC2.html): Explains the solution and best practices for monitoring NGINX on EC2.
- [NVIDIA GPU workload on EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-NVIDIA-GPU-On-EC2.html): Explains the solution and best practices for monitoring NVIDIA GPU workloads on EC2.
- [Kafka workload on EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-Kafka-On-EC2.html): Explains the solution and best practices for monitoring Apache Kafka and Java Virtual Machine (JVM) on EC2.
- [Tomcat workload on EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-Tomcat-On-EC2.html): Explains the solution and best practices for monitoring Apache Tomcat and Java Virtual Machine (JVM) on EC2.
- [EC2 health](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Solution-EC2-Health.html): Explains the solution and best practices for monitoring EC2 instance health.


## [CloudWatch pipelines](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.html)

- [Creating pipelines](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html): Use the pipeline configuration wizard to create data processing pipelines through a guided 4-step process that configures sources, processors, and destinations.
- [Managing pipelines](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managing-pipelines.html): Monitor pipeline health, view processing metrics, and manage pipeline lifecycle through the Pipelines dashboard.

### [Data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-sources.html)

CloudWatch pipelines supports three types of data: AWS services, third-party sources, and custom sources.

### [Third-party data sources integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/third-party-integration-setup.html)

Connect external security tools, identity providers, and monitoring platforms to CloudWatch pipelines for centralized log analysis.

### [CrowdStrike](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/crowdstrike-setup.html)

Integrate CrowdStrike Falcon Data Replicator with CloudWatch Logs using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/crowdstrike-source-setup.html): Configure CrowdStrike Falcon Data Replicator as a data source using Amazon S3 and Amazon SQS.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/crowdstrike-pipeline-setup.html): Set up CloudWatch pipeline to ingest CrowdStrike FDR data into CloudWatch Logs.

### [SentinelOne](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sentinelone-setup.html)

Collect endpoint security logs from SentinelOne using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sentinelone-source-setup.html): Configure SentinelOne as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sentinelone-pipeline-setup.html): Set up CloudWatch pipeline to process SentinelOne security logs.

### [WIZ CNAPP](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/wizcnapp-setup.html)

Collect cloud security data from Wiz CNAPP using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/wizcnapp-source-setup.html): Configure Wiz CNAPP as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/wizcnapp-pipeline-setup.html): Set up CloudWatch pipeline to process Wiz CNAPP security data.

### [Okta SSO](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/okta-sso-setup.html)

Collect system and audit logs from Okta SSO using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/okta-sso-source-setup.html): Configure Okta SSO as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/okta-sso-pipeline-setup.html): Set up CloudWatch pipeline to process Okta SSO logs.

### [Zscaler Internet Access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/zscaler-zia-setup.html)

Collect security logs from Zscaler Internet Access using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/zscaler-zia-source-setup.html): Configure Zscaler Internet Access as a data source for CloudWatch pipeline.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/zscaler-zia-pipeline-setup.html): Set up CloudWatch pipeline to process Zscaler ZIA security logs.

### [Okta Auth0](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth0-setup.html)

Collect authentication and API activity logs from Okta Auth0 using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth0-source-setup.html): Configure Okta Auth0 as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth0-pipeline-setup.html): Set up CloudWatch pipeline to process Okta Auth0 logs.

### [ServiceNow CMDB Audit Log](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicenow-cmdb-setup.html)

Collect configuration data from ServiceNow CMDB using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicenow-cmdb-source-setup.html): Configure ServiceNow CMDB as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicenow-cmdb-pipeline-setup.html): Set up CloudWatch pipeline to process ServiceNow CMDB data.

### [Microsoft Entra ID](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/entraid-setup.html)

Collect sign-in and audit logs from Microsoft Entra ID using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/entraid-source-setup.html): Configure Microsoft Entra ID as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/entraid-pipeline-setup.html): Set up CloudWatch pipeline to process Microsoft Entra ID logs.

### [Microsoft Windows Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/windows-events-setup.html)

Collect Windows Event logs using CloudWatch pipelines for security monitoring.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/windows-events-source-setup.html): Configure Windows Event logs as a data source for CloudWatch pipeline integration.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/windows-events-pipeline-setup.html): Set up CloudWatch pipeline to process Windows Event logs.

### [Palo Alto Networks Next-Generation Firewalls](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/paloalto-ngfw-setup.html)

Collect firewall logs from Palo Alto Networks NGFW using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/paloalto-ngfw-source-setup.html): Configure Palo Alto Networks NGFW as a data source for CloudWatch pipeline.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/paloalto-ngfw-pipeline-setup.html): Set up CloudWatch pipeline to process Palo Alto NGFW logs.

### [GitHub Audit Log](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/github-audit-log-setup.html)

Collect audit logs from GitHub organizations and enterprises using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/github-audit-log-source-setup.html): Configure GitHub as a data source for CloudWatch pipeline audit log collection.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/github-audit-log-pipeline-setup.html): Set up CloudWatch pipeline to process GitHub audit logs.

### [Microsoft 365](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/microsoft365-setup.html)

Collect activity logs from Microsoft 365 services using CloudWatch pipelines.

- [Source configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/microsoft365-source-setup.html): Configure Microsoft 365 as a data source using Office 365 Management API.
- [Pipeline configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/microsoft365-pipeline-setup.html): Set up CloudWatch pipeline to process Microsoft 365 activity logs.
- [Custom log data from CloudWatch Logs or an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ingestion-custom-data-sources.html): Create CloudWatch pipelines pipelines for custom application logs stored in CloudWatch Logs or Amazon S3 buckets.
- [Configuring Custom S3 Bucket Sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/configuring-custom-s3-bucket-sources.html): With CloudWatch pipelines, you can process arbitrary logs stored in S3 buckets.
- [AWS service logs from CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-service-logs-from-cwl.html): Configure CloudWatch Logs from an AWS service as a data source

### [Processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-processors.html)

Configure data transformation and enrichment for your pipeline.

- [Parser processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/parser-processors.html): Parser processors convert raw or semi-structured log data into structured formats.
- [Transformation processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/transformation-processors.html): Transformation processors modify the structure of log events by adding, copying, moving, or removing fields.
- [String manipulation processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/string-processors.html): String processors modify text values within log events through operations like case conversion, trimming, and pattern matching.
- [Common processor use cases](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-examples.html): Here are common scenarios and example configurations for combining processors:
- [Processor compatibility and restrictions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)
- [Sinks](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-sinks.html): Configure destinations for processed log data.
- [CloudWatch pipelines IAM policies and permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-iam-reference.html): This section provides detailed IAM requirements for CloudWatch pipelines, including permissions for API callers, source-specific policies, trust relationships, and resource policies.
- [Extensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-extensions.html): Configure additional pipeline functionality.
- [Monitoring Pipelines Using CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipelines-metrics.html): Monitor your CloudWatch pipelines' health, performance, and data flow using Amazon CloudWatch metrics in the AWS/Observability Admin namespace.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/troubleshooting.html): Common issues and solutions for CloudWatch pipelines configuration, data processing, and performance optimization.


## [Monitor across accounts and Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Cross-Account-Methods.html)

### [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)

Learn how to set up a monitoring account to view CloudWatch, CloudWatch Logs, X-Ray, and CloudWatch Application Insights data from multiple source accounts.

- [Link monitoring accounts with source accounts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html): Learn how to link different AWS accounts for CloudWatch cross-account observability so that you can include necessary permissions.
- [Manage monitoring accounts and source accounts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Unified-Cross-Account-Manage.html): Learn how to manage existing monitoring accounts and source accounts in CloudWatch cross-account observability.
- [Cross-account cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html): Add cross-account cross-Region functionality to your CloudWatch console, dashboards, metrics, and alarms.


## [Explore related telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ExploreRelated.html)

- [How does CloudWatch find related telemetry?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/how-does-related-telemetry-work.html): The CloudWatch Explore related pane shows you metrics and logs that are related to each other, but how does that work?
- [AWS services that support related telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/services-with-related-telemetry.html): The following table lists the AWS services that support related entity information in their CloudWatch telemetry.
- [Add related information to custom telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html): When you publish your own metrics and logs to CloudWatch, the entity information needed for related telemetry is not there by default.


## [Query metrics from other data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.html)

- [Managing access to data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources_Permissions.html): Learn about the permissions needed to connect CloudWatch to other data sources.
- [Connect to a prebuilt data source with a wizard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Connect.html): Learn how to use the wizard to connect CloudWatch to supported data sources, so that you can use CloudWatch to graph, visualize, and create alarms for metrics from these other data sources.
- [Create a custom connector to a data source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Connect-Custom.html): Learn how to manually connect CloudWatch to any data source.
- [Use your custom data source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Custom-Use.html): Learn how to use your custom data source to query and visualize data and create alarms in Amazon CloudWatch.
- [Delete a connector to a data source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Delete.html): Learn how to delete a connector between CloudWatch and a data source.


## [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

- [Supported operating systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/supported-operating-systems.html): The CloudWatch agent is supported on the following operating systems:
- [Prerequisites](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/prerequisites.html): Make sure the following prerequisites are completed before installing the CloudWatch agent for the first time.
- [Download the CloudWatch agent package](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-CloudWatch-Agent-on-EC2-Instance-commandline-first.html): Explains how to use an Amazon S3 download link to install the CloudWatch agent.
- [Verifying the signature of the CloudWatch agent package](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/verify-CloudWatch-Agent-Package-Signature.html): Explains how to verify the authenticity of the CloudWatch agent package using a signature.

### [Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html)

Explains how to install the CloudWatch agent to collect metrics, logs, and traces from Amazon EC2 instances and on-premises servers.

- [Install and Configure Amazon CloudWatch Agent with Workload Detection in the CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-cloudwatch-agent-workload-detection.html)
- [Manual installation on Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/manual-installation.html)
- [Install the CloudWatch agent using AWS Systems Manager](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/installing-cloudwatch-agent-ssm.html): Explains how to use AWS Systems Manager to install the CloudWatch agent to collect metrics, logs, and traces from Amazon EC2 instances and on-premises servers.
- [Install the CloudWatch agent on on-premises servers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-premise.html): Explains how to install the CloudWatch agent on an on-premises server.
- [Install the CloudWatch agent on new instances using CloudFormation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent-New-Instances-CloudFormation.html): Explains how to install the CloudWatch agent using AWS CloudFormation.
- [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html): Explains how to install the CloudWatch agent by installing the CloudWatch Observability EKS add-on.
- [Set up the CloudWatch agent with security-enhanced Linux (SELinux)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-SELinux.html): If your system has security-enhanced Linux (SELinux) enabled, you must apply the appropriate security policies to ensure that the CloudWatch agent runs in a confined domain.

### [Create the CloudWatch agent configuration file](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html)

Explains how to create the CloudWatch agent configuration file, either using the wizard or creating it manually.

### [Create the CloudWatch agent configuration file with the wizard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html)

Explains how to create the CloudWatch agent configuration file using the wizard.

- [Examples of configuration files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-examples.html): Basic system metrics configuration

### [Manually create or edit the CloudWatch agent configuration file](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)

Explains how to manually create the CloudWatch agent configuration file, including the sections and settings inside the CloudWatch agent configuration file.

- [Enable CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Application_Signals.html): Learn how to use the CloudWatch agent to enable CloudWatch Application Signals.
- [Collect network performance metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-network-performance.html): How to use the CloudWatch agent and the ethtool plugin to collect network metrics from EC2 instances.
- [Collect Amazon EBS NVMe driver metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EBS-Collect.html): For CloudWatch agent to collect AWS NVMe driver metrics for Amazon EBS volumes attached to an Amazon EC2 instance, add the diskio section inside the metrics_collected section of the CloudWatch agent configuration file.
- [Collect EC2 instance store metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-instance-store-Collect.html): For CloudWatch agent to collect AWS NVMe driver metrics for instance store volumes attached to an Amazon EC2 instance, add the diskio section inside the metrics_collected section of the CloudWatch agent configuration file.
- [Collect NVIDIA GPU metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html): How to use the CloudWatch agent and to collect NVIDIA GPU metrics from Linux servers.
- [Collect Java Management Extensions (JMX) metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-JMX-metrics.html): How to use the CloudWatch agent to collect Java Management Extensions (JMX) metrics from Amazon EC2 instances and Amazon EKS.
- [Collect metrics and traces with OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html): How to use the CloudWatch agent and OpenTelemetry Protocol (OTLP) to collect metrics and traces.
- [Collect process metrics with the procstat plugin](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-procstat-process-metrics.html): How to use the CloudWatch agent and procstat to collect metrics from processes.
- [Retrieve custom metrics with StatsD](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-statsd.html): How to use the CloudWatch agent and StatsD to collect custom metrics from your applications or services.
- [Retrieve custom metrics with collectd](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-collectd.html): How to use the CloudWatch agent and collectd to collect custom metrics from your applications or services.
- [Set up and configure Prometheus metrics collection on Amazon EC2 instances](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-PrometheusEC2.html): How to use the CloudWatch agent to collect Prometheus metrics from Amazon EC2 instances.
- [Configure information about related entities](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-configure-related-telemetry.html): The CloudWatch agent can send metrics and logs with entity data to support the Explore related pane in the CloudWatch console.
- [Start the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/start-CloudWatch-Agent-on-premise-SSM-onprem.html): Explains how to start the CloudWatch agent.
- [Metrics collected by the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html): Lists the on-premises and additional Amazon EC2 metrics made available by the CloudWatch agent.
- [Using the CloudWatch agent with related telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-RelatedEntities.html): Metrics and logs that are sent to CloudWatch can include an optional entity to correlate telemetry.
- [Common scenarios with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.html): Common scenarios for the CloudWatch agent, including adding custom metric dimensions and running as a different user.
- [CloudWatch agent credentials preference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Credentials-Preference.html): Explains how the CloudWatch agent uses AWS credentials to perform actions with your resources.
- [Troubleshooting the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/troubleshooting-CloudWatch-Agent.html): Troubleshooting tips for installing and running the CloudWatch agent.


## [Embedding metrics within logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)

### [Publishing logs with the embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation.html)

Explains how to generate embedded metric format logs, including the specification for the format.

- [Using the client libraries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html): Explains how to create embedded metric format logs using the client libraries supplied by Amazon.
- [Specification: Embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html): Explains the format of the specification for CloudWatch embedded metric format.
- [Using the PutLogEvents API to send manually-created embedded metric format logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation_PutLogEvents.html): Explains how to generate embedded metric format logs by using the PutLogEvents API.
- [Using the CloudWatch agent to send embedded metric format logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.html): Explains how to generate embedded metric format logs by using the CloudWatch agent.
- [Using the embedded metric format with AWS Distro for OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_OpenTelemetry.html): Explains how to use embedded metric format with the AWS Distro for OpenTelemetry.
- [Viewing your metrics and logs in the console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_View.html): Explains how to view the metrics and logs from embedded metric format logs.
- [Setting alarms on metrics created with the embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Alarms.html): Explains important details about setting alarms on metrics that were created using CloudWatch embedded metric format.


## [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.html)

- [Visualizing your service quotas and setting alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.html): Explains how to visualize your service quotas on a CloudWatch graph, and how to set alarms on them.
- [AWS API usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AWS-API-Usage-Metrics.html): Explains how most AWS services send API usage metrics to CloudWatch.
- [CloudWatch usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html): You can track the usage of CloudWatch APIs in your AWS account.


## [CloudWatch tutorials](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-tutorials.html)

- [Scenario: Monitor estimated charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/gs_monitor_estimated_charges_with_cloudwatch.html): Walks through the scenario of how to monitor your estimated AWS charges using an Amazon CloudWatch alarm.
- [Scenario: Publish metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/PublishMetrics.html): Walks through the scenario of how to publish metrics to Amazon CloudWatch.


## [Code examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/service_code_examples_basics.html)

The following code examples show how to use the basics of CloudWatch with AWS SDKs.

- [Hello CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_Hello_section.html): Hello CloudWatch
- [Learn the basics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.html): Learn core operations for CloudWatch using an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/service_code_examples_actions.html)

The following code examples show how to use CloudWatch with AWS SDKs.

- [DeleteAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DeleteAlarms_section.html): Use DeleteAlarms with an AWS SDK or CLI
- [DeleteAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DeleteAnomalyDetector_section.html): Use DeleteAnomalyDetector with an AWS SDK or CLI
- [DeleteDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DeleteDashboards_section.html): Use DeleteDashboards with an AWS SDK or CLI
- [DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DescribeAlarmHistory_section.html): Use DescribeAlarmHistory with an AWS SDK or CLI
- [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DescribeAlarms_section.html): Use DescribeAlarms with an AWS SDK or CLI
- [DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DescribeAlarmsForMetric_section.html): Use DescribeAlarmsForMetric with an AWS SDK or CLI
- [DescribeAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DescribeAnomalyDetectors_section.html): Use DescribeAnomalyDetectors with an AWS SDK or CLI
- [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_DisableAlarmActions_section.html): Use DisableAlarmActions with an AWS SDK or CLI
- [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_EnableAlarmActions_section.html): Use EnableAlarmActions with an AWS SDK or CLI
- [GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetDashboard_section.html): Use GetDashboard with an AWS SDK or CLI
- [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetMetricData_section.html): Use GetMetricData with an AWS SDK or CLI
- [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetMetricStatistics_section.html): Use GetMetricStatistics with an AWS SDK or CLI
- [GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetMetricWidgetImage_section.html): Use GetMetricWidgetImage with an AWS SDK or CLI
- [ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_ListDashboards_section.html): Use ListDashboards with an AWS SDK or CLI
- [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_ListMetrics_section.html): Use ListMetrics with an AWS SDK or CLI
- [PutAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_PutAnomalyDetector_section.html): Use PutAnomalyDetector with an AWS SDK or CLI
- [PutDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_PutDashboard_section.html): Use PutDashboard with an AWS SDK or CLI
- [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_PutMetricAlarm_section.html): Use PutMetricAlarm with an AWS SDK or CLI
- [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_PutMetricData_section.html): Use PutMetricData with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/service_code_examples_scenarios.html)

The following code examples show how to use CloudWatch with AWS SDKs.

- [Get started with alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_Scenario_GettingStarted_section.html): Get started with CloudWatch alarms using an AWS SDK
- [Manage metrics and alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_Usage_MetricsAlarms_section.html): Manage CloudWatch metrics and alarms using an AWS SDK
- [Monitor DynamoDB performance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cross_MonitorDynamoDB_section.html): Monitor performance of Amazon DynamoDB using an AWS SDK


## [Security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security.html)

- [Data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon CloudWatch.

### [Identity and access management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)

How to authenticate requests and manage access to your CloudWatch resources.

- [How Amazon CloudWatch works with IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_service-with-iam.html): Learn about how Amazon CloudWatch with IAM.
- [Identity-based policy examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_id-based-policy-examples.html): Information about IAM policies and CloudWatch, including the permissions needed to use the CloudWatch console.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security_iam_troubleshoot.html): Learn about how to troubleshoot common issues that you might encounter when working with CloudWatch and IAM.
- [CloudWatch dashboard permissions update](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/dashboard-permissions-update.html): Describes how you can update CloudWatch dashboard permissions to manage access to CloudWatch dashboards.
- [AWS managed (predefined) policies for CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managed-policies-cloudwatch.html): Describes the AWS managed policies for Amazon CloudWatch.
- [Customer managed policy examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/customer-managed-policies-cw.html): Lists example customer managed policies for Amazon CloudWatch.

### [Using condition keys to limit access to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.html)

Provides examples of using IAM policies to limit users to publishing metrics in only specified namespaces.

- [Using condition keys to limit access to CloudWatch namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-namespace.html): Provides examples of using IAM policies to limit users to publishing metrics in only specified namespaces.
- [Using condition keys to limit Contributor Insights users' access to log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-contributor.html): Provides examples of using IAM policies to specify which log groups that users of Contributor Insights can see data from.
- [Using condition keys to limit alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-alarm-actions.html): Provides examples of using IAM policies and condition keys to limit users to creating alarms that can only perform allowed actions.
- [Condition keys for CloudWatch Observability Admin](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/condition-keys-observabilityadmin.html): You can use IAM policies to control access to Amazon CloudWatch Observability Admin resources and actions by using condition keys.
- [Using service-linked roles](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-service-linked-roles.html): How to use service-linked roles to give CloudWatch access to resources in your AWS account.
- [Using a service-linked role for CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-service-linked-roles-RUM.html): How to use a service-linked role to give CloudWatch RUM access to resources in your AWS account.
- [Using service-linked roles for Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CHAP_using-service-linked-roles-appinsights.html): How to use service-linked roles to give CloudWatch Application Insights access to resources in your AWS account.
- [AWS managed policies for Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam-awsmanpol-appinsights.html): Learn about AWS managed policies for Application Insights and recent changes to those policies.
- [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html): Describes the Amazon CloudWatch API operations and the corresponding actions you grant permissions to perform.
- [Compliance validation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon CloudWatch features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/infrastructure-security.html): Learn how Amazon CloudWatch isolates service traffic.
- [AWS Security Hub](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_and_Security_Hub.html): Explains how using AWS Security Hub can benefit you when you use Amazon CloudWatch.
- [Interface VPC endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-interface-VPC.html): Explains how to use CloudWatch CloudWatch Synthetics, and CloudWatch Network Monitoring with interface VPC endpoints.
- [Security considerations for Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html): Explains security considerations for canaries in Amazon CloudWatch Synthetics and the X-Ray Trace Map.
