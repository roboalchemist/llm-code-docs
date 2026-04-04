# Source: https://docs.aws.amazon.com/sap/latest/sap-businessobjects/llms.txt

# SAP BusinessObjects on AWS SAP BusinessObjects Guides

> Provides information about implementing SAP BusinessObjects solutions on AWS.

- [Home](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/welcome.html)

## [SAP BOBI Platform on AWS Deployment and Operations Guide for Linux](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-ops-guide.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-prerequisites.html): Before you start implementing your SAP BOBI Platform systems, we recommend that you review these prerequisites to ensure there are minimal interruptions and delays.

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-planning.html)

The following topics are important for planning the SAP BOBI Platform in AWS Cloud.

- [Choosing a Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-choosing-a-region.html): When choosing which AWS Region to deploy your SAP environment in you should consider the following topics:
- [Choosing an Availability Zone](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-choosing-an-availability-zone.html): No special considerations are required when choosing an Availability Zone for your SAP deployment on AWS.
- [Architecture Options](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-architecture-options.html): The server-side architecture of SAP BOBI Platform consists of five tiers: web, management, storage, processing, and data. (For details, see the administratorâs guide on the SAP BusinessObjects Business Intelligence Platform website).
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-sizing.html): At a high level, BOBI platform sizing is a two-step process.
- [High Availability (HA) and Disaster Recovery (DR)](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-high-availability-ha-and-disaster-recovery-dr.html): If you require a highly available BOBI environment, then it critical to design the HA and DR environment that can support the recovery time objective (RTO) and recovery point objective (RPO) that your business teams have established.
- [Security & Compliance](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-security-compliance.html): The following AWS security resources help you achieve the level of security you require for your SAP NetWeaver environment on AWS:
- [Operating System](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-operating-system.html): Customers can choose to bring their license subscriptions or use AWS Marketplace to purchase licenses.
- [Compute](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-compute.html): AWS has certified multiple instance families with different sizes to run SAP workloads.
- [Network](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-network.html): Ensure that you have your network constructs set up to deploy resources related to your SAP workload.
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-storage.html): The SAP BOBI Platform uses the following AWS storage services:
- [Deployment](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-deployment.html): In this deployment, we will provision an Amazon EC2 instance for installing the SAP application servers and the CMS database (if you are using database on EC2).
- [Operations](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-operations.html)
- [Support](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-support.html): To get help from SAP, SAP and AWS requires a business support agreement on AWS.
- [Document Revisions](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-document-revisions.html)


## [SAP BOBI Platform on AWS Deployment and Operations Guide for Windows](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-ops-guide.html)

- [Prerequisites](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-prerequisites.html): Before you start implementing your SAP BOBI Platform systems, we recommend that you review these prerequisites to ensure there are minimal interruptions and delays.

### [Planning](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-planning.html)

The following topics are important for planning the SAP BOBI Platform in AWS Cloud.

- [Choosing a Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-choosing-a-region.html): When choosing which AWS Region to deploy your SAP environment in you should consider the following topics:
- [Choosing an Availability Zone](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-choosing-an-availability-zone.html): No special considerations are required when choosing an Availability Zone for your SAP deployment on AWS.
- [Architecture Options](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-architecture-options.html): The server-side architecture of SAP BOBI Platform consists of five tiers: web, management, storage, processing, and data. (For details, see the administratorâs guide on the SAP BusinessObjects Business Intelligence Platform website).
- [Storage](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-storage-plan.html): See the Sizing section for resources on SAPâs standard recommendations.
- [Sizing](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-sizing.html): At a high level, BOBI platform sizing is a two-step process.
- [High Availability (HA) and Disaster Recovery (DR)](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-high-availability-ha-and-disaster-recovery-dr.html): If you require a highly available BOBI environment, then it critical to design the HA and DR environment that can support the recovery time objective (RTO) and recovery point objective (RPO) that your business teams have established.
- [Security & Compliance](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-security-compliance.html): The following AWS security resources help you achieve the level of security you require for your SAP NetWeaver environment on AWS:
- [Operating System](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-operating-system.html): If you plan on using Windows other than via Amazon EC2 for Windows Server, then ensure you have the appropriate licenses in place and the appropriate tenancy type selected.
- [Compute](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-compute.html): AWS has certified multiple instance families with different sizes to run SAP workloads.
- [Network](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-network.html): Ensure that you have your network constructs set up to deploy resources related to your SAP workload.
- [Storage Services](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-storage-services.html): The SAP BOBI Platform uses the following AWS storage services:
- [Deployment](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-deployment.html): In this deployment, we will provision an Amazon EC2 instance for installing the SAP application servers and the CMS database (if you are using database on EC2).
- [Operations](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-operations.html)
- [Support](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-support.html): To get help from SAP, SAP and AWS requires a business support agreement on AWS.
- [Document Revisions](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-document-revisions.html)


