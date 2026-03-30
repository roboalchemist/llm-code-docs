# Source: https://docs.aws.amazon.com/smc/latest/ag/llms.txt

# AWS Service Management Connector Administrator Guide

> Provides a conceptual overview of AWS Service Management Connector and includes detailed instructions for using the service as an administrator.

- [Document history](https://docs.aws.amazon.com/smc/latest/ag/doc-history.html)

## [What is AWS Service Management Connector?](https://docs.aws.amazon.com/smc/latest/ag/overview.html)

- [Security in AWS Service Management Connector](https://docs.aws.amazon.com/smc/latest/ag/w2aab5b9.html): Learn how AWS Service Management Connector keeps your resources secure.


## [Connector for ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-what-is.html)

- [Align the ServiceNow Connector to industry best practices](https://docs.aws.amazon.com/smc/latest/ag/sn-alignment.html): This Connector aligns to industry best practices such as ITILÂ®âs service management areas by enabling tools (services) with the intersection of people, processes and partners.

### [Setting up AWS Service Management Connector for ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-start.html)

Before installing the AWS Service Management Connector for ServiceNow, verify that you have the necessary permissions in your AWS account and ServiceNow instance.

- [Prerequisites](https://docs.aws.amazon.com/smc/latest/ag/aws-prereqs.html): Make sure you have AWS and ServiceNow prerequisites configured before you get started.
- [Setting baseline permissions for AWS Service Management Connector for ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-base-perms.html): This section describes how to configure AWS Identity and Access Management (IAM) permissions, AWS Service Catalog, and other AWS services to use AWS Service Management Connector for ServiceNow.

### [Creating Connector for ServiceNow users](https://docs.aws.amazon.com/smc/latest/ag/create-sc-users.html)

Create the two required users for Connector for ServiceNow, an AWS Sync User and an AWS End User.

- [Creating AWS Service Management Connector Sync user](https://docs.aws.amazon.com/smc/latest/ag/scsyncuser.html): This section describes how to create the AWS Sync user and associate the appropriate IAM permission.
- [Creating AWS Service Management Connector end user](https://docs.aws.amazon.com/smc/latest/ag/scenduser.html): This section describes how to create the AWS Service Management Connector end user and associates the appropriate IAM permission.
- [Creating the SCConnectLaunch role](https://docs.aws.amazon.com/smc/latest/ag/scconnectlaunchrole.html): Configuring the SCConnectLaunch role enables segregation of duty through provisioning product resources for ServiceNow end users.

### [Configuring core ServiceNow components](https://docs.aws.amazon.com/smc/latest/ag/sn-config-core-components.html)

This section describes how to configure core components in ServiceNow.

- [Activating ServiceNow plugins](https://docs.aws.amazon.com/smc/latest/ag/sn-activate-plugins.html): AWS Service Management Connector uses three ServiceNow plugins to provide useful components to the integration features.
- [Installing ServiceNow Connector scoped application](https://docs.aws.amazon.com/smc/latest/ag/sn-install-connector.html): The AWS Service Management Connector for ServiceNow is a conventional, scoped application that was developed and released through a ServiceNow update set.
- [Configuring Connector using Guided Setup](https://docs.aws.amazon.com/smc/latest/ag/sn-guided-setup.html): The Connector for ServiceNow includes a Guided Setup mechanism to enable customers to configure and mark complete ServiceNow installation components for the AWS Service Management Connector.

### [Platform system administrator components](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-connector.html)

To enable the AWS Service Management Connector scoped application named AWS Service Management, the system admin must create a discovery source, and configure specific platform tables, forms, and views.

- [Administering AWS Service Management Connector Dashboard](https://docs.aws.amazon.com/smc/latest/ag/admin-dashboard.html): As the system administrator, you can restrict access to the dashboard and its reports for specific users, roles or groups.
- [Enabling permissions on ServiceNow Platform](https://docs.aws.amazon.com/smc/latest/ag/sn-enable-permissions.html): For AWS products to display under AWS portfolios as sub-categories in the ServiceNow Service Catalog, you need to modify the Application Access form for Catalog Item Category tables.
- [ServiceNow permissions for administrators of the Connector scoped app](https://docs.aws.amazon.com/smc/latest/ag/sn-permissions-admin.html): The AWS Service Management scoped app has two ServiceNow roles that enable access to configure the application.
- [Configuring AWS Service Management Connector scoped application](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-sc-connector-scoped-app.html): After installing and configuring the AWS Service Management Connector, you must configure the scoped application and applicable roles.
- [Configuring AWS accounts to synchronize in the Connector](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-accounts.html): Learn how to configuring AWS accounts to synchronize in the Connector.
- [Validating ServiceNow connectivity to AWS Regions](https://docs.aws.amazon.com/smc/latest/ag/validate-regions.html): You can now validate connectivity to AWS accounts between the ServiceNow Connector_Demo account and the AWS IAM SMSyncUser and SMEndUser.
- [Manually syncing scheduled jobs](https://docs.aws.amazon.com/smc/latest/ag/manual-sync-scheduled-jobs.html): The Connector for ServiceNow includes nine sync jobs related to AWS services integrations.

### [AWS Service Catalog](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-sc.html)

After you create two IAM users with baseline permissions in each account, the next step is to configure AWS Service Catalog.

### [Configuring AWS Service Catalog](https://docs.aws.amazon.com/smc/latest/ag/sn-config-sc.html)

This section provides the configurations you need to integrate AWS services in ServiceNow.

- [Creating StackSet constraints](https://docs.aws.amazon.com/smc/latest/ag/create-stackset-constraints.html): CloudFormation StackSets enable users to create and deploy products across multiple accounts and Regions.
- [Relating budgets to products and portfolios](https://docs.aws.amazon.com/smc/latest/ag/sn-budgets.html): The Connector for ServiceNow enables ServiceNow administrators to view budgets related to Service Catalog products and portfolios.
- [Service Catalog Terraform Open Source product type support](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-terraform.html): AWS Service Management Connector supports AWS Service Catalog's Terraform open source product type.
- [Configuring AppRegistry](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-appregistry.html)

### [Configuring AWS Service Catalog in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-config-sn.html)

This section provides the configurations you need to integrate AWS Service Catalog in ServiceNow.

- [Configuring the AWS Service Catalog product widget components and assignment group for closed change records](https://docs.aws.amazon.com/smc/latest/ag/configure-sc-widget.html): Modify the AWS product view and associate the assignment group for change records from AWS Service Catalog post provision actions.
- [Granting access to AWS Service Catalog portfolios](https://docs.aws.amazon.com/smc/latest/ag/grant-access-portfolios.html): To grant access to Service Catalog products in ServiceNow, you must establish a link between the Service Catalog portfolios and the ServiceNow group.
- [Configuring AWS tags](https://docs.aws.amazon.com/smc/latest/ag/configure-aws-tags.html): Add tags (metadata) to provisioned products globally across the scoped app or granularly at the portfolio level.
- [Adding the My AWS Products widget to the Service Portal view](https://docs.aws.amazon.com/smc/latest/ag/add-aws-product-widget.html): Add the My AWS Products widget to the ServiceNow Portal view.
- [Activate AWS Service Catalog portfolio categorization in ServiceNow Service Portal](https://docs.aws.amazon.com/smc/latest/ag/sc-portfolio-categorization.html): Learn how to activate Portfolio categorization in the ServiceNow Portal and for existing users.
- [Viewing budgets related to Service Catalog portfolios and products](https://docs.aws.amazon.com/smc/latest/ag/view-budgets.html): Learn how to view budgets and actual costs related to Service Catalog portfolios and products in the ServiceNow standard user interface.
- [Validating AWS Service Catalog integration](https://docs.aws.amazon.com/smc/latest/ag/sn-sc-validate.html): This section describes how you can use service integration features to validate AWS Service Management Connector for ServiceNow installation.
- [Viewing products in the Standard User Interface](https://docs.aws.amazon.com/smc/latest/ag/view-products.html): View provisioned products as an end user and from the scoped app as an administrator.
- [Ordering Service Catalog products](https://docs.aws.amazon.com/smc/latest/ag/service-portal.html): The Connector for ServiceNow supports the ordering of Service Catalog products through Service Portal.

### [AWS Config](https://docs.aws.amazon.com/smc/latest/ag/sn-configure-config.html)

This section shows you how to use AWS Config to integrate to ServiceNow.

### [](https://docs.aws.amazon.com/smc/latest/ag/sn-configuration-integ.html)

This version of the AWS Service Management Connector enables ServiceNow administrators to configure system properties, Config aggregators, and AWS Config custom resources from select ServiceNow tables.

- [Validating the synchronization of Amazon WorkSpaces from AWS Config](https://docs.aws.amazon.com/smc/latest/ag/validating-config.html): Validate the synchronization of Amazon WorkSpaces in AWS Config by executing a scheduled job.
- [Addressing stale AWS Config items in the ServiceNow CMDB](https://docs.aws.amazon.com/smc/latest/ag/stale-config.html)
- [Configuring synchronization of AWS Config data using an Aggregator in ServiceNow CMDB](https://docs.aws.amazon.com/smc/latest/ag/config-sync.html): Prerequisite: You need to opt-in and configure the AWS account that contains the aggregated AWS Config resources details prior to performing the steps below.
- [Configuring available ServiceNow tables to sync as AWS Config custom resources](https://docs.aws.amazon.com/smc/latest/ag/custom-resources.html): In this Connector for ServiceNow release, you can now sync a set of ServiceNow tables in the CMDB to AWS Config as custom resources.
- [Validating AWS Config integration](https://docs.aws.amazon.com/smc/latest/ag/sn-validate-config.html): Configure the service settings to record data for the resource types of interest.
- [Updating the AWS Load Balancer resource details in the ServiceNow CMDB](https://docs.aws.amazon.com/smc/latest/ag/update-balancer.html): If you are upgrading from version 3 of the Connector to version 4, run fix scripts.

### [AWS Security Hub CSPM](https://docs.aws.amazon.com/smc/latest/ag/sn-config-security-hub.html)

View security Findings from AWS services such as Amazon Guard Duty and Amazon Inspector, as well as AWS Partner solutions.

- [Configuring AWS](https://docs.aws.amazon.com/smc/latest/ag/sn-security-hub-integ.html): This section describes how to configure your AWS services in ServiceNow.
- [Synchronizing AWS Security Hub CSPM to the Connector in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-synchronize-servicenow.html): This section shows you how to synchronize AWS Security Hub CSPM to the Connector in ServiceNow.
- [Validating AWS Security Hub CSPM integration](https://docs.aws.amazon.com/smc/latest/ag/sn-security-hub-validate.html): Learn how to validate AWS Security Hub CSPM integration in ServiceNow.

### [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/smc/latest/ag/sn-config-opscenter.html)

Integrate Systems Manager OpsCenter in ServiceNow.

- [Configuring ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-opscenter-integ.html): This section shows you how to integrate AWS Systems Manager OpsCenter in ServiceNow.
- [Validating AWS Systems Manager OpsCenter integration](https://docs.aws.amazon.com/smc/latest/ag/sn-opscenter-validate.html): This section describes how to validate AWS Systems Manager OpsCenter integration in ServiceNow.
- [Fields mapped from OpsCenter OpsItem records to ServiceNow Incident records](https://docs.aws.amazon.com/smc/latest/ag/fields-opsitems.html): Learn how AWS OpsItems map to ServiceNow Incidents.

### [AWS Systems Manager Automation](https://docs.aws.amazon.com/smc/latest/ag/sn-sm-automation.html)

To allow the Connector to execute Automation Documents, you must ensure that the Connector Sync and End user has the permissions required to sync and execute Automation Documents.

- [Validating AWS Systems Manager Automation integration](https://docs.aws.amazon.com/smc/latest/ag/sn-sm-automation-validate.html): This section describes how to validate AWS Systems Manager Automation integration in ServiceNow.

### [Support](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-support-integ.html)

AWS Service Management Connector allows AWS Managed Services (AMS) Accelerate users to create Incidents and Service Requests through ServiceNow.

- [Configuring Support integration in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-support-config-aws.html): This section describes how to configure Support integration in ServiceNow.
- [Configuring ServiceNow for integration with Support](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-support-config.html): This section shows you how to integrate Support in ServiceNow.
- [Advanced Mode for Support (optional)](https://docs.aws.amazon.com/smc/latest/ag/enabling-advanced-mode-aws-support.html): Learn about some advanced mode for Support options.
- [Validating Support integration](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-support-validate.html): This section describes how to manage integration features for Support in order to validate integration.

### [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/smc/latest/ag/sn-config-change-mgr.html)

AWS Service Management Connector includes a curated version of the Change Manager integration.

- [Configuring AWS](https://docs.aws.amazon.com/smc/latest/ag/sn-config-change-mgr-integ.html): Configure AWS roles for AWS Systems Manager and AutomationAssumeRole.
- [Configuring Support integration system properties with ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/changemanager-config.html): The AWS Systems Manager Change Manager integration for AWS Service Management Connector aligns with the Change Management process in ServiceNow.
- [Validating AWS Systems Manager Change Manager integration](https://docs.aws.amazon.com/smc/latest/ag/sn-config-change-mgr-validate.html): Perform tasks to validate AWS Systems Manager Change Manager integration in ServiceNow

### [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/smc/latest/ag/sn-im.html)

To allow the Connector to synchronize Incidents from AWS Systems Manager Incident Manager for a specific Region, you must enable Incident Manager in that account and Region.

- [Configuring ServiceNow for integration with AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/smc/latest/ag/sn-im-config.html): This section shows you how to integrate AWS Systems Manager Incident Manager in ServiceNow.
- [Validating AWS Systems Manager Incident Manager integration](https://docs.aws.amazon.com/smc/latest/ag/sn-im-validate.html): This section describes how to validate AWS Systems Manager Incident Manager integration in ServiceNow.

### [AWS Health](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-health.html)

AWS Health integration includes a dashboard that provides ongoing visibility into your resource performance and the availability of your AWS services and accounts.

- [Configuring AWS](https://docs.aws.amazon.com/smc/latest/ag/sn-config-health.html): This section describes how to configure AWS Health integration in ServiceNow.
- [Synchronizing AWS Health events with ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-health-configure.html): This section shows you how to synchronize AWS Health events with ServiceNow.
- [Validating AWS Health integration](https://docs.aws.amazon.com/smc/latest/ag/sn-health-validate.html): Validate the AWS Health integration in SeviceNow.
- [AWS Service Management Connector for ServiceNow Pricing](https://docs.aws.amazon.com/smc/latest/ag/sn-pricing.html): The AWS Service Management Connector for ServiceNow is a conventional ServiceNow scoped application developed and released through a ServiceNow Update Set.
- [Release notes](https://docs.aws.amazon.com/smc/latest/ag/sn-release-notes.html): Review release notes for AWS Service Management Connector for ServiceNow.
- [Reference: AWS API calls](https://docs.aws.amazon.com/smc/latest/ag/sn-api-ref.html): The following provides the reference AWS API calls for AWS Service Management Connector.
- [Updated key synchronization](https://docs.aws.amazon.com/smc/latest/ag/sn-sync-keys.html): AWS Service Management Connector for ServiceNow allows synchronization of updated keys using any automation or integration through a new REST endpoint.
- [Contacting the Connector specialist team](https://docs.aws.amazon.com/smc/latest/ag/sn-contact-SMC.html): In AWS Service Management Connector, you can now directly contact the AWS SMC Specialist team through an Support case directly from the Connector.
- [Upgrading to AWS Service Management Connector from a previous version](https://docs.aws.amazon.com/smc/latest/ag/transition-recommendations.html): To upgrade to AWS Service Management Connector from a previous Connector version in a ServiceNow Production instance, you must:


## [Connector for Jira Service Management Data Center](https://docs.aws.amazon.com/smc/latest/ag/integrations-jiraservicedesk.html)

- [Service management alignment](https://docs.aws.amazon.com/smc/latest/ag/service-mgmt-alignment.html): Learn how this Connector aligns to industry best practices, such as ITILÂ®âs service management areas by enabling tools (services) with the intersection of people, processes and partners.
- [Jira Service Management supported versions](https://docs.aws.amazon.com/smc/latest/ag/jsd-supported-versions.html): The AWS Service Management Connector (connector) for Jira Service Management Data Center supports Jira software (Jira Service Management) release for both the current and single prior version in each of the major, minor, and point release streams for:
- [Release notes](https://docs.aws.amazon.com/smc/latest/ag/jsd-integration-release-notes.html): Version 2.0.8 includes updates to core features.
- [Prerequisites for Jira Service Management Data Center](https://docs.aws.amazon.com/smc/latest/ag/jsd-integration-getting-started.html): Before installing the AWS Service Management Connector for Jira Service Management, you need an AWS account and an Atlassian instance with Jira Service Management pre-installed.

### [Setting up baseline AWS users and permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html)

Set up the baseline AWS users and permissions needed for the AWS Service Management Connector for Jira Service Management.

- [Creating AWS Service Management Connector Sync User](https://docs.aws.amazon.com/smc/latest/ag/jsd-creating-sc-sync-user.html): Create the AWS Connector sync user and associate the appropriate IAM permissions.
- [Creating AWS Service Management Connector End User](https://docs.aws.amazon.com/smc/latest/ag/jsd-creating-sc-end-user.html): Create the AWS Service Management Connector end user and associate the appropriate IAM permissions.
- [Creating SCConnectLaunch Role](https://docs.aws.amazon.com/smc/latest/ag/jsd-creating-scconnectlaunch-role.html): Create the SCConnectLaunch role to place baseline AWS service permissions into the Service Catalog launch constraints.

### [Configuring Service Catalog Integration](https://docs.aws.amazon.com/smc/latest/ag/jsd-integration-configure-sc.html)

Configure Service Catalog for the AWS Service Management Connector for Jira Service Management.

- [Creating Stack Set Constraint](https://docs.aws.amazon.com/smc/latest/ag/creating-stackset-constraint.html): CloudFormation StackSets enable users to create products that deploy across multiple accounts and Regions.
- [Configuring AWS Security Hub CSPM Integration](https://docs.aws.amazon.com/smc/latest/ag/config-security-hub.html): How to configure AWS Security Hub CSPM to view security findings from AWS services, such as Amazon Guard Duty, Amazon Inspector, as well as AWS Partner solutions.
- [Configuring Support Integration](https://docs.aws.amazon.com/smc/latest/ag/config-support.html): To enable the Connector to synchronize Support tickets, the account should have a Business or Enterprise Support plan.
- [Configuring AWS Systems Manager Incident Manager Integration](https://docs.aws.amazon.com/smc/latest/ag/jsd-integration-configure-incident-manager.html): To allow the Connector to synchronize Incidents from AWS Systems Manager Incident Manager for a specific Region, you must enable Incident Manager in that account and Region.

### [Configuring Jira Service Management](https://docs.aws.amazon.com/smc/latest/ag/jsd-integration-configure-jsd.html)

Configure Jira Service Management for the AWS Service Management Connector for Jira Service Management.

- [Installing Jira Service Management Connector add-on](https://docs.aws.amazon.com/smc/latest/ag/install-jsd-connector.html): Follow these steps to install the Jira Service Management Connector add-on.
- [Configuring AWS Accounts and Regions](https://docs.aws.amazon.com/smc/latest/ag/jsd-configure-accounts-regions.html): After you install the AWS Service Management Connector, you need to configure it.

### [Configuring Service Catalog portfolios in Jira](https://docs.aws.amazon.com/smc/latest/ag/config-SC-portfolios-jsd.html)

This section describes how to configure AWS Service Catalog portfolios within Jira.

- [Jira Service Management Approvals for Products in Service Catalog Portfolios](https://docs.aws.amazon.com/smc/latest/ag/jsd-product-approvals.html): The AWS Service Management Connector for Jira Service Management enables administrators to configure approvals for products at the portfolio level.
- [Products and budgets](https://docs.aws.amazon.com/smc/latest/ag/jsd-view-budgets.html): Two other tabs in the Admin - AWS Accounts - Manage section let you view information on portfolios.
- [Configuring Connector Settings (Jira Project Enablement and Request Type)](https://docs.aws.amazon.com/smc/latest/ag/jsd-configure-connector.html): In addition to configuring AWS accounts, the AWS Service Management Connector contains AWS services and UI settings (AWS Service Catalog) that enable projects and configure AWS Systems Manager OpsCenter.
- [Connector features enabled by default](https://docs.aws.amazon.com/smc/latest/ag/connector-features-default.html): Learn which Connector features are enabled by default.
- [Configuring UI Settings (AWS Service Catalog)](https://docs.aws.amazon.com/smc/latest/ag/settings-service-catalog.html): Configure the AWS Service Catalog product widget components to make them viewable to end users.
- [Configuring projects enabled for the Connector](https://docs.aws.amazon.com/smc/latest/ag/projects-connector.html): You can configure which Connector features are enabled for each Jira project.
- [Associate Jira projects to the AWS Systems Manager OpsCenter integration](https://docs.aws.amazon.com/smc/latest/ag/ops-center-config.html): Once you've enabled projects for the Connector, AWS Systems Manager OpsCenter requires Jira admins to associate Jira project(s) to this integration, as well as determine the full sync and delta sync intervals.
- [Associating Jira projects to the AWS Security Hub CSPM integration](https://docs.aws.amazon.com/smc/latest/ag/secure-hub-config.html): Associate the Jira projects enabled for the Connector to the AWS Security Hub CSPM integration features.
- [Associate Jira projects to the Support integration](https://docs.aws.amazon.com/smc/latest/ag/support-config.html): Learn how to associate the Jira projects enabled for the Connector to the AWS Systems Manager OpsCenter integration features.
- [Associating Jira projects to the AWS Systems Manager Incident Manager integration](https://docs.aws.amazon.com/smc/latest/ag/sys-man-incident-man.html): Learn how to associate the Jira projects enabled for the Connector to the AWS Systems Manager Incident Manager integration features
- [Configuring core operational settings](https://docs.aws.amazon.com/smc/latest/ag/core-ops-settings.html): Learn how to configure operational settings for the AWS Service Management Connector for Jira Service Management
- [Configuring automated tags for AWS Service Catalog](https://docs.aws.amazon.com/smc/latest/ag/auto-tags.html): Learn how to add tags (metadata) to AWS Service Catalog provisioned products globally across the add-on or granularly at the portfolio level.
- [Configuring project request type groups](https://docs.aws.amazon.com/smc/latest/ag/jsd-configure-request-type.html): The AWS request type must be in a group for users to be able to access it in Jira Service Management.

### [Setting up AWS resources through Jira Service Management to natively manage resources](https://docs.aws.amazon.com/smc/latest/ag/jsd-it-lifecycle.html)

Enable the IT Lifecycle Management for AWS Service Management Connector for Jira Service Management.

- [AWS Config Linked Resources](https://docs.aws.amazon.com/smc/latest/ag/jsd-config-linked-resources.html): The AWS Config Linked Resources field should be set to the JSON string representation of a list of objects (maps) corresponding to the linked resources.
- [AWS Systems Manager Automation Suggested Remediation](https://docs.aws.amazon.com/smc/latest/ag/jsd-sys-remediation.html): The AWS Systems Manager Automation Suggested Remediation field should be set to the JSON string that represents a list of objects (maps) that correspond to the automation documents as remediations.
- [Creating issues with suggestions and a linked AWS resource from AWS Systems Manager](https://docs.aws.amazon.com/smc/latest/ag/jsd-create-issues-linked-resource.html): A Systems Manager Automation Document can automatically create a Jira issue with the fields set to have a linked AWS resource and up to three suggested remediation documents.

### [Validating AWS Service Management Connector configurationsfor for Jira Service Management](https://docs.aws.amazon.com/smc/latest/ag/jsd-validate-configurations.html)

Validate configurations for the AWS Service Management Connector for Jira Service Management.

- [Service Catalog](https://docs.aws.amazon.com/smc/latest/ag/validate-sc.html): To validate Service Catalog integration, order a Service Catalog product or view provisioned products.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/smc/latest/ag/jsd-sys-automation.html): To validate AWS Systems Manager Automation integration, execute an automation document and view automation executions.
- [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/smc/latest/ag/opscenter.html): To validate AWS Systems Manager OpsCenter integration, manage OpsItems.
- [Support](https://docs.aws.amazon.com/smc/latest/ag/jsd-support-validation.html): To validate Support integration, manage Support cases and incidents.
- [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/smc/latest/ag/validate-sys-man-incident.html): To validate AWS Systems Manager Incident Manager integration, view and resolve AWS Systems Manager Incident Manager incidents.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/smc/latest/ag/jsd-security-hub.html): This section describes how to view AWS Security Hub CSPM Findings, update AWS Systems Manager OpsItems, and view AWS related resources in AWS Systems Manager OpsItems in Jira Service Management.
- [Jira approvals and access controls](https://docs.aws.amazon.com/smc/latest/ag/jsd-admin-features.html): Additional Jira administrator features for the AWS Service Management Connector for Jira Service Management.


## [Connector for Jira Service Management Cloud](https://docs.aws.amazon.com/smc/latest/ag/integrations-jsmcloud.html)

- [Service management alignment](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-service-mgmt-alignment.html): This Connector aligns with industry best practices, such as ITIL service management areas, and addresses a baseline set of service management practices you can use in existing tools.
- [Pricing](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-pricing.html): Learn about costs associated with AWS Service Management Connector for Atlassian's Jira Service Management Cloud.
- [Prerequisites](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-start.html): Before installing the AWS Service Management Connector for Atlassian's Jira Service Management Cloud, you must have an AWS account and an Atlassian site with Jira Service Management pre-installed.

### [Configuring baseline permissions for Jira Service Management Cloud](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-base-perms.html)

This section describes how to configure IAM permissions, Service Catalog, and other AWS services to use AWS Service Management Connector for Jira Service Management Cloud.

- [Creating AWS Service Management Connector Sync user](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-scsyncuser.html): This section describes how to create the AWS Sync user and associate the appropriate IAM permission.
- [Creating AWS Service Management Connector end user](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-scenduser.html): This section describes how to create the AWS Service Management Connector end user and associates the appropriate IAM permission.
- [Creating SCConnectLaunch role](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-scconnectlaunch.html): This section describes how to create the SCConnectLaunch role.

### [Configuring Jira Service Management Cloud](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-integration-config.html)

AWS Service Management Connector for Jira Service Management is based on Forge.

- [Installing AWS Service Management Connector](https://docs.aws.amazon.com/smc/latest/ag/install-jsm-connector.html): Install Service Management Connector in the Atlassian site.
- [Configuring AWS Accounts and Regions](https://docs.aws.amazon.com/smc/latest/ag/jsm-configure-accounts-regions.html): After installing the AWS Service Management Connector, you must configure AWS accounts and Regions in the connector.
- [Configuring Service Catalog Portfolios in Jira](https://docs.aws.amazon.com/smc/latest/ag/configure-SC-portfolios-in-jira.html): This section describes how to configure AWS Service Catalog portfolios within Jira.
- [Enabling the AWS Service Catalog request type in the Jira Customer Portal](https://docs.aws.amazon.com/smc/latest/ag/customer-portal.html): The Jira Customer Portal enables registered Atlassian site internal customers and Jira agents to provision resources using the Jira Service Management (JSM) AWS Service Catalog integration.
- [Enabling the Support request type in the Jira Customer Portal](https://docs.aws.amazon.com/smc/latest/ag/customer-portal-sup.html): The connector enables registered Atlassian site internal customers and Jira agents to create and manage Support cases using the Jira Service Management (JSM) Customer portal.

### [AWS Service Catalog](https://docs.aws.amazon.com/smc/latest/ag/cloud-configure-sc.html)

This section describes how to configure and validate Service Catalog to have a portfolio with an Amazon S3 bucket product.

### [Configuring AWS Service Catalog integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-config-sc.html)

This section provides the configurations you need to integrate AWS services in Jira Service Management Cloud.

- [Creating stack set constraints](https://docs.aws.amazon.com/smc/latest/ag/stackset-constraints.html): Enable users to create and deploy products across multiple accounts and Regions.
- [Relating budgets to products and portfolios](https://docs.aws.amazon.com/smc/latest/ag/cloud-budgets.html): View budgets related to Service Catalog products and portfolios
- [Validating AWS Service Catalog integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-sc-validate.html): Learn how you can use service integration features to validate AWS Service Management Connector for Jira Service Management Cloud installation.

### [AWS Security Hub CSPM](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-config-security-hub.html)

If you use both AWS Security Hub CSPM and Jira Service Management, the AWS Service Management Connector for Jira Service Management allows you to create an automated, bidirectional integration between Security Hub and Jira Service Management.

- [Configuring AWS Security Hub CSPM integration](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-security-hub-integ.html): Learn how to configure your AWS services in Jira Service Management Cloud.
- [Validating AWS Security Hub CSPM integration](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-security-hub-validate.html): Learn how to validate AWS Security Hub CSPM Findings, update AWS Systems Manager OpsItems, and view AWS related resources in Jira Service Management.

### [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-im.html)

To allow the Connector to synchronize Incidents from AWS Systems Manager Incident Manager for a specific Region, you must enable Incident Manager in that account and Region.

- [Configuring AWS Systems Manager Incident Manager integration](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-im-configure.html): To allow the connector to synchronize Incidents from AWS Systems Manager Incident Manager for a specific AWS region, you must first enable Incident Manager in that AWS account and region.
- [Validating AWS Systems Manager Incident Manager integration](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-im-validate.html): This section describes how to validate AWS Systems Manager Incident Manager integration in Jira.

### [Support](https://docs.aws.amazon.com/smc/latest/ag/cloud-configure-sup.html)

AWS Service Management Connector allows AWS Managed Services (AMS) Accelerate users to create Incidents and Service Requests through JSM Cloud.

- [Configuring Support integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-config-sup.html): Learn how to configure Support in Jira Service Management Cloud.
- [Validating Support integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-sup-validate.html): Learn how to create, view, and manage integration features of Support.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/smc/latest/ag/cloud-configure-sys.html): To allow the Connector to execute Automation Documents, you must ensure that the Connector's sync user and end user have the required permissions.

### [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/smc/latest/ag/systems-manager-opscenter.html)

To allow the Connector to synchronize AWS Systems Manager OpsCenter data for a specific Region, you must enable OpsCenter in that account and Region.

- [Configuring AWS Systems Manager OpsCenter integration](https://docs.aws.amazon.com/smc/latest/ag/systems-manager-opscenter-configure.html): Learn how to configure the AWS Systems Manager OpsCenter integration in Jira Service Management.
- [Validating AWS Systems Manager OpsCenter integration](https://docs.aws.amazon.com/smc/latest/ag/systems-manager-opscenter-validate.html): Learn how to validate the AWS Systems Manager OpsCenter integration in Jira.

### [AWS Health](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health.html)

This section describes how you can use AWS Health for Jira Service Management.

- [Configuring AWS Health integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health-configure.html): Learn how to configure AWS Health integration in Jira Service Management.
- [Validating AWS Health integration](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health-validate.html): Learn how to validate the AWS Health integration in Jira Service Management.
- [Reference: AWS API calls](https://docs.aws.amazon.com/smc/latest/ag/cloud-api-ref.html): This section provides the reference AWS API calls for AWS Service Management Connector.
- [Contacting the Connector specialist team](https://docs.aws.amazon.com/smc/latest/ag/cloud-contact-SMC.html): You can contact the AWS Service Management Connector (SMC) specialist team directly from the connector using an Support case.
- [Jira approvals and access controls](https://docs.aws.amazon.com/smc/latest/ag/cloud-add-admin-features.html): This section describes approvals and access controls that are available in Jira.
- [Release notes](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-integration-release-notes.html): The AWS Service Management Connector is for Atlassian's Jira Service Management Cloud, an application based on Forge.
- [Release history](https://docs.aws.amazon.com/smc/latest/ag/cloud-release-history.html): Review the release history for AWS Service Management Connector for Atlassian's Jira Service Management Cloud.
