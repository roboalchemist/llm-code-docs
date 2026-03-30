# Source: https://pipedream.com/docs/workspaces/sso.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Sign On Overview

Pipedream supports Single Sign-On (SSO) with [Okta](/workspaces/sso/okta/), [Google](/workspaces/sso/google/), or [any provider](/workspaces/sso/saml/) that supports SAML or Google OAuth, which allows IT and workspace administrators easier controls to manage access and security.

Using SSO with your Identity Provider (IdP) centralizes user login management and provides a single point of control for IT teams and employees.

## Requirements for SSO

* Your workspace must be on a [Business plan](https://pipedream.com/pricing)
* If using SAML, your Identity Provider must support SAML 2.0
* Only workspace admins and owners can configure SSO
* Your workspace admin or owner must [verify ownership](/workspaces/sso/#verifying-your-email-domain) of the SSO email domain

<Warning>
  The below content is for workspace admins and owners. Only workspace admins and owners have access to add verified domains, set up SSO, and configure workspace login methods.
</Warning>

## Verifying your Email Domain

In order to configure SAML SSO for your workspace, you first need to verify ownership of the email domain. If configuring Google OAuth (not SAML), you can skip this section.

[Refer to the guide here](/workspaces/domain-verification/) to verify your email domain.

## Setting up SSO

Navigate to the [Authentication section](https://pipedream.com/settings/domains) in your workspace settings to get started.

### SAML SSO

1. First, make sure you’ve verified the domain(s) you intend to use for SSO ([see above](/workspaces/sso/#verifying-your-email-domain))
2. Click the **Enable SSO** toggle and select **SAML**
3. If setting up SAML SSO, you’ll need to enter a metadata URL, which contains all the necessary configuration for Pipedream. Refer to the provider-specific docs for the detailed walk-through ([Okta](/workspaces/sso/okta/), [Google Workspace](/workspaces/sso/google/), [any other SAML provider](/workspaces/sso/saml/)).
4. Click **Save**

### Google OAuth

1. Click the **Enable SSO** toggle and select **Google**
2. Enter the domain that you use with Google OAuth. For example, `vandalayindustries.com`
3. Click **Save**

## Restricting Login Methods

Once you’ve configured SSO for your workspace, you can restrict the allowed login methods for [non-workspace owners](/workspaces/sso/#workspace-owners-can-always-sign-in-using-any-login-method).

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/6a24bb8b-Google_Chrome_-_Settings_-_Authentication_-_Pipedream_2023-11-13_at_2.27.08_PM_x1ahod.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=9ef200f5792255f25d1785e47aaedcfe" width="1426" height="910" data-path="images/6a24bb8b-Google_Chrome_-_Settings_-_Authentication_-_Pipedream_2023-11-13_at_2.27.08_PM_x1ahod.png" />
</Frame>

| Login Method         | Description                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Any login method** | Everyone in the workspace can sign in either using SSO or via the login method they used to create their account (email and password, Google OAuth, GitHub)                                                                                       |
| **SSO only**         | Workspace members and admins must [sign in using SSO](https://pipedream.com/auth/sso)                                                                                                                                                             |
| **SSO with guests**  | When signing in using a verified email domain, members and admins must [sign in using SSO](https://pipedream.com/auth/sso). If signing in with a different domain (`gmail.com` for example), members (guests) can sign in using any login method. |

### Workspace owners can always sign in using any login method

In order to ensure you don’t get locked out of your Pipedream workspace in the event of an outage with your identity provider, workspace owners can always sign in via the login method they used to create the account (email and password, Google, or GitHub).

### Login methods are enforced when signing in to pipedream.com

This means if you are a member of 2 workspaces and one of them allows **any login method** but the other **requires SSO**, you will be required to sign in to Pipedream using SSO every time, independent of the workspace you are trying to access.

Built with [Mintlify](https://mintlify.com).
