# Source: https://docs.envzero.com/guides/sso-integrations/onelogin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OneLogin Integration

> Integrate OneLogin as a SAML identity provider for env zero single sign-on authentication

## Introduction

This guide will detail the various steps required to integrate OneLogin as a SAML provider for your env zero organization. The current implementation supports SAML 2.0 and is used for authentication only, where you define your users in your OneLogin account to enable them access to your env zero organization. You can also add env zero as an application in your user application dashboard.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to your OneLogin Administrator account.
2. Under the Application tab go to the Application.
3. Click on the `Add App` button.
4. In the search box enter `SAML Custom Connector` and select `SAML Custom Connector (Advanced)`

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/f96dce3-onelogin_find_app.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=03e9dcf42a98ce21e85f93ae14ac541e" alt="" width="1600" height="312" data-path="images/guides/sso-integrations/f96dce3-onelogin_find_app.png" />

1. Change the display name to be `env zero` and upload an icon.
2. Enter a relevant description and click on the save button.

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/b4cdff9-onelogin_-_custom_connector.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=af5fd222b07edd1396047db2a3bf91f6" alt="" width="1600" height="788" data-path="images/guides/sso-integrations/b4cdff9-onelogin_-_custom_connector.png" />

1. Go to the configuration tab.
2. Under Audience (EntityID) enter `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
3. Under ACS (Consumer) URL Validator enter: `[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)`
4. Under ACS (Consumer) URL enter `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
5. Under the Login URL enter `https://app.env0.com/login/sso`
6. In the `SAML initiator` dropdown select `Service Provider`
7. In the `SAML nameID format` dropdown select `Unspecified`
8. In the `SAML signature element` dropdown select `Both`
9. Click on the save button.
10. Go to the “Parameters” tab
11. Add the following Parameters:

| Name         | Marco | Value                  | Include in SAML assertion |
| :----------- | :---- | :--------------------- | :------------------------ |
| NameID value | false | Email                  | N/A                       |
| email        | false | Email                  | true                      |
| firstName    | false | First Name             | true                      |
| lastName     | false | Last Name              | true                      |
| name         | true  | {firstname} {lastname} | true                      |

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/8339b9e-onelogin_custom_connector.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=5cdbd6d7e894b39cfbf03ebdb9794438" alt="" width="1600" height="503" data-path="images/guides/sso-integrations/8339b9e-onelogin_custom_connector.png" />

1. Click on the `Save` button.
2. Go to the `SSO` tab.
3. Copy the `SAML 2.0 Endpoint (HTTP)` URL.
4. Copy the `SLO Endpoint (HTTP)` URL.
5. In the `X.509 Certificate` click on the `View Details` link.
6. Under the `X.509 Certificate` choose `X.509 PEM` and download it.
7. Assign the relevant users to this application.
8. Navigate to your env zero organization settings and go to the **SSO** tab.
9. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL (SAML 2.0 Endpoint (HTTP) URL)
    * X.509 Certificate

Built with [Mintlify](https://mintlify.com).
