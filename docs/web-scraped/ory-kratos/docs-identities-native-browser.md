# Source: https://www.ory.com/docs/identities/native-browser

Title: Browser vs. native apps | Ory

URL Source: https://www.ory.com/docs/identities/native-browser

Markdown Content:
Browser vs. native apps | Ory
===============

[Skip to main content](https://www.ory.com/docs/identities/native-browser#__docusaurus_skipToContent_fallback)

[![Image 1: Ory](https://www.ory.com/docs/img/logos/logo-light-mode.svg)](https://www.ory.com/)[Start](https://www.ory.com/docs/getting-started/overview)

[Products](https://www.ory.com/docs/identities/native-browser#)
*   [Ory Kratos Identities](https://www.ory.com/docs/identities)
*   [Ory Hydra OAuth2](https://www.ory.com/docs/oauth2-oidc)
*   [Ory Keto Permissions](https://www.ory.com/docs/keto)
*   [Ory Polis SAML](https://www.ory.com/docs/polis)
*   [Ory Oathkeeper Zero Trust](https://www.ory.com/docs/oathkeeper)
*   [Ory Enterprise License](https://www.ory.com/docs/self-hosted/oel)
*   [Ory Elements](https://www.ory.com/docs/elements)

[Manage](https://www.ory.com/docs/identities/native-browser#)
*   [Platform](https://www.ory.com/docs/guides/operations)
*   [Troubleshooting](https://www.ory.com/docs/category/troubleshooting)
*   [Security and compliance](https://www.ory.com/docs/security-compliance/compliance-and-certifications)

[Reference](https://www.ory.com/docs/identities/native-browser#)
*   [REST API](https://www.ory.com/docs/reference/api)
*   [Ory CLI](https://www.ory.com/docs/category/ory-cli-reference)
*   [Ory SDKs](https://www.ory.com/docs/sdk)
*   [Operations](https://www.ory.com/docs/category/operations-reference)

[Open Source](https://www.ory.com/docs/ecosystem/projects)

[Need Support?](https://www.ory.com/docs/identities/native-browser#)
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
    *   [OpenID Connect SSO](https://www.ory.com/docs/guides/oauth2-oidc) 
    *   [Flows](https://www.ory.com/docs/kratos/self-service) 
    *   [Session](https://www.ory.com/docs/kratos/session-management/overview) 
    *   [Multi-factor authentication](https://www.ory.com/docs/kratos/mfa/overview) 
    *   [Emails and SMS](https://www.ory.com/docs/guides/email-sms) 
    *   [Ory Actions](https://www.ory.com/docs/guides/integrate-with-ory-cloud-through-webhooks) 
    *   [Search](https://www.ory.com/docs/identities/native-browser#) 
    *   [Identity management](https://www.ory.com/docs/kratos/manage-identities/overview) 
    *   [Identity schema](https://www.ory.com/docs/kratos/manage-identities/identity-schema) 
    *   [User interface](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview) 

*   [Configuration](https://www.ory.com/docs/identities/native-browser) 
    *   [Two-step registration](https://www.ory.com/docs/identities/sign-in/two-step-registration)
    *   [Identifier first authentication](https://www.ory.com/docs/identities/sign-in/identifier-first-authentication)
    *   [Login hints](https://www.ory.com/docs/identities/sign-in/login-hint)
    *   [Login and registration actions](https://www.ory.com/docs/identities/sign-in/actions)
    *   [Code submissions limit](https://www.ory.com/docs/identities/sign-in/code-submission-limit)

*   [Self-Hosted](https://www.ory.com/docs/kratos/quickstart) 
    *   [Installation](https://www.ory.com/docs/kratos/install)
    *   [Quickstart](https://www.ory.com/docs/kratos/quickstart)
    *   [Configuration](https://www.ory.com/docs/identities/native-browser#) 
    *   [Guides](https://www.ory.com/docs/identities/native-browser#) 
    *   [Reference](https://www.ory.com/docs/identities/native-browser#) 

*   [Concepts](https://www.ory.com/docs/category/concepts)
*   Browser vs. native apps

On this page

Browser vs. native apps
=======================

Ory Identities supports both mobile (native) and browser applications. Because of the broad capabilities browsers offer, they pose a higher security risk than native applications. To shield your users from those risks, Ory Identities implements special browser APIs which use additional security measures such as anti-CSRF cookies.

Browser apps[​](https://www.ory.com/docs/identities/native-browser#browser-apps "Direct link to Browser apps")
--------------------------------------------------------------------------------------------------------------

Browser apps use the `https://$PROJECT_SLUG.projects.oryapis.com/self-service/{flow-type}/browser` endpoint to initialize flows such as sign in, registration, profile changes, and so on. When using this endpoint, Ory will set anti CSRF cookies.

When a user signs in successfully, Ory will issue an Ory Session Cookie. Calling `ory.toSession()` will return the same session but does not require any additional calls when used in client-side browser apps (for example React, Vue, Angular).

Native apps[​](https://www.ory.com/docs/identities/native-browser#native-apps "Direct link to Native apps")
-----------------------------------------------------------------------------------------------------------

Native apps use the `https://$PROJECT_SLUG.projects.oryapis.com/self-service/{flow-type}/api` endpoint to initialize flows such as sign in, registration, profile changes, and so on. When using this endpoint, no CSRF cookies will be issued by Ory.

Additionally, Ory issues an Ory Session Token instead of an Ory Session Cookie. This token is equivalent to the session cookie and returns the same session response when calling `ory.toSession({ xSessionToken: "{session-token}" })`.

Because it is very dangerous to use native app endpoints in a browser context, Ory prevents you from using these APIs in the browser.

[Edit this page](https://github.com/ory/docs/edit/master/docs/identities/native-browser.mdx)

Last updated on **Jun 17, 2024** by **Vincent**

[Previous Cookie-based security](https://www.ory.com/docs/security-model)[Next Browser redirects and flow completion](https://www.ory.com/docs/concepts/redirects)

*   [Browser apps](https://www.ory.com/docs/identities/native-browser#browser-apps)
*   [Native apps](https://www.ory.com/docs/identities/native-browser#native-apps)

### Ory Network

The best way to manage identities, authentication, authorization, and access control—designed for speed, security, and compliance.

[Sign up for a free account](https://console.ory.sh/?mtm_campaign=Docs-SideCta&mtm_kwd=variant-0)

[Need Support?](https://www.ory.com/support)·[Search](https://www.ory.com/docs/search)·[Status](https://status.ory.com/)·[Privacy](https://www.ory.com/legal/privacy)·[Company](https://www.ory.com/legal/company)·[Terms of Service](https://www.ory.com/legal/tos)·[Schedule a discovery call](https://www.ory.com/contact)·Consent Preferences

[![Image 2: Ory logo in white](https://www.ory.com/docs/img/logos/logo-dark-mode.svg)](https://www.ory.com/)

Copyright © 2026 Ory Corp

![Image 3: Project Logo](https://www.ory.com/docs/img/kapa-logo.png)

Ask AI

![Image 4](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=da01db86-5f5f-40b4-b062-c1188dff8662&bo=1&sid=c0100e401d3e11f1a8721f28a9f5987b&vid=c01045001d3e11f199e68b0f0b53ae5e&vids=1&msclkid=N&gtm_tag_source=1&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&tl=Browser%20vs.%20native%20apps%20%7C%20Ory&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fidentities%2Fnative-browser&r=&lt=760&evt=pageLoad&sv=2&cdb=AQAS&rn=806685)![Image 5](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=da01db86-5f5f-40b4-b062-c1188dff8662&bo=2&sid=c0100e401d3e11f1a8721f28a9f5987b&vid=c01045001d3e11f199e68b0f0b53ae5e&vids=0&msclkid=N&tpp=1&ea=Page%20View%20-%20All%20Pages%20(excluding%20console)&en=Y&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fidentities%2Fnative-browser&sw=800&sh=600&sc=24&evt=custom&cdb=AQAS&rn=204650)
