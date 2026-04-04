# Source: https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-security-integration-multiple.md

# Using multiple identity providers for federated authentication

You can configure Snowflake to allow users to authenticate with multiple identity providers (IdPs).

Implementing a federated environment that uses multiple IdPs consists of the following steps:

1. Enable the identifier-first login flow (in this topic).
2. [Configure each identity provider](admin-security-fed-auth-configure-idp.md).
3. [Create multiple SAML security integrations](admin-security-fed-auth-security-integration.md), one for each IdP.
4. Associate users with IdPs (in this topic).

> **Note:**
>
> Keep the following in mind as you implement an environment using multiple IdPs:
>
> * Each IdP must have a corresponding SAML security integration. If you have an existing single-IdP environment that uses the deprecated
>   SAML_IDENTITY_PROVIDER parameter, you must use the [SYSTEM$MIGRATE_SAML_IDP_REGISTRATION](../sql-reference/functions/system_migrate_saml_idp_registration.md) function to
>   migrate it to a SAML security integration.
> * Currently, only a subset of Snowflake drivers support the use of multiple identity providers. These drivers include JDBC, ODBC, and Python.

## Enable identifier-first login

When the federated environment for an account uses multiple IdPs, Snowflake must be able to determine which IdPs are associated with a user
*before* presenting the user with authentication options. In this flow, Snowflake prompts the user for only their email address or username,
then displays authentication methods after identifying the user. Only IdPs associated with the user appear as authentication options.

The identifier-first login flow must be enabled if you are using multiple IdPs. To enable identifier-first login, set the
[ENABLE_ICEBERG_MERGE_ON_READ](../sql-reference/parameters.md) parameter to `TRUE`:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Projects » Worksheets.
3. Execute the following SQL statements:

   ```sqlexample
   USE ROLE ACCOUNTADMIN;
   ALTER ACCOUNT SET ENABLE_IDENTIFIER_FIRST_LOGIN = true;
   ```

For more information about the identifier-first login flow, see [Identifier-first login](identifier-first-login.md).

## Associate users with IdPs

In an environment with multiple IdPs, you can choose how you want to associate a user with an IdP. You can use the security integration
associated with an IdP, an authentication policy, or combine the two methods.

Security Integration:
:   Use the `ALLOWED_USER_DOMAINS` and `ALLOWED_EMAIL_PATTERNS` properties of the SAML2 security integration associated with each
    IdP. In this configuration, a user only sees an IdP as an authentication option if their `EMAIL` matches an email address domain or
    pattern in the security integration.

Authentication Policy:
:   Use the `SECURITY_INTEGRATIONS` property of an [authentication policy](authentication-policies.md) to specify which
    security integrations are available to the user. In this configuration, the authentication policy is assigned to an entire account or an
    individual user. A user can only authenticate with IdPs associated with security integrations that are specified in the authentication
    policy.

    If you want a user to only see the identity providers that they are allowed to use, create multiple authentication policies and then
    assign the appropriate policy to a user.

    For an example of using an authentication policy to implement multiple IdPs, see [Allow authentication from multiple identity providers on an account](authentication-policies.md).

Combined:
:   You can combine the security integration and authentication policy methods to further refine how users authenticate in an environment that
    has multiple IdPs.

    If you use both methods, Snowflake first evaluates which security integrations are associated with the authentication policy governing the
    user’s login. Once Snowflake has identified the security integrations, the user’s `EMAIL` is matched to one of the integrations
    based on the `ALLOWED_USER_DOMAINS` and `ALLOWED_EMAIL_PATTERNS` properties. Snowflake only displays the IdP option for the
    security integration that matches the user’s `EMAIL`.

## Use multiple SAML2 security integrations with Microsoft Entra ID using the same issuer ID

This section guides you through configuring Snowflake and Microsoft Entra ID to let users authenticate through SSO using both a public or
private issuer URL. You can use two different SAML2 security integrations with Microsoft Entra ID to implement this experience. You can
configure Microsoft Entra ID to differentiate between public and private issuer URLs by appending a different application ID to each issuer
URL.

Before continuing, you must enable the identifier-first login flow.

Follow the sections below to learn how to use multiple SAML2 security integrations with Microsoft Entra ID using the same issuer
ID:

* Configure Microsoft Entra ID to append application IDs to Microsoft Entra Identifier URLs.
* Gather the Login URL, Microsoft Entra identifier, and application ID.
* Create public and private SAML2 security integrations.

### Configure Microsoft Entra ID to append application IDs to Microsoft Entra Identifier URLs

1. Log in to [Microsoft Azure](https://portal.azure.com/).
2. Under Azure services, select Microsoft Entra ID.
3. In the left navigation, select Manage » Enterprise applications.
4. Select your application.
5. In the left navigation, select Manage » Single sign-on.
6. In Attributes & Claims, select Edit.
7. Under Additional claims, expand Advanced settings.
8. Beside Advanced SAML claims options, select Edit.

   A panel on the right appears.
9. Select Append application ID to issuer.

### Gather the Login URL, Microsoft Entra identifier, and application ID

1. Ensure you configured Microsoft Entra ID.
2. In the left navigation, select Manage » Single sign-on.
3. Under Set up <your application name>, save the following values for later:

   * Login URL
   * Microsoft Entra Identifier
4. In the left navigation, select Overview
5. Under Properties, save the Application ID for later.
6. Repeat for additional applications.

### Create public and private SAML2 security integrations

1. Ensure you configured Microsoft Entra ID.
2. Ensure you gathered the Login URL, Microsoft Entra identifier, and application ID.
3. Sign in to [Snowsight](ui-snowsight-gs.md).
4. In the navigation menu, select Projects » Worksheets.
5. Switch to a role with the [CREATE INTEGRATION](../sql-reference/sql/create-security-integration-saml2.md) privilege.
6. Execute the following SQL statement to create a SAML2 security integration:

   ```sqlexample
   CREATE OR REPLACE SECURITY INTEGRATION entra_id_public
     TYPE = SAML2
     ENABLED = TRUE
     SAML2_ISSUER = '<microsoft_entra_identifier>/<application_id>'
     SAML2_SSO_URL = '<login_url>'
     SAML2_PROVIDER = 'CUSTOM'
     SAML2_X509_CERT = 'MIIC...TAs/'
     SAML2_SP_INITIATED_LOGIN_PAGE_LABEL = 'Entra ID SSO Public'
     SAML2_ENABLE_SP_INITIATED = TRUE
     SAML2_SNOWFLAKE_ACS_URL = 'https://<organization_name>-<account_name>.snowflakecomputing.com/fed/login'
     SAML2_SNOWFLAKE_ISSUER_URL = 'https://<organization_name>-<account_name>.snowflakecomputing.com';
   ```

   Where the following placeholders are replaced with the values you gathered earlier:

   | Placeholder | Example value |
   | --- | --- |
   | `<login_url>` | `https://login.microsoftonline.com/91ccae45-d439-xxxx-xxxx-e22c06bfe4f9/saml2` |
   | `<microsoft_entra_identifier>` | `https://sts.windows.net/91ccae45-d439-xxxx-xxxx-e22c06bfe4f9` |
   | `<application_id>` | `456xyz00-4567-4567-4567-4567xyz5678` |
   | `<organization_name>` | `EXAMPLE-USER12_AA12` |
   | `<account_name>` | `MSMITH` |

7. Create another SAML2 security integration, appending the private application ID to the Microsoft Entra Identifier in the SAML2_ISSUER
   parameter.
