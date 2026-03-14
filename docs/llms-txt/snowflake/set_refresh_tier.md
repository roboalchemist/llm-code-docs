# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/set_refresh_tier.md

# <budget_name>!SET_REFRESH_TIER

Sets the [refresh interval of a budget](../../../../user-guide/budgets.md). The budget refresh interval controls how long it takes for a
budget to be refreshed with the most current consumption data.

See also:
:   [<budget_name>!GET_REFRESH_TIER](get_refresh_tier.md)

## Syntax

```sqlsyntax
<budget_name>!SET_REFRESH_TIER( '<refresh_interval>' )
```

## Arguments

`'refresh_interval'`
:   Sets the budget refresh interval. Specify one of the following values:

    * `TIER_1H`: Sets the budget refresh interval to one hour. Setting the budget refresh interval to one hour increases the cost of the
      budget.
    * `TIER_6H`: Sets the budget refresh interval to the default of up to 6.5 hours.

    Default: `TIER_6H`

## Returns

Returns a VARCHAR value that indicates whether the refresh interval was successfully updated.

## Access control requirements

The following minimum privileges and roles are required to call this method for *custom budgets*:

> * ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
> * USAGE privilege on the database and schema that contains the budget instance.

The following role is required to call this method for the *account budget*:

> * BUDGET_ADMIN [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* Setting the budget refresh interval to one hour increases the cost of the budget by a factor of 12 compared to the default interval.
* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Set the refresh interval for a custom budget to one hour:

```sqlexample
CALL my_database.my_schema.my_budget!SET_REFRESH_TIER('TIER_1H');
```

Revert the refresh interval for the same budget back to the default (6.5 hours):

```sqlexample
CALL my_database.my_schema.my_budget!SET_REFRESH_TIER('TIER_6H');
```

Set the account root budget to the one-hour interval:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_REFRESH_TIER('TIER_1H');
```
