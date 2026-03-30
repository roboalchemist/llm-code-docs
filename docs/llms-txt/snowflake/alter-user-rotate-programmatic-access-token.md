# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-user-rotate-programmatic-access-token.md

# ALTER USER … ROTATE PROGRAMMATIC ACCESS TOKEN (PAT)

Rotates [programmatic access token](../../user-guide/programmatic-access-tokens.md), generating a new token secret with an
extended expiration time, and expiring the existing token secret. The new secret is generated using the same DAYS_TO_EXPIRY
property set when the token was first created.

> **Note:**
>
> You cannot rotate a programmatic access token in a session where you used a programmatic access token for authentication.

See also:
:   [ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-add-programmatic-access-token.md) ,
    [ALTER USER … MODIFY PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-modify-programmatic-access-token.md) ,
    [ALTER USER … REMOVE PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-remove-programmatic-access-token.md) ,
    [SHOW USER PROGRAMMATIC ACCESS TOKENS](show-user-programmatic-access-tokens.md)

## Syntax

```sqlsyntax
ALTER USER [ IF EXISTS ] [ <username> ] ROTATE { PROGRAMMATIC ACCESS TOKEN | PAT } <token_name>
  [ EXPIRE_ROTATED_TOKEN_AFTER_HOURS = <integer> ]
```

## Parameters

`username`
:   The name of the user that the token is associated with.

    If you omit this parameter, the command rotates the token for the user who is currently logged in (the active user in the
    current session).

`ROTATE { PROGRAMMATIC ACCESS TOKEN | PAT } token_name`
:   Rotates a programmatic access token with the specified name.

    You can use the keyword PAT as a shorter way of specifying the keywords PROGRAMMATIC ACCESS TOKEN.

`EXPIRE_ROTATED_TOKEN_AFTER_HOURS = integer`
:   Sets the expiration time of the existing token secret to expire after the specified number of hours.

    You can set this to a value of `0` to expire the current token secret immediately.

    You can set this to a value in the range of `0` to the number of hours remaining before the current secret expires.

    Default: `24`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MODIFY PROGRAMMATIC AUTHENTICATION METHODS | User | Required only when rotating a programmatic access token for a human user other than yourself or a service user. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The command output provides information about the rotated programmatic access token in the following columns:

| Column | Description |
| --- | --- |
| `token_name` | Name of the rotated token. |
| `token_secret` | The token itself. Use this to authenticate to an endpoint.  **Note:** The token only appears in the output of the ALTER USER … ROTATE PROGRAMMATIC ACCESS TOKEN command. No other SQL command or function prints out or returns the token.  If you need to access this token programmatically, you can use [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) to execute this command and retrieve the token from the [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md). |
| `rotated_token_name` | Name of the token that represents the prior secret.  You can use this token object to determine how long the prior secret remains valid. You can also expire the token, if needed. You can’t make any other types of changes to this token.  Note that this token object counts against the maximum number of tokens allowed per user. |

## Usage notes

You cannot rotate a programmatic access token in a session where you used a programmatic access token for authentication.

## Examples

Rotate a programmatic access token associated with the user `example_user`:

```sqlexample
ALTER USER IF EXISTS example_user ROTATE PROGRAMMATIC ACCESS TOKEN token_name;
```

Rotate a programmatic access token associated with the user `example_user` and expire the existing token secret
immediately:

```sqlexample
ALTER USER IF EXISTS example_user ROTATE PROGRAMMATIC ACCESS TOKEN token_name
  EXPIRE_ROTATED_TOKEN_AFTER_HOURS=0;
```
