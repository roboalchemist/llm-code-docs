# Source: https://docs.aws.amazon.com/prometheus/latest/userguide/llms.txt

# Amazon Managed Service for Prometheus User Guide

> Provides a conceptual overview of Amazon Managed Service for Prometheus and includes detailed instructions for using the various features.

- [What is Amazon Managed Service for Prometheus?](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
- [Understand and optimize costs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html)
- [Troubleshooting](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-troubleshooting.html)
- [Service quotas](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html)
- [Document History](https://docs.aws.amazon.com/prometheus/latest/userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-getting-started.html)

- [Set up AWS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-setting-up.html): How to get set up with AWS IAM as you begin to use Amazon Managed Service for Prometheus.
- [Create a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-create-workspace.html): Learn how to create your first Amazon Managed Service for Prometheus workspace to store and query metrics from your system.
- [Ingest metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics.html): Learn how to ingest metrics from an EKS cluster into your first Amazon Managed Service for Prometheus workspace.
- [Query metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query.html): Learn what you can do with metrics in your first Amazon Managed Service for Prometheus workspace.


## [Manage workspaces](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-manage-ingest-query.html)

- [Create a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-create-workspace.html): Learn the details of creating an Amazon Managed Service for Prometheus workspace through the AWS CLI or Amazon Managed Service for Prometheus console.
- [Configure your workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-workspace-configuration.html): Learn how to define label sets and set limits for active time series that match them.
- [Edit a workspace alias](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-edit-workspace.html): Learn how to make changes to your Amazon Managed Service for Prometheus workspace setup.
- [Find your workspace details](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-find-workspace-details.html): Learn how to find the ARN or other details for your Amazon Managed Service for Prometheus workspaces using either the AWS CLI or the Amazon Managed Service for Prometheus console.
- [Delete a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-delete-workspace.html): Learn how to delete an Amazon Managed Service for Prometheus workspace, using either the AWS CLI or the Amazon Managed Service for Prometheus console.


## [Ingest metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-methods.html)

### [AWS managed collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector.html)

You can ingest metrics from an Amazon EKS cluster into a Amazon Managed Service for Prometheus workspace using a collector (a scraper) managed by AWS.

- [Integrate Amazon EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html): Learn how to set up and configure AWS managed collectors to automatically scrape Prometheus-compatible metrics from Amazon EKS clusters.
- [Integrate Amazon MSK](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-integration.html): Integrate Amazon MSK with Amazon Managed Service for Prometheus to monitor Kafka clusters with fully managed metric collection.
- [Prometheus-compatible metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-compatible-metrics.html): AWS managed collectors for Amazon Managed Service for Prometheus automatically scrape Prometheus-compatible metrics from an Amazon EKS cluster.
- [Monitor collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-vended-logs.html): Track and troubleshoot collectors using vended logs in Amazon CloudWatch Logs to monitor service discovery, metric collection, and data export operations.

### [Customer managed collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/self-managed-collectors.html)

Learn about ingesting metrics into Amazon Managed Service for Prometheus using a collector that you manage yourself.

- [Secure the ingestion of your metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-secure-metric-ingestion.html): Learn how to keep the data that you ingest into Amazon Managed Service for Prometheus secure.

### [ADOT collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-adot.html)

Learn how you can use AWS Distro for OpenTelemetry to collect metrics from applications running on Amazon EKS, Amazon ECS, and on Amazon EC2 instances.

- [Ingest from EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-OpenTelemetry.html): Learn to use AWS Distro for OpenTelemetry to ingest metrics into an Amazon Managed Service for Prometheus workspace from an Amazon EKS cluster
- [Ingest from Amazon ECS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-OpenTelemetry-ECS.html): Learn how to set up metrics ingestion from Amazon ECS using ADOT.
- [Ingest from an Amazon EC2 instance](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-remote-write-EC2.html): Learn how to ingest metrics from a Prometheus server with remote write running in an Amazon EC2 instance into an Amazon Managed Service for Prometheus workspace.

### [Prometheus collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-prometheus.html)

Learn about using a Prometheus instance as a scraper for metrics to send to Amazon Managed Service for Prometheus.

- [Ingest from a new Prometheus server with Helm](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-new-Prometheus.html): Learn how to use Helm to set up a Prometheus server as an agent to collect metrics for Amazon Managed Service for Prometheus
- [Ingest from Prometheus in Kubernetes on Amazon EC2](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-existing-Prometheus.html): Learn how to use an existing Prometheus server as an agent to collect metrics for Amazon Managed Service for Prometheus.
- [Ingest from Prometheus in Kubernetes on Fargate](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-existing-Prometheus-fargate.html): Learn to use an existing Prometheus server running in Kubernetes on Fargate to scrape metrics and send them to your Amazon Managed Service for Prometheus workspace.

### [High-availability data](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-high-availability.html)

Learn how to set up high availability metric ingestion for Amazon Managed Service for Prometheus.

- [Deduplicating high availability metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-dedupe.html): When sending multiple copies of the same data to Amazon Managed Service for Prometheus to increase availability, you must deduplicate the metrics to avoid changing your totals or being charged multiple times.
- [Send high availability data with Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/Send-high-availability-data.html): Learn how to send high-availability metric data to Amazon Managed Service for Prometheus using a Prometheus agent.
- [Set up high availability metrics with the Prometheus Operator](https://docs.aws.amazon.com/prometheus/latest/userguide/Send-high-availability-data-operator.html): Learn to set up high availability metrics for Amazon Managed Service for Prometheus with a Prometheus agent set up with the Prometheus Operator Helm chart.
- [Send high availability data with ADOT](https://docs.aws.amazon.com/prometheus/latest/userguide/Send-high-availability-data-ADOT.html): Learn to use AWS Distro for Opentelemetry to send high availability data and metrics to your Amazon Managed Service for Prometheus workspace.
- [Send high availability data with the Prometheus community Helm chart](https://docs.aws.amazon.com/prometheus/latest/userguide/Send-high-availability-prom-community.html): Learn how to send high availability metrics to Amazon Managed Service for Prometheus using a Prometheus agent created with the Prometheus community Helm chart.
- [FAQ: High availability configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/HA_FAQ.html)
- [Cross-Region availability](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-send-to-multiple-workspaces.html): Send metrics to multiple Amazon Managed Service for Prometheus workspaces, across Regions, to provide high availability.


## [Query your metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-query.html)

- [Secure your metric queries](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-secure-querying.html): Learn ways that you can secure your data in Amazon Managed Service for Prometheus, while allowing queries from trusted sources.
- [Use Amazon Managed Grafana](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-amg.html): Learn how to set up Amazon Managed Grafana to create dashboards with visualizations for metrics and data stored in Amazon Managed Service for Prometheus.
- [Use Grafana open source](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query-standalone-grafana.html): Learn how to set up open source versions of Grafana to create dashboards with visualizations for metrics and data stored in Amazon Managed Service for Prometheus.
- [Use Grafana in Amazon EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query-grafana-7.3.html): Learn how to set up open source Grafana in an Amazon EKS cluster to create dashboards with visualizations for metrics and data stored in Amazon Managed Service for Prometheus.

### [Use direct queries](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query-APIs.html)

Learn how to directly query Amazon Managed Service for Prometheus with PromQL and the Prometheus-compatible APIs.

- [Query with awscurl](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-compatible-APIs.html): Learn how to use awscurl to call Prometheus-compatible APIs to query your Amazon Managed Service for Prometheus workspace.
- [Query statistics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-stats.html): Learn how to view query statistics for each Amazon Managed Service for Prometheus query.


## [Anomaly detection](https://docs.aws.amazon.com/prometheus/latest/userguide/prometheus-anomaly-detection.html)

- [PreviewAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/userguide/anomaly-detection-api.html): Learn how to use the PreviewAnomalyDetector API in Amazon Managed Service for Prometheus.


## [Recording and alerting rules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-Ruler.html)

- [Necessary IAM permissions](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-IAM-permissions.html): Learn about the IAM permissions needed to set up rules that modify or monitor metrics in Amazon Managed Service for Prometheus.
- [Create a rules file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html): Learn how to create the YAML file to define rules in Amazon Managed Service for Prometheus that can be used to modify or monitor metrics as they are received.
- [Upload a rules file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-rules-upload.html): Learn how to upload a rules file that you have created to your Amazon Managed Service for Prometheus workspace.
- [Edit a rules file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-rules-edit.html): Learn how to edit a rules file in your Amazon Managed Service for Prometheus workspace.
- [Troubleshoot rule evaluations](https://docs.aws.amazon.com/prometheus/latest/userguide/troubleshoot-rule-evaluations.html): Learn how to troubleshoot rule evaluations in Amazon Managed Service for Prometheus.
- [Troubleshooting Ruler](https://docs.aws.amazon.com/prometheus/latest/userguide/Troubleshooting-rule-fail-error.html): Learn how to use CloudWatch Logs to get information about errors in Amazon Managed Service for Prometheus rules configuration.


## [Alert manager](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alert-manager.html)

- [Necessary IAM permissions](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-IAM-permissions.html): Learn about the IAM permissions needed to configure alert manager in Amazon Managed Service for Prometheus.
- [Create a configuration file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html): Learn how to create a configuration file for Amazon Managed Service for Prometheus alert manager.

### [Set up an alert receiver](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver.html)

Learn how to create an Amazon SNS alert receiver for Amazon Managed Service for Prometheus, and send alerts to it.

### [Amazon SNS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-createtopic.html)

Learn how to create a new Amazon SNS topic for use as an alert receiver.

- [Amazon SNS permissions needed](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-AMPpermission.html): Learn how to give Amazon Managed Service for Prometheus the necessary IAM permissions to forward alert messages to an Amazon SNS topic.
- [Send alerts to your Amazon SNS topic](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-config.html): Learn how to configure your Amazon Managed Service for Prometheus alert manager to forward messages to your Amazon SNS topic
- [Send messages as JSON](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-JSON.html): Learn how to configure alert manager to send Amazon Managed Service for Prometheus alerts in JSON rather than plain text.
- [Send alerts to other destinations](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-SNS-otherdestinations.html): Learn to configure Amazon SNS to send Amazon Managed Service for Prometheus alerts to other destinations, such as email, Slack, or OpsGenie.
- [Amazon SNS validation rules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-validation-truncation.html): Amazon Simple Notification Service (Amazon SNS) requires messages to meet certain standards.

### [PagerDuty](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-pagerduty.html)

Learn how to configure PagerDuty for use as an alert receiver in Amazon Managed Service for Prometheus.

- [Configure Secrets Manager and permissions](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-pagerduty-permissions.html): Before you can send alerts to PagerDuty, you must securely store your PagerDuty integration key and configure the necessary permissions.
- [Send alerts to PagerDuty](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-pagerduty-configure-alertmanager.html): To configure alert manager to send alerts to PagerDuty, you need to update your alert manager definition.
- [Upload a configuration file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-upload.html): Learn how to upload an alert manager configuration file that you have created to your Amazon Managed Service for Prometheus workspace.
- [Integrate alerts with Grafana](https://docs.aws.amazon.com/prometheus/latest/userguide/integrating-grafana.html): Learn how to integrate alerts with Amazon Managed Grafana and open source Grafana instances.
- [Troubleshoot alert manager](https://docs.aws.amazon.com/prometheus/latest/userguide/Troubleshooting-alerting.html): Learn how to get more information about alert manager issues using CloudWatch Logs.


## [Monitoring workspaces](https://docs.aws.amazon.com/prometheus/latest/userguide/logging-and-monitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-CW-usage-metrics.html): Learn about Amazon Managed Service for Prometheus metrics that are vended to CloudWatch, and how to create alarms on them.
- [CloudWatch Logs](https://docs.aws.amazon.com/prometheus/latest/userguide/CW-logs.html): Learn how to configure and use Amazon CloudWatch Logs to monitor events in Amazon Managed Service for Prometheus.
- [Query insights and control](https://docs.aws.amazon.com/prometheus/latest/userguide/query-insights-control.html): Learn how to configure and use Amazon CloudWatch Logs to monitor events in Amazon Managed Service for Prometheus.


## [Integrations](https://docs.aws.amazon.com/prometheus/latest/userguide/integrations.html)

- [Amazon EKS cost monitoring](https://docs.aws.amazon.com/prometheus/latest/userguide/integrating-kubecost.html): Learn how to monitor and manage cost and capacity in your container environments using Amazon Managed Service for Prometheus and Amazon EKS cost monitoring with Kubecost.
- [AWS Observability Accelerator](https://docs.aws.amazon.com/prometheus/latest/userguide/obs_accelerator.html): Describes how to use AWS Observability Accelerator Terraform modules to configure observability with Amazon Managed Service for Prometheus.
- [AWS Controllers for Kubernetes](https://docs.aws.amazon.com/prometheus/latest/userguide/integrating-ack.html): Learn how to set up and manage Amazon Managed Service for Prometheus resources using AWS Controllers for Kubernetes (ACK).
- [Amazon CloudWatch metrics with Firehose](https://docs.aws.amazon.com/prometheus/latest/userguide/integrating-cw-firehose.html): Learn how to get Amazon CloudWatch metrics into Amazon Managed Service for Prometheus via Firehose.


## [Security](https://docs.aws.amazon.com/prometheus/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/prometheus/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Managed Service for Prometheus.

- [Data collected by Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/data-protection-Amazon-Service-Prometheus.html): Learn what data is collected by Amazon Managed Service for Prometheus and how it is stored and protected.
- [Encryption at rest](https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html): By default, Amazon Managed Service for Prometheus automatically provides you with encryption at rest and does this using AWS owned encryption keys.

### [Identity and Access Management](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Managed Service for Prometheus resources.

- [How Amazon Managed Service for Prometheus works with IAM](https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Managed Service for Prometheus, learn what IAM features are available to use with Amazon Managed Service for Prometheus.
- [Identity-based policy examples](https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Managed Service for Prometheus resources.
- [Troubleshooting](https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Managed Service for Prometheus and IAM.
- [IAM permissions and policies](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-and-IAM.html): Discusses authentication, authorization, and how Amazon Managed Service for Prometheus works with IAM.
- [Compliance Validation](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/prometheus/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Managed Service for Prometheus features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/prometheus/latest/userguide/infrastructure-security.html): Learn how Amazon Managed Service for Prometheus isolates service traffic.
- [Using service-linked roles](https://docs.aws.amazon.com/prometheus/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon Managed Service for Prometheus access to resources in your AWS account.
- [CloudTrail logs](https://docs.aws.amazon.com/prometheus/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon Managed Service for Prometheus with AWS CloudTrail.
- [Set up IAM roles for service accounts](https://docs.aws.amazon.com/prometheus/latest/userguide/set-up-irsa.html): Learn how to set up IAM roles for service accounts in Amazon Managed Service for Prometheus.
- [Interface VPC endpoints](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-and-interface-VPC.html): Explains how to use Amazon Managed Service for Prometheus with interface VPC endpoints.


## [Tagging](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_tagging.html)

### [Tagging workspaces](https://docs.aws.amazon.com/prometheus/latest/userguide/tagging-workspaces.html)

Explains how to create or change tags on Amazon Managed Service for Prometheus workspaces.

- [Add a tag to a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-workspace-add.html): Explains how to add a tag to an Amazon Managed Service for Prometheus workspace.
- [View tags for a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-workspace-list.html): Explains how to list the tags for an Amazon Managed Service for Prometheus workspace.
- [Edit tags for a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-workspace-update.html): Explains how to edit the tags for an Amazon Managed Service for Prometheus workspace.
- [Remove a tag from a workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-workspace-delete.html): Explains how to remove a tag from an Amazon Managed Service for Prometheus workspace.

### [Tagging rule groups namespaces](https://docs.aws.amazon.com/prometheus/latest/userguide/tagging-rulegroupsnamespaces.html)

Explains how to create or change tags on Amazon Managed Service for Prometheus rule groups namespaces.

- [Add a tag to a rule groups namespace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-rule-groups-namespace-add.html): Explains how to add a tag to an Amazon Managed Service for Prometheus rule groups namespace.
- [View tags for a rule groups namespace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-rule-groups-namespace-list.html): Explains how to get the list of tags for an Amazon Managed Service for Prometheus rule groups namespace.
- [Edit tags for a rule groups namespace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-rule-groups-namespace-update.html): Explains how to edit the tags for an Amazon Managed Service for Prometheus rule groups namespace.
- [Remove a tag from a rule groups namespace](https://docs.aws.amazon.com/prometheus/latest/userguide/how-to-tag-rule-groups-namespace-delete.html): Explains how to remove a tag from an Amazon Managed Service for Prometheus rule groups namespace.


## [API Reference](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference.html)

- [Amazon Managed Service for Prometheus APIs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-AMPApis.html): Provides an overview of the AWS APIs provided by Amazon Managed Service for Prometheus.

### [Prometheus-compatible APIs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-Prometheus-Compatible-Apis.html)

Lists and explains the Prometheus-compatible APIs provided by Amazon Managed Service for Prometheus.

- [CreateAlertManagerAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-CreateAlertManagerAlerts.html): The CreateAlertManagerAlerts operation creates an alert in the workspace.
- [DeleteAlertManagerSilence](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-DeleteSilence.html): The DeleteSilence deletes one alert silence.
- [GetAlertManagerStatus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerStatus.html): The GetAlertManagerStatus retrieves information about the status of alert manager.
- [GetAlertManagerSilence](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerSilence.html): The GetAlertManagerSilence retrieves information about one alert silence.
- [GetLabels](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetLabels.html): The GetLabels operation retrieves the labels associated with a time series.
- [GetMetricMetadata](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetMetricMetadata.html): The GetMetricMetadata operation retrieves metadata about metrics that are currently being scraped from targets.
- [GetSeries](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetSeries.html): The GetSeries operation retrieves list of time series that match a certain label set.
- [ListAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlerts.html): The ListAlerts operation retrieves currently active alerts in the workspace.
- [ListAlertManagerAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlerts.html): The ListAlertManagerAlerts retrieves information about the alerts currently firing in alert manager in the workspace.
- [ListAlertManagerAlertGroups](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlertGroups.html): The ListAlertManagerAlertGroups operation retrieves a list of alert groups configured in alert manager in the workspace.
- [ListAlertManagerReceivers](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerReceivers.html): The ListAlertManagerReceivers operation retrieves information about the receivers configured in alert manager.
- [ListAlertManagerSilences](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerSilences.html): The ListAlertManagerSilences operation retrieves information about the alert silences configured in the workspace.
- [ListRules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListRules.html): The ListRules retrieves information about the rules configured in the workspace.
- [PutAlertManagerSilences](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-PutAlertManagerSilences.html): The PutAlertManagerSilences operation creates a new alert silence or updates an existing one.
- [QueryMetrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-QueryMetrics.html): The QueryMetrics operation evaluates an instant query at a single point in time or over a range of time.
- [RemoteWrite](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-RemoteWrite.html): The RemoteWrite operation writes metrics from a Prometheus server to a remote URL in a standardized format.
