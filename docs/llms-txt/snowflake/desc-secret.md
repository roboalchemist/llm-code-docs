# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-secret.md

# DESCRIBE SECRET

Describes the properties of a secret.

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER SECRET](alter-secret.md) , [CREATE SECRET](create-secret.md) , [DROP SECRET](drop-secret.md) , [SHOW SECRETS](show-secrets.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } SECRET <name>
```

## Parameters

`name`
:   Specifies the identifier for the secret to describe. If the identifier contains spaces or special characters, the entire string
    must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Output

The command output provides secret properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the secret was created. |
| `name` | Name of the secret. |
| `schema_name` | Name of the schema that contains the secret. |
| `database_name` | Name of the database that contains the secret. |
| `owner` | Name of the role that owns the secret. |
| `comment` | Comment for the secret or NULL if a comment is not specified. |
| `secret_type` | Either `OAUTH2`, `PASSWORD`, `GENERIC`, or `SYMMETRIC_KEY`. |
| `username` | The username that is stored in the secret. |
| `oauth_access_token_expiry_time` | The timestamp as a string when the OAuth access token expires. |
| `oauth_refresh_token_expiry_time` | The timestamp as a string when the OAuth refresh token expires or NULL if the secret does not store this value. |
| `oauth_scopes` | A comma-separated list of scopes to use when making a request from the OAuth server by a role with USAGE on the integration during the OAuth client credentials flow or NULL if there are no scopes. |
| `integration_name` | The name of the External API Authentication integration that is referenced in the secret or NULL if the secret does not reference an External API Authentication integration. |
| `algorithm` | The algorithm used, for [symmetric key secrets](create-secret.md). |
| `key_length` | Length of the key used, for [symmetric key secrets](create-secret.md). |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Secret |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Snowflake never returns the `PASSWORD` property value.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

Describe the secret:

> ```sqlexample
> DESC SECRET service_now_creds_pw;
> ```
