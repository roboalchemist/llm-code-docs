# Source: https://docs.aws.amazon.com/guardduty/latest/ug/llms.txt

# Amazon GuardDuty Amazon GuardDuty User Guide

> Use Amazon GuardDuty to continuously monitor the security of your AWS environment.

- [Concepts and key terms](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_concepts.html)
- [Getting started](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html)
- [Foundational data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html)
- [Extended Threat Detection](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html)
- [Protecting AI workloads](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html)
- [Monitoring usage and estimating costs](https://docs.aws.amazon.com/guardduty/latest/ug/monitoring_costs.html)
- [Suspending or disabling](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html)
- [GuardDuty announcements](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_sns.html)
- [GuardDuty quotas](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_limits.html)
- [Managed Instances Support](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managed-instances.html)
- [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html)
- [Legacy actions and parameters](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-legacy-parameters.html)
- [Document history](https://docs.aws.amazon.com/guardduty/latest/ug/doc-history.html)

## [What is GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

- [Pricing in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-pricing.html): This section focuses on the AWS Free Tier model that GuardDuty uses for various protection plans, and how you can view estimated and actual usage costs.
- [Accessing GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-access.html): Amazon GuardDuty is available in most AWS Regions.


## [EKS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html)

- [Enabling EKS Protection in multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/eks-protection-enable-multiple-accounts.html): In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable the EKS Protection; feature for the member accounts in their organization.
- [Enabling EKS Protection for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/eks-protection-enable-standalone-account.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific Region.


## [S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html)

- [Enabling S3 Protection in multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/s3-multiaccount.html): In a multi-account environment, only the delegated GuardDuty administrator account has the option to configure (enable or disable) S3 Protection for the member accounts in their AWS organization.
- [Enabling S3 Protection for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/data-source-configure.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.


## [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html)

### [How it works](https://docs.aws.amazon.com/guardduty/latest/ug/how-does-runtime-monitoring-work.html)

To use Runtime Monitoring, you must enable Runtime Monitoring and then manage the GuardDuty security agent.

- [With Amazon EKS clusters](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-eks.html): Runtime Monitoring uses an EKS add-on aws-guardduty-agent, also called as GuardDuty security agent.
- [With Amazon EC2 instances](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ec2.html): Your Amazon EC2 instances can run multiple types of applications and workloads in your AWS environment.
- [With Fargate (Amazon ECS only)](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ecs-fargate.html): When you enable Runtime Monitoring, GuardDuty becomes ready to consume the runtime events from a task.
- [After you enable Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-after-configuration.html): Learn more about what to expect after you have enabled Runtime Monitoring and deployed the GuardDuty security agent.

### [30-day free trial](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-free-trial-works.html)

The 30-day free trial period works differently for the new GuardDuty accounts and the existing accounts that have already enabled EKS Runtime Monitoring prior to when Runtime Monitoring capability extended to Amazon EC2 instances and AWS Fargate (Amazon ECS only).

- [I enabled EKS Runtime Monitoring prior to the launch of Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/enabled-eks-gdu-prior-runtime-monitoring-30-day.html): Use this section only when EKS Runtime Monitoring was enabled for your AWS account, and now you want to migrate to Runtime Monitoring.

### [Prerequisites](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-prerequisites.html)

Learn more about prerequisites to use Runtime Monitoring and manage the GuardDuty security agent.

- [For EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html): This section includes the prerequisites for monitoring runtime behavior of your Amazon EC2 instances.
- [For Fargate (ECS only) cluster](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.html): This section includes the prerequisites for monitoring runtime behavior of your Fargate-Amazon ECS resources.
- [For EKS cluster](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-eks-support.html): This section includes the prerequisites for monitoring runtime behavior of your Amazon EKS resources.

### [Enabling Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html)

Before enabling Runtime Monitoring in your account, make sure that the resource type for which you want to monitor the runtime events, supports the platforms requirements.

- [Enabling Runtime Monitoring for multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/enable-runtime-monitoring-multiple-acc-env.html): In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable Runtime Monitoring for the member accounts, and manage automated agent configuration for the resource types belonging to the member accounts in their organization.
- [Enabling Runtime Monitoring for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/enable-runtime-monitoring-standalone-acc.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.

### [Managing GuardDuty security agents](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-managing-agents.html)

You can manage the GuardDuty security agent for the resource that you want to monitor.

### [Automated agent on Amazon EC2 resource](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-automated.html)

This section includes steps to enable GuardDuty automated agent for your Amazon EC2 resources in your standalone account or a multiple-account environment.

- [Enabling GuardDuty agent in multiple-account environment](https://docs.aws.amazon.com/guardduty/latest/ug/manage-agent-ec2-multi-account-env.html): In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable automated agent configuration for the resource types belonging to the member accounts in their organization.
- [Enabling GuardDuty automated agent in a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/manage-agent-ec2-standalone-account.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.
- [Migrating from Amazon EC2 manual agent to automated agent](https://docs.aws.amazon.com/guardduty/latest/ug/migrate-from-ec2-manual-to-automated-agent.html): Learn about how you can migrate from managing the security agent for Amazon EC2 manually to using GuardDuty automated agent configuration.

### [Manual agent management for Amazon EC2 resource](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html)

This section provides the steps to manually install and update the security agent for your Amazon EC2 resources.

- [Prerequisite â Creating Amazon VPC endpoint manually](https://docs.aws.amazon.com/guardduty/latest/ug/creating-vpc-endpoint-ec2-agent-manually.html): Before you can install the GuardDuty security agent, you must create an Amazon Virtual Private Cloud (Amazon VPC) endpoint.
- [Installing the security agent manually](https://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html): GuardDuty provides the following two methods to install the GuardDuty security agent on your Amazon EC2 instances.
- [Updating security agent manually](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-update-security-agent-ec2.html): GuardDuty releases updates to the security agent versions.
- [Automated agent on Fargate (Amazon ECS only)](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ecs-automated.html): Runtime Monitoring supports managing the security agent for your Amazon ECS clusters (AWS Fargate) only through GuardDuty.
- [Automated agent on Amazon EKS resource](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html): Runtime Monitoring supports enabling the security agent through GuardDuty automated configuration and manually.

### [Manual agent management for Amazon EKS cluster](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-manually.html)

This section describes how you can manage your Amazon EKS add-on agent (GuardDuty agent) after you enable Runtime Monitoring (or EKS Runtime Monitoring).

- [Prerequisite â Creating an Amazon VPC endpoint](https://docs.aws.amazon.com/guardduty/latest/ug/eksrunmon-prereq-deploy-security-agent.html): Before you can install the GuardDuty security agent, you must create an Amazon Virtual Private Cloud (Amazon VPC) endpoint.
- [Installing GuardDuty security agent manually on Amazon EKS resources](https://docs.aws.amazon.com/guardduty/latest/ug/eksrunmon-deploy-security-agent.html): This section describes how you can deploy the GuardDuty security agent for the first time for specific EKS clusters.
- [Updating security agent manually for Amazon EKS resources](https://docs.aws.amazon.com/guardduty/latest/ug/eksrunmon-update-security-agent.html): When you manage the GuardDuty security agent manually, you are responsible to update it for your account.
- [Configure EKS add-on parameters](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-configure-security-agent-eks-addon.html): Learn how you can configure specific parameters of your Amazon EKS add-on for agent versions 1.5.0 and above.
- [Validating VPC endpoint configuration](https://docs.aws.amazon.com/guardduty/latest/ug/validate-vpc-endpoint-config-runtime-monitoring.html): After you install the security agent manually or through GuardDuty automated configuration, you can use this document to validate that the VPC endpoint configuration.

### [Runtime coverage issues and troubleshooting](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-assessing-coverage.html)

Learn more about assessing runtime coverage for your AWS workloads and containers.

- [Coverage and troubleshooting for Amazon EC2 resources](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-ec2.html): Learn more about how to assess coverage, manage configurations and troubleshoot coverage issues for Amazon EC2 resource.
- [Coverage and troubleshooting for Amazon ECS clusters](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-ecs.html): Learn more about how to assess coverage, manage configurations and troubleshoot coverage issues for Amazon ECS clusters.
- [Coverage and troubleshooting for Amazon EKS clusters](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-coverage.html): Learn how you can assess coverage status for your Amazon EKS clusters when you turn on EKS Runtime Monitoring.
- [Setting up CPU and memory monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-setting-cpu-mem-monitoring.html): Learn how you can set up CPU and memory monitoring on your Amazon EKS and Amazon ECS clusters.
- [Using shared VPC](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-shared-vpc.html): GuardDuty Runtime Monitoring supports using shared Amazon Virtual Private Cloud (Amazon VPC) for your AWS accounts that belong to the same organization in AWS Organizations.
- [Using IaC with automated agents](https://docs.aws.amazon.com/guardduty/latest/ug/using-iac-with-gdu-automated-agents-runtime-monitoring.html): Use this section only if the following list applies to your use case:
- [Collected runtime event types](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-collected-events.html): The GuardDuty security agent collects the following events types and sends them to the GuardDuty backend for threat detection and analysis.

### [Amazon ECR repository hosting GuardDuty agent](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-ecr-repository-gdu-agent.html)

Learn more about Amazon ECR repository URI hosting GuardDuty security agent in various AWS Regions.

- [ECR repo for EKS v1.12.1 - 1.8.1 (eks.build.2)](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-agent-ecr-image-uri-v1-8-1-build-2.html): When you enable GuardDuty automated configuration for Runtime Monitoring for EKS, GuardDuty will deploy this agent version to your Amazon EKS clusters.
- [ECR repo for EKS version 1.8.1.eks.build.1](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-agent-ecr-image-uri-v1-8-1-build-1.html): Learn about which Amazon ECR repositories are used to host the Amazon EKS add-on GuardDuty agent versions 1.8.1-eks-build.1 and older.
- [ECR repository for security agent on AWS Fargate (Amazon ECS only)](https://docs.aws.amazon.com/guardduty/latest/ug/ecs-runtime-agent-ecr-image-uri.html): Learn about which Amazon ECR repositories are used to host the GuardDuty agent for AWS Fargate (Amazon ECS only).
- [Security agents on same host](https://docs.aws.amazon.com/guardduty/latest/ug/two-security-agents-installed-on-ec2-node.html): Amazon EC2 instances can support multiple types of workloads.

### [EKS Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-guardduty.html)

EKS Runtime Monitoring provides runtime threat detection coverage for Amazon Elastic Kubernetes Service (Amazon EKS) nodes and containers within your AWS environment.

- [Configuring EKS Runtime Monitoring for multiple-account environments (API)](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-multiple-accounts.html): In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable EKS Runtime Monitoring for the member accounts, and manage GuardDuty agent management for the EKS clusters belonging to the member accounts in their organization.
- [Configuring EKS Runtime Monitoring for a standalone account (API)](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.

### [Migrating from EKS Runtime Monitoring to Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/migrating-from-eksrunmon-to-runtime-monitoring.html)

With the launch of GuardDuty Runtime Monitoring, the threat detection coverage has been expanded to Amazon ECS containers and Amazon EC2 instances.

- [Checking EKS Runtime Monitoring configuration status](https://docs.aws.amazon.com/guardduty/latest/ug/checking-eks-runtime-monitoring-enable-status.html): Use the following APIs or AWS CLI commands to check the existing configuration status of EKS Runtime Monitoring.
- [Disable EKS Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/disabling-eks-runtime-monitoring.html): After you have ensured that the existing settings for your account or organization have been replicated to Runtime Monitoring, you can disable EKS Runtime Monitoring.
- [GuardDuty security agent release versions](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-release-history.html): Learn more about the versions of the GuardDuty security agent for all the resources that Runtime Monitoring supports.

### [Disabling, uninstalling, and resource cleanup](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-resource-clean-up.html)

Learn about which resources does GuardDuty clean up after your disable Runtime Monitoring or EKS Runtime Monitoring and which resources can you delete.

- [Uninstalling security agent manually for Amazon EC2 resources](https://docs.aws.amazon.com/guardduty/latest/ug/uninstalling-gdu-ec2-agent-runtime-monitoring.html): This section provides methods to uninstall the GuardDuty security agent from your Amazon EC2 resources.
- [Cleaning up security agent resources](https://docs.aws.amazon.com/guardduty/latest/ug/clean-up-guardduty-agent-resources-process.html): This section explains how you can clean up the AWS resources associated with the security agent.


## [Malware Protection for EC2](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html)

- [How GuardDuty scans EBS volumes for malware detection](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_malware_protection-ebs-volume-data.html): This section explains how Malware Protection for EC2, including both GuardDuty-initiated malware scan and On-demand malware scan, scans the Amazon EBS volumes associated with your Amazon EC2 instances and container workloads.
- [Supported EBS volumes](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malpro-supported-volumes.html): In all of the AWS Regions where GuardDuty supports the Malware Protection for EC2 feature, you can scan the Amazon EBS volumes that are unencrypted or encrypted.
- [Set up snapshot retention and EC2 scan coverage](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-customizations.html): Learn how to retain snapshots when Amazon GuardDuty detects malware in Malware Protection for EC2 scans, and how to exclude or include specific EC2 instances for malware scanning.

### [GuardDuty-initiated malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-initiated-malware-scan.html)

With GuardDuty-initiated malware scan enabled, whenever GuardDuty generates , an agentless malware scan on the Amazon Elastic Block Store (Amazon EBS) volumes attached to the potentially impacted Amazon EC2 resource will initiate.

- [30-day free trial](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-ec2-guardduty-30-day-free-trial.html): You can choose to enable or disable GuardDuty-initiated malware scan for an AWS account in a supported AWS Region at any time.
- [Enabling GuardDuty-initiated malware scan in multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/configure-malware-protection-guardduty-initiated-multi-account.html): Learn how to configure GuardDuty-initiated malware scan to detect potentially malicious activities in your AWS Organizations member accounts.
- [Enabling GuardDuty-initiated malware scan for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/configure-malware-protection-single-account.html): Learn how to configure GuardDuty-initiated malware scan to detect potentially malicious activities in your own (standalone) AWS accounts.
- [Findings that invoke GuardDuty-initiated malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/gd-findings-initiate-malware-protection-scan.html): Learn more about which GuardDuty findings initiate an automatic scan to detect presence of malware in your resources.

### [On-demand malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/on-demand-malware-scan.html)

On-demand malware scan helps you detect the presence of malware on Amazon Elastic Block Store (Amazon EBS) volumes attached to your Amazon EC2 instances.

- [Starting On-demand malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.html): Learn how to start an On-demand malware scan within GuardDuty Malware Protection for EC2.
- [Re-scanning previously scanned Amazon EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/initiate-on-demand-scan-on-same-resource.html): Whether a scan is GuardDuty-initiated or started on-demand, you can start a new on-demand malware scan on the same Amazon EC2 instance after 1 hour from the start time of the previous malware scan.
- [Monitoring malware scan statuses and results](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-scans.html): Learn how you can access and filter the GuardDuty Malware Protection for EC2 scans using the https://console.aws.amazon.com/guardduty/ console and the API.
- [GuardDuty service account](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-service-account-region-list.html): When a snapshot gets created and shared with a GuardDuty service account, a new event gets created in your CloudTrail logs.
- [Quotas in Malware Protection for EC2](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-limitations.html): This section includes the quotas associated with using Malware Protection for EC2.


## [Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html)

### [Pricing and usage cost](https://docs.aws.amazon.com/guardduty/latest/ug/pricing-malware-protection-for-s3-guardduty.html)

Learn about 12-month Free Tier pricing for Malware Protection for S3 in GuardDuty.

- [Reviewing usage cost](https://docs.aws.amazon.com/guardduty/latest/ug/usage-cost-malware-protection-s3-gdu.html): Learn how to view the usage cost for GuardDuty Malware Protection for S3.
- [How it works](https://docs.aws.amazon.com/guardduty/latest/ug/how-malware-protection-for-s3-gdu-works.html): Learn how GuardDuty Malware Protection for S3 works and understand the differences of enabling it with and without GuardDuty.
- [Capabilities of Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/s3-malware-protection-capability.html): Learn what Malware Protection for S3 can offer after you enable it for an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.
- [(Optional) Get started with Malware Protection for S3 only (console)](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-get-started-independent.html): Use this optional step when you want to get started with Malware Protection for S3 threat detection option independent of the GuardDuty status in your AWS account.

### [Configuring Malware Protection for S3 for your bucket](https://docs.aws.amazon.com/guardduty/latest/ug/configuring-malware-protection-for-s3-guardduty.html)

Start using Malware Protection for S3 to detect if the newly uploaded files to your Amazon S3 buckets and object prefixes potentially contains malware.

- [Enabling Malware Protection for S3 threat detection for your bucket](https://docs.aws.amazon.com/guardduty/latest/ug/enable-malware-protection-s3-bucket.html): This section provides detailed steps on how to enable Malware Protection for S3 for a bucket in your own account.
- [IAM role permissions](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-iam-policy-prerequisite.html): For Malware Protection for S3 to scan and (optionally) add tags to your S3 objects, you can use service roles that has the necessary permissions to perform malware scan actions on your behalf.
- [Troubleshooting IAM role permissions error](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshoot-malware-protection-s3-iam-role-permissions-error.html): If your request to enable Malware Protection for S3 is getting rejected because of IAM role missing required permissions, then follow these troubleshooting steps to validate your Amazon S3 bucket ownership.
- [Steps after enabling Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-steps-after-enabling.html): This section lists the steps that you may take after enabling Malware Protection for S3 for a bucket.
- [On-demand S3 malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-on-demand.html): GuardDuty Malware Protection for S3 continuously monitors new S3 uploads.
- [Using tag-based access control (TBAC)](https://docs.aws.amazon.com/guardduty/latest/ug/tag-based-access-s3-malware-protection.html): When enabling Malware Protection for S3 for your bucket, you can optionally choose to enable tagging.
- [View and understand protected bucket status](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-bucket-status-gdu.html): The status of a protected bucket indicates whether or not Malware Protection for S3 would work as expected.

### [Monitoring S3 object scans](https://docs.aws.amazon.com/guardduty/latest/ug/monitoring-malware-protection-s3-scans-gdu.html)

When using Malware Protection for S3 with a GuardDuty detector ID, if your Amazon S3 object is potentially malicious, GuardDuty will generate .

- [Using Amazon EventBridge](https://docs.aws.amazon.com/guardduty/latest/ug/monitor-with-eventbridge-s3-malware-protection.html): Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources.

### [Using S3 Object Tags](https://docs.aws.amazon.com/guardduty/latest/ug/monitor-enable-s3-object-tagging-malware-protection.html)

Use enable tagging option so that GuardDuty can add tags to your Amazon S3 object after completing the malware scan.

- [Troubleshooting S3 object post-scan tag failures](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshoot-s3-post-scan-tag-failures.html): This section applies to you only if you in your protected bucket.
- [Using CloudWatch alarms and metrics](https://docs.aws.amazon.com/guardduty/latest/ug/monitor-cloudwatch-metrics-s3-malware-protection.html): You can monitor GuardDuty using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

### [Troubleshooting](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshoot-s3-malware-protection.html)

Contents

- [Troubleshooting Malware Protection plan status](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshoot-s3-malware-protection-status-errors.html): For any protected bucket, GuardDuty displays the Status based on the ranking.
- [Troubleshooting on-demand malware scan](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshoot-s3-malware-protection-on-demand.html)
- [Editing Malware Protection plan for a protected bucket](https://docs.aws.amazon.com/guardduty/latest/ug/edit-malware-protection-protected-s3-bucket.html): You may need to edit the preferred IAM permissions policy, enable or disable tagging of the scanned S3 object, or add or remove S3 object prefixes.
- [Disabling Malware Protection for S3 for a protected bucket](https://docs.aws.amazon.com/guardduty/latest/ug/disable-malware-s3-protected-bucket.html): When you disable Malware Protection for S3 for a protected bucket, GuardDuty deletes the Malware Protection plan ID associated with that bucket.
- [Supportability of Amazon S3 features](https://docs.aws.amazon.com/guardduty/latest/ug/supported-s3-features-malware-protection-s3.html): The following table specifies whether or not Malware Protection for S3 supports the listed Amazon S3 features.
- [Malware Protection for S3 quotas](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-quotas-guardduty.html): This section provides default quotas, often referred to as limits.


## [Malware Protection for AWS Backup](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup.html)

- [How it works](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-how-it-works.html): This section describes components of Malware Protection for Backup, how it works, and how you can review the malware scan status and result.
- [IAM Role Permissions](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-iam-permissions.html)
- [Get started independently](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-get-started-independent.html): Use this optional step when you want to get started with Malware Protection for Backup threat detection option independent of the GuardDuty status in your AWS account.
- [Starting on-demand scans](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-start-on-demand-scan.html)
- [Monitoring malware scan statuses and results](https://docs.aws.amazon.com/guardduty/latest/ug/monitoring-malware-protection-backup-scans.html): After a malware scan is initiated, GuardDuty provides a few mechanisms through which you may monitor the status and result of a scan.
- [Malware Protection for Backup Quotas](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-quotas.html)


## [RDS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)

- [Enabling RDS Protection in multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/configure-rds-pro-multi-account.html): In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable the RDS Protection feature for the member accounts in their organization.
- [Enabling RDS Protection for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/configure-rds-pro-standalone.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.
- [Troubleshooting RDS Protection monitoring issues](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting-rds-protection-guardduty.html): GuardDuty RDS Protection analyzes and profiles your RDS login activity for potential access threats to the .


## [Lambda Protection](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html)

- [Enabling Lambda Protection in multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/configure-lambda-protection-multi-acc-env.html): In a multi-account environment, only the delegated GuardDuty administrator account has the option to enable or disable Lambda Protection for the member accounts in their organization.
- [Enabling Lambda Protection for a standalone account](https://docs.aws.amazon.com/guardduty/latest/ug/configure-lambda-protection-standalone-acc.html): A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.


## [Multiple accounts in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html)

- [Administrator account and member account relationships](https://docs.aws.amazon.com/guardduty/latest/ug/administrator_member_relationships.html): When you use GuardDuty in a multiple-account environment, the administrator account can manage certain aspects of GuardDuty on behalf of the member accounts.

### [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)

Learn how you can manage a multiple-account environment in Amazon GuardDuty by using AWS Organizations.

- [Permissions required to designate a delegated GuardDuty administrator account](https://docs.aws.amazon.com/guardduty/latest/ug/organizations_permissions.html): To start using Amazon GuardDuty with AWS Organizations, the AWS Organizations management account for the organization designates an account as the delegated GuardDuty administrator account.
- [Designating delegated GuardDuty administrator account](https://docs.aws.amazon.com/guardduty/latest/ug/delegated-admin-designate.html): This section provides steps to designate a delegated administrator in the GuardDuty organization.
- [Setting organization auto-enable preferences](https://docs.aws.amazon.com/guardduty/latest/ug/set-guardduty-auto-enable-preferences.html): The auto-enable organization feature in GuardDuty helps you set the same GuardDuty and protection plans status for ALL existing or NEW member accounts in your organization, in a single step.
- [Adding members to the organization](https://docs.aws.amazon.com/guardduty/latest/ug/add-member-accounts-guardduty-organization.html): As a delegated GuardDuty administrator account, you can add one or more AWS accounts to the GuardDuty organization.
- [(Optional) Enable protection plans for existing member accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_quick_protection_plan_config.html): The following procedure includes steps to enable protection plans for existing member accounts by using the Accounts page.
- [Continually managing your member accounts within GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/maintaining-guardduty-organization-delegated-admin.html): Learn how to maintain your large organization as a delegated GuardDuty administrator account.
- [Suspending GuardDuty for member account](https://docs.aws.amazon.com/guardduty/latest/ug/suspending-guardduty-member-account-from-admin.html): As a delegated GuardDuty administrator account, you can suspend the GuardDuty service for a member account in your organization.
- [Disassociating (removing) member account from administrator account](https://docs.aws.amazon.com/guardduty/latest/ug/disassociate-remove-member-account-from-admin.html): When you want to stop configuring the GuardDuty settings and accessing the data from a member account, remove that account as a GuardDuty member account.
- [Deleting member accounts from GuardDuty organization](https://docs.aws.amazon.com/guardduty/latest/ug/delete-member-accounts-guardduty-organization.html): As a delegated GuardDuty administrator account, after you have disassociated a member account and you no longer want to keep that member account in the GuardDuty organization, you can delete that member account from your GuardDuty organization.
- [Changing the delegated GuardDuty administrator account](https://docs.aws.amazon.com/guardduty/latest/ug/change-guardduty-delegated-admin.html): You can remove the delegated GuardDuty administrator account for your organization in each Region and then delegate a new administrator in each Region.

### [Managing accounts by invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html)

Invite other accounts to have their GuardDuty managed by your GuardDuty administrator account.

- [Adding accounts by invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_become_console.html): As an administrator account that already has GuardDuty enabled, you can add members to start using GuardDuty.
- [Consolidating administrator accounts under a single organization](https://docs.aws.amazon.com/guardduty/latest/ug/consolidate-orgs.html): GuardDuty recommends using association through AWS Organizations to manage member accounts under a delegated GuardDuty administrator account.
- [GuardDuty considerations for Export CSV option in accounts](https://docs.aws.amazon.com/guardduty/latest/ug/exporting-guardduty-accounts-data-to-csv.html): Learn when you can use the Amazon GuardDuty console to download the details associated with your member accounts, in a CSV.


## [Finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html)

- [EC2 finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html): Learn about EC2 finding types in GuardDuty.
- [IAM finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html): Learn about IAM finding types in GuardDuty.
- [Attack sequence finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html): Learn about attack sequence findings that GuardDuty generates in your AWS account.
- [S3 Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html): Learn about Amazon Simple Storage Service (Amazon S3) finding types in GuardDuty.
- [EKS Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html): Learn about EKS audit logs finding types in GuardDuty.
- [Runtime Monitoring finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html): Learn more about the findings that get generated when Runtime Monitoring identifies a potential threat in your AWS environment.
- [Malware Protection for EC2 finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html): GuardDuty Malware Protection for EC2 provides a single Malware Protection for EC2 finding for all threats detected during the scan of an EC2 instance or a container workload.
- [Malware Protection for S3 finding type](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3-finding-types.html): Learn about the Malware Protection for S3 finding type that gets generated when the malware scan identifies a potentially malicious file.
- [Malware Protection for Backup finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html): GuardDuty Malware Protection for Backup provides a single finding for all threats detected during the scan of the requested resource.
- [RDS Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html): Learn about GuardDuty RDS Protection finding types.
- [Lambda Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html): Learn about the finding types that GuardDuty may generate when you turn on the Lambda Protection feature.
- [Retired finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html): Learn about the GuardDuty retired finding types.


## [Understanding and generating findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)

- [GuardDuty finding format](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-format.html): Learn about the Amazon GuardDuty finding format.
- [GuardDuty malware detection scan engine](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-malware-detection-scan-engine.html): Learn about Amazon GuardDuty malware detection methodology and which scan engines does it use.
- [Sample findings](https://docs.aws.amazon.com/guardduty/latest/ug/sample_findings.html): Amazon GuardDuty helps you generate sample findings to visualize and understand the various finding types that it can generate.
- [Test GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-scripts.html): Learn how you can run a guardduty-tester script in your dedicated non-production AWS account to generate Amazon GuardDuty findings, and understand these findings.
- [Findings page in GuardDuty console](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_working-with-findings.html): When GuardDuty detects an activity that matches the pattern of a security issue, GuardDuty generates a finding.
- [Findings severity levels](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html): Each GuardDuty finding has an assigned severity level and value that reflects the potential risk the finding could have to your environment, as determined by our security engineers.
- [Finding details](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html): Learn about the types of data available within GuardDuty findings.
- [GuardDuty finding aggregation](https://docs.aws.amazon.com/guardduty/latest/ug/finding-aggregation.html): GuardDuty updates the generated findings dynamically.


## [Managing GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/findings_management.html)

- [GuardDuty Summary dashboard](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-summary.html): Learn how you can view the insights about Amazon GuardDuty findings in your AWS environment.
- [Filtering GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html): A finding filter allows you to view findings that match the criteria you specify and filter out any unmatched findings.

### [Suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rule.html)

A suppression rule is a set of criteria, consisting of a filter attribute paired with a value, used to filter findings by automatically archiving new findings that match the specified criteria.

- [Creating suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/create-suppression-rules-guardduty.html): A suppression rule is a set of criteria that includes using filter attributes and providing values for which you don't want GuardDuty to generate a finding type.
- [Updating suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/update-suppression-rules-guardduty.html): This section provides the steps to update a suppression rule in your AWS account in a specific AWS Region.
- [Deleting suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/delete-suppression-rules-guardduty.html): This section provides the steps to delete a suppression rule in your AWS account in a specific AWS Region.

### [Entity lists and IP address lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html)

Learn to customize the threat detection scope of Amazon GuardDuty using trusted and threat intelligence lists containing IP addresses, domains, or both.

- [Setting up prerequisites for entity lists and IP address lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-prerequisites.html): GuardDuty uses entity lists and IP address lists to customize threat detection in your AWS environment.
- [Adding and activating an entity list or IP list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html): Entity lists and IP address lists help you customize the threat detection capabilities in GuardDuty.
- [Updating an entity list or IP address list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-update-procedure.html): Entity lists and IP address lists help you customize the threat detection capabilities in GuardDuty.
- [De-activating entity list or IP address list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-deactivate-procedure.html): When you no longer want GuardDuty to use a list, you can deactivate it.
- [Deleting entity list or IP address list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-delete-procedure.html): When you no longer want to keep a list entry in your entity set or IP address set, you can delete it.
- [Exporting generated findings to Amazon S3](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html): Learn how you can configure settings for exporting GuardDuty findings to your Amazon S3 bucket.
- [Processing findings with EventBridge](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_eventbridge.html): Learn how to use Amazon EventBridge, formerly Amazon CloudWatch Events, to detect, monitor, and process Amazon GuardDuty findings automatically.
- [Understanding CloudWatch Logs and reasons for skipping resources](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-auditing-scan-logs.html): Learn how you can audit the CloudWatch Logs for GuardDuty Malware Protection for EC2 and what are the reasons because of which your impacted Amazon EC2 instance or Amazon EBS volumes may have been skipped during the scanning process.
- [Reporting false positive EC2 malware scan result](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-false-positives.html): Learn about submitting a false positive finding in GuardDuty Malware Protection for EC2, where you believe the file is not malicious.
- [Reporting false positive S3 object scan result](https://docs.aws.amazon.com/guardduty/latest/ug/report-malware-protection-s3-false-positives.html): Learn how you can report potential false positive scenarios in GuardDuty Malware Protection for S3.
- [Reporting false positive Backup malware scan result](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-backup-false-positives.html): Learn about submitting a false positive or negative finding in GuardDuty Malware Protection for EC2, when you believe the file is not malicious.


## [Remediating findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html)

- [Remediating a potentially compromised Amazon EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ec2.html): When GuardDuty generates finding types that indicate potentially compromised Amazon EC2 resources, then your Resource will be Instance.
- [Remediating a potentially compromised S3 bucket](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-s3.html): When GuardDuty generates , it indicates that your Amazon S3 buckets have been compromised.
- [Remediating a potentially malicious S3 object](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-s3object-malware-protection-gdu.html): Learn how you can remediate the Malware Protection for S3 finding type that gets generated in your AWS account that has GuardDuty enabled.
- [Remediating a potentially compromised EBS Snapshot](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-snapshot.html): When GuardDuty generates an Execution:EC2/MaliciousFile!Snapshot finding type, it indicates that malware has been detected in an Amazon EBS snapshot.
- [Remediating a potentially compromised EC2 AMI](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ami.html): When GuardDuty generates an Execution:EC2/MaliciousFile!AMI finding type, it indicates that malware has been detected in an Amazon Machine Image (AMI).
- [Remediating a potentially compromised EC2 Recovery Point](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ec2-recoverypoint.html): When GuardDuty generates an Execution:EC2/MaliciousFile!RecoveryPoint finding type, it indicates that malware has been detected in an EC2 Recovery Point Backup resource.
- [Remediating a potentially compromised S3 Recovery Point](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-s3-recoverypoint.html): When GuardDuty generates an Execution:S3/MaliciousFile!RecoveryPoint finding type, it indicates that malware has been detected in an S3 Recovery Point Backup resource.
- [Remediating a potentially compromised ECS cluster](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ecs.html): A potentially compromised ECS cluster finding indicates suspicious or malicious activity has been detected within your Amazon ECS environment.
- [Remediating potentially compromised AWS credentials](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-creds.html): When GuardDuty generates , it indicates that your AWS credentials have been compromised.
- [Remediating a potentially compromised standalone container](https://docs.aws.amazon.com/guardduty/latest/ug/remediate-compromised-standalone-container.html): When GuardDuty generates finding types that indicate potentially compromised container, your Resource type will be Container.
- [Remediating EKS Protection findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-remediate-kubernetes.html): Learn how to remediate potential Kubernetes security issues discovered by Amazon GuardDuty.
- [Remediating Runtime Monitoring findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-remediate-runtime-monitoring.html): Learn how to remediate potential EKS Runtime Monitoring security issues discovered by Amazon GuardDuty.
- [Remediating a potentially compromised database](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-remediate-compromised-database-rds.html): Learn how to remediate potential Amazon Aurora login activity issues discovered by Amazon GuardDuty.
- [Remediating a potentially compromised Lambda function](https://docs.aws.amazon.com/guardduty/latest/ug/remediate-lambda-protection-finding-types.html): Learn how to remediate a Lambda Protection finding type in Amazon GuardDuty.


## [Feature names for protection plans in API](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-features-activation-model.html)

- [GuardDuty API changes](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-feature-object-api-changes-march2023.html): The GuardDuty APIs configure protection features that don't belong to the list of .


## [Security](https://docs.aws.amazon.com/guardduty/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/guardduty/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon GuardDuty.

- [Opting out of using your data for service improvement](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-opting-out-using-data.html): Learn how you can opt-out of allowing Amazon GuardDuty use your data for service improvement.

### [Logging with CloudTrail](https://docs.aws.amazon.com/guardduty/latest/ug/logging-using-cloudtrail.html)

Amazon GuardDuty is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in GuardDuty.

- [Example: GuardDuty log file entries](https://docs.aws.amazon.com/guardduty/latest/ug/understanding-guardduty-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

### [Identity and Access Management](https://docs.aws.amazon.com/guardduty/latest/ug/security-iam.html)

How to authenticate requests and manage access your GuardDuty resources.

- [How Amazon GuardDuty works with IAM](https://docs.aws.amazon.com/guardduty/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to GuardDuty, learn what IAM features are available to use with GuardDuty.
- [Identity-based policy examples](https://docs.aws.amazon.com/guardduty/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify GuardDuty resources.

### [Using service-linked roles](https://docs.aws.amazon.com/guardduty/latest/ug/using-service-linked-roles.html)

How to use service-linked roles to give Amazon GuardDuty access to resources in your AWS account.

- [GuardDuty service-linked role (SLR)](https://docs.aws.amazon.com/guardduty/latest/ug/slr-permissions.html): GuardDuty uses the service-linked role (SLR) named AWSServiceRoleForAmazonGuardDuty.
- [Service-linked role permissions for Malware Protection for EC2](https://docs.aws.amazon.com/guardduty/latest/ug/slr-permissions-malware-protection.html): Malware Protection for EC2 uses the service-linked role (SLR) named AWSServiceRoleForAmazonGuardDutyMalwareProtection.
- [AWS managed policies](https://docs.aws.amazon.com/guardduty/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for GuardDuty and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/guardduty/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with GuardDuty and IAM.
- [Compliance validation](https://docs.aws.amazon.com/guardduty/latest/ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/guardduty/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific GuardDuty features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/guardduty/latest/ug/infrastructure-security.html): Learn how Amazon GuardDuty isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/guardduty/latest/ug/security-vpc-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon GuardDuty without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [Integration with AWS security services](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_integrations.html)

- [AWS Security Hub CSPM integration](https://docs.aws.amazon.com/guardduty/latest/ug/securityhub-integration.html): Learn how Amazon GuardDuty integrates with and sends findings to AWS Security Hub CSPM.
- [Amazon Detective integration](https://docs.aws.amazon.com/guardduty/latest/ug/detective-integration.html): Learn how to use the Amazon GuardDuty integration with Amazon Detective.


## [Troubleshooting](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting.html)

- [Exporting findings to Amazon S3 - access error](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting-guardduty-general-issues.html): When you export GuardDuty findings to an Amazon S3 bucket (publishing destination), if GuardDuty is unable to access this publishing destination, then you may get an access error.
- [Malware Protection for EC2 issues](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting-guardduty-malware-protection-issues.html): This section lists the errors that you may experience when setting up or using Malware Protection for EC2.
- [Runtime Monitoring issues](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting-guardduty-runtime-monitoring.html): This section lists the errors that you may experience when setting up or using Runtime Monitoring.
- [Other troubleshooting issues](https://docs.aws.amazon.com/guardduty/latest/ug/troubleshooting-other-topics.html): If you don't find a scenario suitable to your issue, view the following troubleshooting options:
