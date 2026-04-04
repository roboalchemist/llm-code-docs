# Source: https://docs.aws.amazon.com/inspector/v1/userguide/llms.txt

# Amazon Inspector Classic User Guide

> Use Amazon Inspector Classic to analyze the behavior of your AWS resources and identify potential security issues.

- [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html)
- [Getting started](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_getting-started.html)
- [Amazon Inspector Classic assessment targets](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_applications.html)
- [Amazon Inspector Classic assessment templates and assessment runs](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_assessments.html)
- [Amazon Inspector Classic findings](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_findings.html)
- [Assessment reports](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_reports.html)
- [Exclusions in Amazon Inspector Classic](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_exclusions.html)
- [Amazon Inspector Classic rules packages for supported operating systems](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_rule-packages_across_os.html)
- [Logging Amazon Inspector Classic API calls with AWS CloudTrail](https://docs.aws.amazon.com/inspector/v1/userguide/logging-using-cloudtrail.html)
- [Monitoring Amazon Inspector Classic using Amazon CloudWatch](https://docs.aws.amazon.com/inspector/v1/userguide/using-cloudwatch.html)
- [Configuring Amazon Inspector Classic using AWS CloudFormation](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cloudformation-integration.html)
- [Security Hub CSPM integration](https://docs.aws.amazon.com/inspector/v1/userguide/securityhub-integration.html)
- [Document history](https://docs.aws.amazon.com/inspector/v1/userguide/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/inspector/v1/userguide/glossary.html)

## [What is Amazon Inspector Classic?](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_introduction.html)

- [Terminology and concepts](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_concepts.html): Learn the terms and concepts of Amazon Inspector Classic.
- [Service limits](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_limits.html): Learn about the Amazon Inspector Classic limits.
- [Pricing](https://docs.aws.amazon.com/inspector/v1/userguide/InspectorPricing.html): Amazon Inspector Classic pricing is based on the number of EC2 instances included in each assessment and the rules packages used in those assessments.
- [Supported operating systems and Regions](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_supported_os_regions.html): Learn about the operating systems and AWS Regions that Amazon Inspector Classic supports.


## [Tutorials](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_tutorials.html)

- [Amazon Inspector Classic tutorial - Red Hat Enterprise Linux](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_walkthrough.html): Follow the steps in this tutorial to use Amazon Inspector Classic to analyze the behavior of an EC2 instance that runs the Red Hat Enterprise Linux 7.5 operating system.
- [Amazon Inspector Classic tutorial - Ubuntu Server](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_walkthrough_ubuntu.html): Follow these steps in this tutorial to use Amazon Inspector Classic to analyze the behavior of an EC2 instance that runs the Ubuntu Server 16.04 LTS operating system.


## [Security](https://docs.aws.amazon.com/inspector/v1/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/inspector/v1/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Inspector Classic.

- [Encryption at rest](https://docs.aws.amazon.com/inspector/v1/userguide/encryption-at-rest.html): Learn about encryption of data at rest for Amazon Inspector Classic
- [Encryption in transit](https://docs.aws.amazon.com/inspector/v1/userguide/encryption-in-transit.html): Learn about encryption of data in transit for Amazon Inspector Classic.

### [Identity and Access Management](https://docs.aws.amazon.com/inspector/v1/userguide/security-iam.html)

How to authenticate requests and manage access to your Amazon Inspector resources.

- [How Amazon Inspector Classic works with IAM](https://docs.aws.amazon.com/inspector/v1/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Inspector, learn what IAM features are available to use with Amazon Inspector.
- [Identity-based policy examples](https://docs.aws.amazon.com/inspector/v1/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Inspector resources.
- [Using service-linked roles](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_slr.html): How to use service-linked roles to give Amazon Inspector Classic access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/inspector/v1/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Inspector and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/inspector/v1/userguide/security-logging-and-monitoring.html): Learn about logging and monitoring in Amazon Inspector Classic.
- [Incident response](https://docs.aws.amazon.com/inspector/v1/userguide/security-incident-response.html): Learn how Amazon Inspector Classic responds to security incidents.
- [Compliance validation](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/inspector/v1/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Inspector Classic features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/inspector/v1/userguide/infrastructure-security.html): Learn how Amazon Inspector Classic isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/inspector/v1/userguide/security-vulnerability-analysis-management.html): Learn how Amazon Inspector Classic analyzies configuration and vulnerability.
- [Security best practices](https://docs.aws.amazon.com/inspector/v1/userguide/security-best-practices.html): Learn about security best practices for Amazon Inspector Classic.


## [Amazon Inspector Classic agents](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_agents.html)

- [Installing Amazon Inspector Classic agents](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_installing-uninstalling-agents.html): Install Amazon Inspector Classic agents on your EC2 instances that run Linux-based and Windows-based operating systems.
- [Working with Amazon Inspector Classic agents on Linux-based operating systems](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_agents-on-linux.html): Install, remove, verify, and modify the behavior of Amazon Inspector Classic agents for your EC2 instances that run on Linux-based operating systems.
- [Working with Amazon Inspector Classic agents on Windows-based operating systems](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_agents-on-win.html): Start, stop, and modify the behavior of the Amazon Inspector Classic agents on your EC2 instances that run supported Windows-based operating systems.
- [(Optional) Verify the signature of the Amazon Inspector Classic agent installation script on Linux-based operating systems](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_verify-sig-agent-download-linux.html): Verify the signature of the Amazon Inspector Classic agent download on Linux-based operating systems.
- [(Optional) Verify the signature of the Amazon Inspector Classic agent installation script on Windows-based operating systems](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_verify-sig-agent-download-win.html): Verify the signature of the Amazon Inspector Classic agent download on Windows-based operating systems.


## [Amazon Inspector Classic rules packages and rules](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_rule-packages.html)

- [Network Reachability](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_network-reachability.html): Use the Network Reachability rules package in Amazon Inspector Classic to check your network configurations for security vulnerabilities.
- [Common vulnerabilities and exposures](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cves.html): Use the common vulnerabilities and exposures rules package to learn whether your assessment targets are vulnerable to publicly known issues.
- [Center for Internet Security (CIS) Benchmarks](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cis.html): Learn about the CIS Benchmarks rules package for Amazon Inspector Classic.
- [Security best practices for Amazon Inspector Classic](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_security-best-practices.html): Use Amazon Inspector Classic rules to help determine whether your systems are configured securely.


## [Amazon Inspector Classic ARNs](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-arns.html)

- [ARNs for Amazon Inspector Classic resources](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-arns-resources.html): Learn about the ARN format for Amazon Inspector Classic resources.
- [Amazon Inspector Classic ARNS for rules packages](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_rules-arns.html): View a list of Amazon Inspector Classic ARNs for rules packages in all supported Regions.
