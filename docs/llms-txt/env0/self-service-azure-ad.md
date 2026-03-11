# Source: https://docs.envzero.com/guides/sso-integrations/self-service-azure-ad.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Active Directory Integration

> Configure Azure Active Directory or Microsoft Entra ID as an OAuth provider for env zero SSO

## Overview

Configure Azure Active Directory (Microsoft Entra ID) as an OAuth provider for your env zero organization. This integration enables authentication through Microsoft Entra ID and supports automatic team syncing based on Azure AD groups.

## Prerequisites

**Edit Organization Settings permission** is required to configure SSO.

## Setup Steps

<Steps>
  <Step title="Register Application in Microsoft Entra ID">
    Register an application in the [Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). In platform settings, select **Web** and add a Redirect URI: `https://login.app.env0.com/login/callback`
  </Step>

  <Step title="Create Client Secret">
    Create a Client Secret and note the value. Copy the Application (client) ID and Client Secret Value for the next step.
  </Step>

  <Step title="Configure in env zero">
    Navigate to your organization settings > **SSO** tab. Click **Azure AD** and complete the self-service form with:

    * Application (client) ID
    * Client Secret Value
    * Email domain (e.g., env0.com) or Microsoft tenant domain (e.g., env0.onmicrosoft.com)
  </Step>
</Steps>

<Note>
  **Multitenant Microsoft Entra ID**

  If you are in a Multitenant environment, under **Authentication / Supported account types**, select **"Accounts in any organizational directory (Any Azure AD directory - Multitenant)"**.
</Note>

## Enabling Access

If users have trouble accessing the App Registration, grant admin consent:

<Steps>
  <Step title="Navigate to API Permissions">
    Go to **Manage > API Permissions** or **Security > Permissions** in your Azure AD application.
  </Step>

  <Step title="Grant Admin Consent">
    Click **"Grant Admin consent for env zero"** for:

    * **Microsoft Graph User.Read** - `Sign in and read user profile` permissions
    * **Microsoft Graph Directory.Read.All** permissions
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/ef8e498ade6a2517c5b9aee31a443a14c9f5080254bb1128cc7d36947fc97ee2-cleanshot_2024-10-08_at_11.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=73c0b0445fdf456bbc22e959416ec4ae" alt="Azure AD API Permissions showing admin consent for Microsoft Graph permissions" width="1310" height="784" data-path="images/guides/sso-integrations/ef8e498ade6a2517c5b9aee31a443a14c9f5080254bb1128cc7d36947fc97ee2-cleanshot_2024-10-08_at_11.png" />
</Frame>

## Teams Syncing

<Info>
  **Teams Syncing**

  Teams are synced each time a user logs in:

  1. env zero creates a new team if one doesn't exist based on the group name from the OAuth provider.
  2. If the team exists in env zero, we will not create a new team.
  3. Users are assigned to all teams in env zero based on the group names they belong to in the OAuth provider.
  4. If a user is removed from a group in the OAuth provider, they are removed from the team in env zero.
</Info>

Learn more: [Sync Roles & Groups From Your IdP](/guides/sso-integrations/importing-roles-or-groups-from-your-identity-provider)

## Automated User Provisioning (SCIM)

Microsoft Entra ID supports SCIM 2.0 for automatically provisioning and deprovisioning users in env zero. With SCIM, user access is updated continuously rather than only at login. See [SCIM Provisioning](/guides/sso-integrations/scim-provisioning) to set it up.

Built with [Mintlify](https://mintlify.com).
