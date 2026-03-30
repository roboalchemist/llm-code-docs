# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-security-integration-oauth-external.md

# ALTER SECURITY INTEGRATION (External OAuth)

> **Attention:**
>
> Mentions of Microsoft Azure Active Directory refer to Microsoft Entra ID.

Modifies the properties of an existing security integration created for External OAuth. For information about modifying other types of
security integrations (e.g. Snowflake OAuth), see [ALTER SECURITY INTEGRATION](alter-security-integration.md).

See also:
:   [CREATE SECURITY INTEGRATION (External OAuth)](create-security-integration-oauth-external.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

## Syntax

```sqlsyntax
ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name> SET
  [ TYPE = EXTERNAL_OAUTH ]
  [ ENABLED = { TRUE | FALSE } ]
  [ EXTERNAL_OAUTH_TYPE = { OKTA | AZURE | PING_FEDERATE | CUSTOM } ]
  [ EXTERNAL_OAUTH_ISSUER = '<string_literal>' ]
  [ EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = '<string_literal>' | ('<string_literal>', '<string_literal>' [ , ... ] ) ]
  [ EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'LOGIN_NAME | EMAIL_ADDRESS' ]
  [ EXTERNAL_OAUTH_JWS_KEYS_URL = '<string_literal>' ] -- For OKTA | PING_FEDERATE | CUSTOM
  [ EXTERNAL_OAUTH_JWS_KEYS_URL = '<string_literal>' | ('<string_literal>' [ , '<string_literal>' ... ] ) ] -- For Azure
  [ EXTERNAL_OAUTH_RSA_PUBLIC_KEY = <public_key1> ]
  [ EXTERNAL_OAUTH_RSA_PUBLIC_KEY_2 = <public_key2> ]
  [ EXTERNAL_OAUTH_BLOCKED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
  [ EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
  [ EXTERNAL_OAUTH_AUDIENCE_LIST = ('<string_literal>') ]
  [ EXTERNAL_OAUTH_ANY_ROLE_MODE = DISABLE | ENABLE | ENABLE_FOR_PRIVILEGE ]
  [ EXTERNAL_OAUTH_SCOPE_DELIMITER = '<string_literal>' ] -- Only for EXTERNAL_OAUTH_TYPE = CUSTOM
  [ NETWORK_POLICY = '<network_policy>' ]
  [ COMMENT = '<string_literal>' ]

ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name>  UNSET {
                                                            ENABLED                      |
                                                            EXTERNAL_OAUTH_AUDIENCE_LIST |
                                                            }
                                                            [ , ... ]

ALTER [ SECURITY ] INTEGRATION <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER [ SECURITY ] INTEGRATION <name> UNSET TAG <tag_name> [ , <tag_name> ... ]
```

## Parameters

`name`
:   Identifier for the integration to alter. If the identifier contains spaces or special characters, the entire string must be enclosed in
    double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`SET ...`
:   Specifies one or more properties/parameters to set for the integration (separated by blank spaces, commas, or new lines):

    `TYPE = EXTERNAL_OAUTH`
    :   Distinguishes the [External OAuth](../../user-guide/oauth-ext-overview.md) integration from a
        [Snowflake OAuth](../../user-guide/oauth-snowflake-overview.md) integration.

    `ENABLED = { TRUE | FALSE }`
    :   Specifies whether to initiate operation of the integration or suspend it.

        * `TRUE` allows the integration to run based on the parameters specified in the pipe definition.
        * `FALSE` suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails to work.

    `EXTERNAL_OAUTH_TYPE = { OKTA | AZURE | PING_FEDERATE | CUSTOM }`
    :   Specifies the OAuth 2.0 authorization server to be Okta, Microsoft Entra ID, Ping Identity PingFederate, or a Custom OAuth 2.0
        authorization server.

    `EXTERNAL_OAUTH_ISSUER = 'string_literal'`
    :   Specifies the URL to define the OAuth 2.0 authorization server.

    `EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = { 'string_literal' | ('string_literal', 'string_literal' [ , ... ] ) }`
    :   Specifies the access token claim or claims that can be used to map the access token to a Snowflake user record.

        The data type of the claim must be a string or a list of strings.

    `EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = { 'LOGIN_NAME | EMAIL_ADDRESS' }`
    :   Indicates which Snowflake user record attribute should be used to map the access token to a Snowflake user record.

    `EXTERNAL_OAUTH_JWS_KEYS_URL = 'string_literal'`
    :   Specifies the endpoint from which to download public keys or certificates to validate an External OAuth access token.

        This syntax applies to security integrations where `EXTERNAL_OAUTH_TYPE = { OKTA | PING_FEDERATE | CUSTOM }`

    `EXTERNAL_OAUTH_JWS_KEYS_URL = { 'string_literal' | ('string_literal' [ , 'string_literal' ... ] ) }`
    :   Specifies the endpoint or a list of endpoints from which to download public keys or certificates to validate an External OAuth access
        token. The maximum number of URLs that can be specified in the list is 3.

        This syntax applies to security integrations where `EXTERNAL_OAUTH_TYPE = AZURE`

    `EXTERNAL_OAUTH_RSA_PUBLIC_KEY = public_key1`
    :   Specifies a Base64-encoded RSA public key, without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` headers.

    `EXTERNAL_OAUTH_RSA_PUBLIC_KEY_2 = public_key2`
    :   Specifies a second RSA public key, without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` headers. Used
        for key rotation.

    `EXTERNAL_OAUTH_BLOCKED_ROLES_LIST = ( 'role_name' [ , 'role_name' , ... ] )`
    :   Specifies the list of roles that a client cannot set as the [primary role](../../user-guide/security-access-control-overview.md). A role
        in this list cannot be used when creating a Snowflake session based on the access token from the External OAuth
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

    `EXTERNAL_OAUTH_AUDIENCE_LIST = ('string_literal')`
    :   Specifies additional values that can be used for the access token’s audience validation on top of using the Customer’s Snowflake
        Account URL (i.e. `<account_identifier>.snowflakecomputing.com`). For more information, see
        [Account identifiers](../../user-guide/admin-account-identifier.md).

        For details on this property when using Power BI SSO, refer to
        [Power BI SSO security integrations](../../user-guide/oauth-powerbi.md).

        Currently, multiple audience URLs can be specified for [External OAuth Custom Clients](../../user-guide/oauth-ext-custom.md) only. Each
        URL must be enclosed in single quotes, with a comma separating each URL. For example:

        > ```sqlexample
        > external_oauth_audience_list = ('https://example.com/api/v2/', 'https://example.com')
        > ```

    `EXTERNAL_OAUTH_ANY_ROLE_MODE = { DISABLE | ENABLE | ENABLE_FOR_PRIVILEGE }`
    :   Specifies whether the OAuth client or user can use a role that is not defined in the OAuth access token. Note that with a
        [Power BI to Snowflake integration](../../user-guide/oauth-powerbi.md), the PowerBI user cannot switch roles even when this parameter is enabled.

        * `DISABLE` does not allow the OAuth client or user to switch roles (i.e. `USE ROLE role;`). Default.
        * `ENABLE` allows the OAuth client or user to switch roles.
        * `ENABLE_FOR_PRIVILEGE` allows the OAuth client or user to switch roles only for a client or user with the USE_ANY_ROLE
          privilege. This privilege can be granted and revoked to one or more roles available to the user. For example:

          ```sqlexample
          GRANT USE_ANY_ROLE ON INTEGRATION external_oauth_1 TO role1;
          ```

          ```sqlexample
          REVOKE USE_ANY_ROLE ON INTEGRATION external_oauth_1 FROM role1;
          ```

        Note that the value can be optionally enclosed in single quotes (e.g. either `DISABLE` or `'DISABLE'`).

    `EXTERNAL_OAUTH_SCOPE_DELIMITER = 'string_literal'`
    :   Specifies the scope delimiter in the authorization token.

        The delimiter can be any single character, such as comma (`','`) or space (`' '`).

        This security integration property is optional and can be used to override the default comma delimiter. Note that this property is only
        supported for custom External OAuth integrations, where:

        > `EXTERNAL_OAUTH_TYPE = CUSTOM`

        Contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support) to enable this
        property in your Snowflake account.

    `NETWORK_POLICY = 'network_policy'`
    :   Specifies an existing [network policy](../../user-guide/network-policies.md). This network policy controls network traffic from the client
        to Snowflake.

        For more information, see [Restricting network traffic for External OAuth](../../user-guide/oauth-ext-overview.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the integration.

        Default: No value

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`UNSET ...`
:   Specifies one or more properties/parameters to unset for the security integration, which resets them back to their defaults:

    * `ENABLED`
    * `EXTERNAL_OAUTH_AUDIENCE_LIST`
    * `TAG tag_name [ , tag_name ... ]`

## Usage notes

Regarding metadata:

> > **Attention:**
> >
> > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example initiates operation of a suspended integration:

```sqlexample
ALTER SECURITY INTEGRATION myint SET ENABLED = TRUE;
```
