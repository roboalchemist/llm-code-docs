# Source: https://docs.aws.amazon.com/wickr/latest/adminguide/llms.txt

# AWS Wickr Administration Guide

> This is Amazon Web Services (AWS) administration documentation for AWS Wickr. This Administration Guide describes Wickr concepts, and provides instructions on using the various features with both the console and the command line interface.

- [What is AWS Wickr?](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html)
- [Setting up](https://docs.aws.amazon.com/wickr/latest/adminguide/setting-up.html)
- [Document history](https://docs.aws.amazon.com/wickr/latest/adminguide/doc-history.html)
- [Release notes](https://docs.aws.amazon.com/wickr/latest/adminguide/release-notes.html)

## [Getting started](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started.html)

- [Step 1: Create a network](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started-step1.html): Learn how to create a network.
- [Step 2: Configure your network](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started-step2.html): Complete the following procedure to access the AWS Management Console for Wickr, where you can add users, add security groups, configure SSO, configure data retention, and additional network settings.
- [Step 3: Create and invite users](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started-step3.html): You can create users in your Wickr network using the following methods:


## [Manage network](https://docs.aws.amazon.com/wickr/latest/adminguide/managing-network.html)

### [Network details](https://docs.aws.amazon.com/wickr/latest/adminguide/network-profile.html)

You can edit the name of your Wickr network and view your network ID in the Network details section of the AWS Management Console for Wickr.

- [View network details](https://docs.aws.amazon.com/wickr/latest/adminguide/view-network-profile.html): You can view the details of your Wickr network, including your network name and network ID.
- [Edit network name](https://docs.aws.amazon.com/wickr/latest/adminguide/edit-network-name.html): You can edit the name of your Wickr network.
- [Delete network](https://docs.aws.amazon.com/wickr/latest/adminguide/delete-network.html): You can delete your AWS Wickr network.

### [Security groups](https://docs.aws.amazon.com/wickr/latest/adminguide/security-groups.html)

In the Security Groups section of the AWS Management Console for Wickr, you can manage security groups and their settings, such as password complexity policies, messaging preferences, calling features, security features and network federation.

- [View security groups](https://docs.aws.amazon.com/wickr/latest/adminguide/view-security-groups.html): You can view the details of your Wickr security groups.
- [Create security group](https://docs.aws.amazon.com/wickr/latest/adminguide/create-security-group.html): You can create a new Wickr security group.
- [Edit security group](https://docs.aws.amazon.com/wickr/latest/adminguide/edit-security-group.html): You can edit the details of your Wickr security group.
- [Delete security group](https://docs.aws.amazon.com/wickr/latest/adminguide/delete-security-group.html): You can delete your Wickr security group.

### [SSO configuration](https://docs.aws.amazon.com/wickr/latest/adminguide/sso-configuration.html)

In the AWS Management Console for Wickr, you can configure Wickr to use a single sign-on system to authenticate.

- [View SSO details](https://docs.aws.amazon.com/wickr/latest/adminguide/view-sso-details.html): You can view the details of your single sign-on configuration for your Wickr network and the network endpoint.

### [Configure SSO](https://docs.aws.amazon.com/wickr/latest/adminguide/configure-sso.html)

To ensure secure access to your Wickr network, you can set up your current single sign-on configuration.

- [Configure AWS Wickr with Microsoft Entra SSO](https://docs.aws.amazon.com/wickr/latest/adminguide/entra-ad-sso.html): Learn how to configure Microsoft Entra for your AWS Wickr network.
- [Grace period for token refresh](https://docs.aws.amazon.com/wickr/latest/adminguide/token-refresh.html): Occasionally, there may be instances where identity providers encounter temporary or extended outages, which may lead to your users being logged out unexpectedly due to a failed refresh token for their client session.

### [Network tags](https://docs.aws.amazon.com/wickr/latest/adminguide/network-tags.html)

You can apply tags to Wickr networks.

- [Manage network tags](https://docs.aws.amazon.com/wickr/latest/adminguide/manage-tags.html): You can manage network tags for your Wickr network.
- [Add network tag](https://docs.aws.amazon.com/wickr/latest/adminguide/add-tag.html): You can add a network tag to your Wickr network.
- [Edit network tag](https://docs.aws.amazon.com/wickr/latest/adminguide/edit-tag.html): You can edit a network tag to your Wickr network.
- [Remove network tag](https://docs.aws.amazon.com/wickr/latest/adminguide/remove-tag.html): You can remove a network tag to your Wickr network.
- [Read receipts](https://docs.aws.amazon.com/wickr/latest/adminguide/read-receipts.html): Read receipts for AWS Wickr are notifications sent to the sender to show when their message has been read.
- [Manage network plan](https://docs.aws.amazon.com/wickr/latest/adminguide/manage-plan.html): Learn how to manage a plan based on your business needs.

### [Data retention](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention.html)

AWS Wickr Data retention can retain all conversations in network.

- [View data retention](https://docs.aws.amazon.com/wickr/latest/adminguide/view-data-retention-details.html): Complete the following procedure to view the data retention details for your Wickr network.

### [Configure data retention](https://docs.aws.amazon.com/wickr/latest/adminguide/configure-data-retention.html)

Learn how to configure data retention for your AWS Wickr network.

- [Password](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-password.html): The first time you start the data retention bot, you specify the initial password using one of the following options:
- [Storage options](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-storage-options.html): After data retention is enabled and the data retention bot is configured for your Wickr network, it will capture all messages and files sent within your network.
- [Environment variables](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-bot-env-variables.html): You can use the following environment variables to configure the data retention bot.
- [Secrets Manager values](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-aws-secret-values.html): You can use Secrets Manager to store the data retention bot credentials and AWS service information.
- [IAM policy](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-aws-services.html): If you plan to use other AWS services with the Wickr data retention bot, you must ensure the host has the appropriate AWS Identity and Access Management (IAM) role and policy to access them.

### [Start the bot](https://docs.aws.amazon.com/wickr/latest/adminguide/starting-data-retention-bot.html)

Learn how to start the data retention bot for your Wickr network.

- [Start bot with password environment variable](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-basic-startup.html): The following Docker command starts the data retention bot.
- [Start bot with password prompt](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-startup-password.html): The following Docker command starts the data retention bot.
- [Start bot with 15 minute message file rotation](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-startup-rotation.html): The following Docker command starts the data retention bot using environment variables.
- [Start bot and specify initial password with Secrets Manager](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-startup-asm.html): You can use the Secrets Manager to identify the data retention botâs password.
- [Start bot and configure Amazon S3 with Secrets Manager](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-startup-asm-s3.html): You can use the Secrets Manager to host the credentials, and the Amazon S3 bucket information.
- [Start bot and configure Amazon S3 and AWS KMS with Secrets Manager](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-startup-asm-s3-KMS.html): You can use the Secrets Manager to host the credentials, the Amazon S3 bucket, and AWS KMS master key information.
- [Start bot and configure Amazon S3 using environment variables](https://docs.aws.amazon.com/wickr/latest/adminguide/using-env-variables.html): If you don't want to use Secrets Manager to host the data retention bot credentials, you can start the data retention bot Docker image with the following environment variables.
- [Stop the bot](https://docs.aws.amazon.com/wickr/latest/adminguide/stopping-data-retention-bot.html): Learn how to stop the data retention bot for your Wickr network.
- [Get logs](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-data-retention-logs.html): Learn how to get the logs from the data retention bot for your Wickr network.

### [Data retention metrics and events](https://docs.aws.amazon.com/wickr/latest/adminguide/metrics-events.html)

Learn about the metrics and events that you can get from the data retention bot for your Wickr network.

- [CloudWatch metrics for your Wickr network](https://docs.aws.amazon.com/wickr/latest/adminguide/cloudwatch-metrics.html): Metrics are generated by the bot in 1 minute intervals and transmitted to the CloudWatch service associated with the account the data retention bot Docker image is running on.
- [Amazon SNS events for your Wickr network](https://docs.aws.amazon.com/wickr/latest/adminguide/sns-events.html): The following events are posted to the Amazon SNS topic defined by the Amazon Resource Name (ARN) value identified using the WICKRIO_SNS_TOPIC_ARN environment variable or the sns_topic_arn Secrets Manager secret value.

### [What is ATAK?](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-atak.html)

The Android Team Awareness Kit (ATAK)âor Android Tactical Assault Kit (also ATAK) for military useâis a smart phone geospatial infrastructure and situational awareness application that enables safe collaboration over geography.

- [Install and pair](https://docs.aws.amazon.com/wickr/latest/adminguide/install-and-pair.html): Learn how to install and pair the Wickr plugin for ATAK.
- [Unpair](https://docs.aws.amazon.com/wickr/latest/adminguide/unpair.html): You can unpair the Wickr plugin for ATAK.
- [Dial and receive a call](https://docs.aws.amazon.com/wickr/latest/adminguide/dial-and-receive-call.html): Learn how to dial and receive a call in the Wickr plugin for ATAK.
- [Send a file](https://docs.aws.amazon.com/wickr/latest/adminguide/send-a-file.html): Learn how to send a file in the Wickr plugin for ATAK.
- [Send secure voice message](https://docs.aws.amazon.com/wickr/latest/adminguide/send-secure-voice-message.html): Learn how to send a secure voice message (Push-to-talk) in the Wickr plugin for ATAK.
- [Pinwheel](https://docs.aws.amazon.com/wickr/latest/adminguide/pinwheel.html): Learn how to use the pinwheel in the Wickr plugin for ATAK.
- [Navigation](https://docs.aws.amazon.com/wickr/latest/adminguide/navigation.html): Learn the basic navigation of the Wickr plugin for ATAK.
- [Ports and domains to allow list](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html): Learn the ports you should open and the domains to allow list on your network for AWS Wickr to function correctly.
- [GovCloud](https://docs.aws.amazon.com/wickr/latest/adminguide/govcloud-cross-boundary.html): AWS Wickr offers WickrGov client tailored for GovCloud users.
- [File preview](https://docs.aws.amazon.com/wickr/latest/adminguide/file-preview.html): Organizations using the Wickr Premium tier (including Premium free trial), can now manage file download permissions at the security group level.


## [Manage users](https://docs.aws.amazon.com/wickr/latest/adminguide/managing-users.html)

### [Team directory](https://docs.aws.amazon.com/wickr/latest/adminguide/team-directory.html)

You can view current Wickr users and modify their details in the User management section of the AWS Management Console for Wickr.

- [View users](https://docs.aws.amazon.com/wickr/latest/adminguide/view-users.html): You can view the details of users registered to your Wickr network.
- [Invite user](https://docs.aws.amazon.com/wickr/latest/adminguide/invite-user.html): You can invite a user in your Wickr network.
- [Edit users](https://docs.aws.amazon.com/wickr/latest/adminguide/edit-users.html): You can edit users in your Wickr network.
- [Delete user](https://docs.aws.amazon.com/wickr/latest/adminguide/delete-user.html): You can delete a user in your Wickr network.
- [Bulk delete users](https://docs.aws.amazon.com/wickr/latest/adminguide/bulk-delete.html): You can bulk delete Wickr network users in the User management section in the AWS Management Console for Wickr.
- [Bulk suspend users](https://docs.aws.amazon.com/wickr/latest/adminguide/bulk-suspend.html): You can bulk suspend Wickr network users in the User management section in the AWS Management Console for Wickr.

### [Guest users](https://docs.aws.amazon.com/wickr/latest/adminguide/guest-users.html)

Learn how to how to enable guest users for your AWS Wickr network.

- [Enable or disable guest users](https://docs.aws.amazon.com/wickr/latest/adminguide/guest-users-enable-disable.html): You can enable or disable guest users in your Wickr network.
- [View guest user count](https://docs.aws.amazon.com/wickr/latest/adminguide/view-guest-users.html): You can view the guest user count in your Wickr network.
- [View monthly usage](https://docs.aws.amazon.com/wickr/latest/adminguide/guest-user-monthly-usage.html): You can view the number of guest users your network has communicated with during a billing period.
- [View guest users](https://docs.aws.amazon.com/wickr/latest/adminguide/guest-user-communicate.html): You can view the guest users a network user has communicated with during a specific billing period.
- [Block guest user](https://docs.aws.amazon.com/wickr/latest/adminguide/guest-user-block-user.html): You can block and unblock a guest user in your Wickr network.


## [Security](https://docs.aws.amazon.com/wickr/latest/adminguide/security.html)

- [Data protection](https://docs.aws.amazon.com/wickr/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Wickr.

### [Identity and access management](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)

How to authenticate requests and manage access your Wickr resources.

- [Audience](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_audience.html): How you use AWS Identity and Access Management (IAM) differs based on your role:

### [Authenticating with identities](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_authentication.html)

Authentication is how you sign in to AWS using your identity credentials.

- [AWS account root user](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_authentication-rootuser.html): When you create an AWS account, you begin with one sign-in identity called the AWS account root user that has complete access to all AWS services and resources.
- [Federated identity](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_authentication-federated.html): As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.
- [IAM users and groups](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_authentication-iamuser.html): An IAM user is an identity with specific permissions for a single person or application.
- [IAM roles](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_authentication-iamrole.html): An IAM role is an identity with specific permissions that provides temporary credentials.

### [Managing access using policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage.html)

You control access in AWS by creating policies and attaching them to AWS identities or resources.

- [Identity-based policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage-id-based-policies.html): Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role).
- [Resource-based policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage-resource-based-policies.html): Resource-based policies are JSON policy documents that you attach to a resource.
- [Access control lists (ACLs)](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage-acl.html): Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource.
- [Other policy types](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage-other-policies.html): AWS supports additional, less-common policy types.
- [Multiple policy types](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_access-manage-multiple-policies.html): When multiple types of policies apply to a request, the resulting permissions are more complicated to understand.
- [AWS Wickr managed policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Wickr and recent changes to those policies.

### [How AWS Wickr works with IAM](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam.html)

Before you use IAM to manage access to Wickr, learn what IAM features are available to use with Wickr.

- [Identity-based policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-id-based-policies.html): Supports identity-based policies: Yes
- [Resource-based policies](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-resource-based-policies.html): Supports resource-based policies: No
- [Policy actions](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-id-based-policies-actions.html): Supports policy actions: Yes
- [Policy resources](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-id-based-policies-resources.html): Supports policy resources: No
- [Policy condition keys](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-id-based-policies-conditionkeys.html): Supports service-specific policy condition keys: No
- [ACLs](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-acls.html): Supports ACLs: No
- [ABAC](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-tags.html): Supports ABAC (tags in policies): No
- [Principal permissions](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-principal-permissions.html): Supports forward access sessions (FAS): No
- [Service roles](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-roles-service.html): Supports service roles: No
- [Service-linked roles](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-roles-service-linked.html): Supports service-linked roles: No

### [Identity-based policy examples](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_id-based-policy-examples.html)

By default, a brand new IAM user has no permissions to do anything.

- [Policy best practices](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_service-with-iam-policy-best-practices.html): Identity-based policies determine whether someone can create, access, or delete Wickr resources in your account.
- [Using the console](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_id-based-policy-examples-console.html): Attach the AWSWickrFullAccess AWS managed policy to your IAM identities to grant them full administrative permission to the Wickr service, including the Wickr administrator console in the AWS Management Console.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_id-based-policy-examples-view-own-permissions.html): This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.
- [Troubleshooting](https://docs.aws.amazon.com/wickr/latest/adminguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Wickr and IAM.
- [Compliance validation](https://docs.aws.amazon.com/wickr/latest/adminguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/wickr/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Wickr features for data resiliency.

### [AWS PrivateLink](https://docs.aws.amazon.com/wickr/latest/adminguide/privatelink-overview.html)

Learn about AWS PrivateLink to create a private connection between your VPC and AWS Wickr.

- [Create VPC endpoints](https://docs.aws.amazon.com/wickr/latest/adminguide/vpc-endpoints.html): Learn how to create VPC endpoints.
- [Limitations](https://docs.aws.amazon.com/wickr/latest/adminguide/privatelink-limitations.html): The following features are not supported through AWS PrivateLink and require internet connectivity:
- [Infrastructure Security](https://docs.aws.amazon.com/wickr/latest/adminguide/infrastructure-security.html): Learn how AWS Wickr isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/wickr/latest/adminguide/vulnerability-analysis-and-management.html): Learn how Wickr handles configuration and vulnerability analysis.
- [Security best practices](https://docs.aws.amazon.com/wickr/latest/adminguide/security-best-practices.html): Security best practices for AWS Wickr.


## [Monitoring](https://docs.aws.amazon.com/wickr/latest/adminguide/monitoring-overview.html)

### [CloudTrail logs](https://docs.aws.amazon.com/wickr/latest/adminguide/logging-using-cloudtrail.html)

Learn about logging AWS Wickr with AWS CloudTrail.

- [Wickr information in CloudTrail](https://docs.aws.amazon.com/wickr/latest/adminguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Understanding Wickr log file entries](https://docs.aws.amazon.com/wickr/latest/adminguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.
- [Analytics dashboard](https://docs.aws.amazon.com/wickr/latest/adminguide/dashboard.html): Learn about the admin analytics dashboard.
