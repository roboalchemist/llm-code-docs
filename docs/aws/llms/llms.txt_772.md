# Source: https://docs.aws.amazon.com/servicequotas/latest/userguide/llms.txt

# Service Quotas User Guide

> Service Quotas is an AWS service that enables you to view and manage the service quotas for your AWS resources and accounts.

- [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [Getting started: Customize the Service Quotas dashboard](https://docs.aws.amazon.com/servicequotas/latest/userguide/getting-started.html)
- [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html)
- [Using request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html)
- [Quotas for Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/reference_limits.html)
- [Document history](https://docs.aws.amazon.com/servicequotas/latest/userguide/document-history.html)

## [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)

- [Verifying your quota request](https://docs.aws.amazon.com/servicequotas/latest/userguide/quota-history.html): Verify your quota request by viewing the request history history in the Service Quotas console.


## [Tagging resources](https://docs.aws.amazon.com/servicequotas/latest/userguide/sq-tagging.html)

- [Enabling required permissions](https://docs.aws.amazon.com/servicequotas/latest/userguide/sq_tags_permissions.html): You must configure permissions to allow your users or roles to manage tags in Service Quotas.
- [Managing tags](https://docs.aws.amazon.com/servicequotas/latest/userguide/sq_tags_managing-console.html): You can manage Service Quotas tags by using the AWS Management Console, the AWS CLI, or the AWS API.
- [Controlling access using tags](https://docs.aws.amazon.com/servicequotas/latest/userguide/sq_tags_access.html): To control access to Service Quotas resources based on tags, you provide the tag information in the condition element of a policy using the aws:ResourceTag/key-name, aws:RequestTag/key-name, or aws:TagKeys condition keys.


## [Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html)

- [Getting started](https://docs.aws.amazon.com/servicequotas/latest/userguide/getting-started-auto-mgmt.html): Start and configure Automatic Management for your Service Quotas.
- [Viewing Automatic Management configuration](https://docs.aws.amazon.com/servicequotas/latest/userguide/viewing-automatic-management.html): Learn how to view Automatic Management configurations for Service Quotas.
- [Updating Automatic Management configuration](https://docs.aws.amazon.com/servicequotas/latest/userguide/updating-automatic-management.html): Learn how to update Automatic Management configurations for service quotas.
- [Excluding quotas from Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/excluding-quotas.html): Learn how to exclude service quotas from Automatic Management.
- [Stopping Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/stopping-automatic-management.html): Use the following procedure to stop Service Quotas Automatic Management of service quotas for supported AWS services in your AWS account using the AWS Management Console or AWS CLI.
- [FAQ](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management-faq.html): Find answers to common questions about Service Quotas Automatic Management.


## [Security](https://docs.aws.amazon.com/servicequotas/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/servicequotas/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Service Quotas.

### [Logging and monitoring](https://docs.aws.amazon.com/servicequotas/latest/userguide/monitoring-overview.html)

Monitor Service Quotas to maintain reliability, availability, and performance.

### [Logging Service Quotas APIs with CloudTrail](https://docs.aws.amazon.com/servicequotas/latest/userguide/logging-using-cloudtrail.html)

Learn about logging Service Quotas with AWS CloudTrail.

- [Service Quotas Automatic Management AWS CloudTrail logs](https://docs.aws.amazon.com/servicequotas/latest/userguide/auto-mgmt-ct-logs.html): The following are AWS CloudTrail logs for Automatic Management critical and non-critical events.
- [Using CloudWatch alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html): >Learn about using Amazon CloudWatch alarms in Service Quotas.

### [Identity and access management](https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html)

Specify the actions that a user can perform with your Service Quotas resources by using IAM permissions.

- [AWS managed policies](https://docs.aws.amazon.com/servicequotas/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Service Quotas and recent changes to those policies.
- [Integrating Service Quotas into EDAs](https://docs.aws.amazon.com/servicequotas/latest/userguide/eventbridge-integration.html): Receive notifications when specific Service Quotas events such as object creation or deletion occur in an Service Quotas with EventBridge.
- [Compliance validation](https://docs.aws.amazon.com/servicequotas/latest/userguide/SERVICE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/servicequotas/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Service Quotas features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/servicequotas/latest/userguide/infrastructure-security.html): Learn how Service Quotas isolates service traffic.
