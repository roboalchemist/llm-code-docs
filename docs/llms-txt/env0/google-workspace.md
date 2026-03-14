# Source: https://docs.envzero.com/guides/sso-integrations/google-workspace.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Workspace Integration

> Set up Google Workspace as a SAML identity provider for env zero single sign-on

## Introduction

This guide will detail the various steps required to integrate Google Workspace as a SAML provider for your env zero organization. The current implementation is used for authentication only, where you define your users in your Google Workspace account to enable them access to your env zero organization. You can also add env zero as an application in your user application dashboard.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to your Google Workspace admin dashboard - [https://admin.google.com](https://admin.google.com)
2. Go to `Apps` > `Web and mobile apps`
3. Under the `Add app` button dropdown select `Add custom SAML app`
4. Give the app a name and set the app icon and click on the `Continue` button

<Frame caption="App Details">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/app_details.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=b6ac0dc9ea8ff5cb33ae109df2e5d267" alt="Google Workspace app details configuration showing custom SAML app setup form" width="1053" height="695" data-path="images/guides/sso-integrations/app_details.png" />
</Frame>

1. Copy the SSO URL, Entity ID and download the certificate. You will need to send those over to env zero so we can set up the SAML on our side. Then click on the `Continue` button
2. In the `ACS URL` enter the following: `https://login.app.env0.com/login/callback?connection=YOUR_ENV0_ORG_ID`
3. In the `Entity ID` enter `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
4. Check the `Signed Response` checkbox
5. In the `Name ID format` choose `Unspecified`
6. In the `Name ID`, choose `Basic Information` and `Primary Email`
7. Click on the `Continue` button
8. In the `Attributes` add the following:

| Google Directory attributes | App attributes         |
| :-------------------------- | :--------------------- |
| Primary email               | email                  |
| First Name                  | firstName              |
| Last Name                   | lastName               |
| Name                        | {firstName} {lastName} |

<Frame caption="Attributes Mapping">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/attributes_mapping.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=ea655d59b839a1fc2d1ee515e7e8f68d" alt="Google Workspace attributes mapping interface showing user attribute configuration for SAML" width="1045" height="517" data-path="images/guides/sso-integrations/attributes_mapping.png" />
</Frame>

1. In the `Group membership` add any Groups you would like to sync with env zero, and in the `App attribute` enter `teams`

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/ad1fc6f-group_membership.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=c5751e6d1f5e632e1d190ac0870cf6d4" alt="" width="1041" height="223" data-path="images/guides/sso-integrations/ad1fc6f-group_membership.png" />

<Info>
  **Groups Syncing**

  Groups will be synced each time a user logins with the following logic:

  1. env zero will create a new team if one doesn't exist based on the group name it received from the Google Workspace.
  2. If the team exists in env zero, env zero will not create a new team.\
     env zero will assign the user to all the teams in env zero based on the group **names** they are part of in the Google Workspace.
  3. If the user was removed from a group in the Google Workspace, env zero will remove them from the team in env zero.
  4. The names of the teams in env zero will be the same as the Group Name (including whitespaces) and not the Group Email.
</Info>

  13. Click on the `Finish`
  14. In the `User Access` set the user you would like to have access to env zero

<Frame caption="User Access">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/user_access.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=2ea669fae8db8e9ac277e42909febf8b" alt="Google Workspace user access settings showing app access permissions and user assignment" width="1178" height="175" data-path="images/guides/sso-integrations/user_access.png" />
</Frame>

1. Navigate to your env zero organization settings and go to the **SSO** tab.
2. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL (SSO URL)
    * Entity ID
    * X.509 Certificate

Built with [Mintlify](https://mintlify.com).
