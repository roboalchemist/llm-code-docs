# Source: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/llms.txt

# AWS CloudTrail User Guide

> Get a history of actions taken by a user, role, or an AWS service account with AWS CloudTrail.

- [Document history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-document-history.html)

## [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

- [How CloudTrail works](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html): This page provides information about CloudTrail features like CloudTrail Event history, CloudTrail Lake, CloudTrail trails, and CloudTrail Insights events.
- [Concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html): This page summarizes basic concepts related to CloudTrail such as describing the types of CloudTrail events.
- [Supported Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html): See the AWS Regions that support CloudTrail.
- [Supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html): This page provides information about supported services and integrations with CloudTrail.
- [Quotas in AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html): This page lists and describes the resource quotas for CloudTrail.


## [CloudTrail tutorials](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html)

- [View event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html): This walkthrough shows you how to use the CloudTrail console to view the last 90 days of management events on the Event history page.

### [Create a trail to log management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html)

This walkthrough shows you how to use the CloudTrail console to create a trail that logs only management events.

- [View your log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail-logs.html): This walkthrough shows you how to view the log files for a trail.
- [Create an event data store for S3 data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-lake-S3.html): This walkthrough shows you how to create an event data store that logs S3 data events.


## [Viewing CloudTrail cost and usage](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-costs.html)

- [Using AWS Budgets to manage costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-budgets-tools.html): AWS Budgets a feature of AWS Billing and Cost Management, allows you to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.
- [Managing CloudTrail trail costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trail-manage-costs.html): This page provides information about how you can configure and manage CloudTrail trails in ways that capture the data you need while remaining cost-effective.
- [Managing CloudTrail Lake costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html): This page provides information about how CloudTrail Lake event data stores and queries incur charges and lists some of the ways you can manage your AWS CloudTrail Lake costs.


## [Working with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)

- [Viewing recent management events with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html): This page describes how to use the CloudTrail console; to view, filter, and download the last 90 days of CloudTrail management events for your AWS account for the current Region.
- [Viewing recent management events with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-cli.html): This page describes how to use the AWS CLI to look up and filter up to the last 90 days of CloudTrail management events for your AWS account for the current Region.


## [Working with CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html)

- [Costs for Insights events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/insights-events-costs.html): This page describes the costs for CloudTrail Insights events and provides some example scenarios to explain how costs are incurred.
- [Delivery of Insights events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/insights-events-understanding.html): This page provides information about CloudTrail Insights events delivery for trails and event data stores.
- [Logging Insights events with the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/insights-events-enable.html): This page describes how to enable an existing trail or event data store to log Insights events using the CloudTrail console.
- [Logging Insights events with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/insights-events-CLI-enable.html): This page describes how to enable a trail or event data store to log Insights events using the AWS CLI.

### [Viewing Insights events for trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-insights-events.html)

This section provides information about viewing the last 90 days of Insights events trails in your AWS account.

- [Viewing Insights events for trails with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-insights-events-console.html): This page provides information about how to use the CloudTrail console to look up, filter, and view the last 90 days of Insights events for trails.
- [Viewing Insights events for trails with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-insights-events-cli.html): This page provides information about how to use the AWS CLI lookup-events command to view and filter the last 90 days of Insights events for any trails that are subscribed to Insights in your AWS account.
- [Viewing Insights events for event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/insights-events-view-lake.html): This page describes how to view the CloudTrail Lake Insights events dashboard.


## [Working with CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

- [CloudTrail Lake supported Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-supported-regions.html): This page lists the supported AWS Regions for CloudTrail Lake.
- [CloudTrail Lake concepts and terminology](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html): This page describes concepts and terminology that are useful for understanding CloudTrail Lake.

### [Event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html)

This page provides information about the CloudTrail Lake event data store types.

### [Create, update, and manage event data stores with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/manage-lake-eds-console.html)

This section describes how to use the CloudTrail console to create, update, and manage CloudTrail Lake event data stores.

