# Source: https://www.ory.com/docs/account-experience

Title: Account Experience Overview | Ory

URL Source: https://www.ory.com/docs/account-experience

Markdown Content:
Account Experience Overview | Ory
===============

[Skip to main content](https://www.ory.com/docs/account-experience#__docusaurus_skipToContent_fallback)

[![Image 1: Ory](https://www.ory.com/docs/img/logos/logo-light-mode.svg)](https://www.ory.com/)[Start](https://www.ory.com/docs/getting-started/overview)

[Products](https://www.ory.com/docs/account-experience#)
*   [Ory Kratos Identities](https://www.ory.com/docs/identities)
*   [Ory Hydra OAuth2](https://www.ory.com/docs/oauth2-oidc)
*   [Ory Keto Permissions](https://www.ory.com/docs/keto)
*   [Ory Polis SAML](https://www.ory.com/docs/polis)
*   [Ory Oathkeeper Zero Trust](https://www.ory.com/docs/oathkeeper)
*   [Ory Enterprise License](https://www.ory.com/docs/self-hosted/oel)
*   [Ory Elements](https://www.ory.com/docs/elements)

[Manage](https://www.ory.com/docs/account-experience#)
*   [Platform](https://www.ory.com/docs/guides/operations)
*   [Troubleshooting](https://www.ory.com/docs/category/troubleshooting)
*   [Security and compliance](https://www.ory.com/docs/security-compliance/compliance-and-certifications)

[Reference](https://www.ory.com/docs/account-experience#)
*   [REST API](https://www.ory.com/docs/reference/api)
*   [Ory CLI](https://www.ory.com/docs/category/ory-cli-reference)
*   [Ory SDKs](https://www.ory.com/docs/sdk)
*   [Operations](https://www.ory.com/docs/category/operations-reference)

[Open Source](https://www.ory.com/docs/ecosystem/projects)

[Need Support?](https://www.ory.com/docs/account-experience#)
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
    *   [Search](https://www.ory.com/docs/account-experience#) 
    *   [Identity management](https://www.ory.com/docs/kratos/manage-identities/overview) 
    *   [Identity schema](https://www.ory.com/docs/kratos/manage-identities/identity-schema) 
    *   [User interface](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview) 
        *   [Account Experience](https://www.ory.com/docs/account-experience)
        *   [Configure Ory to use your UI](https://www.ory.com/docs/kratos/bring-your-own-ui/configure-ory-to-use-your-ui)
        *   [When to use custom UI?](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-vs-built-in-ui)
        *   [Ory Elements](https://www.ory.com/docs/elements)
        *   [Build your own UI](https://www.ory.com/docs/getting-started/custom-ui) 

*   [Configuration](https://www.ory.com/docs/account-experience) 
    *   [Two-step registration](https://www.ory.com/docs/identities/sign-in/two-step-registration)
    *   [Identifier first authentication](https://www.ory.com/docs/identities/sign-in/identifier-first-authentication)
    *   [Login hints](https://www.ory.com/docs/identities/sign-in/login-hint)
    *   [Login and registration actions](https://www.ory.com/docs/identities/sign-in/actions)
    *   [Code submissions limit](https://www.ory.com/docs/identities/sign-in/code-submission-limit)

*   [Self-Hosted](https://www.ory.com/docs/kratos/quickstart) 
    *   [Installation](https://www.ory.com/docs/kratos/install)
    *   [Quickstart](https://www.ory.com/docs/kratos/quickstart)
    *   [Configuration](https://www.ory.com/docs/account-experience#) 
    *   [Guides](https://www.ory.com/docs/account-experience#) 
    *   [Reference](https://www.ory.com/docs/account-experience#) 

*   [Guides](https://www.ory.com/docs/category/guides)
*   [User interface](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview)
*   Account Experience

On this page

Account Experience Overview
===========================

The Ory Account Experience is the default user interface for all self-service screens like login, registration, or consent. It can be accessed under `https://your-slug.projects.oryapis.com/login`. New Ory Network projects are automatically configured to use the Account Experience. You can find various customizations and settings in the Ory Console under `Account Experience`.

Theming[​](https://www.ory.com/docs/account-experience#theming "Direct link to Theming")
----------------------------------------------------------------------------------------

The Account Experience can be themed using the Ory Console. Head over to the [theming settings](https://console.ory.sh/projects/current/account-experience/theming). It is also possible to set a custom logo and favicon.

Translations (i18n) & Message Customization[​](https://www.ory.com/docs/account-experience#translations-i18n--message-customization "Direct link to Translations (i18n) & Message Customization")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Ory Account Experience is available in 83 languages.

Full list of supported languages

*   Afrikaans (`af`)
*   Akan (`ak`)
*   Amharic (`am`)
*   Arabic (`ar`)
*   Assamese (`as`)
*   Azerbaijani (Latin) (`az`)
*   Belarusian (`be`)
*   Bulgarian (`bg`)
*   Bamanankan (`bm`)
*   Bangla (`bn`)
*   Catalan (`ca`)
*   Czech (`cs`)
*   Danish (`da`)
*   German (`de`)
*   Greek (`el`)
*   English (`en`)
*   Spanish (`es`)
*   Estonian (`et`)
*   Persian (`fa`)
*   Finnish (`fi`)
*   French (`fr`)
*   Gujarati (`gu`)
*   Hausa (Latin) (`ha`)
*   Hebrew (`he`)
*   Hindi (`hi`)
*   Croatian (`hr`)
*   Hungarian (`hu`)
*   Armenian (`hy`)
*   Indonesian (`id`)
*   Igbo (`ig`)
*   Italian (`it`)
*   Japanese (`ja`)
*   Georgian (`ka`)
*   Kazakh (`kk`)
*   Khmer (`km`)
*   Kannada (`kn`)
*   Korean (`ko`)
*   Central Kurdish (`ku`)
*   Kyrgyz (`ky`)
*   Lithuanian (`lt`)
*   Latvian (`lv`)
*   Macedonian (`mk`)
*   Malayalam (`ml`)
*   Mongolian (Cyrillic) (`mn`)
*   Marathi (`mr`)
*   Malay (`ms`)
*   Burmese (`my`)
*   Nepali (`ne`)
*   Dutch (`nl`)
*   Norwegian (Bokmal) (`no`)
*   Odia (`or`)
*   Punjabi (`pa`)
*   Polish (`pl`)
*   Pashto (`ps`)
*   Portuguese (`pt`)
*   Romanian (`ro`)
*   Russian (`ru`)
*   Sindhi (`sd`)
*   Sinhala (`si`)
*   Slovak (`sk`)
*   Slovenian (`sl`)
*   Somali (`so`)
*   Albanian (`sq`)
*   Serbian (Latin) (`sr`)
*   Sundanese (`su`)
*   Swedish (`sv`)
*   Kiswahili (`sw`)
*   Tamil (`ta`)
*   Telugu (`te`)
*   Tajik (Cyrillic) (`tg`)
*   Thai (`th`)
*   Turkmen (`tk`)
*   Tagalog (`tl`)
*   Turkish (`tr`)
*   Uyghur (`ug`)
*   Ukrainian (`uk`)
*   Urdu (`ur`)
*   Uzbek (Latin) (`uz`)
*   Vietnamese (`vi`)
*   Xhosa (`xh`)
*   Yoruba (`yo`)
*   Chinese (Simplified) (`zh`)
*   Zulu (`zu`)

The source is available in the [GitHub repository of Ory Elements](https://github.com/ory/elements/tree/main/packages/elements-react/src/locales).

To determine the language to use, the Account Experience uses the `Accept-Language` header. If the language isn't available, the fallback language (English) is used. Custom translations are supported as well, use the edit button next to the language to override the default translations.

Custom Domains[​](https://www.ory.com/docs/account-experience#custom-domains "Direct link to Custom Domains")
-------------------------------------------------------------------------------------------------------------

The Account Experience is also available under custom domains the same way it works on the slug URL.

[Edit this page](https://github.com/ory/docs/edit/master/docs/account-experience/index.mdx)

Last updated on **Jan 12, 2026** by **Parth**

[Previous Overview](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview)[Next Configure Ory to use your UI](https://www.ory.com/docs/kratos/bring-your-own-ui/configure-ory-to-use-your-ui)

*   [Theming](https://www.ory.com/docs/account-experience#theming)
*   [Translations (i18n) & Message Customization](https://www.ory.com/docs/account-experience#translations-i18n--message-customization)
*   [Custom Domains](https://www.ory.com/docs/account-experience#custom-domains)

### Ory Network

The best way to manage identities, authentication, authorization, and access control—designed for speed, security, and compliance.

[Sign up for a free account](https://console.ory.sh/?mtm_campaign=Docs-SideCta&mtm_kwd=variant-0)

[Need Support?](https://www.ory.com/support)·[Search](https://www.ory.com/docs/search)·[Status](https://status.ory.com/)·[Privacy](https://www.ory.com/legal/privacy)·[Company](https://www.ory.com/legal/company)·[Terms of Service](https://www.ory.com/legal/tos)·[Schedule a discovery call](https://www.ory.com/contact)·Consent Preferences

[![Image 2: Ory logo in white](https://www.ory.com/docs/img/logos/logo-dark-mode.svg)](https://www.ory.com/)

Copyright © 2026 Ory Corp

![Image 3: Project Logo](https://www.ory.com/docs/img/kapa-logo.png)

Ask AI

![Image 4](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=244ccb47-bd5e-499e-b303-559928134acd&bo=1&sid=e2afd6f01d3e11f18268954b904ba03a&vid=e2afc8a01d3e11f190bf87c99f0a712d&vids=1&msclkid=N&gtm_tag_source=1&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&tl=Account%20Experience%20Overview%20%7C%20Ory&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Faccount-experience&r=&lt=908&evt=pageLoad&sv=2&cdb=AQAS&rn=946774)![Image 5](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=244ccb47-bd5e-499e-b303-559928134acd&bo=2&sid=e2afd6f01d3e11f18268954b904ba03a&vid=e2afc8a01d3e11f190bf87c99f0a712d&vids=0&msclkid=N&tpp=1&ea=Page%20View%20-%20All%20Pages%20(excluding%20console)&en=Y&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Faccount-experience&sw=800&sh=600&sc=24&evt=custom&cdb=AQAS&rn=858012)
