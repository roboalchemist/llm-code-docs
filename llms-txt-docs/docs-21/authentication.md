# Source: https://docs.unifygtm.com/reference/management/authentication.md

# Authentication Options

> Learn about the login methods available for your organization in Unify.

## Overview

Unify supports the following forms of authentication:

1. **Username and Password**: Users can log in with an email address and password managed by Unify.

2. **Google Workspace**: Users can log in using a Google account associated with your organization's Google Workspace.

3. **Single Sign-On (SSO) via SAML 2.0**: For enterprise customers, Unify supports SSO through the SAML 2.0 protocol. This allows your organization to use your existing identity provider (IdP), such as Okta or Azure AD, to authenticate your users.

All methods are powered by Auth0, the leading industry standard for secure authentication.

### Single Sign-On (SSO)

Our team will work directly with you to integrate Unify with your identify provider. Below are the steps and information we'll cover during this process.

#### Supported Identity Providers (IdPs)

* Okta
* Azure Active Directory (AD)
* Any SAML 2.0 compliant IdP

#### Information required for SSO setup

* **Sign In URL**: The URL where SAML authentication requests are sent. This is also called the single sign-on (SSO) endpoint.
* **Sign Out URL**: The URL where SAML logout requests are sent. This is also called the single logout (SLO) endpoint.
* **X.509 Certificate**: A certificate used to verify the SAML response.
