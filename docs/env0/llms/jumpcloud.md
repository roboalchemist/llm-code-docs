# Source: https://docs.envzero.com/guides/sso-integrations/jumpcloud.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Jumpcloud Integration

> Integrate JumpCloud as a SAML identity provider for env zero single sign-on authentication

## Introduction

This guide will detail the steps required to integrate Jump Cloud as a SAML provider for your env zero organization. The current implementation supports SAML 2.0 and is used for authentication only, where you define your users in your Jump Cloud account to enable them access to your env zero organization.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to the Jump Cloud admin console.
2. Under the User Authentication menu click on the SSO.
3. Add a new application.
4. Click on the “Custom SAML app”.

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/679618d-jumpcloud_saml_app.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=8c058cd10c9833f694d4ccaa3a32cb64" alt="" width="563" height="75" data-path="images/guides/sso-integrations/679618d-jumpcloud_saml_app.png" />

1. In the `General Info` tab fill in the Display name as `env zero` add a description and choose a color indication or upload the env zero logo.
2. In the `SSO` tab fill in the following information:

* IdP Entity ID - `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
* SP Entity ID - `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
* ACS URL - `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
* SP Certificate: Upload [this file](https://drive.google.com/file/d/1jz1BgKR5pmWB9WFITpBIczPsytgKXRUt)
* SAMLSubject NameID: email
* SAMLSubject NameID Format: `urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified`
* Signature Algorithm: RSA-SHA256
* Groups Attributes: Check the `include group attribute` and set it to be `teams`
* Attributes:

| Service Provider Attribute Name | JumpCloud Attribute Name |
| :------------------------------ | :----------------------- |
| email                           | email                    |
| firstName                       | firstname                |
| lastName                        | lastname                 |
| name                            | fullname                 |

<Info>
  **Teams Syncing**

  Teams will be synced each time a user will login with the following logic:

  1. env zero will create a new team if one doesn't exist based on the group name we received from the SAML provider.
  2. If the team exists in env zero we will not create a new team.
  3. We will assign the user to all the teams in env zero based on the group names they are a member of in the SAML provider.
  4. If the user was removed from a group in the SAML provider we will remove them from the team in env zero.
</Info>

  7. In the `User Groups` tab Select the group of users you would like to have access to the env zero platform.
  8. Click on the `activate` button and create the application.
  9. Go to the env zero application to edit it.
  10. On the right-hand side click on the `IDP Certificate` dropdown and click on the `Download certificate` option.
  11. In the SSO tab copy the `IDP URL`
  12. Navigate to your env zero organization settings and go to the **SSO** tab.
  13. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL (IDP URL)
    * X.509 Certificate

Built with [Mintlify](https://mintlify.com).
