# Source: https://docs.aws.amazon.com/proton/latest/userguide/llms.txt

# AWS Proton User Guide

> Provides an overview of AWS Proton and how your team can use it to create and manage infrastructure and deployment tools for your cloud services or applications.

- [Tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/proton/latest/userguide/ag-troubleshooting.html)
- [AWS Proton quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html)
- [Document history](https://docs.aws.amazon.com/proton/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/proton/latest/userguide/glossary.html)

## [What is AWS Proton?](https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html)

- [Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html): AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026.


## [Setting up](https://docs.aws.amazon.com/proton/latest/userguide/ag-setting-up.html)

- [Setting up with IAM](https://docs.aws.amazon.com/proton/latest/userguide/ag-setting-up-iam.html): When you sign up for AWS, your AWS account is automatically signed up for all services in AWS, including AWS Proton.
- [Setting up with AWS Proton](https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html): If you want to use the AWS CLI to run AWS Proton APIs, verify that you have installed it.


## [Getting started](https://docs.aws.amazon.com/proton/latest/userguide/ag-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/proton/latest/userguide/getting-started-prerequisites.html): Before you start using AWS Proton, make sure that the following prerequisites are met.
- [Getting started workflow](https://docs.aws.amazon.com/proton/latest/userguide/ag-admin-workflow.html): Learn to create template bundles, create and register templates, and create environments and services by following the example steps and links.
- [Getting started with the console](https://docs.aws.amazon.com/proton/latest/userguide/ag-getting-started-console.html)
- [Getting started with the CLI](https://docs.aws.amazon.com/proton/latest/userguide/ag-getting-started-cli.html): To get started with AWS Proton using the AWS CLI, follow this tutorial.
- [Template library](https://docs.aws.amazon.com/proton/latest/userguide/ag-getting-started-templates.html): The AWS Proton team maintains a library of template examples on GitHub.


## [How AWS Proton works](https://docs.aws.amazon.com/proton/latest/userguide/ag-works.html)

- [Objects](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-objects.html): Learn about AWS Proton objects and their relationship to other AWS and third-party objects.
- [Provisioning methods](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html): AWS Proton can provision infrastructure in one of several ways:
- [AWS Proton terminology](https://docs.aws.amazon.com/proton/latest/userguide/terminology.html)


## [Template authoring and bundles](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html)

### [Parameters](https://docs.aws.amazon.com/proton/latest/userguide/parameters.html)

Learn how to define and use parameters in your AWS Proton infrastructure as code (IaC) files to make them flexible and re-usable.

- [Environment CloudFormation IaC parameters](https://docs.aws.amazon.com/proton/latest/userguide/env-parameters.html): You can define and reference parameters in your environment infrastructure as code (IaC) files.
- [Service CloudFormation IaC parameters](https://docs.aws.amazon.com/proton/latest/userguide/svc-parameters.html): You can define and reference parameters in your service and pipeline infrastructure as code (IaC) files.
- [Component CloudFormation IaC parameters](https://docs.aws.amazon.com/proton/latest/userguide/comp-parameters.html): You can define and reference parameters in your component infrastructure as code (IaC) files.
- [CloudFormation parameter filters](https://docs.aws.amazon.com/proton/latest/userguide/parameter-filters.html): When you make references to AWS Proton parameters in your AWS CloudFormation IaC files, you can use Jinja modifiers known as filters to validate, filter, and format parameter values before they get inserted into the rendered template.
- [CodeBuild provisioning parameters](https://docs.aws.amazon.com/proton/latest/userguide/parameters-codebuild.html): You can define parameters in your templates for CodeBuild-based AWS Proton resources and reference these parameters in your provisioning code.
- [Terraform IaC parameters](https://docs.aws.amazon.com/proton/latest/userguide/env-parameters-tform.html): You can include Terraform input variables in variable.tf files in your template bundle.

### [Infrastructure as code files](https://docs.aws.amazon.com/proton/latest/userguide/ag-infrastructure-tmp-files.html)

Learn how to author infrastructure as code (IaC) files for AWS Proton templates.

- [CloudFormation IaC files](https://docs.aws.amazon.com/proton/latest/userguide/ag-infrastructure-tmp-files-cloudformation.html): Learn how to use AWS CloudFormation infrastructure as code (IaC) files in AWS Proton template bundles.
- [CodeBuild bundle](https://docs.aws.amazon.com/proton/latest/userguide/ag-infrastructure-tmp-files-codebuild.html): Learn how to use CodeBuild provisioning with AWS Proton.
- [Terraform IaC files](https://docs.aws.amazon.com/proton/latest/userguide/ag-infrastructure-tmp-files-terraform.html): Learn how to use Terraform infrastructure as code (IaC) files in AWS Proton template bundles.
- [Schema file](https://docs.aws.amazon.com/proton/latest/userguide/ag-schema.html): Learn how to author schema files to define input parameters for AWS Proton template bundles.
- [Manifest and wrap up](https://docs.aws.amazon.com/proton/latest/userguide/ag-wrap-up.html): Learn how to author manifest files to wrap up AWS Proton template bundles.
- [Template bundle considerations](https://docs.aws.amazon.com/proton/latest/userguide/template-considerations.html)


## [Templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html)

- [Versions](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-versions.html): As an administrator or a member of a platform team, you define, create, and manage a library of versioned templates that are used to provision infrastructure resources.
- [Publish](https://docs.aws.amazon.com/proton/latest/userguide/template-create.html): You can register and publish environment and service templates with AWS Proton, as described in the following sections.
- [View templates](https://docs.aws.amazon.com/proton/latest/userguide/template-view.html): You can view lists of templates with details and view individual templates with detail data by using the AWS Proton console and AWS CLI.
- [Update a template](https://docs.aws.amazon.com/proton/latest/userguide/template-update.html): You can update a template as described in the following list.
- [Delete templates](https://docs.aws.amazon.com/proton/latest/userguide/template-delete.html): Templates can be deleted using the console and AWS CLI.

### [Template sync configurations](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html)

Create template sync configurations with AWS Proton.

- [Create](https://docs.aws.amazon.com/proton/latest/userguide/create-template-sync.html): Learn how to create a template sync configuration with AWS Proton.
- [View](https://docs.aws.amazon.com/proton/latest/userguide/view-template-sync.html): View template sync configuration detail data using the console or CLI.
- [Edit](https://docs.aws.amazon.com/proton/latest/userguide/update-template-sync.html): You can edit any of the template sync configuration parameters except template-name and template-type.
- [Delete](https://docs.aws.amazon.com/proton/latest/userguide/delete-template-sync.html): Delete a template sync configuration using the console or CLI.

### [Service sync configurations](https://docs.aws.amazon.com/proton/latest/userguide/ag-service-sync-configs.html)

Create service sync configurations with AWS Proton.

- [Create](https://docs.aws.amazon.com/proton/latest/userguide/create-service-sync.html): Learn how to create a service sync configuration with AWS Proton.
- [View](https://docs.aws.amazon.com/proton/latest/userguide/get-service-sync.html): Learn how to view the configuration details for a service sync.
- [Edit](https://docs.aws.amazon.com/proton/latest/userguide/update-service-sync.html): Learn how to edit an AWS Proton service sync configuration using the console or AWS CLI.
- [Delete](https://docs.aws.amazon.com/proton/latest/userguide/delete-service-sync.html): Learn how to delete a service sync configuration.


## [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html)

- [IAM Roles](https://docs.aws.amazon.com/proton/latest/userguide/ag-environment-roles.html): With AWS Proton, you supply the IAM roles and AWS KMS keys for the AWS resources that you own and manage.
- [Create](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-env.html): Learn to create AWS Proton environments.
- [View](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-view.html): You can view environment detail data using either the AWS Proton console or the AWS CLI.
- [Update](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html): If the AWS Proton environment is associated with an environment account connection, don't update or include the protonServiceRoleArn parameter to update or connect to an environment account connection.
- [Delete](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-delete.html): You can delete an AWS Proton environment by using the AWS Proton console or the AWS CLI.
- [Account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html): Overview
- [Customer-managed](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-customer-managed.html): With customer-managed environments, you can use existing infrastructure, like a VPC, that you already have deployed as your AWS Proton environment.
- [CodeBuild provisioning role creation](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-codebuild-provisioning-role-creation.html): Infrastructure as a Code (IaaC) tools like CloudFormation and Terraform require permissions for the many different types of AWS resources.


## [Services](https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html)

- [Create](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html): To deploy an application with AWS Proton, as a developer, you create a service and provide the following inputs.
- [View](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-view.html): You can view and list service detail data using the AWS Proton console or the AWS CLI.
- [Edit](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html): You can make the following edits to an AWS Proton service.
- [Delete](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-delete.html): You can delete an AWS Proton service, with its instances and pipeline, by using the AWS Proton console or the AWS CLI.
- [View instances](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-view.html): Learn to view AWS Proton service instance detail data.
- [Update instance](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html): Learn to update an AWS Proton service instance and cancel the update.
- [Update pipeline](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html): Learn to update an AWS Proton service pipeline and cancel the update.


## [Components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html)

- [Component states](https://docs.aws.amazon.com/proton/latest/userguide/ag-components-states.html): AWS Proton components can be in two fundamentally different states:
- [Component IaC files](https://docs.aws.amazon.com/proton/latest/userguide/ag-components-iac.html): Component infrastructure as code (IaC) files are similar to those for other AWS Proton resources.
- [Component CloudFormation example](https://docs.aws.amazon.com/proton/latest/userguide/ag-components-example-cfn.html): Here is a complete example of an AWS Proton directly defined component and how you can use it in an AWS Proton service.


## [Repositories](https://docs.aws.amazon.com/proton/latest/userguide/ag-repositories.html)

- [Create a repository link](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-repo.html): You can create a link to your repository using the console or CLI.
- [View linked repository data](https://docs.aws.amazon.com/proton/latest/userguide/ag-repo-view.html): You can list and view linked repository details using the console or the AWS CLI.
- [Delete a repository link](https://docs.aws.amazon.com/proton/latest/userguide/ag-repo-delete.html): You can delete a repository link by using the console or the AWS CLI.


## [Monitoring](https://docs.aws.amazon.com/proton/latest/userguide/monitoring.html)

- [Automate AWS Proton with EventBridge](https://docs.aws.amazon.com/proton/latest/userguide/event-bridge.html): You can monitor AWS Proton events in Amazon EventBridge.
- [EventBridgeTutorial: Send Amazon Simple Notification Service alerts for AWS Proton service status changes](https://docs.aws.amazon.com/proton/latest/userguide/event-tutorial-sns.html): In this tutorial, you use an AWS Proton pre-configured event rule that captures status changes for your AWS Proton service.
- [AWS Proton dashboard](https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html): Use the AWS Proton dashboard to view deployed service instances and how updated they are relative to recommended major and minor template versions.


## [Security](https://docs.aws.amazon.com/proton/latest/userguide/ag-security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/proton/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS Proton resources.

- [How AWS Proton works with IAM](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Proton, learn what IAM features are available to use with AWS Proton.

### [Policy examples](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_policy-examples.html)

Find AWS Proton IAM policy examples in the following sections.

- [Identity-based policy examples](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Proton resources.
- [Service role policy examples](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-role-policy-examples.html): Administrators own and manage the resources that AWS Proton creates as defined by the environment and service templates.
- [Condition-key based policy examples](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_condition-key-based-policy-examples.html): The following example IAM policy denies access to AWS Proton actions that match the templates specified in the Condition block.
- [AWS managed policies](https://docs.aws.amazon.com/proton/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Proton and recent changes to those policies.

### [Using service-linked roles](https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give AWS Proton access to resources in your AWS account.

- [Sync roles](https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles-sync.html): How to use service-linked roles to give AWS Proton access to resources in your AWS account.
- [CodeBuild role](https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles-codebuild.html): How to use service-linked roles to give AWS Proton access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/proton/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Proton and IAM.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/proton/latest/userguide/vulnerability-analysis-and-management.html): Describes the customer responsibility regarding updates and patches in AWS Proton.
- [Data protection](https://docs.aws.amazon.com/proton/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Proton.
- [Infrastructure security](https://docs.aws.amazon.com/proton/latest/userguide/infrastructure-security.html): Learn how AWS Proton isolates service traffic.
- [Logging and monitoring](https://docs.aws.amazon.com/proton/latest/userguide/security-logging-and-monitoring.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Proton features for data resiliency.
- [Resilience](https://docs.aws.amazon.com/proton/latest/userguide/disaster-recovery-resiliency.html): Describes AWS architecture for data redundancy and specific AWS Proton services for data resiliency.
- [Security best practices](https://docs.aws.amazon.com/proton/latest/userguide/security-best-practices.html): Describes guidelines and best practices for addressing security issues in AWS Proton.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/proton/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Codebuild custom support](https://docs.aws.amazon.com/proton/latest/userguide/vpc-codebuild-custom-support.html): AWS Proton CodeBuild Provisioning executes arbitrary customer-supplied CLI commands in a CodeBuild project located in the AWS Proton Environment account.
