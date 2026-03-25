# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-catalog-integration.md

# ALTER CATALOG INTEGRATION

Modifies the properties of an existing [catalog integration](../../user-guide/tables-iceberg.md).

See also:
:   [CREATE CATALOG INTEGRATION](create-catalog-integration.md) , [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md), [DROP CATALOG INTEGRATION](drop-catalog-integration.md) , [SHOW CATALOG INTEGRATIONS](show-catalog-integrations.md)

## Syntax

```sqlsyntax
ALTER CATALOG INTEGRATION [ IF EXISTS ] <name> SET
  REST_AUTHENTICATION = (
    restAuthenticationParams
  )
  [ REFRESH_INTERVAL_SECONDS = <value> ]
  [ COMMENT = '<string_literal>' ]
```

The `restAuthenticationParams` are as follows, depending on your authentication method:

**OAuth**

```sqlsyntax
restAuthenticationParams (for OAuth) ::=

  OAUTH_CLIENT_SECRET = '<oauth_client_secret>'
```

**Bearer token**

```sqlsyntax
restAuthenticationParams (for Bearer token) ::=

  BEARER_TOKEN = '<bearer_token>'
```

## Parameters

`name`
:   Specifies the identifier for the catalog integration to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Sets one or more specified properties or parameters to set for the catalog integration:

    `REFRESH_INTERVAL_SECONDS = value`
    :   Specifies the number of seconds that Snowflake waits between attempts to poll the external Iceberg catalog for metadata updates
        for [automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).

        For Delta-based tables, specifies the number of seconds that Snowflake waits between attempts to poll your external cloud storage for
        new metadata.

        Values: 30 to 86400, inclusive

        Default: 30 seconds

    `COMMENT = 'string_literal'`
    :   String (literal) that specifies a comment for the integration.

        Default: No value

### REST authentication parameters (restAuthenticationParams)

**OAuth**

> `OAUTH_CLIENT_SECRET = oauth_client_secret`
> :   Your OAuth2 client secret.

**Bearer token**

> `BEARER_TOKEN = bearer_token`
> :   The bearer token for your identity provider. You can alternatively specify a personal access token (PAT).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Integration (catalog) | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example updates the refresh interval for automated refresh to 30 seconds:

```sqlexample
ALTER CATALOG INTEGRATION myCatalogIntegration SET REFRESH_INTERVAL_SECONDS = 30;
```
