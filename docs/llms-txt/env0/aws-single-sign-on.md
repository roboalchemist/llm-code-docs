# Source: https://docs.envzero.com/guides/sso-integrations/aws-single-sign-on.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS Single Sign On Integration

> Configure AWS Single Sign-On as a SAML provider for env zero organization authentication

## Introduction

This guide will detail the various steps required to integrate AWS SSO as a SAML provider for your env zero organization. The current implementation supports SAML 2.0 and is used for authentication only, where you define your users in your AWS SSO account to enable them access to your env zero organization.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to your AWS Account and navigate to the AWS SSO service.
2. Click on the Applications tabs on the left-hand side menu.
3. Click on the `Add a new application` button.
4. Select `I have an application I want to set up`.
5. Select the `SAML 2.0`

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/aws_sso_saml_20_selection.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=d115c8013c50da4e72bde23c70e08fcf" alt="AWS SSO application setup interface showing SAML 2.0 selection option" width="918" height="884" data-path="images/guides/sso-integrations/aws_sso_saml_20_selection.png" />
</Frame>

1. Enter the `Display name` and `Description`
2. Configure the `User and group assignment method` section
3. In the `AWS access portal` set the `Application URL` to be `https://app.env0.com/login/sso`
4. Click on the `Next` button
5. In the `IAM Identity Center metadata` section download the `IAM Identity Center Certificate` and copy the `IAM Identity Center sign-in URL`
6. In the `Application properties` set the `Application start URL` to `https://app.env0.com/login/sso`
7. Set the desired `Session duration`
8. In the `Application metadata` section click on the `If you don't have a metadata file, you can manually type your metadata values` link
9. In the `Application metadata` section, under `Application ACS URL` enter the following `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
10. In the `Application SAML audience` enter `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
11. Click on the `Submit` button
12. In the Action Dropdown select `Edit Attribute mappings`
13. Add the following attributes:

| Name      | Value                | Format      | Mandatory |
| :-------- | :------------------- | :---------- | :-------- |
| Subject   | \$\{user:subject}    | persistent  | Yes       |
| name      | \$\{user:name}       | basic       | Yes       |
| lastName  | \$\{user:familyName} | basic       | Yes       |
| firstName | \$\{user:givenName}  | basic       | Yes       |
| groups    | \$\{user:groups}     | unspecified | No        |
| email     | \$\{user:subject}    | unspecified | Yes       |

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/aws_sso_attribute_mappings.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=d3021d8e0f2f65810320536e8133b3b8" alt="AWS SSO attribute mappings configuration showing user attribute settings for SAML integration" width="1625" height="464" data-path="images/guides/sso-integrations/aws_sso_attribute_mappings.png" />
</Frame>

<Note>
  Groups Mapping with AWS SSO

  The `groups` attribute in AWS SSO currently supports the UUID of the groups and not the actual name of the group.

  This means that if you set the `groups` attribute we will sync the groups based on their UUID.
</Note>

1. Click on `Assigned users` button and assign the relevant users and groups to the application
2. Navigate to your env zero organization settings and go to the **SSO** tab.
3. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL (AWS SSO sign-in URL)
    * X.509 Certificate (AWS SSO Certificate)

Built with [Mintlify](https://mintlify.com).
