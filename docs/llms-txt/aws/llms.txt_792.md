# Source: https://docs.aws.amazon.com/singlesignon/latest/userguide/llms.txt

# AWS IAM Identity Center User Guide

> Learn how AWS IAM Identity Center can provide single sign-on services to your applications and AWS accounts

- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Integrating AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/integrating-aws-cli.html)
- [Considerations for Private Access](https://docs.aws.amazon.com/singlesignon/latest/userguide/private-access-considerations.html)
- [Quotas](https://docs.aws.amazon.com/singlesignon/latest/userguide/limits.html)
- [Document history](https://docs.aws.amazon.com/singlesignon/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/singlesignon/latest/userguide/glossary.html)

## [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html)

### [IAM Identity Center prerequisites and considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-prerequisites.html)

You can use IAM Identity Center for access to AWS managed applications only, AWS accounts only, or both.

### [Choosing an AWS Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-region-considerations.html)

Learn about AWS Region selection and how it works with IAM Identity Center.

- [IAM Identity Center Region data storage and operations](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html): Learn how IAM Identity Center handles data storage and operations across AWS Regions.
- [Switching AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/switching-regions.html): We recommend that you install IAM Identity Center in a Region that you intend to keep available for users, not a Region that you might need to disable.
- [Disabling an AWS Region where IAM Identity Center is enabled](https://docs.aws.amazon.com/singlesignon/latest/userguide/disabling-region-with-identity-center.html): If you disable an AWS Region in which IAM Identity Center is installed, IAM Identity Center is also disabled.
- [Using IAM Identity Center for applications only](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-for-apps-only.html): With IAM Identity Center, you can manage access to applications only, AWS accounts only, or both.
- [IAM roles created by IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-and-iam-roles.html): Information about how IAM roles are used with IAM Identity Center.
- [IAM Identity Center and AWS Organizations](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-and-orgs.html): Information about how AWS Organizations works with IAM Identity Center.

### [IAM Identity Center instances](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html)

Learn about organization and account instances of IAM Identity Center.

- [Organization instances of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html): Learn about the benefits of enabling an organization instance of IAM Identity Center.

### [Account instances of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/account-instances-identity-center.html)

Learn when to deploy account instances of IAM Identity Center for specialized authentication needs.

- [Permit account instance creation in member accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-account-instance-console.html): Allow member accounts in your organization to create account instances of IAM Identity Center
- [SCPs for account instance creation](https://docs.aws.amazon.com/singlesignon/latest/userguide/control-account-instance.html): Learn how to use Service Control Policies to manage account instance creation across your organization.
- [Delete your IAM Identity Center instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/delete-config.html): Learn how to permanently delete your IAM Identity Center instance and understand what data will be removed based on your configuration.


## [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html)

- [Confirm your identity sources](https://docs.aws.amazon.com/singlesignon/latest/userguide/confirm-identity-source.html): Information about how identity sources are used with IAM Identity Center.
- [Update firewalls and gateways](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center-portal-access.html): Information to help you set up your firewalls and gateway to allow your users to access the AWS access portal and sign in to AWS.


## [Identity source tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html)

- [Active Directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-ad.html): Information to help you set up to use Active Directory to manage identities for your organization.
- [CyberArk](https://docs.aws.amazon.com/singlesignon/latest/userguide/cyberark-idp.html): Learn how to set up SCIM provisioning between CyberArk and IAM Identity Center.
- [Google Workspace](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-gwp.html): Learn how to set up Google Workspace and IAM Identity Center.
- [JumpCloud](https://docs.aws.amazon.com/singlesignon/latest/userguide/jumpcloud-idp.html): Learn how to use IAM Identity Center to connect with your JumpCloud Directory Platform.
- [Microsoft Entra ID](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html): Learn how to set up a SAML connection and SCIM provisioning between Microsoft Entra ID and IAM Identity Center.
- [Okta](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-okta.html): You can automatically provision or synchronize user and group information from Okta into IAM Identity Center using the System for Cross-domain Identity Management (SCIM) 2.0 protocol.
- [OneLogin](https://docs.aws.amazon.com/singlesignon/latest/userguide/onelogin-idp.html): Learn how to set up SCIM provisioning between OneLogin and IAM Identity Center.

### [Ping Identity](https://docs.aws.amazon.com/singlesignon/latest/userguide/pingidentity.html)

The following Ping Identity products have been tested with IAM Identity Center.

- [PingFederate](https://docs.aws.amazon.com/singlesignon/latest/userguide/pingfederate-idp.html): Learn how to set up SCIM provisioning between PingFederate and IAM Identity Center.
- [PingOne](https://docs.aws.amazon.com/singlesignon/latest/userguide/pingone-idp.html): Learn how to set up SCIM provisioning between PingOne and IAM Identity Center.
- [Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html): When you enable IAM Identity Center for the first time, it is automatically configured with an Identity Center directory as your default identity source, so you do not need to choose an identity source.


## [Set up your workforce](https://docs.aws.amazon.com/singlesignon/latest/userguide/identities.html)

- [Users, groups, and provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html): IAM Identity Center enables you to control who can sign in and what resources they can access.

### [Manage your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html)

Your identity source in IAM Identity Center defines where your users and groups are managed.

- [Considerations for changing your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-considerations.html): Understand how changing your identity source affects your users, groups, and assignments.
- [Change your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-change.html): The following procedure describes how to change from a directory that IAM Identity Center provides (the default Identity Center directory) to Active Directory or an external identity provider, or the other way around.
- [User and group attributes in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-attribute-use.html): Learn about the user attributes that IAM Identity Center supports for mapping users from an external identity provider (IdP) to IAM Identity Center.

### [External identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html)

Learn how to use IAM Identity Center to connect with an external identity provider (IdP) other than a self-managed directory in Active Directory or an AWS Managed Microsoft AD.

- [Connect an external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-connect-idp.html): Learn how to connect your current identity provider to IAM Identity Center
- [Change an external identity provider's metadata](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-change-idp-metadata.html): Learn how to change the metadata for your external identity provider
- [Using SAML and SCIM identity federation](https://docs.aws.amazon.com/singlesignon/latest/userguide/other-idps.html): Learn about how other external identity providers work with IAM Identity Center.

### [SCIM profile and SAML 2.0 implementation](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html)

Learn about how IAM Identity Center works with SCIM and SAML 2.0.

### [Provision an external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html)

Learn important considerations and walk through steps to configure automatic and manual provisioning between an external identity provider and IAM Identity Center.

- [Generate an access token](https://docs.aws.amazon.com/singlesignon/latest/userguide/generate-token.html): Use the following procedure to generate a new access token in the IAM Identity Center console.
- [Enable automatic provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-with-scim.html): Use the following procedure to enable automatic provisioning of users and groups from your IdP to IAM Identity Center using the SCIM protocol.
- [Delete an access token](https://docs.aws.amazon.com/singlesignon/latest/userguide/delete-token.html): Use the following procedure to delete an existing access token in the IAM Identity Center console.
- [Disable automatic provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/disable-provisioning.html): Use the following procedure to disable automatic provisioning in the IAM Identity Center console.
- [Rotate an access token](https://docs.aws.amazon.com/singlesignon/latest/userguide/rotate-token.html): An IAM Identity Center directory supports up to two access tokens at a time.
- [Audit and reconcile auto-provisioned resources](https://docs.aws.amazon.com/singlesignon/latest/userguide/reconcile-auto-provisioning.html): Learn how to audit and reconcile users, groups, and group memberships in IAM Identity Center using AWS CLI commands.

### [Rotate SAML 2.0 certificates](https://docs.aws.amazon.com/singlesignon/latest/userguide/managesamlcerts.html)

Learn about SAML 2.0 certificates used to form a trust between an external identity provider and IAM Identity Center.

- [Rotate a SAML 2.0 certificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/rotatesamlcert.html): Learn how to rotate SAML 2.0 certificates used to form a trust between an external identity provider and IAM Identity Center.
- [Certificate expiration status indicators](https://docs.aws.amazon.com/singlesignon/latest/userguide/samlcertexpirationindicators.html): Learn about what the various status indicator icons mean for certificates in the IAM Identity Center console.

### [Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html)

Use AWS IAM Identity Center to connect a self-managed directory in Active Directory or a directory in AWS Managed Microsoft AD from AWS Directory Service.

- [Connect Active Directory and specify a user](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-connect-id-source-ad-idp-specify-user.html): If you are already using Active Directory, the following topics will help you prepare to connect your directory to IAM Identity Center.
- [Connect a directory in AWS Managed Microsoft AD to IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/connectawsad.html): Connect a directory in AWS Managed Microsoft AD to IAM Identity Center.
- [Connect a self-managed directory in Active Directory to IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/connectonpremad.html): Connect a self-managed directory in Active Directory to IAM Identity Center.

### [Attribute mappings](https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html)

Attribute mappings are used to map attribute types that exist in IAM Identity Center with like attributes in your external identity source such as Google Workspace, Microsoft Active Directory (AD), and Okta.

- [Mapping user attributes between IAM Identity Center and Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/mapssoattributestocdattributes.html): Specify how user attributes in IAM Identity Center should map to corresponding attributes in your Microsoft AD directory.

### [IAM Identity Center configurable AD sync](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-from-ad-configurable-ADsync.html)

Learn how to provision users and groups from Active Directory.

- [How configurable AD sync works](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-it-works-configurable-ADsync.html): IAM Identity Center refreshes the AD-based identity data in the identity store by using the following process.
- [Configure attribute mappings for your sync](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-configure-attribute-mapping-configurable-ADsync.html): For more information about available attributes, see .
- [First-time Active Directory to IAM Identity Center sync setup](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-configurable-ADsync.html): If you are synchronizing your users and groups from Active Directory into IAM Identity Center for the first time, follow these steps.
- [Add users and groups to your sync scope](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-add-users-groups-configurable-ADsync.html)
- [Remove users and groups from your sync scope](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-remove-users-groups-configurable-ADsync.html): For more information about what happens when you remove users and groups from your sync scope, see .
- [Pause and resume your sync](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-pause-resume-sync-configurable-ADsync.html): Pausing your sync pauses all future sync cycles and prevents any changes that you make to users and groups in Active Directory from being reflected in IAM Identity Center.
- [Automate sync configuration](https://docs.aws.amazon.com/singlesignon/latest/userguide/automate-sync-configuration-configurable-ADsync.html): To ensure that your automated workflow works as expected with configurable AD sync, we recommend that you perform the following steps to automate your sync configuration.

### [Manage users in the Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html)

IAM Identity Center provides the following capabilities for your users and groups:

- [Add users](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html): Users and groups that you create in your Identity Center directory are available in IAM Identity Center only.
- [Add groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html): Use the following procedure to add groups to your Identity Center directory.
- [Add users to groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/adduserstogroups.html): Use the following procedure to add users as members of a group that you previously created in your Identity Center directory.
- [Delete groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/deletegroups.html): When you delete a group in your IAM Identity Center directory, it removes access to AWS accounts and applications for all users who are members of this group.
- [Delete users](https://docs.aws.amazon.com/singlesignon/latest/userguide/deleteusers.html): When you delete a user in your IAM Identity Center directory, it removes their access to AWS accounts and applications.
- [Remove users from groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/removeusersfromgroups.html): Use the following procedure to remove members from a group.
- [Edit user properties](https://docs.aws.amazon.com/singlesignon/latest/userguide/edituser.html): Use the following procedure to edit the properties of a user in your Identity Center directory.


## [Workforce access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-workforce-access.html)

- [Understanding authentication sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html): When a user signs in to the AWS access portal, IAM Identity Center creates an authentication session that represents the userâs verified identity.

### [Configure session duration](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html)

You can configure the session duration for your workforce users when they use the AWS access portal and applications that work with IAM Identity Center, including Kiro.

- [User interactive sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/user-interactive-sessions.html): User interactive sessions are sessions tied to a user's sign-in to the AWS access portal or access to AWS managed applications.
- [User background sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/user-background-sessions.html): User background sessions allow a user to initiate a long-running job on an AWS managed application such as Amazon SageMaker Studio, without that user having to remain signed in while the job runs.
- [Extended sessions for Kiro](https://docs.aws.amazon.com/singlesignon/latest/userguide/90-day-extended-session-duration.html): If your developers use Kiro as part of an integrated development environment (IDE), you can set the session duration for Kiro to 90 days.
- [End active sessions for workforce users](https://docs.aws.amazon.com/singlesignon/latest/userguide/end-active-sessions.html): As an IAM Identity Center administrator, you can view the list of your workforce users' active sessions, and if required, end one or more sessions for a user.
- [Considerations for external IdPs, the AWS CLI, and AWS SDKs](https://docs.aws.amazon.com/singlesignon/latest/userguide/user-session-duration-prereqs-considerations.html): Following are considerations for configuring the session duration if you are using an external identity provider (IdP), or the AWS Command Line Interface, AWS Software Development Kits (SDKs), or other AWS development tools to access AWS services programmatically.
- [Disable user access](https://docs.aws.amazon.com/singlesignon/latest/userguide/disableuser.html): Learn how to disable an IAM Identity Center user's access to AWS access portal to prevent access to their assigned AWS accounts and applications.
- [Deny user access](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept-revoke-access.html): Deny access immediately to make authorized API calls when IAM Identity Center users are deleted or whose access has been disabled.

### [Managing access for users in the Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/managing-workforce-access-identity-center-directory.html)

If you're using the Identity Center directory, learn about password management and MFA options.

### [Setting up user passwords](https://docs.aws.amazon.com/singlesignon/latest/userguide/set-up-user-passwords.html)

For users created in the Identity Center directory, administrators can manage password policies, handle users without initial passwords, and reset passwords when needed.

- [Password requirements](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html): Understand the password requirements for AWS IAM Identity Center.
- [Email one-time password](https://docs.aws.amazon.com/singlesignon/latest/userguide/userswithoutpwd.html): Learn how to configure IAM Identity Center to allow users to authenticate when they do not have password.
- [Reset an end user password](https://docs.aws.amazon.com/singlesignon/latest/userguide/reset-password-for-user.html): Administrators can reset IAM Identity Center passwords for their IAM Identity Center end users.

### [Multi-factor authentication](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html)

Learn about MFA (multi-factor authentication) for workforce users in the Identity Center directory.

- [Available MFA types](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-types.html): Multi-factor authentication (MFA) is a simple and effective mechanism to enhance the security of your users.

### [Configure MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-configure.html)

You can configure Multi-factor authentication (MFA) capabilities in IAM Identity Center when your identity source is configured with IAM Identity Centerâs identity store, AWS Managed Microsoft AD, or AD Connector.

- [Prompt users for MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-getting-started.html): Enable and disable MFA in IAM Identity Center for enhanced security in AWS accounts
- [Choose MFA types](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-configure-mfa-types.html): Use the following procedure to choose the device types your users can authenticate with when prompted for multi-factor authentication (MFA) in the AWS access portal.
- [Configure MFA device enforcement](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-configure-mfa-device-enforcement.html): Use the following procedure to determine whether your users must have a registered MFA device when signing in to the AWS access portal.
- [Allow users to register their own MFA devices](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-allow-user-registration.html): IAM Identity Center administrators can allow users to self-register their own MFA devices.
- [Register an MFA device](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-register-device.html): IAM Identity Center administrators can set up a new MFA device for access by a specific user in the IAM Identity Center console.
- [Rename and delete MFA devices](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-manage-device.html): Learn how to manage a user's MFA device in IAM Identity Center, including steps to rename or delete an MFA device.


## [Application access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html)

### [AWS managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html)

Use IAM Identity Center to grant single sign-on access to AWS managed applications.

- [Applications that you can use with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-that-work-with-identity-center.html): Use IAM Identity Center to grant single sign-on access to AWS managed applications.
- [Setting up IAM Identity Center to test AWS managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-identity-center-quick-start.html): If your administrator hasnât already provided you with access to IAM Identity Center, you can use the steps in this topic to set up IAM Identity Center to test AWS managed applications.
- [Viewing and changing application details](https://docs.aws.amazon.com/singlesignon/latest/userguide/aws-managed-applications-view-details.html): After you connect an AWS managed application to IAM Identity Center by using the console or APIs for the application, the application is registered with IAM Identity Center.
- [Disabling an AWS managed application](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-remove.html): To prevent users from authenticating to an AWS managed application, you can disable the application in the IAM Identity Center console.
- [Enabling identity-enhanced console sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-enhanced-sessions.html): An identity-enhanced session for the console enhances a user's AWS console session by providing some additional user context to personalize that user's experience.

### [Customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html)

Use IAM Identity Center to grant single sign-on access to customer managed applications.

- [SAML 2.0 and OAuth 2.0 applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html): Understand how SAML 2.0 and OAuth 2.0 applications work with IAM Identity Center.

### [SAML 2.0 application setup](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html)

Learn how to set up a customer managed SAML 2.0 application to work with IAM Identity Center.

- [Set up an application from the catalog](https://docs.aws.amazon.com/singlesignon/latest/userguide/saasapps.html): Grant user single sign-on access to applications in the IAM Identity Center application catalog.
- [Set up your own SAML 2.0 application](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-set-up-your-own-app-saml2.html): You can set up your own applications that allow identity federation using SAML 2.0 and add them to IAM Identity Center.

### [Trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)

Learn how trusted identity propagation with IAM Identity Center enables services to grant permissions based on user attributes, add context to IAM roles, and propagate user identity across services for enhanced access control and auditing.

- [Prerequisites and considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.html): Learn about prerequisites and considerations for setting up trusted identity propagation with IAM Identity Center, including requirements for enabling and configuring IAM Identity Center and connecting applications.

### [Use cases](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-integrations.html)

Learn about trusted identity propagation use cases for AWS services and applications, including analytics and data lakehouse scenarios, like Amazon Redshift, Athena, Amazon EMR, Amazon OpenSearch Service, and Amazon Q.

### [Trusted identity propagation with Amazon Redshift](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-usecase-redshift.html)

The steps to enable trusted identity propagation depend on whether your users interact with AWS managed applications or customer managed applications.

- [Amazon Redshift Query Editor V2](https://docs.aws.amazon.com/singlesignon/latest/userguide/setting-up-tip-redshift.html): The following procedure walks you through how to achieve trusted identity propagation from Amazon Redshift Query Editor V2 to Amazon Redshift.

### [Trusted identity propagation with Amazon EMR](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-usecase-emr.html)

The following diagram shows a trusted identity propagation configuration for Amazon EMR Studio using Amazon EMR on Amazon EC2 with access control provided by AWS Lake Formation and Amazon S3 Access Grants.

- [Amazon EMR Studio](https://docs.aws.amazon.com/singlesignon/latest/userguide/setting-up-tip-emr.html): The following procedure walks you through setting up Amazon EMR Studio for trusted identity propagation in queries against an Amazon Athena workgroups or Amazon EMR clusters running Apache Spark.

### [Trusted identity propagation with Amazon Athena](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-usecase-ate.html)

The steps to enable trusted identity propagation depend on whether your users interact with AWS managed applications or customer managed applications.

- [Amazon Athena workgroups](https://docs.aws.amazon.com/singlesignon/latest/userguide/setting-up-tip-ate.html): The following procedure walks you through setting up Amazon Athena workgroups for trusted identity propagation.

### [Trusted identity propagation with Amazon SageMaker Studio](https://docs.aws.amazon.com/singlesignon/latest/userguide/trusted-identity-propagation-usecase-sagemaker-studio.html)

Amazon SageMaker Studio integrates with IAM Identity Center, and it supports user background sessions and trusted identity propagation.

- [SageMaker Studio](https://docs.aws.amazon.com/singlesignon/latest/userguide/setting-up-trusted-identity-propagation-sagemaker-studio.html): The following procedure walks you through setting up SageMaker Studio for trusted identity propagation and user background sessions.

### [Authorization services](https://docs.aws.amazon.com/singlesignon/latest/userguide/authorization-services.html)

In all analytics and data lakehouse use cases, you can achieve fine-grained access controls using:

- [AWS Lake Formation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html): AWS Lake Formation is a managed service that simplifies the creation and management of data lakes on AWS.
- [Amazon S3 Access Grants](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html): Amazon S3 Access Grants provides the flexibility to grant identity-based fine-grain access control to S3 locations.

### [Setting up your own OAuth 2.0 application](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-setup.html)

Trusted identity propagation enables a customer managed application to request access to data in AWS services on behalf of a user.

- [Set up customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.html): To set up a customer managed OAuth 2.0 application for trusted identity propagation, you must first add it to IAM Identity Center.
- [Specify trusted applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.html): After you set up your customer managed application, you must specify one or more trusted AWS services, or trusted applications, for identity propagation.

### [Trusted token issuer](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html)

Trusted token issuers enable you to use trusted identity propagation with applications that authenticate outside of AWS.

- [Trusted token issuer configuration settings](https://docs.aws.amazon.com/singlesignon/latest/userguide/trusted-token-issuer-configuration-settings.html): The following sections describe the settings required to set up and use a trusted token issuer.
- [Setting up a trusted token issuer](https://docs.aws.amazon.com/singlesignon/latest/userguide/setuptrustedtokenissuer.html): To enable trusted identity propagation for an application that authenticates externally to IAM Identity Center, one or more administrators must set up a trusted token issuer.
- [Identity-enhanced IAM role sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.html): The AWS Security Token Service (STS) enables an application to obtain an identity-enhanced IAM role session.

### [Rotate certificates](https://docs.aws.amazon.com/singlesignon/latest/userguide/managecerts.html)

IAM Identity Center uses certificates to set up a SAML trust relationship between IAM Identity Center and your application's service provider.

- [Rotate an IAM Identity Center certificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/rotatecert.html): Rotating an IAM Identity Center certificate is a multistep process that involves the following:
- [Certificate expiration status indicators](https://docs.aws.amazon.com/singlesignon/latest/userguide/certexpirationindicators.html): In the IAM Identity Center console, the Applications page displays status indicator icons in the properties of each application.
- [Understand application properties](https://docs.aws.amazon.com/singlesignon/latest/userguide/appproperties.html): Configure the application start URL, relay state, and session duration in IAM Identity Center to optimize your users' experience.
- [Assign user access to applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/assignuserstoapp.html): Assign users single sign-on access to SAML 2.0 applications in the application catalog and custom SAML 2.0 applications.
- [Remove user access to applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/removeaccessfromapp.html): Remove IAM Identity Center user access to SAML 2.0 applications in the application catalog or custom SAML 2.0 applications.
- [Map attributes](https://docs.aws.amazon.com/singlesignon/latest/userguide/mapawsssoattributestoapp.html): Some service providers require custom SAML assertions to pass additional data about your user sign-ins.


## [AWS account access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html)

### [Delegated administration](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html)

Delegated administration provides a convenient way for assigned users in a registered member account to perform most IAM Identity Center administrative tasks.

- [Register a member account](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin-how-to-register.html): To configure delegated administration, you must first register a member account in your organization as a delegated administrator.
- [Deregister a member account](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin-how-to-deregister.html): You can only deregister a member account while signed in with credentials from the management account.
- [View delegated administrator accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin-how-to-view-member-account.html): Use the following procedure to find which member account in your AWS Organizations has been configured as the delegated administrator for IAM Identity Center.
- [Temporary elevated access](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html): set Guidelines for implementing temporary elevated access in IAM Identity Center.

### [Single sign-on access to AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html)

Use AWS IAM Identity Center to set up single sign-on access to one or more AWS accounts in your AWS organization.

- [Assign user or group access to AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/assignusers.html): Use the following procedure to assign single sign-on access to users and groups in your connected directory and use permission sets to determine their level of access.
- [Remove user and group access to an AWS account](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoremoveaccess.html): Use this procedure to remove single sign-on access to an AWS account for one or more users and groups in your connected directory.
- [Revoke an active permission set session](https://docs.aws.amazon.com/singlesignon/latest/userguide/revoke-user-permissions.html): General procedure for revoking an active IAM Identity Center permission set session.
- [Delegate who can assign single sign-on access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtodelegatessoaccess.html): Assigning single sign-on access to the management account using the IAM Identity Center console is a privileged action.

### [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html)

Learn how permissions sets are used to assign AWS account access through templates of IAM policies to users and groups.

- [Predefined permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetpredefined.html): You can create a predefined permission set with AWS managed policies.
- [Custom permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetcustom.html): You can create a permission set with Custom permissions, combining any of the AWS managed and customer managed policies that you have in AWS Identity and Access Management (IAM) along with inline policies.

### [Create, manage, and delete permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsets.html)

Use IAM Identity Center to create, manage, and delete permission sets that define the level of access for users and groups.

- [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html): Use IAM Identity Center to create a permission set that defines the level of access for users and groups.
- [View and change a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoviewandchangepermissionset.html): Use AWS IAM Identity Center console to view and change a permission set for IAM Identity Center users and groups.
- [Delegate permission set administration](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetdelegation.html): IAM Identity Center enables you to delegate management of permission sets and assignments in accounts by creating IAM policies that reference the Amazon Resource Names (ARNs) of IAM Identity Center resources.
- [Use IAM policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocmp.html): In , you learned how to add policies, including customer managed policies and permissions boundaries, to a permission set.
- [Remove permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoremovepermissionset.html): You can remove a permission set from IAM Identity Center users and groups in the IAM Identity Center console.
- [Delete permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtodeletepermissionset.html): Before you can delete a permission set from IAM Identity Center, you should remove it from all AWS accounts that use the permission set.

### [Configure permission set properties](https://docs.aws.amazon.com/singlesignon/latest/userguide/permproperties.html)

In IAM Identity Center, administrators can complete the following configuration and management tasks to control user access and session duration.

- [Set session duration for AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html): For each permission set, you can specify a session duration to control the length of time that a user can be signed in to an AWS account.
- [Set relay state](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtopermrelaystate.html): Learn how to set and manage the relay state in IAM Identity Center to direct users to specific Amazon Web Services after login.
- [Use a Deny policy to revoke active user permissions](https://docs.aws.amazon.com/singlesignon/latest/userguide/prereqs-revoking-user-permissions.html): You might need to revoke an IAM Identity Center userâs access to AWS accounts while the user is actively using a permission set.
- [Referencing permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/referencingpermissionsets.html): When you assign a permission set to an AWS account, IAM Identity Center creates a role with a name that begins with AWSReservedSSO_.

### [Attribute-based access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/abac.html)

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes.

- [Checklist: Configuring ABAC in AWS using IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html): This checklist includes the configuration tasks that are necessary to prepare your AWS resources and to set up IAM Identity Center for ABAC access.

### [Attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/attributesforaccesscontrol.html)

Attributes for access control is the name of the page in the IAM Identity Center console where you select user attributes that you want to use in policies to control access to resources.

### [Enable and configure attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac.html)

To use attribute-based access control (ABAC), you must first enable it in either the Settings page of the IAM Identity Center console or the IAM Identity Center API.

- [Enable attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-abac.html): Use the following procedure to enable the attributes for access (ABAC) control feature using the IAM Identity Center console.
- [Select your attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac-attributes.html): Use the following procedure to set up attributes for your ABAC configuration.
- [Disable attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/disable-abac.html): Use the following procedure to disable the ABAC feature and delete all of the attribute mappings that have been configured.
- [Create permission policies for ABAC](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac-policies.html): You can create permissions policies that determine who can access your AWS resources based on the configured attribute value.
- [Service-linked roles](https://docs.aws.amazon.com/singlesignon/latest/userguide/slrconcept.html): Service-linked roles are predefined IAM permissions that allow IAM Identity Center to delegate and enforce which users have single sign-on access to specific AWS accounts in your organization in AWS Organizations.


## [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html)

### [Configure the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-the-access-portal.html)

Configure the AWS access portal by activating user access and customizing the portal URL for your organization.

- [Activating the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoactivateaccount.html): If this is your first time attempting to sign in to the AWS access portal, check your email for instructions on how to activate your user credentials.
- [Customizing the AWS access portal URL](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtochangeURL.html): By default, you can access the AWS access portal by using a URL that follows this format: d-xxxxxxxxxx.awsapps.com/start.
- [Confirm users can sign in to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosigninprocedure.html): The following steps are for IAM Identity Center administrator to confirm that the IAM Identity Center user can sign in to the AWS access portal and access the AWS account.

### [Use the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/access-portal-for-workforce-users.html)

You can launch multiple applications by choosing the AWS account or application tab in the portal.

- [Signing in to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosignin.html): The AWS access portal provides IAM Identity Center users with single sign-on access to all their assigned AWS accounts and applications through a web portal.
- [Resetting your user password](https://docs.aws.amazon.com/singlesignon/latest/userguide/resetpassword-accessportal.html): Whether youâve forgotten your AWS access portal password or suspect unauthorized access, this topic describes how to reset your AWS access portal password so you can regain access securely.
- [AWS CLI and AWS SDK access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html): You can access AWS services programmatically by using the AWS Command Line Interface or AWS Software Development Kits (SDKs) with user credentials from IAM Identity Center.
- [Creating shortcut links](https://docs.aws.amazon.com/singlesignon/latest/userguide/createshortcutlink.html): Learn how to create shortcut links that take IAM Identity Center users to destinations in the AWS Management Console.
- [Registering your device for MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/user-device-registration.html): Learn how as an end user to register your devices to enable multi-factor authentication (MFA) to access AWS resources.
- [Ending your active session](https://docs.aws.amazon.com/singlesignon/latest/userguide/end-user-how-to-end-active-sessions-accessportal.html): You can use your AWS access portal to view the list of your active sessions, and if required, end one or more sessions.


## [Using IAM Identity Center across multiple AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html)

- [Replicate IAM Identity Center to an additional Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/replicate-to-additional-region.html): If your environment meets the prerequisites, follow the steps below to replicate your IAM Identity Center instance to an additional Region:
- [Workforce access through an additional Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-workforce-access.html): This section explains how your workforce can access the AWS access portal, AWS accounts, and applications when you have enabled IAM Identity Center in multiple Regions.
- [Failover to an additional Region for AWS account access](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-failover.html): The topic of AWS account access through IAM Identity Center is covered extensively in .
- [Deploying and managing applications across multiple AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-application-use.html): The topic of application access through IAM Identity Center is covered extensively in .
- [Remove a Region from IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/remove-region.html): To remove an additional Region from your IAM Identity Center instance, follow these steps:
- [Service APIs supported in additional AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/api-support-in-additional-regions.html)
- [CloudTrail events in the primary and additional Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/cloudtrail-events.html): In AWS CloudTrail, you can audit actions that IAM Identity Center users and administrators take across all enabled AWS Regions of your IAM Identity Center instance.
- [IAM Identity Center use cases in the primary and additional Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/use-cases-across-regions.html)


## [Resiliency design and Regional behavior](https://docs.aws.amazon.com/singlesignon/latest/userguide/resiliency-regional-behavior.html)

### [Set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html)

IAM Identity Center is built from highly available AWS infrastructure and uses an Availability Zone architecture to eliminate single points of failure.

- [Summary of emergency access configuration](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-implementation.html): To configure emergency access, you must complete the following tasks:
- [How to d esign your critical operations roles](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-implementation-design.html): With this design, you configure a single AWS account in which you federate through IAM, so that users can assume critical operations roles.
- [How to plan your access model](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-planning.html): Before you configure emergency access, create a plan for how the access model will work.
- [How to design e mergency role, account, and group mapping](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-mapping-design.html): The following diagram shows how to map your emergency access groups to roles in your emergency access account.
- [How to create your emergency access configuration](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-role-idp-group-creation-mapping-plan.html): Use the following mapping table to create your emergency access configuration.
- [Emergency preparation tasks](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-prepare-configuration.html): To prepare your emergency access configuration, we recommend that you perform the following tasks before an emergency occurs.
- [Emergency failover process](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-failover-steps.html): When an IAM Identity Center instance isn't available and you determine that you must provide emergency access to the AWS Management Console, we recommend the following failover process.
- [Return to normal operations](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-return-to-normal-operations.html): Check the AWS Health Dashboard to confirm when the health of the IAM Identity Center service is restored.
- [One-time setup of a direct IAM federation application in Okta](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.html)


## [Security](https://docs.aws.amazon.com/singlesignon/latest/userguide/security.html)

### [Identity and access management for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html)

Create permissions that specify which actions a user or group in your AWS account can perform and on which IAM Identity Center resources.

- [Overview of managing access](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-overview.html): Learn the basic concepts of managing access permissions to AWS IAM Identity Center resources.
- [Identity-based policy examples](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html): Find examples of permissions for AWS IAM Identity Center that you can grant to AWS identities.
- [Resource-based policy example](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-resource-based-policies.html): Every application that works with IAM Identity Center and uses OAuth 2.0 requires a resource-based policy.
- [AWS managed policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for IAM Identity Center and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-service-linked-roles.html): Learn how the service-linked role for IAM Identity Center is used to access resources in your AWS account.
- [IAM Identity Center console and API authorization](https://docs.aws.amazon.com/singlesignon/latest/userguide/security-authorization.html): Review information about console and API authorization in IAM Identity Center.
- [AWS STS condition keys for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/condition-context-keys-sts-idc.html): When a principal makes a request to AWS, AWS gathers the request information into a request context, which is used to evaluate and authorize the request.

### [Logging and monitoring](https://docs.aws.amazon.com/singlesignon/latest/userguide/security-logging-and-monitoring.html)

Monitor your AWS IAM Identity Center by using AWS CloudTrail and Amazon CloudWatch Events.

### [Logging IAM Identity Center API calls with AWS CloudTrail](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-using-cloudtrail.html)

Learn about integrating IAM Identity Center with AWS CloudTrail.

- [CloudTrail use cases for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/sso-cloudtrail-use-cases.html): The CloudTrail events that IAM Identity Center emits can be valuable for a variety of use cases.

### [IAM Identity Center information in CloudTrail](https://docs.aws.amazon.com/singlesignon/latest/userguide/sso-info-in-cloudtrail.html)

CloudTrail is enabled on your AWS account when you create the account.

- [CloudTrail events for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/understanding-sso-entries.html): A trail is a configuration that enables delivery of events to an Amazon S3 bucket that you specify.

### [IAM Identity Center sign-in events](https://docs.aws.amazon.com/singlesignon/latest/userguide/understanding-sign-in-events.html)

AWS CloudTrail records successful and unsuccessful sign-in events for all IAM Identity Center identity sources.

- [Username in sign-in CloudTrail events](https://docs.aws.amazon.com/singlesignon/latest/userguide/username-sign-in-cloudtrail-events.html): IAM Identity Center emits the UserName field under the additionalEventData element once per successful sign-in of an IAM Identity Center user.
- [Example events for IAM Identity Center sign-in](https://docs.aws.amazon.com/singlesignon/latest/userguide/sign-in-events-examples.html): The following examples illustrate the typical CloudTrail event sequences generated during various AWS sign-in scenarios.
- [Logging IAM Identity Center SCIM with AWS CloudTrail](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-logging-using-cloudtrail.html): Learn about integrating IAM Identity Center SCIM API calls with AWS CloudTrail.
- [Amazon EventBridge](https://docs.aws.amazon.com/singlesignon/latest/userguide/eventbridge-integration.html): You can integrate IAM Identity Center with Amazon EventBridge to raise events that initiate administrative notifications or invoke automated workflows in response to specific IAM Identity Center actions recorded in CloudTrail events.
- [Logging configurable AD sync errors](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-ad-sync-errors.html): You can enable logging on your configurable Active Directory (AD) sync configurations to receive logs with information about errors that can occur during the sync process.
- [Compliance validation](https://docs.aws.amazon.com/singlesignon/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/singlesignon/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and learn about specific AWS IAM Identity Center features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/singlesignon/latest/userguide/infrastructure-security.html): Learn how AWS IAM Identity Center isolates service traffic.


## [Data protection](https://docs.aws.amazon.com/singlesignon/latest/userguide/data-protection.html)

### [Encryption at rest](https://docs.aws.amazon.com/singlesignon/latest/userguide/encryption-at-rest.html)

IAM Identity Center provides encryption to protect customer data at rest

- [Implementing customer managed KMS keys](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-customer-managed-keys.html): Learn how to implement customer managed KMS keys for encryption at rest in AWS IAM Identity Center.
- [Baseline KMS key and IAM policy statements](https://docs.aws.amazon.com/singlesignon/latest/userguide/baseline-KMS-key-policy.html): The baseline KMS key and identity-based policies provided here serve as a foundation for common requirements.

### [Advanced KMS key policy statements](https://docs.aws.amazon.com/singlesignon/latest/userguide/advanced-kms-policy.html)

Use advanced KMS key policy statements to implement more granular access controls for your customer managed KMS key.

- [Considerations for customer managed KMS keys and advanced KMS key policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/considerations-for-customer-managed-kms-keys-advanced.html): When implementing customer managed KMS keys with IAM Identity Center, consider these factors that affect setup, security, and ongoing maintenance of your encryption configuration.


## [Tagging resources](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging.html)

- [Manage tags with the console](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-console.html): You can use the IAM Identity Center console to add, edit, and remove tags that are associated with your instance or permission sets.
- [AWS CLI examples](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-cli-examples.html): The AWS CLI provides commands that you can use to manage the tags that you assign to your permission set.
- [API actions](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-api.html): Use the following API actions to assign, view, and remove tags for a permission set or instance of IAM Identity Center.


## [Troubleshooting](https://docs.aws.amazon.com/singlesignon/latest/userguide/troubleshooting.html)

- [Troubleshoot customer managed keys in AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/cmk-related-errors.html): This topic describes common customer managed key related errors you might encounter when using AWS IAM Identity Center and provides troubleshooting steps to resolve them.
- [Troubleshoot multi-Region setup in AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-related-errors.html): This topic describes common multi-Region setup related errors you might encounter when using AWS IAM Identity Center and provides troubleshooting steps to resolve them.
