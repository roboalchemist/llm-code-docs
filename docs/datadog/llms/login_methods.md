# Source: https://docs.datadoghq.com/account_management/login_methods.md

---
title: Configuring Login Methods
description: >-
  Enable or disable authentication methods like username/password, Google OAuth,
  and SAML for your Datadog organization with MFA enforcement options.
breadcrumbs: Docs > Account Management > Configuring Login Methods
---

# Configuring Login Methods

Login Methods determine how users may authenticate themselves and log into your Datadog organization. Using Login Methods to enable or disable the default login methods requires one of the following privileged access permissions:

- Datadog Admin Role
- Org Management (`org_management`) permission

When a login method is enabled by default, any user who is not explicitly denied access ([by a user login method override](https://docs.datadoghq.com/account_management/users/#edit-a-users-login-methods)) can use that login method to access Datadog, provided their username (their email address) matches the user that is invited to the organization.

The following login methods are available:

- Datadog Username and Password (also known as Standard)
  - Passwords must use at least 8 characters containing at least 1 number and 1 lowercase letter
- Sign in with Google
- [Sign in with SAML](https://docs.datadoghq.com/account_management/saml/)

## Enabling or disabling a default login method{% #enabling-or-disabling-a-default-login-method %}

As an organization manager, you can enable or disable the default login methods for your organization. New organizations start with **Datadog Username and Password** and **Sign in with Google** enabled and configured for all organizations and users. After you configure SAML, **Sign in with SAML** is also enabled.

1. Navigate to [Login Methods](https://app.datadoghq.com/organization-settings/login-methods).
1. Set the **Enabled by Default** setting for each method to `On` or `Off`, according to your organization's preference or policy requirements.
1. Confirm your selection.

**Note**: You cannot disable all login methods for an organization. At least one login method must be enabled by default for your organization.

## Requiring Multi-factor Authentication{% #requiring-multi-factor-authentication %}

For enhanced security, organization managers can enforce [Multi-factor Authentication](https://docs.datadoghq.com/account_management/multi-factor_authentication/) (MFA) for all users in the organization that log in with an email and password.

1. Navigate to [Login Methods](https://app.datadoghq.com/organization-settings/login-methods).
1. Set the **Require Multi-Factor Authentication** setting to `On` or `Off`, according to your organization's preference or policy requirements.
1. Confirm your selection.

Setting **Require Multi-Factor Authentication** to `On` has two effects:

- Users that log in with an email and password must register a second authentication factor before accessing the organization.
- In Login Methods, a link to [**View users without MFA**](https://app.datadoghq.com/organization-settings/users?filter%5Ballowed_login_methods%5D=standard&filter%5Bmfa_enabled%5D=false&filter%5Bstatus%5D=Active) appears. Click on the link to see the users list, filtered on users without MFA.

The setting to require multi-factor authentication is independent of the default login method settings. Regardless of which login methods you enable by default, enforcing MFA requires a second authentication factor for users that log in with an email and password.

## Reviewing user overrides{% #reviewing-user-overrides %}

Using overrides, you can change the available login methods for individual users. In the following example, **Sign in with Google** is Off by default in the organization, but one user has it enabled by having an override set.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/login_methods_enabled_off.2642430182dd63fa9db73d2fa4242d98.png?auto=format"
   alt="Login method disabled, with user override enabled" /%}

In [User Management](https://app.datadoghq.com/organization-settings/users), you can filter users by the override methods set, or view users who have the Default login methods enabled:

{% image
   source="https://datadog-docs.imgix.net/images/account_management/users/user_page_login_methods_override_view.4289845d3fa19c9c44522929dc7500c1.png?auto=format"
   alt="User Management view filtered to show users by login methods set." /%}

You can edit the user's overrides or remove the override altogether to allow the user to only use the defaults. For more information see [Edit a user's login methods](https://docs.datadoghq.com/account_management/users/#edit-a-users-login-methods).
