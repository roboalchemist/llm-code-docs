# Source: https://docs.aws.amazon.com/managedservices/latest/userguide/llms.txt

# AMS Advanced User Guide AMS Advanced Concepts and Procedures

> Describes AMS Advanced Multi-Account Landing Zone and Single-Account Landing Zone concepts, functions, and how to use the options. Includes information on access, security, defaults, incidents and service requests, monitoring, logging, backup and patch configuration changes.

- [Planned event management](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-pem.html)
- [Operations On Demand](https://docs.aws.amazon.com/managedservices/latest/userguide/ops-on-demand.html)
- [Document history](https://docs.aws.amazon.com/managedservices/latest/userguide/doc-history-ug.html)

## [What is AWS Managed Services?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html)

- [Operations plans](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams-op-plans.html): Describes AMS operations plans.
- [Getting started](https://docs.aws.amazon.com/managedservices/latest/userguide/get-start.html): Describes how to get started with AWS Managed Services.
- [Key terms](https://docs.aws.amazon.com/managedservices/latest/userguide/key-terms.html): Describes AMS key terms.

### [Service description](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sd.html)

AMS Advanced service description.

- [AWS Managed Services (AMS) AMS Advanced operation plan features](https://docs.aws.amazon.com/managedservices/latest/userguide/features.html): These are the AMS features.
- [What we do, what we do not do](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-do-not-do.html): AMS gives you a standardized approach to deploying AWS infrastructure and provides the necessary ongoing operational management, and there are some things that we do not do.
- [AMS responsibility matrix (RACI)](https://docs.aws.amazon.com/managedservices/latest/userguide/raci-table.html): The AMS responsibility matrix (RACI)
- [AMS environment basic components](https://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html): The following table lists the components of an example AWS Managed Services (AMS) managed infrastructure.
- [AMS account limits](https://docs.aws.amazon.com/managedservices/latest/userguide/account-limits.html): There are three distinct types of limits to consider within AMS multi-account landing zone: AMS API limits, AMS resource limits, and AWS limits.
- [AMS service level objectives (SLOs)](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-slo.html): Describes AMS service level objectives (SLOs).
- [Supported AWS services](https://docs.aws.amazon.com/managedservices/latest/userguide/supported-services.html): Describes AWS supported services in AMS.
- [Supported configurations](https://docs.aws.amazon.com/managedservices/latest/userguide/supported-configs.html): Describes AMS supported configurations.
- [Unsupported operating systems](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-unsupported-os.html): Describes AMS Advanced capabilities for unsupported operating systems.
- [AMS Advanced interfaces](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-interfaces.html): Learn about AMS Advanced interfaces.
- [VPC endpoints](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-endpoints.html): Describes AMS VPC endpoints.
- [AMS protected namespaces](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-namespaces.html): The list of protected namespaces for AMS.
- [AMS reserved prefixes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-reserved-prefixes-2.html): AMS reserved prefixes.
- [AMS maintenance window](https://docs.aws.amazon.com/managedservices/latest/userguide/maintenance-win.html): Describes the AMS maintenance window.
- [AMS information resources](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-info-resources.html): AMS provides several information resources to help you succeed.
- [AMS compliance](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-compliance.html): AMS has undergone auditing for the following standards and is eligible for use as part of solutions for which you must obtain compliance certification.

### [AMS Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-amis.html)

Learn about AMS Amazon machine images or AMIs.

- [Security enhanced AMIs](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-amis-security-enhanced.html): Security enhanced AMIs contain additional security settings that are aligned with the Center for Internet Security (CIS) Operating System Security Configuration Benchmarks - Level-1.
- [How integration between AD FS and AMS works](https://docs.aws.amazon.com/managedservices/latest/userguide/how-integ-between-adfs-and-ams-works.html): Describes how integration between AD FS and AMS works.
- [AMS Managed Active Directory](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-managed-AD.html): Describes AMS Managed Active Directory (aka Managed AD).
- [Application deployments](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-deployments.html): Learn about AMS application deployments.


## [Service management](https://docs.aws.amazon.com/managedservices/latest/userguide/service-management.html)

- [Account governance](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-gov.html): Describes account governance in AWS Managed Services.
- [Service commencement](https://docs.aws.amazon.com/managedservices/latest/userguide/srv-mgmt-srv-commence.html): Describes service commencement in AWS Managed Services.
- [Customer relationship management (CRM)](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-crm.html): The purpose of AMS's customer relationship management (CRM) process is to ensure that a well-defined relationship is established and maintained with you.
- [Cost optimization](https://docs.aws.amazon.com/managedservices/latest/userguide/cost-optimization.html): Describs cost optimization for your AMS Advanced accounts.
- [Service hours](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-gov-hours.html): Describes AMS contact hours
- [Getting help](https://docs.aws.amazon.com/managedservices/latest/userguide/faq-get-help.html): Describes how to get help in AWS Managed Services.


## [Network architecture](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-net-arch.html)

### [MALZ network architecture](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-net-arch-section.html)

AMS multi-account landing zone architecture.

### [Choosing single MALZ or multiple MALZs](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-single-or-multi.html)

Single multi-account landing zone vs. multiple multi-account landing zones considerations.

- [Single multi-account landing zone vs. Multiple multi-account landing zone FAQs](https://docs.aws.amazon.com/managedservices/latest/userguide/single-or-multi-malz-faq.html): Some commonly asked questions when choosing to set up a single multi-account landing zone or multiple multi-account landing zones.

### [Multi-Account Landing Zone accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-net-arch-accounts.html)

Multi-account landing zone accounts.

- [Management account](https://docs.aws.amazon.com/managedservices/latest/userguide/management-account.html): The management account is your initial AWS account when you begin onboarding with AMS.

### [Networking account](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-account.html)

The Networking account serves as the central hub for network routing.

### [Networking account architecture](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-network-arch.html)

The following diagram depicts the AMS multi-account landing zone environment, showcasing network traffic flows across account, and is an example of a highly-available setup.

### [Private network connectivity to AMS Multi-account landing zone environment](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-net-arch-private-net.html)

AWS offers private connectivity via either virtual private network (VPN) connectivity, or dedicated lines with AWS Direct Connect.

- [Centralized edge connectivity using transit gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-net-arch-cent-edge.html): AWS Transit Gateway is a service that enables you to connect your VPCs and your on-premises networks to a single gateway.
- [Connecting DX or VPN to account VPCs](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-net-arch-dx-vpn.html): With this option, the VPCs in your AMS multi-account landing zone environments are directly connected to Direct Connect or VPN.

### [Resources in the networking account](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-account-resources.html)

Resources in the networking account.

- [AWS Network Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-manager.html): AWS Network Manager.
- [Egress VPC](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-vpc.html): Insert abstract here.
- [Managed Palo Alto egress firewall](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-palo-alto.html): AMS provides a Managed Palo Alto egress firewall solution.
- [Perimeter (DMZ) VPC](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-dmz.html): Perimeter (DMZ) VPC.
- [AWS Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-transit-gateway.html): AWS Transit Gateway (TGW) is a service that enables you to connect your Amazon Virtual Private Clouds (VPCs) and your on-premises networks to a single gateway.

### [Shared Services account](https://docs.aws.amazon.com/managedservices/latest/userguide/shared-services-account.html)

The Shared Services account serves as the central hub for most AMS data plane services.

- [Updates to shared services: Multi-Account Landing Zone](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-dp-release-process.html): AMS applies data plane releases to managed accounts on a monthly basis, without prior notice.
- [Log Archive account](https://docs.aws.amazon.com/managedservices/latest/userguide/logging-account.html): The Log Archive account serves as the central hub for archiving logs across your AMS multi-account landing zone environment.
- [Security account](https://docs.aws.amazon.com/managedservices/latest/userguide/security-account.html): The Security account is the central hub for housing security related operations.

### [Application account types](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account.html)

AMS offers three types of Application accounts with different operational models, responsibilities and features.

- [AMS-managed application accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account-ams-managed.html): Application accounts that are fully managed by AMS are referred to as AMS-managed application accounts, where all operational tasks are performed by AMS.
- [AMS Accelerate accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-accelerate-account.html): You can have AMS Accelerate enabled in a multi-account landing zone AMS Advanced account.

### [Customer Managed application accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account-cust-man.html)

You can create accounts that AMS doesn't manage in the standard way.

- [Accessing your Customer Managed account](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account-cust-man-access.html): After you provision a Customer Managed account in multi-account landing zone is in the account for you to assume to configure the account.
- [Connecting your CMA with Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account-cust-man-connect-tg.html): AMS does not manage the network setup of Customer Managed accounts.
- [Getting operational help with your Customer Managed accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/application-account-cust-man-op-help.html): Getting operational help with your Customer Managed accounts.

### [Tools account (migrating workloads)](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account.html)

Learn about migrating workloads in AMS with a Tools account.

- [AWS Application Migration Service (AWS MGN)](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account-mgn.html): Learn about the AWS Application Migration Service and AMS
- [Enable access to the new Tools account](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account-enable.html): Describes how to enable access to the new AMS Tools account.
- [Example IAM CloudEndure policy](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account-ex-policy.html): See an AMS pre-approved IAM CloudEndure policy.
- [Testing connectivity and end-to-end setup](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account-test.html): Describes how to test the AMS Tools account connectivity and end-to-end setup.
- [Tools account hygiene](https://docs.aws.amazon.com/managedservices/latest/userguide/tools-account-hygiene.html): Learn about AMS Tools account hygiene.
- [Migration at scale - Migration Factory](https://docs.aws.amazon.com/managedservices/latest/userguide/migration-factory.html): Learn about AWS Migration at scale - Migration Factory

### [SALZ network architecture](https://docs.aws.amazon.com/managedservices/latest/userguide/salz-net-arch-section.html)

AMS single-account landing zone network architecture.

- [AMS Single-account landing zone shared services](https://docs.aws.amazon.com/managedservices/latest/userguide/salz-shared-services.html): Shared services subnets contain AMS Directory Services, the Management Host that automates provisioning and common tasks, antivirus (TrendMicro) management server, and internal bastion hosts:


## [Setting up AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/setting-up.html)

### [AMS default settings](https://docs.aws.amazon.com/managedservices/latest/userguide/understanding-defaults.html)

Your AWS Managed Services (AMS) network is configured in a standardized manner with defaults for most services.

- [DNS resolution defaults (MALZ)](https://docs.aws.amazon.com/managedservices/latest/userguide/default-dns-resolution.html): AMS multi-account landing zone resources that you provision in your AMS environment automatically include the installation of an EPS monitoring client.
- [EC2 IAM instance profile](https://docs.aws.amazon.com/managedservices/latest/userguide/defaults-instance-profile.html): An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.
- [Alerts from baseline monitoring in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-default-metrics.html): Describes AWS Managed Services monitoring defaults.
- [Log retention and rotation defaults](https://docs.aws.amazon.com/managedservices/latest/userguide/log-defaults.html): This section describes AMS log management defaults.
- [Using the AMS consoles](https://docs.aws.amazon.com/managedservices/latest/userguide/use-ams-console.html): The AMS consoles are AWS management consoles available to you to monitor and operate your AMS resources.

### [Using the AMS API and CLI](https://docs.aws.amazon.com/managedservices/latest/userguide/understand-sent-api.html)

The AWS Managed Services (AMS) API is similar to the APIs for other AWS services.

- [Using the AMS API in CLI, Ruby, Python, and Java](https://docs.aws.amazon.com/managedservices/latest/userguide/sent-api-ruby-python-java.html): Code snippets for the AMS API ListChangeTypeClassificationSummaries operation, in all available languages.
- [AMS bring your own EPS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-byoeps.html): AMS bring your own EPS.

### [Receiving AMS notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/notifications.html)

Communications between you and AMS occur for many reasons.

- [AMS AMI notifications with SNS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-ami-notifications.html): AMS provides an AMI notification service.
- [Service notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/service-notices.html): AMS sends outbound service requests, or service notifications, when you need to act on, or be aware of, something that might impact your account or resources.

### [RFC state change notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-state-change-notices.html)

AMS offers notifications for RFC state changes by email and CloudWatch Events

- [Email notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/console-event-triggers.html): You can add email addresses to receive RFC state changes to an RFC that you create in the AMS console, or by using the AMS API/CLI.
- [CloudWatch Events notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/cloudwatch-event-triggers.html): AMS offers push notifications for the RFC State changes through CloudWatch Events.
- [Setting up private and public DNS](https://docs.aws.amazon.com/managedservices/latest/userguide/set-dns.html): During onboarding, AMS sets up a private DNS service for communications between your managed resources and AMS.
- [AMS egress traffic management](https://docs.aws.amazon.com/managedservices/latest/userguide/egress-traffic-mgmt.html): AMS egress traffic management.

### [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html)

Describes how to deploy IAM resources in AWS Managed Services.

### [Automated IAM Provisioning](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-iam-provisioning.html)

Learn about Automated IAM Provisioning in AMS.

- [How it works](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-how-works.html): Learn how Automated IAM Provisioning in AMS works.
- [Onboarding](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-onboarding.html): Learn how to onboard to AMS Automated IAM Provisioning in AMS.
- [Using the change types](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-using.html): Learn how to use AMS Automated IAM Provisioning in AMS.
- [Runtime checks](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-runtime-checks.html): Learn how AMS Automated IAM Provisioning uses runtime checks in AMS.
- [Permission boundary check](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-runtime-checks-perm-boundary.html): Learn about the AMS Automated IAM Provisioning permission Boundary check.
- [Troubleshooting findings and errors](https://docs.aws.amazon.com/managedservices/latest/userguide/aip-troubleshooting.html): Learn how to respond to findings and errors reported by AMS Automated IAM Provisioning runtime checks.

### [Setting permissions with IAM roles and profiles](https://docs.aws.amazon.com/managedservices/latest/userguide/setting-permissions.html)

Describes how to set AMS permissions with IAM roles and profiles.

- [Restrict permissions with IAM role policy statements](https://docs.aws.amazon.com/managedservices/latest/userguide/request-iam-user.html): AMS uses an IAM role to set user permissions through your federation service.
- [Restrict permissions with Amazon EC2 IAM instance profiles](https://docs.aws.amazon.com/managedservices/latest/userguide/request-instance-profile.html): AMS: restrict permissions with Amazon EC2 IAM instance profiles.
- [AD FS claim rule and SAML settings](https://docs.aws.amazon.com/managedservices/latest/userguide/adfs-claim-rule-saml.html): AMS and ADFS configuration options
- [Restrict with network ACL](https://docs.aws.amazon.com/managedservices/latest/userguide/restrict-nacl.html): A network access control list (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.
- [AMS on Outposts](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-outposts.html): AWS Outposts is a managed hardware solution that extends AMS managed landing zones to customer data centers.

### [Using tags](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-using-tags.html)

Describes using tags in AMS.

- [AMS infrastructure automatic tagging](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-auto-tagging.html): AMS can tag all resources created by AMS for management purposes, in your multi-account landing zone (MALZ) and single-account landing zone (SALZ) accounts.

### [AMS recommended tags](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-tags.html)

AMS recommends the following tags on supported resources.

- [AMS reserved prefixes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-reserved-prefixes.html): AMS reserved prefixes.
- [Tag bulk update notes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-tags-bu-notes.html): Describes tips for using the tag bulk update change type examples.

### [Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-resource-scheduler.html)

Describes the AMS Resource Scheduler.

- [Deploying Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/userguide/res-sched-deploying.html): Deploying AMS Resource Scheduler.
- [Customizing Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/userguide/res-sched-customize.html): Customizing AMS Resource Scheduler.
- [Using Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/userguide/res-sched-using.html): Describes using AMS Resource Scheduler.

### [AMS Resource Scheduler cost estimator](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-cost-est.html)

AMS Resource Scheduler cost estimator

- [Cost estimator tips](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-cost-est-faqs.html): AMS Resource Scheduler tips
- [AMS Resource Scheduler best practices](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-bp.html): Scheduling Amazon EC2 Instances

### [AWS Systems Manager in AMS Advanced](https://docs.aws.amazon.com/managedservices/latest/userguide/ssm-documents.html)

Learn how AWS Systems Manager documents (SSM document) define the actions that Systems Manager performs on your AWS resources in your AMS account.

- [Available AMS Advanced SSM documents](https://docs.aws.amazon.com/managedservices/latest/userguide/available-ams-ssm-documents.html): Learn about AMS Advanced SSM documents available exclusively to AMS Advanced customers to operate your account.
- [AMS Advanced SSM document versions](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-ssm-document-versions.html): Learn how SSM documents support versioning in AMS.
- [Systems Manager pricing](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-ssm-costs.html): Learn about Systems Manager pricing in AMS.

### [Offboard AMS accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding.html)

AMS offers off-boarding assistance.

- [Offboard from single-account landing zone accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding-salz.html): Describes how to get AMS offboarding assistance for single-account landing zone accounts.
- [Offboard from multi-account landing zone accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding-malz.html): Learn about offboarding from AMS multi-account landing zone accounts


## [Change management modes](https://docs.aws.amazon.com/managedservices/latest/userguide/using-change-management.html)

### [Modes overview](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-ug.html)

AWS Managed Services modes overview.

- [Types of modes and accounts in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-types.html): Different types of AMS modes.
- [AMS modes and applications or workloads](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-and-apps-ug.html): Selecting the appropriate mode for your application or workload.
- [Real world use cases for AMS modes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-use-cases.html): Use cases for AMS modes.

### [RFC mode](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-mode.html)

AMS RFC mode.

### [Learn about RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-works.html)

In AWS Managed Services (AMS) requests for change, or RFCs, work in a two-fold manner: you configure the request and the parameters for the request.

- [What are RFCs?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-r-rfcs.html): To order a new request for change (RFC) you first create it, and then submit it, using either the AMS console or the API commands CreateRfc and SubmitRfc.
- [Authenticate when using the AMS API/CLI](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-authentication.html): When using the AMS API/CLI you must authenticate with temporary credentials.
- [RFC security reviews](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-security.html): How RFC security works.
- [RFC change type classifications](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-csio.html): The change types that you use when submitting an RFC are divided into two broad classifications: Deployment for creating resources and Management for updating or deleting resources.

### [RFC action and activity states](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-action-state.html)

RfcActionState (API) / Activity State (console) help you understand the status of human intervention, or action, on an RFC.

- [RFC action states use case examples](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-action-state-examples.html): Examples of RFC action states.
- [RFC status codes](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-status-codes.html): RFC status codes help you track your requests.
- [RFC update CTs and CloudFormation template drift detection](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-updates-and-dd.html): Resources provisioned in AMS use a modified CloudFormation template.
- [Schedule RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-scheduling.html): Describes how to schedule an RFC or choose to have it run as soon as possible.
- [Approve or reject RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-approvals.html): RFCs submitted with approval-required (manual) CTs must be approved by you or by AMS.
- [Request RFC restricted run periods](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-restrict-execute.html): Formerly known as "blackout days", you can request that certain time periods be restricted so that no changes can be run whatsoever.

### [Create, clone, update, find, and cancel RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-use-examples.html)

These examples walk you through various RFC operations.

- [Create an RFC](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-create-col.html): The generic steps for how to create an RFC using the AMS console or the AMS API/CLI.
- [Clone RFCs (re-create) with the AMS console](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-clone-rfcs.html): You can use the AMS console to clone an existing RFC.
- [Update RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-update-rfcs.html): You can resubmit an RFC that has been rejected or that has not yet been submitted, by updating the RFC and then submitting it, or re-submitting it.
- [Find RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-find-col.html): Find an RFC using the AMS console or the AMS API/CLI.
- [Cancel RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-cancel-rfcs.html): You can cancel an RFC using the Console or the AMS API/CLI.

### [Use the AMS console with RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-gui.html)

Use the AMS console with RFCs

- [Configure RFC email notifications (console)](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-email-notices.html): The AMS console Requests for Change create page provides you with an option to add email addresses to receive notifications of RFC state changes:
- [Common RFC parameters](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-common-params.html): RFC common parameters.
- [Sign up for the RFC daily email](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-digest.html): RFC digest allows you to sign up for a daily email summarizing all the active and recently completed RFCs in your account.

### [What are change types?](https://docs.aws.amazon.com/managedservices/latest/userguide/understanding-cts.html)

Change type refers to the action that an RFC performs and encompasses the change action itself, and the type of change â manual vs automated.

- [Automated and manual CTs](https://docs.aws.amazon.com/managedservices/latest/userguide/ug-automated-or-manual.html): A constraint on change types is whether they are automated or manual.
- [CT approval requirements](https://docs.aws.amazon.com/managedservices/latest/userguide/constrained-unconstrained-ctis.html): Change type approval requirements
- [Change type versions](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-versions.html): After selecting a change type using the AMS console, you have the option of opening the Additional configuration area and selecting a change type version.
- [Create change types](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-creates.html): Create change types are matched version-to-version with the Update change types.
- [Update change types](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-updates.html): Update change types are restricted in their usage to match version-to-version with the Create change type originally used to provision the resource.
- [Internal-only change types](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-internals.html): You can see change types that are for internal use only.
- [Change type schemas](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-schemas.html): All change types provide a JSON schema for your input in the creation, modification, or access, of resources.
- [Managing permissions for change types](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-permissions.html): You can use a custom policy to restrict which change types (CTs) are available to different groups or users.
- [Redacting sensitive information from change types](https://docs.aws.amazon.com/managedservices/latest/userguide/ct-redaction.html): AMS change type schemas offer a parameter attribute, "metadata":"ams:sensitive":"true" that is used for parameters that would contain sensitive information, such as a password.
- [Finding a change type, using the query option](https://docs.aws.amazon.com/managedservices/latest/userguide/ug-find-ct-ex-section.html): This example demonstrates how to use the AMS API/CLI to find the appropriate Change Type for the RFC that you want to submit.
- [Troubleshooting RFC errors](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-troubleshoot.html): Learn how to troubleshoot RFC errors in AMS Advanced.

### [Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/userguide/direct-change-mode-section.html)

Using AMS Direct Change mode.

- [Getting Started with Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-get-started.html): Getting Started with Direct Change mode.
- [Security and compliance](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-security-n-compliance.html): Security and compliance in Direct Change mode.
- [Change management in Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-change-mgmt.html): Change management in Direct Change mode.
- [Creating stacks using Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-creating-stacks.html): Creating stacks using Direct Change mode
- [Direct Change Mode use cases](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-use-cases.html): Direct Change Mode use cases

### [Developer mode](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-section.html)

Describes AWS Managed Services Developer mode.

### [Getting started with Developer mode](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-implement.html)

Describes getting started with AMS Advanced Developer mode..

- [Before you begin](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-faqs.html): Describs some AMS Advanced Developer mode implementation tips.
- [Security and compliance](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-security-and-compliance.html): Learn how security and compliance work in AMS Advanced Developer mode.
- [Change management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-change-management.html): Learn about change management in AMS Advanced Developer mode.
- [Provisioning infrastructure](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-provisioning.html): Learn about provisioning infrastructure in AMS Developer mode.
- [Detective controls](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-detective-controls.html): Learn about detective controls in AMS Developer mode.
- [Logging, monitoring, and event management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-logging.html): Learn about logging, monitoring, and event management in AMS Developer mode.
- [Incident management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-incident-management.html): Learn about incident management in AMS Developer mode.
- [Patch management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-patch-management.html): Learn about patch management in AMS Developer mode.
- [Continuity management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-continuity.html): Learn about continuity management in AMS Developer mode.
- [Security and access management](https://docs.aws.amazon.com/managedservices/latest/userguide/developer-mode-security-and-access.html): Learn about security and access management in AMS Developer mode.

### [Self-Service Provisioning mode in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/self-service-provisioning-section.html)

Describes the AMS Self-Service Provisioning mode.

- [Getting started with SSP mode in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/ssp-mode-get-start.html): Describes how to get started with SSP mode in AMS.
- [Amazon API Gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/api-gateway.html): Describes Amazon API Gateway in AMS.
- [Alexa for Business](https://docs.aws.amazon.com/managedservices/latest/userguide/aws-alexa-bus.html): Describes Alexa for Business in AMS.
- [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-app-stream-2.0.html): Describes Amazon WorkSpaces Applications (WorkSpaces Applications) in AMS.
- [Amazon Athena](https://docs.aws.amazon.com/managedservices/latest/userguide/athena.html): Describes Amazon Athena in AMS.
- [Amazon Bedrock](https://docs.aws.amazon.com/managedservices/latest/userguide/bedrock.html): Describes Amazon Bedrock in AMS.
- [Amazon CloudSearch](https://docs.aws.amazon.com/managedservices/latest/userguide/cloud-search.html): Describes Amazon CloudSearch in AMS.
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/managedservices/latest/userguide/cloud-synth.html): Describes Amazon CloudWatch Synthetics in AMS.
- [Amazon Cognito](https://docs.aws.amazon.com/managedservices/latest/userguide/cognito-pool.html): Describes Amazon Cognito user pools in AMS.
- [Amazon Comprehend](https://docs.aws.amazon.com/managedservices/latest/userguide/comprehend.html): Describes Amazon Comprehend in AMS.
- [Amazon Connect](https://docs.aws.amazon.com/managedservices/latest/userguide/connect.html): Describes Amazon Connect in AMS.
- [Amazon Data Firehose](https://docs.aws.amazon.com/managedservices/latest/userguide/kdf.html): Describes Amazon Data Firehose (KDF) in AMS.
- [Amazon DevOpsÂ Guru](https://docs.aws.amazon.com/managedservices/latest/userguide/devops-guru.html): Describes Amazon DevOpsÂ Guru in AMS.
- [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/managedservices/latest/userguide/document-db.html): Describes Amazon DocumentDB (with MongoDB compatibility) in AMS.
- [Amazon DynamoDB](https://docs.aws.amazon.com/managedservices/latest/userguide/dynamo-db.html): Describes Amazon DynamoDB in AMS.
- [Amazon Elastic Container Registry](https://docs.aws.amazon.com/managedservices/latest/userguide/ecr.html): Describes Amazon Elastic Container Registry in AMS.
- [EC2 Image Builder](https://docs.aws.amazon.com/managedservices/latest/userguide/ec2-image-build.html): Describes EC2 Image Builder in AMS.
- [Amazon ECS on AWS Fargate](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-ecs-fargate.html): Describes AWS Fargate in AMS.
- [Amazon EKS on AWS Fargate](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-eks.html): Describes AWS Fargate in AMS.
- [Amazon EMR](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-emr.html): Describes Amazon EMR in AMS.
- [Amazon EventBridge](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-eventbridge.html): Describes Amazon EventBridge in AMS.
- [Amazon Forecast](https://docs.aws.amazon.com/managedservices/latest/userguide/forecast.html): Describes Amazon Forecast in AMS.
- [Amazon FSx](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-fsx.html): Describes Amazon FSx in AMS.
- [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-fsx-open-zfs.html): Describes Amazon FSx for OpenZFS in AMS.
- [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-fsx-netapp-ontap.html): Describes Amazon FSx in AMS.
- [Amazon Inspector Classic](https://docs.aws.amazon.com/managedservices/latest/userguide/inspector.html): Describes Amazon Inspector Classic in AMS.
- [Amazon Kendra](https://docs.aws.amazon.com/managedservices/latest/userguide/kendra.html): Describes Amazon Kendra in AMS.
- [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/managedservices/latest/userguide/kds.html): Describes Amazon Kinesis Data Streams in AMS.
- [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/managedservices/latest/userguide/kvs.html): Describes Amazon Kinesis Video Streams (KVS) in AMS.
- [Amazon Lex](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-lex.html): Describes Amazon Lex in AMS.
- [Amazon MQ](https://docs.aws.amazon.com/managedservices/latest/userguide/mq-comp.html): Describes Amazon MQ in AMS.
- [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managedservices/latest/userguide/kda.html): Describes Managed Service for Apache Flink (KDA) Amazon Managed Service for Apache Flink in AMS.
- [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/managedservices/latest/userguide/msk.html): Describes Amazon MSK in AMS.
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/managedservices/latest/userguide/pro.html): Describes Amazon Managed Service for Prometheus (AMP) in AMS.
- [Amazon Personalize](https://docs.aws.amazon.com/managedservices/latest/userguide/personalize.html): Describes Amazon Personalize in AMS.
- [Amazon Quick](https://docs.aws.amazon.com/managedservices/latest/userguide/quicksight.html): Describes Quick in AMS.
- [Amazon Rekognition](https://docs.aws.amazon.com/managedservices/latest/userguide/rekognition.html): Describes Amazon Rekognition in AMS.
- [Amazon SageMaker AI](https://docs.aws.amazon.com/managedservices/latest/userguide/sagemaker.html): Describes SageMaker AI in AMS.
- [Amazon Simple Email Service](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-ses.html): Describes Amazon Simple Email Service (Amazon SES) in AMS.
- [Amazon Simple Workflow Service](https://docs.aws.amazon.com/managedservices/latest/userguide/workflow.html): Describes Amazon Simple Workflow Service (Amazon SWF) in AMS.
- [Amazon Textract](https://docs.aws.amazon.com/managedservices/latest/userguide/textract.html): Describes Amazon Textract in AMS.
- [Amazon Transcribe](https://docs.aws.amazon.com/managedservices/latest/userguide/transcribe.html): Describes Amazon Transcribe in AMS.
- [Amazon WorkSpaces](https://docs.aws.amazon.com/managedservices/latest/userguide/workspaces.html): Describes WorkSpaces in AMS.
- [AMS Code services](https://docs.aws.amazon.com/managedservices/latest/userguide/code-services.html): Describes AMS Code services in AMS.
- [AWS Amplify](https://docs.aws.amazon.com/managedservices/latest/userguide/amplify.html): Describes AWS Amplify in AMS.
- [AWS AppSync](https://docs.aws.amazon.com/managedservices/latest/userguide/app-sync.html): Describes AWS AppSync in AMS.
- [AWS App Mesh](https://docs.aws.amazon.com/managedservices/latest/userguide/app-mesh.html): Describes AWS App Mesh in AMS.
- [AWS Audit Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/audit-mgr.html): Describes Audit Manager in AMS.
- [AWS Batch](https://docs.aws.amazon.com/managedservices/latest/userguide/batch.html): Describes AWS Batch in AMS.
- [AWS Certificate Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/acm.html): Describes AWS Certificate Manager in AMS.
- [AWS Private Certificate Authority](https://docs.aws.amazon.com/managedservices/latest/userguide/acm-priv-ca.html): Describes AWS Private CA in AMS.
- [AWS CloudEndure](https://docs.aws.amazon.com/managedservices/latest/userguide/cloud-endure.html): Describes AWS CloudEndure in AMS.
- [AWS CloudHSM](https://docs.aws.amazon.com/managedservices/latest/userguide/cloud-hsm.html): Describes AWS CloudHSM in AMS.
- [AWS CodeBuild](https://docs.aws.amazon.com/managedservices/latest/userguide/code-build.html): Describes AWS CodeBuild in AMS.
- [AWS CodeCommit](https://docs.aws.amazon.com/managedservices/latest/userguide/codecommit.html): Describes AWS CodeCommit in AMS.
- [AWS CodeDeploy](https://docs.aws.amazon.com/managedservices/latest/userguide/code-deploy.html): Describes AWS CodeDeploy in AMS.
- [AWS CodePipeline](https://docs.aws.amazon.com/managedservices/latest/userguide/code-pipeline.html): Describes AWS CodePipeline in AMS.
- [AWS Compute Optimizer](https://docs.aws.amazon.com/managedservices/latest/userguide/compute-optimizer.html): Describes AWS Compute Optimizer in AMS.
- [AWS DataSync](https://docs.aws.amazon.com/managedservices/latest/userguide/data-sync.html): Describes AWS DataSync in AMS.
- [AWS Device Farm](https://docs.aws.amazon.com/managedservices/latest/userguide/device-farm.html): Learn about the AMS SSPS AWS Device Farm.
- [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/managedservices/latest/userguide/elastic-disaster-recovery.html): Learn about the AMS SSPS AWS Elastic Disaster Recovery.
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-elemental-media-convert.html): Describes AWS Elemental MediaConvert in AMS.
- [AWS Elemental MediaLive](https://docs.aws.amazon.com/managedservices/latest/userguide/elemental-media-live.html): Describes AWS Elemental MediaLive in AMS.
- [AWS Elemental MediaPackage](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-elemental-media-package.html): Describes AWS Elemental MediaPackage in AMS.
- [AWS Elemental MediaStore](https://docs.aws.amazon.com/managedservices/latest/userguide/elemental-media-store.html): Describes AWS Elemental MediaStore in AMS.
- [AWS Elemental MediaTailor](https://docs.aws.amazon.com/managedservices/latest/userguide/amz-elemental-media-tailor.html): Describes AWS Elemental MediaTailor in AMS.
- [AWS Global Accelerator](https://docs.aws.amazon.com/managedservices/latest/userguide/global-acc.html): Describes Global Accelerator in AMS.
- [AWS Glue](https://docs.aws.amazon.com/managedservices/latest/userguide/glue.html): Describes AWS Glue in AMS.
- [AWS Lake Formation](https://docs.aws.amazon.com/managedservices/latest/userguide/lake-formation.html): Describes AWS Lake Formation in AMS.
- [AWS Lambda](https://docs.aws.amazon.com/managedservices/latest/userguide/lambda.html): Describes AWS Lambda in AMS.
- [AWS License Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/license-manager.html): Describes AWS License Manager in AMS.
- [AWS Migration Hub](https://docs.aws.amazon.com/managedservices/latest/userguide/migration-hub.html): Describes AWS Migration Hub in AMS.
- [AWS Outposts](https://docs.aws.amazon.com/managedservices/latest/userguide/outposts.html): Describes AWS Outposts in AMS.
- [AWS Resilience Hub](https://docs.aws.amazon.com/managedservices/latest/userguide/res-hub.html): Describes AWS Resilience Hub in AMS.
- [AWS Secrets Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/secrets-manager.html): Describes AWS Secrets Manager in AMS.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-hub.html): Describes AWS Security Hub CSPM in AMS.
- [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/managedservices/latest/userguide/service-catalog-appregistry.html): Describes AWS Service Catalog AppRegistry in AMS.
- [AWS Shield](https://docs.aws.amazon.com/managedservices/latest/userguide/aws-shield.html): Describes AWS Shield Advanced in AMS.
- [AWS Snowball Edge](https://docs.aws.amazon.com/managedservices/latest/userguide/snowball.html): Describes Snowball Edge in AMS.
- [AWS Step Functions](https://docs.aws.amazon.com/managedservices/latest/userguide/step.html): Describes AWS Step Functions in AMS.
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/managedservices/latest/userguide/sys-man-param-store.html): Describes AWS Systems Manager Parameter Store in AMS.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/managedservices/latest/userguide/sys-man-runbook.html): Describes AWS Systems Manager automation runbook in AMS.
- [AWS Transfer Family](https://docs.aws.amazon.com/managedservices/latest/userguide/transfer-sftp.html): Describes AWS Transfer Family (Transfer Family) in AMS.
- [AWS Transit Gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/transit-gateway.html): Describes AWS Transit Gateway in AMS.
- [AWS WAF](https://docs.aws.amazon.com/managedservices/latest/userguide/set-waf.html): Describes AWS WAF in AMS.
- [AWS Well-Architected Tool](https://docs.aws.amazon.com/managedservices/latest/userguide/well-arch.html): Describes AWS Well-Architected Tool in AMS.
- [AWS X-Ray](https://docs.aws.amazon.com/managedservices/latest/userguide/comp-xray.html): Describes AWS X-Ray (X-Ray) in AMS.
- [VM Import/Export](https://docs.aws.amazon.com/managedservices/latest/userguide/vm-im-ex.html): Describes VM Import/Export in AMS.

### [Customer Managed mode](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-customer-section.html)

AMS Customer Managed mode description.

- [Getting started with Customer Managed mode](https://docs.aws.amazon.com/managedservices/latest/userguide/cust-man-mode-get-start.html): Describes how to get started with AMS Customer Managed mode.

### [AMS and AWS Service Catalog](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-service-catalog-section.html)

Describes how you can use Service Catalog in AWS Managed Services.

- [Getting started with Service Catalog](https://docs.aws.amazon.com/managedservices/latest/userguide/serv-cat-get-start.html): Describes how to get started with AWS Service Catalog in AMS.
- [Service Catalog in AMS before you begin](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-service-catalog-section-faq.html): In accounts where Service Catalog is enabled, it will act as the change management system in which you provision and update IT services in your AMS account through your predefined product catalog; AMS will provide a default portfolio/product catalog, and your IT admins can create and configure your own.


## [Finding the data you need (SKMS)](https://docs.aws.amazon.com/managedservices/latest/userguide/skms.html)

- [Find VPC IDs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-vpc.html): Learn about finding VPC IDs in AWS Managed Services.
- [Find subnet IDs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-subnet.html): Learn about finding a subnet ID in AWS Managed Services.
- [Find AMI IDs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-ami.html): Learn about finding AMI IDs in AMS.
- [Find security group (SG) IDs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-SGs.html): Learn how to find your security group (SG) IDs in AWS Managed Services.
- [Find IAM entities](https://docs.aws.amazon.com/managedservices/latest/userguide/find-iam-entities.html): Learn how to find IAM entities in AWS Managed Services.
- [Find stack IDs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-stack.html): Learn how to find stack IDs in AWS Managed Services.
- [Find instance IDs or IP addresses](https://docs.aws.amazon.com/managedservices/latest/userguide/find-instance-id.html): Learn about finding an instance ID or IP address in AWS Managed Services.
- [Find ARNs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-arn.html): Learn about finding the Amazon Resource Name (ARN) for an AWS resource.
- [Find resources by ARN](https://docs.aws.amazon.com/managedservices/latest/userguide/find-resource-by-arn.html): Learn about finding a resource with its ARN.

### [Find account settings](https://docs.aws.amazon.com/managedservices/latest/userguide/find-your-settings.html)

Learn how to find your AMS account settings.

- [Find FQDNs](https://docs.aws.amazon.com/managedservices/latest/userguide/find-FQDN.html): Learn how to find your FQDN in AWS Managed Services.
- [Find availability zones (AZs)](https://docs.aws.amazon.com/managedservices/latest/userguide/find-AZs.html): Learn how to find your availability zones (AZs) in AWS Managed Services.
- [Find SNS topics](https://docs.aws.amazon.com/managedservices/latest/userguide/find-SNS-settings.html): Learn how to find your SNS topics in AWS Managed Services.
- [Find backup settings](https://docs.aws.amazon.com/managedservices/latest/userguide/find-backup-settings.html): Learn how to find your backup settings in AWS Managed Services.


## [Access management](https://docs.aws.amazon.com/managedservices/latest/userguide/access-mgmt.html)

### [What is Access Management?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-access-mgmt.html)

Access management is how AMS protects your resources by allowing only authorized and authenticated access.

- [Why and when we access your account](https://docs.aws.amazon.com/managedservices/latest/userguide/access-justification.html): Certain events can cause AMS to access your account through IAM roles.
- [How and when to use root](https://docs.aws.amazon.com/managedservices/latest/userguide/how-when-to-use-root.html): Using the root user account in AMS.
- [AMS Advanced console and Amazon EC2 access](https://docs.aws.amazon.com/managedservices/latest/userguide/access-how-works-prereqs.html): AMS Advanced console and Amazon EC2 access.

### [Accessing the AWS Management console and the AMS console](https://docs.aws.amazon.com/managedservices/latest/userguide/access-console.html)

Describes how you access the AWS and AMS consoles.

- [Temporary AMS console access](https://docs.aws.amazon.com/managedservices/latest/userguide/access-console-temp.html): Describes how temporary AMS console access works.

### [Accessing instances using bastions](https://docs.aws.amazon.com/managedservices/latest/userguide/using-bastions.html)

AWS Managed Services: accessing instances using bastions.

- [DNS friendly bastion names](https://docs.aws.amazon.com/managedservices/latest/userguide/dns-bastions.html): Describes AWS Managed Services DNS friendly bastion names.
- [Saving costs on Single-account landing zone (SALZ) bastions](https://docs.aws.amazon.com/managedservices/latest/userguide/dns-bastions-saving-costs.html): Describes saving costs on AWS Managed Services bastion instances.
- [Using bastion IP addresses](https://docs.aws.amazon.com/managedservices/latest/userguide/find-bastions.html): Learn how to find AMS bastion IP addresses.

### [Instance access examples](https://docs.aws.amazon.com/managedservices/latest/userguide/access-examples.html)

Examples of accessing AWS Managed Services (AMS) instances.

- [Linux computer to Linux instance](https://docs.aws.amazon.com/managedservices/latest/userguide/linux-to-linux.html): Example Linux computer to Linux instance access.
- [Linux computer to Windows instance](https://docs.aws.amazon.com/managedservices/latest/userguide/linux-to-windows.html): Example Linux computer to Windows instance access.
- [Windows computer to Windows instance](https://docs.aws.amazon.com/managedservices/latest/userguide/windows-to-windows.html): Example Windows computer to Windows instance access.
- [Windows computer to Linux instance](https://docs.aws.amazon.com/managedservices/latest/userguide/windows-to-linux.html): Example Windows computer to Linux instance access.
- [Team, or role, based access control in an AMS account](https://docs.aws.amazon.com/managedservices/latest/userguide/faq-tbac.html): Scenarios.


## [Automated EC2 instance configuration](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-instance-config.html)

- [Prerequisites for automated instance configuration](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-pre-reqs.html): Describes prerequisites for automated instance configuration
- [SSM Agent automatic installation](https://docs.aws.amazon.com/managedservices/latest/userguide/ssm-agent-auto-install.html): Learn how to automatically install the SSM Agent in AMS.

### [Automated changes](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-changes-made.html)

A list of automated instance configuration changes.

- [Automatically update code on Linux instances](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-instance-code.html): Describes automatic updates on instance code on Linux instances.
- [Automatically update PBIS on Linux instances](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-pbis.html): Describes automatic updates PBIS on Linux instances.
- [Automatically update the minimum version of SSM and CloudWatch agents](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-changes-agents.html): Describes how AMS automated changes update SSM and CloudWatch agents to minimum versions
- [CloudWatch configuration files, update details](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-files.html): Describes additional details on the CloudWatch configuration.
- [Automatically configured logs](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-logs-cw.html): Describes automatically configured logs emitted through CloudWatch.


## [Monitoring and event management](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring.html)

### [What does the AMS monitoring system monitor?](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-what-services.html)

Describes what the the AMS monitoring system monitors.

- [Single-Account Landing Zone proactive monitoring of Active Directory Trust](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-ad-trust.html): Describes AMS single-account landing zone proactive monitoring of Active Directory Trust.
- [How monitoring works](https://docs.aws.amazon.com/managedservices/latest/userguide/how-monitoring-works.html): AMS monitoring processes.
- [Viewing the monitoring configuration for an account](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-view-config.html): Learn how to view the monitoring configuration for an AMS account
- [Changing the monitoring configuration for an account](https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-change-config.html): Describes changing the monitoring configuration for an AMS account.
- [Application aware incident notifications in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/app-aware-inc-notifications.html): Describes AWS Managed Services customized incident notifications.

### [Alert notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/sent-alerts.html)

Learn about alert notifications from AMS.

- [Receiving alerts](https://docs.aws.amazon.com/managedservices/latest/userguide/sent-alert-views.html): Describes how AMS enables you to receive alert notifications for Amazon EC2 resources directly to reduce communication delays.
- [Tag-based alert notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/tag-alerts.html): Learn about tag-based alert notifications in AMS.
- [AMS automatic remediation of alerts](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-remediation.html): Some alerts are automatically remediated by AMS.
- [Creating additional CloudWatch alarms](https://docs.aws.amazon.com/managedservices/latest/userguide/custom-cloudwatch-alarms.html): Learn about creating additional CloudWatch alarms in AMS.
- [Creating custom CloudWatch metrics and alarms](https://docs.aws.amazon.com/managedservices/latest/userguide/custom-cloudwatch-events.html): Describes how you can store your business and application metrics in Amazon CloudWatch.
- [Using CloudWatch Application Insights for .Net and SQL server](https://docs.aws.amazon.com/managedservices/latest/userguide/mon-cwai.html): Describes how you can use CloudWatch Application Insights to set up the monitors for your application resources in AMS.
- [AMS Event Router](https://docs.aws.amazon.com/managedservices/latest/userguide/how-event-router-works.html): How AMS Advanced uses Amazon EventBridge Managed Rules to ingest customer events.

### [Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/userguide/trusted-remediator.html)

How to use the Trusted Remediator feature.

- [Get started with Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-gs.html): Information on how to get started using Trusted Remediator in AMS.
- [Supported Compute Optimizer recommendations](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-supported-recommendations-co.html): Compute Optimizer checks supported by Trusted Remediator
- [Supported Trusted Advisor checks](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-supported-checks.html): Trusted Advisor checks supported by Trusted Remediator
- [Supported Security Hub CSPM recommendations](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-supported-sec-hub-recommendations.html): Security Hub CSPM recommendations supported by Trusted Remediator
- [Configure check remediation](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-configure-remediations.html): Manage Trusted Advisor check remediation configurations in Trusted Remediator
- [Execution mode decision workflow](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-ex-mode-workflow.html): Understand the decision logic on Trusted Remediator
- [Configure remediation tutorials](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-tutorials.html): Review tutorials on how to configure remediations in Trusted Remediator
- [Work with remediations](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-remediation.html): Learn how to work with remediations in Trusted Remediator
- [Remediation logs](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-logging.html): Learn how to work with remediation logs in Trusted Remediator
- [Best practices](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-best-practices.html): Learn about Trusted Remediator best practices
- [FAQs](https://docs.aws.amazon.com/managedservices/latest/userguide/tr-faq.html): Learn about Trusted Remediator FAQs


## [Log management](https://docs.aws.amazon.com/managedservices/latest/userguide/log-mgmt.html)

- [How AMS logging works](https://docs.aws.amazon.com/managedservices/latest/userguide/getting-started-log-mgmt.html): How AMS logging works.

### [Accessing your logs](https://docs.aws.amazon.com/managedservices/latest/userguide/access-to-logs.html)

Default IAM roles allow your access to all logs within your account.

- [AMS aggregated service logs](https://docs.aws.amazon.com/managedservices/latest/userguide/service-logs.html): Each AWS service logs to either CloudWatch Logs or a specific location in an Amazon S3 bucket.
- [AMS shared services logs](https://docs.aws.amazon.com/managedservices/latest/userguide/shared-service-logs.html): The following table describes the logs, and log location, for the AMS Shared Services in your account.
- [Amazon Elastic Compute Cloud (Amazon EC2) - system level logs](https://docs.aws.amazon.com/managedservices/latest/userguide/access-to-logs-ec2.html): Instance logs are collected by a CloudWatch Logs agent running on the instance and can be accessed through a CloudWatch Log group of the same name as the instance.
- [Integrating with Splunk](https://docs.aws.amazon.com/managedservices/latest/userguide/enable-Splunk-log-push.html): AMS supports AWS Lambda-based push to customer log analytics services, such as Splunk.

### [Customizing your log configuration](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize.html)

Customizing your log configuration.

- [Altering CloudWatch log retention](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-retention.html): Altering CloudWatch log retention.
- [Enabling logging for supported services](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-enable-service.html): Enabling logging for supported services.


## [Security management](https://docs.aws.amazon.com/managedservices/latest/userguide/security-mgmt.html)

- [Data protection in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-data-protect.html): Learn about data protection in AMS.

### [Identity and access management](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-iam.html)

Identity and access management in AMS.

### [Authenticating with identities](https://docs.aws.amazon.com/managedservices/latest/userguide/iam-auth.html)

Authenticating with identities

- [IAM user role](https://docs.aws.amazon.com/managedservices/latest/userguide/defaults-user-role.html): Learn about IAM user roles in AMS.
- [Security event logging and monitoring](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-log-mon.html): Security event logging and monitoring
- [Endpoint Security (EPS)](https://docs.aws.amazon.com/managedservices/latest/userguide/eps-defaults.html): Resources that you provision in your AMS Advanced environment automatically include the installation of an EPS monitoring client.

### [Malware mitigation process](https://docs.aws.amazon.com/managedservices/latest/userguide/malware-mitigation.html)

AMS uses Trend Microâs Deep Security Platform (anti-malware system), by default, to detect and respond to malware on your AMS-managed instances.

- [Enable IDS and IPS in Trend Micro Deep Security](https://docs.aws.amazon.com/managedservices/latest/userguide/gui-enable-IPSIDS.html): You can request that AMS enable Trend Micro Intrusion Detection System (IDS) and Intrusion Protection Systems (IPS) non-default features for your account.
- [Full system malware scans](https://docs.aws.amazon.com/managedservices/latest/userguide/malware-full-system-scans.html): The Payment Card Industry Data Security Standard (PCI DSS) requires full system malware scans, which are enabled on your AMS-managed VPC by default.
- [AMS incident response](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-incident-response.html): Incident response
- [Compliance validation](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-compli-valid.html): Describes AMS compliance validation.
- [Multi-Account Landing Zone viewing the compliance status of your AWS Config Rules](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-view-compliance.html): AMS multi-account landing zone utilizes the AWS Config aggregator service to create a centralized view of compliance across all your accounts.
- [AMS multi-account landing zone service control policy restrictions](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-scps-malz.html): The following table describes the goals of the AMS service control policies.
- [Resilience](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-resilience.html): Learn about AMS resilience.

### [Infrastructure security](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-infrastructure.html)

Learn about AMS infrastructure security

- [Security control for end-of-support operating systems](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-eos-sec-controls-os.html): Operating systems that are outside of the general support period of the operating system manufacturer's "end-of-support" or EOS, and do not receive security updates.
- [Security groups](https://docs.aws.amazon.com/managedservices/latest/userguide/about-security-groups.html): In AWS Virtual Private Clouds (VPCs), AWS Security Groups act as virtual firewalls, controlling the traffic for one or more stacks (an instance or a set of instances).

### [Preventative and detective controls](https://docs.aws.amazon.com/managedservices/latest/userguide/scp-library.html)

Describes AMS preventative and detective controls library.

- [Curated SCPs and Config Rules](https://docs.aws.amazon.com/managedservices/latest/userguide/scp-library-compliance.html): Curated SCPs and Config Rules for AMS Advanced.
- [Custom notification for Config rules](https://docs.aws.amazon.com/managedservices/latest/userguide/scp-lib-custom-notice.html): SCP custom notification for ConfigRules.
- [Amazon EventBridge rule SLR](https://docs.aws.amazon.com/managedservices/latest/userguide/slr-evb-rule-advanced.html): AMS Advanced uses the service-linked role (SLR) named AWSServiceRoleForManagedServices_Events â This role trusts one of the AWS Managed Services service principals (events.managedservices.amazonaws.com) to assume the role for you.
- [Security best practices](https://docs.aws.amazon.com/managedservices/latest/userguide/sec-best-practice.html): Learn about AMS security best practices

### [Security Incident Response](https://docs.aws.amazon.com/managedservices/latest/userguide/security-incident-response.html)

Learn about Security Incident Response in AMS.

- [How it works](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-how-works.html): Learn how Security Incident Response in AMS works.
- [Prepare](https://docs.aws.amazon.com/managedservices/latest/userguide/preparation-phase.html): Learn what the preparation phase in Security Incident Response in AMS contains.
- [Detect](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-detect.html): Learn about the AMS Security Incident Response detection.
- [Analyze](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-analyze.html): Learn about analyzing security events to AMS.
- [Contain](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-contain.html): Learn about containing security events to AMS.
- [Eradicate](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-eradicate.html): Learn about eradicating security events in AMS.
- [Recover](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-recover.html): Learn about recovering from security events in AMS.
- [Post Incident Report](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-post-report.html): Learn about the security events post-incident report in AMS.

### [Security Incident Response Runbooks](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-runbooks.html)

Learn about the security incidents runbooks in AMS.

- [Response to root user activity](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-root-user.html): Learn about the security incidents root user in AMS.
- [Response to malware events](https://docs.aws.amazon.com/managedservices/latest/userguide/sir-malware.html): Learn about the security incidents malware in AMS.

### [Change request security reviews in AMS Advanced](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sec-change-request-review.html)

Change request security review process AMS Advanced.

- [Customer Security Risk Management process](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sec-csrm-process.html): CSRM process in AMS Advanced
- [AMS Advanced technical standards](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sec-technical-standards.html): Technical standards AMS Advanced
- [Standard controls in AMS Advanced](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sec-stand-controls.html): Standard controls in AMS Advanced
- [Changes that introduce high or very high security risks in your environment](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sec-high-risk-con.html): Changes that introduce high or very high security risks in the environment in AMS Advanced


## [Continuity management](https://docs.aws.amazon.com/managedservices/latest/userguide/continuity-mgmt.html)

- [How continuity management works](https://docs.aws.amazon.com/managedservices/latest/userguide/how-continuity-mgmt-works.html): Describes how AMS uses AWS Backup for continuity management.
- [Disaster recovery response](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-dr-response.html): AMS disaster recovery response
- [Disaster recovery planning](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-disaster-recovery.html): Learn about disaster recovery (DR) planning in AMS.


## [Patch management](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-mgmt.html)

- [AMS Patch Orchestrator: a tag-based patching model](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-orchestrator.html): If you have been onboarded to the new AMS Patch Orchestrator tag-based patching model, you can use tags to apply your patch configuration to a precise set of resources, called a patch group, ranging from one instance to all of your instances.

### [Using Patch Orchestrator](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-orchestrator-using.html)

Enable AMS Patch Orchestrator for your account by submitting a service request that includes the following details:

- [Patch windows](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-windows.html): Instances in a specific patch group are patched during one or more patch windows.
- [Patch notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-notifications.html): The subscribed email addresses (up to 5) receive an email before the patch maintenance window starts.
- [Patch baselines](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-baselines.html): By default, all operating system (OS) vendor-provided patches are installed using the AMS-default patch baseline.

### [AMS standard patching](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-overview.html)

AMS standard patching.

### [How AMS standard patching works](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-how-works.html)

AMS uses the Systems Manager Run Command service for regularly scheduled monthly and as-needed critical patching, with two principal patching methods, in-place and AMI replacement, depending on your infrastructure deployment strategy (mutable vs. immutable).

- [In-place patching](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-method-mutable.html): In-place patching refers to a method where AMS logs into each stack instance and applies patches.
- [AMI updates patching (using patched AMIs for Auto Scaling groups)](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-method-immutable.html): Using Patched AMIs for Auto Scaling Groups
- [Actions you can take in AMS standard patching](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-actions.html): In addition to testing new AMIs, there are several actions you can take to manage the patching of your infrastructure:
- [AMS standard patching FAQs](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-faqs.html): AMS Standard Patching FAQs
- [Patching service commitments](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-service-commitments.html): Based on your type of infrastructure deployment, and criticality of the update, we provide service commitments for critical security updates for mutable and immutable infrastructures, and important updates for mutable and immutable infrastructures.


## [Reports and options](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-reporting.html)

### [On-request reports](https://docs.aws.amazon.com/managedservices/latest/userguide/on-request-reporting.html)

AMS collates data from various native AWS services to provide value added reports on major AMS offerings.

- [AMS Patch reports](https://docs.aws.amazon.com/managedservices/latest/userguide/reporting-patch.html): AMS patch reporting.
- [AMS Backup reports](https://docs.aws.amazon.com/managedservices/latest/userguide/reporting-backup.html): AWS Managed Services Backup reports.
- [Incidents Prevented and Monitoring Top Talkers reports](https://docs.aws.amazon.com/managedservices/latest/userguide/incidents-prevented-top-talkers.html): AMS Incidents Prevented and Top Talkers reports.
- [Billing Charges Details report](https://docs.aws.amazon.com/managedservices/latest/userguide/reporting-billing-details.html): AMS Billing Charges Details report.
- [Trusted Remediator reports](https://docs.aws.amazon.com/managedservices/latest/userguide/trusted-remediator-reports.html): Trusted Remediator reports

### [Self-service reports](https://docs.aws.amazon.com/managedservices/latest/userguide/self-service-reporting.html)

About AWS Managed Services self-service reports.

- [Internal API operations](https://docs.aws.amazon.com/managedservices/latest/userguide/internal-apis.html): Internal API operations in AMS self-service report CloudTrail logs.
- [Patch report (daily)](https://docs.aws.amazon.com/managedservices/latest/userguide/daily-patch-report.html): AWS Managed Services daily patch report.
- [Backup report (daily)](https://docs.aws.amazon.com/managedservices/latest/userguide/daily-backup-report.html): Daily backup report.
- [Incident report (weekly)](https://docs.aws.amazon.com/managedservices/latest/userguide/weekly-incident-report.html): AWS Managed Services weekly incident report.
- [Billing report (monthly)](https://docs.aws.amazon.com/managedservices/latest/userguide/monthly-billing.html): AWS Managed Services monthly billing report.
- [Aggregated reports](https://docs.aws.amazon.com/managedservices/latest/userguide/aggregated-reports.html): Aggregated self-service reports.
- [AMS self-service reports dashboards](https://docs.aws.amazon.com/managedservices/latest/userguide/ssr-dashboards.html): AMS self-service reports dashboards include resource tagger and security configurations dashboards.
- [Data retention policy](https://docs.aws.amazon.com/managedservices/latest/userguide/data-retention-policy.html): Data retention policy.
- [Offboard from SSR](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding-ssr.html): How to offboard from SSR.


## [Get support](https://docs.aws.amazon.com/managedservices/latest/userguide/support-experience.html)

### [Incident management](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-adv-manage-incidents.html)

About AMS incident management.

- [What is incident management?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-incident-mgmt.html): Incident management is the process AMS uses to record, act on, communicate progress of, and provide notification of, active incidents.
- [Incident management service commitments](https://docs.aws.amazon.com/managedservices/latest/userguide/incident-serv-commits.html): The incident management service commitments AMS offers.

### [Incident management examples](https://docs.aws.amazon.com/managedservices/latest/userguide/incident-mgmt-examples.html)

Using the AMS console Create Incident page, you can create cases.

- [Reporting incidents](https://docs.aws.amazon.com/managedservices/latest/userguide/gui-ex-report-incident.html): Information on how to report incidents to AMS.
- [Monitoring and updating incidents](https://docs.aws.amazon.com/managedservices/latest/userguide/mon-update-incident-console.html): Information on how to monitor and update incidents in the console.
- [Managing incidents with the AWS Support API](https://docs.aws.amazon.com/managedservices/latest/userguide/report-manage-incidents-api.html): The AWS Support API enables you to create incidents and add correspondence to them throughout investigations of your issues and interactions with AWS Support staff.
- [Responding to AMS-generated incidents](https://docs.aws.amazon.com/managedservices/latest/userguide/respond-to-sent-generated-incident.html): AMS proactively monitors your resources.

### [Service request management](https://docs.aws.amazon.com/managedservices/latest/userguide/service-request-management.html)

Describes service request management.

- [When to use a service request](https://docs.aws.amazon.com/managedservices/latest/userguide/service-request-when-to-use.html): Describes service request management.
- [How service request management works](https://docs.aws.amazon.com/managedservices/latest/userguide/service-request-resolution.html): Learn how service request management works.
- [Testing a service request](https://docs.aws.amazon.com/managedservices/latest/userguide/service-request-testing.html): Describes testing AMS service request submissions.
- [Creating a service request](https://docs.aws.amazon.com/managedservices/latest/userguide/gui-ex-create-service-request.html): Describes how to create an AMS service request.
- [Monitoring and updating service requests](https://docs.aws.amazon.com/managedservices/latest/userguide/update-monitor-review-service-requests.html): Describes how to monitor and update service requests in AMS
- [Responding to an AMS-generated service requests](https://docs.aws.amazon.com/managedservices/latest/userguide/respond-to-sent-generated-sr.html): Describes how to respond to an AMS-generated service request.
- [Billing questions](https://docs.aws.amazon.com/managedservices/latest/userguide/billing-questions.html): Describes how to submit a billing query using the AWSSupport console.
