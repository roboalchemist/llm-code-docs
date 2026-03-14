# Source: https://docs.snowflake.com/en/user-guide/opencatalog/sso-overview.md

# Overview of SSO in Snowflake Open Catalog

This topic describes single sign-on (SSO) for Snowflake Open Catalog. SSO for Open Catalog lets you integrate Open Catalog with a third-party
identity provider. This integration lets users sign in to the Open Catalog web application by using existing credentials managed by an identity provider
(IdP), so you don’t have to manage separate usernames and passwords in Open Catalog.

SSO for Open Catalog supports signing in and out of the Open Catalog UI and timing out the system due to inactivity.

## Supported identity providers

Open Catalog supports SSO for the following identity providers (IdPs):

* Auth0
* Okta
* Any other SAML-based IdP

The steps for configuring any other SAML-based IdP are similar to [configuring Auth0](sso-configure-idp.md) or
[configuring Okta](sso-configure-idp.md).

## Security integration support

Only SAML is supported.

A Snowflake security integration is an account-level object. You use the security integration to integrate with the IdP you are using to
implement SSO. For more information, see [CREATE SECURITY INTEGRATION (SAML2)](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-saml2).

You can only use one SAML integration at a time. To see which one is enabled, see [Verify the security integration](sso-configure-open-catalog.md).

## Configuring SSO for Open Catalog

A service admin in Open Catalog can set up SSO by following these steps:

1. [Configure an identity provider (IdP) for Snowflake Open Catalog](sso-configure-idp.md). During this process, you generate values that
   you need to configure SSO in Open Catalog.
2. [Configure Snowflake Open Catalog to use SSO](sso-configure-open-catalog.md).
