# Source: https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-api-auth.md

# CREATE SECURITY INTEGRATION (External API Authentication)

Creates a new security integration for external API Authentication in the account or replaces an existing integration.

For information about creating other types of security integrations (e.g. External OAuth), see [CREATE SECURITY INTEGRATION](create-security-integration.md).

See also:
:   [ALTER SECURITY INTEGRATION (External API Authentication)](alter-security-integration-api-auth.md) , [DESCRIBE INTEGRATION](desc-integration.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)

## Syntax

### OAuth: Client credentials

```sqlsyntax
CREATE SECURITY INTEGRATION <name>
  TYPE = API_AUTHENTICATION
  AUTH_TYPE = OAUTH2
  ENABLED = { TRUE | FALSE }
  [ OAUTH_TOKEN_ENDPOINT = '<string_literal>' ]
  [ OAUTH_CLIENT_AUTH_METHOD = { CLIENT_SECRET_BASIC | CLIENT_SECRET_POST } ]
  [ OAUTH_CLIENT_ID = '<string_literal>' ]
  [ OAUTH_CLIENT_SECRET = '<string_literal>' ]
  [ OAUTH_GRANT = 'CLIENT_CREDENTIALS']
  [ OAUTH_ACCESS_TOKEN_VALIDITY = <integer> ]
  [ OAUTH_ALLOWED_SCOPES = ( '<scope_1>' [ , '<scope_2>' ... ] ) ]
  [ COMMENT = '<string_literal>' ]
```

### OAuth: Authorization code grant flow

```sqlsyntax
CREATE SECURITY INTEGRATION <name>
  TYPE = API_AUTHENTICATION
  AUTH_TYPE = OAUTH2
  ENABLED = { TRUE | FALSE }
  [ OAUTH_AUTHORIZATION_ENDPOINT = '<string_literal>' ]
  [ OAUTH_TOKEN_ENDPOINT = '<string_literal>' ]
  [ OAUTH_CLIENT_AUTH_METHOD = { CLIENT_SECRET_BASIC | CLIENT_SECRET_POST } ]
  [ OAUTH_CLIENT_ID = '<string_literal>' ]
  [ OAUTH_CLIENT_SECRET = '<string_literal>' ]
  [ OAUTH_GRANT = 'AUTHORIZATION_CODE']
  [ OAUTH_ACCESS_TOKEN_VALIDITY = <integer> ]
  [ OAUTH_REFRESH_TOKEN_VALIDITY = <integer> ]
  [ COMMENT = '<string_literal>' ]
```

### OAuth: JWT bearer flow

```sqlsyntax
CREATE SECURITY INTEGRATION <name>
  TYPE = API_AUTHENTICATION
  AUTH_TYPE = OAUTH2
  ENABLED = { TRUE | FALSE }
  [ OAUTH_AUTHORIZATION_ENDPOINT = '<string_literal>' ]
  [ OAUTH_TOKEN_ENDPOINT = '<string_literal>' ]
  [ OAUTH_CLIENT_AUTH_METHOD = { CLIENT_SECRET_BASIC | CLIENT_SECRET_POST } ]
  [ OAUTH_CLIENT_ID = '<string_literal>' ]
  [ OAUTH_CLIENT_SECRET = '<string_literal>' ]
  [ OAUTH_GRANT = 'JWT_BEARER']
  [ OAUTH_ACCESS_TOKEN_VALIDITY = <integer> ]
  [ OAUTH_REFRESH_TOKEN_VALIDITY = <integer> ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the integration. This value must be unique in your account.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless
    the entire identifier string is enclosed in double quotes (e.g. “My object”). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TYPE = API_AUTHENTICATION`
:   Specifies that you are creating a security interface between Snowflake and an external service that uses OAuth 2.0 with
    External API Authentication.

`AUTH_TYPE = OAUTH2`
:   Specifies that the integration uses OAuth 2.0 to authenticate to the external service.

`ENABLED = { TRUE | FALSE }`
:   Specifies whether this security integration is enabled or disabled.

    `TRUE`
    :   Allows the integration to run based on the parameters specified in the integration definition.

    `FALSE`
    :   Suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails to work.

    The value is case-insensitive.

    The default is `TRUE`.

## Optional parameters

Note that this is an exhaustive list of parameters that you can configure. Configure the parameters in the integration to match the
parameters that you configure when [creating a secret](create-secret.md) based on the OAuth flow that you choose.

