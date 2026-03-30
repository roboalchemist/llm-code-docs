# Source: https://docs.aws.amazon.com/outposts/latest/server-userguide/llms.txt

# AWS Outposts User Guide for Outposts servers

> AWS Outposts is a fully-managed service that extends AWS infrastructure, APIs, and tools to customer premises. By providing local access to AWS-managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.

- [What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/server-userguide/what-is-outposts.html)
- [How AWS Outposts works](https://docs.aws.amazon.com/outposts/latest/server-userguide/how-outposts-works.html)
- [Site requirements](https://docs.aws.amazon.com/outposts/latest/server-userguide/outposts-requirements.html)
- [Return a server](https://docs.aws.amazon.com/outposts/latest/server-userguide/shipping-outposts-server.html)
- [Shared resources](https://docs.aws.amazon.com/outposts/latest/server-userguide/sharing-outposts.html)
- [Third-party block storage](https://docs.aws.amazon.com/outposts/latest/server-userguide/outpost-third-party-block-storage.html)
- [Maintenance](https://docs.aws.amazon.com/outposts/latest/server-userguide/outpost-maintenance.html)
- [End-of-term options](https://docs.aws.amazon.com/outposts/latest/server-userguide/term-end-server.html)
- [Quotas](https://docs.aws.amazon.com/outposts/latest/server-userguide/outposts-limits.html)
- [Document history](https://docs.aws.amazon.com/outposts/latest/server-userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/outposts/latest/server-userguide/get-started-outposts.html)

- [Create an Outpost and order capacity](https://docs.aws.amazon.com/outposts/latest/server-userguide/order-outpost-capacity.html): Create an AWS Outposts and order capacity.
- [Launch an instance](https://docs.aws.amazon.com/outposts/latest/server-userguide/launch-instance.html): Launch an instance on AWS Outposts.


## [Service link](https://docs.aws.amazon.com/outposts/latest/server-userguide/region-connectivity.html)

- [Connectivity](https://docs.aws.amazon.com/outposts/latest/server-userguide/service-links.html): During AWS Outposts provisioning, you or AWS creates a service link connection that connects your Outposts server to your chosen AWS Region or home Region.
- [Updates and the service link](https://docs.aws.amazon.com/outposts/latest/server-userguide/updates-service-link.html): AWS maintains a secure network connection between your Outposts server and its parent AWS Region.
- [Firewalls and the service link](https://docs.aws.amazon.com/outposts/latest/server-userguide/firewalls-sl.html): This section discusses firewall configurations and the service link connection.
- [Network troubleshooting](https://docs.aws.amazon.com/outposts/latest/server-userguide/network-troubleshoot.html): Use this checklist to help troubleshoot a service link that has a status of DOWN.


## [Local network interfaces](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html)

- [Add a local network interface](https://docs.aws.amazon.com/outposts/latest/server-userguide/add-lni.html): You can add a local network interface to an Amazon EC2 instance on an Outposts subnet during or after launch.
- [Local connectivity](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-server.html): Use this topic to understand the network cabling and topology requirements for hosting an Outposts server.


## [Capacity management](https://docs.aws.amazon.com/outposts/latest/server-userguide/outposts-capacity.html)

- [View capacity](https://docs.aws.amazon.com/outposts/latest/server-userguide/view-capacity-management.html): You can view the capacity configuration at the instance or Outpost level.
- [Modify instance capacity](https://docs.aws.amazon.com/outposts/latest/server-userguide/modify-instance-capacity.html): The capacity of each new Outpost order is configured with a default capacity configuration.
- [Troubleshooting capacity task issues](https://docs.aws.amazon.com/outposts/latest/server-userguide/order-troubleshooting.html): Review the following known issues to resolve an issue related to capacity management in a new order.


## [Security](https://docs.aws.amazon.com/outposts/latest/server-userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/outposts/latest/server-userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Outposts.

### [Identity and access management](https://docs.aws.amazon.com/outposts/latest/server-userguide/identity-access-management.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

- [How AWS Outposts works with IAM](https://docs.aws.amazon.com/outposts/latest/server-userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Outposts, learn what IAM features are available to use with AWS Outposts.
- [Policy examples](https://docs.aws.amazon.com/outposts/latest/server-userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Outposts resources.
- [Service-linked roles](https://docs.aws.amazon.com/outposts/latest/server-userguide/using-service-linked-roles.html): Understand how service-linked roles give AWS Outposts access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/outposts/latest/server-userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Outposts and recent changes to those policies.
- [Infrastructure security](https://docs.aws.amazon.com/outposts/latest/server-userguide/infrastructure-security.html): Learn how AWS Outposts isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/outposts/latest/server-userguide/disaster-recovery-resiliency.html): AWS Outposts contains features that support data resiliency, and AWS architecture supports data redundancy.
- [Compliance validation](https://docs.aws.amazon.com/outposts/latest/server-userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.


## [Monitoring](https://docs.aws.amazon.com/outposts/latest/server-userguide/monitor-outposts.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/outposts/latest/server-userguide/outposts-cloudwatch-metrics.html): Monitor your Outposts server using metrics gathered by Amazon CloudWatch.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/outposts/latest/server-userguide/logging-using-cloudtrail.html): Log AWS Outposts API calls by using AWS CloudTrail.
