# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/commands/create-budget.md

# CREATE BUDGET

*Fully qualified name*: SNOWFLAKE.CORE.BUDGET

Creates a new budget instance or replaces and existing budget instance in the current or
specified schema.

See also:
:   [ALTER BUDGET](alter-budget.md),
    [SHOW BUDGET](show-budget.md),
    [DROP BUDGET](drop-budget.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.CORE.BUDGET [ IF NOT EXISTS ] <name> ()
  [ [ WITH ] COMMENT = '<string_literal>' ]
```

## Parameters

`name`:
:   Specifies the identifier for the budget. The identifier must start with an alphabetic character and cannot contain spaces or
    special characters unless the identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double
    quotes are also case-sensitive.

    For more details, refer to [Identifier requirements](../../../identifiers-syntax.md).

## Optional parameters

`COMMENT = 'string_literal'`:
:   Specifies a comment for the budget.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege / Role | Object | Notes |
| --- | --- | --- |
| CREATE SNOWFLAKE.CORE.BUDGET | Schema | The role used to create a budget must be granted this privilege on the schema in which the budget is created. |
| SNOWFLAKE.BUDGET_CREATOR | Role | The role used to create a budget must be granted this [database role](../../../../user-guide/security-access-control-considerations.md). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* To refer to this class by its unqualified name, include the database and schema of the class in your
  [search path](../../../snowflake-db-classes.md).
* [Replication](../../../../user-guide/account-replication-intro.md) is supported only for instances
  of the [CUSTOM_CLASSIFIER](../../custom_classifier.md) class.
* An account can contain a maximum of 100 custom budgets.

## Examples

Create budget `my_budget` in the current schema:

```sqlexample
CREATE SNOWFLAKE.CORE.BUDGET my_budget();
```
