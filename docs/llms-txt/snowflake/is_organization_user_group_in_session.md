# Source: https://docs.snowflake.com/en/sql-reference/functions/is_organization_user_group_in_session.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# IS_ORGANIZATION_USER_GROUP_IN_SESSION

Assuming a role was imported from an [organization user group](../../user-guide/organization-users.md), verifies whether the role is in the user’s
active primary or secondary role hierarchy for the session.

The function returns FALSE if the specified role is not linked to an organization user group.

See also:
:   [Advanced Column-level Security topics](../../user-guide/security-column-advanced.md)

## Syntax

> ```sqlsyntax
> IS_ORGANIZATION_USER_GROUP_IN_SESSION( '<string_literal>' )
> ```

## Arguments

`'string_literal'`
:   The name of an role.

## Returns

`TRUE`
:   The current user’s active [primary role or secondary roles](../../user-guide/security-access-control-overview.md) in the session inherit the
    privileges of the specified role.

    When the `DEFAULT_SECONDARY_ROLES` value is `ALL`, any role granted to the user inherits the privileges of the
    specified role.

    The specified role can be the current primary role or secondary role (that is, the roles returned by
    [CURRENT_ROLE](current_role.md) or [CURRENT_SECONDARY_ROLES](current_secondary_roles.md), respectively) or any role
    lower in the role hierarchy.

`FALSE`
:   Either of the following:

    * The specified role is a local role that is not linked to an organization user group.
    * The specified role is either higher in the role hierarchy of the current primary or secondary roles
      or is not in the role hierarchy at all.

`NULL`
:   In a data sharing consumer account, this function returns NULL if referencing a shared object (e.g. secure UDF or secure view), such
    as in a masking policy condition. This behavior prevents exposing the role hierarchy in a data sharing consumer account.

## Usage notes

The IS_ORGANIZATION_USER_GROUP_IN_SESSION function is similar to the [IS_DATABASE_ROLE_IN_SESSION](is_database_role_in_session.md) and
[IS_ROLE_IN_SESSION](is_role_in_session.md) functions. The following usage notes apply to all of these context functions:

* Use one syntax.
* Name syntax:

  * Only one role name can be passed as an argument.
  * The argument must be a string and use the same casing as how the role is stored in Snowflake. For details, see
    [Identifier requirements](../identifiers-syntax.md).
* Column syntax:

  * Only one column can be passed as an argument.
  * The column must have a [STRING](../data-types-text.md) data type.
  * Specify the column as one of the following:

    * `column_name`
    * `table_name.column_name`
    * `schema_name.table_name.column_name`
    * `database_name.schema_name.table_name.column_name`
* Virtual columns:

  A virtual column, which contains the result of a calculated value from an expression rather than the calculated value being stored in the
  table, is not supported.

  ```sqlexample
  SELECT IS_ROLE_IN_SESSION(UPPER(authz_role)) FROM t1;
  ```

  A virtual column is supported only when the expression has an alias for the column name:

  ```sqlexample
  CREATE VIEW v2 AS
  SELECT
    authz_role,
    UPPER(authz_role) AS upper_authz_role
  FROM t2;

  SELECT IS_ROLE_IN_SESSION(upper_authz_role) FROM v2;
  ```

* Policies:

  If you use these functions with a [masking policy](../../user-guide/security-column-intro.md) or
  [row access policy](../../user-guide/security-row-intro.md), verify that your Snowflake account is Enterprise Edition or higher.

  Snowflake recommends using this function when the policy conditions need to evaluate role hierarchy and inherited privileges.
* Result cache:

  If you use this function in a masking policy or row access policy and neither the policy nor the table or column protected by the policy
  change from a previous query, you can use the [RESULT_SCAN](result_scan.md) function to return the results of a query on
  the protected table. The result cache applies when using the nonliteral syntax only.
* These functions cannot be used in the materialized view definition because the functions are not deterministic and Snowflake cannot
  determine what data to materialize.

## Examples

The following example returns TRUE if the following is true:

* Role `analyst` was created or linked when an organization user group was added to the account.
* The privileges granted to the `analyst` role are inherited by the current role in the session.

```sqlexample
SELECT IS_ORGANIZATION_USER_GROUP_IN_SESSION('ANALYST');
```
