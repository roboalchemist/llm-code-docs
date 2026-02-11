# Source: https://docs.icepanel.io/other-information/sso-saml.md

# SSO - SAML

{% hint style="success" %}
IdP-initiated login is now available. If you’re an existing client and would like to be migrated, please email us. If you’re new, fill out the form below.
{% endhint %}

Configuring single sign using SAML integrates IcePanel with your organizations identity provider. This allows users in your organization to securely and easily sign in to IcePanel without the need to manage additional credentials.

## Getting started

Instructions can vary based on your SAML identity provider. See examples for [identity providers](#identity-providers) below.

Step 1: Create a new SAML application in your identity provider with the following info:

* ACS URL / Reply URL - **leave this empty. We will provide you with this link as a very last step.**
* Entity ID / Identifier - `icepanel.io`

Step2: Fill out below form:

* Fill out our [SAML registration form](https://icepanel.io/sso-registration/saml) with the requested information from your app. Once that's submitted, it can take up to 1 business day for us to configure it. We'll be in touch shortly to confirm and check everything is working.

***

## SSO share links

Once you've configured a SAML app with us you can globally secure access to share links with SSO.

In organization management you can set one or more domains that can access your share links securely. The example below will restrict all share link access to users who authenticate with `@icepanel.io` email addresses.

![Configure SAML SSO](https://assets.icepanel.io/docs/sso/share-link-sso.png)

Users will now be redirected to your SAML authentication flow before gaining access to a share link. They will not be required to create an IcePanel account, so these users will not count toward your plan seat count in any way.

***

## Identity providers

We support all identity providers that support SAML 2.0.

### Google Workspace

1. First navigate to `Apps` / `Web and mobile apps` on the [Google Admin console](https://admin.google.com/).
2. Click `Add app` / `Add custom SAML app`.
3. Fill in the app name as `IcePanel` and upload the [IcePanel logo](https://assets.icepanel.io/logo/blue/460.png).
4. Copy the values from the `SSO URL`, `Entity ID` and `Certificate` fields into our [SAML registration form](https://icepanel.io/sso-registration/saml).
5. Leave the `ACS URL` field to empty. We will provide you with this URL as a very last step.
6. Set the `Entity ID` field to `icepanel.io`.
7. Set the `Name ID format` field to `EMAIL` and the `Name ID` field to `Primary email`.
8. Click the `User access` section and check the toggle for `ON for everyone`.
9. Done, now wait for us to let you know it's all setup on our end.

### Microsoft Entra ID

1. First navigate to `Entra ID` on the [Microsoft Entra ID portal](https://portal.azure.com).
2. Click `Enterprise applications` from the left sidebar.
3. Click `New application` and pick the `Non-gallery application` type.
4. Fill in the app name as `IcePanel` and upload the [IcePanel logo](https://assets.icepanel.io/logo/blue/460.png).
5. Click `Single sign-on` in the left sidebar and choose the `SAML` method.
6. Click the edit pencil in the `Basic SAML configuration`.
7. Set the `Identifier (Entity ID)` field to `icepanel.io`.
8. Leave the `Reply URL (Assertion Consumer Service URL)` field to empty. We will provide you with this URL as a very last step.
9. Copy the `Certificate (Base64)`, `Login URL` and `Azure AD Identifier` fields into our [SAML registration form](https://icepanel.io/sso-registration/saml).
10. Click `Users and groups` in the left sidebar and add the users or groups that need access to IcePanel.
11. Done, now wait for us to let you know it's all setup on our end.

### Okta

1. First navigate to `Admin > Applications` on the Okta portal.
2. Click `Add New App` and select SAML 2.0.
3. Leave the `Single sign on URL` field to empty. We will provide you with this URL as a very last step.
4. Set the `Audience URI (SP Entity ID)`to icepanel.io.
5. Set the `Name ID format` to email address and the `Application username`to email.
6. Click `View setup instructions` get the necessary information.
7. Copy the values from the `SSO URL`, `Identity Provider Issuer (Entity ID)` and `Certificate` fields into our [SAML registration form](https://icepanel.io/sso-registration/saml).
8. Make sure the required users or groups have permission to access to the Okta app.
9. Done, now wait for us to let you know it's all setup on our end.

### Need more support?

[Book a call](https://cal.com/team/icepanel/icepanel-technical-support) with our technical team if you have any questions about SSO.
