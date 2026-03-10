# Source: https://docs.aws.amazon.com/cognito/latest/developerguide/llms.txt

# Amazon Cognito Developer Guide

> Amazon Cognito is a service that you can use to sign in users, federate with identity providers, control permissions to access your backend resources, and save mobile user data in the AWS Cloud. This guide provides an overview of Amazon Cognito and includes development instructions for its features.

- [Additional getting started options](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-guided-setup.html)
- [Common Amazon Cognito scenarios](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-scenarios.html)
- [Troubleshooting](https://docs.aws.amazon.com/cognito/latest/developerguide/troubleshooting.html)
- [Tagging resources](https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/cognito/latest/developerguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-document-history.html)

## [What is Amazon Cognito?](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)

- [Terms and concepts](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-terms.html): Understand how this guide uses some commonly-understood terms, and the terminology specific to Amazon Cognito user pools and identity pools.
- [Getting started with AWS](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-getting-started-account-iam.html): Set up and AWS account and sign in with new administrative credentials.


## [Getting started with user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools.html)

- [Your first app and user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools-application.html): Use the Amazon Cognito console to create a user pool and get example code that you can implement in an application
- [Other application options](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools-application-other-options.html): Learn about SDK authentication with Amazon Cognito user pools.

### [Next steps](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-next-steps.html)

Build a new user pool in the Amazon Cognito console.

- [Add a social provider](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool-social-idp.html): Set up user sign-in to your application through existing social media accounts.
- [Add a SAML IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool-saml-idp.html): As part of the getting started with user pools experience, add a SAML 2.0 IdP to manage sign-in for users who have credentials with a private user directory like Active Directory or Okta.


## [Getting started with identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html)

- [Example application](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-identity-pools-application.html): Use the Amazon Cognito identity pools example application to explore different authentication methods and understand how identity pools work with various identity providers to provide temporary AWS credentials to your application users.


## [Integrating with apps](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html)

- [How authentication works](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-how-to-authenticate.html): Describes how Amazon Cognito signs in consumer and enterprise users with API operations, managed login, and third-party identity providers.
- [Working with AWS SDKs](https://docs.aws.amazon.com/cognito/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Authorization with Amazon Verified Permissions](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-authorization-with-avp.html): Learn how to integrate Amazon Verified Permissions with your app to authorize requests with universal attribute-based access control.


## [Code examples](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples.html)

### [Amazon Cognito Identity](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity.html)

Code examples that show how to use Amazon Cognito Identity with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity_basics.html)

The following code examples show how to use the basics of Amazon Cognito Identity with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity_actions.html)

The following code examples show how to use Amazon Cognito Identity with AWS SDKs.

- [CreateIdentityPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_CreateIdentityPool_section.html): Use CreateIdentityPool with an AWS SDK or CLI
- [DeleteIdentityPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_DeleteIdentityPool_section.html): Use DeleteIdentityPool with an AWS SDK or CLI
- [DescribeIdentityPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_DescribeIdentityPool_section.html): Use DescribeIdentityPool with a CLI
- [GetCredentialsForIdentity](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_GetCredentialsForIdentity_section.html): Use GetCredentialsForIdentity with an AWS SDK
- [GetIdentityPoolRoles](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_GetIdentityPoolRoles_section.html): Use GetIdentityPoolRoles with a CLI
- [ListIdentityPools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_ListIdentityPools_section.html): Use ListIdentityPools with an AWS SDK or CLI
- [SetIdentityPoolRoles](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_SetIdentityPoolRoles_section.html): Use SetIdentityPoolRoles with a CLI
- [UpdateIdentityPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cognito-identity_UpdateIdentityPool_section.html): Use UpdateIdentityPool with a CLI

### [Scenarios](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity_scenarios.html)

The following code examples show how to use Amazon Cognito Identity with AWS SDKs.

- [Create an Amazon Textract explorer application](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity_example_cross_TextractExplorer_section.html): Create an Amazon Textract explorer application

