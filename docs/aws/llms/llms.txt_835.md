# Source: https://docs.aws.amazon.com/verified-access/latest/ug/llms.txt

# AWS Verified Access User Guide

> AWS Verified Access provides secure access to corporate applications without a VPN connection. It evaluates each request in real time and determines whether the user has access to the application.

- [What is AWS Verified Access?](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)
- [How Verified Access works](https://docs.aws.amazon.com/verified-access/latest/ug/how-it-works.html)
- [Get started tutorial](https://docs.aws.amazon.com/verified-access/latest/ug/getting-started.html)
- [Connectivity Client](https://docs.aws.amazon.com/verified-access/latest/ug/connectivity-client.html)
- [Quotas](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-quotas.html)
- [Document history](https://docs.aws.amazon.com/verified-access/latest/ug/doc-history.html)

## [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)

- [Create and manage a Verified Access instance](https://docs.aws.amazon.com/verified-access/latest/ug/create-verified-access-instance.html): Learn about creating a Verified Access instance, and about attaching or detaching a trust provider.
- [Delete a Verified Access instance](https://docs.aws.amazon.com/verified-access/latest/ug/delete-verified-access-instance.html): Learn how to delete a Verified Access instance when you no longer need it.
- [Integrate with AWS WAF](https://docs.aws.amazon.com/verified-access/latest/ug/waf-integration.html): Learn about integrating Verified Access with AWS WAF to apply perimeter protection.
- [FIPS compliance](https://docs.aws.amazon.com/verified-access/latest/ug/fips-compliance.html): Learn how to enable FIPS compliance with Verified Access.


## [Trust providers](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html)

- [User-identity](https://docs.aws.amazon.com/verified-access/latest/ug/user-trust.html): Learn about user-identify trust providers that you can use for Verified Access.
- [Device-based](https://docs.aws.amazon.com/verified-access/latest/ug/device-trust.html): Learn about device-based trust providers that you can use for Verified Access.


## [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)

- [Create and manage a Verified Access group](https://docs.aws.amazon.com/verified-access/latest/ug/create-verified-access-group.html): Learn how to create a Verified Access group.
- [Modify a Verified Access group policy](https://docs.aws.amazon.com/verified-access/latest/ug/modify-verified-access-group-policy.html): Learn how to modify a Verified Access group policy.
- [Share a group with another account](https://docs.aws.amazon.com/verified-access/latest/ug/sharing-groups.html): When you share a Verified Access group that you own with other AWS accounts, you enable those accounts to create Verified Access endpoints in your group.
- [Delete a Verified Access group](https://docs.aws.amazon.com/verified-access/latest/ug/delete-verified-access-group.html): Learn how to delete a Verified Access group when you no longer need it.


## [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html)

- [Create a load balancer endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/create-load-balancer-endpoint.html): Learn how to create a load balancer endpoint for Verified Access.
- [Create a network interface endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/create-network-interface-endpoint.html): Learn how to create a network interface endpoint for Verified Access.
- [Create a network CIDR endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/create-network-cidr-endpoint.html): Learn how to create a network CIDR endpoint for Verified Access.
- [Create an Amazon Relational Database Service endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/create-rds-endpoint.html): Learn how to create an RDS endpoint for Verified Access.
- [Allow traffic from your endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/configure-endpoint-security-group.html): Learn how to configure security groups to allow traffic that originates from a Verified Access endpoint.
- [Modify a Verified Access endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/modify-endpoint.html): Learn how to modify the configuration of a Verified Access endpoint.
- [Modify a Verified Access endpoint policy](https://docs.aws.amazon.com/verified-access/latest/ug/modify-endpoint-policy.html): Learn how to modify the policy of a Verified Access endpoint.
- [Delete a Verified Access endpoint](https://docs.aws.amazon.com/verified-access/latest/ug/delete-endpoint.html): Learn how to delete a Verified Access endpoint.


## [Verified Access trust data](https://docs.aws.amazon.com/verified-access/latest/ug/trust-data.html)

- [Default context](https://docs.aws.amazon.com/verified-access/latest/ug/trust-data-default-context.html): Learn about the default context used for Verified Access when evaluating a trust provider policy.
- [AWS IAM Identity Center context](https://docs.aws.amazon.com/verified-access/latest/ug/trust-data-iam.html): Learn about the context used to evaluate policies for Verified Access when you define AWS IAM Identity Center as a trust provider.
- [Third-party context](https://docs.aws.amazon.com/verified-access/latest/ug/trust-data-third-party-trust.html): Learn about the context used to evaluate policies for Verified Access when you use a third-party trust provider.
- [User claims passing](https://docs.aws.amazon.com/verified-access/latest/ug/user-claims-passing.html): Learn how identity provider user claims are passed to Verified Access endpoints and verified.


## [Verified Access policies](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies.html)

- [Policy statements](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies-policy-statement-struct.html): Learn about the structure of a Verified Access policy statement.
- [Built-in operators](https://docs.aws.amazon.com/verified-access/latest/ug/built-in-policy-operators.html): Learn how Verified Access policies use built-in operators
- [Policy evaluation](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies-policy-eval.html): Learn how Verified Access policies are evaluated and applied.
- [Policy logic short circuit](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies-policy-eval-short-circ.html): Learn about the logic in how Verified Access policies are evaluates.
- [Example policies](https://docs.aws.amazon.com/verified-access/latest/ug/trust-data-iam-add-pol.html): View example policies for Verified Access.
- [Policy assistant](https://docs.aws.amazon.com/verified-access/latest/ug/policy-assistant.html): The Verified Access policy assistant is a tool in the Verified Access console that you can use to test and develop your polices.


## [Security](https://docs.aws.amazon.com/verified-access/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/verified-access/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Verified Access.

- [Data encryption at rest](https://docs.aws.amazon.com/verified-access/latest/ug/encryption-at-rest.html): Learn how to use customer managed keys in AWS KMS for encrypting data at rest in Verified Access.

### [Identity and access management](https://docs.aws.amazon.com/verified-access/latest/ug/security-iam.html)

Control access to AWS Verified Access resources using IAM.

- [How Verified Access works with IAM](https://docs.aws.amazon.com/verified-access/latest/ug/security_iam_service-with-iam.html): Learn about the IAM features that Verified Access supports.
- [Identity-based policy examples](https://docs.aws.amazon.com/verified-access/latest/ug/security_iam_id-based-policy-examples.html): Learn how to use identity-based policies to grant users and roles access to Verified Access.
- [Troubleshooting](https://docs.aws.amazon.com/verified-access/latest/ug/security_iam_troubleshoot.html): Troubleshoot common issues with IAM in Verified Access.
- [Use service-linked roles](https://docs.aws.amazon.com/verified-access/latest/ug/using-service-linked-roles.html): Learn how to use service-linked roles to grant access to resources in your AWS account for AWS Verified Access.
- [AWS managed policies](https://docs.aws.amazon.com/verified-access/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Verified Access, and about changes to those policies.
- [Compliance validation](https://docs.aws.amazon.com/verified-access/latest/ug/compliance-validation.html): Learn about the security and compliance of Verified Access.
- [Resilience](https://docs.aws.amazon.com/verified-access/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Verified Access features for data resiliency.


## [Monitoring](https://docs.aws.amazon.com/verified-access/latest/ug/monitoring-overview.html)

### [Verified Access logs](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html)

Learn how to monitor your AWS Verified Access instance using access logs.

- [Logging versions](https://docs.aws.amazon.com/verified-access/latest/ug/logging-versions.html): Learn about the logging versions that are used by Verified Access.
- [Logging permissions](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs-permissions.html): Learn about logging permissions used by the IAM principal when configuring Verified Access logging destinations.
- [Enable or disable logs](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs-enable.html): Learn how to enable or disable logging for Verified Access.
- [Enable or disable trust context](https://docs.aws.amazon.com/verified-access/latest/ug/include-trust-context.html): Learn how to enable or disable trust context for Verified Access logging.
- [OCSF version 0.1 log examples](https://docs.aws.amazon.com/verified-access/latest/ug/ocsfv01-examples.html): View sample Verified Access logs using OCSF version 0.1.
- [OCSF version 1.0.0-rc.2 log examples](https://docs.aws.amazon.com/verified-access/latest/ug/ocsfv1-examples.html): View sample Verified Access logs using OCSF version 1.0.0-rc.2.
- [CloudTrail logs](https://docs.aws.amazon.com/verified-access/latest/ug/logging-using-cloudtrail.html): Capture detailed information about the calls made to Verified Access using AWS CloudTrail.
