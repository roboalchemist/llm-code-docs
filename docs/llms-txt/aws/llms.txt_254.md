# Source: https://docs.aws.amazon.com/controltower/latest/userguide/llms.txt

# AWS Control Tower User Guide

> Describes key concepts for AWS Control Tower. Provides instructions for setting up and using a landing zone, a secure and compliant multi-account AWS environment for enterprises or organizations at scale.

- [Terminology](https://docs.aws.amazon.com/controltower/latest/userguide/terminology.html)
- [Pricing](https://docs.aws.amazon.com/controltower/latest/userguide/pricing.html)
- [Setting up](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html)
- [The Controls Reference Guide](https://docs.aws.amazon.com/controltower/latest/userguide/link-to-new-guide.html)
- [Manage resources](https://docs.aws.amazon.com/controltower/latest/userguide/about-resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/controltower/latest/userguide/troubleshooting.html)
- [Additional information](https://docs.aws.amazon.com/controltower/latest/userguide/related-information.html)
- [Document history](https://docs.aws.amazon.com/controltower/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/controltower/latest/userguide/glossary.html)

## [What Is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

### [How it works](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html)

How AWS Control Tower works.

- [What are the shared accounts?](https://docs.aws.amazon.com/controltower/latest/userguide/what-shared.html): In AWS Control Tower, the shared accounts in your landing zone are provisioned during setup: the management account, the log archive account, and the audit account.
- [How controls work](https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html): A control is a high-level rule that provides ongoing governance for your overall AWS environment.


## [Getting started](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)

- [Quick start guide](https://docs.aws.amazon.com/controltower/latest/userguide/quick-start.html): If you are new to AWS, you can follow the steps in this section to get started quickly with AWS Control Tower.
- [Pre-launch checks](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-prereqs.html): Learn about the automated pre-launch checks that make sure your management account is ready for changes that establish your landing zone.

### [Setup your controls dedicated environment](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up-controls-dedicated-environment.html)

Learn how to get started with AWS Control Tower by setting up a controls dedicated environment.

- [Getting Started](https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-getting-started.html): Learn about steps for setting up a minimal landing zone for controls only experience.
- [AWS Config Considerations](https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-considerations.html): Learn about steps for setting up AWS Config integration on a minimal landing zone for controls only experience with detective controls.
- [Implementation Process](https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-implement.html): Learn about the minimal landing zone for controls only experience with and without detective controls.
- [Important Notes](https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-notes.html): Learn about the minimal landing zone for controls only experience.

### [Get started from the console](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-from-console.html)

Learn how to get started with AWS Control Tower from the console.

- [Expectations for landing zone configuration](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-configure.html): Learn about configuration expectations when setting up a landing zone.
- [Step 1: Create your shared account email addresses](https://docs.aws.amazon.com/controltower/latest/userguide/step-one.html): Learn about the email addresses that are required for your audit account and log archive account.

### [Step 2. Configure and launch your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/step-two.html)

Learn how to configure and launch your landing zone by first determining the most appropriate home Region.

- [Step 2a. Review and select your AWS Regions](https://docs.aws.amazon.com/controltower/latest/userguide/pricing-and-regions.html): Learn how to configure and launch your landing zone by selecting any additional AWS Regions and determining whether certain AWS Regions should be denied access to AWS resources.
- [Step 2b. Configure your organizational units (OUs)](https://docs.aws.amazon.com/controltower/latest/userguide/configure-ous.html): Learn how to configure and launch your landing zone by accepting or changing the default names of your organizational units (OUs).

### [Step 2c. Configure your shared accounts, logging, and encryption](https://docs.aws.amazon.com/controltower/latest/userguide/configure-shared-accounts.html)

Learn how to configure and launch your landing zone by deciding whether to customize the names of your audit and log archive accounts, optionally specifying exisiting AWS accounts as your shared accounts, and providing unique email addresses for your audit and log archive accounts.

- [Optionally configure log retention](https://docs.aws.amazon.com/controltower/latest/userguide/configure-log-retention.html): Learn how to configure and launch your landing zone by deciding whether to customize the log retention policy.
- [Optionally self-manage AWS account access](https://docs.aws.amazon.com/controltower/latest/userguide/select-idp.html): You can select whether AWS Control Tower sets up AWS account access with AWS Identity and Access Management (IAM), or whether to self-manage AWS account accessâeither with AWS IAM Identity Center users, roles, and permissions that you can set up and customize on your own, or with another method such as an external IdP, either for direct account federation or federation to multiple accounts by means of IAM Identity Center.
- [Optionally configure AWS CloudTrail trails](https://docs.aws.amazon.com/controltower/latest/userguide/configure-org-trails.html): Learn how to configure and launch your landing zone by deciding whether to set up logging.
- [Optionally configure AWS KMS keys](https://docs.aws.amazon.com/controltower/latest/userguide/configure-kms-keys.html): Learn how to configure and launch your landing zone by deciding whether to encrypt and decrypt resources with AWS KMS keys.
- [Optionally configure auto-enrollment for accounts](https://docs.aws.amazon.com/controltower/latest/userguide/configure-auto-enroll.html): Learn to configure automatic account enrollment
- [Optionally configure and create customized member accounts](https://docs.aws.amazon.com/controltower/latest/userguide/configure-customized-accounts.html): Learn how to configure and launch your landing zone by deciding whether to specify a previously-defined blueprint for provisioning customized member accounts
- [Step 3. Review and set up the landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/review-and-set-up.html): Learn how to configure and launch your landing zone by reviewing service permissions and finshing setting up your landing zone.

### [Get started using APIs](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-apis.html)

Learn about how to get started with AWS Control Tower using APIs.

- [Expectations for landing zone configuration with APIs](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-expectations-api.html): Learn about configuration expectations when setting up a landing zone using APIs.
- [Step 1: Configure your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-prereques.html): The process of setting up your AWS Control Tower landing zone has multiple steps.
- [Step 2: Launch your landing zone using the AWS Control Tower APIs](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch.html): You can use AWS Control Tower APIs to launch your landing zone.
- [Identify your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-list.html): Calling ListLandingZones can help you determine if your account is already set up with AWS Control Tower.
- [Update your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-update.html): When a new landing zone version is available, or to make other updates to your landing zone configuration, you can call the UpdateLandingZone API and reference an updated landing zone manifest file.
- [Reset the landing zone to resolve drift](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-reset.html): When you create your landing zone, the landing zone and all the organizational units (OUs), accounts, and resources are compliant with the governance rules enforced by your chosen controls.
- [View the details of your landing zone manifest file](https://docs.aws.amazon.com/controltower/latest/userguide/lz-manifest-file.html): Learn about Landing Zone setup operations.
- [View the status of your landing zone operations](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-examples-short.html): Learn about Landing Zone operations.
- [Examples: Set up an AWS Control Tower landing zone with APIs only](https://docs.aws.amazon.com/controltower/latest/userguide/walkthrough-api-setup.html): This walkthrough of examples is a companion document.
- [Landing zone schemas](https://docs.aws.amazon.com/controltower/latest/userguide/landing-zone-schemas.html): AWS Control Tower landing zones are created using specific schemas, with each version having a unique schema definition.

### [Launch a landing zone using CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/lz-apis-cfn.html)

Learn how to launch a landing zone using CloudFormation.

- [Prerequisites for using CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/lz-apis-cfn-setup.html)
- [Create a new landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-apis-cfn-launch.html): From the CloudFormation console or using the AWS CLI, deploy the following CloudFormation template to create a landing zone.
- [Manage existing landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-apis-cfn-launch-existing.html): You can use CloudFormation to manage a landing zone that you have already launched by importing the landing zone in a new or existing CloudFormation stack.
- [Next steps](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-next.html): Learn more about how you can use AWS Control Tower.


## [Limitations and quotas](https://docs.aws.amazon.com/controltower/latest/userguide/limits.html)

- [Request a quota increase](https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html): AWS Control Tower provides service quotas that can be viewed and, in some cases, adjusted through the Service Quotas console.
- [Control limitations](https://docs.aws.amazon.com/controltower/latest/userguide/control-limitations.html): Learn about the limitations and considerations for AWS Control Tower controls, including regional restrictions and the impact of modifying AWS Control Tower resources.
- [Limitations based on underlying AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/region-stackset-limitations.html): AWS Control Tower faces limitations based on underlying AWS services, particularly when registering organizational units (OUs) with a large number of accounts across multiple Regions.
- [Regional differences](https://docs.aws.amazon.com/controltower/latest/userguide/regional-differences.html): AWS Control Tower functionality varies across AWS Regions due to the availability of underlying AWS services it orchestrates.


## [Best practices for administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html)

- [Plan your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/planning-your-deployment.html): When you go through the setup process, AWS Control Tower launches a key resource associated with your account, called a landing zone, which serves as a home for your organizations and their accounts.
- [Best practices: Set up an AWS multi-account landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html): AWS Control Tower customers often seek guidance about how to set up their AWS environment and accounts for best results.Â AWS has created a unified set of recommendations, called the multi-account strategy, to help you make the best use of your AWS resources, including your AWS Control Tower landing zone.
- [Administrative tips for landing zone setup](https://docs.aws.amazon.com/controltower/latest/userguide/tips-for-admin-setup.html): Learn about tips for setting up a landing zone as the administrator.

### [Landing Zone v4.0 migration guide](https://docs.aws.amazon.com/controltower/latest/userguide/landing-zone-v4-migration-guide.html)

Learn about updates related to Landing Zone 4.0 and quick guide for migration onto version 4.0 and above

- [Key changes](https://docs.aws.amazon.com/controltower/latest/userguide/key-changes-lz-v4.html)
- [AWS Config Updates](https://docs.aws.amazon.com/controltower/latest/userguide/config-updates-v4.html)
- [Recommendations for setting up groups, roles, and policies](https://docs.aws.amazon.com/controltower/latest/userguide/roles-recommendations.html): Learn about recommendations for granting users access to accounts when setting up your landing zone.
- [Guidance about AWS Control Tower resources](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-guidance.html): Learn about best practices for creating and modifying resources in AWS Control Tower.
- [When to sign in as a root user](https://docs.aws.amazon.com/controltower/latest/userguide/root-login.html): Learn about administrative tasks/actions that require you to sign in as the root user.
- [AWS Organizations guidance](https://docs.aws.amazon.com/controltower/latest/userguide/orgs-guidance.html): Learn about guidance for using AWS Control Tower with AWS Organizations.
- [IAM Identity Center guidance](https://docs.aws.amazon.com/controltower/latest/userguide/sso-guidance.html): Learn about resources that you can use to understand how AWS IAM Identity Center interacts with AWS Control Tower.
- [Account Factory guidance](https://docs.aws.amazon.com/controltower/latest/userguide/af-guidance.html): Learn about isses that can occur when provisioning accounts in Account Factory and how you might troubleshoot them.
- [Guidance on subscribing to SNS Topics](https://docs.aws.amazon.com/controltower/latest/userguide/sns-guidance.html): Learn about subscribing to SNS topics in AWS Control Tower.
- [Guidance for KMS keys](https://docs.aws.amazon.com/controltower/latest/userguide/kms-guidance.html): Learn about best practices for using AWS Control Tower with AWS Key Management Service.
- [Landing zone updates](https://docs.aws.amazon.com/controltower/latest/userguide/lz-update-best-practices.html): Find the best practices to use when you update your landing zone version on AWS Control Tower
- [Policies for AI-based services](https://docs.aws.amazon.com/controltower/latest/userguide/ai-opt-out.html): You can create service control policies (SCPs) that allow you to opt out of having your data stored by AI-based services on AWS.


## [Configuration update management](https://docs.aws.amazon.com/controltower/latest/userguide/configuration-updates.html)

- [About updates](https://docs.aws.amazon.com/controltower/latest/userguide/about-updates.html): AWS Control Tower requires various types of updates to correct governance drift and adopt new versions, including landing zone updates, individual account updates, and full updates.
- [Update your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/update-controltower.html): Updating the AWS Control Tower landing zone can be done through the Landing zone settings page, which shows the current version and available updates.
- [Select a landing zone version](https://docs.aws.amazon.com/controltower/latest/userguide/lz-version-selection.html): How to select a landing zone version.
- [Retain account trails](https://docs.aws.amazon.com/controltower/latest/userguide/retain-account-trails.html): Learn how to retain account-level trails when you upgrade your landing zone version on AWS Control Tower
- [Resolve drift with Reset and Re-register](https://docs.aws.amazon.com/controltower/latest/userguide/resolve-drift.html): AWS Control Tower automatically detects drift in landing zone configurations and provides methods to resolve it, including the Reset and Re-register features in the console and programmatic options.
- [Provision and update accounts using automation](https://docs.aws.amazon.com/controltower/latest/userguide/update-accounts-by-script.html): AWS Control Tower offers multiple methods for provisioning and updating individual accounts, including AWS Control Tower Account Factory for Terraform (AFT), Customizations for AWS Control Tower (CfCT), and script automation using Service Catalog APIs.


## [Automate tasks](https://docs.aws.amazon.com/controltower/latest/userguide/automating-tasks.html)

### [AWS CloudShell and the AWS CLI](https://docs.aws.amazon.com/controltower/latest/userguide/using-aws-with-cloudshell.html)

Learn about how you can use AWS CloudShell to work with AWS Control Tower through the CLI.

- [Interact with AWS Control Tower through AWS CloudShell](https://docs.aws.amazon.com/controltower/latest/userguide/cshell-examples.html): After you launch AWS CloudShell from the AWS Management Console, you can immediately start to interact with AWS Control Tower from the command line interface.
- [AWS CloudFormation resources](https://docs.aws.amazon.com/controltower/latest/userguide/creating-resources-with-cloudformation.html): Learn about how to create resources for AWS Control Tower using an AWS CloudFormation template.


## [Customize your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/customize-landing-zone.html)

- [Customize from the AWS Control Tower console](https://docs.aws.amazon.com/controltower/latest/userguide/console-customize.html): To make these customizations to your landing zone, follow the steps given by the AWS Control Tower console.
- [Automate customizations outside the AWS Control Tower console](https://docs.aws.amazon.com/controltower/latest/userguide/automate-customizations.html): Some customizations are not available through the AWS Control Tower console, but they can be implemented in other ways.
- [AWS Control Tower and LZA](https://docs.aws.amazon.com/controltower/latest/userguide/about-lza.html): This section describes the benefits of working with AWS Control Tower and the Landing Zone Accelerator (LZA) solution, together.

### [Customizations for AWS Control Tower (CfCT) overview](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html)

Learn about customizations for AWS Control Tower.

- [Architecture](https://docs.aws.amazon.com/controltower/latest/userguide/architecture.html): Learn about the CfCT architecture.
- [Cost](https://docs.aws.amazon.com/controltower/latest/userguide/cost.html): Learn about the cost of CfCT.
- [Component services](https://docs.aws.amazon.com/controltower/latest/userguide/components.html): Learn about customizations for AWS Control Tower components
- [Deployment considerations](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-considerations.html): Learn about considerations when deploying customizations for AWS Control Tower.
- [Template and source code](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-template.html): Learn about deploying customizations for AWS Control Tower.

### [Deploy CfCT](https://docs.aws.amazon.com/controltower/latest/userguide/deployment.html)

Learn about the step-by-step deployment instructions for setting up CfCT.

- [Step 1. Launch the stack](https://docs.aws.amazon.com/controltower/latest/userguide/step1.html): Learn how to launch the stack, so you can deploy CfCT.
- [Step 2. Create a custom package](https://docs.aws.amazon.com/controltower/latest/userguide/step2.html): Learn about creating a custom package to deploy CfCT.
- [Update the stack](https://docs.aws.amazon.com/controltower/latest/userguide/update-stack.html): Learn how to update the stack after deploying CfCT.
- [Delete a stack set](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-delete-stack.html): Learn how to delete a stack if you enabled stack set deletion in your manifest file.
- [Set up Amazon S3 as the configuration source](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-s3-source.html): Learn how to set up Amazon Simple Storage Service as the configuration source if you choose to modify the configuration file.
- [Set up GitHub as the configuration source](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-github-configuration-source.html): Learn how to set up GitHub as the configuration source if you choose to modify the configuration file.
- [Operational metrics](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-metrics.html): Overview of Customizations for AWS Control Tower operational metrics on AWS.

### [CfCT customization guide](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-customizations-dev-guide.html)

Learn about the Customizations for AWS Control Tower (CfCT) guide.

- [Code pipeline overview](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-codepipeline-overview.html): Learn about the configuration package for CfCT and AWS CodePipeline.

### [Define a custom configuration](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-custom-configuration.html)

You'll define your custom AWS Control Tower configuration with the CfCT manifest file, the accompanying set of templates, and other JSON files.

- [The CfCT manifest file](https://docs.aws.amazon.com/controltower/latest/userguide/the-manifest-file.html): The CfCT manifest.yaml file is a text file that describes your AWS resources.
- [The resources section of the CfCT manifest file](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-manifest-file-resources-section.html): Learn about the resources section of the CfCT manifest file.
- [Root OU](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-root-ou.html): Learn about the Root OU feature.
- [Nested OU](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-nested-ou.html): Learn about nested OUs in the manifest file.

### [Build your own customizations](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-customizations.html)

Learn about building your own customizations by modifying the CfCT manifest file.

- [Set up a configuration package for SCPs or RCPs](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-set-up-custom-scps.html): Learn about how to create a configuration package for service control policies (SCPs) or resource control policies (RCPs)
- [Set up a configuration package for CloudFormation StackSets](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-cfn-stacksets.html): Learn about how to set up a configuration package for AWS CloudFormation StackSets.
- [The âalfredâ helper and the CloudFormation parameter files](https://docs.aws.amazon.com/controltower/latest/userguide/alfred-helper.html): Learn about the 'alfred' helper and the AWS CloudFormation parameter files.
- [Version upgrades for the CfCT manifest](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-compatibility.html): Learn about manifest versions and manifest upgrades.


## [Networking](https://docs.aws.amazon.com/controltower/latest/userguide/networking.html)

### [Overview of AWS Control Tower and VPCs](https://docs.aws.amazon.com/controltower/latest/userguide/vpc-concepts.html)

Learn about concepts to help you work effectively with AWS Control Tower and VPCs.

- [CIDR and Peering for VPC and AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/vpc-ct-cidr.html): Learn about CIDR range for your AWS Control Tower organization.
- [AWS PrivateLink](https://docs.aws.amazon.com/controltower/latest/userguide/networking-privatelink.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Control Tower.


## [Roles and permissions](https://docs.aws.amazon.com/controltower/latest/userguide/roles-overview.html)

### [Roles and accounts](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html)

Learn about how AWS Control Tower works with roles.

- [AWSControlTowerExecution role](https://docs.aws.amazon.com/controltower/latest/userguide/awscontroltowerexecution.html): The AWSControlTowerExecution role must be present in all enrolled accounts.
- [Optional conditions for your role trust relationships](https://docs.aws.amazon.com/controltower/latest/userguide/conditions-for-role-trust.html): To add additional layers of security to your AWS Control Tower environment, you can impose conditions in your role trust policies, to restrict the accounts and resources that interact with certain roles in AWS Control Tower.


## [Configure Regions](https://docs.aws.amazon.com/controltower/latest/userguide/region-how.html)

- [Avoid mixed governance when configuring Regions](https://docs.aws.amazon.com/controltower/latest/userguide/mixed-governance.html): Mixed governance in AWS Control Tower occurs when the controls governing an OU do not match those governing each account within the OU, typically after extending or removing governance from a Region.
- [About opt-in Regions](https://docs.aws.amazon.com/controltower/latest/userguide/opt-in-region-considerations.html): AWS Control Tower supports the activation and governance of opt-in Regions, which are AWS Regions that require manual selection for activation.
- [Configure the Region deny control](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html): AWS Control Tower offers two Region deny controls: GRREGIONDENY, which applies to the entire landing zone, and CTMULTISERVICEPV1, which can be applied to specific organizational units (OUs).


## [About accounts](https://docs.aws.amazon.com/controltower/latest/userguide/accounts.html)

- [About the shared accounts](https://docs.aws.amazon.com/controltower/latest/userguide/special-accounts.html): Three special AWS accounts are associated with AWS Control Tower; the management account, the audit account, and the log archive account.
- [Shared account resources](https://docs.aws.amazon.com/controltower/latest/userguide/shared-account-resources.html): This section shows the resources that AWS Control Tower creates in the shared accounts, when you set up your landing zone.
- [About member accounts](https://docs.aws.amazon.com/controltower/latest/userguide/member-accounts.html): Member accounts are the accounts through which your users perform their AWS workloads.

### [Interact with AWS Control Tower accounts from AWS Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/handle-accounts-with-service-catalog.html)

This section tells how to handle your AWS Control Tower accounts with the capabilities of AWS Service Catalog.

- [Create and provision an account](https://docs.aws.amazon.com/controltower/latest/userguide/provision-as-end-user.html): Learn how to create and provision accounts as a user in AWS IAM Identity Center through AWS Service Catalog.
- [Automate Account Provisioning in AWS Control Tower by Service Catalog APIs](https://docs.aws.amazon.com/controltower/latest/userguide/automated-provisioning-walkthrough.html): This walkthrough demonstrates how to automate account provisioning in AWS Control Tower using Service Catalog APIs and AWS CLI commands.
- [Update the provisioned product in Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/update-provisioned-product.html): The following procedure guides you through how to update your account in Account Factory or move it to a new OU, by updating the account's provisioned product in Service Catalog.
- [Unenroll an account in Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/unenroll-with-sc.html): Unenrolling an account can be done in the Service Catalog console by an IAM Identity Center user in the AWSAccountFactory group, by terminating the Provisioned Product.


## [Provision and manage accounts](https://docs.aws.amazon.com/controltower/latest/userguide/provision-and-manage-accounts.html)

- [Methods of provisioning](https://docs.aws.amazon.com/controltower/latest/userguide/methods-of-provisioning.html): AWS Control Tower offers multiple methods for creating and updating member accounts, including console-based options like Account Factory and automated approaches such as Lambda code and Terraform.
- [Provision accounts in console](https://docs.aws.amazon.com/controltower/latest/userguide/account-create-console.html): Learn how to create and provision accounts as a user in AWS IAM Identity Center through AWS Control Tower.
- [View your accounts](https://docs.aws.amazon.com/controltower/latest/userguide/view-your-accounts.html): The Organization page lists all OUs and accounts in your organization, regardless of OU or enrollment status in AWS Control Tower.

### [About enrolling accounts](https://docs.aws.amazon.com/controltower/latest/userguide/enroll-account.html)

Learn about enrolling an existing AWS account.

- [Prerequisites for enrollment](https://docs.aws.amazon.com/controltower/latest/userguide/enrollment-prerequisites.html): Learn about the required prerequisites to enroll an existing AWS account in AWS Control Tower.
- [Auto-enrollment option](https://docs.aws.amazon.com/controltower/latest/userguide/account-auto-enrollment.html): The account auto-enrollment feature is available for landing zones of version 3.1 and above.
- [Enroll from console](https://docs.aws.amazon.com/controltower/latest/userguide/quick-account-provisioning.html): Learn about enrolling an existing account that is not governed by AWS Control Tower.
- [If the account does not meet the prerequisites](https://docs.aws.amazon.com/controltower/latest/userguide/fulfill-prerequisites.html): Remember that, as a prerequisite, accounts eligible to be enrolled into AWS Control Tower governance must be part of the same overall organization.
- [Manually add the required IAM role to an existing AWS account and enroll it](https://docs.aws.amazon.com/controltower/latest/userguide/enroll-manually.html): Learn how to enroll organization accounts into an OU that's registered with AWS Control Tower after you've already set up your AWS Control Tower landing zone.
- [Enroll accounts that have existing AWS Config resources](https://docs.aws.amazon.com/controltower/latest/userguide/existing-config-resources.html): Learn about enrolling accounts with existing AWS Config resources into AWS Control Tower.

### [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)

Learn about how to provision new member accounts in an AWS Control Tower landing zone.

- [Update and move accounts](https://docs.aws.amazon.com/controltower/latest/userguide/updating-account-factory-accounts.html): Learn how to update and migrate accounts for Account Factory.
- [Change email address of an enrolled account](https://docs.aws.amazon.com/controltower/latest/userguide/change-account-email.html): Learn how to change the email address of an enrolled account in AWS Control Tower.
- [Change the name of an enrolled account](https://docs.aws.amazon.com/controltower/latest/userguide/change-account-name.html): Learn how to change the name of an enrolled account in AWS Control Tower.
- [Configure Amazon VPC settings](https://docs.aws.amazon.com/controltower/latest/userguide/configuring-account-factory-with-VPC-settings.html): Learn how to configure Account Factory accounts with Amazon VPC settings.
- [Unenroll an account](https://docs.aws.amazon.com/controltower/latest/userguide/unmanage-account.html): Learn how to unenroll an enrolled account in Account Factory.
- [Close an account](https://docs.aws.amazon.com/controltower/latest/userguide/delete-account.html): Learn about how to close AWS accounts.
- [Account Factory resources](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory-considerations.html): Learn about resources that are created when accounts are provisioned with Account Factory.

### [Account Factory Customization (AFC)](https://docs.aws.amazon.com/controltower/latest/userguide/af-customization-page.html)

Learn about how AWS Control Tower allows you to customize new and existing accounts from the console.

### [Set up for customization](https://docs.aws.amazon.com/controltower/latest/userguide/afc-setup-steps.html)

Learn about the steps to set up Account Factory for the customization process.

- [Step 1. Create the required role](https://docs.aws.amazon.com/controltower/latest/userguide/step-1-create-blueprint-access-role.html): Before you begin to customize accounts, you must set up a role that contains a trust relationship between AWS Control Tower and your hub account.
- [Step 2. Create the AWS Service Catalog product](https://docs.aws.amazon.com/controltower/latest/userguide/step-2-create-blueprint-product.html): To create an AWS Service Catalog product, follow the steps at Creating products in the AWS Service Catalog Administrator Guide.
- [Step 3. Review your custom blueprint](https://docs.aws.amazon.com/controltower/latest/userguide/step-3-review-blueprint.html): You can view your blueprint in the AWS Service Catalog console.
- [Step 4. Call your blueprint to create a customized account](https://docs.aws.amazon.com/controltower/latest/userguide/step-4-call-the-blueprint.html): When you follow the Create account workflow in the AWS Control Tower console, you'll see an optional section where you can enter information about the blueprint you'd like to use for customizing accounts.
- [Create a customized account from a blueprint](https://docs.aws.amazon.com/controltower/latest/userguide/create-afc-customized-account.html): Learn about how to create custom accounts after you've created custom blueprints.
- [Customize accounts with AFC as you enroll them](https://docs.aws.amazon.com/controltower/latest/userguide/enroll-and-customize.html): Learn about the steps to enroll and customize accounts from the AWS Control Tower console.
- [Add a blueprint to an AWS Control Tower account](https://docs.aws.amazon.com/controltower/latest/userguide/add-blueprint-to-account.html): Learn about adding a blueprint to an existing AWS Control Tower member account.
- [Update a blueprint](https://docs.aws.amazon.com/controltower/latest/userguide/update-a-blueprint.html): Learn how to update and deploy custom blueprints.
- [Remove a blueprint from an account](https://docs.aws.amazon.com/controltower/latest/userguide/remove-a-blueprint.html): Learn how to remove a blueprint from an account.
- [Partner blueprints](https://docs.aws.amazon.com/controltower/latest/userguide/partner-blueprints.html): Learn about pre-defined blueprints that you can access to customize accounts.

### [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/taf-account-provisioning.html)

Learn about AWS Control Tower Account Factory for Terraform (AFT).

### [AFT overview](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html)

Learn how Account Factory for Terraform (AFT) integrates with AWS Control Tower to provide a Terraform-based pipeline for account provisioning and customization.

- [AFT Architecture](https://docs.aws.amazon.com/controltower/latest/userguide/aft-architecture.html): Learn about the architecture and order of operations for AWS Control Tower's Account Factory for Terraform (AFT).
- [Cost](https://docs.aws.amazon.com/controltower/latest/userguide/aft-pricing.html): Learn how Account Factory for Terraform (AFT) itself incurs no additional charges, but users pay for the resources and services deployed and enabled by AFT.

### [Deploy AFT](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html)

Learn about how to set up an Account Factory for Terraform (AFT) environment with a new AFT management account.

- [Post-deployment steps](https://docs.aws.amazon.com/controltower/latest/userguide/aft-post-deployment.html): Learn about the post-deployment steps that are required to complete the setup process.
- [Provision a new account](https://docs.aws.amazon.com/controltower/latest/userguide/aft-provision-account.html): Learn how Account Factory for Terraform (AFT) enables new account provisioning through the creation of an account request Terraform file containing specific parameters.
- [Multiple account requests](https://docs.aws.amazon.com/controltower/latest/userguide/aft-multiple-account-requests.html): Learn how Account Factory for Terraform (AFT) allows users to submit multiple account requests, which are processed in a first-in, first-out order.
- [Update an existing account](https://docs.aws.amazon.com/controltower/latest/userguide/aft-update-account.html): Learn about how to update an existing AFT account.

### [Versions supported](https://docs.aws.amazon.com/controltower/latest/userguide/version-supported.html)

Account Factory for Terraform (AFT) in AWS Control Tower supports Terraform version 1.6.0 or later and offers compatibility with three Terraform distributions: Community Edition, Cloud, and Enterprise.

- [Check the AFT version](https://docs.aws.amazon.com/controltower/latest/userguide/check-aft-version.html): Learn how to check the deployed version of AWS Control Tower Account Factory for Terraform (AFT).
- [Update the AFT version](https://docs.aws.amazon.com/controltower/latest/userguide/update-aft-version.html): Updating the deployed AFT (Account Factory for Terraform) version in AWS Control Tower can be done by pulling the latest changes from the main repository branch using the command 'terraform get -update'.
- [Enable feature options](https://docs.aws.amazon.com/controltower/latest/userguide/aft-feature-options.html): Learn about Account Factory for Terraform (AFT) optional features for AWS Control Tower environments, including CloudTrail data event logging, automatic Enterprise Support enrollment, and default VPC deletion.
- [Resources for AFT](https://docs.aws.amazon.com/controltower/latest/userguide/aft-resources.html): Learn what Account Factory for Terraform (AFT) creates various AWS resources across multiple accounts when setting up a landing zone.
- [Required roles](https://docs.aws.amazon.com/controltower/latest/userguide/aft-required-roles.html): Learn why Account Factory for Terraform (AFT) creates multiple IAM roles and policies in the AFT management and AWS Control Tower management accounts to support its pipeline operations.
- [Component services](https://docs.aws.amazon.com/controltower/latest/userguide/aft-components.html): Learn about the various AWS services and components that are integrated when deploying AWS Control Tower Account Factory for Terraform (AFT).
- [AFT account provisioning pipeline](https://docs.aws.amazon.com/controltower/latest/userguide/aft-provisioning-framework.html): The Account Factory for Terraform (AFT) account provisioning pipeline automates a series of steps to prepare newly provisioned accounts for customization, including metadata storage, role creation, and tag application.
- [Account customizations](https://docs.aws.amazon.com/controltower/latest/userguide/aft-account-customization-options.html): Learn how to apply global and account customizations.

### [Alternative VCS](https://docs.aws.amazon.com/controltower/latest/userguide/aft-alternative-vcs.html)

Learn about the process of setting up alternative version control systems for source code in AWS Control Tower's Account Factory for Terraform (AFT), including support for GitHub, BitBucket, and GitLab.

- [Move to another VCS](https://docs.aws.amazon.com/controltower/latest/userguide/move-a-vcs.html): This section contains procedures to help you move AFT from AWS CodeCommit to another VCS provider.
- [Data protection](https://docs.aws.amazon.com/controltower/latest/userguide/aft-data-protection.html): This document outlines data protection practices for AWS Control Tower Account Factory for Terraform (AFT), emphasizing the AWS shared responsibility model and best practices for security.
- [Remove an account](https://docs.aws.amazon.com/controltower/latest/userguide/aft-remove-account.html): Learn how to remove an account from AFT.
- [Operational metrics](https://docs.aws.amazon.com/controltower/latest/userguide/aft-operational-metrics.html): Learn how Account Factory for Terraform (AFT) collects anonymous operational metrics by default to improve the solution's quality and features.
- [Troubleshooting guide](https://docs.aws.amazon.com/controltower/latest/userguide/account-troubleshooting-guide.html): This section provides methods to troubleshoot common issues when using Account Factory for Terraform (AFT).


## [Drift](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html)

- [Viewing drift](https://docs.aws.amazon.com/controltower/latest/userguide/viewing-drift.html): You can view the drift status for your accounts and OUs through the console or APIs, and identify when account and OU configurations are drifted, or out of sync.
- [Resolving drift](https://docs.aws.amazon.com/controltower/latest/userguide/resolving-drift.html): Although detection is automatic, the steps to resolve drift must be done manually through the console, or with the APIs. (Except in certain cases when auto-enroll is enabled for accounts that are moved.)
- [Types of governance drift](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html): Learn about various types of governance drift that can occur in AWS Control Tower, including moved or removed member accounts, unplanned updates to managed SCPs, and changes to organizational units.
- [If you manage resources outside of AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/external-resources.html): Learn how to manage resources outside of AWS Control Tower, including renaming, deleting, and moving resources, which can cause the console to become out of sync.


## [Organizations](https://docs.aws.amazon.com/controltower/latest/userguide/existing-orgs.html)

- [Extend governance to an existing organization](https://docs.aws.amazon.com/controltower/latest/userguide/about-extending-governance.html): Learn how to extend AWS Control Tower governance to an existing AWS Organizations structure.
- [Nested OUs](https://docs.aws.amazon.com/controltower/latest/userguide/nested-ous.html): AWS Control Tower supports nested Organizational Units (OUs), allowing for a more complex hierarchical structure in managing AWS accounts and resources.

### [Register an OU to enroll multiple accounts](https://docs.aws.amazon.com/controltower/latest/userguide/importing-existing.html)

Learn how to register an existing organizational unit (OU) with AWS Control Tower, extending governance to multiple AWS accounts efficiently.

- [Register an existing OU](https://docs.aws.amazon.com/controltower/latest/userguide/how-to-register-existing-ou.html): In the AWS Control Tower console, on the Organization page, you can view all of of your organization's OUs and accounts in a hierarchy, including OUs that are registered with AWS Control Tower, and those that are not registered.
- [Create a new OU](https://docs.aws.amazon.com/controltower/latest/userguide/create-new-ou.html): Learn how to create an OU in AWS Control Tower.
- [Remove an OU](https://docs.aws.amazon.com/controltower/latest/userguide/remove-ou.html): Learn how to remove an OU from AWS Control Tower.
- [Common causes of failure during registration or re-registration](https://docs.aws.amazon.com/controltower/latest/userguide/common-eg-failures.html): Learn about the common causes of failure during the registration or re-registration of organizational units (OUs) and accounts in AWS Control Tower.

### [Update organizations](https://docs.aws.amazon.com/controltower/latest/userguide/ou-updates.html)

Re-registering an organizational unit (OU) is the quickest way to update an OU or multiple accounts within it in AWS Control Tower.

- [When to update OUs and accounts](https://docs.aws.amazon.com/controltower/latest/userguide/update-existing-accounts.html): After performing a landing zone update in AWS Control Tower, it's necessary to update enrolled accounts to apply new controls.
- [Update multiple accounts in one OU](https://docs.aws.amazon.com/controltower/latest/userguide/update-multiple-accounts.html): AWS Control Tower allows updating multiple accounts within the same organizational unit (OU) through a single action of re-registering the OU.
- [Update a single account](https://docs.aws.amazon.com/controltower/latest/userguide/update-account-in-sc.html): Individual AWS Control Tower accounts can be updated through either the AWS Control Tower console or the AWS Service Catalog console.


## [Integrated services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html)

- [AWS Backup](https://docs.aws.amazon.com/controltower/latest/userguide/with-backup.html): AWS Backup allows you to create a backup plan for your AWS Control Tower landing zone.
- [CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/cloudformation.html): Use CloudFormation in conjunction with AWS Control Tower, and use stacksets to apply controls on accounts, enabling efficient management of cloud resources across an organization.
- [CloudTrail](https://docs.aws.amazon.com/controltower/latest/userguide/cloudtrail.html): Learn how AWS Control Tower utilizes AWS CloudTrail to provide centralized logging and auditing capabilities for AWS environments.
- [CloudWatch](https://docs.aws.amazon.com/controltower/latest/userguide/cloudwatch.html): Learn how Amazon CloudWatch offers a robust, scalable, and flexible monitoring solution for AWS resources and services that can be quickly implemented.
- [AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/config.html): Learn how AWS Config provides a comprehensive view of AWS account resources, their configurations, and relationships over time, with resources provisioned by AWS Control Tower automatically tagged for easy identification.
- [AWS Identity and Access Management](https://docs.aws.amazon.com/controltower/latest/userguide/iam.html): AWS Identity and Access Management is a service for centrally managing access to AWS resources, allowing you to control users, security credentials, and permissions.
- [AWS Key Management Service](https://docs.aws.amazon.com/controltower/latest/userguide/kms-integration.html): AWS Key Management Service (AWS KMS) is a service that allows users to create and manage encryption keys for data protection.
- [AWS Lambda](https://docs.aws.amazon.com/controltower/latest/userguide/lambda.html): AWS Lambda enables serverless compute functions, allowing users to run code without managing servers for various applications and backend services.
- [AWS Organizations](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html): AWS Organizations is an account management service that allows for the consolidation and central management of multiple AWS accounts within an organization.
- [Amazon S3](https://docs.aws.amazon.com/controltower/latest/userguide/s3.html): Amazon Simple Storage Service (Amazon S3) provides internet-based storage, allowing users to store and retrieve any amount of data from anywhere on the web.
- [Security Hub CSPM](https://docs.aws.amazon.com/controltower/latest/userguide/security-hub.html): AWS Control Tower is integrated with AWS Security Hub CSPM through the Service-Managed Standard: AWS Control Tower.
- [AWS Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/service-catalog.html): AWS Service Catalog enables IT administrators to create, manage, and distribute portfolios of approved products to end users, providing access to needed products in a personalized portal.
- [Amazon SNS](https://docs.aws.amazon.com/controltower/latest/userguide/sns.html): Learn how AWS Control Tower utilizes Amazon Simple Notification Service (Amazon SNS) to send programmatic alerts to management and audit account email addresses, helping prevent drift within the landing zone.
- [Step Functions](https://docs.aws.amazon.com/controltower/latest/userguide/step-functions.html): AWS Step Functions simplifies the process of coordinating components in distributed applications by allowing developers to create visual workflows consisting of a series of steps.


## [Identity and access management](https://docs.aws.amazon.com/controltower/latest/userguide/auth-access.html)

### [IAM Identity Center and AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html)

Manage users and access through AWS IAM Identity Center.

- [User groups, roles, and permission sets](https://docs.aws.amazon.com/controltower/latest/userguide/user-groups-roles-permissions.html): AWS Control Tower uses user groups to manage specialized roles within shared accounts, with all group members inheriting the associated permission sets or roles.
- [IAM Identity Center Groups for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/sso-groups.html): AWS Control Tower offers preconfigured groups to organize users performing specific tasks in various accounts, allowing administrators to add users and assign them to these groups directly in IAM Identity Center.

### [Overview of managing resource access with IAM](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-overview.html)

Learn how to manage access permissions to AWS Control Tower resources, covering topics such as resource ownership, policy elements, and specifying conditions in policies.

### [Manage access to resources](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-manage-access-intro.html)

Learn how to manage access to resources in AWS Control Tower using identity-based policies (IAM policies) attached to IAM identities such as users, groups, or roles.

- [Create roles and assign permissions](https://docs.aws.amazon.com/controltower/latest/userguide/assign-permissions.html): Find detailed instructions on creating roles and assigning permissions in AWS Control Tower and other AWS services, including steps for using the IAM console, JSON policy editor, and visual editor to create policies.
- [Prevent confused deputy attacks](https://docs.aws.amazon.com/controltower/latest/userguide/prevent-confused-deputy.html): Cross-service impersonation in AWS can lead to the confused deputy problem, where one service manipulates another to act on a customer's resources beyond its intended permissions.

### [IAM policies for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html)

Find detailed information on identity-based policies (IAM policies) used in AWS Control Tower, including the AWSControlTowerAdmin role, AWSControlTowerServiceRolePolicy, and other essential roles and policies.

- [Permissions Required to use the AWS Control Tower console](https://docs.aws.amazon.com/controltower/latest/userguide/additional-console-required-permissions.html): Learn about the three essential roles when setting up a landing zone, which are required for console access: AWSControlTowerAdmin, AWSControlTowerStackSetRole, and AWSControlTowerCloudTrailRole.
- [Managed policies for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html): AWS Control Tower uses managed IAM policies to grant necessary permissions for common use cases, reducing the need for manual investigation of required permissions.


## [Security](https://docs.aws.amazon.com/controltower/latest/userguide/security.html)

- [Data Protection](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-console-encryption.html): Learn how the AWS shared responsibility model applies to data protection in AWS Control Tower.
- [Compliance Validation](https://docs.aws.amazon.com/controltower/latest/userguide/compliance-validation.html): This chapter contains info about our AWS compliance program that you should consider when using AWS Control Tower.
- [Resilience](https://docs.aws.amazon.com/controltower/latest/userguide/disaster-recovery-resiliency.html): This chapter contains info about disaster recovery resiliency that you should consider when using AWS Control Tower.
- [Infrastructure Security](https://docs.aws.amazon.com/controltower/latest/userguide/infrastructure-security.html): Learn how AWS Control Tower isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/controltower/latest/userguide/logging-and-monitoring.html)

- [About logging in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/about-logging.html): AWS Control Tower automatically logs actions and events through integration with AWS CloudTrail, AWS Config, and CloudWatch, covering both management and member account activities.
- [S3 bucket policy](https://docs.aws.amazon.com/controltower/latest/userguide/logging-s3-audit-bucket.html): Learn how AWS Control Tower implements a specific Amazon S3 bucket policy in the audit account to ensure that only AWS services within the organization or organizational unit can access resources.
- [Monitoring overview](https://docs.aws.amazon.com/controltower/latest/userguide/monitoring-overview.html): Monitor AWS Control Tower actions to maintain reliability, availability, and performance.
- [Logging AWS Control Tower Actions with AWS CloudTrail](https://docs.aws.amazon.com/controltower/latest/userguide/logging-using-cloudtrail.html): Learn how AWS Control Tower integrates with AWS CloudTrail to provide a comprehensive record of actions taken by users, roles, or AWS services within the AWS Control Tower environment.

### [Monitor resource changes with AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/monitoring-with-config.html)

Learn how AWS Control Tower enables AWS Config to enforce detective controls and log resource changes.

- [Manage Config costs](https://docs.aws.amazon.com/controltower/latest/userguide/config-costs.html): Learn how AWS Config records and bills for resource changes in AWS Control Tower accounts, helping users understand and manage associated costs.
- [Lifecycle Events](https://docs.aws.amazon.com/controltower/latest/userguide/lifecycle-events.html): AWS Control Tower uses lifecycle events to mark the completion of actions that change the state of resources such as organizational units, accounts, and controls.
- [User notifications](https://docs.aws.amazon.com/controltower/latest/userguide/using-user-notifications.html): AWS User Notifications User Notifications can be used with AWS Control Tower to set up delivery channels for event notifications through multiple channels, including email, Amazon Q Developer in chat applications chat notifications, and AWS Console Mobile Application push notifications.


## [Backup](https://docs.aws.amazon.com/controltower/latest/userguide/backup.html)

- [Prerequisites](https://docs.aws.amazon.com/controltower/latest/userguide/backup-prerequisites.html): Before setting up AWS Backup for AWS Control Tower resources, users must have an existing AWS Organizations organization and allocate two additional AWS accounts for central backup and backup administration.
- [Enable backups](https://docs.aws.amazon.com/controltower/latest/userguide/enable-backup.html): AWS Control Tower allows enabling backups for enrolled account resources during landing zone setup or updates, requiring a Backup Administrator account, a Central Backup account, and a multi-Region AWS KMS key.
- [Turn off backups](https://docs.aws.amazon.com/controltower/latest/userguide/stop-backups.html): Turning off backups in AWS Control Tower involves a two-step process: first disabling the AWS Backup baseline on each OU with enabled backups, then turning off AWS Backup for the entire landing zone.
- [Moved accounts](https://docs.aws.amazon.com/controltower/latest/userguide/moving-accounts-and-backup.html): When an account is moved into an AWS Control Tower OU with AWS Backup enabled, the backup plan doesn't automatically apply if the account isn't enrolled in AWS Control Tower.
- [Backup drift](https://docs.aws.amazon.com/controltower/latest/userguide/backup-drift.html): AWS Control Tower does not report drift for AWS Backup configurations, but certain modifications to the backup plan can lead to a state of drift.
- [Backup resources](https://docs.aws.amazon.com/controltower/latest/userguide/backup-resources.html): When AWS Backup is enabled in AWS Control Tower, various resources are created across different accounts including the Central Backup account, Backup Administrator account, Audit account, Log Archive account, and member accounts in other OUs.
- [Controls for AWS Backup](https://docs.aws.amazon.com/controltower/latest/userguide/backup-controls.html): Enabling AWS Backup in an AWS Control Tower landing zone activates preventive controls to protect resources essential for AWS Backup's operation with AWS Backup.


## [Decommission a landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/decommission-landing-zone.html)

- [Overview of the decommissioning process](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html): This overview outlines the comprehensive decommissioning process for an AWS Control Tower landing zone.

### [How to decommission a landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/how-to-decommission.html)

Learn how to decommission an AWS Control Tower landing zone, including the confirmation process and post-decommissioning cleanup tasks.

- [Decommission your landing zone with APIs](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-decommission.html): The process of cleaning up all of a landing zones resources is referred to as decommissioning a landing zone.
- [Manual cleanup tasks required after decommissioning](https://docs.aws.amazon.com/controltower/latest/userguide/manual-cleanup-required.html): This section lists manual cleanup tasks you must perform after the initial decommissioning step.
- [Resources not removed during decommissioning](https://docs.aws.amazon.com/controltower/latest/userguide/resources-not-removed.html): Decommissioning an AWS Control Tower landing zone does not fully reverse the setup process, leaving certain resources intact.

### [Remove AWS Control Tower resources](https://docs.aws.amazon.com/controltower/latest/userguide/walkthrough-delete.html)

This chapter contains walkthrough procedures so you can maintain or clean up specific resources and workflows in your AWS Control Tower landing zone.

- [Delete SCPs](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-delete-scps.html): Learn how to delete Service Control Policies (SCPs) specifically related to AWS Control Tower within AWS Organizations.
- [Delete StackSets and Stacks](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-delete-stacksets.html): Review step-by-step instructions for deleting CloudFormation StackSets and stacks associated with AWS Control Tower.
- [Delete Amazon S3 Buckets in the Log Archive Account](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-delete-s3-buckets.html): Learn about deleting S3 buckets in the log archive account of AWS Control Tower.
- [Remove an Account Factory Portfolio and Product](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-cleanup-account-factory.html): Learn about removing an Account Factory Portfolio and Product in AWS Control Tower.
- [Remove AWS Control Tower Roles and Policies](https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-cleanup-identity.html): Learn how to remove AWS Control Tower roles and policies that were created during the landing zone setup or subsequently.
- [Setup after decommissioning a landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/known-issues-decommissioning.html): After decommissioning an AWS Control Tower landing zone, manual cleanup of remaining resources is necessary before setting up a new landing zone.


## [Walkthroughs](https://docs.aws.amazon.com/controltower/latest/userguide/walkthroughs.html)

- [Walkthrough: Move from ALZ to AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/alz-to-control-tower.html): Transition from ALZ to AWS Control Tower.
- [Walkthrough: Configure AWS Control Tower Without a VPC](https://docs.aws.amazon.com/controltower/latest/userguide/configure-without-vpc.html): Find out how to configure your AWS Control Tower accounts without a VPC.
- [Walkthrough: Set Up Security Groups in AWS Control Tower With AWS Firewall Manager](https://docs.aws.amazon.com/controltower/latest/userguide/firewall-setup-walkthrough.html): Learn how to enhance network security in AWS Control Tower using AWS Firewall Manager to set up and manage security groups.


## [Baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)

- [Partial enrollment](https://docs.aws.amazon.com/controltower/latest/userguide/partial-enrollment.html): When you're working with baselines, an account can be placed into a state called Partially enrolled.
- [Compare console and API](https://docs.aws.amazon.com/controltower/latest/userguide/console-vs-api-baseline.html): When you change the governance status of an OU, the AWS Control Tower console performs more operations for you automatically, compared to changing governance by means of the APIs for baselines.
- [AWSControlTowerBaseline table](https://docs.aws.amazon.com/controltower/latest/userguide/table-of-baselines.html): AWS Control Tower baselines allow setting governance standards at the OU level, with the AWSControlTowerBaseline available for registering OUs.
- [Examples: Register an AWS Control Tower OU with APIs only](https://docs.aws.amazon.com/controltower/latest/userguide/walkthrough-baseline-steps.html): Learn about registering and re-registering AWS Control Tower organizational units (OUs) using APIs only.
- [Baseline API examples](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html): See examples of how to call the AWS Control Tower baseline APIs.


## [Release notes](https://docs.aws.amazon.com/controltower/latest/userguide/release-notes.html)

- [January 2026 - Present](https://docs.aws.amazon.com/controltower/latest/userguide/2026-all.html): See the updates released by AWS Control Tower in 2026.
- [January 2025 - December 2025](https://docs.aws.amazon.com/controltower/latest/userguide/2025-all.html): See the updates released by AWS Control Tower in 2025.
- [January - December 2024](https://docs.aws.amazon.com/controltower/latest/userguide/2024-all.html): See the updates released by AWS Control Tower in 2024.
- [January - December 2023](https://docs.aws.amazon.com/controltower/latest/userguide/2023-all.html): See the updates released by AWS Control Tower in 2023.
- [January - December 2022](https://docs.aws.amazon.com/controltower/latest/userguide/2022-all.html): See the updates released by AWS Control Tower in 2022.
- [January - December 2021](https://docs.aws.amazon.com/controltower/latest/userguide/2021-all.html): See the updates released by AWS Control Tower in 2021.
- [January - December 2020](https://docs.aws.amazon.com/controltower/latest/userguide/2020-all.html): See the updates released by AWS Control Tower in 2020.
- [June - December 2019](https://docs.aws.amazon.com/controltower/latest/userguide/2019-all.html): See the updates released by AWS Control Tower in 2019.