### [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider.html)

Code examples that show how to use Amazon Cognito Identity Provider with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider_basics.html)

The following code examples show how to use the basics of Amazon Cognito Identity Provider with AWS SDKs.

- [Hello Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_Hello_section.html): Hello Amazon Cognito

### [Actions](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider_actions.html)

The following code examples show how to use Amazon Cognito Identity Provider with AWS SDKs.

- [AdminCreateUser](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AdminCreateUser_section.html): Use AdminCreateUser with an AWS SDK or CLI
- [AdminGetUser](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AdminGetUser_section.html): Use AdminGetUser with an AWS SDK or CLI
- [AdminInitiateAuth](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AdminInitiateAuth_section.html): Use AdminInitiateAuth with an AWS SDK or CLI
- [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AdminRespondToAuthChallenge_section.html): Use AdminRespondToAuthChallenge with an AWS SDK or CLI
- [AdminSetUserPassword](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AdminSetUserPassword_section.html): Use AdminSetUserPassword with an AWS SDK or CLI
- [AssociateSoftwareToken](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_AssociateSoftwareToken_section.html): Use AssociateSoftwareToken with an AWS SDK or CLI
- [ConfirmDevice](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ConfirmDevice_section.html): Use ConfirmDevice with an AWS SDK or CLI
- [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ConfirmForgotPassword_section.html): Use ConfirmForgotPassword with an AWS SDK or CLI
- [ConfirmSignUp](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ConfirmSignUp_section.html): Use ConfirmSignUp with an AWS SDK or CLI
- [CreateUserPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_CreateUserPool_section.html): Use CreateUserPool with an AWS SDK or CLI
- [CreateUserPoolClient](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_CreateUserPoolClient_section.html): Use CreateUserPoolClient with an AWS SDK or CLI
- [DeleteUser](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_DeleteUser_section.html): Use DeleteUser with an AWS SDK or CLI
- [ForgotPassword](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section.html): Use ForgotPassword with an AWS SDK or CLI
- [InitiateAuth](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_InitiateAuth_section.html): Use InitiateAuth with an AWS SDK or CLI
- [ListUserPools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ListUserPools_section.html): Use ListUserPools with an AWS SDK or CLI
- [ListUsers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ListUsers_section.html): Use ListUsers with an AWS SDK or CLI
- [ResendConfirmationCode](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_ResendConfirmationCode_section.html): Use ResendConfirmationCode with an AWS SDK or CLI
- [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_RespondToAuthChallenge_section.html): Use RespondToAuthChallenge with an AWS SDK or CLI
- [SignUp](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_SignUp_section.html): Use SignUp with an AWS SDK or CLI
- [UpdateUserPool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_UpdateUserPool_section.html): Use UpdateUserPool with an AWS SDK or CLI
- [VerifySoftwareToken](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_VerifySoftwareToken_section.html): Use VerifySoftwareToken with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider_scenarios.html)

The following code examples show how to use Amazon Cognito Identity Provider with AWS SDKs.

- [Automatically confirm known users with a Lambda function](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.html): Automatically confirm known Amazon Cognito users with a Lambda function using an AWS SDK
- [Automatically migrate known users with a Lambda function](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.html): Automatically migrate known Amazon Cognito users with a Lambda function using an AWS SDK
- [Sign up a user with a user pool that requires MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cognito-identity-provider_Scenario_SignUpUserWithMfa_section.html): Sign up a user with an Amazon Cognito user pool that requires MFA using an AWS SDK
- [Use Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cross_CognitoFlows_section.html): Use Amazon Cognito identity pools and authentication flows
- [Write custom activity data with a Lambda function after Amazon Cognito user authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.html): Write custom activity data with a Lambda function after Amazon Cognito user authentication using an AWS SDK

### [Amazon Cognito Sync](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-sync.html)

Code examples that show how to use Amazon Cognito Sync with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-sync_basics.html)

