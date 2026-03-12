# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/refresh_usage.md

# <budget_name>!REFRESH_USAGE

Causes the budget to retrieve consumption data so that the budget can compare it to the spending limit without waiting for the next
automatic retrieval of data.

## Syntax

```sqlsyntax
<budget_name>!REFRESH_USAGE()
```

## Returns

Returns a VARCHAR value that indicates whether the usage was successfully refreshed.

## Access control requirements

The following minimum privileges and roles are required to call this method for custom budgets:

* ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
* USAGE privilege on the database and schema that contains the budget instance.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* This method can only be called on *custom budget* instances.
* It takes a few minutes for the budget to be refreshed with new usage data.
* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.

## Example

Retrieve consumption data for the `budget_db.budget_schema.my_budget` budget:

```sqlexample
CALL budget_db.budget_schema.my_budget!REFRESH_USAGE();
```
