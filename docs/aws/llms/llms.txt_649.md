# Source: https://docs.aws.amazon.com/partner-central/latest/crm/llms.txt

# AWS Partner Central CRM Guide

> Describes how to get started with the CRM integration.

- [Creating a custom integration with the Partner Central API](https://docs.aws.amazon.com/partner-central/latest/crm/create-custom-integration.html)
- [Integration FAQ](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-faq.html)
- [Glossary](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-glossary.html)

## [What is CRM integration?](https://docs.aws.amazon.com/partner-central/latest/crm/aws-partner-crm-integration.html)

- [Integration options](https://docs.aws.amazon.com/partner-central/latest/crm/routes-for-crm-integration.html): The options for creating a CRM integration: the CRM connector, a third-party integration, or a custom integration.
- [Integration prerequisites](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-setting-up.html): The prerequisites needed for a custom CRM integration, and for using the CRM connector.
- [Working with referrals, leads, and opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-business-flows.html): Learn the basics of referrals, leads, and opportunities, and the types of referrals created by AWS Sales.

### [Getting started](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-getting-started.html)

How to start the process of creating a CRM integration.

- [Linking your AWS Partner Central and AWS Marketplace accounts](https://docs.aws.amazon.com/partner-central/latest/crm/link-pc-mkt-accounts.html): The steps for linking an AWS Partner Central account with an AWS Marketplace account.

### [Creating the IAM user in your AWS Marketplace seller account](https://docs.aws.amazon.com/partner-central/latest/crm/create-iam-user-seller-account.html)

The steps for creating the IAM user that enables Salesforce to connect with your AWS Marketplace seller account.

- [Creating the IAM user](https://docs.aws.amazon.com/partner-central/latest/crm/create-user-steps.html): Follow these steps to create the IAM user in your AWS Marketplace seller account.
- [Setting Amazon S3 permissions for the IAM user](https://docs.aws.amazon.com/partner-central/latest/crm/s3-iam-perms.html): The permissions needed for the AWS Marketplace IAM user to interact with the Amazon S3 bucket.
- [Maintaining an integration](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-ongoing-maintenance.html): Learn about routine maintenance for a CRM Integration.
- [Troubleshooting an integration](https://docs.aws.amazon.com/partner-central/latest/crm/troubleshooting.html): The following topics explain how to create a support case and troubleshoot common onboarding and integration errors.
- [Partner Central API setup](https://docs.aws.amazon.com/partner-central/latest/crm/guided-setup-apis.html): The steps for setting up the AWS Partner Central API.


## [What is the AWS Partner CRM connector?](https://docs.aws.amazon.com/partner-central/latest/crm/aws-partner-crm-connector.html)

- [CRM connector overview](https://docs.aws.amazon.com/partner-central/latest/crm/connector-overview.html): The concepts and terms behind the AWS Partner Customer Relationship Management (CRM) connector.
- [Available features](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-feature-list.html): Learn the features of the AWS Partner Central API and the AWS Partner CRM connector for Salesforce.
- [Installing the connector](https://docs.aws.amazon.com/partner-central/latest/crm/install-connector.html): Learn how to install the AWS Partner Customer Relationship Management (CRM) connector and integrate Salesforce with AWS Partner Central and AWS Marketplace.
- [Upgrading the connector to the latest version](https://docs.aws.amazon.com/partner-central/latest/crm/upgrading-from-previous-versions.html): Learn how to upgrade the AWS Partner CRM connector.
- [Setting up real-time notifications](https://docs.aws.amazon.com/partner-central/latest/crm/set-up-real-time-notifications.html): How to add real-time EventBridge notifications for AWS Partner Central and AWS Marketplace events.

### [Mapping ACE objects](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-mapping.html)

Learn how to map objects and fields between Salesforce and an earlier CRM with Amazon S3 integration.

- [Using the ACE Mappings page](https://docs.aws.amazon.com/partner-central/latest/crm/mapping-page.html): AWS Partner Central provides the following ways to navigate to the ACE Mappings page:
- [Multi-object mapping](https://docs.aws.amazon.com/partner-central/latest/crm/multi-object-mappings.html): Multi-object mapping allows partners to map AWS fields to a primary source object, such as an opportunity or lead, and to the Salesforce objects related to the primary source.
- [Picklist mapping](https://docs.aws.amazon.com/partner-central/latest/crm/picklist-mapping.html): The picklist dialog box allows limited and extended mappings between the partnerâs picklist field and APN.
- [Sync logs and reports](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-sync-logs-and-reports.html): Learn about the synchronization logs with Amazon Web Services and the reports included with the AWS Partner CRM connector package

### [Configuring the CRM connector](https://docs.aws.amazon.com/partner-central/latest/crm/configure-crm-connector.html)

How to configure the AWS Partner CRM connector for use with AWS Partner Central, the AWS Partner network, and AWS Marketplace.

- [Using guided setup](https://docs.aws.amazon.com/partner-central/latest/crm/use-guided-setup.html): You always use Salesforce to configure the CRM connector, and you start on the Guided setup tab.

### [Configuring the connector for a Partner Central API integration](https://docs.aws.amazon.com/partner-central/latest/crm/p-c-api-integration.html)

The following sections explain how to configure the CRM connector for use with the AWS Partner Central APIs.

- [Using flow templates](https://docs.aws.amazon.com/partner-central/latest/crm/flow-templates.html): Learn how to use pre-built Salesforce flow templates to integrate with AWS Partner Central.

### [Configuring the connector for AWS Marketplace](https://docs.aws.amazon.com/partner-central/latest/crm/aws-marketplace-integration.html)

Learn how AWS partners can manage private offers and resale authorizations directly from Salesforce with the AWS Partner Partner CRM connector.

- [Onboarding an AWS Seller account](https://docs.aws.amazon.com/partner-central/latest/crm/onboard-seller-account.html): The following steps explain how to onboard AWS Seller accounts to the CRM connector.
- [Entering system configuration settings](https://docs.aws.amazon.com/partner-central/latest/crm/mkt-system-config.html): The system configuration settings needed for an AWS Marketplace integration.
- [Entering custom settings](https://docs.aws.amazon.com/partner-central/latest/crm/mkt-custom-settings.html): The settings for the Amazon S3 bucket that stores the custom EULAs for an AWS Marketplace CRM integration.

### [Personas for CRM connector permission sets](https://docs.aws.amazon.com/partner-central/latest/crm/permission-sets.html)

The personas supported by the CRM connector permissions sets.

- [AWS Partner Network permission sets](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-pemissions-sets.html): The CRM connector supports the following primary AWS Partner Network personas:
- [AWS Marketplace permission sets](https://docs.aws.amazon.com/partner-central/latest/crm/mkt-permissions-sets.html): The permission sets and values that enable a Salesforce user to perform tasks in AWS Marketplace.
- [CRM connector tabs and permission sets](https://docs.aws.amazon.com/partner-central/latest/crm/permission-set-table.html): A table that lists and describes the permission sets allowed to use the tabs provided by the CRM connector app.

### [Using the CRM connector in Salesforce](https://docs.aws.amazon.com/partner-central/latest/crm/using-the-connector.html)

Learn how to use Salesforce with the AWS Partner CRM connector.

### [Managing ACE opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/manage-ace-opportunities.html)

How to use the AWS Partner CRM connector to manage ACE opportunities.

- [Creating partner-originated opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/create-partner-opportunity.html): The following steps explain how to create a partner-originated opportunity.
- [Viewing opportunity records](https://docs.aws.amazon.com/partner-central/latest/crm/viewing-opportunities.html): How to use the AWS Partner CRM connector to view opportunity records.
- [Updating an opportunity's stage](https://docs.aws.amazon.com/partner-central/latest/crm/update-opportunity-stage.html): The following steps explain how to update an opportunity's stage.
- [Cloning an opportunity](https://docs.aws.amazon.com/partner-central/latest/crm/clone-opportunity.html): Cloning enables you to create a new opportunity that contains details from an existing opportunity.

### [Managing opportunities in a Partner Central API integration](https://docs.aws.amazon.com/partner-central/latest/crm/manage-aws-opportunities.html)

How to use the AWS Partner CRM connector to manage sales opportunities from AWS Sales.

- [Accepting or rejecting AWS originated opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/accept-reject-aws-opportunity.html): The following steps explain how to accept or reject an opportunity that originates from AWS Sales.
- [Assigning an opportunity to another user](https://docs.aws.amazon.com/partner-central/latest/crm/assign-opportunity.html): The following steps explain how to assign an opportunity to another user in your Partner Central account.
- [Associating or dissociating an opportunity](https://docs.aws.amazon.com/partner-central/latest/crm/associate-disassociate-opportunity.html): The following steps explain how to associate and disassociate an opportunity from Partner Solutions, AWS products, or AWS Marketplace offers.
- [Accepting multiple opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/accepting-multiple-opportunities.html): You can accept multiple AWS-originated opportunities simultaneously using the bulk accept functionality.
- [Assigning multiple opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/assigning-multiple-opportunities.html): You can assign multiple opportunities to another user in your Partner Central account simultaneously using the bulk assign functionality.

### [Managing opportunities in a CRM with Amazon S3 integration](https://docs.aws.amazon.com/partner-central/latest/crm/manage-s3-opportunities.html)

The following topics explain how to use the CRM connector with a CRM with Amazon S3 integration.

- [Importing solutions into Salesforce](https://docs.aws.amazon.com/partner-central/latest/crm/import-solutions-tab.html): How to import solutions from Partner Central into Salesforce by using the Solution Offerings tab in Salesforce.
- [Accepting or rejecting AWS-originated opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/accept-reject-opportunities.html): The following steps explain how to accept or reject opportunities in an APN Amazon S3 integration.
- [Synchronizing opportunity and lead data](https://docs.aws.amazon.com/partner-central/latest/crm/send-receive-opportunities-leads.html): To sync an opportunity or lead with APN, you must set the Sync with Partner Central field to True.
- [Linking AWS Marketplace private offers to ACE opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/link-private-offer-to-opportunity.html): You can link private offers directly from the AWS delivered ACE opportunity record page in Salesforce.
- [Viewing sync log detail records for ACE opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/view-ace-details.html): You can view sync log details for AWS-delivered ACE opportunities on the Related section of the ACE opportunity record.

### [Managing AWS Marketplace activities](https://docs.aws.amazon.com/partner-central/latest/crm/crm-manage-marketplace.html)

The following topics explain how to use the CRM connector to manage AWS Marketplace activities from within Salesforce.

- [Synchronizing Salesforce with your AWS Marketplace products](https://docs.aws.amazon.com/partner-central/latest/crm/crm-sync-salesforce.html): Before you can work with AWS Marketplace products, you must first synchronize them with Salesforce.
- [Managing private offers](https://docs.aws.amazon.com/partner-central/latest/crm/crm-manage-private-offers.html): The following topics explain how to use Salesforce to create and manage private offers for your AWS Marketplace products.
- [Managing AWS Marketplace agreements](https://docs.aws.amazon.com/partner-central/latest/crm/crm-manage-agreements.html): The following topics explain how AWS sellers and Channel Partners can use the CRM connector to access agreements and view agreement details.
- [Managing AWS Marketplace resale authorizations](https://docs.aws.amazon.com/partner-central/latest/crm/crm-resale-authorizations.html): As an ISV, you can authorize an AWS Channel Partner to resell your products by creating a resale authorization directly within Salesforce using the AWS Partner CRM Connector.

### [Using an earlier CRM with Amazon S3 integration](https://docs.aws.amazon.com/partner-central/latest/crm/custom-integration-using-amazon-s3.html)

Learn how to integrate your CRM system with the AWS SDK for SAP ABAP Customer Engagement Pipeline manager.

### [Upgrading to the Partner Central API](https://docs.aws.amazon.com/partner-central/latest/crm/upgrade-crm-api.html)

- [Upgrade features](https://docs.aws.amazon.com/partner-central/latest/crm/api-upgrade-features.html): The advantages of upgrading from a CRM with Amazon S3 integration to the AWS Partner Central API.
- [Set up named credentials](https://docs.aws.amazon.com/partner-central/latest/crm/set-up-api-credentials.html): How to set up named credentials needed to upgrade from an Amazon S3 integration to the AWS Partner Central API.
- [Add the Approval Status button to the Opportunity Lightning Record page](https://docs.aws.amazon.com/partner-central/latest/crm/add-approval-status-button.html): How to add the Approval Status button to an Opportunity Lightning Record page.
- [Add the remaining buttons](https://docs.aws.amazon.com/partner-central/latest/crm/add-remaining-buttons.html): How to add more buttons to Lightning Records pages and finish upgrading to the AWS Partner Central API.
- [Refresh the Solution Offerings tab](https://docs.aws.amazon.com/partner-central/latest/crm/refresh-the-solutions-from-the-solution-offerings-tab.html): After you complete the steps for migrating to the AWS Partner Central API, you confirm

### [Configuring the connector for a CRM with Amazon S3 integration](https://docs.aws.amazon.com/partner-central/latest/crm/s3-config.html)

- [Production checklist](https://docs.aws.amazon.com/partner-central/latest/crm/ace-production-checklist.html): Follow these steps to complete the production installation of your AWS Partner CRM connector.
- [Upgrading AWS Partner CRM connector to the new data model](https://docs.aws.amazon.com/partner-central/latest/crm/connector-upgrade-plan.html): Learn how to upgrade the AWS Partner CRM connector to the new data model.
- [Sandbox testing with the custom ACE opportunity and ACE lead objects](https://docs.aws.amazon.com/partner-central/latest/crm/custom-ace-opportunity.html): TBD
- [Integration resources](https://docs.aws.amazon.com/partner-central/latest/crm/resources.html): Deprecated.
- [Lead sharing](https://docs.aws.amazon.com/partner-central/latest/crm/custom-lead-sharing.html)
- [Opportunity sharing](https://docs.aws.amazon.com/partner-central/latest/crm/custom-opportunity-sharing.html)
- [Field mapping](https://docs.aws.amazon.com/partner-central/latest/crm/custom-field-mapping.html): Field mapping is an essential step in the integration process where partners align their customer relationship management (CRM) systemâs fields with those defined by Amazon Web Services (AWS).
- [Creating synchronization schedules](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-scheduling.html): Learn how to schedule inbound and outbound sync operations between Salesforce and the AWS Partner Network.
- [Best practices](https://docs.aws.amazon.com/partner-central/latest/crm/best-practices.html): Use these best practices to optimize your custom integration development and maintenance.
- [Quotas](https://docs.aws.amazon.com/partner-central/latest/crm/quotas.html)
- [Version history](https://docs.aws.amazon.com/partner-central/latest/crm/version-history.html): Current fields version: 14 (November 15, 2023)

### [FAQs](https://docs.aws.amazon.com/partner-central/latest/crm/faqs.html)

Use these common questions and answers to assist in the custom integration.

- [General FAQ](https://docs.aws.amazon.com/partner-central/latest/crm/general-faq.html)
- [Technical FAQâfields](https://docs.aws.amazon.com/partner-central/latest/crm/technical-faq-fields.html): Q: Does the integration support CSV format?
- [Technical FAQâAmazon S3](https://docs.aws.amazon.com/partner-central/latest/crm/technical-faq-s3.html): Q: Where can I get the Amazon Simple Storage Service (Amazon S3) REST API documentation?
- [Technical FAQâleads and opportunities](https://docs.aws.amazon.com/partner-central/latest/crm/technical-faq-leads-and-opps.html)
- [Technical FAQâversioning and backward compatibility](https://docs.aws.amazon.com/partner-central/latest/crm/technical-faq-versioning.html): Q: What is a payload in Amazon Web Services (AWS) data exchange?
- [Getting help](https://docs.aws.amazon.com/partner-central/latest/crm/getting-help.html): Learn how to get help with AWS Partner CRM connector
- [AWS Partner CRM connector FAQ](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-faq.html): AWS Partner CRM connector frequently asked questions (FAQs).
- [Release notes](https://docs.aws.amazon.com/partner-central/latest/crm/crm-connector-release-notes.html): Learn about the release history for the AWS Partner Customer Relationship Management (CRM) Connector.