- [Create an event data store for CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.html): This page describes how to create an event data store to log CloudTrail management and data events.
- [Create an event data store for Insights events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-insights.html): This page describes how to create a destination event data store to collect CloudTrail Insights events based on unusual management event activity in a source event data store that logs management events and enables Insights.
- [Create an event data store for AWS Config configuration items](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-config.html): This page describes how to create an event data store for AWS Config configuration items with the CloudTrail console.
- [Create an event data store for events outside of AWS](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/event-data-store-integration-events.html): This page describes how you can create an event data store to include events outside of AWS.
- [Update an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-update.html): This page describes how you can use the CloudTrail console to update an event data store's settings.
- [Stop and start event ingestion](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-stop-ingestion.html): This page describes how you can use the CloudTrail console to start or stop an event data store from ingesting live events.
- [Change termination protection](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-termination-protection.html): This page describes how you can use the CloudTrail console to change the termination protection setting on an event data store.
- [Delete an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-delete.html): This page describes how to use the CloudTrail console to delete an event data store.
- [Restore an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-restore.html): This page describes how to use the CloudTrail console to restore an event data store that's pending deletion.
- [Export Data from an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-export-cloudwatch.html): This page describes how CloudTrail Lake event data stores can be used to export historical data into a unified data store for CloudWatch for centralized analysis.

### [Create, update, and manage event data stores with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html)

This page describes the available AWS CLI commands for CloudTrail Lake event data stores.

- [Create an event data store with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-create-eds.html): This page describes how to use the AWS CLI create-event-data-store to create an event data store.
- [Import trail events with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-import-trail-events.html): This page describes how to import trail events to a CloudTrail Lake event data store using the AWS CLI start-import command.
- [Update an event data store with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-update-eds.html): This page describes how to update a CloudTrail Lake event data store by running the AWS CLI update-event-data-store command.
- [Managing event data stores with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-manage-eds.html): This page describes how to run AWS CLI commands to view information about your event data store's settings, start and stop event ingestion, enable and disable Lake query federation, and restore an event data store that is pending deletion.
- [Delete an event data store with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-delete-eds.html): This page describes how to delete an event data store by using the AWS CLI delete-event-data-store command.
- [Manage event data store lifecycles](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-disable-termination.html): This page describes the lifecycle stages of a CloudTrail Lake event data store.

### [Copy trail events to an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake-eds.html)

This page provides information about copying trail events to a CloudTrail Lake event data store.

- [Copy trail events to an existing event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-events-lake.html): This page describes how to copy trail events to an existing CloudTrail Lake event data store from the Event data stores page on the CloudTrail console.
- [Copy trail events to a new event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/scenario-lake-import.html): This page shows you how to copy trail events to a new CloudTrail Lake event data store using the CloudTrail console.
- [View event copy details](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/copy-trail-details.html): This page describes how to view details of a trail event copy with the CloudTrail console.

### [Federate an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html)

This page describes how you can federate an event data store to query your event data from Amazon Athena.

- [Enable Lake query federation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-enable-federation.html): This page describes how you can enable federation on an event data store to query your event data from Amazon Athena.
- [Disable Lake query federation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-disable-federation.html): This page describes how you can disable federation on an event data store.
- [Managing CloudTrail Lake federation resources with AWS Lake Formation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation-lake-formation.html): This page describes how you can manage your CloudTrail Lake federation resources with AWS Lake Formation.
- [Organization event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html): This page provides information about CloudTrail Lake organization event data stores and lists the capabilities that can be performed by the management account and the delegated administrator account.

### [Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html)

This section provides information about how to create a CloudTrail Lake integration with a CloudTrail partner, or a custom integration to collect events outside of AWS.

- [Create an integration with a CloudTrail partner with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration-partner.html): This page describes how to use the CloudTrail console to create a CloudTrail Lake integration with a CloudTrail partner.
- [Create a custom integration with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration-custom.html): This page describes how to use the CloudTrail console to create a custom CloudTrail Lake integration.

### [Create, update, and manage CloudTrail Lake integrations with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html)

This page describes the AWS CLI commands you can use to create, update and manage your CloudTrail Lake integrations.

