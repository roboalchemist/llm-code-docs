# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-secret.md

# ALTER SECRET

Modifies the properties of an existing secret.

See also:
:   [CREATE SECRET](create-secret.md) , [DESCRIBE SECRET](desc-secret.md) , [DROP SECRET](drop-secret.md) , [SHOW SECRETS](show-secrets.md)

## Syntax

**OAuth with client credentials flow:**

```sqlsyntax
ALTER SECRET [ IF EXISTS ] <name> SET [ OAUTH_SCOPES = ( '<scope_1>' [ , '<scope_2>' ... ] ) ]
                                      [ COMMENT = '<string_literal>' ]

ALTER SECRET [ IF EXISTS ] <name> UNSET COMMENT
```

**OAuth with authorization code grant flow:**

```sqlsyntax
ALTER SECRET [ IF EXISTS ] <name> SET [ OAUTH_REFRESH_TOKEN = '<token>' ]
                                      [ OAUTH_REFRESH_TOKEN_EXPIRY_TIME = '<string_literal>' ]
                                      [ COMMENT = '<string_literal>' ]

ALTER SECRET [ IF EXISTS ] <name> UNSET COMMENT
```

**Cloud provider:**

[Preview Feature](../../release-notes/preview-features.md) — Open

Available to all accounts.

```sqlsyntax
ALTER SECRET [ IF EXISTS ] <name> SET [ API_AUTHENTICATION = '<cloud_provider_security_integration>' ]
                                      [ COMMENT = '<string_literal>' ]

ALTER SECRET [ IF EXISTS ] <name> UNSET COMMENT
```

**Basic authentication:**

```sqlsyntax
ALTER SECRET [ IF EXISTS ] <name> SET [ USERNAME = '<username>' ]
                                      [ PASSWORD = '<password>' ]
                                      [ COMMENT = '<string_literal>' ]

ALTER SECRET [ IF EXISTS ] <name> UNSET COMMENT
```

**Generic string:**

```sqlsyntax
ALTER SECRET [ IF EXISTS ] <name> SET [ SECRET_STRING = '<string_literal>' ]
                                      [ COMMENT = '<string_literal>' ]

ALTER SECRET [ IF EXISTS ] <name> UNSET COMMENT
```

## OAuth with client credentials flow parameters

`name`
:   String that specifies the identifier (i.e. name) for the secret, must be unique in your schema.

`SET ...`
:   Specifies one (or more) parameters to set (separated by blank spaces, commas, or new lines).

    `OAUTH_SCOPES = ( 'scope_1' [ , 'scope_2' ... ] )`
    :   Specifies a comma-separated list of scopes to use when making a request from the OAuth server by a role with USAGE on the integration
        during the OAuth client credentials flow.

        This list must be a subset of the scopes defined in the `OAUTH_ALLOWED_SCOPES` property of the security integration. If the
        `OAUTH_SCOPES` property values are not specified, the secret inherits all of the scopes that are specified in the security
        integration.

## AWS IAM required parameters

[Preview Feature](../../release-notes/preview-features.md) — Open

Available to all accounts.

`SET ...`
:   Specifies one (or more) parameters to set (separated by blank spaces, commas, or new lines).

    `TYPE = CLOUD_PROVIDER_TOKEN`
    :   Specifies that this is secret for use with a cloud provider, such as Amazon Web Services (AWS).

    `API_AUTHENTICATION = 'cloud_provider_security_integration'`
    :   Specifies the `name` value of the Snowflake [security integration](create-security-integration-aws-iam.md)
        that connects Snowflake to a cloud provider.

## OAuth with authorization code grant flow parameters

`name`
:   String that specifies the identifier (i.e. name) for the secret, must be unique in your schema.

`SET ...`
:   Specifies one (or more) parameters to set (separated by blank spaces, commas, or new lines).

    `OAUTH_REFRESH_TOKEN = 'token'`
    :   Specifies the token as a string that is used to obtain a new access token from the OAuth authorization server when the access token
        expires.

    `OAUTH_REFRESH_TOKEN_EXPIRY_TIME = 'string_literal'`
    :   Specifies the timestamp as a string when the OAuth refresh token expires.

## Basic authentication parameters

`name`
:   String that specifies the identifier (i.e. name) for the secret, must be unique in your schema.

`SET ...`
:   > Specifies one (or more) parameters to set for the session (separated by blank spaces, commas, or new lines).

    `USERNAME = 'username'`
    :   Specifies the username value to store in the secret.

        Specify this property value when using a secret for basic authentication (i.e. the secret is `TYPE = PASSWORD`).

    `PASSWORD = 'password'`
    :   Specifies the password value to store in the secret.

        Specify this property value when using a secret for basic authentication (i.e. the secret is `TYPE = PASSWORD`).

## Generic string parameters

`name`
:   String that specifies the identifier (i.e. name) for the secret, must be unique in your schema.

`SET ...`
:   Specifies one (or more) parameters to set (separated by blank spaces, commas, or new lines).

    `SECRET_STRING = 'string_literal'`
    :   Specifies the string to store in the secret.

        The string can be an API token or a string of sensitive value that can be used in the handler code of a UDF or stored procedure. For
        details, see [Creating and using an external access integration](../../developer-guide/external-network-access/creating-using-external-network-access.md).

        You should not use this property to store any kind of OAuth token; use one of the other secret types for your OAuth use cases.

## Common parameters: all syntaxes

`SET ...`
:   > Specifies one (or more) parameters to set for the session (separated by blank spaces, commas, or new lines).

    `COMMENT = 'string_literal'`
    :   String (literal) that specifies a comment for the secret.

        Default: No value

`UNSET ...`
:   Specifies one (or more) properties/parameters to unset for the secret, which resets them back to their defaults:

    * `COMMENT`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Secret | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

Regarding metadata:

> **Attention:**
>
> Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Modify the comment for a secret:

> ```sqlexample
> ALTER SECRET service_now_creds_pw SET COMMENT = 'production secret for servicenow';
> ```
