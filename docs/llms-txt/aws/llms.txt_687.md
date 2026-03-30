# Source: https://docs.aws.amazon.com/ram/latest/userguide/llms.txt

# AWS Resource Access Manager User Guide

> Learn the key concepts of AWS RAM and how to use the features of AWS RAM.

- [What is AWS RAM?](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
- [Shareable resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html)
- [Service quotas](https://docs.aws.amazon.com/ram/latest/userguide/service-quotas.html)
- [Using the AWS SDKs](https://docs.aws.amazon.com/ram/latest/userguide/sdk-general-info.html)
- [Document history](https://docs.aws.amazon.com/ram/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/ram/latest/userguide/getting-started.html)

- [Terms and concepts](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-terms-and-concepts.html): Get started with AWS RAM.
- [Sharing your resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html): Learn how to use AWS Resource Access Manager to share a resource with other AWS accounts.
- [Using shared resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html): Learn how to access a resource that was shared with your account using AWS Resource Access Manager.


## [Working with shared resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with.html)

- [Regional and global resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-regional-vs-global.html): Learn how AWS Resource Access Manager handles resources in AWS Regions compared to global resources.

### [Resources owned by you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html)

Manage resource shares that you have created.

- [Viewing resource shares you created](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-rs.html): Learn how to view resource shares and resources that you have shared with others.
- [Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html): To share resources that you own, create a resource share.
- [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html): Learn how to make changes to resource shares that you have shared with others.
- [Viewing your shared resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-sr.html): Learn how to view resources that you've shared with others.
- [Viewing principals you share with](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-principals.html): Learn how to view the principals with whom you've shared your resources.
- [Deleting a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.html): Learn how to delete a resource share in AWS RAM.

### [Resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html)

Learn how to manage resource shares that have been shared with you.

- [Accepting and rejecting invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html): Learn how to accept or reject an invitation to use a resource share.
- [Viewing resource shares shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-rs.html): Learn how to view the resource shares to which you have access.
- [Viewing resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-sr.html): Learn how to view AWS resources that have been shared with you from other AWS accounts.
- [View principals sharing with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-view-principals.html): Learn how to view the principals that are sharing AWS resources with you.
- [Leaving a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-leave.html): Learn how to leave a resource share that has AWS resources that you no longer need to access.
- [Availability Zone IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html): Learn how AWS uses availability zones and AZ IDs.


## [Managing permissions in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security-ram-permissions.html)

- [Viewing managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-view-permissions.html): Learn how to view the available managed permissions for a resource type.
- [Creating and using customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html): Learn how to create and use a customer managed permission for a resource type in AWS RAM.
- [Updating managed permission versions](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update-permissions.html): Learn how to update the version of the managed permission for a resource type.
- [Customer managed permission considerations](https://docs.aws.amazon.com/ram/latest/userguide/managed-permission-considerations.html): Learn about the unsupported conditions in customer managed permissions in AWS RAM.


## [Security](https://docs.aws.amazon.com/ram/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/ram/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS RAM.

### [Identity and access management](https://docs.aws.amazon.com/ram/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS RAM resources.

- [How AWS RAM works with IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html): By default, IAM principals don't have permission to create or modify AWS RAM resources.
- [AWS managed policies](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS RAM and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/ram/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS RAM access to resources in your AWS account.
- [Example IAM policies](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies-examples.html): This topic includes examples of IAM policies for AWS RAM that demonstrate sharing specific resources and resource types and restricting sharing.
- [Example SCPs](https://docs.aws.amazon.com/ram/latest/userguide/security-scp.html): AWS RAM supports service control policies (SCPs).
- [Disable sharing with Organizations](https://docs.aws.amazon.com/ram/latest/userguide/security-disable-sharing-with-orgs.html): Learn how to disable sharing with AWS Organizations.

### [Logging and monitoring](https://docs.aws.amazon.com/ram/latest/userguide/security-monitoring.html)

Monitor AWS RAM to maintain reliability, availability, and performance.

- [Monitoring using EventBridge](https://docs.aws.amazon.com/ram/latest/userguide/using-eventbridge.html): How to monitor AWS RAM using EventBridge.
- [Logging AWS RAM API calls with AWS CloudTrail](https://docs.aws.amazon.com/ram/latest/userguide/cloudtrail-logging.html): Learn about logging AWS RAM with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/ram/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/ram/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS RAM features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/ram/latest/userguide/infrastructure-security.html): Learn how AWS Resource Access Manager isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/ram/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Resource Access Manager.


## [Troubleshooting](https://docs.aws.amazon.com/ram/latest/userguide/troubleshooting.html)

- [Error: Account ID doesn't exist](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-no-slr.html)
- [Error: Access Denied Exception](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-access-denied.html)
- [Error: Unknown Resource Exception](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-unknown-resource.html)
- [Error: Sharing outside an organization not permitted](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-sharing-outside-org.html)
- [Error: Can't see shared resources](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-cant-see-shared.html)
- [Error: Limit Exceeded Exception](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-limits-exceeded.html)
- [No invitations received](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-shared-org-no-invite.html)
- [Can't share a VPC](https://docs.aws.amazon.com/ram/latest/userguide/tshoot-subnet-limits.html)
