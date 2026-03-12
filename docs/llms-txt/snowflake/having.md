# Source: https://docs.snowflake.com/en/sql-reference/constructs/having.md

Categories:
:   [Query syntax](../constructs.md)

# HAVING

Filters rows produced by [GROUP BY](group-by.md) that do not satisfy a predicate.

## Syntax

```sqlsyntax
SELECT ...
FROM ...
GROUP BY ...
HAVING <predicate>
[ ... ]
```

## Parameters

`predicate`
:   A [Boolean expression](../data-types-logical.md).

## Usage notes

* The condition specified by the HAVING clause applies to expressions produced by the [GROUP BY](group-by.md).
  Therefore, the same restrictions that apply to [GROUP BY](group-by.md) expressions also apply to the HAVING
  clause. The predicate can only refer to:

  > * Constants.
  > * Expressions that appear in [GROUP BY](group-by.md).
  > * [Aggregate functions](../functions-aggregation.md).
* Expressions in the [SELECT](../sql/select.md) list can be referred to by the column alias defined in the list.

## Examples

Find the departments that have fewer than 10 employees:

> ```sqlexample
> SELECT department_id
> FROM employees
> GROUP BY department_id
> HAVING count(*) < 10;
> ```
