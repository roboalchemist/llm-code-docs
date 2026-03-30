# Source: https://docs.aws.amazon.com/outposts/latest/userguide/llms.txt

# AWS Outposts User guide for first-generation Outposts racks

> AWS Outposts is a fully-managed service that extends AWS infrastructure, APIs, and tools to customer premises. By providing local access to AWS-managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.

- [What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)
- [How AWS Outposts works](https://docs.aws.amazon.com/outposts/latest/userguide/how-outposts-works.html)
- [Requirements for Outposts racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html)
- [Requirements for ACE racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-ace-requirements.html)
- [Local network connectivity](https://docs.aws.amazon.com/outposts/latest/userguide/local-rack.html)
- [Shared resources](https://docs.aws.amazon.com/outposts/latest/userguide/sharing-outposts.html)
- [Third-party block storage](https://docs.aws.amazon.com/outposts/latest/userguide/outpost-third-party-block-storage.html)
- [Maintenance](https://docs.aws.amazon.com/outposts/latest/userguide/outpost-maintenance.html)
- [End-of-term options](https://docs.aws.amazon.com/outposts/latest/userguide/term-end-racks.html)
- [Quotas](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-limits.html)
- [Document history](https://docs.aws.amazon.com/outposts/latest/userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/outposts/latest/userguide/get-started-outposts.html)

- [Place an order](https://docs.aws.amazon.com/outposts/latest/userguide/order-outpost-capacity.html): Complete the required steps to order an Outposts rack, such as creating a site, creating an Outpost, and placing the order.
- [Launch an instance](https://docs.aws.amazon.com/outposts/latest/userguide/launch-instance.html): Launch an Amazon EC2 instance on your Outposts rack.
- [Optimization](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-optimizations.html): Describes how to optimize Amazon EC2 capacity in AWS Outposts.


## [Service link](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html)

- [Connectivity](https://docs.aws.amazon.com/outposts/latest/userguide/service-links.html): The service link is a necessary connection between your Outposts and the AWS Region (or home Region).
- [Public connectivity options](https://docs.aws.amazon.com/outposts/latest/userguide/sl-public-connectivity.html): You can configure the service link with a public connection for the traffic between the Outposts and home AWS Region.
- [Private connectivity options](https://docs.aws.amazon.com/outposts/latest/userguide/private-connectivity.html): You can configure the service link with a private connection for the traffic between the Outposts and home AWS Region.
- [Firewalls and the service link](https://docs.aws.amazon.com/outposts/latest/userguide/firewalls-sl.html): This section discusses firewall configurations and the service link connection.
- [Network troubleshooting](https://docs.aws.amazon.com/outposts/latest/userguide/network-troubleshoot.html): Use this checklist to help troubleshoot a service link that has a status of DOWN.


## [Local gateways](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html)

- [Route tables](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html): Understand the key concepts for local gateway route tables.
- [Route table routes](https://docs.aws.amazon.com/outposts/latest/userguide/manage-lgw-routes.html): You can create local gateway route tables and inbound routes to network interfaces on your Outpost.
- [CoIP pools](https://docs.aws.amazon.com/outposts/latest/userguide/coip-pools.html): You can provide IP address ranges to facilitate communication between your on-premises network and instances in your VPC.


## [Capacity management](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-capacity.html)

- [View capacity](https://docs.aws.amazon.com/outposts/latest/userguide/view-capacity-management.html): You can view the capacity configuration at the instance or Outpost level.
- [Modify instance capacity](https://docs.aws.amazon.com/outposts/latest/userguide/modify-instance-capacity.html): The capacity of each new Outpost order is configured with a default capacity configuration.
- [Troubleshooting capacity task issues](https://docs.aws.amazon.com/outposts/latest/userguide/order-troubleshooting.html): Review the following known issues to resolve an issue related to capacity management in a new order.


## [Security](https://docs.aws.amazon.com/outposts/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Outposts.

### [Identity and access management](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

- [How AWS Outposts works with IAM](https://docs.aws.amazon.com/outposts/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Outposts, learn what IAM features are available to use with AWS Outposts.
- [Policy examples](https://docs.aws.amazon.com/outposts/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Outposts resources.
- [Service-linked roles](https://docs.aws.amazon.com/outposts/latest/userguide/using-service-linked-roles.html): Understand how service-linked roles give AWS Outposts access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/outposts/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Outposts and recent changes to those policies.
- [Infrastructure security](https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html): Learn how AWS Outposts isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html): AWS Outposts contains features that support data resiliency, and AWS architecture supports data redundancy.
- [Compliance validation](https://docs.aws.amazon.com/outposts/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Internet access](https://docs.aws.amazon.com/outposts/latest/userguide/internet-access.html): Learn how AWS Outposts workloads can access the internet.


## [Monitoring](https://docs.aws.amazon.com/outposts/latest/userguide/monitor-outposts.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html): Monitor your Outposts rack using metrics gathered by Amazon CloudWatch.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/outposts/latest/userguide/logging-using-cloudtrail.html): Log AWS Outposts API calls by using AWS CloudTrail.
