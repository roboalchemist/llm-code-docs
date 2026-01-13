# Source: https://docs.datadoghq.com/account_management/saml/auth0.md

---
title: Auth0 SAML IdP
description: >-
  Configure Auth0 as a SAML identity provider for Datadog with user metadata and
  profile attribute management for secure authentication.
breadcrumbs: Docs > Account Management > Single Sign On With SAML > Auth0 SAML IdP
source_url: https://docs.datadoghq.com/saml/auth0/index.html
---

# Auth0 SAML IdP

## Setup and configuration{% #setup-and-configuration %}

Follow the [Configure Auth0 as Identity Provider for Datadog](https://auth0.com/docs/protocols/saml-protocol/saml-configuration-options/configure-auth0-as-identity-provider-for-datadog) docs to configure Auth0 as a SAML identity provider.

## Additional information{% #additional-information %}

`first_name` and `give_name` are root attributes of an Auth0 user. These can only be set upon creation with Auth0 Management API. See [Normalized User Profiles](https://auth0.com/docs/users/normalized/auth0#normalized-user-profile-schema) for reference.

The `user_metadata` section of the user profile is used to specify additional user information, for example:

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/auth0_metadata.2bad9d3c8e49ab28d8d56b6a74bef0fe.png?auto=format"
   alt="Update this" /%}

## Further Reading{% #further-reading %}

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
