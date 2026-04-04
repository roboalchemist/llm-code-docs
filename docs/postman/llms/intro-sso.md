# Intro to SSO

**[SSO is available with Postman Enterprise plans.](https://www.postman.com/pricing/)**

Single sign-on (SSO) services enable you to manage your team’s identity across all the SaaS products that you use.

With an SSO service, a user can access multiple applications using one set of credentials (for example, an email address and password). The SSO service authenticates the user once for all the applications the user has been given rights to and eliminates further prompts when the user switches applications during the same session.

An example of SSO is Google's sign-in implementation for products like Gmail, YouTube, and Google Drive. Any user who is signed in to one of Google's products is automatically signed in to their other products as well.

## What are the advantages of SSO?

* Removes the need for users to remember and manage multiple passwords.
* Simplifies users’ experience by enabling them to sign in at a single access point and work seamlessly across multiple applications.
* Increases productivity by reducing the password-related support emails.
* Reduces phishing attempts that try to trick users into giving away sensitive information.

## Prerequisites for SSO with Postman

* Team’s identity provider (IdP) must support the SAML 2.0 standard.

## Supported IdPs

* [Microsoft AD FS](/docs/administration/sso/microsoft-adfs/)
* [Microsoft Entra ID](/docs/administration/sso/azure-ad/)
* [Custom SAML](/docs/administration/sso/custom-saml/)
* [Duo](/docs/administration/sso/duo/)
* [Google Workspace](/docs/administration/sso/google-workspace/)
* [Okta](/docs/administration/sso/okta/)
* [OneLogin](/docs/administration/sso/onelogin/)
* [Ping Identity](/docs/administration/sso/ping-identity/)

## SSO setup for SAML 2.0 compliant IdPs

Most SAML 2.0 compliant identity providers require the same information about the service provider for setup (Postman is the service provider). These values are specific to a Postman team and are available while [configuring SSO](/docs/administration/sso/admin-sso/).

While configuring your IdP, make sure to set your users' email address in SAML attributes and claims. Postman expects to receive an email address from your IdP to identify each user.

If you configure SSO, Postman Password, Google OAuth 2.0, and GitHub authentication methods remain enabled for your team. You can turn off these authentication methods to allow your team to sign in using SSO only.

## Learn more

To learn more about SSO and SCIM, see the following:

* [Sign in to an SSO team](/docs/administration/sso/user-sso/) - How to sign in and use SSO when it’s enabled for your team.
* [Configure SSO for a team](/docs/administration/sso/admin-sso/) - How Team Admins can enable and configure SSO for team users.
* [SCIM (System for Cross-domain Identity Management) provisioning](/docs/administration/scim-provisioning/scim-provisioning-overview/) - How Team Admins can use SCIM to automate user provisioning and de-provisioning for a team.
* [SSO and SCIM FAQs](/docs/administration/sso/sso-faqs/) - Frequently asked questions on configuring SSO and SCIM.