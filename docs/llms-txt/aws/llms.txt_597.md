# Source: https://docs.aws.amazon.com/mpa/latest/userguide/llms.txt

# Multi-party approval User Guide

> Learn about Multi-party approval, which allows you to protect a predefined list of operations through a distributed approval process.

- [How it works](https://docs.aws.amazon.com/mpa/latest/userguide/how-it-works.html)
- [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/team-health.html)
- [Troubleshooting](https://docs.aws.amazon.com/mpa/latest/userguide/troubleshooting.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/mpa/latest/userguide/creating-resources-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/mpa/latest/userguide/doc-history.html)

## [What is Multi-party approval?](https://docs.aws.amazon.com/mpa/latest/userguide/what-is.html)

- [Terms and concepts](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html): Learn about key terms and concepts for Multi-party approval.
- [Region support](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-region-support.html): To use Multi-party approval, you must create approval teams and the identity source in the US East (N.
- [Quotas](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-limits.html): Learn about the quotas for Multi-party approval.


## [Administrator tasks](https://docs.aws.amazon.com/mpa/latest/userguide/administrator.html)

- [Set up Multi-party approval](https://docs.aws.amazon.com/mpa/latest/userguide/setting-up.html): Learn about how to set up Multi-party approval
- [Create team](https://docs.aws.amazon.com/mpa/latest/userguide/create-team.html): Learn about creating an approval team for Multi-party approval.
- [View team](https://docs.aws.amazon.com/mpa/latest/userguide/admin-view-team.html): Learn about viewing an approval team for Multi-party approval as an administrator.
- [Update team](https://docs.aws.amazon.com/mpa/latest/userguide/update-team.html): Learn about updating an approval team for Multi-party approval as an administrator.
- [Baseline team](https://docs.aws.amazon.com/mpa/latest/userguide/baseline-team.html): Learn about baselining an approval team for Multi-party approval as an administrator.
- [Share team](https://docs.aws.amazon.com/mpa/latest/userguide/share-team.html): Learn about sharing an approval team for Multi-party approval.
- [Delete team](https://docs.aws.amazon.com/mpa/latest/userguide/delete-team.html): Learn about deleting an approval team for Multi-party approval.
- [Cancel session](https://docs.aws.amazon.com/mpa/latest/userguide/cancel-session.html): Learn about canceling an approval session for Multi-party approval.
- [Disable Multi-party approval](https://docs.aws.amazon.com/mpa/latest/userguide/delete-identity-source.html): Learn about disabling Multi-party approval by deleting its identity source.


## [Approver tasks](https://docs.aws.amazon.com/mpa/latest/userguide/approver.html)

- [Respond to requested operations](https://docs.aws.amazon.com/mpa/latest/userguide/respond-request.html): Learn about responding to requested operations with Multi-party approval.
- [View an approval team](https://docs.aws.amazon.com/mpa/latest/userguide/approver-view-team.html): Learn about viewing an approval team with Multi-party approval as an approver.
- [View operation history](https://docs.aws.amazon.com/mpa/latest/userguide/view-operation-history.html): Learn about viewing operation history with Multi-party approval.


## [Monitoring](https://docs.aws.amazon.com/mpa/latest/userguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/mpa/latest/userguide/logging-using-cloudtrail.html): Learn about logging Multi-party approval with AWS CloudTrail.
- [Monitoring with CloudWatch](https://docs.aws.amazon.com/mpa/latest/userguide/monitoring-cloudwatch.html): You can monitor Multi-party approval using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Portal APIs](https://docs.aws.amazon.com/mpa/latest/userguide/web-api.html): Learn about the supported Multi-party approval portal APIs.


## [Security](https://docs.aws.amazon.com/mpa/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/mpa/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Multi-party approval.

### [Identity and access management](https://docs.aws.amazon.com/mpa/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Multi-party approval resources.

- [How Multi-party approval works with IAM](https://docs.aws.amazon.com/mpa/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Multi-party approval, learn what IAM features are available to use with Multi-party approval.
- [Identity-based policy examples](https://docs.aws.amazon.com/mpa/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Multi-party approval resources.
- [AWS managed policies](https://docs.aws.amazon.com/mpa/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Multi-party approval and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/mpa/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Multi-party approval and IAM.
- [AWS PrivateLink](https://docs.aws.amazon.com/mpa/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and Multi-party approval.
- [Compliance validation](https://docs.aws.amazon.com/mpa/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mpa/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Multi-party approval features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/mpa/latest/userguide/infrastructure-security.html): Learn how Multi-party approval isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/mpa/latest/userguide/vulnerability-analysis-and-management.html): Learn how Multi-party approval performs vulnerability and compliance scanning.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mpa/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
