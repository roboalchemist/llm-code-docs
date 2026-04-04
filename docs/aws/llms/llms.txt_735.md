# Source: https://docs.aws.amazon.com/scheduler/latest/UserGuide/llms.txt

# EventBridge Scheduler User Guide

> Describes key concepts and features of Amazon EventBridge Scheduler and provides instructions on data security, authentication, authorization, and examples of interacting with the EventBridge Scheduler API using the console, the AWS CLI, and the EventBridge Scheduler SDKs.

- [What is EventBridge Scheduler?](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)
- [Setting up](https://docs.aws.amazon.com/scheduler/latest/UserGuide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html)
- [Schedule types](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/scheduler/latest/UserGuide/vpc-interface-endpoints.html)
- [Troubleshooting](https://docs.aws.amazon.com/scheduler/latest/UserGuide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/scheduler/latest/UserGuide/doc-history.html)

## [Managing a schedule](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule.html)

- [Changing the schedule state](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-state.html): Learn how to enable or disable an EventBridge Scheduler schedule using the UpdateSchedule API, including AWS CLI and Python examples.
- [Configuring flexible time windows](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html): Learn how to set a flexible time window for an EventBridge Scheduler schedule, using the UpdateSchedule API with the AWS CLI or Python.
- [Configuring a DLQ](https://docs.aws.amazon.com/scheduler/latest/UserGuide/configuring-schedule-dlq.html): Learn how to set up an Amazon SQS dead-letter queue for EventBridge Scheduler schedules, to capture target invocation failures for later troubleshooting.
- [Deleting a schedule](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-delete.html): Learn how to delete an EventBridge Scheduler schedule, either by configuring automatic deletion, or by manually deleting an individual schedule.


## [Managing a schedule group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html)

- [Creating a schedule group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group-create.html): Learn how to create a schedule group in EventBridge Scheduler using the console or AWS CLI, including associating schedules with schedule groups.
- [Deleting a schedule group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group-delete.html): Learn how to delete a schedule group and all associated schedules in EventBridge Scheduler using the console or AWS CLI.


## [Managing targets](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets.html)

- [Using templated targets](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-templated.html): Learn how to use templated targets to invoke common APIs across AWS services such as Amazon SQS, Lambda, and others.
- [Using universal targets](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html): Learn how to use a universal targets, a customizable set of parameters, to invoke a wide set AWS service APIs as EventBridge Scheduler schedule targets.
- [Adding context attributes](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-context-attributes.html): Learn how to use keywords to collect metadata about your EventBridge Scheduler schedule to pass to the invoked target.


## [Security](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security.html)

### [Managing access](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security-iam.html)

How to authenticate requests and manage access to your EventBridge Scheduler resources.

- [Integration with IAM](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security_iam_service-with-iam.html): Learn about what IAM features are available to use with EventBridge Scheduler.
- [Using identity-based policies](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security_iam_id-based-policy-examples.html): Learn how to use IAM identity-based policies to grant users and roles permission to create or modify EventBridge Scheduler resources.
- [Confused deputy prevention](https://docs.aws.amazon.com/scheduler/latest/UserGuide/cross-service-confused-deputy-prevention.html): Learn about how to limit permissions to avoid confused deputy security issues by preventing cross-service impersonation.
- [Troubleshooting](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security_iam_troubleshoot.html): Discover information to help you diagnose and fix common issues when working with EventBridge Scheduler and IAM.

### [Data protection](https://docs.aws.amazon.com/scheduler/latest/UserGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in EventBridge Scheduler.

- [Encryption at rest](https://docs.aws.amazon.com/scheduler/latest/UserGuide/encryption-rest.html): Learn how EventBridge Scheduler integrates with AWS Key Management Service to encrypt and decrypt your data at rest, including using customer managed keys.
- [Encryption in transit](https://docs.aws.amazon.com/scheduler/latest/UserGuide/encryption-transit.html): Learn how EventBridge Scheduler encrypts your data in transit using Transport Layer Security (TLS) for EventBridge Scheduler and target API calls.
- [Compliance validation](https://docs.aws.amazon.com/scheduler/latest/UserGuide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/scheduler/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific EventBridge Scheduler features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/scheduler/latest/UserGuide/infrastructure-security.html): Learn how Amazon EventBridge Scheduler isolates service traffic.


## [Monitoring and metrics](https://docs.aws.amazon.com/scheduler/latest/UserGuide/monitoring-overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/scheduler/latest/UserGuide/monitoring-cloudwatch.html)

Learn how to monitor EventBridge Scheduler using CloudTrail, which collects raw data and processes it into readable, near real-time metrics.

- [Usage metrics](https://docs.aws.amazon.com/scheduler/latest/UserGuide/monitoring-cloudwatch-usage-metrics.html): Discover detailed reference information on the EventBridge Scheduler metrics and dimensions that CloudWatch collects.
- [Monitoring with CloudTrail logs](https://docs.aws.amazon.com/scheduler/latest/UserGuide/logging-using-cloudtrail.html): Learn about logging Amazon EventBridge Scheduler with AWS CloudTrail, which provides a record of actions taken by a user, role, or AWS service.


## [Quotas](https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html)

- [Troubleshooting quotas](https://docs.aws.amazon.com/scheduler/latest/UserGuide/quotas-troubleshooting.html): Learn
