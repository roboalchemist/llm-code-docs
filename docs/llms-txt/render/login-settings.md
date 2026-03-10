# Source: https://render.com/docs/login-settings.md

# Login Settings — Connect your login provider and enforce requirements for your workspace.

Render integrates with multiple login providers and helps you enforce secure login requirements for your workspace.

## Supported login methods

- Any of the following account providers:
  - Google
  - GitHub
  - GitLab
  - Bitbucket
- Email and password
- [SAML SSO](saml-sso) (Enterprise organizations only)

## Managing login methods

Go to the *Account Security* section of your [Account Settings](https://dashboard.render.com/u/settings#account-security) page:

[image: Managing login methods in the Render Dashboard]

Here, you can:

- Update your password
- Add or remove connected login methods
- Add or remove connected Git deployment credentials
  - Render uses these credentials to access your repositories for [deploys](/deploys).
- Toggle two-factor authentication (2FA)

### Rules for account connections

- If you connect GitHub for both login and deployment, you _must_ use the same GitHub account for both.
  - The same is true for GitLab and Bitbucket.
- You _can_ use a Git provider for deployment _without_ using it for login (or vice versa).
- Multiple Render accounts _can't_ use the same provider account to _log in_.
- Multiple Render accounts _can_ use the same provider account for _deployment_.
- You _can't_ disconnect your Google account if you belong to a workspace that enforces [Google-account-based login](#google-account-login). First, leave any such workspaces.

## Enforcing secure login

Your workspace can require its members to use any combination of the following login practices:

- [Two-factor authentication (2FA)](#two-factor-authentication)
- [Google account login](#google-account-login)

Only workspace [admins](team-members#member-roles) can configure these enforcements.

Enterprise organizations can also enforce secure login via [SAML SSO](saml-sso).

### Two-factor authentication

Enforce two-factor authentication (2FA) from your *Workspace Settings* page:

[image: UI for enabling 2FA]

If you enforce 2FA, your team members can't access the workspace's resources or settings until they enable 2FA for their Render account.

> Team members with SSH or [API keys](api#1-create-an-api-key) can't use these keys to access workspace resources until they enable 2FA.

### Google account login

Enforce Google-account-based login from your *Workspace Settings* page:

[image: UI for enforcing Google account login]

*If you enable this feature:*

- Team members can't access the workspace's resources or settings if they log in using any method _besides_ their Google account (such as username and password).
-  Team members can't change their Render account's associated email address.
- Team members must sign in with the Google account that matches the invited email address.
  - For example, a workspace invitation for `person@example.com` must be accepted by signing in with that specific Google account, not a personal Gmail address.

[API keys](api#1-create-an-api-key) must be created while signed in via Google account to access resources of a workspace that enables this feature. API keys created before May 1, 2024 are not subject to this restriction.