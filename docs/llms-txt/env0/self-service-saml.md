# Source: https://docs.envzero.com/guides/sso-integrations/self-service-saml.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-Service SAML Setup

> Self-service SAML 2.0 configuration guide for env zero single sign-on authentication

## Overview

This guide explains how to configure SAML 2.0 authentication for your env zero organization using the self-service SSO configuration. You can use this with any SAML-compatible identity provider.

## Prerequisites

**Edit Organization Settings permission** is required to configure SSO.

<Note>
  Before proceeding, ensure you've accessed the SSO configuration in Organization Settings > SSO tab and selected **SAML** as described in the [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) guide.
</Note>

## Required SAML Settings

Configure the following in your SAML identity provider:

* **ACS URL (Assertion Consumer Service URL)**: `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
  * Replace `{YOUR_ENV0_ORG_ID}` with your organization ID (found in Organization > Settings tab)

* **Entity ID / Audience URL**: `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
  * Replace `{YOUR_ENV0_ORG_ID}` with your organization ID

* **Name ID Format**: `Unspecified` or `urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified`

### Required Attribute Mappings

Configure the following attribute mappings in your SAML provider:

| Attribute Name      | Description                                     | Required |
| :------------------ | :---------------------------------------------- | :------- |
| `email`             | User's email address                            | Yes      |
| `firstName`         | User's first name                               | Yes      |
| `lastName`          | User's last name                                | Yes      |
| `name`              | User's full name                                | Yes      |
| `groups` or `teams` | User's group/team membership (for team syncing) | No       |

## Completing the Self-Service Form

<Steps>
  <Step title="Configure SAML Application">
    Set up the SAML application in your identity provider using the required SAML settings and attribute mappings above.
  </Step>

  <Step title="Enter Provider Details">
    In the env zero self-service form, enter:

    * Identity Provider Single Sign-on URL (SSO URL)
    * X.509 Certificate (download from your identity provider)
  </Step>

  <Step title="Complete Configuration">
    Complete the remaining steps in the self-service form and save your configuration.
  </Step>
</Steps>

## Provider-Specific Guides

For detailed setup instructions for specific SAML providers, see:

* [AWS Single Sign-On](/guides/sso-integrations/aws-single-sign-on)
* [Okta Integration](/guides/sso-integrations/okta-integration)
* [Google Workspace](/guides/sso-integrations/google-workspace)
* [Keycloak](/guides/sso-integrations/keycloak)
* [OneLogin](/guides/sso-integrations/onelogin)
* [JumpCloud](/guides/sso-integrations/jumpcloud)
* [VMware Workspace ONE](/guides/sso-integrations/vmware-workspace-one)

<Note>
  If your SAML provider is not listed, we support all SAML providers. Follow the general configuration above, or contact [support@env0.com](mailto:support@env0.com) for assistance.
</Note>

## Teams Syncing

<Info>
  **Teams Syncing**

  Teams will be synced each time a user logs in with the following logic:

  1. env zero will create a new team if one doesn't exist based on the group name received from the SAML provider.
  2. If the team exists in env zero, we will not create a new team.
  3. We will assign the user to all the teams in env zero based on the group names they are part of in the SAML provider.
  4. If the user was removed from a group in the SAML provider, we will remove them from the team in env zero.
</Info>

Learn more: [Sync Roles & Groups From Your IdP](/guides/sso-integrations/importing-roles-or-groups-from-your-identity-provider)

Built with [Mintlify](https://mintlify.com).
