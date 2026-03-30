# Source: https://docs.aws.amazon.com/rtb-fabric/latest/userguide/llms.txt

# AWS RTB Fabric User Guide

> Provides a conceptual overview of RTB Fabric and offers step-by-step instructions for how to use it.

- [What is AWS RTB Fabric?](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/what-is-rtb-fabric.html)
- [Setting up AWS RTB Fabric](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/setting-up-aws-rtb-service.html)
- [Links](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/links.html)
- [Modules](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html)
- [Quotas](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/rtb-fabric-quotas.html)
- [Glossary](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/glossary.html)
- [Document history](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/doc-history.html)

## [RTB Fabric gateways](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/gateways.html)

- [Requester gateways](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-requester-gateways.html): Learn how to understand, create, and manage requester real-time bidding (RTB) applications in AWS RTB Fabric.
- [Responder gateways](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html): Learn how to create and configure responder real-time bidding (RTB) applications that receive and process bid requests from requester applications.
- [Managed endpoints](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/managed-endpoints.html): Managed endpoints is an optional feature for responder gateways that allows RTB Fabric to distribute load directly across bidder hosts in your fleet.


## [Security](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security-iam.html)

How to authenticate requests and manage access your RTB Fabric resources.

- [How RTB Fabric works with IAM](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to RTB Fabric, learn what IAM features are available to use with RTB Fabric.
- [Identity-based policy examples](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify RTB Fabric resources.
- [AWS managed policies](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for RTB Fabric and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with RTB Fabric and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give RTB Fabric access to resources in your AWS account.
- [Data protection](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in RTB FabricSERVICEfirst;.
- [Incident response](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/incident-response.html): Learn about incident response procedures for RTB Fabric.
- [Compliance validation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/compliance-validation.html): Learn whether RTB Fabric is in scope for specific compliance programs.


## [Monitoring RTB Fabric](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch.html)

You can monitor RTB Fabric using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

- [CloudWatch Logs configuration](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-logs.html): You can configure RTB Fabric to send application logs to Amazon CloudWatch Logs using log delivery.
- [RTB Fabric metrics](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-metrics.html): RTB Fabric publishes the following metrics to CloudWatch.
- [RTB Fabric dimensions](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-dimensions.html): The following dimensions are supported for RTB Fabric metrics.
- [Creating alarms](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-alarms.html): You can create CloudWatch alarms to monitor RTB Fabric metrics and automatically notify you when metric values cross specified thresholds.
- [Creating dashboards](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-dashboards.html): You can create CloudWatch dashboards to visualize RTB Fabric metrics and monitor the health and performance of your RTB gateways and links in real time.
- [CloudTrail logs](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS RTB Fabric with AWS CloudTrail.
