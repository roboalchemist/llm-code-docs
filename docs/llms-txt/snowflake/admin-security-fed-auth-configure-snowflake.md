# Source: https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-configure-snowflake.md

# Migrating to a SAML2 security integration

> **Important:**
>
> The [SAML_IDENTITY_PROVIDER](../sql-reference/parameters.md) and [SSO_LOGIN_PAGE](../sql-reference/parameters.md) parameters used for SAML SSO configuration and management are
> deprecated. Snowflake configurations should use a
> [SAML2 security integration](admin-security-fed-auth-security-integration.md) instead of these parameters.
>
> Snowflake will continue to support these deprecated parameters as long as there are implementations that use them.

If you are implementing federated authentication for the first time, refer to
[Configuring Snowflake to use federated authentication](admin-security-fed-auth-security-integration.md).

If you have an existing SSO implementation that uses the SAML_IDENTITY_PROVIDER account parameter, follow the steps below to migrate your
SSO implementation to a SAML2 security integration:

1. Run the [SYSTEM$MIGRATE_SAML_IDP_REGISTRATION](../sql-reference/functions/system_migrate_saml_idp_registration.md) function.
2. Confirm that a SAML2 security integration was created by running the following SQL statement:

   > ```sqlexample
   > desc security integration <integration_name>;
   > ```

If you want to configure your security integration, refer to [Configuring Snowflake to use federated authentication](admin-security-fed-auth-security-integration.md).
