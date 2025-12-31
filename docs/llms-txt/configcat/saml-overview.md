# Source: https://configcat.com/docs/advanced/team-management/saml/saml-overview.md

# SAML SSO Overview

This section describes how you can enable SAML Single Sign-On (SSO) for your organization in ConfigCat.

SAML SSO allows your team members to sign up and log in to ConfigCat via their company accounts using your own Identity Provider (IdP).

Go to the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page to set up SAML SSO. You need to be an organization admin to do this.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Verified domain](https://configcat.com/docs/docs/advanced/team-management/domain-verification/.md)
  <br />
  <!-- -->
  In order to configure SAML, you have to verify the ownership of the domain that your company uses for email addresses. This step is required because, at the beginning of the login process, we use the user's email domain to select the appropriate SAML Identity Provider.
* Identity Provider that supports SAML 2.0

## Configure a SAML Identity Provider[​](#configure-a-saml-identity-provider "Direct link to Configure a SAML Identity Provider")

We tested and validated the following SAML Identity Providers:

* [Entra ID (Azure AD)](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/azure-ad/.md)
* [ADFS](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/adfs/.md)
* [Google](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/google/.md)
* [Okta](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/okta/.md)
* [Auth0](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/auth0/.md)
* [OneLogin](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/onelogin/.md)
* [Cloudflare Zero Trust](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/cloudflare/.md)

info

Other Identity Providers might also work with ConfigCat, if they support the SAML 2.0 protocol.

## Supported SAML flows[​](#supported-saml-flows "Direct link to Supported SAML flows")

* Identity Provider initiated SSO
* Service Provider initiated SSO

## SAML Requirements[​](#saml-requirements "Direct link to SAML Requirements")

These are the Identity Provider configuration requirements for ConfigCat:

* **Name ID**: ConfigCat only supports the email address in the `NameID` field.
* **Signature algorithm**: ConfigCat only supports the `RSA-SHA256` signature algorithm.
