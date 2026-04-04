# Source: https://docs.aws.amazon.com/IAM/latest/UserGuide/llms.txt

# AWS Identity and Access Management User Guide

> Control access to your AWS resources with user identity (authentication) and with policies that define specific permissions (authorization).

- [Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/resources.html)
- [Making HTTP query requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/programming.html)
- [Document history](https://docs.aws.amazon.com/IAM/latest/UserGuide/document-history.html)

## [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

- [Why should I use IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-iam-features.html): AWS Identity and Access Management is a powerful tool for securely managing access to your AWS resources.
- [When do I use IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/when-to-use-iam.html): AWS Identity and Access Management is a core infrastructure service that provides the foundation for access control based on identities within AWS.
- [How do I manage IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-managing-iam.html): Managing AWS Identity and Access Management within an AWS environment involves leveraging a variety of tools and interfaces.
- [How IAM works](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html): Learn the infrastructure that AWS Identity and Access Management uses to control authorization and access control for your AWS account.
- [Compare IAM identities and credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html): Learn about users identities and federation in AWS Identity and Access Management (IAM).
- [How permissions and policies provide access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html): Learn about how identity-based policies and resource-based policies can be used in access management.
- [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html): Learn about using attribute-based access control in AWS.


## [Getting started](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)

- [Setting up your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html): Before you start working with IAM, make sure you have completed the initial set up of your AWS environment.
- [Viewing your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html): If you are signed into the console, you can view the account ID for your AWS account using the following methods.

### [Using an alias for your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-alias.html)

Find step-by-step instructions and CLI and API commands for creating an alias for your AWS account, which substitutes for an account ID in the URL for your account.

- [Creating an account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-alias-create.html): To perform the following steps, you must have at least the following IAM permissions:
- [Deleting an account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-alias-delete.html): To perform the following steps, you must have at least the following IAM permissions:

### [Plan access to your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities.html)

Learn about how to plan to give people access to your AWS account.

### [Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html)

IAM users that you create in your AWS account have long-term credentials that you manage directly.

- [Create an IAM user for emergency access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-emergency-iam-user.html): An IAM user is an identity within your AWS account that has specific permissions for a single person or application.
- [Create an IAM user for workloads](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-workloads.html): Provides a step-by-step tutorial on how to use the AWS Management Console to create an AWS Identity and Access Management (IAM user) and group and grant the user permissions to access your AWS resources.
- [Use multi-factor authentication with your identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-mfa.html): Using multi-factor authentication (MFA) with your identities is another IAM best practice.

### [Prepare for least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-reduce-permissions.html)

Using least-privilege permissions is an IAM best practice recommendation.

- [Reviewing last accessed information for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-reduce-permissions-last-accessed.html): You can view service last accessed information for IAM using the IAM console, AWS CLI, or AWS API.
- [Generating a policy based on access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_reduce-permissions-edit-policy.html): You can use the access activity recorded in AWS CloudTrail for an IAM user or IAM role to have IAM Access Analyzer generate a customer managed policy to allow access to only the services that specific users and roles need.
- [Using search to find IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_search.html): Use the IAM console search feature to locate access keys, users, groups, roles, identity providers, and policies.


## [Security best practices and use cases](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices-use-cases.html)

- [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html): Follow these best practices for using AWS Identity and Access Management (IAM) to help secure your AWS account and resources.
- [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html): Follow these best practices for using AWS Identity and Access Management (IAM) to help secure your AWS root user account.
- [Business use cases](https://docs.aws.amazon.com/IAM/latest/UserGuide/business-use-cases.html): Study business use cases and the lessons they offer for securing AWS resources with AWS Identity and Access Management (IAM).


## [Tutorials](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorials.html)

- [Delegate access across AWS accounts using roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html): Learn the steps for delegating API access in your AWS account to an AWS Identity and Access Management (IAM) user in another account. (First of four).
- [Create a customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html): Step-by-step guide to creating a customer managed policy using the IAM console.

### [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html)

Implement a strategy that uses principal and resource tags for permissions management.

- [Use SAML session tags for ABAC](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_abac-saml.html): Implement a strategy that uses SAML session tags and resource tags for permissions management.
- [Permit users to manage their credentials and MFA settings](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.html): Configure the users in your AWS account to self-manage their own passwords, MFA devices, and credentials.
- [Create SAML IdP with CloudFormation](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_saml-idp.html): Provides step-by-step tutorial for creating a SAML IdP using CloudFormation.
- [Create SAML federated role with CloudFormation](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_saml-federated-role.html): Provides step-by-step tutorial for creating a SAML federated IAM role using CloudFormation.
- [Create SAML IdP and federated role with CloudFormation](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_saml-idp-and-federated-role.html): Provides step-by-step tutorial for creating a SAML IdP and federated IAM role using CloudFormation.


## [Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

### [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

Manage the root user for an AWS account, including changing its password, and creating and removing access keys.

- [Centralize root access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html): Learn how to secure the root user credentials of your AWS accounts managed using AWS Organizations.
- [Perform a privileged task](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html): The AWS Organizations management account or a delegated administrator account for IAM can perform some root user tasks on member accounts using short-term root access.

### [MFA for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html)

Multi-factor authentication (MFA) is a simple and effective mechanism to enhance your security.

- [Enable a passkey or security key](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-fido-mfa-for-root.html): You can configure and enable a passkey for your root user from the AWS Management Console only, not from the AWS CLI or AWS API.
- [Enable a virtual MFA device](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html): You can use the AWS Management Console to configure and enable a virtual MFA device for your root user.
- [Enable a hardware TOTP token](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-hw-mfa-for-root.html): You can configure and enable a physical MFA device for your root user from the AWS Management Console only, not from the AWS CLI or AWS API.
- [Change the password](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-password.html): Learn how to change the password for the AWS account root user.
- [Reset a lost or forgotten root user password](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html): When you first created your AWS account, you provided an email address and password.
- [Create access keys for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_add-key.html)
- [Delete access keys for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_delete-key.html): You can use the AWS Management Console, the AWS CLI or the AWS API to delete the root user access keys.

### [Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)

Learn the relationship of IAM users to credentials, permissions, and AWS accounts.

### [How IAM users sign in to AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_sign-in.html)

Create a sign-in URL for IAM users to access the AWS Management Console and use the permitted resources in your AWS account.

- [MFA enabled sign-in](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_sign-in-mfa.html): Learn how multi-factor authentication (MFA) works with the AWS Management Console.
- [Create a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html): Basic overview of the process used to create an IAM user and credentials in AWS Identity and Access Management.
- [View IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_list.html): Learn how to list, rename, delete, or deactivate an IAM user in AWS Identity and Access Management.
- [Rename a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_rename.html): Learn how to list, rename, delete, or deactivate an IAM user in AWS Identity and Access Management.
- [Remove a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_remove.html): Learn how to remove or deactivate an IAM user in AWS Identity and Access Management.
- [Control user access to the console](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_controlling-access.html): Learn what permissions IAM users need in order to access the AWS Management Console, AWS resources, forums, billing information, account information, and security credentials.
- [Change user permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html): Use the AWS Management Console to change permissions associated with an IAM user.

### [User passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords.html)

Learn how to create, change, or delete passwords for IAM users in your account.

- [Set a password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html): Set a password policy to help users create strong passwords, and learn about password strength, minimum length, and rotation requirements.
- [Manage user passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html): Use AWS CLI or AWS API commands to create, change, or delete the password for an IAM user in your AWS account.
- [Permit IAM users to change their own passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html): Grant permissions to IAM users so they can change their own passwords.
- [How an IAM user changes their own password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_user-change-own.html): Change your own password as an IAM user if you have received the appropriate permissions.

### [Manage access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

Create, modify, view, or update access keys (credentials) for programmatic calls to AWS.

- [Control the use of access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys_inline-policy.html): As a best practice we recommend that workloads use temporary credentials with IAM roles to access AWS.
- [Permissions required to manage access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys_required-permissions.html)
- [How IAM users can manage their own access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-key-self-managed.html): IAM administrators can grant IAM users the permission to self-manage their access keys by attaching the policy described in .
- [How an IAM administrator can manage IAM user access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys-admin-managed.html): IAM administrators can create, activate, deactivate, and delete the access keys associated with individual IAM users.
- [Update access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html): Learn how to update access keys for AWS Identity and Access Management users.
- [Secure access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/securing_access-keys.html): Learn how to secure access keys for AWS Identity and Access Management users.

### [Multi-factor authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)

Multi-factor authentication in IAM helps you ensure users securely access AWS resources using two factor authentication.

### [Assign a passkey or security key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_fido.html)

Learn how to enable a passkey or security key for your AWS account.

- [Supported configurations for using passkeys and security keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_fido_supported_configurations.html): Use multi-factor authentication (MFA) in IAM by using supported configurations such as AWS supported FIDO2 devices and browsers with WebAuthn support.
- [Assign a virtual MFA device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html): Learn how to to set up a virtual MFA device using the IAM console.
- [Assign a hardware TOTP token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html): Use the AWS Management Console to enable a hardware-based multi-factor authentication (MFA) device for your AWS account.
- [Assign MFA devices in the AWS CLI or AWS API](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_cliapi.html): Learn how to use command line tools or the IAM API to enable a multi-factor authentication device in IAM.
- [Check MFA status](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_checking-status.html): Learn how to check whether a multi-factor authentication (MFA) device is enabled for an AWS account or IAM user.
- [Resynchronize virtual and hardware MFA devices](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html): Learn how to resync multi-factor authentication (MFA) devices with AWS Identity and Access Management.
- [Deactivate an MFA device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_disable.html): Learn how to deactivate a multi-factor authentication device in AWS Identity and Access Management.
- [Recover an MFA protected identity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html): Learn what to do in IAM when an MFA device is lost or stops working.
- [Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html): Configure IAM so that users must authenticate using MFA before they make programmatic calls to AWS services.
- [Sample code: MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sample-code.html): Examine sample code to see how to request temporary security credentials that enforce multi-factor authentication (MFA).

### [Service-specific credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_service-specific-creds.html)

Learn more about service-specific credentials for programmatic calls to specific AWS services.

- [API keys for Amazon Bedrock and Amazon CloudWatch Logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_bedrock_cloudwatchlogs.html): Generate and manage long-term API keys for Amazon Bedrock using the console, AWS CLI, or AWS API.
- [Use IAM with Amazon Keyspaces](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_keyspaces.html): Use Amazon Keyspaces (for Apache Cassandra) credentials.
- [Find unused credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html): Find potentially unused credentials so that they can be deleted and helping reduce the attack surface of the AWS account.
- [Generate credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html): Use IAM credential reports to view the status of all user credentials, including passwords, access keys, and multi-factor authentication (MFA) devices.
- [IAM credentials for CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html): Use Git credentials (static user name and password) or SSH keys (public and private key pairs) in AWS Identity and Access Management (IAM) for authentication with CodeCommit repositories.
- [Manage server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html): Upload and manage third-party X.509 SSL/TLS certificates (server certificates) with IAM for use with other AWS services.

### [User groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)

Use IAM user groups to simplify granting permissions to multiple users.

- [Create IAM groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html): Learn how to create an IAM groups and attach a policy that applies to all users in the group.
- [View IAM groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_list.html): Learn how to view all of the IAM groups in your AWS account, list the users in a user group, or list the IAM groups that a user belongs to.
- [Edit users in IAM groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html): Learn how to add or remove users from your IAM groups.
- [Attach a policy to a user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html): Learn how to attach or detach IAM policies from the IAM groups in your AWS account.
- [Rename a user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html): Learn how to rename the IAM user groups in your AWS account.
- [Delete an IAM group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html): Delete an IAM group in your AWS account.

### [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

Learn how and when to use IAM roles.

- [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

### [Common scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

Use IAM roles to grant special permissions for users, applications, and services.

- [Access across AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html): Use roles to grant an IAM user access to another AWS account that you own.
- [Access for non AWS workloads](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.html): Use IAM Roles Anywhere to grant access to non AWS workloads for your AWS account resources using roles.
- [Access to third-party AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html): Use roles to grant access to your AWS account to an AWS account owned by a third party.
- [Access to AWS services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_services.html): Use roles to grant an IAM user access to an AWS service.
- [Access through identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html): Use roles to grant an IAM user access through identity federation (authorization by an external service).

### [Role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)

Create an IAM role from the AWS Management Console, the AWS CLI, or the IAM API.

- [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html): Create an IAM role that determines the permissions that users have when they access resources that belong to the same or a different account.
- [Create a role for an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html): Create an IAM role that determines what an AWS service is allowed to do with AWS account resources.
- [Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html): Learn how to use service-linked roles to give a service access to resources in your AWS account.

### [Create a role for identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html)

Create an IAM role for users authenticated by third-party providers.

- [Create a role for OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html): Create an IAM role that determines what permissions that users have when they are authenticated through an OpenID connect-compatible identity provider.
- [Create a role for SAML 2.0 federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html): Create an IAM role that determines that permissions for users who are authenticated by a third-party provider.
- [Create a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html): Create an IAM role that determines the permissions that users have based on a custom trust policy.
- [Examples of policies for delegating access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_policy-examples.html): Find examples of policies that use roles to delegate cross-account permissions.

### [Role management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage.html)

Manage IAM roles from the AWS Management Console, the AWS CLI, or the API.

- [Grant permissions to switch roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html): Learn how to grant permissions to an IAM user, so that user can switch roles.
- [Grant permissions to pass a role to a service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html): Learn how to grant permissions to an IAM user to pass a role to an AWS service.
- [Revoke role temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html): Immediately revoke permissions from a console session or a role whose credentials have been compromised or are suspected of being compromised.
- [Update a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html): Learn how to edit service-linked roles to change the role description and maximum session duration.
- [Update a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-trust-policy.html): Learn how to update the role trust policy for an AWS Identity and Access Management role.
- [Update role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-permissions.html): Learn how to update the permissions policy and permissions boundaries for an AWS Identity and Access Management role.
- [Update role settings](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html): Learn how to update the role description and session duration for an AWS Identity and Access Management role.
- [Delete roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html): Use the AWS Management Console or AWS Command Line Interface to delete an IAM role and associated permissions or to remove roles from instance profiles.

### [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html)

Learn the different methods you can use to assume an IAM role.

- [Switch from a user to a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html): Use the AWS Management Console to switch from a user to a role to perform different tasks with different permissions.
- [Switch roles (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-cli.html): Use the AWS Command Line Interface to switch to an IAM role that provides temporary access to resources in an AWS account.
- [Switch roles (Tools for Windows PowerShell)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-twp.html): Use the Tools for Windows PowerShell to switch to an IAM role that provides temporary access to resources in an AWS account.
- [Switch roles (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html): Use the AWS API to switch to an IAM role that provides temporary access to resources in an AWS account.
- [Use roles for applications on Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html): Pass an IAM role to an Amazon EC2 instance to supply AWS credentials to applications running on the instance.
- [Use instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html): Use IAM instance profiles to pass a role to an Amazon EC2 instance when the instance starts.

### [Identity providers and federation into AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)

Create identity providers, which are entities in IAM to describe trust between a SAML 2.0 or OpenID Connect (OIDC) identity provider and AWS.

- [Common scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_federation_common_scenarios.html): Understand how identity federation works with IAM.

### [OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)

Create temporary AWS security credentials for applications that access AWS resources that do not run on AWS.

- [Create OIDC identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html): Create an OpenID Connect (OIDC) identity provider that describes a trust relationship between an OIDC-compatible IdP and AWS.
- [Obtain the thumbprint for an OIDC provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html): Manually obtain the thumbprint (signature) of the server certificate for an OIDC identity provider to validate that the certificate automatically retrieved by IAM is the correct one.
- [Identity-provider controls for shared OIDC providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_secure-by-default.html): For recognized shared OIDC providers, IAM requires explicit evaluation of specific claims in role trust policies to validate that only authorized federated identities can assume roles.

### [SAML 2.0 federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)

Use SAML federation to create temporary IAM security credentials that provide access to AWS resources.

- [Create SAML identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html): Create and update your IAM SAML provider, a trust relationship with between a SAML 2.0 IdP and AWS.
- [Configure relying party trust and claims](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.html): Configure trust between your SAML identity provider (IdP) and AWS.
- [Integrate third-party SAML solution providers with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.html): Get information about how to configure third-party IdP solutions with AWS SAML 2.0 federation.
- [Configure SAML assertions for the authentication response](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.html): Learn the requirements of SAML assertions that are sent by the SAML 2.0 identity provider service to AWS for validation.
- [Enable SAML federated principals access to AWS console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html): Configure IAM roles and SAML 2.0 IdPs to allow federated principals to access the AWS Management Console.
- [View SAML response in browser](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml_view-saml-response.html): Learn how to view a SAML response in your web browser for troubleshooting problems with AWS Identity and Access Management.

### [Federating AWS Identities to external services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html)

Use outbound identity federation to enable your AWS workloads to securely access external services without storing long-term credentials.

- [Getting started with outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html): This walkthrough guides you through enabling outbound identity federation for your AWS account and requesting your first identity token.
- [Understanding token claims](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_token_claims.html): Learn about the structure and contents of JSON Web Tokens (JWTs) returned by the GetWebIdentityToken API.
- [Controlling access with IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_policies.html): Use IAM policies to control access to outbound identity federation and enforce specific token properties.

### [Temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

Learn about temporary security credentials in AWS Identity and Access Management and how they are used.

- [Compare AWS STS credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html): Learn more about the types and features of temporary security credentials from AWS Security Token Service.
- [Service bearer tokens](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_bearer.html): Understand AWS STS service bearer tokens.
- [Request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html): Learn how to request temporary security credentials from AWS Security Token Service.
- [Use temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html): Learn how to use temporary security credentials from IAM STS to make programmatic requests for AWS resources with the AWS SDKs or API calls.

### [Permissions for temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access.html)

Learn how to create, update, or disable permissions that are assigned to temporary AWS security credentials.

- [Permissions for AssumeRole API operations](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_assumerole.html): Assign permissions to the temporary security credentials returned by the AWS STS API operations AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity.
- [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html): Use AWS CloudTrail logs to monitor who performed actions with your IAM roles by requiring that users set a source identity when assuming a role.
- [Permissions for GetFederationToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_getfederationtoken.html): Assign permissions to the temporary security credentials returned by the AWS STS API call GetFederationToken.
- [Permissions for GetSessionToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_getsessiontoken.html): Create and assign permissions to the temporary security credentials returned by the AWS STS API operation GetSessionToken.
- [Disabling permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_disable-perms.html): Disable or revoke permissions assigned to AWS STS temporary security credentials, to the creator of the credentials, and to credentials by name or by the time created.
- [Granting permissions to create credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_enable-create.html): Grant permissions to an IAM group to create temporary AWS security credentials for federated users.
- [Granting permissions to use identity-enhanced console sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.html): Grant permission to use identity-enhanced console sessions.
- [Manage AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html): Learn how to manage AWS STS with Regional and global endpoints.
- [AWS STS Regions and endpoints](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_region-endpoints.html): Learn about the available AWS STS Regions and endpoints.
- [Enable custom identity broker console access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html): Create a URL with a sign-in token to give roles and federated principals single sign-on (SSO) access to the AWS Management Console.

### [Tags for IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)

Learn about custom key-value pair attributes you can assign to IAM resources to control access.

- [Tag IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_users.html): Learn how to use IAM tag key-value pairs to add custom attributes to an IAM user.
- [Tag IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_roles.html): Learn how to tag IAM roles to control access to your AWS resources.
- [Tag customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_customer-managed-policies.html): Learn how to add custom attributes to your identity-based policies to control access to your AWS resources.
- [Tag OIDC identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_oidc.html): Learn how to add custom attributes to OIDC identity providers to control access to your AWS resources.
- [Tag IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_saml.html): Learn how to add custom attributes to SAML identity providers to control access to your AWS resources.
- [Tagging instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_instance-profiles.html): Learn how to tag instance profile roles to control access to your AWS resources.
- [Tag server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_server-certificates.html): Use IAM tag key-value pairs to add custom attributes to a server certificate.
- [Tag virtual MFA devices](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_virtual-mfa.html): Use IAM tag key-value pairs to add custom attributes to a virtual MFA device.
- [Pass session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html): Learn how to use session tags to add or import attributes when you assume an IAM role or federate an IAM user.


## [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html)

### [Policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

Learn about AWS policies and how they work to define permissions for AWS services and resources.

### [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)

Learn the differences between an AWS managed policy, a customer managed policy, and an inline policy.

- [Choose between managed or inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html): Explain use cases for choosing an inline policy or a managed policy.
- [Convert inline policy to managed](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-convert-inline-to-managed.html): Convert an inline policy to a managed policy that can be attached to multiple principal entities.
- [Deprecated AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-deprecated.html): Understand deprecated AWS managed policies and what to do to replace them.
- [Data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html): Learn how data perimeters policies can be used to help protect your data across a broad set of AWS accounts and resources.
- [Permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html): Learn how policies can be used to set the permissions boundary for a user or role.
- [Identity vs resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html): Learn the difference between identity-based policies and resource-based policies.
- [Control access using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html): Learn how to control access to resources within AWS Identity and Access Management or all of AWS.
- [Control access to IAM users and roles using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html): Use tags to control access to IAM users and roles.
- [Control access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html): Use tags on your AWS resources to control access.
- [Cross account resource access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html): Define permissions on a resource in order to grant IAM users access to resources in other AWS accounts.
- [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html): Learn about passing your identity, permissions, and session attributes when an AWS service makes a request on your behalf.

### [Example policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)

Use this library of example IAM identity-based policies to build your own policies.

- [AWS: Specific access during a date range](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws-dates.html): Use this IAM example policy to allow specific access during a date range
- [AWS: Enable or disable AWS Regions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.html): Use this IAM example policy to allow enabling and disabling AWS Regions.
- [AWS: Self-manage credentials with MFA (Security credentials)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage.html): Use this IAM policy to allow users to manage their credentials in the AWS Management Console.
- [AWS: Specific access with MFA during a date range](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_mfa-dates.html): Use this IAM example policy to allow specific access during a date range
- [AWS: Self-manage credentials no MFA (Security credentials)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-no-mfa.html): Use this IAM policy to allow users to manage all credentials except MFA in the AWS Management Console.
- [AWS: Self-manage MFA device (Security credentials)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.html): Use this IAM policy to allow users to manage their MFA device in the AWS Management Console.
- [AWS: Self-manage console password (Security credentials)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-password-only.html): Use this IAM policy to allow users to change their own console password.
- [AWS: Self-manage password, access keys, & SSH public keys (My security credentials)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-pass-accesskeys-ssh.html): Use this IAM policy to allow users to manage their password, access keys, and SSH public keys.
- [AWS: Deny access based on requested Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html): Use this IAM policy to deny access to AWS based on the requested region.
- [AWS: Deny access based on source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html): Use this IAM policy to deny access to AWS based on the source IP.
- [AWS: Deny access to Amazon S3 resources outside your account except AWS Data Exchange](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_resource_account_data_exch.html): This example shows how you might create an identity-based policy that denies access to all resources in AWS that don't belong to your account, except for the resources that AWS Data Exchange requires for normal operation.
- [Data Pipeline: Deny access to pipelines not created by user](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_datapipeline_not-owned.html): Use this IAM policy to deny DataPipeline access to pipelines that a user did not create.
- [DynamoDB: Access specific table](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.html): Use this IAM policy to allow access to a specific DynamoDB table.
- [DynamoDB: Allow access to specific attributes](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_attributes.html): Use this IAM policy to allow access to attributes in DynamoDB.
- [DynamoDB: Allow item access based on a Amazon Cognito ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_items.html): Use this IAM policy to allow item access in DynamoDB based on Amazon Cognito ID.
- [EC2: Attach or detach tagged EBS volumes](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_ebs-owner.html): Use this IAM policy to attach or detach EBS volumes to EC2 instances based on tags.
- [EC2: Launch instances in a subnet (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_instances-subnet.html): Use this IAM policy to launch EC2 instances in a subnet and use the AWS Management Console..
- [EC2: Manage security groups with the same tags (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_securitygroups-vpc.html): Use this IAM policy to manage Amazon EC2 security groups with the same tags.
- [EC2: Start or stop instances a user has tagged (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_tag-owner.html): Use this IAM policy to start or stop EC2 instances a user has tagged.
- [EC2: Start or stop instances based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2-start-stop-tags.html): Use this EC2 policy to start/stop instances based on tags.
- [EC2: Start or stop for matching tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2-start-stop-match-tags.html): Use this EC2 policy to start/stop instances based on matching principal and resource tags.
- [EC2: Full access within a Region (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_region.html): Use this IAM policy to restrict Amazon EC2 access to a specific Region
- [EC2: Start or stop an instance, modify security group (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_instance-securitygroup.html): Use this IAM policy to start and stop an EC2 instance and modify its security group.
- [EC2: Requires MFA (GetSessionToken) for operations](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_require-mfa.html): Use this IAM policy to require MFA for specific Amazon EC2 operations.
- [EC2: Limit terminating instances to IP range](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_terminate-ip.html): Use this IAM policy to terminate EC2 instances based on the source IP address.
- [IAM: Access the policy simulator API](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_policy-sim.html): Use this IAM policy to use the policy simulator API to simulate any policy that is attached to a user, group, or role.
- [IAM: Access the policy simulator console](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_policy-sim-console.html): Use this IAM policy to allow access to the policy simulator in the AWS Management Console.
- [IAM: Assume tagged roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-assume-tagged-role.html): Use this IAM policy to assume roles that have a specific tag.
- [IAM: Allows and denies multiple services (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_multiple-services-console.html): Use this IAM policy to allow and deny access to multiple services.
- [IAM: Add specific tag to tagged user](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-add-tag.html): Use this IAM policy to add a specific tag to a user with a specific tag.
- [IAM: Add a specific tag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-add-tag-user-role.html): Use this IAM policy to add a specific tag with specific values.
- [IAM: Create only tagged users](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-new-user-tag.html): Use this IAM policy to create new users only with specific tags.
- [IAM: Generate credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-credential-report.html): Use this IAM policy to generate and retrieve IAM credential reports.
- [IAM: Manage group membership (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_manage-group-membership.html): Use this IAM policy to allow managing a group's membership.
- [IAM: Manage a tag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-manage-tags.html): Use this IAM policy to manage a specific tag.
- [IAM: Pass a role to a service](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html): Use this IAM policy to pass a role to a service.
- [IAM: Read-only console access (no reporting)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_read-only-console-no-reporting.html): Use this IAM policy to allow read-only access to the IAM console without reporting.
- [IAM: Read-only console access](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_read-only-console.html): Use this IAM policy to allow read-only access to the IAM console.
- [IAM: Specific users manage group (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_users-manage-group.html): Use this IAM policy to allow specific users to manage a group.
- [IAM: Setting account password requirements (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_set-account-pass-policy.html): Use this IAM policy to allow setting the account password requirements.
- [IAM: Access the policy simulator API based on user path](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_policy-sim-path.html): Use this IAM policy to use the policy simulator API based on the user path.
- [IAM: Access the policy simulator console based on user path (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_policy-sim-path-console.html): Use this IAM policy to allow access to the policy simulator console based on the user path in the AWS Management Console.
- [IAM: MFA self-management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_mfa-selfmanage.html): Use this IAM policy to allow users to self-manage an MFA device.
- [IAM: Update credentials (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_credentials_console.html): Use this IAM policy to allow users to rotate credentials in the AWS Management Console.
- [IAM: View AWS Organizations service last accessed information for a policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_service-accessed-data-orgs.html): Use this IAM policy to allow viewing last accessed information for an AWS Organizations policy in the IAM console.
- [IAM: Apply limited managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_limit-managed.html): Use this IAM policy to limit the attaching of managed policies to a new IAM user, group, or role.
- [AWS: Deny access to resources outside your account except AWS managed IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/resource_examples_iam_policies_resource_account.html): Using aws:ResourceAccount in your identity-based policies can impact the user or the role's ability to utilize some services that require interaction with resources in accounts owned by a service.
- [Lambda: Service access to DynamoDB](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_lambda-access-dynamodb.html): Use this IAM policy to allow a Lambda function to access a DynamoDB table.
- [RDS: Full access within a Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_rds_region.html): Use this IAM policy to provide full access to Amazon RDS in a specific Region.
- [RDS: Restore databases (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_rds_db-console.html): Use this IAM policy to restore Amazon RDS databases from the AWS Management Console.
- [RDS: Full access for tag owners](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_rds_tag-owner.html): Use this IAM policy to access existing Amazon RDS resources based on the tag owner.
- [S3: Access bucket if cognito](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_cognito-bucket.html): Use this IAM policy to provide access to Amazon S3 objects in the owner's bucket.
- [S3: Access federated principal home directory (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_federated-home-directory-console.html): Use this IAM policy to provide access to an Amazon S3 home directory in the AWS Management Console.
- [S3: Full access with recent MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_full-access-except-production.html): Use this IAM policy to limit a user to only manage a specific S3 bucket
- [S3: Access IAM user home directory (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_home-directory-console.html): Use this IAM policy to provide access to an Amazon S3 home directory in the AWS Management Console.
- [S3: Restrict management to a specific bucket](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_deny-except-bucket.html): Use this IAM policy to limit a user to only manage a specific S3 bucket
- [S3: Read and write objects to a specific bucket](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html): Learn how to use an IAM policy to grant read and write access to objects in a specific Amazon S3 bucket, enabling management of bucket contents programmatically via AWS CLI or APIs.
- [S3: Read and write to a specific bucket (includes console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket-console.html): Use this IAM policy to provide access to the AWS Management Console and read and write access to objects in an Amazon S3 bucket.

### [Manage IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)

Learn how to create AWS Identity and Access Management policies, attach them to users, view policies, and delete policies using the AWS Management Console, the AWS Command Line Interface (AWS CLI), and the IAM API.

### [Create IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)

Learn how to create customer managed policies in IAM to define permissions for identities and resources using the AWS Management Console, AWS CLI, or API.

- [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html): Learn how to create an IAM policy using the AWS Management Console.
- [Create IAM policies (CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-cli.html): Learn how to create an IAM policy using the AWS CLI.
- [Create IAM policies (API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-api.html): Learn how to create an IAM policy using the AWS API.
- [Policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html): Use policy validation to view potential issues in your policies and correct them.
- [Policy testing](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html): Use the IAM policy simulator to test and troubleshoot IAM policies that are attached to users, IAM groups, roles, or resources.
- [Add or remove identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html): Attach and detach IAM policies using the console, CLI, or API.
- [Versioning IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html): Learn how IAM policy versioning works and how changes to managed policies become new versions of the policy.

### [Edit IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html)

Learn how to update AWS Identity and Access Management policies using the AWS Management Console, AWS Command Line Interface or AWS API.

- [Edit IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit-console.html): Edit IAM policies using the AWS Management Console.
- [Edit IAM policies (CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit-cli.html): Edit IAM policies using the AWS Command Line Interface.
- [Edit IAM policies (API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit-api.html): Edit IAM policies using the AWS API.

### [Delete IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete.html)

Learn how to delete IAM policies using the console, CLI, or API.

- [Delete IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete-console.html): Learn how to delete IAM policies using the console.
- [Delete IAM policies (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete-cli.html): Learn how to delete IAM policies using the CLI.
- [Delete IAM policies (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete-api.html): Learn how to delete IAM policies using the API.

### [Refine permissions using access information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html)

Use IAM last accessed information for services and actions to provide only necessary permissions.

- [View IAM access information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data.html): Learn how to view last accessed information for IAM.
- [View access information for AWS Organizations](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html): How to view last accessed information for AWS Organizations
- [Example scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-example-scenarios.html): Scenarios for using information to reduce permissions
- [Action last accessed services and actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-action-last-accessed.html): A list of services and actions for which IAM action last accessed information is displayed.

### [Policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand.html)

Use the IAM policy summary to understand the permissions granted by a policy.

### [Policy summary (list of services)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand-policy-summary.html)

Use the IAM policy summary's list of services to understand the permissions that the policy grants for each service.

- [View policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_view-policy-summary.html): Use the IAM policy summary's list of services to understand the permissions that the policy grants for each service.
- [Access levels in policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.html): Use the IAM policy summary's access level summaries to understand the access level that the policy grants for each service.

### [Service summary (list of actions)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand-service-summary.html)

Use the policy summary's list of actions to understand the permissions defined for each action within a chosen service.

- [View service summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_view-service-summary.html): Use the policy summary's list of actions to understand the permissions defined for each action within a chosen service.

### [Action summary (list of resources)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand-action-summary.html)

Use the policy summary's list of resources to understand the permissions defined for each resource within a chosen service and action.

- [View action summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_view-action-summary.html): Use the policy summary's list of resources to understand the permissions defined for each resource within a chosen service and action.
- [Example policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-summary-examples.html): Learn more about policy summaries by comparing examples with their associated JSON policy documents.

### [Permissions required to access IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html)

Learn what permissions are required to access IAM resources.

- [Example policies for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_delegate-permissions_examples.html): Consult examples of IAM policies that let users perform tasks associated with managing and administering IAM resources.

### [Temporary delegation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html)

Learn how to use IAM temporary delegation to grant Amazon and AWS Partners limited, temporary access to configure AWS services in your account.

- [Initiate a temporary delegation request](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-initiate-request.html): You can initiate a temporary delegation request only from supported Amazon or AWS Partner products.
- [Review Temporary delegation requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-review-requests.html): After initiating a temporary delegation request, you can monitor, approve, and reject requests in the IAM console.
- [Revoke Temporary delegation access](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-revoke-access.html): Although product provider access sessions are designed to expire automatically after their approved duration, you may need to terminate access immediately in certain situations.
- [Notifications](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-notifications.html): IAM temporary delegation integrates with AWS User Notifications to help you stay informed about delegation request state changes.
- [CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-cloudtrail.html): All actions performed by product providers using temporary delegated access are automatically logged in AWS CloudTrail.

### [Temporary delegation for Partners](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation-partner-guide.html)

Learn how AWS Partners can integrate IAM temporary delegation into their products to streamline customer onboarding and reduce integration complexity.

- [Understanding your integration](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-understanding-integration.html): After completing the onboarding process, you can build your integration with IAM temporary delegation.
- [Understanding permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-understanding-permissions.html): As part of the feature onboarding process, you will need to register policies with IAM that define the permissions you want to request in customers' AWS accounts.
- [Policy evaluation guidelines](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-policy-evaluation-guidelines.html): AWS will evaluate your submitted policies against a set of guidelines.
- [Policy templates](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-policy-templates.html): Policy templates are a new IAM construct designed for defining temporary permissions that partners request in customers' accounts.
- [Building your integration](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-building-integration.html)


## [Code examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples.html)

### [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_iam.html)

Code examples that show how to use IAM with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_iam_basics.html)

The following code examples show how to use the basics of IAM with AWS SDKs.

- [Hello IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Hello_section.html): Hello IAM
- [Learn the basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_CreateUserAssumeRole_section.html): Learn the basics of IAM with an AWS SDK

### [Actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_iam_actions.html)

The following code examples show how to use IAM with AWS SDKs.

- [AddClientIdToOpenIdConnectProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AddClientIdToOpenIdConnectProvider_section.html): Use AddClientIdToOpenIdConnectProvider with a CLI
- [AddRoleToInstanceProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AddRoleToInstanceProfile_section.html): Use AddRoleToInstanceProfile with a CLI
- [AddUserToGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AddUserToGroup_section.html): Use AddUserToGroup with a CLI
- [AttachGroupPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AttachGroupPolicy_section.html): Use AttachGroupPolicy with a CLI
- [AttachRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AttachRolePolicy_section.html): Use AttachRolePolicy with an AWS SDK or CLI
- [AttachUserPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_AttachUserPolicy_section.html): Use AttachUserPolicy with an AWS SDK or CLI
- [ChangePassword](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ChangePassword_section.html): Use ChangePassword with a CLI
- [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateAccessKey_section.html): Use CreateAccessKey with an AWS SDK or CLI
- [CreateAccountAlias](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateAccountAlias_section.html): Use CreateAccountAlias with an AWS SDK or CLI
- [CreateGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateGroup_section.html): Use CreateGroup with an AWS SDK or CLI
- [CreateInstanceProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateInstanceProfile_section.html): Use CreateInstanceProfile with an AWS SDK or CLI
- [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateLoginProfile_section.html): Use CreateLoginProfile with a CLI
- [CreateOpenIdConnectProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateOpenIdConnectProvider_section.html): Use CreateOpenIdConnectProvider with a CLI
- [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreatePolicy_section.html): Use CreatePolicy with an AWS SDK or CLI
- [CreatePolicyVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreatePolicyVersion_section.html): Use CreatePolicyVersion with an AWS SDK or CLI
- [CreateRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateRole_section.html): Use CreateRole with an AWS SDK or CLI
- [CreateSAMLProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateSAMLProvider_section.html): Use CreateSAMLProvider with an AWS SDK or CLI
- [CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateServiceLinkedRole_section.html): Use CreateServiceLinkedRole with an AWS SDK or CLI
- [CreateUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateUser_section.html): Use CreateUser with an AWS SDK or CLI
- [CreateVirtualMfaDevice](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_CreateVirtualMfaDevice_section.html): Use CreateVirtualMfaDevice with a CLI
- [DeactivateMfaDevice](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeactivateMfaDevice_section.html): Use DeactivateMfaDevice with a CLI
- [DeleteAccessKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteAccessKey_section.html): Use DeleteAccessKey with an AWS SDK or CLI
- [DeleteAccountAlias](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteAccountAlias_section.html): Use DeleteAccountAlias with an AWS SDK or CLI
- [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteAccountPasswordPolicy_section.html): Use DeleteAccountPasswordPolicy with a CLI
- [DeleteGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteGroup_section.html): Use DeleteGroup with an AWS SDK or CLI
- [DeleteGroupPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteGroupPolicy_section.html): Use DeleteGroupPolicy with a CLI
- [DeleteInstanceProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteInstanceProfile_section.html): Use DeleteInstanceProfile with an AWS SDK or CLI
- [DeleteLoginProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteLoginProfile_section.html): Use DeleteLoginProfile with a CLI
- [DeleteOpenIdConnectProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteOpenIdConnectProvider_section.html): Use DeleteOpenIdConnectProvider with a CLI
- [DeletePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeletePolicy_section.html): Use DeletePolicy with an AWS SDK or CLI
- [DeletePolicyVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeletePolicyVersion_section.html): Use DeletePolicyVersion with an AWS SDK or CLI
- [DeleteRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteRole_section.html): Use DeleteRole with an AWS SDK or CLI
- [DeleteRolePermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteRolePermissionsBoundary_section.html): Use DeleteRolePermissionsBoundary with a CLI
- [DeleteRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteRolePolicy_section.html): Use DeleteRolePolicy with an AWS SDK or CLI
- [DeleteSAMLProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteSAMLProvider_section.html): Use DeleteSAMLProvider with an AWS SDK or CLI
- [DeleteServerCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteServerCertificate_section.html): Use DeleteServerCertificate with an AWS SDK or CLI
- [DeleteServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteServiceLinkedRole_section.html): Use DeleteServiceLinkedRole with an AWS SDK or CLI
- [DeleteSigningCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteSigningCertificate_section.html): Use DeleteSigningCertificate with a CLI
- [DeleteUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteUser_section.html): Use DeleteUser with an AWS SDK or CLI
- [DeleteUserPermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteUserPermissionsBoundary_section.html): Use DeleteUserPermissionsBoundary with a CLI
- [DeleteUserPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteUserPolicy_section.html): Use DeleteUserPolicy with an AWS SDK or CLI
- [DeleteVirtualMfaDevice](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DeleteVirtualMfaDevice_section.html): Use DeleteVirtualMfaDevice with a CLI
- [DetachGroupPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DetachGroupPolicy_section.html): Use DetachGroupPolicy with a CLI
- [DetachRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DetachRolePolicy_section.html): Use DetachRolePolicy with an AWS SDK or CLI
- [DetachUserPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_DetachUserPolicy_section.html): Use DetachUserPolicy with an AWS SDK or CLI
- [EnableMfaDevice](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_EnableMfaDevice_section.html): Use EnableMfaDevice with a CLI
- [GenerateCredentialReport](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GenerateCredentialReport_section.html): Use GenerateCredentialReport with an AWS SDK or CLI
- [GenerateServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GenerateServiceLastAccessedDetails_section.html): Use GenerateServiceLastAccessedDetails with a CLI
- [GetAccessKeyLastUsed](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetAccessKeyLastUsed_section.html): Use GetAccessKeyLastUsed with an AWS SDK or CLI
- [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetAccountAuthorizationDetails_section.html): Use GetAccountAuthorizationDetails with an AWS SDK or CLI
- [GetAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetAccountPasswordPolicy_section.html): Use GetAccountPasswordPolicy with an AWS SDK or CLI
- [GetAccountSummary](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetAccountSummary_section.html): Use GetAccountSummary with an AWS SDK or CLI
- [GetContextKeysForCustomPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetContextKeysForCustomPolicy_section.html): Use GetContextKeysForCustomPolicy with a CLI
- [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetContextKeysForPrincipalPolicy_section.html): Use GetContextKeysForPrincipalPolicy with a CLI
- [GetCredentialReport](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetCredentialReport_section.html): Use GetCredentialReport with an AWS SDK or CLI
- [GetGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetGroup_section.html): Use GetGroup with a CLI
- [GetGroupPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetGroupPolicy_section.html): Use GetGroupPolicy with a CLI
- [GetInstanceProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetInstanceProfile_section.html): Use GetInstanceProfile with a CLI
- [GetLoginProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetLoginProfile_section.html): Use GetLoginProfile with a CLI
- [GetOpenIdConnectProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetOpenIdConnectProvider_section.html): Use GetOpenIdConnectProvider with a CLI
- [GetPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetPolicy_section.html): Use GetPolicy with an AWS SDK or CLI
- [GetPolicyVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetPolicyVersion_section.html): Use GetPolicyVersion with an AWS SDK or CLI
- [GetRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetRole_section.html): Use GetRole with an AWS SDK or CLI
- [GetRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetRolePolicy_section.html): Use GetRolePolicy with a CLI
- [GetSamlProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetSamlProvider_section.html): Use GetSamlProvider with a CLI
- [GetServerCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetServerCertificate_section.html): Use GetServerCertificate with an AWS SDK or CLI
- [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetServiceLastAccessedDetails_section.html): Use GetServiceLastAccessedDetails with a CLI
- [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetServiceLastAccessedDetailsWithEntities_section.html): Use GetServiceLastAccessedDetailsWithEntities with a CLI
- [GetServiceLinkedRoleDeletionStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetServiceLinkedRoleDeletionStatus_section.html): Use GetServiceLinkedRoleDeletionStatus with an AWS SDK or CLI
- [GetUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetUser_section.html): Use GetUser with an AWS SDK or CLI
- [GetUserPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_GetUserPolicy_section.html): Use GetUserPolicy with a CLI
- [ListAccessKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAccessKeys_section.html): Use ListAccessKeys with an AWS SDK or CLI
- [ListAccountAliases](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAccountAliases_section.html): Use ListAccountAliases with an AWS SDK or CLI
- [ListAttachedGroupPolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAttachedGroupPolicies_section.html): Use ListAttachedGroupPolicies with a CLI
- [ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAttachedRolePolicies_section.html): Use ListAttachedRolePolicies with an AWS SDK or CLI
- [ListAttachedUserPolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAttachedUserPolicies_section.html): Use ListAttachedUserPolicies with a CLI
- [ListEntitiesForPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListEntitiesForPolicy_section.html): Use ListEntitiesForPolicy with a CLI
- [ListGroupPolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListGroupPolicies_section.html): Use ListGroupPolicies with a CLI
- [ListGroups](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListGroups_section.html): Use ListGroups with an AWS SDK or CLI
- [ListGroupsForUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListGroupsForUser_section.html): Use ListGroupsForUser with a CLI
- [ListInstanceProfiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListInstanceProfiles_section.html): Use ListInstanceProfiles with a CLI
- [ListInstanceProfilesForRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListInstanceProfilesForRole_section.html): Use ListInstanceProfilesForRole with a CLI
- [ListMfaDevices](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListMfaDevices_section.html): Use ListMfaDevices with a CLI
- [ListOpenIdConnectProviders](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListOpenIdConnectProviders_section.html): Use ListOpenIdConnectProviders with a CLI
- [ListPolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListPolicies_section.html): Use ListPolicies with an AWS SDK or CLI
- [ListPolicyVersions](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListPolicyVersions_section.html): Use ListPolicyVersions with an AWS SDK or CLI
- [ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListRolePolicies_section.html): Use ListRolePolicies with an AWS SDK or CLI
- [ListRoleTags](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListRoleTags_section.html): Use ListRoleTags with a CLI
- [ListRoles](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListRoles_section.html): Use ListRoles with an AWS SDK or CLI
- [ListSAMLProviders](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListSAMLProviders_section.html): Use ListSAMLProviders with an AWS SDK or CLI
- [ListServerCertificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListServerCertificates_section.html): Use ListServerCertificates with an AWS SDK or CLI
- [ListSigningCertificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListSigningCertificates_section.html): Use ListSigningCertificates with a CLI
- [ListUserPolicies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListUserPolicies_section.html): Use ListUserPolicies with an AWS SDK or CLI
- [ListUserTags](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListUserTags_section.html): Use ListUserTags with a CLI
- [ListUsers](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListUsers_section.html): Use ListUsers with an AWS SDK or CLI
- [ListVirtualMfaDevices](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListVirtualMfaDevices_section.html): Use ListVirtualMfaDevices with a CLI
- [PutGroupPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_PutGroupPolicy_section.html): Use PutGroupPolicy with a CLI
- [PutRolePermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_PutRolePermissionsBoundary_section.html): Use PutRolePermissionsBoundary with a CLI
- [PutRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_PutRolePolicy_section.html): Use PutRolePolicy with an AWS SDK or CLI
- [PutUserPermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_PutUserPermissionsBoundary_section.html): Use PutUserPermissionsBoundary with a CLI
- [PutUserPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_PutUserPolicy_section.html): Use PutUserPolicy with an AWS SDK or CLI
- [RemoveClientIdFromOpenIdConnectProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_RemoveClientIdFromOpenIdConnectProvider_section.html): Use RemoveClientIdFromOpenIdConnectProvider with a CLI
- [RemoveRoleFromInstanceProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_RemoveRoleFromInstanceProfile_section.html): Use RemoveRoleFromInstanceProfile with a CLI
- [RemoveUserFromGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_RemoveUserFromGroup_section.html): Use RemoveUserFromGroup with a CLI
- [ResyncMfaDevice](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ResyncMfaDevice_section.html): Use ResyncMfaDevice with a CLI
- [SetDefaultPolicyVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_SetDefaultPolicyVersion_section.html): Use SetDefaultPolicyVersion with an AWS SDK or CLI
- [TagRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_TagRole_section.html): Use TagRole with a CLI
- [TagUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_TagUser_section.html): Use TagUser with a CLI
- [UntagRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UntagRole_section.html): Use UntagRole with a CLI
- [UntagUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UntagUser_section.html): Use UntagUser with a CLI
- [UpdateAccessKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateAccessKey_section.html): Use UpdateAccessKey with an AWS SDK or CLI
- [UpdateAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateAccountPasswordPolicy_section.html): Use UpdateAccountPasswordPolicy with a CLI
- [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateAssumeRolePolicy_section.html): Use UpdateAssumeRolePolicy with a CLI
- [UpdateGroup](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateGroup_section.html): Use UpdateGroup with a CLI
- [UpdateLoginProfile](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateLoginProfile_section.html): Use UpdateLoginProfile with a CLI
- [UpdateOpenIdConnectProviderThumbprint](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateOpenIdConnectProviderThumbprint_section.html): Use UpdateOpenIdConnectProviderThumbprint with a CLI
- [UpdateRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateRole_section.html): Use UpdateRole with a CLI
- [UpdateRoleDescription](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateRoleDescription_section.html): Use UpdateRoleDescription with a CLI
- [UpdateSamlProvider](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateSamlProvider_section.html): Use UpdateSamlProvider with a CLI
- [UpdateServerCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateServerCertificate_section.html): Use UpdateServerCertificate with an AWS SDK or CLI
- [UpdateSigningCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateSigningCertificate_section.html): Use UpdateSigningCertificate with a CLI
- [UpdateUser](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UpdateUser_section.html): Use UpdateUser with an AWS SDK or CLI
- [UploadServerCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UploadServerCertificate_section.html): Use UploadServerCertificate with an AWS SDK or CLI
- [UploadSigningCertificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_UploadSigningCertificate_section.html): Use UploadSigningCertificate with a CLI

### [Scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_iam_scenarios.html)

The following code examples show how to use IAM with AWS SDKs.

- [Build and manage a resilient service](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_cross_ResilientService_section.html): Build and manage a resilient service using an AWS SDK
- [Create read-only and read-write users](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_UserPolicies_section.html): Create read-only and read-write IAM users using an AWS SDK
- [Manage access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_ManageAccessKeys_section.html): Manage IAM access keys using an AWS SDK
- [Manage policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_PolicyManagement_section.html): Manage IAM policies using an AWS SDK
- [Manage roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_RoleManagement_section.html): Manage IAM roles using an AWS SDK
- [Manage your account](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_AccountManagement_section.html): Manage your IAM account using an AWS SDK
- [Permission policy allows AWS Compute Optimizer Automation to apply recommended actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.10_section.html): Allows the AWS Compute Optimizer Automation feature to apply recommended actions
- [Permission policy to enable Automation across your organization](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.2_section.html): Policy to enable Automation across your organization
- [Permission policy to enable Automation for your account](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.1_section.html): Policy to enable Automation for your account
- [Permission policy to grant full access to Compute Optimizer Automation for a management account of an organization](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section.html): Policy to grant full access to Compute Optimizer Automation for a management account of an organization
- [Permission policy to grant full access to Compute Optimizer Automation for standalone AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section.html): Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
- [Permission policy to grant read-only access to Compute Optimizer Automation for a management account of an organization](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.6_section.html): Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization
- [Permission policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.4_section.html): Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts
- [Permission policy to grant service-linked role permissions for Compute Optimization Automation](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section.html): Policy to grants service-linked role permissions for Compute Optimization Automation
- [Roll back a policy version](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_RollbackPolicyVersion_section.html): Roll back an IAM policy version using an AWS SDK
- [Set up Attribute-Based Access Control](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_dynamodb_Scenario_ABACSetup_section.html): Set up Attribute-Based Access Control for DynamoDB using AWS Command Line Interface v2
- [Work with Streams and Time-to-Live](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_dynamodb_Scenario_StreamsAndTTL_section.html): Work with DynamoDB Streams and Time-to-Live using AWS Command Line Interface v2
- [Work with the IAM Policy Builder API](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_Scenario_IamPolicyBuilder_section.html): Work with the IAM Policy Builder API using an AWS SDK

### [AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_sts.html)

Code examples that show how to use AWS STS with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_sts_basics.html)

The following code examples show how to use the basics of AWS STS with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_sts_actions.html)

The following code examples show how to use AWS STS with AWS SDKs.

- [AssumeRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_AssumeRole_section.html): Use AssumeRole with an AWS SDK or CLI
- [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_AssumeRoleWithWebIdentity_section.html): Use AssumeRoleWithWebIdentity with a CLI
- [DecodeAuthorizationMessage](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_DecodeAuthorizationMessage_section.html): Use DecodeAuthorizationMessage with a CLI
- [GetFederationToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_GetFederationToken_section.html): Use GetFederationToken with a CLI
- [GetSessionToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_GetSessionToken_section.html): Use GetSessionToken with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/service_code_examples_sts_scenarios.html)

The following code examples show how to use AWS STS with AWS SDKs.

- [Assume an IAM role that requires an MFA token](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_Scenario_AssumeRoleMfa_section.html): Assume an IAM role that requires an MFA token with AWS STS using an AWS SDK
- [Construct a URL for federated users](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_Scenario_ConstructFederatedUrl_section.html): Construct a URL with AWS STS for federated users using an AWS SDK
- [Get a session token that requires an MFA token](https://docs.aws.amazon.com/IAM/latest/UserGuide/sts_example_sts_Scenario_SessionTokenMfa_section.html): Get a session token that requires an MFA token with AWS STS using an AWS SDK


## [Security](https://docs.aws.amazon.com/IAM/latest/UserGuide/security.html)

### [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)

Use AWS security credentials (passwords, access keys) to verify who you are and whether you have permission to access the AWS resources that you are requesting.

- [Programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html): Use AWS security credentials for programmatic access to AWS resources.
- [AWS security audit guidelines](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html): Review your AWS account and IAM resources to make sure you are providing the right levels of access for your users.
- [Data protection](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Identity and Access Management (IAM) and AWS Security Token Service (AWS STS).

### [Logging and monitoring](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-logging-and-monitoring.html)

Monitor AWS Identity and Access Management (IAM) and AWS Security Token Service (AWS STS) to maintain reliability, availability, and performance.

- [Log events with CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html): Learn about logging IAM and AWS STS with AWS CloudTrail.
- [Track privileged tasks in CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html): Learn how to track privileged tasks performed by a management account or delegated administrator during a short-term privileged sessions.
- [Compliance validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/IAM/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy.
- [Infrastructure security](https://docs.aws.amazon.com/IAM/latest/UserGuide/infrastructure-security.html): Learn how AWS Identity and Access Management (IAM) and AWS Security Token Service (AWS STS) isolate service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/configuration-and-vulnerability-analysis.html): Information about how AWS handles basic security tasks like guest operating system (OS) and database patching, firewall configuration, and disaster recovery.
- [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for IAM Access Analyzer and recent changes to those policies.
- [Security features outside IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_security-outside-iam.html): Learn which AWS security features are managed outside AWS Identity and Access Management (IAM).


## [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

### [Findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html)

Learn to work with findings in IAM Access Analyzer.

- [How findings work](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html): Learn about IAM Access Analyzer concepts and terminology related to how IAM Access Analyzer monitors access to resources in your account.

### [Getting started with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)

Learn about the prerequisites and how to get started with AWS Identity and Access Management Access Analyzer findings.

- [Create an external access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-external.html): This topic provides information about creating external access analyzers.
- [Manage an external access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-manage-external.html): This topic provides information about managing external access analyzers.
- [Create an internal access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-internal.html): This topic provides information about creating internal access analyzers.
- [Manage an internal access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-manage-internal.html): This topic provides information about managing internal access analyzers.
- [Create an unused access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-unused.html): This topic provides information about creating unused access analyzers.
- [Manage an unused access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-manage-unused.html): This topic provides information about managing unused access analyzers.
- [Findings dashboard](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-dashboard.html): Learn about the IAM Access Analyzer findings dashboard and how to view summaries external access and unused access findings.
- [Review findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html): Learn how to review IAM Access Analyzer findings and determine whether access is expected or unintentional.
- [Filter findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-filter.html): Learn how to filter IAM Access Analyzer findings to display only the findings that meet specified criteria.
- [Archive findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-archive.html): Learn how to archive findings in IAM Access Analyzer.
- [Resolve findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-remediate.html): Learn how to resolve IAM Access Analyzer external, internal, and unused access findings.
- [Error findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-error-findings.html): Learn about error findings in IAM Access Analyzer and how to interpret them.
- [Supported resource types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html): Learn about the resource types supported by IAM Access Analyzer.

### [Delegated administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-delegated-administrator.html)

Learn how to add a delegated administrator for IAM Access Analyzer.

- [Add a delegated administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-delegated-administrator-add.html): Learn how to add a delegated administrator for IAM Access Analyzer.
- [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html): Learn how to create, edit, and delete archive rules in IAM Access Analyzer to automatically archive findings that match specific criteria.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-eventbridge.html): Learn about how to monitor AWS Identity and Access Management Access Analyzer with Amazon EventBridge.
- [Security Hub CSPM integration](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-securityhub-integration.html): Learn how to use the AWS Identity and Access Management Access Analyzer integration with AWS Security Hub CSPM.
- [Logging with CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/logging-using-cloudtrail.html): Learn about logging IAM Access Analyzer with AWS CloudTrail.
- [Filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html): Use filter keys to define an archive rule.
- [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-using-service-linked-roles.html): How to use service-linked roles to give AWS Identity and Access Management Access Analyzer access to resources in your AWS account.

### [Preview access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-access-preview.html)

Learn about how to preview access with IAM Access Analyzer access preview.

- [Previewing access in Amazon S3 console](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-s3-console.html): Learn about how to preview access in Amazon S3 console.
- [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html): Learn about how to preview access with IAM Access Analyzer APIs.

### [Checks for validating policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html)

This topic provides information about policy checks that help validate your IAM policies.

- [Validate with basic policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html): Learn about viewing findings generated by basic IAM Access Analyzer policy checks.
- [Policy check reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html): Learn about the messages that are returned by the policy checks and how to resolve them.
- [Validate with custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html): Learn about how to work with custom policy checks in IAM Access Analyzer.

### [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)

Refine permissions by generating a policy based on IAM user and role access activity information.

- [IAM Access Analyzer policy generation services](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation-action-last-accessed-support.html): A list of services that for which IAM Access Analyzer generates policies with action-level information.
- [IAM Access Analyzer quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-quotas.html): This topic provides information about quotas in IAM Access Analyzer.


## [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html)

- [Access denied error messages](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html): Diagnose and fix access denied error messages that you might encounter when working with AWS Identity and Access Management.
- [Root user issues](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshooting_root-user.html): Diagnose and fix issues that you might encounter when working with the root user.
- [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html): Diagnose and fix issues that you might encounter when working with IAM policies.
- [Passkeys and FIDO Security Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_mfa-fido.html): Diagnose and fix issues that you might encounter when working with FIDO2 security keys.
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html): Diagnose and fix issues that you might encounter when working with IAM roles.
- [IAM and Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_iam-ec2.html): Diagnose and fix issues that you might encounter when working with Amazon Elastic Compute Cloud and AWS Identity and Access Management.
- [IAM and Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_iam-s3.html): Diagnose and fix issues that you might encounter when working with Amazon Simple Storage Service and AWS Identity and Access Management.
- [SAML 2.0 federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml.html): Diagnose and fix issues that you might encounter when working with SAML 2.0 and federation with IAM.


## [How IAM works with other AWS services](https://docs.aws.amazon.com/IAM/latest/UserGuide/iam-cross-service.html)

- [Create IAM resources with CloudFormation](https://docs.aws.amazon.com/IAM/latest/UserGuide/creating-resources-with-cloudformation.html): Learn about how to create resources for AWS Identity and Access Management using an AWS CloudFormation template.
- [Use AWS CloudShell with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-aws-with-cloudshell.html): Learn about how you can use AWS CloudShell to work with AWS Identity and Access Management.
- [Working with AWS SDKs](https://docs.aws.amazon.com/IAM/latest/UserGuide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference.html)

- [Identify AWS resources with Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html): Learn how Amazon Resource Names (ARNs) uniquely identify AWS resources for use in IAM policies, database tags, and API calls, including their syntax, partitions, services, regions, account IDs, resource types, paths, and wildcard usage.
- [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html): Describes resource names (friendly names, identifiers, unique IDs, paths, and ARNs) for AWS Identity and Access Management (IAM) resources such as users, IAM groups, roles, policies, and certificates.
- [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html): Learn the maximum number and size quotas,name requirements, and character limits available in IAM and AWS STS.
- [Dual-stack endpoint support](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_dual-stack_endpoint_support.html): Learn about dual-stack endpoint support for IAM and AWS STS.

### [Interface VPC endpoints](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_interface_vpc_endpoints.html)

Describes the supported VPC endpoints for IAM and AWS STS.

- [Create a VPC endpoint for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam_vpc_endpoint_create.html): Learn how to create a VPC endpoint for IAM.
- [Create a VPC endpoint for AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sts_vpc_endpoint_create.html): Learn how to create a VPC endpoint for AWS STS.
- [Services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html): Learn what AWS services work with IAM and what IAM features they support.

### [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)

Learn about the AWS Signature Version 4 signing process for AWS API requests.

- [SigV4 request elements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html): Learn about the calculation elements required for AWS Signature Version 4 authentication.
- [Authentication methods](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-authentication-methods.html): Learn about the authentication methods available for signing AWS API requests.
- [Create a signed request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html): Learn how to use the AWS SigV4 signing protocol to create a signed request for AWS API requests.
- [Request signature examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-examples.html): Review descriptions and examples of SigV4 and SigV4a signatures.
- [Troubleshoot SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-troubleshooting.html): Learn how to troubleshoot common errors related to creating a signed request to access AWS.

### [Policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)

Lists detailed syntax, descriptions, and examples of the elements and condition keys in AWS Identity and Access Management (IAM) policies.

### [JSON element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)

Describes the structural elements of IAM policies.

- [Version](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html): Describes the Version element of the IAM JSON policy language.
- [Id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_id.html): Describes the Id element of the IAM JSON policy language.
- [Statement](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_statement.html): Describes the Statement element of the IAM JSON policy language.
- [Sid](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html): Describes the Sid element of the IAM JSON policy language.
- [Effect](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html): Describes the Effect element of the IAM JSON policy language.
- [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html): Describes the Principal element of the AWS JSON policy language.
- [NotPrincipal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html): Describes the NotPrincipal element of the AWS JSON policy language.
- [Action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html): Describes the Action element of the IAM JSON policy language.
- [NotAction](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html): Describes the NotAction element of the IAM JSON policy language.
- [Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html): Learn how to use the Resource element of the IAM JSON policy language.
- [NotResource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html): Describes the NotResource element of the IAM JSON policy language.

### [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)

Describes the Condition element of the IAM JSON policy language.

- [Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html): Describes the operators that you can use in the Condition element of the IAM JSON policy language.
- [Conditions with multiple context keys or values](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-logic-multiple-context-keys-or-values.html): Create conditions with multiple context keys or values to test the values in your policy condition against the matching context keys in the request.
- [Single-valued vs. multivalued context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.html): Describes the differences between single-valued and multivalued context keys.

### [Condition policy examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition_examples.html)

The following set of policy examples demonstrates policy conditions with multiple context keys and values.

- [Multivalued context key examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition_examples-multi-valued-context-keys.html): A set of policy examples that demonstrate how to create policy conditions with multivalued context keys.
- [Single-valued context key policy examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition_examples-single-valued-context-keys.html): A set of policy examples that demonstrate how to create policy conditions with single-valued context keys.
- [Variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html): Use AWS Identity and Access Management (IAM) policy variables as placeholders when you don't know the exact value of a resource or condition key when you write the policy.
- [Supported data types](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_datatypes.html): Describes the data types supported by the IAM JSON policy language.

### [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

Learn how JSON policies are evaluated within a single account to return either Allow or Deny.

- [Request context](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-reqcontext.html): When AWS evaluates and authorizes a request, it assembles the request information into a request context.

### [AWS enforcement code logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html)

The AWS enforcement code decides whether a request sent to AWS should be allowed or denied.

- [Single account policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-basics.html)
- [Cross-account policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html): Learn how JSON policies are evaluated across two accounts to return either Allow or Deny.
- [Explicit and implicit denies](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_AccessPolicyLanguage_Interplay.html): A request results in an explicit deny if an applicable policy includes a Deny statement.
- [Policy grammar](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html): Provides a grammar notation for the JSON policy language used to create policies in IAM.

### [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)

Use the special category of AWS managed policies to support common job functions.

- [Creating roles and attaching policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions_create-policies.html): Learn how to create roles and attach policies in the IAM console.
- [Global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html): Describes each of the AWS global condition keys available to use in IAM policies.
- [IAM condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html): Describes the IAM and related condition keys you can use in a policy.
- [Actions, resources, and condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html): Provides a link to all of the available actions, resources, and condition context keys that can be used in IAM policies to control access to AWS services.
