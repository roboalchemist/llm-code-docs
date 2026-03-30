# Source: https://docs.aws.amazon.com/IDR/latest/userguide/llms.txt

# AWS Incident Detection and Response User Guide AWS Incident Detection and Response Concepts and Procedures

> The user guide describes how to onboard to and use the AWS Incident Detection and Response service.

- [Monitoring and observabililty](https://docs.aws.amazon.com/IDR/latest/userguide/observe-idr.html)
- [Reporting](https://docs.aws.amazon.com/IDR/latest/userguide/reporting-idr.html)
- [Security and resiliency](https://docs.aws.amazon.com/IDR/latest/userguide/security-idr.html)
- [Document history](https://docs.aws.amazon.com/IDR/latest/userguide/doc-history-idr.html)

## [What is AWS Incident Detection and Response?](https://docs.aws.amazon.com/IDR/latest/userguide/what-is-idr.html)

- [Terms of use](https://docs.aws.amazon.com/IDR/latest/userguide/idr-prod-terms.html): Describes key terms and conditions for using Incident Detection and Response.
- [Architecture](https://docs.aws.amazon.com/IDR/latest/userguide/idr-arch.html): Learn about the AWS Incident Detection and Response architecture.
- [Roles and responsibilities](https://docs.aws.amazon.com/IDR/latest/userguide/idr-raci.html): Incident Detection and Response RACI
- [Region availability](https://docs.aws.amazon.com/IDR/latest/userguide/idr-availability.html): Describes Incident Detection and Response availability.


## [Get started](https://docs.aws.amazon.com/IDR/latest/userguide/getting-started-idr.html)

- [Onboarding](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-onboard-workload.html): Describes the process to onboard a workload and ingest alarms in AWS Incident Detection and Response.
- [Onboarding questionnaires](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-questionnaire.html): Describes the AWS Incident Detection and Response onboarding and alarm ingestion questionnaire.
- [Workload discovery](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-discovery.html): Describes the AWS Incident Detection and Response workload discovery process.
- [Subscribe a workload](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-acct-subscription.html): Describes AWS Incident Detection and Response account subscription.

### [Define and configure alarms](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarms.html)

Learn about alarm configuration in AWS Incident Detection and Response.

- [Create CloudWatch alarms](https://docs.aws.amazon.com/IDR/latest/userguide/idr-alarms-fit-purpose.html): Describes how to review and configure alarms that best fit the customers' needs.
- [Build CloudWatch alarms with CloudFormation templates](https://docs.aws.amazon.com/IDR/latest/userguide/idr-create-alarms-with-cfn.html): Describes create CloudWatch alarms using CloudFormation templates
- [Example use cases for CloudWatch alarms](https://docs.aws.amazon.com/IDR/latest/userguide/idr-ex-alarm-use-cases.html): Example use cases for CloudWatch alarms in AWS Incident Detection and Response.

### [Ingest alarms](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-ingest-alerts.html)

Describes ingesting alerts from your custom APM tools into AWS Incident Detection and Response.

- [Provision access](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-access-prov.html): Describes provision access to allow AWS Incident Detection and Response to ingest alarms.
- [Integrate with CloudWatch](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-integrate_cloudwatch.html): Describes integrating rules with Amazon CloudWatch.
- [Ingest alarms from APMs with EventBridge integration](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-ingest_alarms_from_apm_to_eventbridge.html): Describes ingesting alarms from APMs with direct integrations with Amazon EventBridge.
- [Example: Integrating notifications from Datadog and Splunk](https://docs.aws.amazon.com/IDR/latest/userguide/example_integrating_notifications.html): Provides a detailed example of integrating Datadog and Splunk notifications to AWS Incident Detection and Response
- [Ingest alarms from APMs without EventBridge integration](https://docs.aws.amazon.com/IDR/latest/userguide/idr-ingesting-alarms-using-webhooks.html): Describes the steps to send events to AWS Incident Detection and Response through Amazon EventBridge using webhooks.
- [Incident Detection and Response Customer Command Line Interface (CLI)](https://docs.aws.amazon.com/IDR/latest/userguide/idr-cli.html): Describes using the AWS Incident Detection and Response CLI to streamline onboarding.


## [Manage workloads](https://docs.aws.amazon.com/IDR/latest/userguide/manage-workloads-idr.html)

- [Develop runbooks and response plans](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-dev-runbook.html): Describes runbook development and coordination in AWS Incident Detection and Response.
- [Test onboarded workloads](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-testing.html): Describes AWS Incident Detection and Response testing.
- [Request changes to a workload](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-change-request.html): Describes AWS Incident Detection and Response Workload change request process

### [Suppress alarms](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-suppress-alarms.html)

Describes how to suppress alarms from engaging AWS Incident Detection and Response

- [Suppress alarms at the alarm source](https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-at-source.html): Learn how to suppress your alarms from engaging Incident Detection and Response at the alarm source.
- [Submit a workload change request to suppress alarms](https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-at-source-wcr.html): Learn how to use a metric match function to suppress a CloudWatch alarm to prevent the alarm engaging with Incident Detection and Response.
- [Tutorial: Use a metric math function to suppress an alarm](https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-tutorial-suppress.html): Follow a tutorial on how to use a metric match function to suppress a CloudWatch alarm to prevent the alarm engaging with Incident Detection and Response.
- [Tutorial: Remove a metric math function to un-suppress an alarm](https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-tutorial-unsuppress.html): Follow a tutorial on how to remove a metric match function to un-suppress a CloudWatch alarm.
- [Offboard a workload](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-offboard.html): Describes how to offboard a workload from AWS Incident Detection and Response


## [Incident management](https://docs.aws.amazon.com/IDR/latest/userguide/incidents-idr.html)

- [Provision access for application teams](https://docs.aws.amazon.com/IDR/latest/userguide/idr-inc-mgmt-access-provision.html): How to provision access to AWS Support Center Console for application teams
- [Request an Incident Response](https://docs.aws.amazon.com/IDR/latest/userguide/inbound-incident-idr.html): Describes the process to request engagement through support cases for any active incident relating to a subscribed workload in AWS Incident Detection and Response.
- [Manage Incident Detection and Response support cases with the AWS Support App in Slack](https://docs.aws.amazon.com/IDR/latest/userguide/aws-support-app-slack.html): Learn more about using the AWS Support App in Slack to manage your Support cases.
