# Source: https://docs.snowflake.com/en/sql-reference/ternary-logic.md

# Ternary logic

As specified in the SQL standard, ternary logic, or three-valued logic (3VL), is a logic system with three truth values: TRUE, FALSE, and UNKNOWN. In Snowflake, UNKNOWN is represented by NULL. Ternary logic
applies to the evaluation of Boolean expressions, as well as predicates, and affects the results of logical operations such as AND, OR, and NOT:

* When used in expressions (for example, in a [SELECT](sql/select.md) list), UNKNOWN results are returned as NULL values.
* When used as a predicate (for example, in a [WHERE](constructs/where.md) clause), UNKNOWN results evaluate to FALSE.

## Truth tables

This section describes the truth tables for the [comparison](operators-comparison.md) and [logical](operators-logical.md) operators.

### Comparison operators

If any operand for a comparison operator is NULL, the result is NULL. The comparison operators and functions are:

* `=` , `!=` , `<>`
* `<` , `<=` , `>` , `>=`
* [GREATEST](functions/greatest.md), [LEAST](functions/least.md)

### Logical operators

Given a BOOLEAN column `C`:

| If `C` is: | `C AND NULL` evaluates to: | `C OR NULL` evaluates to: | `NOT C` evaluates to: |
| --- | --- | --- | --- |
| TRUE | NULL | TRUE | FALSE |
| FALSE | FALSE | NULL | TRUE |
| NULL | NULL | NULL | NULL |

In addition:

| If `C` is: | `C AND (NOT C)` evaluates to: | `C OR (NOT C)` evaluates to: | `NOT (C OR NULL)` evaluates to: |
| --- | --- | --- | --- |
| TRUE | FALSE | TRUE | FALSE |
| FALSE | FALSE | TRUE | NULL |
| NULL | NULL | NULL | NULL |

## Usage notes for conditional expressions

This section describes behavior specific to conditional expressions.

### IFF behavior

[IFF](functions/iff.md) returns the following results for ternary logic. Given a BOOLEAN column `C`:

| If `C` is: | `IFF(C, e1, e2)` evaluates to: |
| --- | --- |
| TRUE | `e1` |
| FALSE | `e2` |
| NULL | `e2` |

### [ NOT ] IN behavior

[[ NOT ] IN](functions/in.md) returns the following results for ternary logic. Given 3 numeric columns `c1`, `c2`, and `c3`:

* `c1 IN (c2, c3, ...)` is syntactically equivalent to `(c1 = c2 OR c1 = c3 OR ...)`.

  As a result, when the value of `c1` is NULL, the expression `c1 IN (c2, c3, NULL)` always evaluates to NULL.
* `c1 NOT IN (c2, c3, ... )` is syntactically equivalent to `(c1 <> c2 AND c1 <> c3 AND ...)`.

  Therefore, even if `c1 NOT IN (c2, c3)` is TRUE, `c1 NOT IN (c2, c3, NULL)` evaluates to NULL.
