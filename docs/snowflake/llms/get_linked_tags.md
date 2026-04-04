# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_linked_tags.md

# <budget_name>!GET_LINKED_TAGS

List the tags that have been added to a [custom budget](../../../../user-guide/budgets.md).

> **Important:**
>
> This method has been deprecated. Use [<budget_name>!GET_BUDGET_SCOPE](get_budget_scope.md) instead.

## Syntax

```sqlsyntax
<budget_name>!GET_LINKED_TAGS()
```

## Returns

The method returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| TAG_ID | NUMBER | System-generated identifier. |
| TAG_VALUE | VARCHAR | Value of the tag. |
| TAG_DATABASE | VARCHAR | Database that contains the tag. |
| TAG_SCHEMA | VARCHAR | Schema that contains the tag. |
| TAG_NAME | VARCHAR | Name of the tag. |

## Access control requirements

The following minimum privileges and roles are required to view results for custom budgets:

* ADMIN or VIEWER [instance role](../../../../user-guide/budgets.md) for the budget instance.
* USAGE privilege on the database and schema that contains the budget instance.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* This method can only be called on *custom budget* instances.
* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.

## Example

Get all tags that were added to the `budget_db.budget_schema.my_budget` budget:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_LINKED_TAGS();
```
