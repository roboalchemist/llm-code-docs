# Source: https://docs.aws.amazon.com/sap/latest/sap-netweaver/llms.txt

# SAP NetWeaver on AWS SAP NetWeaver Guides

> Discusses architectural considerations and configuration steps for setting up an environment to host a standard, singleâAvailability Zone installation of SAP NetWeaver on the AWS Cloud.

- [Home](https://docs.aws.amazon.com/sap/latest/sap-netweaver/welcome.html)
- [Migration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/migrate-sap-netweaver.html)

## [Setup for Linux](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-netweaver-linux-setup.html)

- [Planning and Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-dep-planning-and-prereqs.html)
- [AWS Resource Selection and Configuration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-resource-and-config.html)
- [Launch and Setup Instance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-os-setup.html)


## [Setup for Windows](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-netweaver-windows-guide.html)

### [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-prerequisites.html)

- [Recommended Reading](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-recommended-reading.html): We also recommend reading these overview and best practice guides:
- [Technical Requirements](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-technical-requirements.html)

### [Planning the Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-planning-the-deployment.html)

Plan your SAP system landscape according to the SAP Master Guide for your version of SAP NetWeaver and your combination of operating system and database.

- [Select the Region](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-select-region.html): In choosing the Region for deployment, youâll need to consider some key factors.

### [Architecture Options](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-architecture-options.html)

- [Standard System Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-standard-system-deployment.html): Standard system or single host installation: all main instances of SAP NetWeaver (ASCS/SCS, database, and PAS) run on one Amazon EC2 instance.
- [Distributed System Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-distributed-system-deployment.html): Distributed system: every instance of SAP NetWeaver (ASCS/SCS, database, PAS, and optionally AAS) can run on a separate Amazon EC2 instance.
- [High Availability System Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-high-availability-system-deployment.html): High availability (HA) system: used for business-critical applications.
- [Security and Compliance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-security-and-compliance.html): These additional AWS security resources can help you achieve the level of security that you require for your SAP NetWeaver environment on AWS:
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-sizing.html): One of the first points to consider is whether this deployment is a completely new project (greenfield) or a migration.
- [Operating System](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-operating-system.html): If you plan on using Windows other than via Amazon EC2 for Windows Server, then ensure that you have the appropriate licenses and tenancy type selected.
- [Compute](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-compute-1.html): AWS has certified multiple instance families of various sizes for running SAP NetWeaver workloads.
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-storage-1.html): Refer to the sizing section for resources on SAPâs standard recommendations.
- [Network](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-network-1.html): Ensure that you have your network constructs set up to deploy resources related to SAP NetWeaver.

### [Deployment Steps](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-deployment-steps.html)

- [Step 1: Prepare your AWS Account](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-1-prepare-your-aws-account.html): In this example, we step through setting up a sample environment for the installation, which includes a public subnet for RDP and SSH access via the internet.
- [Step 2: Prepare Each EC2 Instance for SAP Installation](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-2-prepare-each-ec2-instance-for-sap-installation.html)
- [Step 3: Create Amazon FSx Volumes](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-3-create-amazon-fsx-volumes.html)
- [Step 4: Prepare and Run the SAP Installation Prerequisites Check](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-4-prepare-and-run-the-sap-installation-prerequisites-check.html)
- [Step 5: Install SAP NetWeaver on Amazon EC2](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-5-install-sap-netweaver-on-amazon-ec2.html): You are now ready to install SAP NetWeaver on this EC2 instance using the downloaded software.

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-operations.html)

- [Tagging AWS Resources](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-tagging-aws-resources.html): A tag is a label that you assign to an AWS resource.
- [Monitoring](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-monitoring.html): AWS provides multiple native services to monitor and manage your SAP environment.
- [Backup and Restore](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-backup-and-restore.html)
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-storage-2.html): The storage services we use across this guide are:
- [Operating System Maintenance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-operating-system-maintenance.html): In general, operating system maintenance across large numbers of EC2 instances can be managed by:
- [High Availability](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-high-availability.html): After your HA cluster is deployed and configured successfully on AWS, the operation of the HA software still follows the third-party software interface.
- [Disaster Recovery](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-disaster-recovery-1.html)
- [Compute](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-compute-2.html): EBS volumes are exposed as NVMe block devices onÂ Nitro-based instances.
- [Cost Optimization](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-cost-optimization.html): We recommend that you make cost optimization an on-going process.
- [Automation](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-automation.html)
- [Support](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-support.html): To get help from SAP, SAP requires, at the minimum, a business support agreement with AWS.
- [Additional Reading](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-additional-reading.html)
- [Document history](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-document-revisions.html)


