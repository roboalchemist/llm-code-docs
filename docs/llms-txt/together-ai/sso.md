# Source: https://docs.together.ai/docs/sso.md

# Single Sign-On (SSO)

## What is SSO?

<Warning>
  SSO is only available for Scale and Enterprise accounts. If you would like to upgrade your account to use SSO please contact our [sales team](https://www.together.ai/contact-sales)
</Warning>

SSO enables a secure multi-member collaboration model within a single Together account. With SSO you can:

* Securely connect Together accounts with an existing Identity Provider (IdP). Our currently supported platforms include Google Workspace, Okta, Microsoft Entra, and JumpCloud.
* Onboard and offboard members through your IdP.
* Share access to organizational resources like fine-tuned models, inference analytics, and billing.

<Note>
  SSO is currently in early access. Fine-grained role-based access, spend controls, and multi-project support are on our roadmap and will be added to the SSO experience in the future.
</Note>

## Benefits of SSO

**Access the newest collaboration features:** SSO unlocks multi-member org features, including shared resources and billing. Upcoming capabilities like spend controls, granular permissions, and advanced analytics will only be available in SSO.

**Stronger security and compliance:** Individualized authentication via your IdP eliminates shared passwords, reduces risk, and makes onboarding/offboarding seamless.

## FAQs

### What does the setup process involve?

To get started, reach out to Customer Support or your Account Executive to let them know you'd like to enable SSO.

Please include the following information with your request:

* Legal company name
* Email domain(s) used by your team (e.g., @company.com)
* Identity Provider (IdP) (e.g., Google Workspace, Okta, etc.)
* Account to use as the initial owner (this should be the account with the most Together usage)

For detailed instructions on configuring your Identity Provider, see the provider-specific guides below:

| Provider         | Protocol | Setup Guide                                                                                                      |
| ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| Most IdPs        | SAML     | [SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#saml-\(most-idps\))                     |
| Most IdPs        | OIDC     | [OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#oidc-\(most-idps\))                     |
| Okta             | SAML     | [Okta SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#okta-saml)                         |
| Okta             | OIDC     | [Okta OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#okta-oidc)                         |
| Google Workspace | SAML     | [Google Workspace SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#google-workspace-saml) |
| Microsoft Entra  | SAML     | [Microsoft Entra SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#microsoft-entra-saml)   |
| Microsoft Entra  | OIDC     | [Microsoft Entra OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#microsoft-entra-oidc)   |

### How long does setup take?

If you have an existing account/contract with Together, we aim to have SSO fully set up within 24–48 working hours of receiving your request. Complex configurations may take longer.

### Why are we moving away from shared username/password enterprise sign on accounts?

Our legacy "enterprise sign-on" required teams to share a single username/password account. This approach has several downsides:

* **Security risk** – shared credentials increase the chance of unauthorized access.
* **No scalability** – no way to onboard/offboard at the individual level.
* **No collaboration** – all activity is tied to one account, making it impossible to eventually share work or manage usage by members.
* **No future features** – we are retiring enterprise sign-on within the next 1–2 months and will not roll out any new improvements to it.

Going forward, we will not be recommending enterprise sign-on as the default path for team collaboration.

### I have a shared username/password enterprise sign on account, why should I migrate?

Enterprise sign-on will be deprecated in the coming months. Migrating now can prevent disruptive and time-consuming manual transitions later when your team has accumulated models, analytics, and billing history that are difficult to re-map.

### Does Together use my IdP's default session timeout?

No, Together sessions will have their own session timeout.

### What features are on the roadmap for SSO?

The following features are commonly requested and are on our roadmap for the next year:

* Spend controls
* Fine-grained role-based access controls
* Multi-project support
* Multi-org support
* Self-configure SSO
* Domain ownership verification and organization privacy states


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt