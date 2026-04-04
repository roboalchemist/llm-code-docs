# Source: https://docs.aws.amazon.com/accounts/latest/reference/llms.txt

# AWS Account Management Reference Guide

> Learn about AWS accounts and how you can use them to interact with AWS services and the resources you create.

- [Close your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html)
- [Quotas](https://docs.aws.amazon.com/accounts/latest/reference/quotas.html)
- [Manage accounts in India](https://docs.aws.amazon.com/accounts/latest/reference/managing-accounts-india.html)
- [Document history](https://docs.aws.amazon.com/accounts/latest/reference/doc-history.html)

## [What is an AWS account?](https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html)

- [Related AWS services](https://docs.aws.amazon.com/accounts/latest/reference/accounts-related-services.html): Learn about AWS accounts and how to create and manage them.
- [Using the root user](https://docs.aws.amazon.com/accounts/latest/reference/root-user.html): Learn about managing the AWS account root user - its importance, proper use, and security best practices to protect it from misuse.
- [Support and feedback](https://docs.aws.amazon.com/accounts/latest/reference/accounts-support.html): Learn about AWS accounts and how to create and manage them.


## [Getting started with your account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html)

- [Review prerequisites](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html): Learn the essential prerequisites for setting up an AWS account, including obtaining the required email address, account name, and contact information.
- [Step 1: Create your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html): Learn how to sign up and create a standalone AWS account, enabling secure access control and seamless collaboration.
- [Step 2: Activate MFA for your root user](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-step3.html): Learn to configure multi-factor authentication for the root user in your new AWS account.
- [Step 3: Create an administrator user](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-step4.html): Learn to establish an administrator user with secure access controls for your new AWS account.
- [Accessing your account](https://docs.aws.amazon.com/accounts/latest/reference/accounts-access-account.html): Learn about AWS accounts and how to create and manage them.


## [Plan your governance structure](https://docs.aws.amazon.com/accounts/latest/reference/plan-acct-structure.html)

- [Benefits of using multiple AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/welcome-multiple-accounts.html): Learn about the benefits for using multiple AWS accounts within your organization, including considerations for account hierarchy, access control, and billing optimization.

### [When to use AWS Organizations](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs.html)

Learn how to use AWS Organizations to centrally manage and govern multiple AWS accounts, including features for account structure, policy enforcement, and billing consolidation.

- [Enable trusted access](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html): Learn how to configure trusted access between your AWS accounts and AWS Organizations, enabling secure cross-account collaboration and management.
- [Enable a delegated admin account](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-delegated-admin.html): Learn how to leverage delegated administration in AWS Organizations to grant privileged access to manage resources across your AWS accounts.
- [Restrict access using SCPs](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-example-scps.html): Learn how to use example service control policies (SCPs) in AWS Organizations to enforce security and compliance guardrails across your AWS accounts.
- [When to use AWS Control Tower](https://docs.aws.amazon.com/accounts/latest/reference/when-to-use-control-tower.html): Learn when to use AWS Control Tower to centrally govern and manage multiple AWS accounts within your organization, ensuring consistent security best practices and compliance.
- [Understanding API modes of operation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-api-modes-of-operation.html): Learn the different API modes of operation for managing AWS accounts, enabling flexible account administration and programmatic access controls.


## [Configure your account](https://docs.aws.amazon.com/accounts/latest/reference/managing-accounts.html)

- [Create or update your account alias](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-alias.html): Learn how to configure and use an alias for your AWS account.
- [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html): Learn how to enable and disable the AWS Regions that can be accessed by your AWS account, enabling geographic flexibility and data sovereignty compliance.
- [Update billing for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-billing.html): Learn to manage billing, costs, and payment methods for your AWS account, enabling effective cost optimization and budget tracking.
- [Update the root user email](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user-email.html): Learn how to securely update the root user email address for your AWS account.
- [Update root user password](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user-password.html): Learn how to update the root user password for your AWS account.
- [Update your AWS account name](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-acct-name.html): Learn how to securely update your AWS account name.
- [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html): Learn to update the alternate contact information for your AWS account, ensuring reliable communication and account access management.
- [Update the primary contact for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html): Learn to update the primary contact information for your AWS account, ensuring timely communication and account management updates.
- [View your account identifiers](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html): Learn to find and manage the unique identifiers associated with your AWS account, including account IDs and Amazon Resource Names (ARNs), to ensure secure access and resource identification.


## [Secure your account](https://docs.aws.amazon.com/accounts/latest/reference/security.html)

- [Data protection](https://docs.aws.amazon.com/accounts/latest/reference/security-data-protection.html): Learn strategies to ensure the security and data protection of your AWS account, including implementing access controls, encryption, and backup/recovery processes.

### [AWS PrivateLink](https://docs.aws.amazon.com/accounts/latest/reference/security-privatelink.html)

Learn how to use AWS PrivateLink to securely connect your AWS account to other AWS services and on-premises resources, enabling private data exchange.

- [Endpoint policies](https://docs.aws.amazon.com/accounts/latest/reference/vpc-iam.html): Learn how to create a VPC endpoint policy for AWS Account Management

### [Identity and Access Management](https://docs.aws.amazon.com/accounts/latest/reference/security-iam.html)

Learn how to leverage AWS Identity and Access Management (IAM) to implement robust security controls and access policies for your AWS account.

- [AWS Account Management and IAM](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html): Learn how to use features of IAM to help secure AWS Account Management and grant or restrict access.
- [Identity-based policy examples](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Account Management resources.
- [Using identity-based policies](https://docs.aws.amazon.com/accounts/latest/reference/security_account-permissions-ref.html): For a full discussion of AWS accounts and IAM users, see What Is IAM? in the IAM User Guide.
- [Troubleshooting](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Account Management and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/accounts/latest/reference/security-managed-policies.html): Learn how to leverage AWS-managed policies to simplify the application of security controls and permissions across your AWS account resources.
- [Compliance validation](https://docs.aws.amazon.com/accounts/latest/reference/compliance-validation.html): Learn how to ensure your AWS account meets critical compliance and security standards through validation, audits, and adherence to regulatory requirements.
- [Resilience](https://docs.aws.amazon.com/accounts/latest/reference/disaster-recovery-resiliency.html): Learn strategies to build disaster recovery and resilient infrastructure for your AWS account, ensuring business continuity and data protection.
- [Infrastructure security](https://docs.aws.amazon.com/accounts/latest/reference/infrastructure-security.html): Learn how AWS services in an AWS account isolate service traffic.


## [Monitor your account](https://docs.aws.amazon.com/accounts/latest/reference/monitoring.html)

- [CloudTrail logs](https://docs.aws.amazon.com/accounts/latest/reference/monitoring-cloudtrail.html): Learn how to leverage AWS CloudTrail to monitor and audit API activity within your AWS account, ensuring comprehensive visibility and security compliance.
- [Monitoring Account Management events with EventBridge](https://docs.aws.amazon.com/accounts/latest/reference/monitoring-eventbridge.html): Learn how to use Amazon EventBridge to monitor and automate events within your AWS account, enabling proactive incident response and event-driven workflows.


## [Troubleshoot your account](https://docs.aws.amazon.com/accounts/latest/reference/troubleshooting.html)

- [Account creation issues](https://docs.aws.amazon.com/accounts/latest/reference/troubleshooting_create-account.html): Learn about common issues that can occur when you attempt to create an AWS account and methods you can use to mitigate them.
- [Account closure issues](https://docs.aws.amazon.com/accounts/latest/reference/troubleshooting_close-account.html): Learn about common issues that can occur when you attempt to close an AWS account and methods you can use to mitigate them.
- [Other issues](https://docs.aws.amazon.com/accounts/latest/reference/troubleshooting_other.html): Learn about general issues that can occur when managing your AWS account and methods you can use to mitigate them.


## [API Reference](https://docs.aws.amazon.com/accounts/latest/reference/api-reference.html)

### [Actions](https://docs.aws.amazon.com/accounts/latest/reference/API_Operations.html)

The following actions are supported:

- [AcceptPrimaryEmailUpdate](https://docs.aws.amazon.com/accounts/latest/reference/API_AcceptPrimaryEmailUpdate.html): Accepts the request that originated from to update the primary email address (also known as the root user email address) for the specified account.
- [DeleteAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_DeleteAlternateContact.html): Deletes the specified alternate contact from an AWS account.
- [DisableRegion](https://docs.aws.amazon.com/accounts/latest/reference/API_DisableRegion.html): Disables (opts-out) a particular Region for an account.
- [EnableRegion](https://docs.aws.amazon.com/accounts/latest/reference/API_EnableRegion.html): Enables (opts-in) a particular Region for an account.
- [GetAccountInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetAccountInformation.html): Retrieves information about the specified account including its account name, account ID, and account creation date and time.
- [GetAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_GetAlternateContact.html): Retrieves the specified alternate contact attached to an AWS account.
- [GetContactInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetContactInformation.html): Retrieves the primary contact information of an AWS account.
- [GetGovCloudAccountInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetGovCloudAccountInformation.html): Retrieves information about the GovCloud account linked to the specified standard account (if it exists) including the GovCloud account ID and state.
- [GetPrimaryEmail](https://docs.aws.amazon.com/accounts/latest/reference/API_GetPrimaryEmail.html): Retrieves the primary email address for the specified account.
- [GetRegionOptStatus](https://docs.aws.amazon.com/accounts/latest/reference/API_GetRegionOptStatus.html): Retrieves the opt-in status of a particular Region.
- [ListRegions](https://docs.aws.amazon.com/accounts/latest/reference/API_ListRegions.html): Lists all the Regions for a given account and their respective opt-in statuses.
- [PutAccountName](https://docs.aws.amazon.com/accounts/latest/reference/API_PutAccountName.html): Updates the account name of the specified account.
- [PutAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_PutAlternateContact.html): Modifies the specified alternate contact attached to an AWS account.
- [PutContactInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_PutContactInformation.html): Updates the primary contact information of an AWS account.
- [StartPrimaryEmailUpdate](https://docs.aws.amazon.com/accounts/latest/reference/API_StartPrimaryEmailUpdate.html): Starts the process to update the primary email address for the specified account.

### [Related actions](https://docs.aws.amazon.com/accounts/latest/reference/API_Related_Operations.html)

Lists other related account actions that are supported by other services.

- [CreateAccount](https://docs.aws.amazon.com/accounts/latest/reference/API_CreateAccount.html): Provides information and links to the organization:CreateAccount API operation page.
- [CreateGovCloudAccount](https://docs.aws.amazon.com/accounts/latest/reference/API_CreateGovCloudAccount.html): Provides information and links to the organizations:CreateGovCloudAccount API operation page.
- [DescribeAccount](https://docs.aws.amazon.com/accounts/latest/reference/API_DescribeAccount.html): Provides information and links to the organizations:DescribeAccount API operation page.

### [Data Types](https://docs.aws.amazon.com/accounts/latest/reference/API_Types.html)

The following data types are supported:

- [AlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_AlternateContact.html): A structure that contains the details of an alternate contact associated with an AWS account
- [ContactInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_ContactInformation.html): Contains the details of the primary contact information associated with an AWS account.
- [Region](https://docs.aws.amazon.com/accounts/latest/reference/API_Region.html): This is a structure that expresses the Region for a given account, consisting of a name and opt-in status.
- [ValidationExceptionField](https://docs.aws.amazon.com/accounts/latest/reference/API_ValidationExceptionField.html): The input failed to meet the constraints specified by the AWS service in a specified field.
- [Common Parameters](https://docs.aws.amazon.com/accounts/latest/reference/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
- [Common Errors](https://docs.aws.amazon.com/accounts/latest/reference/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Making HTTP Query requests](https://docs.aws.amazon.com/accounts/latest/reference/query-requests.html): Learn how to query and analyze HTTPS requests and activity within your AWS account using the Account Management APIs, enabling comprehensive visibility.
