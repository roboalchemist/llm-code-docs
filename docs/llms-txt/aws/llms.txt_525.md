# Source: https://docs.aws.amazon.com/license-manager/latest/userguide/llms.txt

# AWS License Manager User Guide

> AWS License Manager streamlines the process of bringing software vendor licenses to the cloud. As you build out cloud infrastructure on AWS you can save costs by using Bring Your Own License model (BYOL) opportunities. That is, you can repurpose your existing license inventory for use with cloud resources. License Manager reduces the risk of licensing overages and penalties with inventory tracking that is tied directly into AWS services.

- [What is AWS License Manager?](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)
- [How License Manager works](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager-overview.html)
- [Get started](https://docs.aws.amazon.com/license-manager/latest/userguide/getting-started.html)
- [Troubleshooting](https://docs.aws.amazon.com/license-manager/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/license-manager/latest/userguide/doc-history.html)

## [Working with License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/using-license-manager.html)

### [License asset groups](https://docs.aws.amazon.com/license-manager/latest/userguide/license-asset-groups-overview.html)

Learn how to use License asset groups to centrally manage and monitor license usage across your AWS environment.

- [Understanding AWS License Manager license asset groups](https://docs.aws.amazon.com/license-manager/latest/userguide/understanding-license-asset-groups.html): License asset groups in AWS License Manager provide centralized license management across AWS regions and accounts within an organization, offering consolidated visibility, automated notifications, and comprehensive reporting for software license compliance.
- [Getting started with license asset groups](https://docs.aws.amazon.com/license-manager/latest/userguide/getting-started-license-asset-groups.html): This section helps you get started with license asset groups in AWS License Manager.
- [Working with license asset groups](https://docs.aws.amazon.com/license-manager/latest/userguide/working-with-license-asset-groups.html): This section describes how to create, update, delete, and manage license asset groups in AWS License Manager.
- [Working with license asset rulesets](https://docs.aws.amazon.com/license-manager/latest/userguide/working-with-license-asset-rulesets.html): This section describes how to create, update, delete, and manage license asset rulesets in AWS License Manager.

### [Self-managed licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/license-configurations.html)

Learn about Self-managed licenses in AWS License Manager.

- [Parameters and rules](https://docs.aws.amazon.com/license-manager/latest/userguide/config-overview.html): Review parameters and rules for using self-managed licenses in AWS License Manager.
- [Build rules from vendor licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/licenses-to-rules.html): Learn how to build AWS License Manager rules from vendor licenses.
- [Create a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html): Create a self-managed license in AWS License Manager.
- [Share a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/share-license-configuration.html): Share a self-managed license in AWS License Manager.
- [Edit a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/modify-license-configuration.html): Edit a self-managed license in AWS License Manager.
- [View self-managed licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/view-license-configuration.html): Learn how to view and monitor your self-managed licenses, including organization-wide visibility through License asset groups.
- [Deactivate a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/deactivate-license-configuration.html): Deactivate a self-managed license in AWS License Manager.
- [Delete a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/delete-license-configuration.html): Delete a self-managed license in AWS License Manager.
- [Self Managed License Rules](https://docs.aws.amazon.com/license-manager/latest/userguide/license-rules.html): Learn how to use license rules in AWS License Manager to manage launch mechanisms for new resources and to track licenses.

### [Granted licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html)

Use License Manager to govern the use of granted licenses.

- [Manage your granted licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/manage-granted-licenses.html): Learn how to manage your granted licenses in AWS License Manager.
- [Distribute entitlements](https://docs.aws.amazon.com/license-manager/latest/userguide/distribute-entitlement.html): Learn how to distribute entitlements from your granted licenses in AWS License Manager,
- [Grant acceptance and activation](https://docs.aws.amazon.com/license-manager/latest/userguide/grant-acceptance.html): Learn how License Manager granted licenses are accepted and activated.
- [License status](https://docs.aws.amazon.com/license-manager/latest/userguide/grant-statuses.html): View descriptions of license status for grants in AWS License Manager.
- [Metrics for buyer accounts](https://docs.aws.amazon.com/license-manager/latest/userguide/how-metrics-emit-buyers.html): Learn about CloudWatch metrics associated with buyer accounts for licenses granted in AWS License Manager.

### [License analytics](https://docs.aws.amazon.com/license-manager/latest/userguide/analytics.html)

Learn how to use Analytics to gain visibility into your software licensing portfolio across all AWS regions and accounts in your organization.

- [Primary Dashboard view](https://docs.aws.amazon.com/license-manager/latest/userguide/primary-dashboard-view.html): The license asset groups dashboard displays your top 5 license asset groups based on instance count with real-time consumption tracking.
- [Individual License asset group View](https://docs.aws.amazon.com/license-manager/latest/userguide/individual-license-asset-group-view.html): Select a license asset group from the dropdown menu to view detailed information

### [Create a usage report](https://docs.aws.amazon.com/license-manager/latest/userguide/create-usage-report.html)

AWS License Manager provides comprehensive usage reporting capabilities for both self-managed licenses and License asset groups.

- [Self-managed license reports](https://docs.aws.amazon.com/license-manager/latest/userguide/self-managed-license-reports.html): Self-managed license reports provide periodic snapshots of your license usage.
- [License asset group reports](https://docs.aws.amazon.com/license-manager/latest/userguide/license-asset-group-reports.html): License asset group reports provide on-demand, comprehensive reporting for software license compliance across multiple AWS regions and accounts within your organization.
- [Report storage](https://docs.aws.amazon.com/license-manager/latest/userguide/report-storage-location.html): Usage reports begin publishing within 60 minutes.

### [Inventory search](https://docs.aws.amazon.com/license-manager/latest/userguide/inventory.html)

Discover existing resources in your computing environment that can be managed by AWS License Manager.

- [Work with inventory search](https://docs.aws.amazon.com/license-manager/latest/userguide/discovery.html): Learn how to set up inventory search in AWS License Manager.
- [Automated discovery of inventory](https://docs.aws.amazon.com/license-manager/latest/userguide/automated-discovery.html): Learn about using automated discovery of inventory in AWS License Manager.

### [License type conversions](https://docs.aws.amazon.com/license-manager/latest/userguide/license-conversion.html)

Learn how to use AWS License Manager license type conversions to change the license type of your resources.

### [Eligible license types](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types.html)

Learn about the eligible license types for license type conversion in AWS License Manager.

- [Windows and SQL Server](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types-windows.html): Learn about the eligible license types for Windows and SQL Server in AWS License Manager.
- [Linux](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types-linux.html): Learn about the eligible subscription types for Linux in AWS License Manager.
- [Prerequisites](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-prerequisites.html): View the prerequisites for converting license types with AWS License Manager.

### [Convert a license type](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html)

Learn how to use AWS License Manager to convert license types for Windows and Linux instances.

- [Windows and SQL Server](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures-windows.html): Learn how to convert a license type for Windows instances in AWS License Manager.
- [Linux](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures-linux.html): Learn how to convert a license type for Linux instances in AWS License Manager.
- [Tenancy conversion](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-tenancy.html): Learn how to change the tenancy of an instance in AWS License Manager.
- [Troubleshooting](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-troubleshooting.html): Troubleshoot common issues with license type conversion in AWS License Manager.

### [Host resource groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html)

Learn how host resource groups work in AWS License Manager.

- [Create a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-create.html): Learn how to create a host resource group in AWS License Manager.
- [Share a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-share.html): Learn about sharing a host resource group in AWS License Manager.
- [Add Dedicated Hosts to a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/add-hosts.html): Learn how to add Dedicated Hosts to a host resource group in AWS License Manager.
- [Launch an instance in a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-launch.html): Learn how to launch an instance in a host resource group in AWS License Manager.
- [Modify a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-modify.html): Learn how to modify a host resource group in AWS License Manager.
- [Remove Dedicated Hosts from a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/remove-hosts.html): Learn how to remove Dedicated Hosts from a host resource group in AWS License Manager.
- [Delete a host resource group](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-group-delete.html): Learn how to delete a host resource group in AWS License Manager.

### [User-based subscriptions](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions.html)

Learn how to use supported licensed software products with a per-user subscription fee on Amazon EC2 instances with user-based subscriptions in AWS License Manager.

- [Get started](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions-getting-started.html): Learn how to configure user-based subscriptions in AWS License Manager.
- [Configure GPO for more sessions](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-configure-gpo.html): Configure Microsoft RDS to allow more than two user sessions at the same time with an Active Directory Group Policy Object (GPO)
- [Cross-account License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-cross-account.html): AWS License Manager supports cross-account functionality using a shared AWS Managed Microsoft AD, enabling organizations to centrally manage user subscriptions from a directory owner account while deploying instances across multiple accounts.
- [Launch an instance from a license included AMI](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-launch-instance.html): Launch an EC2 instance from a license included AMI that supports License Manager user-based subscription products.
- [Connect to an instance](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions-connect.html): Process for an Active Directory user to connect using RDP to a license-included instance that provides user-based subscription products.
- [Modify firewall settings for Microsoft Office](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-modify-firewall.html): Learn how to modify AWS Managed Microsoft AD firewall settings for your Microsoft Office subscription in AWS License Manager.

### [Manage subscription users](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-manage-users.html)

Manage subscription users for user-based subscriptions in AWS License Manager, to ensure the accuracy of subscription billing and reporting.

- [Disassociate users from an instance](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-disassociate-users.html): Disassociate AWS License Manager user-based subscription users from an EC2 instance that hosts the product.
- [Unsubscribe users](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-unsubscribe-users.html): Unsubscribe users from their user-based product subscription in AWS License Manager.
- [Deregister Active Directory](https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-deregister-ad.html): Learn how to deregister an Active Directory from AWS License Manager settings for user-based s ubscriptions.
- [Troubleshoot](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions-troubleshoot.html): Troubleshoot common issues with user-based subscriptions in AWS License Manager.

### [Manage Linux subscriptions](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions.html)

Learn how to use AWS License Manager to manage the commercial Linux subscriptions that your EC2 instances use.

- [Configure discovery](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-manage-discovery.html): Learn how to configure Linux subscription discovery from the License Manager console.
- [View instance data](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-instances-view.html): Learn how to view discovered instance data for Linux subscriptions that AWS License Manager discovered for your EC2 instances.
- [Billing information](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-billing-information.html): View billing information for Linux subscriptions in AWS License Manager.
- [Manage CloudWatch alarms](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-alarms.html): Learn how to manage CloudWatch alarms for Linux subscriptions from the AWS License Manager console.

### [Seller issued licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/seller-issued-licenses.html)

Learn how independent software vendors can use AWS License Manager to manage software licenses, and how you can track usage of seller issued licenses.

- [Entitlements](https://docs.aws.amazon.com/license-manager/latest/userguide/entitlements.html): Learn about how AWS License Manager captures seller issued license capabilities as entitlements in the license.
- [License usage](https://docs.aws.amazon.com/license-manager/latest/userguide/license-usage.html): Learn how you can track seller issued license usage in AWS License Manager.
- [Required permissions](https://docs.aws.amazon.com/license-manager/latest/userguide/seller-issued-license-requirements.html): View permissions that you need in order to track seller issued license usage in AWS License Manager.
- [Create seller issued licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/create-seller-issued-license.html): Learn how to create seller issued licenses in AWS License Manager.
- [Grant seller issued licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/isv-grant-licenses.html): The process that independent software vendors can use to grant License Manager seller issued licenses to customers.
- [Temporary credentials for ISV customers](https://docs.aws.amazon.com/license-manager/latest/userguide/granting-temporary-credentials.html): To grant entitlements in AWS License Manager, independent software vendors (ISVs) can get temporary credentials for their customers who don't have an AWS account.
- [Check out seller issued licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/license-consumption.html): Learn how AWS License Manager allows multiple users to concurrently consume entitlements from a single license.
- [Delete seller issued licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/delete-seller-issued-licenses.html): Delete a seller issued license in AWS License Manager.

### [Settings](https://docs.aws.amazon.com/license-manager/latest/userguide/settings.html)

Learn about the settings that you can configure for AWS License Manager.

- [Managed license settings](https://docs.aws.amazon.com/license-manager/latest/userguide/settings-managed-licenses.html): Learn about License Manager settings for managed licenses.
- [Linux subscription settings](https://docs.aws.amazon.com/license-manager/latest/userguide/settings-linux-subscriptions.html): Learn about Linux subscription settings in AWS License Manager.
- [User-based subscription settings](https://docs.aws.amazon.com/license-manager/latest/userguide/settings-user-based-subscriptions.html): Learn about user-based subscription settings in AWS License Manager.
- [Delegated administrator settings](https://docs.aws.amazon.com/license-manager/latest/userguide/delegated-administrator.html): Learn about delegated administrator settings in AWS License Manager.


## [Monitoring License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/license-manager/latest/userguide/monitoring-cloudwatch.html): Monitor the usage of licenses and subscriptions tracked in AWS License Manager by using Amazon CloudWatch.

### [CloudTrail logs](https://docs.aws.amazon.com/license-manager/latest/userguide/logging-using-cloudtrail.html)

Learn about logging AWS License Manager with AWS CloudTrail.

- [License Manager information in CloudTrail](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager-info-in-cloudtrail.html): Learn about the License Manager activity that's recorded in CloudTrail events.
- [Understanding License Manager log file entries](https://docs.aws.amazon.com/license-manager/latest/userguide/understanding-license-manager-entries.html): View example License Manager log file entries.


## [Security](https://docs.aws.amazon.com/license-manager/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/license-manager/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS License Manager.
- [Identity and access management](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html): Control access to AWS License Manager resources by using IAM.

### [Service-linked roles](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html)

Learn how to grant AWS License Manager access to resources in your account using service-links roles.

- [Core role](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager-role-core.html): Learn how the core service-linked role allows AWS License Manager to manage licenses on your behalf.
- [Management account role](https://docs.aws.amazon.com/license-manager/latest/userguide/management-role.html): Learn how the management account service-linked role allows AWS License Manager to manage license management actions on your behalf.
- [Member account role](https://docs.aws.amazon.com/license-manager/latest/userguide/member-role.html): How to use the member account service-linked role to allow AWS License Manager to perform license management actions from a management account on your behalf.
- [User-based subscription role](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscription-role.html): How to use the user-based subscription service-linked role to allow AWS License Manager to perform actions required to utilize user-based subscriptions.
- [Linux subscriptions role](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-role.html): How to use the Linux subscriptions service-linked role to allow AWS License Manager to perform actions required to utilize Linux subscriptions.
- [AWS managed policies](https://docs.aws.amazon.com/license-manager/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS License Manager, and about changes to those policies.
- [License signing](https://docs.aws.amazon.com/license-manager/latest/userguide/license-signing.html): Learn about cryptographically signing ISV-issued licenses in AWS License Manager.
- [Compliance validation](https://docs.aws.amazon.com/license-manager/latest/userguide/compliance-validation.html): Learn about the security and compliance of License Manager.
- [Resilience](https://docs.aws.amazon.com/license-manager/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS License Manager features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/license-manager/latest/userguide/infrastructure-security.html): Learn how AWS License Manager isolates service traffic.
- [VPC endpoints with AWS PrivateLink](https://docs.aws.amazon.com/license-manager/latest/userguide/interface-vpc-endpoints.html): Access AWS License Manager from your VPC without sending traffic over the internet by creating an interface VPC endpoint powered by AWS PrivateLink.
