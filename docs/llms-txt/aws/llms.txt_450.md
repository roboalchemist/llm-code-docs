# Source: https://docs.aws.amazon.com/health/latest/ug/llms.txt

# AWS Health User Guide

> AWS Health provides information about events that can affect your AWS resources. Information is presented in the AWS Management Console as the AWS Health Dashboard and is also available by using the AWS Health API.

- [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
- [Concepts for AWS Health](https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html)
- [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html)
- [Planned lifecycle events for AWS Health](https://docs.aws.amazon.com/health/latest/ug/aws-health-planned-lifecycle-events.html)
- [Document history](https://docs.aws.amazon.com/health/latest/ug/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html)

- [View account events in AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html): You can sign in to your account to get personalized events and recommendations.
- [Configuring Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloud-watch-events-integration.html): Use EventBridge to detect and react to changes for AWS Health events.
- [Manage notifications in AWS User Notifications](https://docs.aws.amazon.com/health/latest/ug/manage-user-notifications.html): Learn how to use AWS User Notifications for AWS Health.


## [Integrating with other systems using the AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html)

- [Demos: Retrieving the last seven days of event data programmatically](https://docs.aws.amazon.com/health/latest/ug/using-global-endpoints-demo.html): Learn how to use a DNS lookup against the global endpoint for AWS Health to determine the active regional endpoint and signing AWS Region.
- [Tutorial: Using the AWS Health API with Java examples](https://docs.aws.amazon.com/health/latest/ug/code-sample-java.html): Learn how to initialize an AWS Health client and retrieve information about events and entities by reviewing Java code examples.


## [Security](https://docs.aws.amazon.com/health/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/health/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Health.

- [Data encryption](https://docs.aws.amazon.com/health/latest/ug/data-encryption.html): Learn about encryption features for AWS Health.

### [Identity and access management](https://docs.aws.amazon.com/health/latest/ug/controlling-access.html)

Authenticate requests and manage access to your AWS Health resources.

- [How AWS Health works with IAM](https://docs.aws.amazon.com/health/latest/ug/security_iam_service-with-iam.html): Use IAM roles, policies, and users to manage access for AWS Health.
- [Identity-based policy examples](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html): Use identity-based policies to allow or restrict access to AWS Health.
- [Troubleshooting](https://docs.aws.amazon.com/health/latest/ug/security_iam_troubleshoot.html): Identify and fix common issues when working with IAM and AWS Health.
- [Using service-linked roles](https://docs.aws.amazon.com/health/latest/ug/using-service-linked-roles.html): Use service-linked roles to give AWS Health access to resources in your AWS account.
- [AWS managed policies for AWS Health](https://docs.aws.amazon.com/health/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Health and recent changes to those policies.
- [Logging and monitoring in AWS Health](https://docs.aws.amazon.com/health/latest/ug/monitoring-overview.html): Monitor and log AWS Health events that occur in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/health/latest/ug/aws-health-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/health/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Health features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/health/latest/ug/infrastructure-security.html): Learn how AWS Health isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/health/latest/ug/vulnerability-analysis-and-management.html): Learn how the AWS shared responsibility model applies to vulnerability analysis and management in AWS Health.
- [Security best practices](https://docs.aws.amazon.com/health/latest/ug/security-best-practices.html): Learn about how to follow security best practices in AWS Health.


## [Aggregating AWS Health events](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html)

- [Enabling organizational view](https://docs.aws.amazon.com/health/latest/ug/enable-organizational-view.html): You can use the AWS Health console to get a centralized view for health events in your AWS organization.
- [Viewing organizational view](https://docs.aws.amazon.com/health/latest/ug/view-organizational-view-events.html): You can use the AWS Health console to get a centralized view for health events in your AWS organization.
- [Disabling organizational view](https://docs.aws.amazon.com/health/latest/ug/disable-organizational-view.html): If you don't want to aggregate events for your organization, you can turn off this feature from the management account or you can disable organizational view by using the DisableHealthServiceAccessForOrganization API operation.

### [Managing delegated administrator views for an organization](https://docs.aws.amazon.com/health/latest/ug/delegated-administrator-organizational-view.html)

Learn how to register and remove delegated administrator accounts for your AWS Health organizational view.

- [Registering a delegated administrator account](https://docs.aws.amazon.com/health/latest/ug/register-a-delegated-administrator.html): Learn how to register delegated administrator accounts in your organization for use with AWS Health.
- [Removing a delegated administrator account](https://docs.aws.amazon.com/health/latest/ug/remove-a-delegated-administrator.html): Learn how to remove a delegated administrator account from your AWS Health orgaizational operations.


## [Monitoring for Health events with EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

- [Creating EventBridge rules for AWS Region coverage](https://docs.aws.amazon.com/health/latest/ug/choosing-a-region.html): TBD
- [Monitoring account-specific and public events for AWS Health](https://docs.aws.amazon.com/health/latest/ug/about-public-events.html): TBD
- [Viewing paginated lists of AWS Health events on EventBridge](https://docs.aws.amazon.com/health/latest/ug/pagnation-of-health-events.html): TBD
- [Aggregating AWS Health events using organizational view and delegated administrator access](https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html): TBD
- [Integrating AWS Health event monitoring and notifications with JIRA and ServiceNow](https://docs.aws.amazon.com/health/latest/ug/SMC-integration.html): TBD
- [Configuring an EventBridge rule to send notifications about events](https://docs.aws.amazon.com/health/latest/ug/creating-event-bridge-events-rule-for-aws-health.html): Learn how to create a rule in Amazon EventBridge to notify you of events in the AWS Health service.
- [Configuring Amazon Q Developer in chat applications to send notifications about events](https://docs.aws.amazon.com/health/latest/ug/receive-health-events-with-aws-chatbot-event-bridge.html): Learn how to configure Amazon Q Developer in chat applications to notify you of events in the AWS Health service.
- [Running operations on EC2 instances automatically in response to events](https://docs.aws.amazon.com/health/latest/ug/automating-instance-actions.html): You can automate actions that respond to scheduled events for your Amazon EC2 instances.
- [Reference: AWS Health events Amazon EventBridge schema](https://docs.aws.amazon.com/health/latest/ug/aws-health-events-eventbridge-schema.html): Review details of the AWS Health events Amazon EventBridge schema.


## [Monitoring AWS Health](https://docs.aws.amazon.com/health/latest/ug/monitoring-logging-health-events.html)

- [Logging AWS Health API calls with AWS CloudTrail](https://docs.aws.amazon.com/health/latest/ug/logging-using-cloudtrail.html): Monitor the use of the AWS Health Dashboard and AWS Health API by using CloudTrail.