- [Create an integration with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-create-integration.html): This page describes the AWS CLI commands you run to create a CloudTrail Lake integration.
- [Update a channel with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-update-channel.html): This page describes how you can use the update-channel command to update the name and destination for a channel that is used for a CloudTrail Lake integration.
- [Delete a channel with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-delete-integration.html): This page describes how to use the AWS CLI delete-channel command to delete the channel for a CloudTrail Lake integration.
- [CloudTrail Lake integrations event schema](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-integration-event-schema.html): This page describes the required and optional schema elements for a CloudTrail Lake integration.

### [Dashboards](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard.html)

This page describes how to view CloudTrail Lake dashboards to see event trends for event data stores.

### [View a managed dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-managed.html)

This page describes how to choose from and view one of the CloudTrail Lake managed dashboards.

- [Available managed dashboards](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-managed-dashboards.html): This page describes the managed dashboards offered by CloudTrail Lake.
- [Enable the Highlights dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-highlights.html): This page describes the widgets on the Highlights dashboard and provides the procedure for enabling the Highlights dashboard.
- [Disable the Highlights dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-highlights-disable.html): This page describes how to disable the Highlights dashboard.

### [Create a custom dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-custom.html)

This page describes how to create a custom dashboard by adding one or more widgets.

- [Add a sample widget](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-custom-widgets.html): This section describes how to add a sample widget to a CloudTrail Lake custom dashboard.
- [Create a new widget](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-custom-widgets-new.html): This section describes how to create a new widget for a CloudTrail Lake custom dashboard.
- [Remove a widget](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-custom-widgets-remove.html): This section describes how to remove a widget from a CloudTrail Lake custom dashboard.
- [Set a refresh schedule for a custom dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-refresh.html): This page describes how to set a refresh schedule for a CloudTrail Lake custom dashboard.
- [Disable the refresh schedule for a custom dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-refresh-disable.html): This page describes how to disable a refresh schedule for a CloudTrail Lake custom dashboard.
- [Change termination protection](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-termination-protection.html): This page describes how you can use the CloudTrail console to change the termination protection setting on a dashboard.
- [Delete a custom dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-delete.html): This page describes how to use the CloudTrail console to delete a custom dashboard.

### [Create, update, and manage dashboards with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-cli.html)

This page describes the AWS CLI commands you can use to create, update, and manage dashboards.

### [Create a dashboard with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-cli-create.html)

This page describes how to use the AWS CLI create-dashboard command to create a CloudTrail Lake dashboard.

- [View properties for widgets](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html): This page describes the properties you can configure for each CloudTrail Lake widget view type.
- [Manage dashboards with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-cli-manage.html): This page describes how to use the AWS CLI to manage your CloudTrail Lake dashboards.
- [Delete a dashboard with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-cli-delete.html): This page describes how to use the AWS CLI delete-dashboard command to delete your CloudTrail Lake dashboard.

### [Queries](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-queries.html)

This section provides information about CloudTrail Lake queries.

- [Create CloudTrail Lake queries from natural language prompts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html): This page describes how to use the CloudTrail Lake query generator to a create a SQL query by providing a natural language prompt in English.
- [View sample queries](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-console-queries.html): This page describes how to view the sample queries for available CloudTrail Lake.
- [Create or edit a query](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-create-edit-query.html): This page provides a walkthrough that shows how to use the CloudTrail console to edit a CloudTrail Lake sample query and save it as a new query.
- [Run a query and save query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-run-query.html): This page shows how to use the console to run a CloudTrail Lake query.
- [View query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-results.html): This page describes how you can view the last 7 days of CloudTrail Lake query results on the CloudTrail console.
- [Summarize query results in natural language](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-results-summary.html): This page describes how you can summarize query results on the CloudTrail Lake query results on the CloudTrail console.
- [Download saved query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-download-cloudtrail-lake-query-results.html): This page describes the file format for saved query results and describes how to find saved query results using the console.
- [Validate saved query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-query-results-validation.html): This page describes how you can check the CloudTrail Lake query result files to determine whether they changed after delivery.
- [Optimize queries](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-queries-optimization.html): This section describes how you can improve the performance of CloudTrail Lake queries.
- [Run and manage CloudTrail Lake queries with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-queries-cli.html): This page describes the AWS CLI commands you can use to run and manage CloudTrail Lake queries.
- [CloudTrail Lake SQL constraints](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-limitations.html): This page lists the SQL constraints for CloudTrail Lake.
- [Supported SQL schemas for event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-supported-event-schemas.html): This page lists the supported SQL schemas for CloudTrail Lake event data stores.
- [Supported CloudWatch metrics](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-cloudwatch-metrics.html): This page describes the CloudWatch metrics that are supported by CloudTrail Lake.


