# Source: https://docs.aws.amazon.com/incident-manager/latest/userguide/llms.txt

#  User Guide

> Describes key concepts of Incident Manager and explains how to set up Incident Manager best practices for handling incidents.

- [Setting up](https://docs.aws.amazon.com/incident-manager/latest/userguide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/incident-manager/latest/userguide/getting-started.html)
- [Managing incidents across AWS accounts and Regions](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-cross-account-cross-region.html)
- [Creating incidents automatically or manually](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html)
- [Viewing incident details in the console](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking.html)
- [Performing a post-incident analysis](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html)
- [Tagging resources](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)
- [Troubleshooting](https://docs.aws.amazon.com/incident-manager/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/incident-manager/latest/userguide/doc-history.html)

## [What Is AWS Systems Manager Incident Manager?](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html)

- [Incident lifecycle](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-lifecycle.html): Learn how you can use Incident Manager to manage the incident lifecycle end to end in your organization.


## [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html)

### [Migration guides](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-guides.html)

As AWS Systems Manager Incident Manager will no longer be adding new features or capabilities, it's important for you to understand your alternatives for incident management.

### [Migrating to AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-opscenter.html)

This guide helps you understand key differences between Incident Manager and OpsCenter to decide if OpsCenter fits your operational needs and provides ways to migrate to OpsCenter from AWS Systems Manager Incident Manager.

- [Using migration runbooks for OpsCenter](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-opscenter-runbooks.html): This guide provides step-by-step instructions for migrating your Amazon CloudWatch alarms and Amazon EventBridge rules from AWS Systems Manager Incident Manager to AWS Systems Manager OpsCenter using automated migration runbooks.
- [Migrating to Jira Service Management](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-jira.html): Jira Service Management (JSM) is an IT service management (ITSM) solution that helps teams receive, track, manage, and resolve employee and customer requests through multiple channels including email, chat, help centers, and widgets.
- [Migrating to ServiceNow](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-servicenow.html): ServiceNow Incident Management is a core ITSM module designed to restore normal service operations after unplanned interruptions while minimizing business impact.
- [Migrating to PagerDuty](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-pagerduty.html): PagerDuty is an incident management platform that helps organizations detect, respond to, and even prevent incidents.
- [Exporting Incident Manager data](https://docs.aws.amazon.com/incident-manager/latest/userguide/export-data.html): This topic describes how to use a Python script to export incident records and post-incident analyses from AWS Systems Manager Incident Manager.
- [Cleaning up Incident Manager Resources](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-cleanup.html): If you are no longer using AWS Systems Manager Incident Manager, we recommend you clean up the remaining Incident Manager resources.


## [Preparing for incidents](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)

- [Configuring replication sets and Findings](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html): Learn how to use replication sets and the "Findings" feature with your incident response plans in Incident Manager, a tool in AWS Systems Manager.
- [Creating and configuring contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html): Learn how to set up and use chat channels in Incident Manager, a tool in AWS Systems Manager, to engage responders during incidents by using email, Short Message Service (SMS), or Voice.

### [Managing responder rotations with on-call schedules](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule.html)

Learn how to create on-call schedules with one more more rotations in Incident Manager.

- [Creating an on-call schedule and rotation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule-create.html): Learn to create on an-call schedule with at least one rotation in Incident Manager.
- [Managing an existing on-call schedule](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule-manage.html): Learn how to manage on-call schedules you have already created in Incident Manager.
- [Creating an escalation plan for responder engagement](https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html): Learn how to use escalation channels to engage responsers when an incident is created in Incident Manager, a tool in AWS Systems Manager.
- [Creating and integrating chat channels for responders](https://docs.aws.amazon.com/incident-manager/latest/userguide/chat.html): Learn how to set up and use chat channels for responders to communicate with one another during incidents in Slack, Microsoft Team, and Amazon Chime.
- [Integrating Systems Manager Automation runbooks for incident remediation](https://docs.aws.amazon.com/incident-manager/latest/userguide/runbooks.html): Learn to set up Systems Manager Automation runbooks for use remediatoin in incident responses in AWS Systems Manager Incident Manager.
- [Creating and configuring response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html): Learn how to create a response plan in Incident Manager.
- [Identifying potential causes of incidents from other services](https://docs.aws.amazon.com/incident-manager/latest/userguide/findings.html): Learn how to enable and work with findings from AWS CodeDeploy and AWS CloudFormation in order to help pinpoint causes of incidents in your operation.


## [Tutorials](https://docs.aws.amazon.com/incident-manager/latest/userguide/tutorials.html)

- [Using runbooks with Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/tutorials-runbooks.html): Discover how to use AWS Systems Manager Automation runbooks to automate Incident Manager incident creation and remediation.
- [Managing security incidents](https://docs.aws.amazon.com/incident-manager/latest/userguide/tutorials-security.html): Learn how to manage security incident in Incident Manager by integrating with AWS Security Hub CSPM and Amazon EventBridge.


## [Security](https://docs.aws.amazon.com/incident-manager/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/incident-manager/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Systems Manager Incident Manager.

### [Identity and Access Management](https://docs.aws.amazon.com/incident-manager/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access your Incident Manager resources.

- [How AWS Systems Manager Incident Manager works with IAM](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_service-with-iam.html): Learn how to work with IAM features and resources for AWS Systems Manager Incident Manager.
- [Identity-based policy examples](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html): Learn how to implement and use identity-based policies in Incident Manager operations.
- [Resource-based policy examples](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_resource-based-policy-examples.html): Learn how to create resource-based policy examples for Incident Manager by viewing examples.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/incident-manager/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how to avoid the confused deputy problem in your Incident Manager cross-account, cross-Region operations.
- [Using service-linked roles](https://docs.aws.amazon.com/incident-manager/latest/userguide/using-service-linked-roles.html): Learn how to use service-linked roles to give Incident Manager access to resources in your AWS account.
- [AWS managed policies for Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Incident Manager and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_troubleshoot.html): Learn how to troubleshoot issues with IAM authentication and authorization in your Incident Manager operations.
- [Working with shared contacts and response plans in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html): Learn how to expand the scope of your incident response in Incident Manager by implementing shared contacts and response plans..
- [Compliance validation](https://docs.aws.amazon.com/incident-manager/latest/userguide/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/incident-manager/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Systems Manager Incident Manager features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/incident-manager/latest/userguide/infrastructure-security.html): Learn how AWS Systems Manager Incident Manager isolates service traffic.
- [Working with VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/incident-manager/latest/userguide/vpc-interface-endpoints.html): Learn about the use of an interface VPC endpoint to create private connections between your VPC and AWS Systems Manager Incident Manager.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/incident-manager/latest/userguide/vulnerability.html): Learn about the shared responsibility model for configuration and IT controls between AWS and you.
- [Security best practices](https://docs.aws.amazon.com/incident-manager/latest/userguide/security-best-practices.html): Learn how to improve the security model for your Incident Manager operation through both preventative and detective best practices.


## [Monitoring](https://docs.aws.amazon.com/incident-manager/latest/userguide/monitoring.html)

- [Monitoring metrics with Amazon CloudWatch](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-metrics.html): Learn how to monitor metrics to identify incident and response plan trends.
- [Logging API calls using AWS CloudTrail](https://docs.aws.amazon.com/incident-manager/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Systems Manager Incident Manager calls with AWS CloudTrail.


## [Product and service integrations](https://docs.aws.amazon.com/incident-manager/latest/userguide/integration.html)

- [Storing PagerDuty access credentials in an AWS Secrets Manager secret](https://docs.aws.amazon.com/incident-manager/latest/userguide/integrations-pagerduty-secret.html): Discover how to store PagerDuty access credentials in an AWS Secrets Manager secret to support using your PagerDuty paging workflow and escalation policies in Incident Manager incidents.
