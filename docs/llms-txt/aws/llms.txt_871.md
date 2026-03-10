# Source: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/llms.txt

# Amazon WorkSpaces Thin Client Administrator Guide

> WorkSpaces Thin Client is a fully managed cloud desktop service that provides users a secure instant access to web applications within a familiar desktop. Focusing on enabling distributed teams of remote workers up and running quickly with minimal IT management efforts, WorkSpaces Thin Client is designed for call center agents using web-based softphones (Amazon Connect), online data entry applications (Zendesk, ADP Payroll, Google WorkSpace, and Freshdesk), and other remote work based tasks. The WorkSpaces Thin Client host securely delivers web applications running on an Amazon Web Services instance, fully managed by Amazon, removing the need for administrators to manage instances. WorkSpaces Thin Client supports a preconfigured list of web applications as well as allowing permissions for proprietary web applications.

- [Setting up Amazon WorkSpaces Thin Client administrator console](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/setting-up.html)
- [Starting the WorkSpaces Thin Client administrator console](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/getting-started.html)
- [Using tags on WorkSpaces Thin Client resources](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/tag-thin-client-resources.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/creating-resources-with-cloudformation.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/vpc-interface-endpoints.html)
- [Document history](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/doc-history.html)

## [What is the Amazon WorkSpaces Thin Client administrator console?](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/what-is-thin-client.html)

- [Are you a first-time user?](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/first-time-user.html): If you are a first-time user of WorkSpaces Thin Client administrator console, we recommend that you begin by reading the following sections:
- [Architecture](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/architecture.html): Each WorkSpaces Thin Client is associated with a virtual desktop interface (VDI) provider.


## [Getting started with your VDI for Amazon WorkSpaces Thin Client administrator console](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/prerequisites.html)

### [Configuring WorkSpaces Personal for WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-WSP.html)

For WorkSpaces Thin Client to be used with Amazon WorkSpaces Personal, your service will need to be configured to access the WorkSpaces directories.

- [Business continuity](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/disaster-recovery.html): WorkSpaces Thin Client provides support for Business continuity as part of a Business Continuity Plan (BCP).
- [Configuring WorkSpaces Pools for WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-wsp-pools.html): For WorkSpaces Thin Client to be used with Amazon WorkSpaces Pools, your SAML 2.0 identity provider (IdP) will need to be configured to access the WorkSpaces Pools directory.
- [Configuring WorkSpaces Applications for Amazon WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-AS2.html): WorkSpaces Applications instances will be listed based on Stack names and will require an IdP login URL to be configured on the create environment page.
- [Configuring Amazon WorkSpaces Secure Browser for Amazon WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-WorkSpaces-web.html): Amazon WorkSpaces Secure Browser are based on their web portal endpoints on the WorkSpaces Thin Client Create environment page within AWS console.


## [Using WorkSpaces Thin Client administrator console](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/administrator-console.html)

### [Environments](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/console-environments.html)

Each WorkSpaces Thin Client device uses an individual virtual desktop environment to access its online resources.

### [Environment Details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-details.html)

When you select an environment, the WorkSpaces Thin Client console displays the details for that environment for you to review.

- [Summary](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-details-summary.html): The Summary section provides a high-level overview of the key features of the WorkSpaces Thin Client Environment.
- [Virtual desktop environment details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/vdi-details.html): WorkSpaces Thin Client environments are run on a virtual desktop interface.

### [Creating an environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/creating-an-environment.html)

The administrator console sets up the virtual desktop environment that is used by WorkSpaces Thin Client devices.

- [Step 1: Enter your environment details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/entering-environment-details.html)
- [Step 2: Select your virtual desktop provider](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/virtual-service-providers.html): You must have a service to provide your users access to their virtual desktop and compatible resources.
- [Step 3: Send the activation code to your device users](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/send-activation-code.html): After you set your environment and virtual desktop service, you will receive a unique activation code for your setup on the AWS Management Console.
- [Editing an environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/editing-an-environment.html): The administrator console edits the virtual desktop environment that is used by WorkSpaces Thin Client devices.
- [Deleting an environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/deleting-an-environment.html)

### [Devices](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/console-devices.html)

Each WorkSpaces Thin Client end user has a dedicated device that connects them to their virtual desktop environments and online resources.

### [Device details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-details.html)

These are the details of the devices.

- [Summary](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-details-summary.html): The Summary section provides a high-level overview of the key features of the WorkSpaces Thin Client device.
- [Device settings](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-details-settings.html): The parameters for your device are listed for your review.
- [User Activity](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-user-activity.html): This tab shows the log of a specific device's setup and usage information.
- [Editing a device name](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/editing-a-device-name.html)
- [Resetting and deregistering a device](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/resetting-and-deregsitering-a-device.html)
- [Archiving a device](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/archiving-a-device.html)
- [Deleting a device](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/deleting-a-device.html)
- [Exporting device details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/exporting-device-details.html)

### [Software updates](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/software-updates.html)

Updating the WorkSpaces Thin Client software for both virtual desktops and devices.

- [Updating environment software](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-software-update.html)
- [Updating device software](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-software-update.html): WorkSpaces Thin Client is an AWS End User Computing service that provides a thin client device that connects users to dedicated virtual desktops.
- [WorkSpaces Thin Client software releases](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-software-sets.html): WorkSpaces Thin Client is an AWS End User Computing service that provides users access to virtual desktops on a device.


## [Security](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security.html)

### [Data protection](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in WorkSpaces Thin Client.

- [Data encryption](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/data-encryption.html): WorkSpaces Thin Client collects environment and device customization data, such as user settings, device identifiers, identity provider information, and streaming desktop identifiers.
- [Encryption at rest](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/encryption-rest.html): Amazon WorkSpaces Thin Client provides encryption by default to protect sensitive customer data at rest by using AWS owned encryption keys.
- [Encryption in transit](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/encryption-transit.html): WorkSpaces Thin Client encrypts data in transit over HTTPS and TLS 1.2.
- [Key management](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/key-management.html): You can supply your own Customer Managed AWS KMS Key to encrypt your customer information.
- [Internet work traffic privacy](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/inter-network-traffic-privacy.html): Administrators are able to view WorkSpaces Thin Client session events, including start times and pending software update information.

### [Identity and access management](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security-iam.html)

How to authenticate requests and manage access your WorkSpaces Thin Client resources.

- [How Amazon WorkSpaces Thin Client works with IAM](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security_iam_service-with-iam.html): Before you use IAM to manage access to WorkSpaces Thin Client, learn what IAM features are available to use with WorkSpaces Thin Client.
- [Identity-based policy examples](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify WorkSpaces Thin Client resources.
- [AWS managed policies](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security-iam-awsmanpol.html): Learn about AWS managed policies for WorkSpaces Thin Client and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with WorkSpaces Thin Client and IAM.
- [Resilience](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific WorkSpaces Thin Client features for data resiliency.
- [Vulnerability Analysis and Management](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/vulnerability-analysis-and-management.html): Learn how AWS manages vulnerabilities in WorkSpaces Thin Client.


## [Monitoring](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/logging-using-cloudtrail.html): Learn about logging Amazon WorkSpaces Thin Client with AWS CloudTrail.
- [Monitor using CloudWatch metrics](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/cloudwatch-metrics.html): WorkSpaces Thin Client devices and Amazon CloudWatch are integrated, so you can gather and analyze performance metrics emitted by your WorkSpaces Thin Client devices.