## [SQL Server setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sql-server-sap-guide.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/prerequisites-sap-sql.html)

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-netweaver/planning.html)

- [Architecture Options](https://docs.aws.amazon.com/sap/latest/sap-netweaver/architecture-options.html): SAP NetWeaver applications based on SQL Server can be installed in three different ways:
- [Deployment Options](https://docs.aws.amazon.com/sap/latest/sap-netweaver/deployment-options.html): Microsoft SQL Server 2008 R2 or later is supported for SAP applications on AWS.
- [Security](https://docs.aws.amazon.com/sap/latest/sap-netweaver/security.html): AWS provides several security capabilities and services to securely run your SAP applications on AWS platform.
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sizing.html): SAP Quick Sizer is generally used to size the SAP environment for new implementations.
- [Operating System](https://docs.aws.amazon.com/sap/latest/sap-netweaver/operating-system.html): SAP applications based on SQL Server are supported only on Windows operating system.
- [Compute](https://docs.aws.amazon.com/sap/latest/sap-netweaver/compute.html): AWS provides multiple SAP certified Amazon EC2 instances.
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/storage.html): The following table lists the main directories for SQL Server database.
- [Network](https://docs.aws.amazon.com/sap/latest/sap-netweaver/network.html): Ensure that your network constructs are set up to deploy resources related to SAP NetWeaver.
- [Business Continuity](https://docs.aws.amazon.com/sap/latest/sap-netweaver/business-continuity.html): We recommend that you architect your business-critical applications to be fault tolerant.

### [Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/deployment.html)

- [Windows EC2 Instance Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/windows-ec2-instance-deployment.html): Deciding the right storage layout is important to ensure you are able to meet required IO.
- [SQL Server Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sql-server-deployment.html): Follow the instructions in the appropriate SAP installation guide for your version of SAP NetWeaver and your combination of operating system and database.
- [SQL Server Deployment for High Availability](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.html)

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/operations.html)

This section provides information on AWS services that help you with day-to-day operations of your SQL Server database for SAP applications.

- [Monitoring](https://docs.aws.amazon.com/sap/latest/sap-netweaver/monitoring.html): AWS provides multiple services to monitor and manage your infrastructure and applications on AWS.
- [Backup and Recovery](https://docs.aws.amazon.com/sap/latest/sap-netweaver/backup-and-recovery.html): You need to regularly back up your operating system and database to recover them in case of any failure.
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/storage-1.html): The following list includes Amazon storage services included in this guide.
- [Operating System Maintenance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/operating-system-maintenance.html): In general, operating system maintenance across large estates of EC2 instances can be managed by:
- [Business Continuity](https://docs.aws.amazon.com/sap/latest/sap-netweaver/business-continuity-1.html): AWS recommends that you periodically schedule business continuity process validations by executing disaster recovery (DR) tests.
- [Support](https://docs.aws.amazon.com/sap/latest/sap-netweaver/support.html): SAP requires customers to have a minimum of an AWS Business Support plan with AWS.
- [Cost Optimization](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cost-optimization.html): Resources (CPU, Memory, additional application servers, system copies for different tests/validations, and so on) require SAP landscape changes over time.
- [FAQ](https://docs.aws.amazon.com/sap/latest/sap-netweaver/faq-sap-sql.html): Q.
- [Document Revisions](https://docs.aws.amazon.com/sap/latest/sap-netweaver/document-revisions-sap-sql.html)


## [NetWeaver High availability (ASCS)](https://docs.aws.amazon.com/sap/latest/sap-netweaver/netweaver-ha-ascs.html)

### [SLES Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-on-aws-sles-pacemaker.html)

This topic applies to SUSE Linux Enterprise Server (SLES) operating system for SAP NetWeaver applications on AWS cloud.

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-planning.html)

This section covers the following topics.

- [Setup Overview](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-setup-overview.html): You must meet the following prerequisites before commencing setup.
- [Deployment Guidance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-references.html): The following section details the documentation and deployment guidance from SUSE.
- [Concepts](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-concepts.html): This section covers AWS, SAP, and SUSE concepts.
- [Parameter Reference](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-parameters.html): The cluster setup relies on the following parameters.
- [Architecture diagrams](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sles-netweaver-ha-diagrams.html): This guide covers two architectures for SAP cluster solutions on SLES for SAP â simple-mount and classic (previous standard).

### [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-prerequisites.html)

- [AWS Infrastructure Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-infra-setup.html): This section covers the one-time setup tasks required to prepare your AWS environment for the cluster deployment:
- [EC2 Instance Configuration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-ec2-configuration.html): Amazon EC2 instance settings can be applied using Infrastructure as Code or manually using AWS Command Line Interface or AWS Console.
- [Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-os-settings.html): This section outlines the required operating system configurations for SUSE Linux Enterprise Server for SAP (SLES for SAP) cluster nodes.

### [SAP ASCS and Cluster Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-sles-setup.html)

This section covers the following topics.

- [SAP Shared File Systems](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-shared-filesystems-nw-sles.html)
- [Check IP availability and resolution](https://docs.aws.amazon.com/sap/latest/sap-netweaver/check-ip-availability-resolution-nw-sles.html)
- [Install SAP](https://docs.aws.amazon.com/sap/latest/sap-netweaver/install-sap-nw-sles.html): The following topics provide information about installing SAP on AWS Cloud in a highly available cluster.
- [Configure SAP for Cluster Control](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-ascs-service-control-nw-sles.html): Modify SAP service configurations, user permissions, and system integration settings to enable proper cluster control of ASCS and ERS instances.
- [Cluster Node Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-node-setup-nw-sles.html): Establish cluster communication between nodes using Corosync and configure required authentication.
- [Cluster Configuration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-config-nw-sles.html): The following sections provide details on the resources, groups and constraints necessary to ensure high availability of SAP Central Services.

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sles-netweaver-ha-operations.html)

This section covers the following topics.

- [Viewing the cluster state](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-state-nw-sles.html): You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by SUSE.
- [Performing planned maintenance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/planned-maintenance-nw-sles.html): The cluster connector is designed to integrate the cluster with SAP start framework (sapstartsrv), including the rolling kernel switch (RKS) awareness.
- [Post-failure analysis and reset](https://docs.aws.amazon.com/sap/latest/sap-netweaver/analysis-reset-nw-sles.html): A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster.
- [Alerting and monitoring](https://docs.aws.amazon.com/sap/latest/sap-netweaver/alerting-monitoring-nw-sles.html): This section covers the following topics.
- [Testing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/testing-nw-sles.html): We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or SAP kernel updates that may impact operations.

### [RHEL Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-on-aws-rhel-pacemaker.html)

This topic applies to Red Hat Enterprise Linux (RHEL) operating system for SAP NetWeaver applications on AWS cloud.

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-planning.html)

This section covers the following topics.

- [Setup Overview](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-setup-overview.html): You must meet the following prerequisites before commencing setup.
- [Vendor Support](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-references.html): The following section details the documentation and deployment guidance from Red Hat.
- [Concepts](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-concepts.html): This section covers AWS, SAP, and Red Hat concepts.
- [Parameter Reference](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-parameters.html): The cluster setup relies on the following parameters.
- [Architecture diagrams](https://docs.aws.amazon.com/sap/latest/sap-netweaver/rhel-netweaver-ha-diagrams.html): This guide covers two architectures for SAP cluster solutions on RHEL for SAP â simple-mount and classic (previous standard).

### [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-prerequisites.html)

- [AWS Infrastructure Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-infra-setup.html): This section covers the one-time setup tasks required to prepare your AWS environment for the cluster deployment:
- [EC2 Instance Configuration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-ec2-configuration.html): Amazon EC2 instance settings can be applied using Infrastructure as Code or manually using AWS Command Line Interface or AWS Console.
- [Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-os-settings.html): This section outlines the required operating system configurations for Red Hat Enterprise Linux for SAP (RHEL for SAP) cluster nodes.

### [SAP ASCS and Cluster Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-pacemaker-rhel-setup.html)

This section covers the following topics.

- [SAP Shared File Systems](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-shared-filesystems-nw-rhel.html)
- [Check IP availability and resolution](https://docs.aws.amazon.com/sap/latest/sap-netweaver/check-ip-availability-resolution-nw-rhel.html)
- [Install SAP](https://docs.aws.amazon.com/sap/latest/sap-netweaver/install-sap-nw-rhel.html): The following topics provide information about installing SAP on AWS Cloud in a highly available cluster.
- [Configure SAP for Cluster Control](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-ascs-service-control-nw-rhel.html): Modify SAP service configurations, user permissions, and system integration settings to enable proper cluster control of ASCS and ERS instances.
- [Cluster Node Setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-node-setup-nw-rhel.html): Establish cluster communication between nodes using Corosync and configure required authentication.
- [Cluster Configuration](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-config-nw-rhel.html): The following sections provide details on the resources, groups and constraints necessary to ensure high availability of SAP Central Services.

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/rhel-netweaver-ha-operations.html)

This section covers the following topics.

- [Viewing the cluster state](https://docs.aws.amazon.com/sap/latest/sap-netweaver/cluster-state-nw-rhel.html): You can view the state of the cluster in two ways - based on your operating system or with a web based console provided by Red Hat.
- [Performing planned maintenance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/planned-maintenance-nw-rhel.html): The cluster connector is designed to integrate the cluster with SAP start framework (sapstartsrv), including the rolling kernel switch (RKS) awareness.
- [Post-failure analysis and reset](https://docs.aws.amazon.com/sap/latest/sap-netweaver/analysis-reset-nw-rhel.html): A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster.
- [Alerting and monitoring](https://docs.aws.amazon.com/sap/latest/sap-netweaver/alerting-monitoring-nw-rhel.html): This section covers the following topics.
- [Testing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/testing-nw-rhel.html): We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or SAP kernel updates that may impact operations.


## [Oracle database](https://docs.aws.amazon.com/sap/latest/sap-netweaver/orc-sap-nw-lx.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/prereq-orc-sap-nw-lx.html): We recommend familiarizing yourself with these guides:

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-netweaver/planning-orc-sap-nw-lx.html)

Plan your SAP system landscape according to the SAP Master Guide for your version of SAP NetWeaver for Linux OS and Oracle database.

- [Deployment options](https://docs.aws.amazon.com/sap/latest/sap-netweaver/deploy-options-orc-sap-nw-lx.html): To install Oracle for SAP NetWeaver, you have four deployment options:
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sizing-orc-sap-nw-lx.html): Sizing applies to three key areas - compute, network, and storage.
- [Amazon Machine Image (AMI)](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ami-orc-sap-nw-lx.html): You can deploy your SAP Oracle workload on Oracle Enterprise Linux 6.4 or later.
- [Security and compliance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sec-orc-sap-nw-lx.html): The following are additional AWS security resources to help you achieve the optimum level of security for your SAP NetWeaver environment on AWS:
- [Storage for Oracle](https://docs.aws.amazon.com/sap/latest/sap-netweaver/storeorc-orc-sap-nw-lx.html): This section describes the key considerations for designing storage layout of Oracle for SAP NetWeaver on AWS.

### [Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/deployment-orc-sap-nw-lx.html)

- [Standalone deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/standalone-dep-orc-sap-nw-lx.html): In this example, we set up a sample environment for installation.
- [HA/DR deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ha-dr-dep-orc-sap-nw-lx.html)

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ops-orc-sap-nw-lx.html)

- [Compute & storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/compstore-orc-sap-nw-lx.html)
- [Backup & restore](https://docs.aws.amazon.com/sap/latest/sap-netweaver/backres-orc-sap-nw-lx.html)
- [HA/DR operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/hadrops-orc-sap-nw-lx.html)
- [Resources](https://docs.aws.amazon.com/sap/latest/sap-netweaver/resources-orc-sap-nw-lx.html): SAP on AWS customers have the flexibility to deploy SAP Oracle database on the scalable, on-demand Amazon EC2 platform in a highly available manner.
- [Document revisions](https://docs.aws.amazon.com/sap/latest/sap-netweaver/docrev-orc-sap-nw-lx.html)


## [SAP ASE database](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ase-linux.html)

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ase-planning.html)

Plan your SAP system landscape according to the SAP Master Guide for your version of SAP system running ASE on Linux.

- [Deployment options](https://docs.aws.amazon.com/sap/latest/sap-netweaver/deploy-options-sap-ase.html): To install SAP ASE for SAP NetWeaver, you have four deployment options:
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sizing-sap-ase.html): Sizing applies to three key areas - compute, network, and storage.
- [Operating system](https://docs.aws.amazon.com/sap/latest/sap-netweaver/os-sap-ase.html): You can deploy your SAP ASE workload on SLES, SLES for SAP, RHEL for SAP with High Availability and Update Services (RHEL for SAP with HA and US) or RHEL for SAP Solutions.
- [Security and compliance](https://docs.aws.amazon.com/sap/latest/sap-netweaver/security-sap-ase.html): The following are additional AWS security resources to help you achieve the optimum level of security for your SAP NetWeaver environment on AWS:

### [Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ase-deployment.html)

This section provides information about example deployments.

- [Standalone deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/standalone-sap-ase.html): In this example, we set up a sample environment for installation.
- [High availability disaster recovery deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/hadr-sap-ase.html): Create an additional Amazon EC2 instance and perform the installation in a secondary Availability Zone.

### [Operations](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ase-operations.html)

- [Compute & storage](https://docs.aws.amazon.com/sap/latest/sap-netweaver/compute-storage-sap-ase.html)
- [Backup & restore](https://docs.aws.amazon.com/sap/latest/sap-netweaver/backup-restore-sap-ase.html)
- [Disaster recovery](https://docs.aws.amazon.com/sap/latest/sap-netweaver/dr-operations-sap-ase.html): See Disaster recovery deployment to learn about disaster recovery for your SAP ASE database.
- [Resources](https://docs.aws.amazon.com/sap/latest/sap-netweaver/ase-resources.html): SAP on AWS customers have the flexibility to deploy SAP ASE database on the scalable, on-demand Amazon EC2 platform in a highly available manner.


## [Automation](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-nw-automation.html)

### [Automated SAP installation](https://docs.aws.amazon.com/sap/latest/sap-netweaver/automation-installation.html)

Automated SAP installation

- [Automated SAP installation architecture](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-install-architecture.html): The example architecture shown in the diagram below uses a centralized AWS account that stores the AWS Systems Manager document (SSM document).
- [Automated SAP NetWeaver on AWS installation prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-installation-prerequisites.html): In addition to the prerequisites described in the Automation prerequisites section of this guide, verify the following prerequisites that are specific to automated SAP installation:
- [Configuring automated SAP installation](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-installation-configuring.html): The sections below contain detailed instructions on how to configure automated SAP NetWeaver on AWS installation.

### [Automated operating system patching](https://docs.aws.amazon.com/sap/latest/sap-netweaver/automation-os-patching.html)

Operating system patching

- [Automated operating system patching architecture](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-architecture.html): The diagram below highlights the AWS services that you can use to set up automated operating system patching and optional notifications on the patch status using Amazon Simple Notification Service (Amazon SNS).
- [Automated operating system patching prerequisites](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-prerequisites.html): In addition to the prerequisites described in the Automation prerequisites section of this guide, verify the following prerequisites that are specific to automated operating system patching:

### [Configuring automated operating system patching](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-configuring.html)

The sections below contain detailed instructions on how to configure automated operating system patching.

### [Configure patch baselines](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-baselines.html)

Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches.

- [Predefined patch baselines](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-predefined-baselines.html): Patch manager provides predefined patch baselines for each of the supported operating systems.
- [Custom patch baselines](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-custom-baselines.html): Unlike predefined patch baselines, custom patch baselines do not have default patch approvals and compliance levels.
- [Create patch groups](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-groups.html): You can use patch groups to organize instances for patching.
- [Applying patches](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-applying.html): After you have created the patch baseline and tagged your Amazon EC2 instances to the patch group, you can apply patches.
- [Monitoring](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-monitoring.html): You can view Patch Manager output after each patch is run.
- [Private and local repositories](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-private-repo.html): If you would like to manage your operating system repository locally, either within your VPC on AWS or an on-premises data center, without using an outbound internet connection for your instance, you can use a private or local repository.
- [Alternative tools for patching](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-alt-tools.html): In addition to AWS Systems Manager, there are other automated patching tools that you might use, which are listed below.
- [Considerations for multiple accounts](https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-multi-account.html): When you run SAP workloads in AWS, you must consider an AWS account strategy that meets the security controls of your organization.
- [Troubleshooting](https://docs.aws.amazon.com/sap/latest/sap-netweaver/automation-troubleshooting.html): Automation troubleshooting