`OAUTH_AUTHORIZATION_ENDPOINT = 'string_literal'`
:   Specifies the URL for authenticating to the external service. For example, to connect to the ServiceNow instance the URL should be in the
    following format:

    ```none
    https://<instance_name>.service-now.com/oauth_token
    ```

    Where `instance_name` is the name of your ServiceNow instance.

`OAUTH_TOKEN_ENDPOINT = 'string_literal'`
:   Specifies the token endpoint used by the client to obtain an access token by presenting its authorization grant or refresh token.
    The token endpoint is used with every authorization grant except for the implicit grant type (since an access token is issued directly).

`OAUTH_CLIENT_AUTH_METHOD = { CLIENT_SECRET_BASIC | CLIENT_SECRET_POST }`
:   Controls how client credentials are sent to the external service.

    `CLIENT_SECRET_BASIC`
    :   Specifies that client credentials are sent using the HTTP Basic Authentication Scheme.

    `CLIENT_SECRET_POST`
    :   Specifies that client credentials are sent in the HTTP request body of a POST request.

    Default: `CLIENT_SECRET_BASIC`

`OAUTH_CLIENT_ID = 'string_literal'`
:   Specifies the client ID for the OAuth application in the external service.

`OAUTH_CLIENT_SECRET = 'string_literal'`
:   Specifies the client secret for the OAuth application in the external service.

`OAUTH_GRANT = 'string_literal'`
:   Specifies the type of OAuth flow. One of the following:

    * `'CLIENT_CREDENTIALS'` when the integration will use client credentials.
    * `'AUTHORIZATION_CODE'` when the integration will use an authorization code.
    * `'JWT_BEARER'` when the integration will use a JWT bearer token.

`OAUTH_ACCESS_TOKEN_VALIDITY = integer`
:   Specifies the default lifetime of the OAuth access token (in seconds) issued by an OAuth server.

    The value set in this property is used if the access token lifetime is not returned as part of OAuth token response. When both
    values are available, the smaller of the two values will be used to refresh the access token.

`OAUTH_REFRESH_TOKEN_VALIDITY = integer`
:   Specifies the value to determine the validity of the refresh token obtained from the OAuth server.

`OAUTH_ALLOWED_SCOPES = ( 'scope_1' [ , 'scope_2' ... ] )`
:   Specifies a comma-separated list of scopes, with single quotes surrounding each scope, to use when making a request from the OAuth by a
    role with USAGE on the integration during the OAuth client credentials flow.

    This list must be a subset of the scopes defined in the `OAUTH_ALLOWED_SCOPES` property of the security integration. If the
    `OAUTH_SCOPES` property values are not specified, the secret inherits all of the scopes that are specified in the security
    integration.

    For the ServiceNow connector, the only possible scope value is `'useraccount'`.

    Default: Empty list (i.e. `[]`).

`COMMENT = 'string_literal'`
:   Specifies a comment for the integration.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE INTEGRATION | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |
| CREATE SECURITY INTEGRATION | Account | Grants the ability to create external security integrations of type API_AUTHENTICATION. This privilege does not grant the ability to create other types of security integrations. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Create a security integration named `servicenow_oauth` to connect Snowflake to the ServiceNow instance named `myinstance` using
OAuth with the code grant flow:

> ```sqlexample
> CREATE SECURITY INTEGRATION servicenow_oauth
>   TYPE = API_AUTHENTICATION
>   AUTH_TYPE = OAUTH2
>   OAUTH_CLIENT_AUTH_METHOD = CLIENT_SECRET_POST
>   OAUTH_CLIENT_ID = 'sn-oauth-134o9erqfedlc'
>   OAUTH_CLIENT_SECRET = 'eb9vaXsrcEvrFdfcvCaoijhilj4fc'
>   OAUTH_TOKEN_ENDPOINT = 'https://myinstance.service-now.com/oauth_token.do'
>   ENABLED = TRUE;
> ```

Create a security integration named `sharepoint_security_integration` to connect Snowflake to Microsoft Sharepoint
using OAuth with client credentials:

> ```sqlexample
> CREATE SECURITY INTEGRATION sharepoint_security_integration
>   TYPE = API_AUTHENTICATION
>   AUTH_TYPE = OAUTH2
>   OAUTH_CLIENT_AUTH_METHOD = CLIENT_SECRET_POST
>   OAUTH_CLIENT_ID = 'YOUR_CLIENT_ID'
>   OAUTH_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
>   OAUTH_GRANT = 'CLIENT_CREDENTIALS'
>   OAUTH_TOKEN_ENDPOINT = 'https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token'
>   OAUTH_ALLOWED_SCOPES = ('https://graph.microsoft.com/.default')
>   ENABLED = TRUE;
> ```
