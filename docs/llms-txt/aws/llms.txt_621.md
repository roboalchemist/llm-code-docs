# Source: https://docs.aws.amazon.com/notifications/latest/userguide/llms.txt

# AWS User Notifications User Guide

> Describes how to set up, configure, and use AWS User Notifications.

- [Enabling AWS Organizations](https://docs.aws.amazon.com/notifications/latest/userguide/uno-orgs.html)
- [Tagging your resources](https://docs.aws.amazon.com/notifications/latest/userguide/tagging-resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/notifications/latest/userguide/user-notifications-troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/notifications/latest/userguide/user-notifications-quotas.html)
- [Glossary](https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html)
- [Document history](https://docs.aws.amazon.com/notifications/latest/userguide/doc-history.html)

## [What is AWS User Notifications?](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html)

- [Supported Regions for User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/supported-regions.html): Learn about supported Regions for User Notifications.


## [AWS managed notifications](https://docs.aws.amazon.com/notifications/latest/userguide/managed-notifications.html)

### [AWS managed notification subscriptions](https://docs.aws.amazon.com/notifications/latest/userguide/manage-mns.html)

You can manage your AWS managed notification subscriptions from the User Notifications console.

- [Adding and removing account contacts for AWS managed notifications](https://docs.aws.amazon.com/notifications/latest/userguide/Add-remove-account-contacts.html): You can determine which contacts receive AWS managed notifications by adding or removing them.
- [Delivery channels](https://docs.aws.amazon.com/notifications/latest/userguide/delivery-channels-managed-notifications.html): Delivery channels are locations where you can send notifications.
- [Viewing AWS managed notifications](https://docs.aws.amazon.com/notifications/latest/userguide/viewing-managed-notifications.html): You can view AWS managed notifications from the Console Notification Center, using the AWS Console Mobile Application, and from your chosen delivery channels.
- [Aggregating and deduplicating AWS managed notifications](https://docs.aws.amazon.com/notifications/latest/userguide/managed-notification-aggregation.html): AWS managed notification aggregation is a standard feature available to all management accounts and delegated administrators that have enabled trusted access with AWS Organizations.


## [User-configured notifications](https://docs.aws.amazon.com/notifications/latest/userguide/uc-notifications.html)

### [Notification configurations](https://docs.aws.amazon.com/notifications/latest/userguide/managing-notifications.html)

This topic covers how to edit and delete notification configurations.

### [Creating your first notification configuration](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html)

Get started with User Notifications.

- [Filtering event rules using customized JSON event patterns](https://docs.aws.amazon.com/notifications/latest/userguide/common-usecases.html): This topic covers common use cases and using the console rule builder.
- [Editing notification configurations](https://docs.aws.amazon.com/notifications/latest/userguide/edit-notifications.html): You can change which configurations create notifications by editing your notification configurations.
- [Deleting notification configurations](https://docs.aws.amazon.com/notifications/latest/userguide/delete-notifications.html): You can stop receiving notifications by deleting notification configurations.

### [Notification hubs](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html)

This topic covers notification hubs.

- [Adding or removing a notification hub](https://docs.aws.amazon.com/notifications/latest/userguide/nhr-add-remove.html): You can add or remove a notification hub using the AWS Management Console.
- [Enabling or disabling opt-in Regions](https://docs.aws.amazon.com/notifications/latest/userguide/nhr-optin-out.html): Although most AWS Regions are active by default for your AWS account, certain Regions are activated only when you manually select them.
- [Managing notifications across your organization](https://docs.aws.amazon.com/notifications/latest/userguide/managing-org-notifications.html): Learn how to configure and manage notifications across your organization using AWS User Notifications.


## [Delivery channels](https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html)

- [Adding delivery channels](https://docs.aws.amazon.com/notifications/latest/userguide/manage-delivery-channels.html): You can add delivery channels for both user-configured notifications and AWS managed notifications from the User Notifications console to have your notifications sent to other locations.

### [Viewing delivery channel details](https://docs.aws.amazon.com/notifications/latest/userguide/detail-delivery-channels.html)

You can view delivery channel details from the User Notifications console.

- [Removing delivery channels](https://docs.aws.amazon.com/notifications/latest/userguide/remove-delivery-channels.html): You can remove delivery channels from notification configurations and toggle off AWS managed notification subscription categories from a delivery channel's detail view.
- [Deleting email addresses](https://docs.aws.amazon.com/notifications/latest/userguide/delete-delivery-channels.html): You can delete emails used as delivery channels.


## [Security](https://docs.aws.amazon.com/notifications/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/notifications/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in User Notifications.
- [Connecting to AWS User Notifications with interface VPC endpoints](https://docs.aws.amazon.com/notifications/latest/userguide/vpc.html): Learn how to connect to AWS User Notifications using interface VPC endpoints.

### [Identity and access management](https://docs.aws.amazon.com/notifications/latest/userguide/security-iam.html)

How to authenticate requests and manage access your User Notifications resources.

- [How AWS User Notifications works with IAM](https://docs.aws.amazon.com/notifications/latest/userguide/security_iam_service-with-iam.html): How User Notifications works with IAM
- [Identity-based policy examples](https://docs.aws.amazon.com/notifications/latest/userguide/security_iam_id-based-policy-examples.html): Learn about User Notifications and its identity based policies
- [Resource-level permissions](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html): How to use resource-based permissions with User Notifications .

### [Using Service-Linked Roles](https://docs.aws.amazon.com/notifications/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give User Notifications access to resources in your AWS account.

- [Service-linked role for calling AWS services, publishing metrics, and using AWS Organizations](https://docs.aws.amazon.com/notifications/latest/userguide/slr-call-services.html): User Notifications uses the service-linked role named AWSServiceRoleForAWSUserNotifications.
- [Managed rules](https://docs.aws.amazon.com/notifications/latest/userguide/ev-managed-rules.html): How to use Amazon EventBridge managed rules in AWS User Notifications.
- [AWS managed policies](https://docs.aws.amazon.com/notifications/latest/userguide/security-iam-awsmanpolicy.html): Learn about AWS managed policies for User Notifications and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/notifications/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with User Notifications and IAM.
- [Compliance validation](https://docs.aws.amazon.com/notifications/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/notifications/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific User Notifications features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/notifications/latest/userguide/infrastructure-security.html): Learn how User Notifications isolates service traffic.


## [Monitoring](https://docs.aws.amazon.com/notifications/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/notifications/latest/userguide/monitoring-cloudwatch.html): You can monitor AWS User Notifications using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [CloudTrail logs](https://docs.aws.amazon.com/notifications/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS User Notifications with AWS CloudTrail.
