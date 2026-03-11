# Source: https://docs.envzero.com/guides/sso-integrations/okta-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta Integration

> Set up Okta as a SAML provider for env zero with user authentication and group syncing

## Introduction

This guide will detail the various steps required to integrate Okta as a SAML provider for your env zero organization. The current implementation supports SAML 2.0 and is used for authentication only, where you define your users in your Okta account to enable them access to your env zero organization. You can also add env zero as an application in your user application dashboard.\
In addition, we also support group syncing of the logged in user to match those with env zero teams.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

<Note>
  **Automated User Provisioning**: Okta supports SCIM 2.0 for automatically provisioning and deprovisioning users in env zero. Once SSO is configured, see [SCIM Provisioning](/guides/sso-integrations/scim-provisioning) to set it up.
</Note>

## Steps

1. Login to the Okta admin console
2. Go to the `Applications > Applications`
3. Click on the `Add Application` button
4. Click on the `Create New App` button
5. Choose `Web` and `SAML 2.0` and click on the Create button

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/94b45b9-okta_new_app_form.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=4163e476af3e6b68863e0f8c69a6f145" alt="" width="1408" height="1018" data-path="images/guides/sso-integrations/94b45b9-okta_new_app_form.png" />

1. Set the application name to `env zero` and upload a logo and click on `Next`
2. In the `Single sign on URL` enter `https://login.app.env0.com/login/callback?connection=YOUR_ENV0_ORG_ID`
3. In the `Audience URL (SP Entity ID)` enter `urn:auth0:env0:YOUR_ENV0_ORG_ID`\
   e.g. `urn:auth0:env0:aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`
4. In the `Name ID format` put `Unspecified`
5. Click on the `Show Advanced Settings`

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/3ea0b1a-okta_saml_form.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=7204266fcf2d2e5a5c28031516ecefb1" alt="" width="1450" height="1154" data-path="images/guides/sso-integrations/3ea0b1a-okta_saml_form.png" />

1. Change the `Assertion Encryption` to be `Encrypted` and upload the PEM located [here](https://drive.google.com/file/d/1jz1BgKR5pmWB9WFITpBIczPsytgKXRUt)
2. In the `ATTRIBUTE STATEMENTS` add the following:

| Name      | Value                                  |
| :-------- | :------------------------------------- |
| email     | user.email                             |
| firstName | user.firstName                         |
| lastName  | user.lastName                          |
| name      | \$\{user.firstName} \$\{user.lastName} |

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/984a3fb-att_okta.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=475e4c02ce8accc586bc155db754a28f" alt="" width="1440" height="908" data-path="images/guides/sso-integrations/984a3fb-att_okta.png" />

1. Leave the rest of the default values and click `Next`
2. If you would like to set up groups as well you should do the following:

* In the `Group Attribute Statements (optional)` add and Attribute
* The name should be teams and then set the filter according to what you wish. For example, to get all groups set a regex filter with the value of `(.*?)`

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/712ed01-group_attr.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=336d9de0e932509153b45c6bfd16c5d3" alt="" width="1482" height="528" data-path="images/guides/sso-integrations/712ed01-group_attr.png" />

<Info>
  **Teams syncing**

  Teams will be synced each time a user logins with the following logic:

  1. env zero will create a new team if one doesn't exist based on the group name we received from the SAML provider.
  2. If the team exists in env zero we will not create a new team.
  3. We will assign the user to all the teams in env zero based on the group names he/she is part of in the SAML provider.
  4. If the user was removed from a group in the SAML provider we will remove him/her from the team in env zero.
</Info>

  16. Choose `I’m an Okta customer adding an internal app` and click on `Finish`.
  17. In the `Sign on` Tab and click on the `View Setup Instructions` button.
  18. Download the `Okta Certificate`

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/0daaab4-okta_final_settings.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=6552b49b7aa07672be6dec7b12054dd7" alt="" width="1494" height="1314" data-path="images/guides/sso-integrations/0daaab4-okta_final_settings.png" />

1. Navigate to your env zero organization settings and go to the **SSO** tab.
2. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL
    * X.509 Certificate (Okta Certificate)

Built with [Mintlify](https://mintlify.com).
