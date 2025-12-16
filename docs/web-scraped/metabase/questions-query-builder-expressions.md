# Source: https://www.metabase.com/docs/latest/questions/query-builder/expressions

<div>

1.  [Home](/docs/latest/)
2.  [Questions](/docs/latest/questions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Custom expressions

![Custom expression editor](../images/custom-expression-editor.png)

[Custom expressions](./expressions-list) are like formulas in spreadsheet software like Excel, Google Sheets, and LibreOffice Calc. They are the power tools in the query builder's editor that allow you to ask more complicated questions.

You can also skip to the [complete list of expressions](./expressions-list).

## Custom expressions to create filters, metrics, and custom columns

To use the custom expression editor, create a **Custom Column** (where the custom expression is used as a Field Formula to calculate values for the new column), or click on **Filter** or **Summarize** and select **Custom Expression**.

When using the query builder, you can use expressions to create new:

-   **Custom columns**. You could use `[Subtotal] / [Quantity]` to create a new column, which you could name "Item price".
-   **Filters**. The expression `contains([comment], "Metabase")` would filter for rows where the `comment` field contained the word "Metabase".
-   **Summaries**. Also known as metrics or aggregations. `Share([Total] > 50)` would return the percentage of orders with totals greater than 50 dollars.

Type in your expression, give it a name, and click **Done**. If the Done button is grayed out, check that your expression is valid, and that you've given the expression a name (which you enter at the bottom of the expression editor).

This page covers the basics of expressions. You can check out a [full list of expressions](./expressions-list) in Metabase, or walk through a tutorial that shows you how you can use [custom expressions in the notebook editor](/learn/metabase-basics/querying-and-dashboards/questions/custom-expressions).

## Types of expressions

There are two basic types of expressions, **Aggregations** and **Functions**. Check out a [full list of expressions](./expressions-list).

### Aggregations

[Aggregations](./expressions-list#aggregations) take values from multiple rows to perform a calculation, such as finding the average value from all values in a column. Aggregations functions can only be used in the **Summarize** section of the notebook editor, because aggregations use values from all rows for that column. So while you could create a custom column with the formula `[Subtotal] + [Tax]`, you could *not* write `Sum([Subtotal] + [Tax])`, unless you were creating a custom metric expression (that would add up all the subtotals and taxes together).

### Functions

[Functions](./expressions-list#functions), by contrast, do something to each value in a column, like searching for a word in each value (`contains`), rounding each value up to the nearest integer (the `ceil` function), and so on.

## Function browser

![Function browser](../images/function-browser.png)

The expression editor includes a function browser to help you find the function you need. To view the browser, flick on the **f** on the right of the expression editor. See also a [list of functions and aggregations](./expressions-list).

## Auto-format

![Auto-format expression](../images/auto-format.png)

To format expressions, click on the auto-format button on the right side of the expression editor (the lightning bolt wrapped in braces).

## Basic mathematical operators

Use `+`, `-`, `*` (multiply), `/` (divide) on numeric columns with numeric values, like integers, floats, and double. You can use parentheses, `(` and `)`, to group parts of your expression.

For example, you could create a new column that calculates the difference between the total and subtotal of a order: `[Total] - [Subtotal]`.

To do math on timestamp columns, you can use [Date functions](expressions-list#date-functions) like [dateDiff](./expressions/datetimediff).

## Conditional and Boolean logic operators 

Comparison operators:

-   `>`
-   `>=` (greater than or equal to)
-   `<`
-   `<=` (less than or equal to)
-   `=`
-   `!=` (not equal to)

Boolean operators for logical conjunction, disjunction, and negation:

-   `AND`
-   `OR`
-   `NOT`

For example, you could create a filter for customers from California or Vermont: `[State] = "CA" OR [State] = "VT"`.

You can also use conditionals with the `case` function (alias `if`):

``` highlight
case([Size] = "L", "LARGE", [SIZE] = "M", "MEDIUM", "SMALL")
```

See [`case`](./expressions/case).

## Referencing other columns

You can refer to columns in the current table, or to columns that are linked via a foreign key relationship. Column names should be included inside of square brackets, like this: `[Name of Column]`. Columns in connected tables can be referred to like this: `[ConnectedTableName.Column]`.

## Referencing Segments and Metrics

You can refer to saved [metrics](../../data-modeling/metrics) and [segments](../../data-modeling/segments) that are present in the currently selected table. You write these out the same as with columns, like this: `[Valid User Sessions]`.

## Filter expressions and conditionals

Some things to keep in mind about filter expressions and conditionals:

-   Filter expressions are different in that they must return a Boolean value (something that's either true or false). For example, you could write `[Subtotal] + [Tax] < 100`. Metabase would look at each row, add its subtotal and tax, the check if that sum is greater than 100. If it is, the statement evaluates as true, and Metabase will include the row in the result. If instead you were to (incorrectly) write `[Subtotal] + [Tax]`, Metabase wouldn't know what to do, as that expression doesn't evaluate to true or false.
-   The arguments of logic operators such as `AND` and `OR` must be Boolean. For example, '\[Subtotal\] \< 100 AND \[Tax\] \> 12\`.
-   You can use functions inside of the conditional portion of the `CountIf` and `SumIf` aggregations, like so: `CountIf( round([Subtotal]) > 100 OR floor([Tax]) < 10 )`.

## Working with dates in filter expressions

If you want to work with dates in your filter expressions, the dates need to follow the format, `"YYYY-MM-DD"` --- i.e., four characters for the year, two for the month, and two for the day, enclosed in quotes `"` and separated by dashes `-`.

Example:

`between([Created At], "2020-01-01", "2020-03-31") OR [Received At] > "2019-12-25"`

This expression would return rows where `Created At` is between January 1, 2020 and March 31, 2020, or where `Received At` is after December 25, 2019.

## List of expressions

See a full list of [expressions](./expressions-list).

For a tutorial on expressions, see [Custom expressions in the query builder](/learn/metabase-basics/querying-and-dashboards/questions/custom-expressions).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/query-builder/expressions.md) ]