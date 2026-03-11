# Source: https://docs.envzero.com/guides/sso-integrations/scim-provisioning.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning

> Automatically sync users and groups from your identity provider to env zero with SCIM 2.0

## Why SCIM

Without SCIM, env zero only syncs user access when someone logs in. That means if you offboard an employee in your IdP, they still have access to env zero until their next login attempt. SCIM fixes this by keeping your user directory in sync continuously - access is granted or revoked as soon as changes happen in your IdP.

### Key benefits

* **Immediate deprovisioning** - When you remove a user in your IdP, their env zero access is revoked right away, not at next login
* **No manual user management** - New team members get env zero access automatically when added to the right groups in your IdP
* **Single source of truth** - Your IdP stays the authoritative record for who has access to what

<Note>
  **Beta Feature** - SCIM Provisioning is currently in beta. We're actively improving the feature and welcome your feedback.
</Note>

## Overview

SCIM (System for Cross-domain Identity Management) is a standard protocol that enables your identity provider to automatically provision and deprovision users in env zero.

## Prerequisites

* **SSO must be configured** - SCIM provisioning is only available after you set up an [SSO connection](/guides/sso-integrations/self-service-sso) (SAML or Azure AD)
* **Edit Organization Settings** permission is required

## Setting Up SCIM

<Steps>
  <Step title="Navigate to SSO Settings">
    Go to **Organization Settings** > **SSO**. Below your SSO connection, you'll see the **SCIM Provisioning** section.

    <Frame>
      <img src="https://mintcdn.com/envzero-b61043c8/OKL42gfT_0D28WaJ/images/guides/sso-integrations/scim-generate-token.png?fit=max&auto=format&n=OKL42gfT_0D28WaJ&q=85&s=facae6f4537b1d3b087c7ec2a6b42ba4" alt="SCIM Provisioning section showing the Generate SCIM Token button" width="3158" height="1438" data-path="images/guides/sso-integrations/scim-generate-token.png" />
    </Frame>
  </Step>

  <Step title="Generate a SCIM Token">
    Click **Generate SCIM Token**. This creates a bearer token and SCIM endpoint URL for your organization.
  </Step>

  <Step title="Copy the Token and Endpoint URL">
    A dialog displays your **SCIM Endpoint URL** and **Bearer Token**. Copy both values immediately.

    <Warning>
      The bearer token is shown only once. If you lose it, you'll need to delete the SCIM configuration and generate a new one.
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/envzero-b61043c8/OKL42gfT_0D28WaJ/images/guides/sso-integrations/scim-token-created.png?fit=max&auto=format&n=OKL42gfT_0D28WaJ&q=85&s=3d857418ab62ce712cf922251c94614f" alt="SCIM Token Created dialog showing the endpoint URL and bearer token" width="3246" height="1394" data-path="images/guides/sso-integrations/scim-token-created.png" />
    </Frame>
  </Step>
</Steps>

Once configured, the SCIM Provisioning section displays your endpoint URL and the date the token was created.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/OKL42gfT_0D28WaJ/images/guides/sso-integrations/scim-configured.png?fit=max&auto=format&n=OKL42gfT_0D28WaJ&q=85&s=e4612f00cb3bea323c488ea2eade989e" alt="SCIM Provisioning configured state showing endpoint URL and creation date" width="3374" height="1480" data-path="images/guides/sso-integrations/scim-configured.png" />
</Frame>

## Configuring Your Identity Provider

Use the SCIM Endpoint URL and Bearer Token to configure provisioning in your identity provider.

<Warning>
  Your IdP must map the user's **email address** to the SCIM `userName` attribute. env zero uses this field to match IdP users to organization members. Without a valid email mapping, provisioning will not work correctly.
</Warning>

See your IdP's documentation for SCIM setup instructions:

* **Okta** - [Configure SCIM provisioning in Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_scim.htm)
* **Microsoft Entra ID (Azure AD)** - [Configure SCIM provisioning in Entra ID](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups)

For other identity providers, refer to their SCIM 2.0 integration documentation and use the endpoint URL and bearer token from the previous step.

## Revoking a SCIM Token

To revoke SCIM access, navigate to **Organization Settings** > **SSO** and click **Delete Configuration** in the SCIM Provisioning section. This immediately invalidates the token and stops all SCIM provisioning from your IdP.

## Related

* [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso)
* [Sync Roles & Groups From Your IdP](/guides/sso-integrations/importing-roles-or-groups-from-your-identity-provider)

Built with [Mintlify](https://mintlify.com).
