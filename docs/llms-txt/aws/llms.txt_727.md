# Source: https://docs.aws.amazon.com/sap/latest/general/llms.txt

# General SAP Guides SAP Guides

> Provides additional information about implementing and configuring SAP solutions on AWS.

- [Home](https://docs.aws.amazon.com/sap/latest/general/welcome.html)
- [Cost estimation](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-pricing-guide.html)

## [Overview](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-overview.html)

- [AWS Overview](https://docs.aws.amazon.com/sap/latest/general/overview-aws.html): AWS offers a broad set of global, cloud-based services, including compute, storage, networking, Internet of Things (IoT), and many others.
- [SAP on AWS Overview](https://docs.aws.amazon.com/sap/latest/general/overview-sap-on-aws.html): AWS has been working with SAP since 2011 to help customers deploy and migrate their SAP applications to AWS, and SAP supports running the vast majority of available SAP applications on AWS.

### [SAP on AWS Planning](https://docs.aws.amazon.com/sap/latest/general/overview-sap-planning.html)

If you are an experienced SAP Basis or SAP NetWeaver administrator, there are a number of AWS-specific considerations relating to compute configurations, storage, security, management, and monitoring that will help you get the most out of your SAP environment on AWS.

### [SAProuter and SAP Solution Manager](https://docs.aws.amazon.com/sap/latest/general/overview-router-solman.html)

The following sections describe options for SAProuter and SAP Solution Manager when running SAP solutions on AWS.

- [For SAP Hybrid AWS Architecture](https://docs.aws.amazon.com/sap/latest/general/overview-router-hybrid.html): When using AWS as an extension of your IT infrastructure, you can use your existing SAP Solution Manager system and SAProuter that are running in your data center to manage SAP systems running on AWS within a VPC.
- [Document Revisions](https://docs.aws.amazon.com/sap/latest/general/overview-revisions.html): Change history table for the SAP overview and planning guide.


## [Amazon EC2 instance types](https://docs.aws.amazon.com/sap/latest/general/ec2-instance-types-sap.html)

- [SAP NetWeaver supported instances](https://docs.aws.amazon.com/sap/latest/general/sap-netweaver-aws-ec2.html): Previous generation Amazon EC2 instances for SAP NetWeaver are fully supported and these instance types retain the same features and functionality.
- [SAP HANA certified and non-certified instances](https://docs.aws.amazon.com/sap/latest/general/sap-hana-aws-ec2.html): AWS has worked closely with SAP to test and certify Amazon EC2 instance types for SAP on AWS solutions.
- [SAP Business One certified instances, version for SAP HANA](https://docs.aws.amazon.com/sap/latest/general/sap-b1-aws-ec2.html): AWS has worked closely with SAP to test and certify Amazon EC2 instance types for SAP on AWS solutions.
- [Document history](https://docs.aws.amazon.com/sap/latest/general/doc-history-ec2-sap.html)


## [AWS Data Provider](https://docs.aws.amazon.com/sap/latest/general/aws-data-provider.html)

- [Introduction](https://docs.aws.amazon.com/sap/latest/general/data-provider-intro.html): Many organizations of all sizes are choosing to host key SAP systems in the Amazon Web Services Cloud.
- [Technical Requirements](https://docs.aws.amazon.com/sap/latest/general/data-provider-req.html): Before creating an SAP instance, ensure that the following technical requirements are met.

### [DataProvider 4.3](https://docs.aws.amazon.com/sap/latest/general/dp4.3.html)

If you are new to AWS Data Provider for SAP, see Installing DataProvider 4.3.

- [Installing DataProvider 4.3](https://docs.aws.amazon.com/sap/latest/general/data-provider-installation.html): The AWS Data Provider for SAP runs as a service that automatically starts at boot and collects, aggregates, and exposes metrics to the SAP host agent.
- [Updating to DataProvider 4.3](https://docs.aws.amazon.com/sap/latest/general/data-provider-update.html): If you have previously installed DataProvider 2.0 or 3.0 and want to update to DataProvider 4.3, you need to uninstall the running version first, and then install DataProvider 4.3.
- [Uninstalling older versions](https://docs.aws.amazon.com/sap/latest/general/uninstall-older-dp.html): Uninstalling the AWS Data Provider for SAP does not require SAP downtime and can be done online.
- [Troubleshooting](https://docs.aws.amazon.com/sap/latest/general/data-provider-troubleshooting.html): This section provides help to analyze installation problems.
- [Customizing the DataProvider](https://docs.aws.amazon.com/sap/latest/general/data-provider-customization.html): Some settings are hard coded in the AWS Data Provider for SAP.

### [Verification of monitoring](https://docs.aws.amazon.com/sap/latest/general/data-provider-verify-monitoring.html)

The AWS Data Provider for SAP exposes AWS-specific metrics through an XML page at http://localhost:8888/vhostmd of the given system.

- [Example of captured metrics](https://docs.aws.amazon.com/sap/latest/general/data-provider-example-metrics.html): This following show example metrics.
- [Version history](https://docs.aws.amazon.com/sap/latest/general/data-provider-version-history.html): Version 4.3.2 (August, 2023)


## [Architecture guidance](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)

- [Introduction](https://docs.aws.amazon.com/sap/latest/general/arch-guide-introduction.html): For decades, SAP customers protected SAP workloads on premise with two common patterns: high availability and disaster recovery.
- [Architecture guidelines and decisionsÂ ](https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html): This section will provides a brief overview of the AWS services typically used for SAP workloads and some of the key points to understand when designing your architecture for hosting SAP on AWS.

### [Architecture patterns](https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-patterns.html)

In this section, we elaborate on the architecture patterns that you can select based on your availability and recovery requirements.

- [Failure scenarios](https://docs.aws.amazon.com/sap/latest/general/arch-guide-failure-scenarios.html): For the failure scenarios below, the primary consideration is the physical unavailability of the compute and/or storage capacity within the Availability Zones.

### [Patterns](https://docs.aws.amazon.com/sap/latest/general/arch-guide-patterns.html)

In this section, we examine the architecture patterns available to handle the failure scenarios detailed above.

- [Single Region architecture patterns](https://docs.aws.amazon.com/sap/latest/general/arch-guide-single-region-architecture-patterns.html): Select a single Region pattern if:
- [Multi-Region Architecture Patterns](https://docs.aws.amazon.com/sap/latest/general/arch-guide-multi-region-architecture-patterns.html): You should select a multi-Region architecture if you require the following:
- [Summary](https://docs.aws.amazon.com/sap/latest/general/arch-guide-summary.html): The table below summarizes the patterns and their key characteristics.

### [Microsoft SQL](https://docs.aws.amazon.com/sap/latest/general/patterns-microsoft.html)

Detailed information about availability and reliability patterns for SAP on Microsoft SQL for SAP on AWS.

- [Single Region patterns](https://docs.aws.amazon.com/sap/latest/general/single-region.html): Detailed information about availability and reliability patterns for SAP on Microsoft SQL for SAP on AWS.
- [Multi-Region patterns](https://docs.aws.amazon.com/sap/latest/general/multi-region.html): Detailed information about availability and reliability patterns for SAP on Microsoft SQL for SAP on AWS.


## [Disaster recovery with Elastic Disaster Recovery](https://docs.aws.amazon.com/sap/latest/general/dr-sap.html)

- [SLAs and licenses](https://docs.aws.amazon.com/sap/latest/general/slas-licenses.html): For a disaster recovery implementation, Service Level Agreements (SLA) are used to define how resilient your system is at avoiding loss of data and reducing downtime when your workload becomes unavailable due to a disaster event.
- [Network, storage, and compute](https://docs.aws.amazon.com/sap/latest/general/key-considerations.html): This section provides information about configuring network, storage, and compute for staging and target environments to achieve disaster recovery goals for your SAP workloads on AWS with Elastic Disaster Recovery.
- [Scenarios](https://docs.aws.amazon.com/sap/latest/general/scenarios.html): The following are the three disaster recovery scenarios.
- [Shared storage resiliency](https://docs.aws.amazon.com/sap/latest/general/file-systems-storage.html): File systems on an SAP server can be created on block type storage, for instance, on locally attached disks or Enterprise Storage Area Network (SAN) devices, or may be based on shared file systems such as SMB or NFS shared volumes from servers or Network Attached Storage (NAS) devices.
- [Implementation](https://docs.aws.amazon.com/sap/latest/general/implementation.html): Using Elastic Disaster Recovery to implement a disaster recovery solution for SAP workloads on AWS follows different considerations for different parts of a typical SAP workload, such as S/4HANA deployment.


## [RISE with SAP](https://docs.aws.amazon.com/sap/latest/general/rise.html)

### [Connectivity](https://docs.aws.amazon.com/sap/latest/general/connectivity-rise.html)

You must establish connectivity between AWS cloud where your RISE with SAP solution is running and on-premises data centers.

- [Roles and responsibility for establishing connectivity](https://docs.aws.amazon.com/sap/latest/general/rise-responsibility.html): Under RISE with SAP, the SAP Enterprise Cloud Services (ECS) team manages the SAP S/4HANA Private Cloud Environment.

### [Connecting to RISE from on-premises networks](https://docs.aws.amazon.com/sap/latest/general/rise-connection-on-premises.html)

Connectivity to RISE with SAP on AWS from on-premises is supported using AWS VPN or AWS Direct Connect or a combination of the two.

- [Connecting to RISE using AWS VPN](https://docs.aws.amazon.com/sap/latest/general/rise-connection-vpc.html): Enable access to your remote network from RISE with SAP VPC using AWS Site-to-Site VPN.
- [Connecting to RISE using AWS Direct Connect](https://docs.aws.amazon.com/sap/latest/general/rise-connection-direct-connect.html): Use AWS Direct Connect if you require a higher throughput or more consistent network experience than an internet-based connection.
- [Connecting to RISE using SD-WAN](https://docs.aws.amazon.com/sap/latest/general/rise-connection-sd-wan.html): What is SD-WAN
- [Implementation steps for connectivity](https://docs.aws.amazon.com/sap/latest/general/rise-connection-implementation-steps.html): This section provides a deeper dive into the implementation steps for connectivity between RISE with SAP and your on-premises environments (without any Customer managed AWS Account usage).

### [Connecting to RISE from your AWS account](https://docs.aws.amazon.com/sap/latest/general/rise-accounts.html)

You can connect to RISE from your AWS account in the following ways.

- [Amazon VPC peering](https://docs.aws.amazon.com/sap/latest/general/rise-connection-peering.html): VPC peering enables network connection between two AWS VPCs using private IPv4 and IPv6 addresses.
- [AWS Transit Gateway](https://docs.aws.amazon.com/sap/latest/general/rise-connection-transit.html): AWS Transit Gateway is a network transit hub to interconnect Amazon VPCs.
- [AWS Direct Connect gateway](https://docs.aws.amazon.com/sap/latest/general/rise-connection-direct-connect-gateway.html): AWS Direct Connect gateway is a global service that enables you to establish private connectivity between your on-premises networks and multiple Amazon VPCs across different AWS regions.
- [AWS Cloud WAN](https://docs.aws.amazon.com/sap/latest/general/rise-connection-cloud-wan.html): AWS Cloud WAN is a managed wide-area networking (WAN) service designed to simplify the process of building, managing, and monitoring unified global networks that connect cloud and on-premises resources.
- [Connecting to RISE using your single AWS account](https://docs.aws.amazon.com/sap/latest/general/rise-connection-accounts.html): You can establish connectivity between on-premises and RISE with SAP VPC using your AWS account.
- [Connecting to RISE using a shared AWS Landing Zone](https://docs.aws.amazon.com/sap/latest/general/rise-landing-zone.html): Modern SAP landscapes have several connectivity requirements.
- [Connect to nearest Direct Connect POP (including Local Zone)](https://docs.aws.amazon.com/sap/latest/general/rise-local-zone.html): AWS Direct Connect point-of-presence (POP) is a physical cross-connect that allows users to establish a network connection from their own premises to an AWS Region or AWS Local Zone.
- [Decision tree on connectivity to RISE](https://docs.aws.amazon.com/sap/latest/general/rise-decision-tree.html): You must establish required connectivity to proceed with RISE with SAP on AWS.

### [Other considerations](https://docs.aws.amazon.com/sap/latest/general/other-considerations.html)

This sections provides information about other considerations when connecting to RISE.

- [SAP BTP with RISE on AWS](https://docs.aws.amazon.com/sap/latest/general/rise-btp.html): You can use SAP Business Technology Platform BTP services on AWS to extend the functionality of the RISE with SAP.
- [Connecting to SaaS from RISE](https://docs.aws.amazon.com/sap/latest/general/rise-saas.html): When modernizing the SAP landscape, you may subscribe to several SAP cloud solutions or SaaS from independent software vendors to complement RISE with SAP solution.
- [Connectivity patterns for multi-cloud](https://docs.aws.amazon.com/sap/latest/general/rise-multi-cloud.html): In a complex connectivity scenario, you may need to integrate RISE with SAP setup with on-premises, AWS-hosted systems, and a variety of SaaS solutions and other cloud service providers.
- [Implement chargeback for connectivity to RISE](https://docs.aws.amazon.com/sap/latest/general/rise-chargeback.html): If you are a company with subsidiaries, you may have different RISE contracts, leading to deployments in separate AWS accounts while requiring an interlinked network connectivity.
- [Connectivity to Overlay IP in RISE on AWS](https://docs.aws.amazon.com/sap/latest/general/rise-oip.html): An Overlay IP is a private IP address assigned to an EC2 instance that is outside the VPCâs CIDR block.
- [Integrating DNS to RISE and Route 53](https://docs.aws.amazon.com/sap/latest/general/rise-dns.html): This documentation offers guidance on Domain Name System (DNS) integration options for âRISE with SAPâ deployments on AWS, focusing on enterprise scenarios where customers want to enable name resolution between RISE with SAP workloads and their existing workloads across AWS and external environments.

### [Security](https://docs.aws.amazon.com/sap/latest/general/security-rise.html)

SAP manages the security in AWS account managed by SAP.

- [SSO â SAP Cloud Identity Services and AWS IAM Identity Center](https://docs.aws.amazon.com/sap/latest/general/sso-iam.html): One of the security best practices for RISE with SAP is to centralize the user access control through the integration with a corporate Identity Provider (IdP).
- [SSO â SAP Cloud Identity Services and Microsoft Entra](https://docs.aws.amazon.com/sap/latest/general/sso-entra.html): Microsoft Entra (previously Azure AD) or other IdPs can be integrated to SAP Cloud Identity Services directly.
- [SSO â SAPGUI Front-End](https://docs.aws.amazon.com/sap/latest/general/sso-sapgui.html): SAPGUI is a graphical user interface client in the SAP ERPâs three-tier architecture of database, application servers and clients.

### [Advanced security using AWS Services](https://docs.aws.amazon.com/sap/latest/general/rise-security-aws-services.html)

AWS offers a comprehensive suite of security services that can act as a multi-layered security envelope around RISE with SAP deployments on AWS.

- [AWS Network Firewall](https://docs.aws.amazon.com/sap/latest/general/networkfirewall.html): AWS Network Firewall is a managed firewall service that provides essential network protection for Amazon Virtual Private Cloud (VPC) environments.
- [Amazon Macie](https://docs.aws.amazon.com/sap/latest/general/macie.html): Amazon Macie is a data security service that helps customers discover, classify, and protect sensitive data stored in Amazon S3 buckets by continuously monitoring and alerting on potential data risks and unauthorized access attempts.
- [Amazon GuardDuty](https://docs.aws.amazon.com/sap/latest/general/guardduty.html): Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behaviour within an AWS environment.
- [Security Hub, Detective, Audit Manager and EventBridge](https://docs.aws.amazon.com/sap/latest/general/securityhub.html): Building on implementation of GuardDuty and Amazon Macie, AWS Security Hub acts as a central hub, consolidating and prioritizing security findings AWS security services.
- [Using All AWS Security Services](https://docs.aws.amazon.com/sap/latest/general/allawssecurity.html): Combining together all services described above allow for an architecture monitoring multiple areas of a RISE on AWS deployment: network traffic, DNS logs, CloudTrail API activity, sensitive information extracted SAP data.
- [Integrating SAP Data Custodian KMS with AWS KMS](https://docs.aws.amazon.com/sap/latest/general/aws-kms.html): SAP Data Custodian Key Management Service enables customer-managed encryption keys for data stored in SAP services.
- [How AWS Nitro helps secure RISE with SAP?](https://docs.aws.amazon.com/sap/latest/general/aws-nitro.html): AWS Nitro System is the underlying technology used for Amazon Elastic Compute Cloud (Amazon EC2) instances in RISE with SAP.
- [Amazon WorkSpaces as remote access solution](https://docs.aws.amazon.com/sap/latest/general/rise-workspaces.html): Using Amazon WorkSpaces provides a secure, scalable, and managed virtual desktop environment for accessing SAP systems.
- [Reliability](https://docs.aws.amazon.com/sap/latest/general/reliability-rise.html): Reliability is one of the six pillars of SAP Lens - AWS Well-Architected Framework.

### [Observability](https://docs.aws.amazon.com/sap/latest/general/rise-observability.html)

Observability is essential for SAP customers to understand their SAP landscape and the internal state of their systems by analyzing external outputs such as logs, metrics, and traces.

- [Shared Responsibility](https://docs.aws.amazon.com/sap/latest/general/rise-observability-shared-responsibility.html): SAP bundles cloud infrastructure, S/4HANA software, tools, and services into a single subscription in the RISE with SAP commercial model.

### [Observability Options](https://docs.aws.amazon.com/sap/latest/general/rise-observability-options.html)

Observability in RISE with SAP requires a strategic approach considering native tools from AWS and SAP, and third-party solutions.

- [Native AWS](https://docs.aws.amazon.com/sap/latest/general/rise-observability-options-nativeaws.html): SAP Monitoring using Amazon CloudWatch
- [SAP Cloud ALM](https://docs.aws.amazon.com/sap/latest/general/rise-observability-sap-cloud-alm.html): SAP Cloud Application Lifecycle Management (ALM) serves as the primary tool for observability in cloud and hybrid landscapes.

### [Partner Solutions](https://docs.aws.amazon.com/sap/latest/general/rise-observability-partner-solutions.html)

While customers can build SAP observability solutions using AWS services, or use SAP Cloud ALM, there are several compelling reasons to choose partner solutions.

- [New Relic Monitoring for SAP](https://docs.aws.amazon.com/sap/latest/general/rise-observability-newrelic.html): New Relic Monitoring for SAP is a comprehensive observability solution that provides a holistic, end-to-end view connecting SAP performance to business outcomes and non-SAP systems.
- [SoftwareOne: PowerConnect for SAP Solutions](https://docs.aws.amazon.com/sap/latest/general/rise-observability-powerconnect.html): PowerConnect, an SAP-certified advanced observability and security monitoring solution that streams real-time telemetry, performance, business, and security data from SAP systems into leading observability platforms such as Splunk and Dynatrace.
- [PowerConnect for SAP on Dynatrace](https://docs.aws.amazon.com/sap/latest/general/rise-observability-dynatrace.html): PowerConnect for SAP on Dynatrace is a comprehensive observability solution that combines SoftwareOneâs deep SAP expertise with Dynatraceâs AI-powered platform to deliver unified visibility across SAP landscapes.
- [Splunk Service Intelligence for SAP Solutions](https://docs.aws.amazon.com/sap/latest/general/rise-observability-splunk.html): Splunk Service Intelligence for SAP Solutions is a comprehensive out-of-the-box solution that provides proactive, end-to-end monitoring of SAP environment.

### [Change Management](https://docs.aws.amazon.com/sap/latest/general/rise-change-management.html)

In RISE with SAP, SAP Enterprise Cloud Services (ECS) manages technical-related transports while customers are responsible for application-related transports through the SAP Transport Management System (TMS), refer to RISE with SAP S/4HANA Roles and Responsibilities for more detail.

- [Change Management for RISE with SAP](https://docs.aws.amazon.com/sap/latest/general/rise-change-management-for-rise.html): SAP Cloud ALM provides capability to manage change and orchestrate deployments across the landscape.
- [Change Management for AWS Services](https://docs.aws.amazon.com/sap/latest/general/rise-change-management-for-aws.html): You manage the change management of the AWS services that are connected to RISE with SAP; therefore, AWS provides services to automate pipeline provisioning and control.
- [Change Management with Partner Solutions](https://docs.aws.amazon.com/sap/latest/general/rise-change-management-partner.html): When your requirement goes beyond standard SAP and AWS change management tools, below are selected few partner solutions in testing and change management.

### [Data Integration and Analytics](https://docs.aws.amazon.com/sap/latest/general/rise-data-integration-analytics.html)

This sections provides information about Data Integration and Analytics in relation to RISE with SAP

### [Data integration](https://docs.aws.amazon.com/sap/latest/general/rise-data-integration.html)

RISE with SAP Extensibility for Data Integration with AWS is a technical framework that enables data flow between SAP systems, AWS services, and third-party solutions.

- [Data Replication](https://docs.aws.amazon.com/sap/latest/general/rise-data-replication.html): Data Replication from SAP is a crucial step in making the data usable for reporting, analysis, and integration with other systems.
- [Replicating data using AWS Services](https://docs.aws.amazon.com/sap/latest/general/rise-data-replication-awsmanaged.html)
- [Replicating data using SAP services](https://docs.aws.amazon.com/sap/latest/general/rise-data-replication-sap.html)
- [Replicating data using Partner Solutions](https://docs.aws.amazon.com/sap/latest/general/rise-data-replication-partner.html): AWS Partner Solutions offer ready to deploy solutions with enhanced features, such as pre-built connectors, specialized data pipelines, and advanced optimization techniques that reduce complexity and improve the speed of deployment.
- [Data Federation using AWS Services](https://docs.aws.amazon.com/sap/latest/general/rise-data-federation.html): Data federation is a data management strategy that enables, real-time analytics, single source-of-trust, no data duplication or expensive pipelines.

### [Data analytics](https://docs.aws.amazon.com/sap/latest/general/rise-data-analytics.html)

SAP customers need business insights in real-time to react to business changes and leverage untapped business opportunities.

- [Data Lake Architecture](https://docs.aws.amazon.com/sap/latest/general/rise-data-lake-architecture.html): The Data lake architecture provides building blocks that demonstrate how to combine and consolidate SAP and non-SAP data from disparate sources using analytics and machine learning services on AWS.
- [Data Warehouse Architecture](https://docs.aws.amazon.com/sap/latest/general/rise-data-warehouse-architecture.html): A Data Warehouse is a centralized repository based on âschema-on-writeâ approach that aggregates structured, historical data from multiple sources (both SAP and non-SAP) to enable advanced analytics, reporting, and business intelligence (BI).

### [Agentic AI](https://docs.aws.amazon.com/sap/latest/general/rise-agenticai.html)

What is an agentic AI

- [Amazon Bedrock Agent](https://docs.aws.amazon.com/sap/latest/general/rise-agenticai-bedrock-agent.html): Amazon Bedrock Agent acts as the intelligent orchestrator that uses the reason-and-act (ReAct) pattern to fulfil complex user requests.
- [Amazon Bedrock Agentcore](https://docs.aws.amazon.com/sap/latest/general/rise-agenticai-bedrock-agentcore.html): Bedrock AgentCore is a suite of services that enables developers to build, deploy, and operate highly capable AI agents securely and at enterprise scale.
- [Strands Agent](https://docs.aws.amazon.com/sap/latest/general/rise-agenticai-strands-agent.html): Strands Agent is an open-source SDK created by AWS for building AI agents that use large language models (LLMs) to reason and act.
- [Agentic AI to manage ERP Exceptions](https://docs.aws.amazon.com/sap/latest/general/rise-agenticai-erpexceptions.html): What is an ERP Exception An Enterprise Resource Planning (ERP) exception is a notification generated by an ERP system when a real-world situation or process deviates from a planned norm, policy or rule.

### [AWS and SAP JRA](https://docs.aws.amazon.com/sap/latest/general/rise-jra.html)

AWS and SAP Joint Reference Architecture (JRA) is a framework designed to guide customers on how to effectively integrate and utilize both AWS and SAP services to achieve specific business outcomes.

### [Data to Value](https://docs.aws.amazon.com/sap/latest/general/rise-jra-datatovalue.html)

Enterprises need data-driven intelligence that delivers measurable business outcomes.

- [Integrating data in SAP BDC with AWS data sources](https://docs.aws.amazon.com/sap/latest/general/rise-jra-datatovalue-bdc-aws.html): Non-SAP data from AWS data sources can be harmonized with SAP data via SAP Datasphere data fabric architecture with SAP BDC.
- [AI Innovation with FedML-AWS and Sagemaker](https://docs.aws.amazon.com/sap/latest/general/rise-jra-datatovalue-fedml-aws.html): In todayâs data-driven enterprises, machine learning models are only as powerful as the data they can access.
- [Artificial Intelligence](https://docs.aws.amazon.com/sap/latest/general/rise-jra-ai.html): Amazon Bedrock and SAP Generative AI Hub combine through Joint Reference Architecture (JRA) to provide enterprise-grade AI capabilities for RISE with SAP environments.
- [Integration](https://docs.aws.amazon.com/sap/latest/general/rise-jra-integration.html): In the RISE with SAP landscape, SAP Business Technology Platform (BTP), particularly the SAP Integration Suite, often facilitates integration scenarios.
- [Custom Application](https://docs.aws.amazon.com/sap/latest/general/rise-jra-customapps.html): Custom applications are created by customers to address their unique business needs and challenges that cannot be fully met by off-the-shelf software solutions.
- [Operational Reliability](https://docs.aws.amazon.com/sap/latest/general/rise-jra-operational-reliability.html): Modern enterprises face significant hurdles in maintaining continuous availability of SAP services, particularly during regional outages or maintenance windows.
- [Internet of Things](https://docs.aws.amazon.com/sap/latest/general/rise-jra-iot.html): Internet of Things (IoT) refers to a network of interconnected physical devices, vehicles, home appliances, and other items embedded with electronics, software, sensors, and network connectivity, enabling these objects to collect and exchange data.

### [Extensions](https://docs.aws.amazon.com/sap/latest/general/extensions-rise.html)

You can extend RISE with SAP by using AWS services to improve performance, security, agility, and reduce costs.

- [Performance](https://docs.aws.amazon.com/sap/latest/general/rise-performance.html): Enhance SAP Fiori performance with Amazon CloudFront
- [Application integration](https://docs.aws.amazon.com/sap/latest/general/application-integration.html): Deploy Amazon API Gateway to extract data out of SAP S/4HANA via HTTP API.
- [Archiving and Document Management](https://docs.aws.amazon.com/sap/latest/general/document-management.html): SAP Data Archiving and Document Management System (DMS) plays a crucial role both before and after migrating to RISE with SAP.
- [Development and extension](https://docs.aws.amazon.com/sap/latest/general/development-extension.html)
- [Security Extension](https://docs.aws.amazon.com/sap/latest/general/security-extension.html)
- [Artificial Intelligence](https://docs.aws.amazon.com/sap/latest/general/artificial-intelligence.html): Generative AI for SAP on AWS
