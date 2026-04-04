# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-security-integration-oauth-snowflake.md

# ALTER SECURITY INTEGRATION (Snowflake OAuth)

Modifies the properties of an existing security integration created for a Snowflake OAuth client. For information about modifying other
types of security integrations (e.g. External OAuth), see [ALTER SECURITY INTEGRATION](alter-security-integration.md).

See also:
:   [CREATE SECURITY INTEGRATION (Snowflake OAuth)](create-security-integration-oauth-snowflake.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

## Syntax

```sqlsyntax
ALTER [ SECURITY ] INTEGRATION <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER [ SECURITY ] INTEGRATION <name> UNSET TAG <tag_name> [ , <tag_name> ... ]
```

**Snowflake OAuth for partner applications**

> ```sqlsyntax
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name> SET
>   [ ENABLED = { TRUE | FALSE } ]
>   [ OAUTH_ISSUE_REFRESH_TOKENS = { TRUE | FALSE } ]
>   [ OAUTH_REDIRECT_URI ] = '<uri>'
>   [ OAUTH_REFRESH_TOKEN_VALIDITY = <integer> ]
>   [ OAUTH_SINGLE_USE_REFRESH_TOKENS_REQUIRED = { TRUE | FALSE } ]
>   [ OAUTH_USE_SECONDARY_ROLES = { IMPLICIT | NONE } ]
>   [ BLOCKED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
>   [ NETWORK_POLICY = '<network_policy>' ]
>   [ USE_PRIVATELINK_FOR_AUTHORIZATION_ENDPOINT = { TRUE | FALSE } ]
>   [ COMMENT = '<string_literal>' ]
>
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name>
>   REFRESH { OAUTH_CLIENT_SECRET | OAUTH_CLIENT_SECRET_2 }
>
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name> UNSET {
>   ENABLED |
>   COMMENT
>   }
>   [ , ... ]
> ```

**Snowflake OAuth for custom clients**

> ```sqlsyntax
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name> SET
>   [ ENABLED = { TRUE | FALSE } ]
>   [ OAUTH_REDIRECT_URI = '<uri>' ]
>   [ OAUTH_ALLOW_NON_TLS_REDIRECT_URI = { TRUE | FALSE } ]
>   [ OAUTH_ENFORCE_PKCE = { TRUE | FALSE } ]
>   [ PRE_AUTHORIZED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
>   [ BLOCKED_ROLES_LIST = ( '<role_name>' [ , '<role_name>' , ... ] ) ]
>   [ OAUTH_ISSUE_REFRESH_TOKENS = { TRUE | FALSE } ]
>   [ OAUTH_REFRESH_TOKEN_VALIDITY = <integer> ]
>   [ OAUTH_SINGLE_USE_REFRESH_TOKENS_REQUIRED = { TRUE | FALSE } ]
>   [ OAUTH_USE_SECONDARY_ROLES = IMPLICIT | NONE ]
>   [ NETWORK_POLICY = '<network_policy>' ]
>   [ OAUTH_CLIENT_RSA_PUBLIC_KEY = <public_key1> ]
>   [ OAUTH_CLIENT_RSA_PUBLIC_KEY_2 = <public_key2> ]
>   [ USE_PRIVATELINK_FOR_AUTHORIZATION_ENDPOINT = { TRUE | FALSE } ]
>   [ COMMENT = '{string_literal}' ]
>
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name>
>   REFRESH { OAUTH_CLIENT_SECRET | OAUTH_CLIENT_SECRET_2 }
>
> ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name>  UNSET {
>                                                            ENABLED                       |
>                                                            NETWORK_POLICY                |
>                                                            OAUTH_CLIENT_RSA_PUBLIC_KEY   |
>                                                            OAUTH_CLIENT_RSA_PUBLIC_KEY_2 |
>                                                            OAUTH_USE_SECONDARY_ROLES = IMPLICIT | NONE
>                                                            COMMENT
>                                                            }
>                                                            [ , ... ]
> ```

## Parameters

### Snowflake OAuth partner application parameters

Use these parameters when `OAUTH_CLIENT = <partner_application>` in the security integration. For example, these parameters are valid
for `OAUTH_CLIENT = TABLEAU_SERVER`.

`name`
:   Identifier for the integration to alter. If the identifier contains spaces or special characters, the entire string must be enclosed in
    double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`SET ...`
:   Specifies one or more properties/parameters to set for the integration (separated by blank spaces, commas, or new lines):

    `ENABLED = { TRUE | FALSE }`
    :   Specifies whether to initiate operation of the integration or suspend it.

        * `TRUE` allows the integration to run based on the parameters specified in the pipe definition.
        * `FALSE` suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails to work.

    `OAUTH_REDIRECT_URI = 'uri'`
    :   Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.

        This parameter is required when `OAUTH_CLIENT = LOOKER`. For details, see the example in the
        [Looker documentation](https://docs.looker.com/setup-and-management/database-config/snowflake#oauth).

    `OAUTH_ISSUE_REFRESH_TOKENS = { TRUE | FALSE }`
    :   Boolean that specifies whether to allow the client to exchange a refresh token for an access token when the current access token has
        expired. If set to `FALSE`, a refresh token is not issued. User consent is revoked, and the user must confirm authorization again.

        Default: `TRUE`

    `OAUTH_REFRESH_TOKEN_VALIDITY = integer`
    :   Integer that specifies how long refresh tokens should be valid (in seconds). This can be used to expire the refresh token periodically.

        Note that if your organization would like the minimum or maximum values lowered or raised, respectively, ask your account administrator
        to send a request to [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

        Values: `86400` (1 day) to `7776000` (90 days)

        Default: `7776000`

    `OAUTH_SINGLE_USE_REFRESH_TOKENS_REQUIRED =  { TRUE | FALSE }`
    :   Specifies whether [single-use refresh tokens](../../user-guide/single-use-refresh-tokens.md) should be used.

        Default: `FALSE`

    `OAUTH_USE_SECONDARY_ROLES = { IMPLICIT | NONE }`
    :   * `IMPLICIT` - Default secondary roles set in the user properties are activated by default in the session being opened.
        * `NONE` - Default secondary roles are not supported in the session being opened.

        Default: `NONE`

    `BLOCKED_ROLES_LIST = ( 'role_name' [ , 'role_name' , ... ] )`
    :   Comma-separated list of Snowflake roles that a user cannot explicitly consent to using after authenticating
        (e.g. `'custom_role1', 'custom_role2'`).

        By default, Snowflake prevents the ACCOUNTADMIN, ORGADMIN, GLOBALORGADMIN, and SECURITYADMIN roles from authenticating. To allow these
        privileged roles to authenticate, use the [ALTER ACCOUNT](alter-account.md) command to set the [OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST](../parameters.md) account parameter to `FALSE`.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `USE_PRIVATELINK_FOR_AUTHORIZATION_ENDPOINT = { TRUE | FALSE }`
    :   When TRUE, the interaction between Snowflake as the authorization server and the user who is authenticating uses
        [private connectivity](../../user-guide/private-connectivity-inbound.md). Interactions between Snowflake and the client, including the
        initial request to the authorization endpoint, still happens over the public internet.

        Default: `FALSE`

    `COMMENT = 'string_literal'`
    :   String (literal) that specifies a comment for the integration.

    `REFRESH { OAUTH_CLIENT_SECRET | OAUTH_CLIENT_SECRET_2 }`
    :   Generates a new client secret for the client to use, which allows an administrator to rotate client secrets. Snowflake provides two client
        secrets (OAUTH_CLIENT_SECRET and OAUTH_CLIENT_SECRET_2) for uninterrupted rotation; you can generate a new secret for either of these
        client secrets.

    `NETWORK_POLICY = 'network_policy'`
    :   Specifies an existing [network policy](../../user-guide/network-policies.md). This network policy controls network traffic that is
        attempting to exchange an authorization code for an access or refresh token, use a refresh token to obtain a new
        access token, or obtain Snowflake resources with an access token.

        For more information, see [Restricting network traffic for Snowflake OAuth](../../user-guide/oauth-snowflake-overview.md).

### Snowflake OAuth custom client parameters

Use these parameters when `OAUTH_CLIENT = CUSTOM` in the security integration.

`name`
:   Identifier for the integration to alter. If the identifier contains spaces or special characters, the entire string must be enclosed in
    double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`SET ...`
:   Specifies one or more properties/parameters to set for the integration (separated by blank spaces, commas, or new lines):

    `ENABLED = { TRUE | FALSE }`
    :   Specifies whether to initiate operation of the integration or suspend it.

        * `TRUE` allows the integration to run based on the parameters specified in the pipe definition.
        * `FALSE` suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails to work.

    `OAUTH_REDIRECT_URI = 'uri'`
    :   Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI. The URI must be protected by TLS
        (Transport Layer Security) unless the optional `OAUTH_ALLOW_NON_TLS_REDIRECT_URI` parameter is set to `TRUE`.

        Do not include query parameters sent with the redirect URI in the request to the [authorization endpoint](../../user-guide/oauth-custom.md). For example, if the value of the `redirect_uri` query parameter in the request
        to the authorization endpoint is `https://www.example.com/connect?authType=snowflake`, make sure the OAUTH_REDIRECT_URI parameter is
        set to `https://www.example.com/connect`.

    `OAUTH_SINGLE_USE_REFRESH_TOKENS_REQUIRED =  { TRUE | FALSE }`
    :   Specifies whether [single-use refresh tokens](../../user-guide/single-use-refresh-tokens.md) should be used.

        Default: `FALSE`

    `OAUTH_ALLOW_NON_TLS_REDIRECT_URI = { TRUE | FALSE }`
    :   If `TRUE`, allows setting `OAUTH_REDIRECT_URI` to a URI not protected by TLS. We highly recommend use of TLS to
        prevent man-in-the-middle OAuth redirects for use in phishing attacks.

        Default: `FALSE`

    `OAUTH_ENFORCE_PKCE = { TRUE | FALSE }`
    :   Boolean that specifies whether Proof Key for Code Exchange (PKCE) should be required for the integration.

        Default: `FALSE`

    `OAUTH_USE_SECONDARY_ROLES = { IMPLICIT | NONE }`
    :   * `IMPLICIT` - Default secondary roles set in the user properties are activated by default in the session being opened.
        * `NONE` - Default secondary roles are not supported in the session being opened.

        Default: `NONE`

    `PRE_AUTHORIZED_ROLES_LIST = '( role_name' [ , 'role_name , ... ] ')`
    :   Comma-separated list of Snowflake roles that a user does not need to explicitly consent to using after authenticating, e.g.
        `'custom_role1', 'custom_role2'`. The ACCOUNTADMIN, ORGADMIN, GLOBALORGADMIN, and SECURITYADMIN roles cannot be included in this list.

        > **Note:**
        >
        > This parameter is supported for confidential clients only.

    `BLOCKED_ROLES_LIST = ( 'role_name' [ , 'role_name' , ... ] )`
    :   Comma-separated list of Snowflake roles that a user cannot explicitly consent to using after authenticating
        (e.g. `'custom_role1', 'custom_role2'`).

        The ACCOUNTADMIN, ORGADMIN, GLOBALORGADMIN, and SECURITYADMIN roles are included in this list by default; however, if these roles should be removed
        for your account, ask your account administrator to send a request to [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    `OAUTH_ISSUE_REFRESH_TOKENS = { TRUE | FALSE }`
    :   Boolean that specifies whether to allow the client to exchange a refresh token for an access token when the current access token has
        expired. If set to `FALSE`, a refresh token is not issued. User consent is revoked, and the user must confirm authorization again.

        Default: `TRUE`

    `OAUTH_REFRESH_TOKEN_VALIDITY = integer`
    :   Integer that specifies how long refresh tokens should be valid (in seconds). This can be used to expire the refresh token periodically.

        When a refresh token expires, the application will need to direct the user through the authorization flow again to obtain a new refresh
        token.

        The supported minimum, maximum, and default values are as follows:

        | Application | Minimum | Maximum | Default |
        | --- | --- | --- | --- |
        | Tableau Desktop | `60` (1 minute) | `36000` (10 hours) | `36000` (10 hours) |
        | Tableau Cloud | `60` (1 minute) | `7776000` (90 days) | `7776000` (90 days) |
        | Custom client | `86400` (1 day) | `7776000` (90 days) | `7776000` (90 days) |

        If you have a business need to lower the minimum value or raise the maximum value, ask your account administrator to send a request to
        [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    `OAUTH_CLIENT_RSA_PUBLIC_KEY = public_key1`
    :   Specifies an RSA public key.

    `OAUTH_CLIENT_RSA_PUBLIC_KEY_2 = public_key2`
    :   Specifies a second RSA public key. Used for key rotation.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `USE_PRIVATELINK_FOR_AUTHORIZATION_ENDPOINT = { TRUE | FALSE }`
    :   When TRUE, the interaction between Snowflake as the authorization server and the user who is authenticating uses
        [private connectivity](../../user-guide/private-connectivity-inbound.md). Interactions between Snowflake and the client, including the
        initial request to the authorization endpoint, still happens over the public internet.

        Default: `FALSE`

    `COMMENT = 'string_literal'`
    :   String (literal) that specifies a comment for the integration.

    `REFRESH { OAUTH_CLIENT_SECRET | OAUTH_CLIENT_SECRET_2 }`
    :   Generates a new client secret for the client to use, which allows an administrator to rotate client secrets. Snowflake provides two client
        secrets (OAUTH_CLIENT_SECRET and OAUTH_CLIENT_SECRET_2) for uninterrupted rotation; you can generate a new secret for either of these
        client secrets.

    `NETWORK_POLICY = 'network_policy'`
    :   Specifies an existing [network policy](../../user-guide/network-policies.md). This network policy controls network traffic that is
        attempting to exchange an authorization code for an access or refresh token, use a refresh token to obtain a new
        access token, or obtain Snowflake resources with an access token.

        For more information, see [Restricting network traffic for Snowflake OAuth](../../user-guide/oauth-snowflake-overview.md).

`UNSET ...`
:   Specifies one or more properties/parameters to unset for the security integration, which resets them back to their defaults:

    * `ENABLED`
    * `NETWORK_POLICY`
    * `OAUTH_CLIENT_RSA_PUBLIC_KEY`
    * `OAUTH_CLIENT_RSA_PUBLIC_KEY_2`
    * `TAG tag_name [ , tag_name ... ]`
    * `COMMENT`

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
