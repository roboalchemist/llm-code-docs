# Source: https://docs.datadoghq.com/account_management/saml/activedirectory.md

---
title: Microsoft Active Directory Federation Services SAML IdP
description: >-
  Configure Microsoft Active Directory Federation Services as a SAML identity
  provider for Datadog with user management and authentication setup.
breadcrumbs: >-
  Docs > Account Management > Single Sign On With SAML > Microsoft Active
  Directory Federation Services SAML IdP
---

# Microsoft Active Directory Federation Services SAML IdP

The Datadog SAML integration for SSO provides a pathway for linking an organization to an external user management system so that credentials can be kept and managed in a central system. This doc is meant to be used as an add-on to the main [Single Sign On With SAML](https://docs.datadoghq.com/account_management/saml/) documentation, which gives an overview of single sign-on from the Datadog perspective.

To begin configuration of SAML for Active Directory Federation Service (AD FS), see Microsoft's [Configure a SAML 2.0 provider for portals with AD FS](https://docs.microsoft.com/en-us/powerapps/maker/portals/configure/configure-saml2-settings) docs.

Once SAML is configured, users can login by using the link provided in the [SAML configuration page](https://app.datadoghq.com/saml/saml_setup). Keep in mind that users still need to be invited and activated before they're able to login. Be sure to invite new users by using the email address corresponding to their Active Directory user records; otherwise they may be denied as shown below.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/6TsPUla.4d90e3aa8f06065ba250f9237a3a35e5.png?auto=format"
   alt="6TsPUla" /%}

In most setups, a user's `user@domain` is their Microsoft login, but this is not enforced. You can confirm the email address used within the user record as shown below.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/0R81SaK.3a013f31e3d21dea0924e929245dfb3b.png?auto=format"
   alt="0R81SaK" /%}

For questions regarding Datadog in-app errors pertaining to SAML, contact [the Datadog support team](https://docs.datadoghq.com/help/). For errors pertaining to AD FS SAML setup and errors, contact [Microsoft support](https://powerapps.microsoft.com/en-us/support/).

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
- [Configuring Teams & Organizations with Multiple Accounts](https://docs.datadoghq.com/account_management/multi_organization/)
