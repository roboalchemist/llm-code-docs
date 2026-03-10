# Source: https://docs.aws.amazon.com/sap/latest/sap-hana/llms.txt

# SAP HANA on AWS SAP HANA Guides

> Provides information about implementing SAP HANA solutions on AWS.

- [Home](https://docs.aws.amazon.com/sap/latest/sap-hana/welcome.html)

## [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html)

### [Amazon S3](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-amazon-s3.html)

This section provides information about setting up and using AWS Backint agent to backup and restore your SAP HANA workloads to Amazon S3.

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-s3-prerequisites.html): After your SAP HANA system is successfully running on an Amazon EC2 instance, verify the following prerequisites to install AWS Backint agent using the Amazon EC2 Systems Manager document or using AWS Backint installer.
- [Install and configure](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-s3-installing-configuring.html): This section provides information to help you install the AWS Backint agent using an AWS Systems Manager document or AWS Backint installer.
- [Backup and restore](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-s3-backup-restore.html): When the AWS Backint agent is installed and configured on your Amazon EC2 instance, you can initiate backup and recovery using SQL statements, SAP HANA Cockpit, or SAP HANA Studio.
- [AWS Backup](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-backup.html): This section provides information about setting up and using to backup and restore your SAP HANA databases to AWS Backup.
- [Verify signature](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-signature.html): The source file of AWS Backint agent (aws-backint-agent.tar.gz) and AWS Backint installer (install-aws-backint-agent) supports signature verification.
- [Uninstall](https://docs.aws.amazon.com/sap/latest/sap-hana/uninstall-agent.html): Use the following steps to uninstall AWS Backint agent.
- [Troubleshoot](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-troubleshooting.html): The following documentation can help you troubleshoot problems that you might have with your AWS Backint Agent for SAP HANA installation or backups.
- [Version history](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-version-history.html): The following table summarizes the changes for each release of AWS Backint agent.


## [EBS snapshots for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/ebs-sap-hana.html)

- [Considerations](https://docs.aws.amazon.com/sap/latest/sap-hana/dlm-sap-considerations.html): Only the following configurations are supported.
- [How to automate the creation of EBS snapshots for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/dlm-sap-how.html): In a running database, to be application-consistent, EBS snapshots must be aligned with an internal database snapshot.
- [Restoring SAP HANA from EBS snapshots](https://docs.aws.amazon.com/sap/latest/sap-hana/restore-strategy.html): A successful restore strategy is dependent on many factors, including:


## [Migrating SAP HANA to AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-sap-hana-to-aws.html)

- [Migration Frameworks](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-frameworks.html): Although this guide focuses on SAP HANA migrations to AWS, it is important to understand AWS migrations in a broader context.
- [Planning](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-planning.html): Before you start migrating your SAP environment to AWS, there are some prerequisites that we recommend you go over, to ensure minimal interruptions or delays.
- [SAP HANA Sizing](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-sizing.html): The size of the SAP HANA system required on the AWS Cloud depends on the migration scenario.
- [Migration Tools and Methodologies](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-tools.html): This section provides an introduction to the tools and methodologies available to you for your SAP system migration.
- [Migration Scenarios](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-migration-steps.html): The following table lists the migration scenarios that we will cover in detail in this guide.
- [Migrating AnyDB to SAP HANA on AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-anydb-to-hana.html): Migrating from anyDB to HANA typically involves changes to the database platform and sometimes includes operating system changes.
- [Migrating SAP HANA from Other Platforms to AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-hana-to-aws.html): This scenario is more straightforward than migrating from anyDB, because youâre already using SAP HANA.
- [Migrating SAP HANA on AWS to an EC2 High Memory Instance](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-to-hm.html): EC2 High Memory instances are built on AWS Nitro System with up to 24TB of memory in a single instance to deliver scalable and elastic infrastructure capabilities for large in-memory databases, such as SAP HANA.
- [Security](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-security.html): In the AWS Cloud Adoption Framework (CAF), security is a perspective that focuses on subjects such as account governance, account ownership, control frameworks, change and access management, and other security best practices.


## [SAP HANA Environment Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/std-sap-hana-environment-setup.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-hana/prerequisites.html): Specialized knowledge and technical requirements to consider before setting up the environment.
- [Plan the deployment](https://docs.aws.amazon.com/sap/latest/sap-hana/planning-the-deployment.html): Review the compute, operating system, and AMI options, and information about storage configuration and network requirements.

### [Configure operating system](https://docs.aws.amazon.com/sap/latest/sap-hana/operating-system-configuration.html)

Follow the steps for configuring the operating system that you are using, and then set up the Amazon EBS volumes.

- [SLES 12/15](https://docs.aws.amazon.com/sap/latest/sap-hana/configure-operating-system-sles-for-sap-12.x.html)
- [RHEL 7/8/9](https://docs.aws.amazon.com/sap/latest/sap-hana/configure-operating-system-rhel-for-sap-7.x.html)

### [Configure storage](https://docs.aws.amazon.com/sap/latest/sap-hana/configure-storage.html)

This section includes instructions for configuring your storage for SAP HANA.

### [Storage architecture](https://docs.aws.amazon.com/sap/latest/sap-hana/architecture.html)

Disk layout diagrams for the environment setup.

- [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/sap/latest/sap-hana/architecture-fsx.html): The following architecture diagrams show different options for SAP HANA workloads using Amazon FSx for NetApp ONTAP.

### [Configure storage (EBS)](https://docs.aws.amazon.com/sap/latest/sap-hana/storage-configuration-ebs.html)

Follow the steps for configuring the Amazon EBS volumes that you are using.

- [Calculate Requirements](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-storage-config-ebs.html)
- [Storage Reference](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-storage-config-reference-layout.html)
- [Deploy Workloads](https://docs.aws.amazon.com/sap/latest/sap-hana/deployment-steps-using-the-aws-management-console.html): This topic explains how to assign EBS Volumes when launching an Amazon EC2 Instance.
- [Configure Fileystems](https://docs.aws.amazon.com/sap/latest/sap-hana/configure-storage-for-sap-hana.html)
- [Architecture](https://docs.aws.amazon.com/sap/latest/sap-hana/architecture-ebs.html): The following architecture diagrams show scale-up and scale-out environments for SAP HANA workloads using Amazon EBS volumes.

### [Configure storage (FSx for ONTAP)](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-amazon-fsx.html)

Deploy and operate SAP HANA systems on AWS with Amazon FSx for NetApp ONTAP.

- [Supported configurations](https://docs.aws.amazon.com/sap/latest/sap-hana/instances-sizing-sap-hana-amazon-fsx.html): The following rules and limitations are applicable for deploying SAP HANA on AWS with Amazon FSx for NetApp ONTAP.
- [Set up FSx for ONTAP file system](https://docs.aws.amazon.com/sap/latest/sap-hana/amazon-fsx-sap-hana.html): Before you create FSx for ONTAP file system, determine the total storage space you need for your SAP HANA workload.

### [Set up host](https://docs.aws.amazon.com/sap/latest/sap-hana/host-setup-fsx-sap-hana.html)

This section walks you through an example host setup for deploying SAP HANA scale-up and scale-out systems on AWS using Amazon FSx for NetApp ONTAP as the primary storage solution.

- [SAP HANA scale-up](https://docs.aws.amazon.com/sap/latest/sap-hana/fsx-host-scaleup.html): The following section is an example host setup for SAP HANA scale-up deployment with FSx for ONTAP.
- [SAP HANA scale-out](https://docs.aws.amazon.com/sap/latest/sap-hana/fsx-host-scaleout.html): The following section is an example host setup for SAP HANA scale-out with standby node on AWS using FSx for ONTAP as the primary storage solution.
- [Configure storage (EFS)](https://docs.aws.amazon.com/sap/latest/sap-hana/configure-nfs-for-scale-out-workloads.html)
- [Configure ENA Express](https://docs.aws.amazon.com/sap/latest/sap-hana/ena-express-sap-hana.html): SAP HANA scale-out systems require a minimum of 9 Gbps of single flow network bandwidth between nodes.
- [Post deployment Steps](https://docs.aws.amazon.com/sap/latest/sap-hana/post-deployment-steps.html): Tasks include setting up any organization-specific monitoring and directory-service connection, setting up a CloudWatch alarm.


## [SAP HANA on AWS Operations Guide](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-operations.html)

- [Introduction](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-intro.html): This guide provides best practices for operating SAP HANA systems that have been deployed on AWS.
- [Administration](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-administration.html): This section provides guidance on common administrative tasks required to operate an SAP HANA system, including information about starting, stopping, and cloning systems.
- [Automated patching](https://docs.aws.amazon.com/sap/latest/sap-hana/automated-patching.html): Maintaining the SAP HANA database software version keeps the database on with supported software versions, and enables you to stay updated with security fixes and software improvements.
- [Storage configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-storage-config.html)
- [Networking](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-networking.html): SAP HANA components communicate over the following logical network zones:
- [SAP support access](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-support.html): In some situations it may be necessary to allow an SAP support engineer to access your SAP HANA systems on AWS.
- [Security](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-security.html): Here are additional AWS security resources to help you achieve the level of security you require for your SAP HANA environment on AWS.

### [Architecture patterns for SAP HANA on AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-patterns.html)

This section provides information on architecture patterns that can be used as guidelines for deploying SAP HANA systems on AWS.

- [Single Region architecture patterns for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-patterns-single.html): Single Region architecture patterns help you avoid network latency as your SAP workload components are located in a close proximity within the same Region.
- [Multi-Region architecture patterns for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-patterns-multi.html): AWS Global Infrastructure spans across multiple Regions around the world and this footprint is constantly increasing.

### [High availability and disaster recovery](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-ha-dr.html)

AWS provides multiple options for performing disaster recovery and making your SAP HANA systems highly available.

- [SAP HANA system replication](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-ha-dr-hsr.html): SAP HANA system replication is a highly available solution provided by SAP for SAP HANA.
- [Testing](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-ha-dr-testing.html): This section covers failure scenarios for backup, testing guidance and considerations for high availability and disaster recovery solutions, and disaster recovery mock exercise.
- [Troubleshoot](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-ha-dr-troubleshoot.html): This section provides guidance for troubleshooting SAP HANA high availability deployments.
- [Appendix: Configuring Linux to recognize Ethernet devices for multiple network interfaces](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-appendix.html): Follow these steps to configure the Linux operating system to recognize and name the Ethernet devices associated with the new elastic network interfaces created for logical network separation, which were discussed earlier in this paper.
- [Document history](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-doc-history.html): Change history table for the SAP HANA operations guide.


## [SAP HANA Data Tiering on AWS Overview](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-data-tiering-overview.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-hana/data-tiering-prerequisites.html)
- [SAP Data Tiering](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-data-tiering.html): SAP data tiering is a data management strategy thatâs used to separate your data into different categories (hot, warm, and cold tiers) by various characteristics of the data.
- [Warm Data Tiering Options](https://docs.aws.amazon.com/sap/latest/sap-hana/warm-data-tiering-options.html): The following sections discuss the warm data tiering options you have on AWS.
- [Cold Data Tiering Options](https://docs.aws.amazon.com/sap/latest/sap-hana/cold-data-tiering-options.html): The following sections discuss cold data tiering options on AWS.
- [Document Revisions](https://docs.aws.amazon.com/sap/latest/sap-hana/data-tiering-document-revisions.html)


## [SAP on AWS HANA High Availability Configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-ha-configuration.html)

### [SUSE Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-sles-pacemaker.html)

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-planning.html)

This guide provides step-by-step instructions for configuring and deploying a high-availability SAP HANA cluster on Amazon Web Services (AWS) using SUSE Linux Enterprise Server for SAP Applications (SLES for SAP).

- [Setup Overview](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-setup-overview.html)
- [Vendor Support](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-references.html)
- [Concepts](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-concepts.html)
- [Automated Deployment](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-automation.html): You can set up a cluster manually using the instructions provided here.
- [Parameter Reference](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-parameters.html): The cluster setup uses parameters, including SID and System Number that are unique to your setup.
- [Architecture Diagrams](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-arch-diagrams.html)

### [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-prerequisites.html)

- [AWS Infrastructure Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-infra-setup.html): This section covers the one-time setup tasks required to prepare your AWS environment for the cluster deployment:
- [EC2 Instance Configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-ec2-configuration.html): Amazon EC2 instance settings can be applied using Infrastructure as Code or manually using AWS Command Line Interface or AWS Console.
- [Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-os-settings.html): This section outlines the required operating system configurations for SUSE Linux Enterprise Server for SAP (SLES for SAP) cluster nodes.

### [SAP HANA and Cluster Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-deployment-cluster.html)

- [SAP HANA Setup and HSR](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-hana-setup-hsr.html): Prepare SAP HANA for System Replication (HSR) by configuring parameters and creating required backups.
- [SAP HANA Service Control](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-hana-control.html): Modify how SAP HANA services are managed to enable cluster takeover and operation.
- [Cluster Node Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-cluster-node-setup.html): Establish cluster communication between nodes using Corosync and configure required authentication.
- [Cluster Configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-cluster-config.html): Bootstrap the cluster and configure all required cluster resources and constraints.
- [Client Connectivity](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-client-connectivity.html): For proper SAP HANA database connectivity:

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-operations.html)

- [Viewing the cluster state](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-ops-cluster-state.html): You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by SUSE.
- [Performing planned maintenance](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-ops-planned-maint.html): When performing maintenance on SAP HANA systems in a cluster environment, itâs important to understand how the cluster interacts with SAP HANA system replication.
- [Post-failure analysis and reset](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-ops-post-failure.html): A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster.
- [Alerting and monitoring](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-ops-alert-monitor.html): This section covers the following topics.
- [Testing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-testing.html): We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or HANA Upgrades that may impact operations.

### [RHEL Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-rhel-pacemaker.html)

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-planning.html)

This guide provides step-by-step instructions for configuring and deploying a high-availability SAP HANA cluster on Amazon Web Services (AWS) using Red Hat Linux Enterprise Server for SAP Applications (RHEL for SAP).

- [Setup Overview](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-setup-overview.html)
- [Vendor Support](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-references.html)
- [Concepts](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-concepts.html)
- [Automated Deployment](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-automation.html): You can set up a cluster manually using the instructions provided here.
- [Parameter Reference](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-parameters.html): The cluster setup uses parameters, including SID and System Number that are unique to your setup.
- [Architecture Diagrams](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-arch-diagrams.html)

### [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-prerequisites.html)

- [AWS Infrastructure Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-infra-setup.html): This section covers the one-time setup tasks required to prepare your AWS environment for the cluster deployment:
- [EC2 Instance Configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-ec2-configuration.html): Amazon EC2 instance settings can be applied using Infrastructure as Code or manually using AWS Command Line Interface or AWS Console.
- [Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-os-settings.html): This section outlines the required operating system configurations for Red Hat Enterprise Linux for SAP (RHEL for SAP) cluster nodes.

### [SAP HANA and Cluster Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-deployment-cluster.html)

- [SAP HANA Setup and HSR](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-hana-setup-hsr.html): Prepare SAP HANA for System Replication (HSR) by configuring parameters and creating required backups.
- [SAP HANA Service Control](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-hana-control.html): Modify how SAP HANA services are managed to enable cluster takeover and operation.
- [Cluster Node Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-cluster-node-setup.html): Establish cluster communication between nodes using Corosync and configure required authentication.
- [Cluster Configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-cluster-config.html): Bootstrap the cluster and configure all required cluster resources and constraints.
- [Client Connectivity](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-client-connectivity.html): For proper SAP HANA database connectivity:

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-operations.html)

- [Viewing the cluster state](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-ops-cluster-state.html)
- [Performing planned maintenance](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-ops-planned-maint.html): When performing maintenance on SAP HANA systems in a cluster environment, itâs important to understand how the cluster interacts with SAP HANA system replication.
- [Post-failure analysis and reset](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-ops-post-failure.html): A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster.
- [Alerting and monitoring](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-ops-alert-monitor.html): This section covers the following topics.
- [Testing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-testing.html): We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or HANA Upgrades that may impact operations.

### [Overlay IP Address Routing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-ha-overlay-ip.html)

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the Amazon Web Services Cloud.

- [SAP on AWS High Availability Setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-sap-on-aws-high-availability-setup.html): SAP customers can fully realize the benefit of running mission-critical SAP workloads by building reliable, fault-tolerant, and highly available systems in the AWS Cloud depending on the operating system and database.

### [Overlay IP Routing using AWS Transit Gateway](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-overlay-ip-routing-using-aws-transit-gateway.html)

With Transit Gateway, you use route table rules which allow the overlay IP address to communicate to the SAP instance without having to configure any additional components, like a Network Load Balancer or Amazon Route 53.

- [Configuration Steps for AWS Transit Gateway](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-configuration-steps-for-aws-transit-gateway.html): This section includes high-level steps necessary to understand overlay IP address configuration for this scenario.

### [Overlay IP Routing with Network Load Balancer](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-overlay-ip-routing-with-network-load-balancer.html)

If you do not use Amazon Route 53 or AWS Transit Gateway, you can use Network Load Balancer for accessing the overlay IP address externally.

- [Configuration Steps for Network Load Balancer](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-configuration-steps-for-network-load-balancer.html): Use the following instructions to set up the Network Load Balancer to access the overlay IP address.
- [Additional Implementation Notes](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-oip-additional-implementation-notes.html)
