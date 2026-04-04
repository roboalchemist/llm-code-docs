# Source: https://www.ory.com/docs/kratos/concepts/credentials

Title: Credentials | Ory

URL Source: https://www.ory.com/docs/kratos/concepts/credentials

Published Time: Wed, 11 Mar 2026 11:38:19 GMT

Markdown Content:
Credentials | Ory
===============

[Skip to main content](https://www.ory.com/docs/kratos/concepts/credentials#__docusaurus_skipToContent_fallback)

[![Image 1: Ory](https://www.ory.com/docs/img/logos/logo-light-mode.svg)](https://www.ory.com/)[Start](https://www.ory.com/docs/getting-started/overview)

[Products](https://www.ory.com/docs/kratos/concepts/credentials#)
*   [Ory Kratos Identities](https://www.ory.com/docs/identities)
*   [Ory Hydra OAuth2](https://www.ory.com/docs/oauth2-oidc)
*   [Ory Keto Permissions](https://www.ory.com/docs/keto)
*   [Ory Polis SAML](https://www.ory.com/docs/polis)
*   [Ory Oathkeeper Zero Trust](https://www.ory.com/docs/oathkeeper)
*   [Ory Enterprise License](https://www.ory.com/docs/self-hosted/oel)
*   [Ory Elements](https://www.ory.com/docs/elements)

[Manage](https://www.ory.com/docs/kratos/concepts/credentials#)
*   [Platform](https://www.ory.com/docs/guides/operations)
*   [Troubleshooting](https://www.ory.com/docs/category/troubleshooting)
*   [Security and compliance](https://www.ory.com/docs/security-compliance/compliance-and-certifications)

[Reference](https://www.ory.com/docs/kratos/concepts/credentials#)
*   [REST API](https://www.ory.com/docs/reference/api)
*   [Ory CLI](https://www.ory.com/docs/category/ory-cli-reference)
*   [Ory SDKs](https://www.ory.com/docs/sdk)
*   [Operations](https://www.ory.com/docs/category/operations-reference)

[Open Source](https://www.ory.com/docs/ecosystem/projects)

[Need Support?](https://www.ory.com/docs/kratos/concepts/credentials#)
*   [Enterprise Support](https://www.ory.com/support)
*   [Search the docs](https://www.ory.com/docs/search)
*   [Ory Community Slack](https://slack.ory.com/)
*   [GitHub Discussions](https://github.com/orgs/ory/discussions)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/ory)
*   [Schedule a discovery call](https://www.ory.com/contact)

[GitHub](https://github.com/ory)

Search

*   [Go to Start Page](https://www.ory.com/docs/welcome)
*   [Introduction](https://www.ory.com/docs/identities)
*   [Get Started](https://www.ory.com/docs/identities/get-started) 
*   [Concepts](https://www.ory.com/docs/category/concepts) 
    *   [Cookie-based security](https://www.ory.com/docs/security-model)
    *   [Browser vs. native apps](https://www.ory.com/docs/identities/native-browser)
    *   [Browser redirects and flow completion](https://www.ory.com/docs/concepts/redirects)
    *   [Ory Actions](https://www.ory.com/docs/kratos/hooks/configure-hooks)

*   [Guides](https://www.ory.com/docs/category/guides) 
    *   [Authentication](https://www.ory.com/docs/guides/authentication) 
        *   [Credentials](https://www.ory.com/docs/kratos/concepts/credentials)
        *   [Password](https://www.ory.com/docs/kratos/concepts/credentials/username-email-password)
        *   [Passwordless](https://www.ory.com/docs/kratos/passwordless/passwordless)
        *   [Passwordless email & SMS](https://www.ory.com/docs/kratos/passwordless/one-time-code)
        *   [Passkeys & WebAuthN](https://www.ory.com/docs/kratos/passwordless/passkeys)
        *   [Passkeys for mobile](https://www.ory.com/docs/kratos/passwordless/passkeys-mobile-web-implementation)
        *   [Organizations](https://www.ory.com/docs/kratos/organizations)
        *   [Email templates](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates)

    *   [OpenID Connect SSO](https://www.ory.com/docs/guides/oauth2-oidc) 
    *   [Flows](https://www.ory.com/docs/kratos/self-service) 
    *   [Session](https://www.ory.com/docs/kratos/session-management/overview) 
    *   [Multi-factor authentication](https://www.ory.com/docs/kratos/mfa/overview) 
    *   [Emails and SMS](https://www.ory.com/docs/guides/email-sms) 
    *   [Ory Actions](https://www.ory.com/docs/guides/integrate-with-ory-cloud-through-webhooks) 
    *   [Search](https://www.ory.com/docs/kratos/concepts/credentials#) 
    *   [Identity management](https://www.ory.com/docs/kratos/manage-identities/overview) 
    *   [Identity schema](https://www.ory.com/docs/kratos/manage-identities/identity-schema) 
    *   [User interface](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview) 

*   [Configuration](https://www.ory.com/docs/kratos/concepts/credentials) 
    *   [Two-step registration](https://www.ory.com/docs/identities/sign-in/two-step-registration)
    *   [Identifier first authentication](https://www.ory.com/docs/identities/sign-in/identifier-first-authentication)
    *   [Login hints](https://www.ory.com/docs/identities/sign-in/login-hint)
    *   [Login and registration actions](https://www.ory.com/docs/identities/sign-in/actions)
    *   [Code submissions limit](https://www.ory.com/docs/identities/sign-in/code-submission-limit)

*   [Self-Hosted](https://www.ory.com/docs/kratos/quickstart) 
    *   [Installation](https://www.ory.com/docs/kratos/install)
    *   [Quickstart](https://www.ory.com/docs/kratos/quickstart)
    *   [Configuration](https://www.ory.com/docs/kratos/concepts/credentials#) 
    *   [Guides](https://www.ory.com/docs/kratos/concepts/credentials#) 
    *   [Reference](https://www.ory.com/docs/kratos/concepts/credentials#) 

*   [Guides](https://www.ory.com/docs/category/guides)
*   [Authentication](https://www.ory.com/docs/guides/authentication)
*   Credentials

Credentials
===========

Each identity has one or more credentials associated with it:

`credentials:  password:    id: password    identifiers:      - john.doe@acme.com      - johnd@ory.com    config:      hashed_password: ...  oidc:    id: oidc    identifiers:      - google:j8kf7a3...      - facebook:83475891...    config:      - provider: google        identifier: j8kf7a3      - provider: facebook        identifier: 83475891`

Ory Kratos supports several credential types:

*   `password`: The most common identifier (username, email, ...) + password credential.
*   `passkey`: Passkeys use WebAuthn standards for secure, user-friendly, and cryptographic passwordless authentication.
*   `code`: The "Log in via email or SMS" credential using a one-time code.
*   `oidc`: The "Log in with Google/Facebook/GitHub/..." credential using OpenID Connect.
*   `saml`: A standard for exchanging auth data between parties, often used for B2B SSO.
*   `webauthn`: The same technology as Passkeys used as a second factor.
*   `totp`: Time-based one-time passwords generated by authenticator apps, used as a second factor.
*   `lookup_secret`: One-time codes used as a recovery mechanism for 2FA when the primary second factor is unavailable.

Each credential - regardless of its type - has one or more identifiers attached to it. Each identifier is universally unique. Assuming we had one identity with credentials

`credentials:  password:    id: password    identifiers:      - john.doe@acme.com`

and tried to create (or update) another identity with the same identifier (`john.doe@acme.com`), the system would reject the request with a 409 Conflict state.

While credentials must be unique per type, there can be duplicates amongst multiple types:

`# This is ok:credentials:  password:    id: password    identifiers:      - john.doe@acme.com  oidc:    id: oidc    identifiers:      - john.doe@acme.com`

The same would apply if those were two separate identities:

`# Identity 1credentials:  password:    id: password    identifiers:      - john.doe@acme.com---# Identity 2credentials:  oidc:    id: oidc    identifiers:      - john.doe@acme.com`

[Edit this page](https://github.com/ory/docs/edit/master/docs/kratos/concepts/credentials.mdx)

Last updated on **Oct 15, 2025** by **unatasha8**

[Previous Authentication](https://www.ory.com/docs/guides/authentication)[Next Password](https://www.ory.com/docs/kratos/concepts/credentials/username-email-password)

[Need Support?](https://www.ory.com/support)·[Search](https://www.ory.com/docs/search)·[Status](https://status.ory.com/)·[Privacy](https://www.ory.com/legal/privacy)·[Company](https://www.ory.com/legal/company)·[Terms of Service](https://www.ory.com/legal/tos)·[Schedule a discovery call](https://www.ory.com/contact)·Consent Preferences

[![Image 2: Ory logo in white](https://www.ory.com/docs/img/logos/logo-dark-mode.svg)](https://www.ory.com/)

Copyright © 2026 Ory Corp

![Image 3: Project Logo](https://www.ory.com/docs/img/kapa-logo.png)

Ask AI

![Image 4](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=f9116910-7d6a-45d5-b353-d58b0f903d4c&bo=1&sid=d1341ac01d3e11f1b64645e7814e7c5e&vid=d13425201d3e11f1927b773088793fa1&vids=1&msclkid=N&gtm_tag_source=1&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&tl=Credentials%20%7C%20Ory&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fkratos%2Fconcepts%2Fcredentials&r=&lt=3185&evt=pageLoad&sv=2&cdb=AQAS&rn=386556)![Image 5](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=f9116910-7d6a-45d5-b353-d58b0f903d4c&bo=2&sid=d1341ac01d3e11f1b64645e7814e7c5e&vid=d13425201d3e11f1927b773088793fa1&vids=0&msclkid=N&tpp=1&ea=Page%20View%20-%20All%20Pages%20(excluding%20console)&en=Y&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fkratos%2Fconcepts%2Fcredentials&sw=800&sh=600&sc=24&evt=custom&cdb=AQAS&rn=46231)
