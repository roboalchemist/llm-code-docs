# Source: https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-oauth-external.md

# CREATE SECURITY INTEGRATION (External OAuth)

> **Attention:**
>
> Mentions of Microsoft Azure Active Directory refer to Microsoft Entra ID.

Creates a new External OAuth security integration in the account or replaces an existing integration. An External OAuth security
integration allows a client to use a third-party authorization server to obtain the access tokens needed to interact with Snowflake.

For information about creating other types of security integrations (e.g. Snowflake OAuth), see [CREATE SECURITY INTEGRATION](create-security-integration.md).

See also:
:   [ALTER SECURITY INTEGRATION (External OAuth)](alter-security-integration-oauth-external.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SECURITY INTEGRATION [IF NOT EXISTS]
  <name>
  TYPE = EXTERNAL_OAUTH
  ENABLED = { TRUE | FALSE }
  EXTERNAL_OAUTH_TYPE = { OKTA | AZURE | PING_FEDERATE | CUSTOM }
  EXTERNAL_OAUTH_ISSUER = '<string_literal>'
  EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = { '<string_literal>' | ('<string_literal>' [ , '<string_literal>' , ... ] ) }
  EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = { 'LOGIN_NAME' | 'EMAIL_ADDRESS' }
  [ EXTERNAL_OAUTH_JWS_KEYS_URL = { '<string_literal>' | ('<string_literal>' [ , '<string_literal>' , ... ] ) } ]
  [ EXTERNAL_OAUTH_BLOCKED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
  [ EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
  [ EXTERNAL_OAUTH_RSA_PUBLIC_KEY = <public_key1> ]
  [ EXTERNAL_OAUTH_RSA_PUBLIC_KEY_2 = <public_key2> ]
  [ EXTERNAL_OAUTH_AUDIENCE_LIST = { '<string_literal>' | ('<string_literal>' [ , '<string_literal>' , ... ] ) } ]
  [ EXTERNAL_OAUTH_ANY_ROLE_MODE = { DISABLE | ENABLE | ENABLE_FOR_PRIVILEGE } ]
  [ EXTERNAL_OAUTH_SCOPE_DELIMITER = '<string_literal>' ]
  [ EXTERNAL_OAUTH_SCOPE_MAPPING_ATTRIBUTE = '<string_literal>' ]
  [ NETWORK_POLICY = '<network_policy>' ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   String that specifies the identifier (i.e. name) for the integration; must be unique in your account.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TYPE = EXTERNAL_OAUTH`
:   Distinguishes the [External OAuth](../../user-guide/oauth-ext-overview.md) integration from a
    [Snowflake OAuth](../../user-guide/oauth-snowflake-overview.md) integration.

`ENABLED = { TRUE | FALSE }`
:   Specifies whether to initiate operation of the integration or suspend it.

    * `TRUE` allows the integration to run based on the parameters specified in the pipe definition.
    * `FALSE` suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails
      to work.

    The value is case-insensitive.

    The default is `TRUE`.

`EXTERNAL_OAUTH_TYPE = { OKTA | AZURE | PING_FEDERATE | CUSTOM }`
:   Specifies the OAuth 2.0 authorization server to be Okta, Microsoft Entra ID, Ping Identity PingFederate, or a Custom OAuth 2.0 authorization
    server.

`EXTERNAL_OAUTH_ISSUER = 'string_literal'`
:   Specifies the URL to define the OAuth 2.0 authorization server.

`EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = { 'string_literal' | ('string_literal' [ , 'string_literal' , ... ] ) }`
:   Specifies the access token claim or claims to map the access token to a user record.

    The data type of the claim must be a string or a list of strings.

`EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = { 'LOGIN_NAME' | 'EMAIL_ADDRESS' }`
:   Indicates which Snowflake user record attribute should be used to map the access token to a user record.

## Optional parameters

`EXTERNAL_OAUTH_JWS_KEYS_URL = { 'string_literal' | ('string_literal' [ , 'string_literal' , ... ] ) }`
:   Specifies the HTTPS URL or a list of HTTPS URLs from where you can download public keys or certificates to validate an External OAuth access
    token.

    If you set the `EXTERNAL_OAUTH_TYPE` parameter to `AZURE`, then you can specify a maximum of three URLs. For example, to
    specify two URLs, use the following syntax:

    > ```sqlexample
    > EXTERNAL_OAUTH_JWS_KEYS_URL = ('https://example.ca', 'https://example.co.uk')
    > ```

    If you set the `EXTERNAL_OAUTH_TYPE` parameter to `OKTA`, `PING_FEDERATE`, or `CUSTOM`, then you can specify only
    one URL. For example:

    > ```sqlexample
    > EXTERNAL_OAUTH_JWS_KEYS_URL = 'https://example.ca'
    > ```

`EXTERNAL_OAUTH_RSA_PUBLIC_KEY = public_key1`
:   Specifies a Base64-encoded RSA public key, without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`
    headers.

    Snowflake supports cryptographic keys generated using the following algorithms:

    * RSA digital signature algorithms RS256, RS384, and RS512.
    * Elliptic Curve Digital Signature Algorithms (ECDSA) algorithms ES256(P-256), ES384 (P-384), and ES512 (P-512).

    These signatures use the SHA-256, SHA-384, and SHA-512 hash algorithms, respectively.

`EXTERNAL_OAUTH_RSA_PUBLIC_KEY_2 = public_key2`
:   Specifies a second RSA public key, without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` headers. Used
    for key rotation.

`EXTERNAL_OAUTH_BLOCKED_ROLES_LIST = ( 'role_name' [ , 'role_name' , ... ] )`
:   Specifies the list of roles that a client cannot set as the [primary role](../../user-guide/security-access-control-overview.md).
    A role in this list cannot be used when creating a Snowflake session based on the access token from the External OAuth
    authorization server.

    By default, this list includes the ACCOUNTADMIN, ORGADMIN, GLOBALORGADMIN, and SECURITYADMIN roles. To remove these privileged roles from the list, use
    the [ALTER ACCOUNT](alter-account.md) command to set the [EXTERNAL_OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST](../parameters.md) account parameter to
    `FALSE`.

`EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ( 'role_name' [ , 'role_name' , ... ] )`
:   Specifies the list of roles that the client can set as the primary role.

    A role in this list can be used when creating a Snowflake session based on the access token from the External OAuth authorization
    server.

    > **Caution:**
    >
    > This parameter supports the ACCOUNTADMIN, ORGADMIN, GLOBALORGADMIN, and SECURITYADMIN system roles.
    >
    > Exercise caution when creating a Snowflake session with these highly privileged roles set as the primary role.

`EXTERNAL_OAUTH_AUDIENCE_LIST = { 'string_literal' | ('string_literal' [ , 'string_literal' , ... ] ) }`
:   Specifies additional values for the access token’s audience validation on top of using the Customer’s Snowflake
    Account URL (i.e. `<account_identifier>.snowflakecomputing.com`). For more information, see
    [Account identifiers](../../user-guide/admin-account-identifier.md).

    For details on this parameter when using Power BI SSO, refer to
    [Power BI SSO security integrations](../../user-guide/oauth-powerbi.md).

    Currently, multiple audience URLs can be specified for [External OAuth Custom Clients](../../user-guide/oauth-ext-custom.md) only. Each URL
    must be enclosed in single quotes, with a comma separating each URL. For example:

    > ```sqlexample
    > EXTERNAL_OAUTH_AUDIENCE_LIST = ('https://example.com/api/v2/', 'https://example.com')
    > ```

`EXTERNAL_OAUTH_ANY_ROLE_MODE = { DISABLE | ENABLE | ENABLE_FOR_PRIVILEGE }`
:   Specifies whether the OAuth client or user can use a role that is not defined in the OAuth access token. Note that with a
    [Power BI to Snowflake integration](../../user-guide/oauth-powerbi.md), the PowerBI user cannot switch roles even when this parameter is
    enabled.

    * `DISABLE` does not allow the OAuth client or user to switch roles (i.e. `USE ROLE role;`). Default.
    * `ENABLE` allows the OAuth client or user to switch roles.
    * `ENABLE_FOR_PRIVILEGE` allows the OAuth client or user to switch roles only for a client or user with the `USE_ANY_ROLE`
      privilege. This privilege can be granted and revoked to one or more roles available to the user. For example:

      ```sqlexample
      GRANT USE_ANY_ROLE ON INTEGRATION external_oauth_1 TO role1;
      ```

      ```sqlexample
      REVOKE USE_ANY_ROLE ON INTEGRATION external_oauth_1 FROM role1;
      ```

    Note that the value can be optionally enclosed in single quotes (e.g. either `DISABLE` or `'DISABLE'`).

`EXTERNAL_OAUTH_SCOPE_DELIMITER = 'string_literal'`
:   Specifies the scope delimiter in the authorization token, overriding the default delimiter, `','`. The delimiter can be any single
    character, such as comma (`','`) or space (`' '`).

    You can only use this property if you set the `EXTERNAL_OAUTH_TYPE` parameter to `CUSTOM`.

`EXTERNAL_OAUTH_SCOPE_MAPPING_ATTRIBUTE = 'string_literal'`
:   Specifies the access token claim to map the access token to an account role.

    You can only set this parameter to `scp` or `scope`.

    You can only use this parameter if you set the `EXTERNAL_OAUTH_TYPE` parameter to `CUSTOM`.

`NETWORK_POLICY = 'network_policy'`
:   Specifies an existing [network policy](../../user-guide/network-policies.md). This network policy controls network traffic from the client
    to Snowflake.

    For more information, see [Restricting network traffic for External OAuth](../../user-guide/oauth-ext-overview.md).

`COMMENT = 'string_literal'`
:   Specifies a comment for the integration.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE INTEGRATION | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

### Microsoft Entra ID example

The following example creates an External OAuth security integration for a Microsoft Entra ID OAuth 2.0 authorization server.

> ```sqlexample
> CREATE SECURITY INTEGRATION external_oauth_azure_1
>     TYPE = external_oauth
>     ENABLED = true
>     EXTERNAL_OAUTH_TYPE = azure
>     EXTERNAL_OAUTH_ISSUER = '<AZURE_AD_ISSUER>'
>     EXTERNAL_OAUTH_JWS_KEYS_URL = '<AZURE_AD_JWS_KEY_ENDPOINT>'
>     EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = 'upn'
>     EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'login_name';
> ```

View the integration settings using [DESCRIBE INTEGRATION](desc-integration.md):

```sqlexample
DESC SECURITY INTEGRATION external_oauth_azure_1;
```

### Okta example

The following example creates an External OAuth security integration for an Okta OAuth 2.0 authorization server.

> ```sqlexample
> CREATE SECURITY INTEGRATION external_oauth_okta_1
>     TYPE = external_oauth
>     ENABLED = true
>     EXTERNAL_OAUTH_TYPE = okta
>     EXTERNAL_OAUTH_ISSUER = '<OKTA_ISSUER>'
>     EXTERNAL_OAUTH_JWS_KEYS_URL = '<OKTA_JWS_KEY_ENDPOINT>'
>     EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = 'sub'
>     EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'login_name';
> ```

View the integration settings using [DESCRIBE INTEGRATION](desc-integration.md):

```sqlexample
DESC SECURITY INTEGRATION external_oauth_okta_1;
```

### Microsoft Power BI SSO examples

For examples, see:

* [Creating a Power BI security integration](../../user-guide/oauth-powerbi.md)
* [Using Power BI SSO with B2B guest users](../../user-guide/oauth-powerbi.md)
