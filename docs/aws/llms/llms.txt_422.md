# Source: https://docs.aws.amazon.com/grafana/latest/userguide/llms.txt

# Amazon Managed Grafana User Guide

> Provides a conceptual overview of Amazon Managed Grafana and includes detailed instructions for using the various features.

- [What is Amazon Managed Grafana?](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)
- [Service quotas](https://docs.aws.amazon.com/grafana/latest/userguide/AMG_quotas.html)
- [Document history](https://docs.aws.amazon.com/grafana/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html)

- [Set up AWS](https://docs.aws.amazon.com/grafana/latest/userguide/Amazon-Managed-Grafana-setting-up.html): How to get set up with Amazon Web Services (AWS) as you begin to use Amazon Managed Grafana.


## [Manage workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-workspaces-users.html)

- [Grafana version differences](https://docs.aws.amazon.com/grafana/latest/userguide/version-differences.html): When creating a Grafana workspace, you must choose a Grafana version to create.
- [Create a workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-create-workspace.html): Learn how to create a workspace with Amazon Managed Grafana.

### [User authentication](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html)

Explains how Amazon Managed Grafana authenticates users of Amazon Managed Grafana workspaces.

### [SAML](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG-SAML.html)

Explains how you can use SAML to integrate your existing identity provider to authenticate users in your Amazon Managed Grafana workspaces.

- [Azure AD](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-Azure.html): How to use SAML to connect to Amazon Managed Grafana workspaces using Azure Active Directory.
- [CyberArk](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-CyberArk.html): How to use SAML to connect to Amazon Managed Grafana workspaces using CyberArk.
- [Okta](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-okta.html): How to use SAML to connect to Amazon Managed Grafana workspaces using Okta.
- [OneLogin](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-onelogin.html): How to use SAML to connect to Amazon Managed Grafana workspaces using OneLogin.
- [Ping Identity](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-pingone.html): How to use SAML to connect to Amazon Managed Grafana workspaces using Ping Identity.
- [IAM Identity Center](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG-SSO.html): How to use AWS IAM Identity Center to sign into Amazon Managed Grafana workspaces.

### [Grafana version](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-workspace-version-update.html)

You can update your Amazon Managed Grafana workspace to a newer version of Grafana in the Amazon Managed Grafana console in two ways.

- [Troubleshooting issues with updated workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-workspace-version-update-troubleshoot.html): Your updated workspace should continue to work after updating.

### [Enterprise plugins](https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-enterprise-plugins.html)

Explains how to upgrade an Amazon Managed Grafana workspace to get access to Enterprise plugins, and the benefits of upgrading.

- [Managing access to Enterprise plugins](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-workspace-manage-enterprise.html)
- [Link with Grafana Labs](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-workspace-register-enterprise.html): Workspaces upgraded to Amazon Managed Grafana Enterprise plugins get access to support and consulting from Grafana Labs.
- [FAQ for AWS Marketplace Enterprise users](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-ws-mp-license-faq.html): Previously, you may have purchased a license for Grafana Enterprise through AWS Marketplace.
- [Migrate content between workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-workspace-content-migration.html): There are times that you want to migrate your content (including data sources, dashboards, folder, and alert rules) from one workspace to another.
- [Workspace user access](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-users-and-groups-AMG.html): Learn how to manage user and group access to Amazon Managed Grafana workspaces.
- [Permissions for data sources and notifications](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html): Learn how to manage permissions for data sources and notification channels in Amazon Managed Grafana.
- [Creating resources with AWS CloudFormation](https://docs.aws.amazon.com/grafana/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon Managed Grafana using an AWS CloudFormation template.
- [Network access control](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html): You can control how users and hosts access your Grafana workspaces.
- [Encryption at rest](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-encryption-at-rest.html): By default, Amazon Managed Grafana automatically provides you with encryption at rest and does this using AWS owned encryption keys.

### [Connect to data in Amazon VPC](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-vpc.html)

Learn how to connect your Amazon Managed Grafana workspace to data source and notification channels that reside in an Amazon VPC.

- [Troubleshoot VPC](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-vpc-faq.html): Answers to common questions regarding using Amazon Virtual Private Cloud (Amazon VPC) with Amazon Managed Grafana.
- [Configure a workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html): Learn how to configure an Amazon Managed Grafana workspace, including options for alerting and plugin management.
- [Delete a workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-edit-delete-workspace.html): Learn how to delete an Amazon Managed Grafana workspace.


## [Use your Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-working-with-Grafana-workspace.html)

- [Connect to a workspace](https://docs.aws.amazon.com/grafana/latest/userguide/connect-to-workspace.html): Learn how to connect to your Amazon Managed Grafana workspace console, by signing in to your chosen identity provider.

### [Users, teams, and permissions](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-administration-authorization.html)

Explains how to work with teams, team sync, and permissions in Amazon Managed Grafana.

- [Users](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-users.html): Explains how to work with users in Amazon Managed Grafana
- [User roles](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html): Explains the Viewer, Editor, and Admin user roles in Amazon Managed Grafana
- [Managing teams](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-teams.html): Explains how to work with teams Amazon Managed Grafana

### [Using permissions](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-permissions.html)

Use Grafana permissions in Amazon Managed Grafana

- [Dashboard and folder permissions](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-and-folder-permissions.html): For dashboards and dashboard folders, you can use the Permissions page to remove the default role based permissions for Editors and Viewers.
- [Data source permissions](https://docs.aws.amazon.com/grafana/latest/userguide/data-source-permissions.html): By default, data sources can be queried by any user.
- [Your first dashboard](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-grafanaui.html): Creating your first dashboard in a Amazon Managed Grafana workspace, and exploring what you can do with Grafana.

### [Grafana plugins](https://docs.aws.amazon.com/grafana/latest/userguide/grafana-plugins.html)

Grafana plugins add the ability to connect to new data sources, or add visualization or other functionality to the workspace.

- [AWS Data Sources plugin](https://docs.aws.amazon.com/grafana/latest/userguide/aws-datasources-plugin.html): Learn how to use the AWS Data Sources plugin in Amazon Managed Grafana to easily discover AWS resources in your account and use them as data sources.

### [Data sources](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-data-sources.html)

Explains what Amazon Managed Grafana data sources are, and lists the available data sources.

- [Working with AWS Organizations](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-Organizations.html): Explains how Amazon Managed Grafana works with AWS IAM Identity Center and AWS Organizations for managing data source access.

### [Built-in data sources](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-data-sources-builtin.html)

The following data sources are supported in every Amazon Managed Grafana workspace.

- [Alertmanager](https://docs.aws.amazon.com/grafana/latest/userguide/data-source-alertmanager.html): Grafana includes built-in support for Prometheus Alertmanager.

### [Amazon CloudWatch](https://docs.aws.amazon.com/grafana/latest/userguide/using-amazon-cloudwatch-in-AMG.html)

With Amazon Managed Grafana, you can add Amazon CloudWatch as a data source by using the AWS data source configuration option in the Grafana workspace console.

- [Use AWS data source configuration to add CloudWatch as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/adding-CloudWatch-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-managed IAM roles that grant the workspace the IAM policies necessary to read the CloudWatch resources in your account or in your entire organizational unit.
- [Manually add CloudWatch as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/adding--CloudWatch-manual.html)

### [Using the query editor](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-query-editor.html)

The CloudWatch data source in Amazon Managed Grafana provides a powerful query editor that allows you to retrieve and analyze metrics and logs from various AWS services that send data to CloudWatch.

### [Using the metric query editor](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-metric-query-editor.html)

The metric query editor allows you to build two types of queries - Metric Search and Metric Query.

- [Using the metric search option](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-metric-search.html): To create a valid query in Metric Search, you must specify the namespace, metric name and at least one statistic.
- [Using the metric query option to query CloudWatch Metrics Insights data](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-metric-query.html)
- [Using the Amazon CloudWatch Logs query editor](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-logs-query-editor.html): To query CloudWatch Logs, select the Region and up to 20 log groups that you want to query.
- [Curated dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-curated-dashboards.html): The updated CloudWatch data source ships with pre-configured dashboards for five of the most popular AWS services:
- [Templated queries](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-templated-queries.html): Instead of hardcoding details such as servers, applications, and sensor names in your metric queries, you can use variables in their place.
- [Using ec2_instance_attribute examples](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-ec2-instance-attribute-examples.html)
- [Using JSON format template variables](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-using-json-format-template-variables.html): Some queries accept filters in JSON format and Grafana supports the conversion of template variables to JSON.
- [Pricing](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-pricing.html): The Amazon CloudWatch data source for Grafana uses the ListMetrics and GetMetricData CloudWatch API calls to list and retrieve metrics.
- [Service quotas](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-service-quotas.html): AWS defines quotas, or limits, for resources, operations, and items in your AWS account.
- [Cross-account observability](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-cross-account.html)

### [Amazon OpenSearch Service](https://docs.aws.amazon.com/grafana/latest/userguide/using-Amazon-OpenSearch-in-AMG.html)

- [Use AWS data source configuration to add OpenSearch Service as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/ES-adding-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-managed IAM roles that grant the workspace the IAM policies necessary to read the OpenSearch Service resources in your account or in your entire organizational units.
- [Manually add Amazon OpenSearch Service as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/ES-adding-the-data-source.html)
- [Using the Amazon OpenSearch Service data source](https://docs.aws.amazon.com/grafana/latest/userguide/ES-use-datasource.html)
- [OpenSearch Service Serverless](https://docs.aws.amazon.com/grafana/latest/userguide/datasources-opensearch-serverless.html)
- [Traces support](https://docs.aws.amazon.com/grafana/latest/userguide/datasources-opensearch-traces.html): The OpenSearch plugin has support for viewing a list of traces in table form, and a single trace in Trace View, which shows the timeline of trace spans.

### [AWS IoT SiteWise](https://docs.aws.amazon.com/grafana/latest/userguide/using-iotsitewise-in-AMG.html)

- [Use AWS data source configuration to add AWS IoT SiteWise as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/IoTSiteWise-adding-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-managed IAM roles that grant the workspace the IAM policies necessary to read the AWS IoT SiteWise resources in your account or in your entire organizational units.
- [Manually adding the AWS IoT SiteWise data source](https://docs.aws.amazon.com/grafana/latest/userguide/iotsitewise-add-the-data-source.html)
- [Using the AWS IoT SiteWise data source](https://docs.aws.amazon.com/grafana/latest/userguide/IoTSiteWise-using.html): For information about how to use the AWS IoT SiteWise data source, see AWS IoT SiteWise Datasource on Github.

### [AWS IoT TwinMaker](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-iot-twinmaker.html)

Describes how to use an AWS IoT TwinMaker data source in Amazon Managed Grafana.

- [Manually adding the AWS IoT TwinMaker data source](https://docs.aws.amazon.com/grafana/latest/userguide/twinmaker-add-the-data-source.html)
- [Using the AWS IoT TwinMaker data source](https://docs.aws.amazon.com/grafana/latest/userguide/IoT-twinmaker-using.html): For information about how to use the AWS IoT TwinMaker data source, see AWS IoT TwinMaker Datasource on GitHub.

### [Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html)

In Amazon Managed Grafana, the Prometheus data source supports using both self-managed Prometheus servers and Amazon Managed Service for Prometheus workspaces as data sources.

- [Add with AWS data source configuration](https://docs.aws.amazon.com/grafana/latest/userguide/AMP-adding-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-managed IAM roles that grant the workspace the IAM policies necessary to read the Amazon Managed Service for Prometheus resources in your account or in your entire organizational units.
- [Add manually](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-manually-adding.html)
- [Using the Prometheus data source](https://docs.aws.amazon.com/grafana/latest/userguide/using-prometheus-datasource.html)
- [Visualize alerts from Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/amp-configure-alerts.html): You can visualize your Amazon Managed Service for Prometheus or Prometheus alerts in Amazon Managed Grafana by configuring an Alertmanager data source for Prometheus data sources that you are already connected to.
- [Configure exemplars](https://docs.aws.amazon.com/grafana/latest/userguide/amp-configure-exemplars.html)

### [Amazon Timestream](https://docs.aws.amazon.com/grafana/latest/userguide/timestream-datasource.html)

- [Add with AWS data source configuration](https://docs.aws.amazon.com/grafana/latest/userguide/Timestream-adding-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-managed IAM roles that grant the workspace the IAM policies necessary to read the Timestream resources in your account or in your entire organizational units.
- [Add manually](https://docs.aws.amazon.com/grafana/latest/userguide/timestream-add-the-data-source.html)
- [Using the Timestream data source](https://docs.aws.amazon.com/grafana/latest/userguide/timestream-query-editor.html)

### [Amazon Athena](https://docs.aws.amazon.com/grafana/latest/userguide/AWS-Athena.html)

- [Prerequisites](https://docs.aws.amazon.com/grafana/latest/userguide/Athena-prereq.html): To use the managed policies for Amazon Managed Grafana for Athena, complete the following tasks before you configure the Athena data source:
- [Use AWS data source configuration to add Amazon Athena as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/Athena-adding-AWS-config.html)
- [Manually adding the Athena data source](https://docs.aws.amazon.com/grafana/latest/userguide/Athena-add-the-data-source.html)
- [Using Athena data source](https://docs.aws.amazon.com/grafana/latest/userguide/Athena-using-the-data-source.html)

### [Amazon Redshift](https://docs.aws.amazon.com/grafana/latest/userguide/AWS-Redshift.html)

- [Prerequisites](https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-prereq.html): To use the AWS managed policies for Amazon Managed Grafana, complete the following tasks before you configure the Amazon Redshift data source:
- [Use AWS data source configuration to add Amazon Redshift as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-configure.html)
- [Manually adding the Amazon Redshift data source](https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-add-the-data-source.html)
- [Configuring Amazon Redshift](https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-config.html): After adding your Amazon Redshift data source to your workspace, configure Amazon Redshift settings as the following:
- [Using the Amazon Redshift data source](https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-using-the-data-source.html)

### [AWS X-Ray](https://docs.aws.amazon.com/grafana/latest/userguide/x-ray-data-source.html)

- [Use AWS data source configuration to add X-Ray as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/xray-adding-AWS-config.html): To use AWS data source configuration, first you use the Amazon Managed Grafana console to enable service-mananged IAM roles that grant the workspace the IAM policies necessary to read the X-Ray resources in your account or in your entire organizational units.
- [Manually adding the X-Ray data source](https://docs.aws.amazon.com/grafana/latest/userguide/xray-add-the-data-source.html)
- [Using the X-Ray data source](https://docs.aws.amazon.com/grafana/latest/userguide/xray-using.html)
- [Azure monitor](https://docs.aws.amazon.com/grafana/latest/userguide/using-azure-monitor-in-AMG.html): The Azure Monitor data source supports multiple services in the Azure cloud:
- [Graphite](https://docs.aws.amazon.com/grafana/latest/userguide/using-graphite-in-AMG.html): Grafana has an advanced Graphite query editor that lets you quickly navigate the metric space, add functions, change function parameters and much more.
- [Google Cloud Monitoring](https://docs.aws.amazon.com/grafana/latest/userguide/using-google-cloud-monitoring-in-grafana.html)
- [InfluxDB](https://docs.aws.amazon.com/grafana/latest/userguide/using-influxdb-in-AMG.html): Grafana ships with a feature-rich data source plugin for InfluxDB.
- [Jaeger](https://docs.aws.amazon.com/grafana/latest/userguide/jaeger-data-source.html): The Jaeger data source provides open-source, end-to-end distributed tracing.
- [Loki](https://docs.aws.amazon.com/grafana/latest/userguide/using-loki-in-AMG.html): The Loki data source provides access to Loki, Grafanaâs log aggregation system.
- [Microsoft SQL Server](https://docs.aws.amazon.com/grafana/latest/userguide/using-microsoft-sql-server-in-AMG.html): Use the Microsoft SQL Server (MSSQL) data source to query and visualize data from any Microsoft SQL Server 2005 or newer, including Microsoft Azure SQL Database.
- [MySQL](https://docs.aws.amazon.com/grafana/latest/userguide/using-mysql-in-AMG.html): Add the MySQL data source to be able to query and visualize data from a MySQL compatible database.
- [OpenSearch](https://docs.aws.amazon.com/grafana/latest/userguide/using-opensearch-in-AMG.html)
- [OpenTSDB](https://docs.aws.amazon.com/grafana/latest/userguide/using-opentsdb-in-AMG.html): Amazon Managed Grafana ships with advanced support for OpenTSDB.
- [PostgreSQL](https://docs.aws.amazon.com/grafana/latest/userguide/using-postgresql-in-AMG.html): You can use the PostgreSQL data source to query and visualize data from your Amazon Aurora PostgreSQL databases.
- [Templ](https://docs.aws.amazon.com/grafana/latest/userguide/tempo-data-source.html): Tempo is a high-volume, minimal dependency trace storage, OSS tracing solution from Grafana Labs.
- [TestData](https://docs.aws.amazon.com/grafana/latest/userguide/testdata-data-source.html): Grafana ships with a TestData data source, which creates simulated time series data for any panel.
- [Zipkin](https://docs.aws.amazon.com/grafana/latest/userguide/zipkin-data-source.html): Zipkin is an open source, distributed tracing system.

### [Enterprise data sources](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-data-sources-enterprise.html)

The following data sources are supported in workspaces that have been upgraded to Amazon Managed Grafana Enterprise plugins.

- [AppDynamics](https://docs.aws.amazon.com/grafana/latest/userguide/appdynamics-AMG-datasource.html): The AppDynamics data source for Amazon Managed Grafana enables you to query metrics from AppDynamics using its Metrics API and visualize them in Grafana dashboards.
- [Databricks](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-databricks-datasource.html): The Databricks data source enables you to query and visualize Databricks data within Amazon Managed Grafana.
- [Datadog](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datadog-datasource-plugin.html): The Datadog data source enables you to visualize metrics from the Datadog monitoring service in Amazon Managed Grafana.
- [Dynatrace](https://docs.aws.amazon.com/grafana/latest/userguide/dynatrace-AMG-datasource.html): Data source for https://www.dynatrace.com/.
- [GitLab](https://docs.aws.amazon.com/grafana/latest/userguide/gitlab-AMG-datasource.html): The GitLab data source allows you to keep track of detailed GitLab statistics, such as top contributors, commits per day, or deployments per day.
- [Honeycomb](https://docs.aws.amazon.com/grafana/latest/userguide/honeycomb-AMG-datasource.html): The Honeycomb data source allows you to query and visualize Honeycomb metrics and link to Honeycomb traces from within Amazon Managed Grafana.
- [Jira](https://docs.aws.amazon.com/grafana/latest/userguide/jira-AMG-datasource.html): Get the whole picture of your development process by combining issue data from Jira with application performance data from other sources.
- [MongoDB](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-mongodb-datasource.html): The MongoDB Data source enables you to visualize data from MongoDB in Amazon Managed Grafana.
- [New Relic](https://docs.aws.amazon.com/grafana/latest/userguide/new-relic-data-source.html): This section covers New Relic APM and Insights for Grafana.
- [Oracle Database](https://docs.aws.amazon.com/grafana/latest/userguide/oracle-datasource-AMG.html)
- [Salesforce](https://docs.aws.amazon.com/grafana/latest/userguide/salesforce-AMG-datasource.html)
- [SAP HANA](https://docs.aws.amazon.com/grafana/latest/userguide/saphana-AMG-datasource.html): SAP HANAis a high-performance, in-memory database that speeds up data-driven, real-time decisions and \ actions.
- [ServiceNow](https://docs.aws.amazon.com/grafana/latest/userguide/grafana-enterprise-servicenow-datasource.html): This is the ServiceNow data source that is used to connect to ServiceNow instances.
- [Snowflake](https://docs.aws.amazon.com/grafana/latest/userguide/snowflake-datasource-for-AMG.html): With the Snowflake Enterprise data source, you can visualize your Snowflake data alongside all of your other data sources in Grafana as well as log and metric data in context.
- [Splunk](https://docs.aws.amazon.com/grafana/latest/userguide/splunk-datasource.html)
- [Splunk Infrastructure Monitoring](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-splunkinfra.html): Provides support for Splunk Infrastructure Monitoring (formerly SignalFx).
- [Wavefront](https://docs.aws.amazon.com/grafana/latest/userguide/wavefront-datasource-for-AMG.html): The Wavefront (VMware Tanzu Observability by Wavefront) data source enables Amazon Managed Grafana users to query and visualize the data theyâre collecting directly from Wavefront and easily visualize it alongside any other metric, log, tracing, or other data source.

### [Using Grafana version 10](https://docs.aws.amazon.com/grafana/latest/userguide/using-grafana-v10.html)

### [Dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dashboards.html)

- [Using dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-using-dashboards.html)

### [Building dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-building-dashboards.html)

- [Creating dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-creating.html)
- [Importing dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-importing.html)
- [Exporting dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-exporting.html)
- [Modifying dashboard settings](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-modify-settings.html)
- [Dashboard URL variables](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-dashboard-url-variables.html)
- [Managing library panels](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-manage-library-panels.html)
- [Managing dashboard version history](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-manage-version-history.html)
- [Managing dashboard links](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-manage-dashboard-links.html)
- [Annotate visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-annotations.html)
- [Dashboard JSON model](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-dashboard-json-model.html)
- [Best practices](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-bestpractices.html)
- [Managing dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-managing-dashboards.html)
- [Managing playlists](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-managing-playlists.html)
- [Sharing dashboards and panels](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-sharing.html)

### [Variables](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-variables.html)

- [Add and manage variables](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-variable-add.html)
- [Inspect Variables](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-variable-add-inspect.html): The variables page lets you easily identify whether a variable is being referenced (or used) in other variables or dashboard.
- [Variable syntax](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-variable-syntax.html)
- [Assessing dashboard usage](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-assess-dashboard-usage.html)
- [Troubleshoot dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-dash-troubleshoot.html)
- [Searching dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v10-search.html)

### [Panels and visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels.html)

- [Panel editor overview](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-editor-overview.html)
- [The panel inspect view](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-panel-inspector.html)

### [Query and transform data](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-query-xform.html)

- [Write expression queries](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-query-xform-expressions.html)
- [Share query results](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-query-share.html)

### [Transform data](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-xform.html)

- [Transformation functions](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-xform-functions.html)
- [Troubleshoot queries](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-query-troubleshoot.html)
- [Calculation types](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-calculation-types.html)
- [Configure panel options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-panel-options.html)
- [Configure standard options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-standard-options.html)
- [Configure legend](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-legend.html)
- [Configure data links](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-data-links.html)
- [Configure value mappings](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-value-mappings.html)
- [Configure thresholds](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-thresholds.html)
- [Configure field overrides](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-configure-overrides.html)

### [Visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-viz.html)

- [Alert list](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-alert-list.html)
- [Annotations list](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-annotations.html)
- [Bar chart](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-bar-chart.html)
- [Bar gauge](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-bar-gauge.html)
- [Candlestick](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-candlestick.html)
- [Canvas](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-canvas.html)
- [Dashboard list](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-dashboard-list.html)
- [Datagrid](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-datagrid.html)
- [Flame graph](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-flamegraph.html)
- [Gauge](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-gauge.html)
- [Geomap](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-geomap.html)
- [Heatmap](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-heatmap.html)
- [Histogram](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-histogram.html)
- [Logs](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-logs.html)
- [News](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-news.html)
- [Node graph](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-node-graph.html)
- [Pie chart](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-piechart.html)
- [Stat](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-stat.html)
- [State timeline](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-state-timeline.html)
- [Status history](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-status-history.html)
- [Table](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-table.html)
- [Text](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-text.html)

### [Time series](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-time-series.html)

- [Tooltip options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-time-series-panel-tooltip.html)
- [Legend options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-time-series-panel-legend.html)
- [Graph styles](https://docs.aws.amazon.com/grafana/latest/userguide/v10-time-series-graph.html)
- [Axis options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-time-series-axis.html)
- [Color options](https://docs.aws.amazon.com/grafana/latest/userguide/v10-time-series-color.html)
- [Traces](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-traces.html)
- [Trend](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-trend.html)
- [XY Chart](https://docs.aws.amazon.com/grafana/latest/userguide/v10-panels-xychart.html): XY charts provide a way to visualize arbitrary x and y values in a graph so that you can easily show the relationship between two variables.

### [Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore.html)

- [Query management](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore-manage.html)
- [Logs in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore-logs.html)
- [Tracing in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore-tracing.html)
- [Correlations editor](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore-correlations.html)
- [Inspector in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v10-explore-inspector.html)

### [Correlations](https://docs.aws.amazon.com/grafana/latest/userguide/v10-correlations.html)

- [Configuration](https://docs.aws.amazon.com/grafana/latest/userguide/v10-correlations-config.html)
- [Create a new correlation](https://docs.aws.amazon.com/grafana/latest/userguide/v10-correlations-create.html)

### [Alerts](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerts.html)

### [Overview](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview.html)

- [Data sources](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-datasources.html)
- [Alerting on numeric data](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-numeric.html)

### [Labels and annotations](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-labels.html)

- [Label matching](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-labels-matching.html)
- [Labels](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-labels-alerting.html)
- [Label templates](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-overview-labels-templating.html)

### [Alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-rules.html)

- [Alert rule types](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-rules-types.html)
- [Recording rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-rule-recording.html)
- [Queries and conditions](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-rules-queries.html)
- [Alert instances](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-rules-instances.html)
- [Namespaces, folders and groups](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-rules-grouping.html)
- [Rule evaluation](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-rules-evaluation.html)
- [State and health](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-state.html)
- [Notification templating](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-rules-notification-templates.html)
- [Alertmanager](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-alertmanager.html)
- [Contact points](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-contacts.html)

### [Notifications](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-notifications.html)

- [Notification policies](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-notifications-policies-details.html)
- [High availability](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-explore-high-availability.html)

### [Set up Alerting](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-setup.html)

- [Migrating to Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-use-grafana-alerts.html)
- [Adding an external Alertmanager](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-setup-alertmanager.html)

### [Provisioning resources](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-setup-provision.html)

- [Using Terraform](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-setup-provision-terraform.html)
- [View provisioned resources](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-setup-provision-view.html)

### [Configure alerts](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure.html)

- [Grafana managed alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure-grafanamanaged.html)
- [Data source managed alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure-datasourcemanaged.html)
- [Recording rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure-recordingrules.html)
- [Contact points](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure-contactpoints.html)
- [Configure notification policies](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-configure-notification-policies.html)

### [Manage](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage.html)

### [Customize notifications](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-notifications.html)

- [Go templating](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-notifications-go-templating.html)
- [Notification templates](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-create-templates.html)
- [Template reference](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-template-reference.html)
- [Manage contact points](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-contactpoints.html)
- [Silences](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-silences.html)
- [View and filter rules](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-rules-viewfilter.html)
- [Mute timings](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-muting.html)
- [State and health of alerts](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-rulestate.html)
- [View and filter by alert groups](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-viewfiltergroups.html)
- [View notification errors](https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-viewnotificationerrors.html)

### [Using Grafana version 9](https://docs.aws.amazon.com/grafana/latest/userguide/using-grafana-v9.html)

### [Dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dashboards.html)

- [Using dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-using-dashboards.html)

### [Building dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-building-dashboards.html)

- [Creating dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-creating.html)
- [Add or edit panels](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-edit-panels.html)
- [Modifying dashboard settings](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-modify-settings.html)
- [Dashboard URL variables](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-dashboard-url-variables.html)
- [Using library panels](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-manage-library-panels.html)
- [Managing dashboard version history](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-manage-version-history.html)
- [Managing dashboard links](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-manage-dashboard-links.html)
- [Dashboard JSON model](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-dashboard-json-model.html)
- [Managing dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-managing-dashboards.html)
- [Sharing dashboards and panels](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-sharing.html)
- [Managing playlists](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-managing-playlists.html)

### [Variables](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-variables.html)

- [Add and manage variables](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-variable-add.html)
- [Variable syntax](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-variable-syntax.html)
- [Assessing dashboard usage](https://docs.aws.amazon.com/grafana/latest/userguide/v9-dash-assess-dashboard-usage.html)
- [Searching dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/v9-search.html)

### [Panels and visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels.html)

- [Panel editor overview](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-editor-overview.html)
- [Configure panel options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-panel-options.html)
- [Configure standard options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-standard-options.html)

### [Query and transform data](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-xform.html)

- [Write expression queries](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-xform-expressions.html)
- [Share query results](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-share.html)
- [Transform data](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-xform.html)
- [Troubleshoot queries](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-troubleshoot.html)
- [Configure thresholds](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-thresholds.html)
- [Configure data links](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-data-links.html)
- [Configure field overrides](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-overrides.html)
- [Configure value mappings](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-value-mappings.html)
- [Configure legend](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-configure-legend.html)
- [Calculation types](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-calculation-types.html)
- [Annotating visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-annotate-visualizations.html)
- [The panel inspect view](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-panel-inspector.html)

### [Visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-viz.html)

- [Alert list panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-alert-list.html)
- [Annotations panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-annotations.html)
- [Bar chart panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-bar-chart.html)
- [Bar gauge](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-bar-gauge.html)
- [Candlestick panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-candlestick.html)
- [Canvas panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-canvas.html)
- [Clock panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-clock.html)
- [Dashboard list](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-dashboard-list.html)
- [Gauge panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-gauge.html)
- [Geomap panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-geomap.html)
- [Graph panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-graph.html)
- [Heatmap panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-heatmap.html)
- [Histogram panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-histogram.html)
- [Logs panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-logs.html)
- [News panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-news.html)
- [Node graph panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-node-graph.html)
- [Pie chart panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-piechart.html)
- [Plotly panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-plotly.html)
- [Sankey panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-sankey.html)
- [Scatter panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-scatter.html)
- [Stat panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-stat.html)
- [State timeline panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-state-timeline.html)
- [Status history panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-status-history.html)
- [Table panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-table.html)
- [Text panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-text.html)

### [Time series panel](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-time-series.html)

- [Tooltip options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-time-series-panel-tooltip.html)
- [Legend options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-time-series-panel-legend.html)
- [Graph style options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-time-series-graph.html)
- [Axis options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-time-series-axis.html)
- [Color options](https://docs.aws.amazon.com/grafana/latest/userguide/v9-time-series-color.html)
- [Traces panel (Beta)](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-traces.html)
- [WindRose](https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-windrose.html): WindRose panel visualization

### [Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v9-explore.html)

- [Query management in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v9-explore-manage.html)
- [Logs in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v9-explore-logs.html)
- [Tracing in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v9-explore-tracing.html)
- [Inspector in Explore](https://docs.aws.amazon.com/grafana/latest/userguide/v9-explore-inspector.html)

### [Alerts](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerts.html)

- [Overview](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-overview.html)

### [Explore alerting](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore.html)

- [Data sources](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-datasources.html)

### [Alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-rules.html)

- [Alert rule types](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-rules-types.html)
- [Alert instances](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-rules-instances.html)
- [Namespaces and groups](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-rules-grouping.html)
- [Notification templating](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-rules-notification-templates.html)
- [Alerting on numeric data](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-numeric.html)

### [Labels and annotations](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-labels.html)

- [Label matching](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-labels-matching.html)
- [Labels](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-labels-alerting.html)
- [Templating labels and annotations](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-labels-templating.html)
- [States and health](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-state.html)
- [Contact points](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-contacts.html)
- [Notifications](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-explore-notifications.html)

### [Set up Alerting](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-setup.html)

- [Add an external Alertmanager](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-setup-alertmanager.html)

### [Provisioning resources](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-setup-provision.html)

- [Using Terraform](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-setup-provision-terraform.html)
- [View provisioned resources](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-setup-provision-view.html)
- [Migrating to Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-use-grafana-alerts.html)

### [Manage alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules.html)

- [Grafana managed alerts](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules-grafana.html)
- [Mimir or Loki manged rules](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules-mimir-loki.html)
- [Mimir or Loki managed recording rules](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules-mimir-loki-recording.html)
- [Mimir or Loki groups and namespaces](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules-mimir-loki-groups.html)
- [View and edit rules](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managerules-view-edit.html)

### [Alert notifications](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managenotifications.html)

- [Alertmanager](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-managenotifications-alertmanager.html)
- [Contact points](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-contact-points.html)
- [Notification policies](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-notification-policies.html)

### [Customize notifications](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-notifications.html)

- [Go templating](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-notifications-go-templating.html)
- [Notification templates](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-create-templates.html)
- [Template reference](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-template-reference.html)
- [Silences](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-silences.html)
- [Mute timings](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-notification-muting.html)
- [View and filter by alert groups](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-viewfiltergroups.html)
- [View notification errors](https://docs.aws.amazon.com/grafana/latest/userguide/v9-alerting-viewnotificationerrors.html)

### [Using Grafana version 8](https://docs.aws.amazon.com/grafana/latest/userguide/using-grafana-v8.html)

### [Panels](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-panels.html)

Explains how to work with Grafana panels in Amazon Managed Grafana

- [Adding a panel](https://docs.aws.amazon.com/grafana/latest/userguide/add-a-panel-to-a-dashboard.html)
- [Deleting a panel](https://docs.aws.amazon.com/grafana/latest/userguide/Deleting-a-panel.html): How to delete panels in Amazon Managed Grafana
- [Queries](https://docs.aws.amazon.com/grafana/latest/userguide/panel-queries.html): Explains how queries work in Amazon Managed Grafana.
- [Recorded queries](https://docs.aws.amazon.com/grafana/latest/userguide/recorded-queries.html): recorded queries
- [Transformations](https://docs.aws.amazon.com/grafana/latest/userguide/panel-transformations.html): How to use transformations to process metrics before visualization, in Amazon Managed Grafana.
- [Field options and overrides](https://docs.aws.amazon.com/grafana/latest/userguide/field-options-overrides.html): How to use field options and field overrides in Amazon Managed Grafana.
- [Panel editor](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-panel-editor.html): How to use the panel editor in Amazon Managed Grafana.
- [Library panels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-library-panel.html): How to use the library panels in Amazon Managed Grafana.

### [Visualizations](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-visualizations.html)

How to create and use visualizations in Amazon Managed Grafana.

- [Alert list panel](https://docs.aws.amazon.com/grafana/latest/userguide/alert-list-panel.html)
- [Bar chart panel](https://docs.aws.amazon.com/grafana/latest/userguide/bar-chart-panel.html)
- [Bar gauge panel](https://docs.aws.amazon.com/grafana/latest/userguide/alert-panel-bar-gauge-panel.html)
- [Clock panel](https://docs.aws.amazon.com/grafana/latest/userguide/clock-panel.html)
- [Dashboard list panel](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-list-panel.html)
- [Gauge panel](https://docs.aws.amazon.com/grafana/latest/userguide/gauge-panel.html)
- [Geomap panel](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-Geomap.html)
- [Graph panel](https://docs.aws.amazon.com/grafana/latest/userguide/graph-panel.html)
- [Heatmap](https://docs.aws.amazon.com/grafana/latest/userguide/visualization-heatmap.html)
- [Histogram panel](https://docs.aws.amazon.com/grafana/latest/userguide/histogram-panel.html)
- [Logs panel](https://docs.aws.amazon.com/grafana/latest/userguide/logs-panel.html)
- [News panel](https://docs.aws.amazon.com/grafana/latest/userguide/news-panel.html)
- [Node graph panel (Beta)](https://docs.aws.amazon.com/grafana/latest/userguide/node-graph-panel.html)
- [Pie chart panel](https://docs.aws.amazon.com/grafana/latest/userguide/pie-chart-panel.html)
- [Plotly panel](https://docs.aws.amazon.com/grafana/latest/userguide/plotly-panel.html)
- [Sankey panel](https://docs.aws.amazon.com/grafana/latest/userguide/sankey-panel.html)
- [Scatter panel](https://docs.aws.amazon.com/grafana/latest/userguide/scatter-panel.html)
- [Stat panel](https://docs.aws.amazon.com/grafana/latest/userguide/stat-panel.html)
- [State timeline panel](https://docs.aws.amazon.com/grafana/latest/userguide/state-timeline-panel.html)
- [Status history panel](https://docs.aws.amazon.com/grafana/latest/userguide/status-history-panel.html)
- [Table panel](https://docs.aws.amazon.com/grafana/latest/userguide/table-panel.html)
- [Text panel](https://docs.aws.amazon.com/grafana/latest/userguide/text-panel.html)

### [Time series panel](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-panel.html)

- [Graph time series as lines](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-graph-lines.html)
- [Graph time series as bars](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-graph-bars.html)
- [Graph time series as points](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-graph-points.html)
- [Change axis display](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-change-axis.html)

### [Graph stacked time series](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-stacked.html)

- [Stack series in groups](https://docs.aws.amazon.com/grafana/latest/userguide/time-series-stacked-groups.html)
- [Thresholds](https://docs.aws.amazon.com/grafana/latest/userguide/thresholds.html)
- [WindRose](https://docs.aws.amazon.com/grafana/latest/userguide/windrose.html): WindRose panel visualization
- [Inspect a panel](https://docs.aws.amazon.com/grafana/latest/userguide/inspect-a-panel.html)
- [Calculations list](https://docs.aws.amazon.com/grafana/latest/userguide/list-of-calculations.html)

### [Dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-overview.html)

- [Annotations](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-annotations.html)
- [Dashboard folders](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-folders.html)
- [Playlist](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-playlist.html)
- [Dashboard search](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-search.html)
- [Sharing a dashboard](https://docs.aws.amazon.com/grafana/latest/userguide/share-a-dashboard.html)
- [Sharing a panel](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-share-a-panel.html)
- [Time range controls](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-time-range-controls.html)
- [Exporting and importing dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-export-and-import.html)
- [Dashboard version history](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-version-history.html)
- [Keyboard shortcuts](https://docs.aws.amazon.com/grafana/latest/userguide/keyboard-shortcuts.html)
- [Dashboard JSON model](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-json-model.html)
- [Scripted dashboards](https://docs.aws.amazon.com/grafana/latest/userguide/scripted-dashboards.html)
- [Explore](https://docs.aws.amazon.com/grafana/latest/userguide/explore.html)

### [Linking](https://docs.aws.amazon.com/grafana/latest/userguide/linking-in-Amazon-Managed-Service-for-Grafana.html)

- [Dashboard links](https://docs.aws.amazon.com/grafana/latest/userguide/dashboard-links.html)
- [Panel links](https://docs.aws.amazon.com/grafana/latest/userguide/panel-links.html)
- [Data links](https://docs.aws.amazon.com/grafana/latest/userguide/data-links.html)

### [Templates and variables](https://docs.aws.amazon.com/grafana/latest/userguide/templates-and-variables.html)

- [Variable types](https://docs.aws.amazon.com/grafana/latest/userguide/variables-types.html)

### [Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/alerts-overview.html)

- [What's new in Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/alerts-whats-new.html)
- [Migrating to Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/alert-opt-in.html)
- [Alerting fundamentals](https://docs.aws.amazon.com/grafana/latest/userguide/alert-fundamentals.html)
- [Alerting rules](https://docs.aws.amazon.com/grafana/latest/userguide/alert-rules.html)
- [Alert groups](https://docs.aws.amazon.com/grafana/latest/userguide/alert-groups.html)
- [Silencing alert notifications for Prometheus data sources](https://docs.aws.amazon.com/grafana/latest/userguide/alert-silences.html)
- [Working with contact points](https://docs.aws.amazon.com/grafana/latest/userguide/alert-contact-points.html)
- [Using messaging templates](https://docs.aws.amazon.com/grafana/latest/userguide/alert-message-templates.html)
- [Working with notification policies](https://docs.aws.amazon.com/grafana/latest/userguide/alert-notifications.html)
- [Change your preferences](https://docs.aws.amazon.com/grafana/latest/userguide/change-your-grafana-preferences.html): You can perform several tasks on the Preferences tab.
- [Support bundles](https://docs.aws.amazon.com/grafana/latest/userguide/support-bundles.html): Learn how to gather information about your Amazon Managed Grafana workspace using support bundles.

### [Classic alerts](https://docs.aws.amazon.com/grafana/latest/userguide/old-alerts-overview.html)

- [Alert notifications](https://docs.aws.amazon.com/grafana/latest/userguide/old-alert-notifications.html)
- [Creating alerts](https://docs.aws.amazon.com/grafana/latest/userguide/old-create-alerts.html)
- [Pausing an alert rule](https://docs.aws.amazon.com/grafana/latest/userguide/old-pause-an-alert-rule.html)
- [Viewing existing alert rules](https://docs.aws.amazon.com/grafana/latest/userguide/old-view-existing-alert-rules.html)
- [Notification templating](https://docs.aws.amazon.com/grafana/latest/userguide/old-alerts-notification-templating.html)
- [Troubleshooting alerts](https://docs.aws.amazon.com/grafana/latest/userguide/old-troubleshoot-alerts.html)


## [Grafana API Reference](https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html)

### [Authenticate with tokens](https://docs.aws.amazon.com/grafana/latest/userguide/authenticating-grafana-apis.html)

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana token.

- [Service accounts](https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html): You can use a service account to run automated workloads in Grafana, such as dashboard provisioning, configuration, or report generation.
- [API Keys](https://docs.aws.amazon.com/grafana/latest/userguide/using-api-keys.html): One way to access Grafana APIs is to use an API key, which is also called an API token.
- [Alerting API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Alerting.html): How to use Grafana's Alerting API in Amazon Managed Grafana.
- [Alerting Notification Channels API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-AlertingNotificationChannels.html): How to use Grafana's Alerting Notification Channels API in Amazon Managed Grafana.
- [Annotations API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Annotations.html): How to use Grafana's Annotations API in Amazon Managed Grafana.
- [Authentication API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Authentication.html): How to use Grafana's Authentication API in Amazon Managed Grafana.
- [Dashboard API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Dashboard.html): How to use Grafana's Dashboard API in Amazon Managed Grafana.
- [Dashboard Permissions API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-DashboardPermissions.html): How to use Grafana's Folder API in Amazon Managed Grafana.
- [Dashboard Versions API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-DashboardVersions.html): How to use Grafana's Dashboard Versions API in Amazon Managed Grafana.
- [Data Source API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Datasource.html): How to use Grafana's Data source API in Amazon Managed Grafana.
- [Data Source Permissions API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-DatasourcePermissions.html): How to use Grafana's Data source permissions API in Amazon Managed Grafana.
- [External Group Synchronization API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-ExternalGroupSynchronization.html): How to use Grafana's External Group Synchronization API in Amazon Managed Grafana.
- [Folder API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Folder.html): How to use Grafana's Folder API in Amazon Managed Grafana.
- [Folder/Dashboard Search API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-FolderDashboard-Search.html): How to use Grafana's Folder/Dashboard Search API in Amazon Managed Grafana.
- [Folder Permissions API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-FolderPermissions.html): How to use Grafana's Folder API in Amazon Managed Grafana.
- [Organization API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Organization.html): How to use Grafana's Organization API in Amazon Managed Grafana.
- [Playlist API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Playlist.html): How to use Grafana's Playlist API in Amazon Managed Grafana.
- [Plugin API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Plugin.html): How to manage plugins using Grafana HTTP API in Amazon Managed Grafana.
- [Preferences API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Preferences.html): How to use Grafana's Preferences API in Amazon Managed Grafana.
- [Snapshot API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Snapshot.html): How to use Grafana's Snapshot API in Amazon Managed Grafana.
- [Team API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-Team.html): How to use Grafana's Team API in Amazon Managed Grafana.
- [User API](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-API-User.html): How to use Grafana's User API in Amazon Managed Grafana.


## [Observability solutions](https://docs.aws.amazon.com/grafana/latest/userguide/AMG_solutions.html)

- [Monitoring Amazon EKS](https://docs.aws.amazon.com/grafana/latest/userguide/solution-eks.html): Explains how to use a pre-built observability solution to monitor Amazon Elastic Kubernetes Service infrastructure with Amazon Managed Grafana and Amazon Managed Service for Prometheus.
- [Monitoring JVM application](https://docs.aws.amazon.com/grafana/latest/userguide/solution-jvm.html): Explains how to use a pre-built observability solution to monitor a Java Virtual Machine application running in Amazon EKS with Amazon Managed Grafana and Amazon Managed Service for Prometheus.
- [Monitoring Kafka application](https://docs.aws.amazon.com/grafana/latest/userguide/solution-kafka.html): Explains how to use a pre-built observability solution to monitor an Apache Kafka application running on Amazon EKS with Amazon Managed Grafana and Amazon Managed Service for Prometheus.


## [Tagging](https://docs.aws.amazon.com/grafana/latest/userguide/Tagging.html)

- [Tagging workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/Tagging_workspaces.html): Learn about organizing and identifying Amazon Managed Grafana workspaces with tags.


## [Security](https://docs.aws.amazon.com/grafana/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/grafana/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Managed Grafana.

### [Identity and Access Management](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Managed Grafana resources.

- [How Amazon Managed Grafana works with IAM](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Managed Grafana, learn what IAM features are available to use with Amazon Managed Grafana.
- [Identity-based policy examples](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Managed Grafana resources.
- [AWS managed policies](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Managed Grafana and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Managed Grafana and IAM.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/grafana/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Using service-linked roles](https://docs.aws.amazon.com/grafana/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon Managed Grafana access to resources in your AWS account.
- [Permissions and policies for other AWS services](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html): Explains how Amazon Managed Service for Grafana manages permissions for your AMG's access to other AWS services in your account and your organization.
- [IAM permissions](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html): Discusses authentication, authorization, and how Amazon Managed Grafana works with IAM.
- [Compliance Validation](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/grafana/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Managed Grafana features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/grafana/latest/userguide/infrastructure-security.html): Learn how Amazon Managed Grafana isolates service traffic.
- [CloudTrail logs](https://docs.aws.amazon.com/grafana/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon Managed Grafana with AWS CloudTrail.
- [Security best practices](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-Security-Best-Practices.html): Lists the best practices to follow to maintain the security when using Amazon Managed Grafana.
- [Interface VPC endpoints](https://docs.aws.amazon.com/grafana/latest/userguide/VPC-endpoints.html): Create AWS PrivateLink to use Amazon Managed Grafana from within a VPC, or to add security, controlling what computers can access your workspace.
