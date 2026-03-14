# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-user-add-programmatic-access-token.md

# ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN (PAT)

Creates a [programmatic access token](../../user-guide/programmatic-access-tokens.md) for a user.

See also:
:   [ALTER USER … MODIFY PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-modify-programmatic-access-token.md) ,
    [ALTER USER … ROTATE PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-rotate-programmatic-access-token.md) ,
    [ALTER USER … REMOVE PROGRAMMATIC ACCESS TOKEN (PAT)](alter-user-remove-programmatic-access-token.md) ,
    [SHOW USER PROGRAMMATIC ACCESS TOKENS](show-user-programmatic-access-tokens.md)

## Syntax

```sqlsyntax
ALTER USER [ IF EXISTS ] [ <username> ] ADD { PROGRAMMATIC ACCESS TOKEN | PAT } <token_name>
  [ ROLE_RESTRICTION = '<string_literal>' ]
  [ DAYS_TO_EXPIRY = <integer> ]
  [ MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT = <integer> ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`ADD { PROGRAMMATIC ACCESS TOKEN | PAT } token_name`
:   Creates a programmatic access token with the specified name.

    You can use the keyword PAT as a shorter way of specifying the keywords PROGRAMMATIC ACCESS TOKEN.

## Optional parameters

`username`
:   The name of the user that the token is associated with. A user cannot use another user’s programmatic access token to
    authenticate.

    To create programmatic access tokens on behalf of a user, administrators must specify the name of that user in the ALTER USER
    command.

    If `username` is omitted, the command generates a programmatic access token for the user who is currently logged in (the
    active user of this session).

`ROLE_RESTRICTION = 'string_literal'`
:   The name of the role used for privilege evaluation and object creation. This must be one of the roles that has already been
    granted to the user.

    > **Note:**
    >
    > This parameter is required if the user is a service user (if the USER object has TYPE=SERVICE).

    When you use this token for authentication, any objects that you create are owned by this role, and this role is used for
    privilege evaluation.

    > **Note:**
    >
    > Secondary roles are not used, even if [DEFAULT_SECONDARY_ROLES](create-user.md) is set to
    > (‘ALL’) for the user.

    If this role is revoked from the user associated with the programmatic access token, any attempts to use the token for
    authentication will fail.

    > **Note:**
    >
    > Specifying a role as the ROLE_RESTRICTION value does not grant the specified role to the programmatic access token. The user
    > must have already been granted this role.

    If you omit ROLE_RESTRICTION, any objects that you create owned by your primary role, and privileges are evaluated against
    your primary and secondary roles (as explained in [Authorization through primary role and secondary roles](../../user-guide/security-access-control-overview.md)).

`DAYS_TO_EXPIRY = integer`
:   The number of days that the programmatic access token can be used for authentication.

    You can specify a value ranging from `1` to the [maximum expiration time](../../user-guide/programmatic-access-tokens.md).

    Default: `15`

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

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MODIFY PROGRAMMATIC AUTHENTICATION METHODS | User | Required only when generating a programmatic access token for a user other than yourself. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The command output provides information about the newly generated programmatic access token in the following columns:

| Column | Description |
| --- | --- |
| `token_name` | Name of the generated token. |
| `token_secret` | The token itself. Use this to authenticate to an endpoint.  **Note:** The token only appears in the output of the ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN command. No other SQL command or function prints out or returns the token.  If you need to access this token programmatically, you can use [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) to execute this command and retrieve the token from the [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md). |

## Usage notes

* Each user can have a maximum of 15 programmatic access tokens.

  * This number includes [tokens that have been disabled](../../user-guide/programmatic-access-tokens.md).
  * This number does not include tokens that have expired.

## Examples

Create a programmatic access token named `example_token` that is associated with the user `example_user`, and inherits all
privileges from the associated user:

```sqlexample
ALTER USER IF EXISTS example_user ADD PROGRAMMATIC ACCESS TOKEN example_token
  COMMENT = 'a reference example';
```

Create a programmatic access token named `example_token` that is associated with the user `example_user`, inherits all
privileges from the role `example_role`, and expires after 15 days:

```sqlexample
ALTER USER IF EXISTS example_user ADD PROGRAMMATIC ACCESS TOKEN example_token
  ROLE_RESTRICTION = 'example_role'
  DAYS_TO_EXPIRY = 15;
```
