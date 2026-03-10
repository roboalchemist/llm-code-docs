# Source: https://docs.aws.amazon.com/audit-manager/latest/userguide/llms.txt

# AWS Audit Manager User Guide

> Describes key concepts of AWS Audit Manager and provides instructions for using the features of AWS Audit Manager.

- [Using the dashboard](https://docs.aws.amazon.com/audit-manager/latest/userguide/dashboard.html)
- [Assessment reports](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessment-reports.html)
- [Download center](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html)
- [Notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/notifications.html)
- [Tagging resources](https://docs.aws.amazon.com/audit-manager/latest/userguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html)
- [Disabling AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/disable.html)
- [Document history](https://docs.aws.amazon.com/audit-manager/latest/userguide/doc-history.html)

## [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

- [Concepts and terminology](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html): Review and understand the definitions of the key concepts and terms used in Audit Manager, such as assessments, frameworks, and controls.
- [How evidence collection works](https://docs.aws.amazon.com/audit-manager/latest/userguide/how-evidence-is-collected.html): Learn about how Audit Manager gathers evidence for a resource assessment.
- [Examples of controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/examples-of-controls.html): Review examples of controls and learn how Audit Manager helps bring your AWS environment in line with their requirements.

### [Using AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/using-auditmanager.html)

Review different ways that you can use AWS Audit Manager.

- [Using Audit Manager with an AWS SDK](https://docs.aws.amazon.com/audit-manager/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders so you can quickly find the information that you need to build applications.
- [Using Audit Manager with CloudFormation](https://docs.aws.amazon.com/audit-manager/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for AWS Audit Manager using an AWS CloudFormation template.
- [Third-party GRC integrations](https://docs.aws.amazon.com/audit-manager/latest/userguide/third-party-integration.html): Provides information about the third-party GRC products that support integration with Audit Manager.
- [Integrating Audit Manager evidence into your GRC system](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-grc-integration.html): Follow this tutorial to understand how to integrate Audit Manager evidence into your GRC system.


## [Supported frameworks](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-overviews.html)

- [ACSC Essential Eight](https://docs.aws.amazon.com/audit-manager/latest/userguide/essential-eight.html): Provides an overview of the prebuilt Essential Eight standard framework that you can use to create assessments in Audit Manager.
- [ACSC ISM](https://docs.aws.amazon.com/audit-manager/latest/userguide/acsc-information-security-manual.html): Provides an overview of the prebuilt ACSC Information Security Manual standard framework that you can use to create assessments in Audit Manager.
- [AWS Audit Manager Sample Framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/Sample.html): Learn about the basic framework that Audit Manager provides to help you get started.
- [AWS Control Tower Guardrails](https://docs.aws.amazon.com/audit-manager/latest/userguide/controltower.html): Provides an overview of the prebuilt standard framework for AWS Control Tower that you can use to create assessments in Audit Manager.
- [AWS Generative AI Best Practices](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html): Provides an overview of the prebuilt standard framework for AWS generative AI Best Practices.
- [AWS License Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/Licensemanager.html): Provides an overview of the prebuilt standard framework for License Manager that you can use to create assessments in Audit Manager.
- [AWS Foundational Security Best Practices](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-foundational-security-best-practices.html): Provides an overview of the prebuilt standard framework for AWS Foundational Security Best Practices that you can use to create assessments in Audit Manager.
- [AWS Operational Best Practices](https://docs.aws.amazon.com/audit-manager/latest/userguide/OBP.html): Provides an overview of the prebuilt standard framework for AWS Operational Best Practices that you can use to create assessments in Audit Manager.
- [AWS Well Architected Framework WAF v10](https://docs.aws.amazon.com/audit-manager/latest/userguide/well-architected.html): Provides an overview of the prebuilt standard framework for AWS Well-Architected that you can use to create assessments in Audit Manager.
- [CCCS Medium Cloud Control Profile](https://docs.aws.amazon.com/audit-manager/latest/userguide/cccs-medium.html): Provides an overview of the prebuilt standard framework for CCCS Medium Cloud Control in Audit Manager.
- [CIS AWS Benchmark v.1.2](https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html): Provides an overview of the prebuilt standard frameworks for CIS AWS Benchmark v.1.2 in Audit Manager.
- [CIS AWS Benchmark v.1.3](https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-3.html): Provides an overview of the prebuilt standard framework for CIS AWS Benchmark v.1.3 in Audit Manager.
- [CIS AWS Benchmark v.1.4](https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-4.html): Provides an overview of the prebuilt standard framework for CIS AWS Benchmark v.1.4 in Audit Manager.
- [CIS Controls v7.1 IG1](https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-controls.html): Provides an overview of the prebuilt standard framework for CIS controls Implementation Group v7.1 in Audit Manager.
- [CIS Critical Security Controls version 8.0, IG1](https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-controls-v8.html): Provides an overview of the prebuilt standard framework for CIS Controls v8 in Audit Manager.
- [FedRAMP Security Baseline Controls r4](https://docs.aws.amazon.com/audit-manager/latest/userguide/fedramp-moderate.html): Provides an overview of the prebuilt standard framework for the FedRAMP Moderate Baseline.
- [GDPR 2016](https://docs.aws.amazon.com/audit-manager/latest/userguide/GDPR.html): Provides an overview of the prebuilt standard framework for GDPR that you can use to create assessments in Audit Manager.
- [GLBA](https://docs.aws.amazon.com/audit-manager/latest/userguide/gramm-leach-bliley-act.html): Provides an overview of the prebuilt standard framework for the Gramm-Leach-Bliley Act that you can use to create assessments in Audit Manager.
- [Title 21 CFR Part 11](https://docs.aws.amazon.com/audit-manager/latest/userguide/GxP.html): Provides an overview of the prebuilt standard framework for Title 21 CFR Part 11 that you can use to create assessments in Audit Manager.
- [EU GMP Annex 11, v1](https://docs.aws.amazon.com/audit-manager/latest/userguide/GxP-EU-Annex-11.html): Provides an overview of the prebuilt standard framework for GMP EU Annex 11 that you can use to create assessments in Audit Manager.
- [HIPAA Security Rule: Feb 2003](https://docs.aws.amazon.com/audit-manager/latest/userguide/HIPAA.html): Provides an overview of the prebuilt standard framework for HIPAA that you can use to create assessments in Audit Manager.
- [HIPAA Omnibus Final Rule](https://docs.aws.amazon.com/audit-manager/latest/userguide/HIPAA-omnibus-rule.html): Provides an overview of the prebuilt standard framework for HIPAA that you can use to create assessments in Audit Manager.
- [ISO/IEC 27001:2013](https://docs.aws.amazon.com/audit-manager/latest/userguide/iso-27001-2013.html): Provides an overview of the prebuilt standard framework for ISO IEC 27001 2013 Annex A in Audit Manager.
- [NIST SP 800-53 R5](https://docs.aws.amazon.com/audit-manager/latest/userguide/NIST800-53r5.html): Provides an overview of the prebuilt standard framework for NIST 800-53 (Rev. 5) that you can use to create assessments in Audit Manager.
- [NIST CSF v1.1](https://docs.aws.amazon.com/audit-manager/latest/userguide/NIST-Cybersecurity-Framework-v1-1.html): Provides an overview of the prebuilt standard framework for NIST Cybersecurity Framework version 1.1 that you can use to create assessments in Audit Manager.
- [NIST SP 800-171 R2](https://docs.aws.amazon.com/audit-manager/latest/userguide/NIST-800-171-r2-1.1.html): Provides an overview of the prebuilt standard framework for NIST SP 800-171 that you can use to create assessments in Audit Manager.
- [PCI DSS v3.2.1](https://docs.aws.amazon.com/audit-manager/latest/userguide/PCI.html): Provides an overview of the prebuilt standard framework for PCI DSS v3.2.1 that you can use to create assessments in Audit Manager.
- [PCI DSS v4](https://docs.aws.amazon.com/audit-manager/latest/userguide/pci-v4.html): Provides an overview of the prebuilt standard framework for PCI DSS v4 that you can use to create assessments in Audit Manager.
- [SSAE-18 SOC 2](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html): Provides an overview of the prebuilt standard framework for SOC 2 that you can use to create assessments in Audit Manager.


## [Supported data sources](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources.html)

- [AWS Config](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html): Review a list of the supported AWS Config Rules that Audit Manager can collect findings for.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html): Review a list of the supported Security Hub CSPM controls that Audit Manager can collect findings for.
- [AWS API calls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html): Review a list of the supported AWS API calls that Audit Manager can use to automatically generate evidence for the controls in your assessments.
- [AWS CloudTrail](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-cloudtrail.html): Review a list of the CloudTrail event names that are not currently supported as data sources in Audit Manager.


## [Setting up](https://docs.aws.amazon.com/audit-manager/latest/userguide/setting-up.html)

- [Prerequisites](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-prerequisites.html): Learn about the requirements that you must complete before you can set up Audit Manager.
- [Enabling Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html): Learn how to enable Audit Manager.
- [Recommendations](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-recommendations.html): Learn about the recommended Audit Manager features and integrations.


## [Getting started](https://docs.aws.amazon.com/audit-manager/latest/userguide/getting-started.html)

- [Tutorial for Audit Owners: Creating an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-audit-owners.html): Follow these steps to start using Audit Manager.
- [Tutorial for Delegates: Reviewing a control set](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-delegates.html): Follow this step-by-step tutorial to start using AWS Audit Manager.


## [Assessments](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessments.html)

- [Creating an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html): Learn how to use Audit Manager to create an assessment based on the compliance framework of your choice.
- [Finding an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-assessments.html): Learn how to view a list of your active and inactive assessments in Audit Manager.

### [Reviewing an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-assessment.html)

Review and understand the different parts of an assessment detail page in Audit Manager.

- [Assessment details](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-assessments.html): Review and understand the different parts of an assessment detail page in Audit Manager.
- [Assessment control details](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-controls.html): Review and understand the different parts of a assessment control summary page in Audit Manager.
- [Evidence folder details](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-evidence-folders-detail.html): Review the evidence folders that Audit Manager creates for the controls in your assessment.
- [Evidence details](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-evidence.html): Review and understand the evidence that Audit Manager collects for the controls in your assessment.
- [Editing an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-assessment.html): Learn how to change the settings for your active assessments in Audit Manager, such as modifying the description, scope, audit owners, and report destination.

### [Adding manual evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html)

Learn how to manually add evidence to your assessments so that you can demonstrate compliance with controls that don't support automatic evidence collection.

- [Importing evidence from S3](https://docs.aws.amazon.com/audit-manager/latest/userguide/import-from-s3.html): Learn how you can manually import evidence from an S3 bucket into your Audit Manager assessment.
- [Uploading evidence from a browser](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-from-computer.html): Learn how you can manually upload evidence from your computer into your Audit Manager assessment.
- [Entering text as evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/enter-text-response.html): Learn how you can add text to a control and save that text as manual evidence in your Audit Manager assessment.
- [Supported file formats](https://docs.aws.amazon.com/audit-manager/latest/userguide/supported-manual-evidence-files.html): Learn which file formats you can use as manual evidence in your Audit Manager assessments.

### [Preparing an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html)

Learn how you can select relevant evidence and use it to create a report about your Audit Manager assessment.

- [Adding evidence to an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report-include-evidence.html): Learn how you can select the relevant evidence that you want to include in your Audit Manager assessment report.
- [Removing evidence from an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report-remove-evidence.html): Learn how you can select the relevant evidence that you want to remove from your Audit Manager assessment report.
- [Generating an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report-generation-steps.html): Learn how you can generate an Audit Manager assessment report.
- [Changing an assessment control status](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-control-status.html): Learn how to change the status of an assessment control in Audit Manager.
- [Changing an assessment status](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-status-to-inactive.html): Learn how to change the status of an assessment to inactive in Audit Manager after you have completed an audit.
- [Deleting an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html): Learn how to delete an assessment that you no longer need in Audit Manager.


## [Delegations](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegate.html)

### [For audit owners](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegate-for-audit-owners.html)

Review the process for delegating a control set in AWS Audit Manager to be reviewed by a subject matter expert.

- [Delegating a control set](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-audit-owners-delegating-a-control-set.html): Review the process for delegating a control set in AWS Audit Manager to be reviewed by a subject matter expert.
- [Finding delegations](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-audit-owners-reviewing-delegations.html): Review the process for viewing a list of your active and completed delegations.
- [Deleting delegations](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-audit-owners-cancel-delegations.html): If you are an audit owner, you can delegate control sets for review.

### [For delegates](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates.html)

Review the process for delegating a control set in AWS Audit Manager to be reviewed by a subject matter expert.

- [Viewing notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-viewing-notifications.html): Review the process for checking your notifications in AWS Audit Manager when a delegation request is shared with you.
- [Reviewing controls and evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-reviewing-control-set-and-evidence.html): Review the process for reviewing a control set in AWS Audit Manager and examining its related evidence.
- [Adding comments](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-add-comment.html): Review the process changing the current status of a control set in AWS Audit Manager to reflect your review progress.
- [Marking a control as reviewed](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-changing-control-status.html): Review the process of changing the current status of a control set in AWS Audit Manager to reflect your review progress.
- [Submitting a control set to the audit owner](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-submitting-back-to-audit-owner.html): Review the process for submitting a control set back to the audit owner after you have completed your review.


## [Evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html)

- [Searching for evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/search-for-evidence-in-evidence-finder.html): Learn how to use evidence finder to query your Audit Manager evidence.
- [Viewing your search results](https://docs.aws.amazon.com/audit-manager/latest/userguide/viewing-search-results-in-evidence-finder.html): Learn how to preview the evidence that you found and how to create a report from it.
- [Exporting your search results](https://docs.aws.amazon.com/audit-manager/latest/userguide/exporting-search-results-from-evidence-finder.html): Learn how to export the evidence that you found and how to create a report from it.
- [Filter and grouping options](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-filters-and-groups.html): Discover the filters and groups that help you refine and navigate your search results.
- [Example use cases](https://docs.aws.amazon.com/audit-manager/latest/userguide/example-use-cases-for-evidence-finder.html): Discover how you might use evidence finder to help you as you prepare for audits.


## [Framework library](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-library.html)

- [Finding a framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-frameworks.html): Learn how to view a list of the available compliance frameworks in Audit Manager that you can use to create assessments.
- [Reviewing a framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-frameworks.html): Use this reference page to understand the details and definitions for frameworks in Audit Manager.

### [Creating a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/custom-frameworks.html)

Create a custom framework for your specific use case.

- [Creating from scratch](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-custom-frameworks-from-scratch.html): Learn how you can use Audit Manager to create and configure a new framework that meets your specific use case.
- [Making an editable copy](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-custom-frameworks-from-existing.html): Learn how you can use an existing framework in Audit Manager as a starting point and make an editable copy that meets your specific needs.
- [Editing a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-custom-frameworks.html): Learn how you can review and update the details of the custom frameworks that you create in Audit Manager.

### [Sharing a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework.html)

Learn how to share a custom Audit Manager framework across AWS accounts and AWS Regions.

- [Concepts and terminology](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html): Review key concepts and terms to help you get started with custom framework sharing in AWS Audit Manager.
- [Sending a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html): Learn how to share your custom frameworks across AWS accounts and Regions.
- [Responding to a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/responding-to-shared-framework-requests.html): Learn how to accept or decline a shared framework request from another AWS account.
- [Deleting a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/deleting-shared-framework-requests.html): Learn how to delete an unwanted share request from your framework library.
- [Deleting a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html): Learn how to delete custom frameworks in Audit Manager that are no longer needed.


## [Control library](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library.html)

- [Finding a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html): Learn how you can use the control library to view a list of the available controls in Audit Manager.

### [Reviewing a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-controls.html)

Use this reference page to understand the details and definitions seen on a control page in Audit Manager.

- [Common controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-common-controls.html): Describes the details and definitions seen on a common control page in Audit Manager.
- [Core controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-core-controls.html): Describes the details and definitions seen on a core control page in Audit Manager.
- [Standard controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-standard-controls.html): Describes the details and definitions seen on a standard control page in Audit Manager.
- [Custom controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-custom-controls.html): Describes the details and definitions seen on a custom control page in Audit Manager.

### [Creating a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-controls.html)

Create a control in Audit Manager for your custom use case.

- [Creating from scratch](https://docs.aws.amazon.com/audit-manager/latest/userguide/customize-control-from-scratch.html): Learn how you can use Audit Manager to create and configure a new control that meets your specific use case.
- [Making an editable copy](https://docs.aws.amazon.com/audit-manager/latest/userguide/customize-control-from-existing.html): Describes how to use an existing control in Audit Manager as a starting point and then make an editable copy that meets your specific needs.

### [Editing a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html)

Learn how you can review and update the details of the custom controls that you create in Audit Manager.

- [Changing evidence collection frequency](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-evidence-collection-frequency.html): Learn about how often Audit Manager collects evidence for each control data source, and in which cases you can specify your preferred frequency.
- [Deleting a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html): Learn how to delete custom controls in Audit Manager that are no longer needed.


## [Settings](https://docs.aws.amazon.com/audit-manager/latest/userguide/console-settings.html)

- [Configuring your data encryption settings](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-KMS.html): Learn how to configure Audit Manager and update your data encryption settings to reflect your specific preferences.
- [Adding a delegated administrator](https://docs.aws.amazon.com/audit-manager/latest/userguide/add-delegated-admin.html): Learn how to configure Audit Manager and add a delegated administrator to manage assessments for your organization.
- [Changing a delegated administrator](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-delegated-admin.html): Learn how to configure Audit Manager and change a delegated administrator to manage assessments for your organization.
- [Removing a delegated administrator](https://docs.aws.amazon.com/audit-manager/latest/userguide/remove-delegated-admin.html): Learn how to configure Audit Manager and remove a delegated administrator to manage assessments for your organization.
- [Configuring your default audit owners](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-default-audit-owner.html): Learn how to configure Audit Manager and update your default audit owner settings to reflect your specific preferences.
- [Configuring your default assessment report destination](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-destination.html): Learn how to configure Audit Manager and update your default assessment report destination to reflect your specific preferences.
- [Configuring your Audit Manager notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-notifications.html): Learn how to configure Audit Manager and update your notification settings to reflect your specific preferences.
- [Enabling evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-settings-enable.html): Learn how to configure Audit Manager and enable the evidence finder feature so that you can start querying your evidence.
- [Confirming the status of evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/confirm-status-of-evidence-finder.html): Learn how to check the status of your request to enable the evidence finder feature in Audit Manager.
- [Disabling evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-settings-disable.html): Learn how to configure Audit Manager and disable the evidence finder feature when you want to stop using the feature.
- [Configuring your default export destination](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-export-destination.html): Learn how to configure Audit Manager and update your default CSV export destination to reflect your specific preferences.


## [Troubleshooting](https://docs.aws.amazon.com/audit-manager/latest/userguide/troubleshooting.html)

- [Troubleshooting assessments and evidence collection](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-collection-issues.html): Find the solutions to common assessment and evidence collection issues in AWS Audit Manager.
- [Troubleshooting assessment reports](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessment-report-issues.html): Find the solutions to common issues with assessment reports in AWS Audit Manager.
- [Troubleshooting controls and control sets](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-issues.html): Find the solutions to common issues with controls and control sets in AWS Audit Manager.
- [Troubleshooting the dashboard](https://docs.aws.amazon.com/audit-manager/latest/userguide/dashboard-issues.html): Find the solutions to common dashboard issues in AWS Audit Manager.
- [Troubleshooting delegated administrators and AWS Organizations](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegated-admin-issues.html): Find the solutions to common Organizations and delegated administrator issues in AWS Audit Manager.
- [Troubleshooting evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-issues.html): Find the solutions to common evidence finder issues in AWS Audit Manager.
- [Troubleshooting frameworks](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-issues.html): Find the solutions to common framework issues in AWS Audit Manager.
- [Troubleshooting notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/notification-issues.html): Find the solutions to common notification issues in AWS Audit Manager.
- [Troubleshooting permissions and access](https://docs.aws.amazon.com/audit-manager/latest/userguide/permissions-issues.html): Find the solutions to common permissions and access issues in AWS Audit Manager.


## [Code examples](https://docs.aws.amazon.com/audit-manager/latest/userguide/service_code_examples.html)

### [Scenarios](https://docs.aws.amazon.com/audit-manager/latest/userguide/service_code_examples_scenarios.html)

The following code examples show how to use Audit Manager with AWS SDKs.

- [Create a custom framework from an AWS Config conformance pack](https://docs.aws.amazon.com/audit-manager/latest/userguide/example_auditmanager_Scenario_CustomFrameworkFromConformancePack_section.html): Create an Audit Manager custom framework from an AWS Config conformance pack using an AWS SDK
- [Create a custom framework that contains Security Hub CSPM controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/example_auditmanager_Scenario_CustomFrameworkFromSecurityHub_section.html): Create an Audit Manager custom framework that contains Security Hub CSPM controls using an AWS SDK
- [Create an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/example_auditmanager_Scenario_CreateAssessmentReport_section.html): Create an Audit Manager assessment report that contains one day of evidence using an AWS SDK


## [Security](https://docs.aws.amazon.com/audit-manager/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Audit Manager.

### [Identity and access management](https://docs.aws.amazon.com/audit-manager/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access your Audit Manager resources.

- [How AWS Audit Manager works with IAM](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_service-with-iam.html): Learn about the IAM features that are supported in Audit Manager.
- [Identity-based policy examples](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html): Review some example identity-based policies that you can use in Audit Manager.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/audit-manager/latest/userguide/cross-service-confused-deputy-prevention.html): Learn more about the confused deputy problem in AWS, and see examples of how you can avoid this type of security issue when you use AWS Audit Manager.
- [Resource-based policy examples](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_resource-based-policy-examples.html): View examples of resource-based policies that you can use with AWS Audit Manager.
- [AWS managed policies](https://docs.aws.amazon.com/audit-manager/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Audit Manager and review recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_troubleshoot.html): Troubleshoot common issues related to authentication and authorization in Audit Manager.
- [Using service-linked roles](https://docs.aws.amazon.com/audit-manager/latest/userguide/using-service-linked-roles.html): Learn how to use service-linked roles to give Audit Manager access to resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/audit-manager/latest/userguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/audit-manager/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Audit Manager features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/audit-manager/latest/userguide/infrastructure-security.html): Learn how AWS Audit Manager is protected by AWS global network security, and how Audit Manager isolates network access within the AWS network.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/audit-manager/latest/userguide/vpc-interface-endpoints.html): Create a private connection between your VPC and Audit Manager via an interface VPC endpoint, without internet access, NAT device, VPN, or Direct Connect.

### [Logging and monitoring](https://docs.aws.amazon.com/audit-manager/latest/userguide/security-logging-and-monitoring.html)

Monitor Audit Manager to maintain reliability, availability, and performance.

- [Monitoring with Amazon EventBridge](https://docs.aws.amazon.com/audit-manager/latest/userguide/automating-with-eventbridge.html): Automate Audit Manager with other AWS services by using EventBridge.
- [CloudTrail logs](https://docs.aws.amazon.com/audit-manager/latest/userguide/logging-using-cloudtrail.html): Learn about how you can use CloudTrail to log Audit Manager API calls.
- [Configuration and vulnerability](https://docs.aws.amazon.com/audit-manager/latest/userguide/vulnerability-analysis-and-management.html): Explains the shared responsibility for configuration and IT controls for Audit Manager.
