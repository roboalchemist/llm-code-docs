# Source: https://docs.aws.amazon.com/evs/latest/userguide/llms.txt

# Amazon Elastic VMware Service User Guide

> Describes all Amazon EVS concepts and provides instructions on using the various features with both the console and the command line interface.

- [Getting started](https://docs.aws.amazon.com/evs/latest/userguide/getting-started.html)
- [Troubleshooting](https://docs.aws.amazon.com/evs/latest/userguide/troubleshooting.html)
- [CloudTrail logs](https://docs.aws.amazon.com/evs/latest/userguide/logging-using-cloudtrail.html)
- [Service quotas](https://docs.aws.amazon.com/evs/latest/userguide/service-quotas-evs.html)
- [Document history](https://docs.aws.amazon.com/evs/latest/userguide/doc-history.html)

## [What is Amazon Elastic VMware Service?](https://docs.aws.amazon.com/evs/latest/userguide/what-is-evs.html)

- [Concepts and components](https://docs.aws.amazon.com/evs/latest/userguide/concepts.html): Learn about Amazon EVS concepts and service components.
- [Architecture](https://docs.aws.amazon.com/evs/latest/userguide/architecture.html): Learn about the Amazon EVS service architecture.


## [Setting up Amazon Elastic VMware Service](https://docs.aws.amazon.com/evs/latest/userguide/setting-up.html)

- [Deployment checklist](https://docs.aws.amazon.com/evs/latest/userguide/evs-deployment-prereq-checklist.html): This section contains a list of prerequisites that must be completed to enable successful Amazon EVS environment deployment.


## [Migration](https://docs.aws.amazon.com/evs/latest/userguide/migrate-evs-hcx.html)

- [HCX public connectivity](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-hcx-internet-access.html): You can configure public internet access for your HCX public VLAN by associating Elastic IP addresses with your VLAN.


## [Managing environments](https://docs.aws.amazon.com/evs/latest/userguide/env-mgmt.html)

- [VCF subscriptions](https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html)
- [VCF versions and EC2 instances](https://docs.aws.amazon.com/evs/latest/userguide/versions-provided.html): Amazon EVS provides multiple versions of VMware Cloud Foundation (VCF), ESX, and EC2 instance types that you can select when creating an environment and creating a host.
- [Lifecycle management](https://docs.aws.amazon.com/evs/latest/userguide/evs-lifecycle-mgmt.html): This page describes your lifecycle management responsibilities within an Amazon EVS environment.

### [Environment maintenance](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-maintenance.html)

This section describes how to perform common maintenance tasks for your Amazon EVS environment.

- [Monitor environment status](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-status-check.html): You can monitor various aspects of your Amazon EVS environment and underlying AWS resources using the Amazon EVS console or AWS CLI.
- [AMI maintenance](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-ami-maintenance.html): Amazon EVS deploys ESX hosts with a custom EVS Amazon Machine Image (AMI).
- [Host maintenance](https://docs.aws.amazon.com/evs/latest/userguide/evs-host-maintenance.html): Because Amazon EVS is a self-managed service, you are responsible for maintenance of the VMware Cloud Foundation (VCF) software that runs on the host, monitoring host health, and remediating host issues, including host replacement in the event of host failure.
- [Configure custom route table](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-config-custom-rt.html): Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created.
- [Configure network ACL](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-nacl-cong.html): A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level.
- [Secrets](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-secret-rotation.html): Amazon EVS uses AWS Secrets Manager to create, encrypt, and store secrets in your account on initial environment deployment.
- [Create host](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-create-host.html): After an Amazon EVS environment deploys, you can add hosts to increase capacity and workload resiliency.
- [Delete host](https://docs.aws.amazon.com/evs/latest/userguide/evs-env-delete-host.html): You can delete an Amazon EVS host from your environment when the host is no longer needed.


## [Security](https://docs.aws.amazon.com/evs/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/evs/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon EVS.

### [Identity and access management](https://docs.aws.amazon.com/evs/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Elastic VMware Service resources.

- [How Amazon EVS works with IAM](https://docs.aws.amazon.com/evs/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon EVS, learn what IAM features are available to use with Amazon EVS.
- [Amazon EVS identity-based policy examples](https://docs.aws.amazon.com/evs/latest/userguide/security-iam-id-based-policy-examples.html): By default, IAM users and roles donât have permission to create or modify Amazon EVS resources.
- [Troubleshooting Amazon EVS identity and access](https://docs.aws.amazon.com/evs/latest/userguide/security-iam-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon EVS and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/evs/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon EVS and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/evs/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon EVS access to resources in your AWS account.
- [Resilience](https://docs.aws.amazon.com/evs/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EVS features for data resiliency.


## [Working with other services](https://docs.aws.amazon.com/evs/latest/userguide/evs-integrations.html)

- [AWS CloudFormation](https://docs.aws.amazon.com/evs/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon EVS using an AWS CloudFormation template.

### [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/evs/latest/userguide/fsx-ontap.html)

The NetApp Trident allows Amazon EVS environments to manage the lifecycle of persistent volumes (PVs) backed by Amazon FSx for NetApp ONTAP file systems.

- [Configure as an NFS datastore](https://docs.aws.amazon.com/evs/latest/userguide/config-fsx-nfs-datastore.html): Learn how to configure FSx for NetApp ONTAP as an NFS datastore for Amazon EVS.
- [Configure as an iSCSI datastore](https://docs.aws.amazon.com/evs/latest/userguide/config-fsx-iscsi-datastore.html): Learn how to configure FSx for NetApp ONTAP as an iSCSI datastore for Amazon EVS.