## [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html)

### [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)

This section provides information about creating and updating a trail for your AWS account.

### [Creating and updating a trail with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-console.html)

This page describes how you can use the CloudTrail console to create a trail and manage trail settings.

- [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html): This page describes how you can create a trail for your AWS account using the CloudTrail console.
- [Updating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-update-a-trail-console.html): This page describes how to update settings for a trail with the CloudTrail console.
- [Deleting a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.html): This page describes how you can delete a trail with the CloudTrail console.
- [Turning off logging for a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-turning-off-logging.html): This page describes how to stop logging for a trail using the CloudTrail console.

### [Creating, updating, and managing trails with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.html)

This page describes the common AWS CLI commands that you can use to create, update, and manage trails.

- [Using create-trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.html): This page describes how to create a trail by running the AWS CLI create-trail command.
- [Using update-trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.html): This page describes how to update trail properties by running the AWS CLI update-trail command.
- [Managing trails with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-additional-cli-commands.html): This page describes the AWS CLI commands that you can run to get trail status, start and stop logging, and delete trails.
- [Creating multiple trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-multiple-trails.html): This section helps you understand how the trail quota is applied to an AWS Region and why different users create trails to troubleshoot operational and security issues.

### [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

This section describes how to create an organization trail which logs activity for all AWS accounts in your organization.

- [Moving from member account trails to organization trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-best-practice.html): This page provides general guidance about moving from member account trails to organization trails.
- [Prepare for creating a trail for your organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html): This page describes the prerequisites for creating an organization trail, such as minimum required permissions and required roles.
- [Creating a trail for your organization in the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-in-the-console.html): This page provides the procedure for creating an organization trail for your AWS Organizations organization using the CloudTrail console.
- [Creating a trail for an organization with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.html): This page provides examples showing how to create, update, and manage a trail for an organization with the AWS CLI.
- [Troubleshooting](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-troubleshooting.html): This page provides information about how to troubleshoot issues with an organization trail.
- [Understanding multi-Region trails and opt-in Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-multi-region-trails.html): Describes multi-Region trails and AWS opt-in Regions.

### [Copying trail events to CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html)

This page discusses how you can copy trail events to a new or existing CloudTrail Lake event data store.

- [Copy trail events to an existing event data store using the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-events.html): This section describes how to copy trail events to an existing event data store from the Trails page on the CloudTrail console.

### [Getting and viewing your CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html)

This page describes the file name format of CloudTrail log files and describes how to find log files using the console.

- [Downloading your CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-read-log-files.html): This page describes how to download, view, and read your CloudTrail log files using the console.
- [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html): This page provides information about how to configure Amazon SNS notifications for when CloudTrail publishes new log files to your Amazon S3 bucket.
- [Using AWS CloudTrail with interface VPC endpoints](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-and-interface-VPC.html): This page explains how to use CloudTrail with interface VPC endpoints.
- [Naming requirements](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trail-naming-requirements.html): This page provides the naming requirements for CloudTrail resources, Amazon S3 buckets, and KMS keys.
- [AWS account closure and trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-account-closure.html): This page describes why trails remain after an AWS account is closed and how you can get trails deleted.


## [Configure CloudTrail settings](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-settings.html)

### [Organization delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator.html)

This page provides general information about CloudTrail delegated administrators and lists the capabilities of the management account and delegated administrator account.

- [Required permissions to assign a delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator-permissions.html): This page lists the required permissions for adding or removing a CloudTrail delegated administrator.
- [Add a CloudTrail delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-add-delegated-administrator.html): This page shows how to add a CloudTrail delegated administrator to manage your organization trails and organization event data stores using the CloudTrail console and AWS CLI.
- [Remove a CloudTrail delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-remove-delegated-administrator.html): This page shows how to remove a CloudTrail delegated administrator using the CloudTrail console and AWS CLI.
- [Service-linked channels](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-service-linked-channels.html): This page describes how to view information about CloudTrail service-linked channels using the CloudTrail console and AWS CLI.


## [Understanding CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html)

- [Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html): This page describes how you can configure your trails and event data stores to log management events.

### [Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

This page lists the available data event resource types and describes how you can configure your trails or event data stores to log data events.

- [Filtering data events by using advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/filtering-data-events.html): This page describes how you can use advanced event selectors to further filter data events on the eventName, resources.ARN, and readOnly fields to log only the data events of interest.
- [Aggregating data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/aggregating-data-events.html): This section describes how to enable aggregation for data events on your trails using the CloudTrail console and AWS CLI.
- [Network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html): Configure CloudTrail trails or event data stores to log network activity events.
- [Add resource tag keys and IAM global condition keys to events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-context-events.html): This page provides an overview of how you can enrich events for CloudTrail enhanced trails and CloudTrail Lake event data stores by adding resource tag keys and IAM global condition keys.
- [CloudTrail record contents for management, data, and network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html): This page describes the fields contained in a CloudTrail event record for a management, data, or network activity event.
- [CloudTrail record contents for aggregated events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aggregated-events.html): This page describes the fields contained in a CloudTrail aggregated event record.
- [CloudTrail record contents for Insights events for trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-insights-fields-trails.html): This page describes the Insights event fields for trails.
- [CloudTrail record contents for Insights events for event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-insights-fields-lake.html): This page describes the Insights event fields for event data stores.
- [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html): This page describes the fields in the userIdentity element of a CloudTrail event.

### [Non-API events captured by CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-non-api-events.html)

This page describes AWS service events and AWS Management Console sign-in events, which are types of non-API events captured by CloudTrail.

- [AWS service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/non-api-aws-service-events.html): This page describes AWS service events, which are a type of non-API event that AWS CloudTrail logs.
- [AWS Management Console sign-in events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html): This page provides examples of console sign-in events including IAM user sign-in events, root user sign-in events, and federated user sign-in events.


## [CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html)

- [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html): This page describes how by creating a multi-Region trail you can receive CloudTrail log files from multiple AWS Regions in a single Amazon S3 bucket.
- [Managing data consistency](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-data-consistency.html): This page describes how CloudTrail uses a distributed model called eventual consistency to manage data consistency.

### [Monitoring CloudTrail log files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)

This page provides information about monitoring CloudTrail logs; using CloudWatch Logs.

- [Sending events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html): This page describes how to configure your trail to send events to CloudWatch Logs so that you can monitor CloudTrail log events.
- [Creating CloudWatch alarms for CloudTrail events: examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html): This page provides examples that show how to create CloudWatch alarms for CloudTrail log events.
- [Stopping CloudTrail from sending events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/stop-cloudtrail-from-sending-events-to-cloudwatch-logs.html): This page discusses how to use the AWS Management Console to update a trail's settings to stop sending CloudTrail log events to CloudWatch Logs.
- [CloudWatch log group and log stream naming for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-log-group-log-stream-naming-for-cloudtrail.html): This page provides information about the naming convention applied by CloudTrail for CloudWatch Logs log group and log streams.
- [Role policy document for CloudTrail to use CloudWatch Logs for monitoring](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-required-policy-for-cloudwatch-logs.html): This page describes the permissions policy required for CloudTrail to send events to CloudWatch Logs.

### [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

This page describes how to aggregate CloudTrail log files from multiple AWS accounts into a single Amazon S3 bucket.

- [Setting bucket policy for multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-set-bucket-policy-for-multiple-accounts.html): This page describes how you can modify the policy on an Amazon S3 bucket, so that CloudTrail log files can be written to the bucket from multiple accounts.
- [Create trails in additional accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/turn-on-cloudtrail-in-additional-accounts.html): This page describes how to create trails in additional AWS accounts with the AWS Management Console or the AWS CLI and aggregate the log files to one Amazon S3 bucket.
- [Sharing CloudTrail log files between AWS accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-sharing-logs.html): This page describes how to share CloudTrail log files between multiple AWS accounts.

### [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)

This page describes how you can check CloudTrail log files to determine whether they have changed after delivery.

