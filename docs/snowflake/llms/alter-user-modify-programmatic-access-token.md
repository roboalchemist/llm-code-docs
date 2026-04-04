# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-user-modify-programmatic-access-token.md

# ALTER USER … MODIFY PROGRAMMATIC ACCESS TOKEN (PAT)

Changes the name of a [programmatic access token](../../user-guide/programmatic-access-tokens.md) or a property of the token.

> **Note:**
>
> You cannot modify or rename a programmatic access token in a session where you used a programmatic access token for
> authentication.

See also:
:   [ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-add-programmatic-access-token.md) ,
    [ALTER USER … ROTATE PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-rotate-programmatic-access-token.md) ,
    [ALTER USER … REMOVE PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-remove-programmatic-access-token.md) ,
    [SHOW USER PROGRAMMATIC ACCESS TOKENS](show-user-programmatic-access-tokens.md)

## Syntax

```sqlsyntax
ALTER USER [ IF EXISTS ] [ <username> ] MODIFY { PROGRAMMATIC ACCESS TOKEN | PAT } <token_name>
  RENAME TO <new_token_name>

ALTER USER [ IF EXISTS ] [ <username> ] MODIFY { PROGRAMMATIC ACCESS TOKEN | PAT } <token_name> SET
  [ DISABLED = { TRUE | FALSE } ]
  [ MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT = <integer> ]
  [ COMMENT = '<string_literal>' ]

ALTER USER [ IF EXISTS ] [ <username> ] MODIFY { PROGRAMMATIC ACCESS TOKEN | PAT } <token_name> UNSET
  [ DISABLED ]
  [ MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT ]
  [ COMMENT ]
```

## Parameters

`username`
:   The name of the user that the token is associated with.

    If `username` is omitted, the command modifies the programmatic access token for the user who is currently logged in
    (the active user of this session).

`MODIFY { PROGRAMMATIC ACCESS TOKEN | PAT } token_name`
:   Modifies a programmatic access token with the specified name.

    You can use the keyword PAT as a shorter way of specifying the keywords PROGRAMMATIC ACCESS TOKEN.

`RENAME TO new_token_name`
:   Specifies a new name for a programmatic access token.

`SET ...`
:   Specifies one (or more) properties to set for the programmatic access token (separated by blank spaces, commas, or new lines).

    `DISABLED = { TRUE | FALSE }`
    :   Disables or enables the programmatic access token.

        If a user is disabled or Snowflake locks a user, the programmatic tokens associated with that user are disabled automatically.
        If the user is subsequently enabled or Snowflake unlocks the user, the programmatic access tokens remain disabled. To enable
        the tokens again, set DISABLED to FALSE.

        For information, see [Re-enabling a disabled programmatic access token](../../user-guide/programmatic-access-tokens.md).

    `MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT = integer`
    :   The number of minutes during which a user can use this token to access Snowflake without being subject to an active
        [network policy](../../user-guide/network-policies.md).

        You can set this for a token for a person (if the USER object has TYPE=PERSON) if that person is not subject to a network policy
        but needs to use a programmatic access token for authentication. See [Network policy requirements](../../user-guide/programmatic-access-tokens.md).

        > **Note:**
        >
        > Setting MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT does not allow users to bypass the network policy itself.

        You can set this to a value in the range of `1` to `1440` (1 day).

        Default: `0`

    `COMMENT = 'string_literal'`
    :   Descriptive comment about the programmatic access token. This comment is displayed in the
        [list of programmatic access tokens](../../user-guide/programmatic-access-tokens.md) in Snowsight.

`UNSET ...`
:   Unsets one or more specified properties or parameters for the programmatic access token, which resets the properties to their
    defaults:

    * `DISABLED`
    * `MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT`
    * `COMMENT`

    To unset multiple properties or parameters with a single ALTER statement, separate each property or parameter with a comma.

    When unsetting a property or parameter, specify only the property or parameter name (unless the syntax above indicates that you
    should specify the value). Specifying the value returns an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MODIFY PROGRAMMATIC AUTHENTICATION METHODS | User | Required only when modifying a programmatic access token for a human user other than yourself or a service user. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

You cannot modify or rename a programmatic access token in a session where you used a programmatic access token for
authentication.

## Examples

Change the name of a programmatic access token associated with the user `example_user`:

```sqlexample
ALTER USER IF EXISTS example_user MODIFY PROGRAMMATIC ACCESS TOKEN old_token_name
  RENAME TO new_token_name;
```

Change the comment associated with a programmatic access token:

```sqlexample
ALTER USER IF EXISTS example_user MODIFY PROGRAMMATIC ACCESS TOKEN token_name
  SET COMMENT = 'my new comment';
```