The following code examples show how to use the basics of Amazon Cognito Sync with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-sync_actions.html)

The following code examples show how to use Amazon Cognito Sync with AWS SDKs.

- [ListIdentityPoolUsage](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync_example_cognito-sync_ListIdentityPoolUsage_section.html): Use ListIdentityPoolUsage with an AWS SDK


## [Multi-tenancy best practices](https://docs.aws.amazon.com/cognito/latest/developerguide/multi-tenant-application-best-practices.html)

- [Per-tenant user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/bp_user-pool-based-multi-tenancy.html): Learn the advantages and disadvantages of granting a separate user pool to each customer in a multi-tenancy user pool setup.
- [Per-tenant app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/application-client-based-multi-tenancy.html): Learn the advantages and disadvantages of granting a separate app client to each customer in a multi-tenancy user pool setup.
- [Per-tenant user pool groups](https://docs.aws.amazon.com/cognito/latest/developerguide/group-based-multi-tenancy.html): Learn the advantages and disadvantages of distinguishing tenants with user pool groups in a multi-tenancy user pool setup.
- [Per-tenant custom attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/custom-attribute-based-multi-tenancy.html): Learn the advantages and disadvantages of distinguishing tenants with custom attributes in a multi-tenancy user pool setup.
- [Per-tenant custom scopes](https://docs.aws.amazon.com/cognito/latest/developerguide/scope-based-multi-tenancy.html): Learn the advantages and disadvantages of distinguishing tenants with custom scopes in a multi-tenancy user pool setup.
- [Multi-tenancy security recommendations](https://docs.aws.amazon.com/cognito/latest/developerguide/multi-tenancy-security-recommendations.html): To help make your application more secure, we recommend the following:


## [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

### [User pool feature plans](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html)

Amazon Cognito user pools has tiers of features that have different per-user costs.

- [Essentials plan features](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html): Learn about the features that are added to your user pool when you choose the Essentials feature plan
- [Plus plan features](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html): Learn about the security features that are added to your user pool when you choose the Plus feature plan
- [Turn off ineligible features](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-deactivate.html): To switch between some feature plans in an Amazon Cognito user pool, you must deactivate features that aren't available in the new feature plan.
- [Security best practices](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-security-best-practices.html): Implement security best practices in Amazon Cognito user pools to protect your applications

### [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)

Amazon Cognito has several authentication methods, including client-side, server-side, and custom flows.

- [Managed login authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-managedlogin.html): To achieve authentication for your application with Amazon Cognito user pools, the lowest-effort approach is managed login and an OpenID Connect relying-party library.
- [SDK authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html): When you implement Amazon Cognito application authentication in the back end with an AWS SDK, you can select one of two typer of initial sign-in flows.
- [Authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html): Learn details about the mechanisms that you can set up in Amazon Cognito user pools for user sign-in.
- [SDK authorization models](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html): Amazon Cognito has an API back end model for authentication.

### [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html)

Adding user pool sign-in through a third party.

- [Identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-provider.html): Add built-in identity provider integrations to your user pool.
- [Social identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-social-idp.html): Adding social identity providers to a user pool.

### [SAML providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html)

Adding SAML identity providers to a user pool.

- [Things to know](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp-things-to-know.html): A list of miscellaneous information that you need to know to set up and troubleshoot SAML federation in an Amazon Cognito user pool.
- [Provider application configuration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-integrating-3rd-party-saml-providers.html): Learn how to set up a third-party identity provider for SAML 2.0 with Amazon Cognito user pools.
- [Add a SAML provider](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp.html): A guide to AWS Management Console and Amazon Cognito user pools API configuration of a user pool to add an external SAML IdP.
- [SP- and IdP-initiated sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-SAML-session-initiation.html): Amazon Cognito supports SP-initiated and IdP-initiate sign-in with user pools.
- [Single sign-out with SAML](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp-sign-out.html): User pools can send a single logout (SLO) request when users want to sign out of your application.
- [Signing and encryption](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-SAML-signing-encryption.html): You can sign SAML requests and require encrypted SAML assertions in Amazon Cognito user pools.
- [SAML names and identifiers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp-naming.html): How to configure user pool identity provider names and identifiers to redirect users from the authorize endpoint.

### [OIDC providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html)

Learn how to configure an OpenID Connect (OIDC) identity provider like Salesforce or Okta to allow users to sign in to your application using their existing accounts from those providers.

- [OIDC user pool IdP authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-flow.html): OIDC user pool IdP authentication flow.
- [Mapping IdP attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html): Map the attribute schema from your identity providers to your user pool.
- [Linking federated users](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html): Learn how to connect user identities from third-party IdPs to local user profiles in your user pool.

### [Managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html)

Integrating a mobile or web app into your Amazon Cognito user pool.

### [Configuring a domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)

Configure a domain for a user pool.

- [Add a prefix domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain-prefix.html): Learn about the AWS-owned domain with a personal prefix that you can use to serve the hosted UI and managed login.
- [Using your own domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html): Configure a user pool custom domain for managed login.

### [Branding and customization](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-branding.html)

Customizing the built-in sign-in and sign-up webpages for your user pool.

- [Managed login branding](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-brandingeditor.html): Configure managed login style, images, background, and logos with the branding editor.
- [Hosted UI (classic) branding](https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html): Configure hosted UI CSS and logo with the classic experience.

### [Using Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html)

Customize Amazon Cognito user pool workflows with AWS Lambda triggers.

- [Pre sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html): Confirm and verify users and modify sign-up requests with a pre sign-up Lambda trigger.
- [Post confirmation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html): The post confirmation Lambda trigger runs custom logic after Amazon Cognito user pools users confirm their attributes or accounts.
- [Pre authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html): Pre authentication Lambda trigger.
- [Post authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html): Post authentication Lambda trigger.
- [Inbound federation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-inbound-federation.html): Transform federated user attributes during authentication with external identity providers using an inbound federation Lambda trigger.

### [Custom challenge](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html)

Challenge Lambda triggers.

- [Define auth challenge](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-define-auth-challenge.html): To initiate the custom authentication flow, Amazon Cognito uses the Define Auth Challenge Lambda trigger .
- [Create auth challenge](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-create-auth-challenge.html): Create auth challenge Lambda trigger.
- [Verify auth challenge response Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-verify-auth-challenge-response.html): Verify auth challenge response Lambda trigger.
- [Pre token generation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html): Customize user pool JWT tokens with the pre token generation Lambda trigger.
- [Migrate user](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html): Migrate user Lambda trigger.
- [Custom message](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html): Custom message Lambda trigger.

### [Custom senders](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-sender-triggers.html)

Learn how to handle codes and send messages with your own message-delivery service in custom Sender Lambda triggers.

- [Custom email sender](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-email-sender.html): Custom email sender Lambda trigger.
- [Custom SMS sender](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-sms-sender.html): Customize your SMS sender Lambda trigger.

### [Managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html)

Learn about options for user sign-up, account creation, and user migration.

- [Allowing user sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-admin-create-user-policy.html): Learn about configuration options for controlling the user sign-up and account creation process in a user pool.

### [Signing up and confirming user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)

Sign up and confirm user accounts in Amazon Cognito.

- [Email or phone verification](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html): Email or phone verification.
- [Customize message templates](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html): Configure and manage SMS and email verification and user invitation messages.
- [Creating users as administrator](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-create-user-accounts.html): Create user accounts in the Amazon Cognito console or with the User Pools API.
- [Adding groups to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html): Create user groups in the Amazon Cognito console or with the User Pools API or CLI.
- [Managing and searching for users](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html): Manage and search for user accounts in Amazon Cognito user pools.
- [Passwords](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html): Learn about user pool passwords, how to configure your user pool for account recovery, and how to assist users with password reset.

### [Importing users into a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-import-users.html)

Import your existing users into a user pool.

- [User migration trigger import](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-import-using-lambda.html): Import your existing users into a user pool with a user migration AWS Lambda trigger.
- [Importing users from a CSV file](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html): Import your existing users into a user pool from a CSV file.
- [Attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html): With Amazon Cognito, you can associate standard and custom attributes with user accounts in your user pool.

### [User pool tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html)

Learn about user pool token formats and usage.

- [ID tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.html): Using the ID Token
- [Access tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html): The user pool access token is an OIDC access-control mechanism that grants access to user pool and external APIs with scopes.
- [Refresh tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html): Refresh tokens are encrypted user pool tokens that signal a request to Amazon Cognito for new ID and access tokens.
- [Revoking tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html): You can revoke refresh tokens when you want to end a user's session.
- [Verifying a JSON Web Token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html): Verify a user pool JSON Web Token in three steps.
- [Caching tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.html): An overview of token request rate limits and an example caching solution with Amazon API Gateway.

### [Accessing resources after sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/accessing-resources.html)

Use tokens from user pools to pass user information to relying party applications and authorize access to other resources.

- [Accessing resources with Verified Permissions](https://docs.aws.amazon.com/cognito/latest/developerguide/scenario-backend.html): Pass ID or access tokens to Amazon Verified Permissions and authorize access to applications and API back ends.
- [Accessing API Gateway resources](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-accessing-resources-api-gateway-and-lambda.html): Authorize API access with user pool access tokens.
- [Accessing AWS resources using an identity pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-integrating-user-pools-with-identity-pools.html): Pass user pool ID tokens to identity pools to authorize access to AWS services
- [M2M and scopes](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html): Authorize access to user attributes and configure resource servers for API access with Amazon Cognito user pools.

### [Additional features](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-configure-features.html)

Configure miscellaneous features in a user pool.

- [Updating a user pool and app client](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-updating.html): Learn about how to construct API requests to update app clients and user pools.
- [App clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html): User pool app clients are a group of settings for one application.
- [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html): Learn how to set up remembered devices for users who want to bypass MFA in custom-build applications
- [Using Amazon Pinpoint analytics](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html): Configure your Amazon Cognito user pool app client to submit analytics data to an Amazon Pinpoint project.
- [Email settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-email.html): Learn about the difference between default and developer email configuration in user pools.
- [SMS message settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html): Send SMS messages from you Amazon Cognito user pools for sign-in, MFA, and account confirmation.

### [Using security features](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-security.html)

Managing security for user pools.

### [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)

Adding MFA to a user pool.

- [SMS and email MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-sms-email-message.html): Sign in users securely with multi-factor authentication using SMS text messages or email messages.
- [TOTP software token MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-totp.html): Activate TOTP software token MFA.

### [Threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html)

Understand the threat protection features of Amazon Cognito user pools..

- [Compromised credentials](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-compromised-credentials.html): Check for user passwords that might have been compromised and block user access if detected.
- [Adaptive authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html): Configure adaptive authentication in threat protection for Amazon Cognito user pools.
- [Data collection](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html): Configure an application to submit data to threat protection for threat analysis.
- [AWS WAF Web ACLs](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html): You can associate an AWS WAF web ACL with an Amazon Cognito user pool.
- [Case sensitivity](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-case-sensitivity.html): Managing user pool case sensitivity settings.
- [Deletion protection](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html): To prevent the accidental deletion of your user pool, activate deletion protection
- [Managing user disclosure](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html): Configure Amazon Cognito to prevent accidental disclosure of existing users in your user pool.

### [User pool endpoints reference](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html)

This documentation describes the managed login, SAML 2.0, OpenID Connect, and OAuth 2.0 authentication and authorization endpoints for Amazon Cognito user pools.

### [Managed login endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-endpoints.html)

This documentation describes the managed login webpages for Amazon Cognito user pools.

- [Login endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/login-endpoint.html): Describes how to interact with the user pool login endpoint, a redirect destination from the authorize endpoint.
- [Logout endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html): Use the logout OAuth 2.0 and OIDC endpoint to sign out from Amazon Cognito.

### [Federation endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints.html)

This documentation describes managed login, SAML 2.0, OpenID Connect, and OAuth 2.0 authentication and authorization endpoints for Amazon Cognito user pools.Amazon Cognito creates user pool endpoints when you set up a domain.

- [Authorize endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html): Use the authorize OAuth 2.0 and OIDC endpoint to sign in to Amazon Cognito.
- [Token endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html): Learn how to generate requests to the /oauth2/token endpoint for Amazon Cognito OAuth 2.0 access tokens, OpenID Connect (OIDC) ID tokens, and refresh tokens.
- [userInfo endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/userinfo-endpoint.html): The userInfo endpoint provides user attributes to applications that present user pool access tokens.
- [Revoke endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/revocation-endpoint.html): Use the revoke endpoint to revoke access and refresh tokens that Amazon Cognito issued.
- [SAML idpresponse endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/saml2-idpresponse-endpoint.html): Use the saml2/idpresponse SAML 2.0 endpoint to sign in to Amazon Cognito.
- [OAuth 2.0 grants](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html): A description of the OAuth 2.0 grants that the user pool authorization server can issue.
- [Using PKCE](https://docs.aws.amazon.com/cognito/latest/developerguide/using-pkce-in-authorization-code.html): Use Proof Key for Code Exchange (PKCE) to authorize sign-in with the Amazon Cognito user pools authorization server.
- [Managed login and federation error responses](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoint-idp-responses.html): A sign-in process in managed login or federated sign-in might return an error.


## [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html)

- [Configuring identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html): Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have been authenticated and received a token.
- [Identity pools authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html): Describes authentication flow in Amazon Cognito.
- [IAM roles](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html): Use IAM roles with Amazon Cognito identity pools.
- [Security best practices](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools-security-best-practices.html): Learn about secure implementation of Amazon Cognito identity pools.
- [Using attributes for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/attributes-for-access-control.html): Using attributes for access control
- [Using role-based access control](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html): Concepts for role-based access control.
- [Getting credentials](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-credentials.html): You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your application, so that your users can access AWS resources.
- [Using credentials](https://docs.aws.amazon.com/cognito/latest/developerguide/accessing-aws-services.html): Use your identity pool credentials to request access to resources in AWS.

### [Third-party identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html)

How Amazon Cognito identity pools use external identity providers for authentication.

- [Facebook](https://docs.aws.amazon.com/cognito/latest/developerguide/facebook.html): Amazon Cognito identity pools work with Facebook to provide federated authentication for your application users.
- [Login with Amazon](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon.html): Amazon Cognito identity pools work with Login with Amazon to provide federated authentication for your mobile and web app users.
- [Google](https://docs.aws.amazon.com/cognito/latest/developerguide/google.html): Amazon Cognito identity pools work with Google to provide federated authentication for your mobile application users.
- [Sign in with Apple](https://docs.aws.amazon.com/cognito/latest/developerguide/apple.html): Amazon Cognito identity pools work with Sign in with Apple to provide federated authentication for your mobile application and web application users.
- [Open ID Connect providers](https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html): OpenID Connect is an open standard for authentication that a number of login providers support.
- [SAML identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html): With Amazon Cognito identity pools, you can authenticate users with identity providers (IdPs) through SAML 2.0.
- [Developer-authenticated identities](https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html): Use Amazon Cognito to register and authenticate users with your existing authentication process.
- [Switching identities](https://docs.aws.amazon.com/cognito/latest/developerguide/switching-identities.html): Use Amazon Cognito to switch user identities.


## [Amazon Cognito Sync](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync.html)

- [Getting started with Amazon Cognito Sync](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-sync.html)
- [Synchronizing data across clients](https://docs.aws.amazon.com/cognito/latest/developerguide/synchronizing-data.html)
- [Handling event callbacks](https://docs.aws.amazon.com/cognito/latest/developerguide/handling-callbacks.html)
- [Implementing push synchronization](https://docs.aws.amazon.com/cognito/latest/developerguide/push-sync.html)
- [Implementing Amazon Cognito Sync streams](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-streams.html)
- [Customizing workflows with Amazon Cognito Events](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-events.html)


## [Security](https://docs.aws.amazon.com/cognito/latest/developerguide/security.html)

- [Data protection](https://docs.aws.amazon.com/cognito/latest/developerguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Cognito.

### [Identity and access management](https://docs.aws.amazon.com/cognito/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your Amazon Cognito resources.

- [How Amazon Cognito works with IAM](https://docs.aws.amazon.com/cognito/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Cognito, learn what IAM features are available to use with Amazon Cognito.
- [Identity-based policy examples](https://docs.aws.amazon.com/cognito/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Cognito resources.
- [Troubleshooting](https://docs.aws.amazon.com/cognito/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Cognito and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon Cognito access to resources in your AWS account.

### [Logging and monitoring](https://docs.aws.amazon.com/cognito/latest/developerguide/monitoring.html)

Monitor Amazon Cognito to maintain reliability, availability, and performance.

- [Monitoring costs](https://docs.aws.amazon.com/cognito/latest/developerguide/tracking-cost.html): Amazon Cognito charges for user pool usage, including monthly active users, federated users, and M2M usage.
- [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html): You can export SMS and email message delivery logs and threat protection user activity logs to CloudWatch Logs and other AWS services.

### [Monitoring quotas and usage](https://docs.aws.amazon.com/cognito/latest/developerguide/tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.html)

Amazon Cognito has tools to monitor usage and quotas, including integrations with CloudWatch for metrics and alarms, and Service Quotas for viewing and managing quota utilization.

- [User pool metrics in CloudWatch](https://docs.aws.amazon.com/cognito/latest/developerguide/metrics-for-cognito-user-pools.html): Amazon Cognito user pools report usage metrics to CloudWatch, including statistics on sign-ups, sign-ins, token refreshes, and federated identity flows.
- [Metrics in Service Quotas](https://docs.aws.amazon.com/cognito/latest/developerguide/use-the-service-quota-console-to-track-metrics.html): You can view and manage user pool and identity pool service quotas through the Service Quotas console.

### [CloudTrail logs](https://docs.aws.amazon.com/cognito/latest/developerguide/logging-using-cloudtrail.html)

Amazon Cognito integrates with AWS CloudTrail, capturing API calls and endpoint requests as events that are recorded as CloudTrail events.

- [Example events](https://docs.aws.amazon.com/cognito/latest/developerguide/understanding-amazon-cognito-entries.html): Lists some example CloudTrail events from Amazon Cognito user pools.
- [AWS PrivateLink](https://docs.aws.amazon.com/cognito/latest/developerguide/vpc-interface-endpoints.html): Learn how to set up AWS PrivateLink to create a private connection between your VPC and Amazon Cognito user pools and identity pools.
- [Compliance validation](https://docs.aws.amazon.com/cognito/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.

### [Resilience](https://docs.aws.amazon.com/cognito/latest/developerguide/disaster-recovery-resiliency.html)

Learn how AWS architecture supports data redundancy, and learn about specific Amazon Cognito features for data resiliency.

- [Regional data considerations](https://docs.aws.amazon.com/cognito/latest/developerguide/security-cognito-regional-data-considerations.html): Amazon Cognito user pools are each created in one AWS Region, and they store the user profile data only in that region.
- [Infrastructure security](https://docs.aws.amazon.com/cognito/latest/developerguide/infrastructure-security.html): Learn how Amazon Cognito isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/cognito/latest/developerguide/vulnerability-analysis-and-management.html): Configuration and vulnerability analysis in Amazon Cognito
- [AWS managed policies](https://docs.aws.amazon.com/cognito/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Cognito and recent changes to those policies.
