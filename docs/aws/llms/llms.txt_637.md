# Source: https://docs.aws.amazon.com/organizations/latest/userguide/llms.txt

# AWS Organizations User Guide

> Combine all of your AWS accounts into an organization to consolidate billing and to achieve new levels of control over your AWS accounts.

- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html)
- [Multi-party approval](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_mpa.html)
- [Troubleshooting](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_troubleshoot.html)
- [Making HTTP Query requests](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_query-requests.html)
- [Document history](https://docs.aws.amazon.com/organizations/latest/userguide/document-history.html)

## [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)

- [Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html): Learn the basic terms and concepts of AWS Organizations.
- [Quotas and service limits](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html): Use AWS Organizations to create, organize, and manage your AWS accounts.
- [Region support](https://docs.aws.amazon.com/organizations/latest/userguide/region-support.html): AWS Organizations is available in all AWS commercial Regions, AWS GovCloud (US) Regions, and China Regions.
- [Billing and pricing](https://docs.aws.amazon.com/organizations/latest/userguide/pricing.html): AWS Organizations is offered at no additional charge.
- [Support and feedback](https://docs.aws.amazon.com/organizations/latest/userguide/support-and-feedback.html): We welcome your feedback.


## [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html)

- [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html): Learn how AWS Organizations helps you to manage multiple AWS accounts.
- [Tutorial: Monitor an organization with Amazon EventBridge](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_cwe.html): Configure Amazon EventBridge to send alerts by email or SMS text message when users make changes to your organization.
- [Working with AWS SDKs](https://docs.aws.amazon.com/organizations/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Managing an entire organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html)

- [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html): Learn how to create an organization to consolidate and manage your AWS accounts.
- [Verifying your email address](https://docs.aws.amazon.com/organizations/latest/userguide/about-email-verification.html): After you create an organization and before you can invite accounts to join, you must verify that you own the email address provided for the management account in the organization.
- [Resending the verification email](https://docs.aws.amazon.com/organizations/latest/userguide/about-email-verification-resend.html): If you don't verify your email address within 24 hours, you can resend the verification request.
- [Changing your email address](https://docs.aws.amazon.com/organizations/latest/userguide/about-email-verification-change-email.html): To change the email address that is associated with your management account, see Update the AWS account name, email address, or password for the root user in the AWS Account Management Reference Guide.

### [Enabling all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html)

Enable all features in your organization so that you can use policy-based controls that provide significant management capabilities over the accounts in your organization.

- [Standard migration process](https://docs.aws.amazon.com/organizations/latest/userguide/manage-begin-all-features-standard-migration.html): This topic describes how to enable all features with the standard migration process.
- [Assisted migration process](https://docs.aws.amazon.com/organizations/latest/userguide/manage-begin-all-features-assisted-migration.html): If you are an Enterprise customer, it can be difficult to complete the standard migration process due to the large number of accounts you might manage.
- [Viewing details of an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_org.html): When you sign in to the organization's management account in the AWS Organizations console, you can view details of the organization.
- [Deleting an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html): Learn how to delete an organization that you no longer need.


## [Managing accounts in an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html)

### [Management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_management.html)

A management account is the AWS account you use to create your organization.

- [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html): Describes best practices related to the management account in AWS Organizations.
- [Closing a management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close_management.html): Close, delete, or suspend an AWS account that you no longer need.

### [Member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_members.html)

A member account is an AWS account, other than the management account, that is part of an organization.

- [Best practices for member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_member-acct.html): Describes best practices related to the member accounts in AWS Organizations.
- [Creating a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html): Manage the accounts that are part of your organization.

### [Accessing member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html)

Access the accounts that are part of your organization in AWS Organizations.

- [Creating an IAM access role](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create-cross-account-role.html): By default, if you create a member account as part of your organization, AWS automatically creates a role in the account that grants administrator permissions to IAM users in the management account who can assume the role.
- [Using the IAM access role](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access-cross-account-role.html): When you create a member account using the AWS Organizations console, AWS Organizations automatically creates an IAM role named OrganizationAccountAccessRole in the account.
- [Closing a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html): Close, delete, or suspend an AWS account that you no longer need.
- [Protecting member accounts from closure](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_close_policy.html): To protect member accounts from accidental closure, create an IAM policy that specifies which accounts are exempt.
- [Removing a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html): Manage the member accounts that are part of your organization.
- [Leaving an organization from a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_leave-as-member.html): When you sign in to a member account, you can leave an organization.
- [Updating the account name for a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_name.html): When you sign in to your organization's management account, you can update the account name for a member account.
- [Updating the root user email for a member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_primary_email.html): Learn how to centrally update the root user email address for a member account using either the AWS Organizations console, AWS CLI commands, or their AWS SDK equivalent operations.

### [Account invitations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html)

Invite existing AWS accounts to join your organization and manage the invitations that you send or receive.

- [Sending invitations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invite-account.html): To invite accounts to your organization, you must first verify that you own the email address associated with the management account.
- [Managing pending invitations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_manage-invites.html): When you sign in to your management account, you can view all the linked AWS accounts in your organization and cancel any pending (open) invitations.
- [Accepting or declining invitations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_accept-decline-invite.html): If you receive an invitation to join an organization, you can accept or decline the invitation.
- [Migrate an account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_migration.html): Learn how to migrate an AWS account that you want to become part of another organization.
- [View details of an account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_account.html): When you sign in to the organization's management account in the AWS Organizations console, you can view details about your member accounts.
- [Export account details](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_export.html): Export a list of all accounts that are part of your organization to a .csv file.
- [Monitor account states](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html): Learn about the different states of your AWS accounts and what each state means for account access and management.
- [Update alternate contacts for an account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts.html): Update alternate contacts for billing, security and operations in your organization.
- [Update primary contact for an account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts_primary.html): Update the primary contact for an AWS account in your organization.
- [Update AWS Regions for an account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_enabled_regions.html): Update enabled AWS Regions for an AWS account in your organization.


## [Organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html)

- [Best practices for OUs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous_best_practices.html): Best practices for managing organizational units (OUs) with AWS Organizations.
- [Navigating the root and tree](https://docs.aws.amazon.com/organizations/latest/userguide/navigate_tree.html): To navigate to different OUs or to the root when moving accounts or attaching policies, you can use the default "tree" view.
- [Viewing details of an OU](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_ou.html): When you sign in to the organization's management account in the AWS Organizations console, you can view details of the OUs in your organization.
- [Creating an OU](https://docs.aws.amazon.com/organizations/latest/userguide/create_ou.html): When you sign in to your organization's management account, you can create an OU in your organization's root.
- [Renaming an OU](https://docs.aws.amazon.com/organizations/latest/userguide/rename_ou.html): When you sign in to your organization's management account, you can rename an OU.
- [Tagging an OU](https://docs.aws.amazon.com/organizations/latest/userguide/tag_ou.html): When you sign in to your organization's management account, you can add or remove the tags attached to an OU.
- [Moving accounts between OUs](https://docs.aws.amazon.com/organizations/latest/userguide/move_account_to_ou.html): When you sign in to your organization's management account, you can move accounts in your organization from the root to an OU, from one OU to another, or back to the root from an OU.
- [Viewing details of the root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_root.html): When you sign in to the organization's management account in the AWS Organizations console, you can view details of the administrative root.
- [Deleting an OU](https://docs.aws.amazon.com/organizations/latest/userguide/delete-ou.html): When you sign in to your organization's management account, you can delete any OUs that you no longer need.


## [Organization policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html)

### [Authorization policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_authorization_policies.html)

Learn about authorization policies in AWS Organizations.

### [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

Service control policies (SCPs) offer central control over the maximum available permissions for IAM users and IAM roles in an organization.

- [SCP evaluation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html): Learn how service control policies (SCPs) are evaluated in AWS Organizations.
- [SCP syntax](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html): Describes the syntax of AWS Organizations service control policies (SCPs) that can restrict what users and roles can do in accounts that are part of an organization.
- [SCP examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html): Learn more about service control policies (SCPs) by examining examples of commonly used policies.
- [Troubleshooting](https://docs.aws.amazon.com/organizations/latest/userguide/org_troubleshoot_policies.html): Diagnose and fix issues that you might encounter when working with AWS Organizations policies.

### [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)

Resource control policies (RCPs) offer central control over the maximum available permissions for resources in an organization.

- [RCP evaluation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_evaluation.html): Learn how resource control policies (RCPs) are evaluated in AWS Organizations.
- [RCP syntax](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_syntax.html): Describes the syntax of AWS Organizations resource control policies (RCPs) that can restrict what users and roles can do in accounts that are part of an organization.
- [RCP examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_examples.html): Learn more about resource control policies (RCPs) by examining examples of commonly used policies.

### [Management policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_management_policies.html)

Learn about policy inheritance in AWS Organizations.

- [Prerequisites and permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_prereqs.html): Learn about prerequisites and required permissions for management policies in an organization.

### [Understanding policy inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html)

Learn how the management policy types support inheritance in an AWS Organizations hierarchy.

- [Terminology](https://docs.aws.amazon.com/organizations/latest/userguide/inheritance-terminology.html): This topic uses the following terms when discussing management policy inheritance.
- [Management policy types](https://docs.aws.amazon.com/organizations/latest/userguide/syntax-inheritance.html): Exactly how policies affect the OUs and accounts that inherit them depends on the type of management policy you choose.
- [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html): Inheritance operators control how inherited policies and account policies merge into the account's effective policy.
- [Inheritance examples](https://docs.aws.amazon.com/organizations/latest/userguide/inheritance-examples.html): These examples show how policy inheritance works by showing how parent and child tag policies are merged into an effective tag policy for an account.
- [Viewing effective policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_effective.html): Learn how to view the effective management policy for AWS Organizations entities.
- [Invalid policy alerts](https://docs.aws.amazon.com/organizations/latest/userguide/invalid-policy-alerts.html): Invalid policy alerts let you know about invalid effective policies and provide mechanisms (APIs) to identify accounts with invalid policies.

### [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html)

Use declarative policies to centrally declare and enforce your desired configuration for a given AWS service at scale across an organization.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-declarative_getting-started.html): Learn how to enable and use declarative policies for the first time.
- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_best-practices.html): Learn about best practices for using declarative policies.
- [Generating the account status report](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html): Use declarative policies to centrally declare and enforce your desired configuration for a given AWS service at scale across an organization.
- [Declarative policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_syntax.html): Learn more about a declarative policy by learning its syntax and supported attributes.

### [Backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html)

Use backup policies to centrally manage and apply backup plans to the AWS resources across an organization's accounts.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-backup_getting-started.html): Learn how to enable and use backup policies for the first time.
- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_best-practices.html): Learn about best practices for using backup policies.
- [Using AWS CloudTrail events to monitor backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_cloudtrail.html): You can use AWS CloudTrail events to monitor when backup policies are created, updated, or deleted from any accounts in your organization, or when there is an invalid organizational backup plan.
- [Backup policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_syntax.html): Learn more about a backup policy by learning its syntax.

### [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

Use tag policies to standardize the tags attached to the AWS resources in an organization's accounts.

- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-best-practices.html): Learn about best practices for using tag policies.
- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html): Learn how to use tag policies for the first time.

### [Report tagging compliance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-report-tagging-compliance.html)

Learn about reporting tagging compliance with tag policies.

- [Generating an organization-wide compliance report](https://docs.aws.amazon.com/organizations/latest/userguide/enforcement-report.html): At any time, you can generate a report that lists all tagged resources in the AWS accounts across your organization.

### [Enforce tagging consistency](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-enforcement.html)

Learn about enforcing tagging consistency with tag policies.

- [Enforce "Required tag key" with IaC](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html): Tag policies help you maintain consistent tagging across your infrastructure as code (IaC) deployments.
- [Tag policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html): Learn more about tag policies by examining examples of commonly used policies.

### [Identify and remediate tagging inconsistencies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-identify-remediate.html)

Learn how to find and correct non-compliant tags in your organization's resources.

- [Finding untagged and mistagged resources](https://docs.aws.amazon.com/organizations/latest/userguide/finding-untagged-mistagged-resources.html): To find untagged resources in your account, use AWS Resource Explorer with a query that uses tag:none.
- [Correcting non-compliant tags in resources](https://docs.aws.amazon.com/organizations/latest/userguide/enforcement-correcting.html): After finding non-compliant tags, make corrections using any of the following methods.
- [Using Amazon EventBridge to monitor noncompliant tags](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-cwe.html): View an example Amazon EventBridge event for monitoring when noncompliant tags are introduced.
- [Services and resource types that support enforcement](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_supported-resources-enforcement.html): Learn about the services and resource types that support enforcing compliance with tag policies.
- [Supported Regions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-supported-regions.html): Learn which Regions support using tag policies.

### [Chat applications policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html)

Use chat applications policies to control access to an organization's accounts from chat applications such as Slack and Microsoft Teams.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-chatbot_getting-started.html): Learn how to enable and use chat applications policies for the first time.
- [Chat applications policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot_syntax.html): Learn more about chat applications policies by examining examples of policies.

### [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)

Use AI services opt-out policies to control data collection for AWS AI services for all the accounts in an organization.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-ai-opt-out_getting-started.html): Learn how to enable and use AI services opt-out policies for the first time.
- [Opt out from all AI services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_all.html): Learn how to opt out from all AI services.
- [AI services opt-out policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html): Learn more about AI services opt-out policies by examining examples of policies.

### [Security Hub policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html)

AWS Security Hub policies provide security teams with a centralized approach to managing security configurations across their AWS Organizations.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_getting_started.html): Before you configure Security Hub policies, ensure you understand the prerequisites and implementation requirements.
- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_best_practices.html): When implementing Security Hub policies across your organization, following established best practices helps ensure successful deployment and maintenance of your security configurations.
- [Security Hub policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_syntax.html): Security Hub policies follow a standardized JSON syntax that defines how Security Hub is enabled and configured across your organization.

### [Amazon Bedrock policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html)

Amazon Bedrock policies allow you to enforce safeguards configured in Amazon Bedrock Guardrails automatically across any element in your organization structure for all model inference calls to Amazon Bedrock.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock_getting_started.html): Before you configure Amazon Bedrock policies, ensure you understand the prerequisites and implementation requirements.
- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock_best_practices.html)
- [Amazon Bedrock policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock_syntax.html): An Amazon Bedrock policy is a plaintext file that is structured according to the rules of JSON.

### [Amazon Inspector policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html)

Amazon Inspector policies allow you to centrally enable and manage Amazon Inspector across accounts in your AWS organization.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector_getting_started.html): Before you configure Amazon Inspector policies, ensure you understand the prerequisites and implementation requirements.
- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector_best_practices.html): When implementing Amazon Inspector policies across your organization, following established best practices helps ensure successful deployment and maintenance.
- [Amazon Inspector policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector_syntax.html): Amazon Inspector policies follow a standardized JSON syntax that defines how Amazon Inspector is enabled and configured across your organization.

### [Upgrade rollout policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html)

Learn how to use upgrade rollout policies to manage and stagger automatic upgrades across your AWS organization.

- [Getting started with upgrade rollout policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_getting_started.html): Learn how to implement and test upgrade rollout policies in your organization.
- [Best practices for using upgrade rollout policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_best_practices.html): Learn recommended practices for implementing and managing upgrade rollout policies in your organization.
- [Upgrade rollout policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_syntax.html): Learn about upgrade rollout policy syntax and view example policy configurations.

### [Amazon S3 policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html)

Amazon S3 policies allow you to centrally manage configurations for Amazon S3 resources at scale across the accounts in an organization.

- [Best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3_best_practices.html): When implementing Amazon S3 policies across your organization, following established best practices helps ensure successful deployment and maintenance.
- [Amazon S3 policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3_syntax.html): An Amazon S3 policy is a plaintext file that is structured according to the rules of JSON.

### [AWS Shield Network Security Director policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html)

AWS Shield Network Security Director helps secure your AWS environment by discovering your compute, networking, and network security resources.

- [Getting started](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director_getting_started.html): Before you configure Network Security Director policies, ensure you understand the prerequisites and implementation requirements.
- [AWS Shield Network Security Director policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director_syntax.html): Network Security Director policies follow a standardized JSON syntax that defines how Network Security Director is enabled and configured across your organization.

### [Delegated administrator for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html)

Learn how to delegate AWS Organizations policy management to your AWS accounts.

- [Create a resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate.html): From the management account, create a resource-based delegation policy for your organization and add a statement that specifies which member accounts can perform actions on policies.
- [Update a resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate-update.html): From the management account, update a resource-based delegation policy for your organization and add a statement that specifies which member accounts can perform actions on policies.
- [View a resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/view-delegated-resource-based-policy.html): From the management account, view your organizationâs resource-based delegation policy to understand which delegated administrators have access to manage which policy types.
- [Delete a resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/delete-delegated-resource-based-policy.html): When you no longer need to delegate the management of policies in your organization, you can delete the resource-based delegation policy from the organization's management account.
- [Enabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/enable-policy-type.html): Before you can create and attach a policy to your organization, you must enable that policy type for use.
- [Disabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/disable-policy-type.html): If you no longer want to use a certain policy type in your organization, you can disable that type to prevent its accidental use.
- [Creating policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html): After you enable policies for your organization, you can create a policy.
- [Updating policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_update.html): When your policy requirements change, you can update an existing policy.
- [Editing tags attached to policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_edit.html): This topic describes how to edit tags attached policies with AWS Organizations.
- [Attaching policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html): This topic describes how to attach policies with AWS Organizations.
- [Detaching policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html): This topic describes how to detach policies with AWS Organizations.
- [Getting policy details](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html): Use AWS Organizations to retrieve details about the policies in your organization.
- [Deleting policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_delete.html): When you no longer need a policy and after you detach it from all organizational units (OUs) and accounts, you can delete it.


## [Tagging resources](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html)

- [Using tags](https://docs.aws.amazon.com/organizations/latest/userguide/use-tags.html): Tags help you to organize resources in your organization by enabling you to group them by whatever categories are useful to you.
- [Adding, updating, and removing tags](https://docs.aws.amazon.com/organizations/latest/userguide/add-tag.html): When you sign in to your organization's management account, you can add tags to the resources in your organization.


## [Using other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html)

### [Services that work with Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)

Learn about which services integrate with AWS Organizations to perform tasks in an organization's member accounts.

- [AWS Account Management](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html): AWS Account Management helps you manage the account information and metadata for all of the AWS accounts in your organization.
- [AWS Application Migration Service](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-application-migration.html): AWS Application Migration Service simplifies, expedites, and reduces the cost of migrating applications to AWS.
- [AWS Artifact](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-artifact.html): AWS Artifact is a service that allows you to download AWS security compliance reports such as ISO and PCI reports.
- [AWS Audit Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-audit-manager.html): AWS Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards.
- [AWS Backup](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html): AWS Backup is a service that allows you to manage and monitor the AWS Backup jobs in your organization.
- [AWS Billing and Cost Management](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-awsaccountbilling.html): AWS Billing and Cost Management provides a suite of features to help you set up your billing, retrieve and pay invoices, and analyze, organize, plan, and optimize your costs.
- [AWS CloudFormation StackSets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html): CloudFormation StackSets enables you to create, update, or delete stacks across multiple AWS accounts and AWS Regions with a single operation.
- [AWS CloudTrail](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudtrail.html): AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account.
- [Amazon CloudWatch](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html): You can use AWS Organizations for Amazon CloudWatch for the following use cases:
- [AWS Compute Optimizer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-compute-optimizer.html): AWS Compute Optimizer is a service that analyzes the configuration and utilization metrics of your AWS resources.
- [AWS Config](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html): Multi-account, multi-region data aggregation in AWS Config enables you to aggregate AWS Config data from multiple accounts and AWS Regions into a single account.
- [AWS Cost Optimization Hub](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-coh.html): AWS Cost Optimization Hub is an AWS Billing and Cost Management feature that helps you consolidate and prioritize cost optimization recommendations across your AWS accounts and AWS Regions, so that you can get the most out of your AWS spend.
- [AWS Control Tower](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-CTower.html): AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices.
- [Amazon Detective](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-detective.html): Amazon Detective uses your log data to generate visualizations that allow you to analyze, investigate, and identify the root cause of security findings or suspicious activity.
- [Amazon DevOpsÂ Guru](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-devops.html): Amazon DevOpsÂ Guru analyzes operational data and application metrics and events to identify behaviors that deviate from normal operating patterns.
- [AWS Directory Service](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-directory-service.html): AWS Directory Service for Microsoft Active Directory, or AWS Managed Microsoft AD, lets you run Microsoft Active Directory (AD) as a managed service.
- [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ec2.html): Amazon Elastic Compute Cloud provides on-demand, scalable computing capacity in the AWS Cloud.
- [EC2 Capacity Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ec2-capacity-manager.html): EC2 Capacity Manager is a new UI experience with accompanying APIs for you to aggregate, view, analyze, and manage your capacity usage across EC2 On-Demand, Spot, and Capacity Reservations.
- [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-eks.html): The Amazon Elastic Kubernetes Service Dashboard is a consolidated dashboard that you can use to monitor, manage, and gain visibility into your Kubernetes clusters across multiple AWS Regions and AWS Accounts.
- [AWS Firewall Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-fms.html): AWS Firewall Manager is a security management service you use to centrally configure and manage firewall rules and other protections across the AWS accounts and applications in your organization.
- [Amazon GuardDuty](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-guardduty.html): Amazon GuardDuty is a continuous security monitoring service that analyzes and processes a variety data sources, using threat intelligence feeds and machine learning to identify unexpected and potentially unauthorized and malicious activity within your AWS environment.
- [AWS Health](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-health.html): AWS Health provides ongoing visibility into your resource performance and the availability of your AWS services and accounts.
- [AWS Identity and Access Management](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-iam.html): AWS Identity and Access Management is a web service for securely controlling access to AWS services.
- [Amazon Inspector](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-inspector2.html): Amazon Inspector is an automated vulnerability management service that continually scans Amazon EC2 and container workloads for software vulnerabilities and unintended network exposure.
- [AWS License Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-license-manager.html): AWS License Manager streamlines the process of bringing software vendor licenses to the cloud.
- [AWS Managed Services (AMS) Self-Service Reporting (SSR)](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-managed-services.html): AWS Managed Services (AMS) Self-Service Reporting (SSR) collects data from various native AWS services and provides access to reports on major AMS offerings.
- [Amazon Macie](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-macie.html): Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover, monitor, and help you protect your sensitive data in Amazon Simple Storage Service (Amazon S3).
- [AWS Marketplace](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-marketplace.html): AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage third-party software, data, and services that you need to build solutions and run your businesses.
- [AWS Marketplace Private Marketplace](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-private-marketplace.html): AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage third-party software, data, and services that you need to build solutions and run your businesses.
- [AWS Marketplace procurement insights dashboard](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-procurement-insights.html): You use the AWS Marketplace procurement insights dashboard to view agreements and cost-analysis data for all of the AWS accounts in your organization.
- [AWS Network Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-network-manager.html): Network Manager enables you to centrally manage your AWS Cloud WAN core network and your AWS Transit Gateway network across AWS accounts, Regions, and on-premises locations.
- [Amazon Q Developer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-amazon-q-dev.html): Amazon Q Developer is a generative AI powered conversational assistant that can help you understand, build, extend, and operate AWS applications.
- [AWS Resource Access Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ram.html): AWS Resource Access Manager (AWS RAM) enables you to share specified AWS resources that you own with other AWS accounts.
- [AWS Resource Explorer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-resource-explorer.html): AWS Resource Explorer is a resource search and discovery service.
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html): AWS Security Hub CSPM provides you with a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices.
- [Amazon S3 Storage Lens](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-s3lens.html): By giving Amazon S3 Storage Lens trusted access to your organization, you allow it to collect and aggregate metrics across all of the AWS accounts in your organization.
- [AWS Security Incident Response](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-security-ir.html): AWS Security Incident Response is a security service that provides 24/7, live, human-assisted security incident support to help customers respond rapidly to cybersecurity incidents such as credential theft and ransomware attacks.
- [Amazon Security Lake](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-sl.html): Amazon Security Lake centralizes security data from cloud, on-premises, and custom sources into a data lake that's stored in your account.
- [AWS Service Catalog](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-servicecatalog.html): Service Catalog enables you to create and manage catalogs of IT services that are approved for use on AWS.
- [Service Quotas](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-servicequotas.html): Service Quotas is an AWS service that enables you to view and manage your quotas from a central location.
- [AWS IAM Identity Center](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-sso.html): AWS IAM Identity Center provides single sign-on access for all of your AWS accounts and cloud applications.
- [AWS Systems Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ssm.html): AWS Systems Manager is a collection of capabilities that enable visibility and control of your AWS resources.
- [AWS User Notifications](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-uno.html): AWS User Notifications is a central location for your AWS notifications.
- [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-tag-policies.html): Tag policies are a type of policy in AWS Organizations that can help you standardize tags across resources in your organization's accounts.
- [AWS Trusted Advisor](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ta.html): AWS Trusted Advisor inspects your AWS environment and makes recommendations when opportunities exist to save money, to improve system availability and performance, or to help close security gaps.
- [AWS Well-Architected Tool](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-wat.html): The AWS Well-Architected Tool helps you document the state of your workloads and compares them to the latest AWS architectural best practices.
- [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ipam.html): Amazon VPC IP Address Manager (IPAM) is a VPC feature that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads.
- [Amazon VPC Reachability Analyzer](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ra.html): Reachability Analyzer is a configuration analysis tool that enables you to perform connectivity testing between a source resource and a destination resource in your virtual private clouds (VPCs).
- [Delegated administrator for integrated AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html): Learn about requirements and permissions for delegated administrators.


## [Security](https://docs.aws.amazon.com/organizations/latest/userguide/security.html)

### [AWS PrivateLink](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_privatelink.html)

Learn how to integrate AWS PrivateLink with AWS Organizations.

- [Creating a VPC endpoint](https://docs.aws.amazon.com/organizations/latest/userguide/create-vpc-endpoint.html): You can create an AWS Organizations endpoint in your VPC using the Amazon VPC Console, the AWS Command Line Interface (AWS CLI) or CloudFormation.
- [Creating a VPC endpoint policy](https://docs.aws.amazon.com/organizations/latest/userguide/create-vpc-endpoint-policy.html): You can attach an endpoint policy to your VPC endpoint that controls access to Organizations.

### [Identity and Access Management](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_iam.html)

How to authenticate requests and manage access to your Organizations resources.

- [How AWS Organizations works with IAM](https://docs.aws.amazon.com/organizations/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Organizations, learn what IAM features are available to use with Organizations.
- [Managing access permissions for an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html): Learn about the permissions
- [Identity-based policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Organizations resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/security_iam_resource-based-policy-examples.html): The following code examples show how you can use resource-based delegation policies.
- [AWS managed policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_available-policies.html): AWS Organizations predefines several policies that are available for you to use to administer your organization.
- [Attribute-based access control with tags](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging_abac.html): Learn about using tags to secure AWS Organizations resources.
- [Troubleshooting](https://docs.aws.amazon.com/organizations/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Organizations and IAM.

### [Logging and monitoring](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_incident-response.html)

Monitor your organization by using AWS CloudTrail and Amazon EventBridge.

- [AWS CloudTrail](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_cloudtrail-integration.html): AWS Organizations is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Organizations.
- [Amazon EventBridge](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_cloudwatch-integration.html): AWS Organizations can work with Amazon EventBridge, formerly Amazon CloudWatch Events, to raise events when administrator-specified actions occur in an organization.
- [Compliance validation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Organizations features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_infrastructure.html): Learn how AWS Organizations isolates service traffic.


## [Code examples](https://docs.aws.amazon.com/organizations/latest/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/organizations/latest/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Organizations with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/organizations/latest/userguide/service_code_examples_actions.html)

The following code examples show how to use Organizations with AWS SDKs.

- [AttachPolicy](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_AttachPolicy_section.html): Use AttachPolicy with an AWS SDK or CLI
- [CreateAccount](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_CreateAccount_section.html): Use CreateAccount with an AWS SDK or CLI
- [CreateOrganization](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_CreateOrganization_section.html): Use CreateOrganization with an AWS SDK or CLI
- [CreateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_CreateOrganizationalUnit_section.html): Use CreateOrganizationalUnit with an AWS SDK or CLI
- [CreatePolicy](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_CreatePolicy_section.html): Use CreatePolicy with an AWS SDK or CLI
- [DeleteOrganization](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_DeleteOrganization_section.html): Use DeleteOrganization with an AWS SDK or CLI
- [DeleteOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_DeleteOrganizationalUnit_section.html): Use DeleteOrganizationalUnit with an AWS SDK or CLI
- [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_DeletePolicy_section.html): Use DeletePolicy with an AWS SDK or CLI
- [DescribePolicy](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_DescribePolicy_section.html): Use DescribePolicy with an AWS SDK or CLI
- [DetachPolicy](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_DetachPolicy_section.html): Use DetachPolicy with an AWS SDK or CLI
- [ListAccounts](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_ListAccounts_section.html): Use ListAccounts with an AWS SDK or CLI
- [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_ListOrganizationalUnitsForParent_section.html): Use ListOrganizationalUnitsForParent with an AWS SDK or CLI
- [ListPolicies](https://docs.aws.amazon.com/organizations/latest/userguide/example_organizations_ListPolicies_section.html): Use ListPolicies with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/organizations/latest/userguide/service_code_examples_scenarios.html)

The following code examples show how to use Organizations with AWS SDKs.

- [Permission policy allows AWS Compute Optimizer Automation to apply recommended actions](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.10_section.html): Allows the AWS Compute Optimizer Automation feature to apply recommended actions
- [Permission policy to enable Automation across your organization](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.2_section.html): Policy to enable Automation across your organization
- [Permission policy to enable Automation for your account](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.1_section.html): Policy to enable Automation for your account
- [Permission policy to grant full access to Compute Optimizer Automation for a management account of an organization](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section.html): Policy to grant full access to Compute Optimizer Automation for a management account of an organization
- [Permission policy to grant full access to Compute Optimizer Automation for standalone AWS accounts](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section.html): Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
- [Permission policy to grant read-only access to Compute Optimizer Automation for a management account of an organization](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.6_section.html): Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization
- [Permission policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.4_section.html): Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts
- [Permission policy to grant service-linked role permissions for Compute Optimization Automation](https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section.html): Policy to grants service-linked role permissions for Compute Optimization Automation
