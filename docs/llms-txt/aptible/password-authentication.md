# Source: https://www.aptible.com/docs/core-concepts/security-compliance/authentication/password-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Password Authentication

Users can use password authentication as one of the authentication methods to access Aptible resources via the Dashboard and CLI.

# Requirements

Passwords must:

1. be at least 10 characters, and no more than 72 characters.
2. contain at least one uppercase letter (A-Z).
3. contain at least one lowercase letter (a-z).
4. include at least one digit or special character (^0-9!@#\$%^&\*()).

Aptible uses [Have I Been Pwned](https://haveibeenpwned.com) to implement a denylist of known compromised passwords.

# Account Lockout Policies

Aptible locks out users if there are:

1. 10 failed attempts in 1 minute result in a 1-minute lockout
2. 20 failed attempts in 1 hour result in a 1-hour lockout
3. 40 failed attempts in 1 day result in a 1-day lockout

Aptible monitors for repeat unsuccessful login attempts and notifies customers of any such repeat attempts that may signal an account takeover attempt. For granular control over login data, such as reviewing every login from your team members, set up [SSO](/core-concepts/security-compliance/authentication/sso) using a SAML provider, and [require SSO](/core-concepts/security-compliance/authentication/sso#require-sso-for-access) for accessing Aptible.

# 2-Factor Authentication (2FA)

Regardless of SSO usage or requirements, Aptible strongly recommends using 2FA to protect your Aptible account and all other sensitive internet accounts.

# 2-Factor Authentication With SSO

When SSO is enabled for your organization, it is not possible to both require that members of your organization have 2-Factor Authentication enabled, and use SSO at the same time.  However, you can require that they login with SSO in order to access your organization’s resources and enforce rules such as requiring 2FA via your SSO provider.

If you’re interested in enabling SSO for your organization contact [Aptible Support](https://app.aptible.com/support).

## Enrollment

Users can enable 2FA Authentication in the Dashboard by navigating to Settings > Security Settings > Configure 2FA.

## Supported Protocols

Aptible supports:

1. software second factors via the TOTP protocol. We recommend using [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en) as your TOTP client
2. hardware second factors via the FIDO protocol.

## Scope

When enabled, 2FA protects access to your Aptible account via the Dashboard, CLI, and API. 2FA does not restrict Git pushes - these are still authenticated with [SSH Public Keys](/core-concepts/security-compliance/authentication/ssh-keys). Sometimes, you may not push code with your user credentials, for example, if you deploy with a CI service such as Travis or Circle that performs all deploys via a robot user. If so, we encourage you to remove SSH keys from your Aptible user account.

Aptible 2FA protects logins, not individual requests. Making authenticated requests to the Aptible API is a two-step process:

1. generate an access token using your credentials
2. use that access token to make requests

2FA protects the first step. Once you have an access token, you can make as many requests as you want to the API until that token expires or is revoked.

## Recovering Account Access

Account owners can [reset 2FA for all other users](/how-to-guides/platform-guides/reset-aptible-2fa), including other account owners, but cannot reset their own 2FA.

## Auditing

[Organization](/core-concepts/security-compliance/access-permissions) administrators can audit 2FA enrollment via the Dashboard by navigating to Settings > Members.