- [Enabling log file integrity validation for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html): This page describes how to enable log file integrity validation for CloudTrail trails.
- [Validating CloudTrail log file integrity with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-cli.html): This page describes how to validate CloudTrail logs by using the AWS CLI.
- [CloudTrail digest file structure](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-digest-file-structure.html): This page describes the purpose and structure of CloudTrail digest files used in log file integrity validation.
- [Custom implementations of CloudTrail log file integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-custom-validation.html): This page provides guidelines for implementing custom solutions for validating the integrity of CloudTrail logs.
- [CloudTrail log file examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-examples.html): This page describes the structure of a CloudTrail log file and shows snippets of logs that show the record for an action.
- [Using the CloudTrail Processing Library](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/use-the-cloudtrail-processing-library.html): This page describes how you can process CloudTrail logs with the CloudTrail Processing Library.


## [Security](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Security.html)

- [Data protection](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS CloudTrail.

### [Identity and Access Management](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security-iam.html)

This section describes how to use IAM to manage access to your CloudTrail resources.

- [How AWS CloudTrail works with IAM](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_service-with-iam.html): This page describes how AWS CloudTrail works with IAM.
- [Identity-based policy examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_id-based-policy-examples.html): This page provides examples of CloudTrail identity-based policies.
- [Resource-based policy examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html): This page describes the requirements for resource-based policies and provides examples.
- [Amazon S3 bucket policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html): This section describes the Amazon S3 bucket policy for CloudTrail trails.
- [Amazon S3 bucket policy for CloudTrail Lake query results](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/s3-bucket-policy-lake-query-results.html): This page describes how you can create and edit a Amazon S3 bucket policy to allow CloudTrail Lake to save query results to the bucket.
- [Amazon SNS topic policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-permissions-for-sns-notifications.html): This page provides an example of an Amazon SNS topic policy that allows CloudTrail to send notifications to it.
- [Troubleshooting](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_troubleshoot.html): This page describes how to troubleshoot IAM issues.

### [Using service-linked roles](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give CloudTrail access to resources in your AWS account.

- [Organization trails and event data stores role](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/using-service-linked-roles-create-slr-for-org-trails.html): How to use service-linked roles to give CloudTrail access to resources in your AWS account.
- [Event context role](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/using-service-linked-roles-create-slr-for-context-management.html): How to use service-linked roles to give CloudTrail access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security-iam-awsmanpol.html): This page provides information about AWS managed policies for CloudTrail and lists recent changes to those policies.
- [Compliance validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/CloudTrail-compliance.html): This page describes what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/disaster-recovery-resiliency.html): This page describes how AWS architecture supports data redundancy, and provides information about specific CloudTrail features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/infrastructure-security.html): This page provides information about infrastructure security and describes how AWS CloudTrail isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cross-service-confused-deputy-prevention.html): This page describes how you can protect against the confused deputy problem by using the aws:SourceArn global condition context key.
- [Security best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html): This page describes security best practices when using AWS CloudTrail.

### [Encrypting CloudTrail log files, digest files, and event data stores with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html)

This page describes how to encrypt CloudTrail trail log files and event data stores with KMS keys.

- [Granting permissions to create a KMS key](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/granting-kms-permissions.html): This page describes how you can grant user permissions to create an KMS key with the AWSKeyManagementServicePowerUser managed policy.

### [Configure AWS KMS key policies for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html)

This page describes how you can give CloudTrail permissions to use an existing KMS key to encrypt log files.

- [Default KMS key policy created in CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/default-kms-key-policy.html): This page shows the default KMS key policy when you create a KMS key from the CloudTrail console.
- [Updating a resource to use your KMS key with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail-update-trail.html): This page describes how to use the AWS Management Console to update an existing trail or an event data store to use an KMS key.
- [Enabling and disabling encryption for CloudTrail log files, digest files and event data stores with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-encryption-cli.html): This page describes how to use the AWS CLI to enable or disable CloudTrail log files encryption with a KMS key.
- [How AWS CloudTrail uses AWS KMS](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-kms-works-with-cloudtrail.html): Learn how AWS CloudTrail uses AWS KMS to encrypt and decrypt log files.
