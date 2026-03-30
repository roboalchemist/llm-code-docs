# Source: https://docs.snowflake.com/en/sql-reference/sql/create-join-policy.md

# CREATE JOIN POLICY

Creates a new [join policy](../../user-guide/join-policies.md) in the current/specified schema or replaces an existing
join policy.

After creating a join policy, assign the policy to a table using an [ALTER TABLE](alter-table.md) command or a view using an [ALTER VIEW](alter-view.md) command. Alternatively, you can assign a join policy to a table when you create it.

See also:
:   [Join policy DDL reference](../../user-guide/join-policies.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] JOIN POLICY [ IF NOT EXISTS ] <name>
  AS () RETURNS JOIN_CONSTRAINT -> <body>
  [ COMMENT = '<string_literal>' ]
```

## Parameters

`name`
:   Identifier for the join policy; must be unique for your schema.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`AS () RETURNS JOIN_CONSTRAINT`
:   Signature and return type of the policy. The signature does not accept any arguments, and the return type is JOIN_CONSTRAINT, which is an internal data type. All join policies have the same signature and return
    type.

`body`
:   SQL expression that determines the restrictions of a join policy.

    To define the body of the join policy, call the JOIN_CONSTRAINT function, which returns TRUE or FALSE.
    When the function returns TRUE, queries are required to use a join to return results.

    The syntax of the JOIN_CONSTRAINT function is:

    ```sqlsyntax
    JOIN_CONSTRAINT (
      { JOIN_REQUIRED => <boolean_expression> }
      )
    ```

    Where:

    `JOIN_REQUIRED => boolean_expression`
    :   Specifies whether a join is required in queries when data is selected from tables or views that have
        the join policy assigned to them.

    The body of a policy cannot reference user-defined functions, tables, or views.

    Allowed join columns are specified in the CREATE or ALTER statement for the table or view to which the
    policy is applied, not in the CREATE JOIN POLICY statement.

`COMMENT = 'string_literal'`
:   Adds a comment or overwrites an existing comment for the join policy.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE JOIN POLICY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For more information about join policy DDL and privileges, see [Managing join policies](../../user-guide/join-policies.md).

## Usage notes

* If you want to update an existing join policy and need to see the current body of the policy, run the
  [DESCRIBE JOIN POLICY](desc-join-policy.md) command or [GET_DDL](../functions/get_ddl.md) function.

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a join policy that requires queries to include a join (when the policy is
applied to tables and views that appear in those queries):

> ```sqlexample
> CREATE JOIN POLICY jp1 AS ()
>   RETURNS JOIN_CONSTRAINT -> JOIN_CONSTRAINT(JOIN_REQUIRED => TRUE);
> ```

Create a join policy that allows a user with the ACCOUNTADMIN role to run queries without joins;
other users must run join queries:

> ```sqlexample
> CREATE JOIN POLICY jp2 AS ()
>   RETURNS JOIN_CONSTRAINT ->
>     CASE
>       WHEN CURRENT_ROLE() = 'ACCOUNTADMIN'
>         THEN JOIN_CONSTRAINT(JOIN_REQUIRED => FALSE)
>       ELSE JOIN_CONSTRAINT(JOIN_REQUIRED => TRUE)
>     END;
> ```
