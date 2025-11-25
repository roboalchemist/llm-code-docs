# Source: https://docs.upsun.com/administration/security/sso.md

# Single Sign-On (SSO)


  **Feature Availability**

  This feature is available as part of the Advanced User Management add-on. You can [upgrade your organization to this add-on](https://docs.upsun.com/administration/billing/add-on-subscription.md#upgrade-to-the-advanced-user-management-add-on) in the Console.
For details about the other features included in this add-on, see the [Advanced User Management add-on](https://docs.upsun.com/administration/billing/add-on-subscription.md#advanced-user-management-add-on) help topic section; for pricing information, see the [Upsun pricing](https://upsun.com/pricing/) page.

Upsun enables you to set up mandatory SSO with a third-party identity provider (IdP) for all your users.

Your SSO provider can be enabled for a specific email domain, for example `@example.com`. Every user with a matching email address needs to log in or register on Upsun using your SSO provider. Such users can't use an alternative provider, or register a password, or change their email address.

## Mitigation controls

If you deactivate a user on your identity provider, they can't log in or register on Upsun.

If the user is already logged in to Upsun, they are automatically deactivated after their access token has expired (generally after 1 hour).

A deactivated user can no longer use SSH, Git, or other Upsun APIs.

## Service users

If you have a service user with an email address under your SSO domain, such as `machine-user@example.com`, you can exclude that user from the SSO enforcement rule so they aren't required to authenticate through your identity provider.

Please open a [support ticket](https://docs.upsun.com/learn/overview/get-support.md) if you need to exclude a service user.

## SSO providers

### Google

Enforce your users to authenticate with Google. To enable Google SSO, please open a [support ticket](https://docs.upsun.com/learn/overview/get-support.md).

#### Issue with re-authenticating every 15 minutes

If your organization has Google SSO enabled on Upsun, you may be required to re-authenticate with Google every 15 minutes. This happens when Upsun doesn't possess a valid refresh token from your Google account.

To resolve this issue:

1. Go to [https://myaccount.google.com/permissions](https://myaccount.google.com/permissions) and revoke the access from the `Upsun` application that has `Access given to auth.api.platform.sh`.
2. Go to [https://auth.upsun.com/auth/authorize/google?prompt=consent](https://auth.upsun.com/auth/authorize/google?prompt=consent) for the system to obtain a valid refresh token for your Google account.

### OpenId Connect

Enforce your users to authenticate with your OpenID Connect (OIDC) provider,
such as Microsoft (Entra ID), Okta, Ory, or Ping Identity.
To enable SSO with your OIDC provider, please
[create a Support ticket](https://console.upsun.com/-/users/~/tickets).

