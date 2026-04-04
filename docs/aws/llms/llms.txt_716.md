# Source: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/llms.txt

# IAM Roles Anywhere User Guide

> Provides conceptual overviews of IAM Roles Anywhere and explains how to use it.

- [What is IAM Roles Anywhere?](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
- [Public key infrastructure](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/public-key-infrastructure.html)
- [Getting started](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html)
- [Get temporary security credentials](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/creating-resources-with-cloudformation.html)
- [Quotas](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/doc-history.html)

## [IAM Roles Anywhere trust model](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html)

### [Certificate attribute mapping](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/attribute-mapping.html)

With IAM Roles Anywhere you can define a custom set of mapping rules, and specify the data extracted from authenticating certificates as session tags.

- [Put attribute mappings](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/put-attribute-mapping.html): Put attribute mappings enable you to attach new mapping rules to your profile.
- [Delete attribute mappings](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/delete-attribute-mappings.html): Delete attribute mappings enable you to delete mapping rules from your profile.
- [Attribute mapping and trust policy](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/attribute-mapping-and-trust-policy.html): The attribute mapping field of a profile controls which attributes from an authenticating X.509 certificate will be mapped for principal tags.


## [IAM Roles Anywhere authentication](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication.html)

- [CreateSession API](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html): CreateSession API returns temporary security credentials for workloads that have been authenticated with IAM Roles Anywhere to access AWS resources.
- [Signing process](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-sign-process.html): The signing process is identical to SigV4, with the exception of the keys used, the signature algorithm, and the addition of headers related to the X.509 certificate and trust chain.


## [Security](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security.html)

- [Workload identities](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/workload-identities.html): Learn how workloads access AWS from your data centers can use temporary credentials served from IAM Roles Anywhere.
- [Data protection](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in IAM Roles Anywhere.

### [Identity and access management](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security-iam.html)

How to authenticate requests and manage access your IAM Roles Anywhere resources.

- [How IAM Roles Anywhere works with IAM](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security_iam_service-with-iam.html): To manage access to IAM Roles Anywhere, learn what IAM features are available to use with IAM Roles Anywhere.
- [Identity-based policy examples](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security_iam_id-based-policy-examples.html): Users and roles don't have permission to create or modify IAM Roles Anywhere resources.
- [Troubleshooting](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with IAM Roles Anywhere and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to grant IAM Roles Anywhere access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for IAM Roles Anywhere and recent changes to those policies.
- [Resilience](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific IAM Roles Anywhere features for data resiliency.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS Identity and Access Management Roles Anywhere without requiring access over the internet or through a NAT device, a VPN connection, or an AWS Direct Connect connection.
- [IPv4 and IPv6 access](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/ip-access.html): Control API access with IAM policies.


## [Monitoring](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/monitoring-overview.html)

### [Customize notification settings](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/customize-notification-settings.html)

To define custom thresholds for a notification event, customize notification settings attached to your trust anchor based on your public key infrastructure.

- [Configuring custom notification threshold (console)](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/how-to-configure-custom-notification-settings.html): Use the following procedure to configure custom notification thresholds for IAM Roles Anywhere through the AWS Console Home.
- [Disabling a notification setting (console)](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/how-to-disable-notification-for-end-entity-certificate-expiry.html): Use the following procedure to learn how to disable a notification setting for IAM Roles Anywhere through the AWS Console Home.
- [Monitoring with CloudWatch](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/monitoring-cloudwatch.html): Monitor AWS Identity and Access Management Roles Anywhere using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Monitoring events with Amazon EventBridge](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/monitoring-events.html): You can monitor and write simple rules for IAM Roles Anywhere events in Amazon EventBridge.
- [Monitoring IAM Roles Anywhere notifications](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/monitoring-health.html): You can monitor IAM Roles Anywhere health notifications in AWS Health.
- [CloudTrail logs](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Identity and Access Management Roles Anywhere with AWS CloudTrail.
- [Monitoring with IAM Roles Anywhere subjects](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/monitoring-subjects.html): Use the Subject Activity tab in the IAM Roles Anywhere console to visualize and audit activities for certificates authenticated with IAM Roles Anywhere.
