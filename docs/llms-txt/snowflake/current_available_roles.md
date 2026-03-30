# Source: https://docs.snowflake.com/en/sql-reference/functions/current_available_roles.md

Categories:
:   [Context functions](../functions-context.md)

# CURRENT_AVAILABLE_ROLES

Returns a list of all account-level roles granted to the current user. The list includes all roles that are granted
directly to the user plus all account-level roles lower in the hierarchies of these roles.

See also:
:   [CURRENT_ROLE](current_role.md) , [CURRENT_SECONDARY_ROLES](current_secondary_roles.md) , [IS_ROLE_IN_SESSION](is_role_in_session.md)

## Syntax

```sqlsyntax
CURRENT_AVAILABLE_ROLES()
```

## Arguments

None.

## Returns

Returns a string (VARCHAR) that is a JSON-encoded list of available account-level roles. The returned value can be
passed to the [PARSE_JSON](parse_json.md) function to get a VARIANT that contains a list of all the
available roles.

## Usage notes

* This function returns a list of account-level roles only when queried by a user. Querying the function using a service that has no active
  user could result in a failed query. For example, the function does not return a list of roles when queried within a
  [task](../../user-guide/tasks-intro.md), because the task runs are executed by a system service that is not associated with a user. In this
  case, the query could time out because the query plan cannot be completed.
* This function does not return the names of database roles, application roles, or class instance roles.
* This function does not account for role activation in a session.

  For example, if specifying this function in the conditions of a [masking policy](../../user-guide/security-column-intro.md) or a
  [row access policy](../../user-guide/security-row-intro.md), the policy might inadvertently restrict access.

  If role activation and role hierarchy is necessary in the policy conditions, use [IS_ROLE_IN_SESSION](is_role_in_session.md).

## Examples

Return the list of roles granted to the current user:

> ```sqlexample
> SELECT CURRENT_AVAILABLE_ROLES();
>
> +----------------------------------------------------------+
> | ROW | CURRENT_AVAILABLE_ROLES()                          |
> +-----+----------------------------------------------------+
> |  1  | [ "PUBLIC", "ANALYST", "DATA_ADMIN", "DATA_USER" ] |
> +-----+----------------------------------------------------+
> ```

Use the PARSE_JSON function to return a VARIANT and the [FLATTEN](flatten.md) function to obtain a single row for each role:

> ```sqlexample
> SELECT INDEX,VALUE,THIS FROM TABLE(FLATTEN(input => PARSE_JSON(CURRENT_AVAILABLE_ROLES())));
>
> +-----+-------+------------------------+---------------------------+
> | ROW | INDEX | VALUE                  | THIS                      |
> +-----+-------+------------------------+---------------------------+
> |   1 |     0 | "PUBLIC"               | [                         |
> |     |       |                        |   "PUBLIC",               |
> |     |       |                        |   "ANALYST",              |
> |     |       |                        |   "DATA_ADMIN",           |
> |     |       |                        |   "DATA_USER"             |
> |     |       |                        | ]                         |
> +-----+-------+------------------------+---------------------------+
> |   2 |     1 | "ANALYST"              | [                         |
> |     |       |                        |   "PUBLIC",               |
> |     |       |                        |   "ANALYST",              |
> |     |       |                        |   "DATA_ADMIN",           |
> |     |       |                        |   "DATA_USER"             |
> |     |       |                        | ]                         |
> +-----+-------+------------------------+---------------------------+
> |   3 |     2 | "DATA_ADMIN"           | [                         |
> |     |       |                        |   "PUBLIC",               |
> |     |       |                        |   "ANALYST",              |
> |     |       |                        |   "DATA_ADMIN",           |
> |     |       |                        |   "DATA_USER"             |
> |     |       |                        | ]                         |
> +-----+-------+------------------------+---------------------------+
> |   4 |     3 | "DATA_USER"            | [                         |
> |     |       |                        |   "PUBLIC",               |
> |     |       |                        |   "ANALYST",              |
> |     |       |                        |   "DATA_ADMIN",           |
> |     |       |                        |   "DATA_USER"             |
> |     |       |                        | ]                         |
> +-----+-------+------------------------+---------------------------+
> ```