## [SAP BusinessObjects BI Platform HA/DR Guide for Linux](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/sap-bobj-ha-dr-linux.html)

- [Prerequisite Knowledge](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-prerequisites.html)

### [High Availability](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-high-availability.html)

HA design for a software application protects single points of failure (SPOFs).

- [HA for SAP BusinessObjects BI Platform on AWS](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-ha-for-sap-bobj.html): In this guide, weâll provide an example HA architecture that closely resembles a typical on-premises installation, and weâll also show how AWS features in combination with SAP BusinessObjects BI Platform installation options support an HA solution that extends beyond a single data center.
- [Planning the Deployment in a Primary Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-planning-primary.html): Good planning is a key step in ensuring a successful HA deployment for SAP BusinessObjects BI Platform on AWS.
- [Installing SAP BusinessObjects BI Platform for HA](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-installing-for-ha.html)
- [HA for SAP Data Services](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-ha-for-sap-data-services.html): The HA architecture of SAP Data Services is very similar to the HA architecture of SAP BusinessObjects BI Platform.

### [Disaster Recovery](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-disaster-recovery.html)

The DR approach you take for SAP BusinessObjects BI Platform, as for any other enterprise application, depends on your RTO and RPO requirements.

- [DR for SAP BusinessObjects BI Platform on AWS](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-dr-for-sap-bobj.html): DR for SAP BusinessObjects BI Platform on the AWS Cloud refers to a scenario in which the primary AWS Region where SAP BusinessObjects BI Platform application is running is unavailable.
- [Planning the Deployment in the DR Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-planning-dr.html): Planning the deployment of a DR system is critical.
- [Installing SAP BusinessObjects BI Platform in the DR Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-installing-sap-bobj-dr.html): When you have selected the DR region, follow the steps in the Preparing the OS section earlier in this guide to build SAP BusinessObjects BI Platform EC2 instances in that region.
- [DR for SAP Data Services](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-dr-for-sap-data-services.html): As described earlier in the HA for SAP Data Services section, you can install SAP Data Services on either an existing SAP BusinessObjects BI Platform node or on SAP BusinessObjects Information Platform Services (IPS).
- [Summary](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-summary.html): SAP customers can now deploy SAP BusinessObjects BI Platform solution and landscapes on the scalable, on-demand Amazon EC2 platform in a highly available manner without having to invest in costly capital expenditures for the underlying infrastructure.
- [Additional Tips](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-appendix-c.html)


## [SAP BusinessObjects BI Platform HA/DR Guide for Windows](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/sap-bobi-ha-dr-win.html)

- [Prerequisite Knowledge](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-prerequisites.html)

### [High Availability](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-high-availability.html)

HA design for a software application protects single points of failure (SPOFs).

- [HA for SAP BusinessObjects BI Platform on AWS](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-ha-for-sap-bobi.html): In this guide, weâll provide an example HA architecture that closely resembles a typical on-premises installation, and weâll also show how AWS features in combination with SAP BusinessObjects BI Platform installation options support an HA solution that extends beyond a single data center.
- [Planning the Deployment in a Primary Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-planning-primary.html): Good planning is a key step in ensuring a successful HA deployment for SAP BusinessObjects BI Platform on AWS.
- [Installing SAP BusinessObjects BI Platform for HA](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-installing-for-ha.html)
- [HA for SAP Data Services](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-ha-for-sap-data-services.html): The HA architecture of SAP Data Services is very similar to the HA architecture of SAP BusinessObjects BI Platform.

### [Disaster Recovery](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-disaster-recovery.html)

The DR approach you take for SAP BusinessObjects BI Platform, as for any other enterprise application, depends on your RTO and RPO requirements.

- [DR for SAP BusinessObjects BI Platform on AWS](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-dr-for-sap-bobi.html): DR for SAP BusinessObjects BI Platform on the AWS Cloud refers to a scenario in which the primary AWS Region where SAP BusinessObjects BI Platform application is running is unavailable.
- [Planning the Deployment in the DR Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-planning-dr.html): Planning the deployment of a DR system is critical.
- [Installing SAP BusinessObjects BI Platform in the DR Region](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-installing-sap-bobi-dr.html): When you have selected the DR region, follow the steps in the Preparing the OS section earlier in this guide to build SAP BusinessObjects BI Platform EC2 instances in that region.
- [DR for SAP Data Services](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-dr-for-sap-data-services.html): As described earlier in the HA for SAP Data Services section, you can install SAP Data Services on either an existing SAP BusinessObjects BI Platform node or on SAP BusinessObjects Information Platform Services (IPS).
- [Summary](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-summary.html): SAP customers can now deploy SAP BusinessObjects BI Platform solution and landscapes on the scalable, on-demand Amazon EC2 platform in a highly available manner without having to invest in costly capital expenditures for the underlying infrastructure.
- [Additional Tips](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-appendix-c.html)
