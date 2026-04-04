# Source: https://docs.snowflake.com/en/sql-reference/constructs/from.md

Categories:
:   [Query syntax](../constructs.md)

# FROM

Specifies the tables, views, or table functions to use in a [SELECT](../sql/select.md) statement.

See also:
:   [AT | BEFORE](at-before.md) , [CHANGES](changes.md) , [CONNECT BY](connect-by.md) , [JOIN](join.md) , [ASOF JOIN](asof-join.md), [MATCH_RECOGNIZE](match_recognize.md), [PIVOT](pivot.md) ,
    [SAMPLE / TABLESAMPLE](sample.md) , [SEMANTIC_VIEW](semantic_view.md), [UNPIVOT](unpivot.md),
    [Working with joins](../../user-guide/querying-joins.md), [Analyzing time-series data](../../user-guide/querying-time-series-data.md)

## Syntax

```sqlsyntax
SELECT ...
FROM objectReference [ JOIN objectReference [ ... ] ]
[ ... ]
```

Where:

> ```sqlsyntax
> objectReference ::=
>    {
>       [<namespace>.]<object_name>
>            [ AT | BEFORE ( <object_state> ) ]
>            [ CHANGES ( <change_tracking_type> ) ]
>            [ MATCH_RECOGNIZE ]
>            [ PIVOT | UNPIVOT ]
>            [ [ AS ] <alias_name> ]
>            [ SAMPLE ]
>      | <table_function>
>            [ PIVOT | UNPIVOT ]
>            [ [ AS ] <alias_name> ]
>            [ SAMPLE ]
>      | ( VALUES (...) )
>            [ SAMPLE ]
>      | [ LATERAL ] ( <subquery> )
>            [ [ AS ] <alias_name> ]
>      | @[<namespace>.]<stage_name>[/<path>]
>            [ ( FILE_FORMAT => <format_name>, PATTERN => '<regex_pattern>' ) ]
>            [ [ AS ] <alias_name> ]
>      | DIRECTORY( @<stage_name> )
>      | SEMANTIC_VIEW( ... )
>    }
> ```

## Parameters

`JOIN`
:   Subclause that specifies to perform a join between two or more tables (or views or table functions).
    The join can be an inner join, outer join, or other type of join.
    The join can use the keyword JOIN or an alternative supported join syntax.
    For more details about joins, see [JOIN](join.md) and
    [ASOF JOIN](asof-join.md).

`[ AS ] alias_name`
:   Specifies a name given to the object reference it is attached to. Can be used with any of the other subclauses in the FROM clause.

    Alias names must follow the rules for [Object identifiers](../identifiers.md).

`VALUES`
:   The `VALUES` clause can specify literal values or expressions to be used in the `FROM` clause.
    This clause can contain table and column aliases (not shown in the diagram above).
    For more details about the VALUES clause, see [VALUES](values.md).

### Object or table function clause

`[namespace.]object_name`
:   Specifies the name of the object (table or view) being queried.

    The object name can be qualified using `namespace` (in the form of `db_name.schema_name.object_name` or `schema_name.object_name`). A namespace is not required if
    the context can be derived from the current database and schema for the session.

    When specifying a table/view name to query, you can also specify the following optional subclause:

    > `{ AT | BEFORE } ( object_state )`
    > :   Optional subclause that specifies the time-based or event-based historical state of the table or view for Time Travel. For more details, see [AT | BEFORE](at-before.md).
    >
    > `MATCH_RECOGNIZE`
    > :   Optional subclause for finding sequences of rows that match a pattern. For more details, see [MATCH_RECOGNIZE](match_recognize.md).

`table_function`
:   Specifies a system-defined table function, a UDF table function, or a class method to call within the FROM clause. For details,
    see the following topics:

    * [Using a table function in the FROM clause](../functions-table.md)
    * [Calling a UDTF](../../developer-guide/udf/udf-calling-sql.md)
    * [Selecting columns from SQL class instance methods that return tabular data](../snowflake-db-classes.md)

`{ PIVOT | UNPIVOT }`
:   Optional subclause that specifies to pivot or unpivot the results of the FROM clause. For more details, see [PIVOT](pivot.md) and [UNPIVOT](unpivot.md).

`SAMPLE`
:   Optional subclause that specifies to sample rows from the table/view. For more details, see [SAMPLE / TABLESAMPLE](sample.md).

### Inline view clause

`[ LATERAL ] ( subquery )`
:   Specifies an inline view within the FROM clause. If the optional `LATERAL` keyword is used, then the
    `subquery` can refer to columns from other tables (or views or table functions) that are in the current
    FROM clause and to the left of the inline view.

    For more information about subqueries in general, see [Working with Subqueries](../../user-guide/querying-subqueries.md).

### Staged file clause

`@[namespace.]stage_name[/path]`
:   Specifies a named stage to be queried (or `~` for referring to the stage for the current user or `%` followed by a table name for referring to the stage for the specified table).

    When querying a stage, you can also optionally specify a named file format and pattern:

    > `( FILE_FORMAT => format_name [ , PATTERN => 'regex_pattern' ] )`
    > :   Specifies a named file format object to use for the stage and a pattern to filter the set of files in the stage.

    For more details about querying stages, see [Query data in staged files](../../user-guide/querying-stage.md).

### Directory table clause

`DIRECTORY( @stage_name )`
:   Specifies the name of a stage that includes a [directory table](../../user-guide/data-load-dirtables.md).

### Hierarchical query result

`hierarchical_query_result`
:   A hierarchical query result is the result set from using a clause such as CONNECT BY to query a table of hierarchical
    data. For more details, see [CONNECT BY](connect-by.md).

### Semantic view clause

`SEMANTIC_VIEW(...)`
:   Specifies the [semantic view](../../user-guide/views-semantic/overview.md) that you want to
    [query](../../user-guide/views-semantic/querying.md). For information, see [SEMANTIC_VIEW](semantic_view.md).

## Usage notes

* Object names are SQL identifiers. They are case-insensitive by default. To preserve case, enclose them between double quotes
  (`" "`).

## Examples

Create a table and load data into it:

> ```sqlexample
> CREATE TABLE ftable1 (retail_price FLOAT, wholesale_cost FLOAT, description VARCHAR);
> INSERT INTO ftable1 (retail_price, wholesale_cost, description)
>   VALUES (14.00, 6.00, 'bling');
> ```

Here is a basic example of using the FROM clause:

> ```sqlexample
> SELECT description, retail_price, wholesale_cost
>     FROM ftable1;
> +-------------+--------------+----------------+
> | DESCRIPTION | RETAIL_PRICE | WHOLESALE_COST |
> |-------------+--------------+----------------|
> | bling       |           14 |              6 |
> +-------------+--------------+----------------+
> ```

This example is identical to the previous example, but specifies the table name qualified by the schema for the table:

> ```sqlexample
> SELECT description, retail_price, wholesale_cost
>     FROM temporary_doc_test.ftable1;
> +-------------+--------------+----------------+
> | DESCRIPTION | RETAIL_PRICE | WHOLESALE_COST |
> |-------------+--------------+----------------|
> | bling       |           14 |              6 |
> +-------------+--------------+----------------+
> ```

This example creates an inline view and then uses it in the query:

> ```sqlexample
> SELECT v.profit
>     FROM (SELECT retail_price - wholesale_cost AS profit FROM ftable1) AS v;
> +--------+
> | PROFIT |
> |--------|
> |      8 |
> +--------+
> ```

This example queries a sample of 10% of the data in the table:

> ```sqlexample
> SELECT *
>     FROM sales SAMPLE(10);
> ```

This example executes a UDTF (user-defined table function):

> ```sqlexample
> SELECT *
>     FROM TABLE(Fibonacci_Sequence_UDTF(6.0::FLOAT));
> ```

These examples use an `AT` clause to return historical data from the following specified points in the past:

> * One day earlier than the current time (`-86400 = -3600 * 24`).
> * Specific time and day.
>
> ```sqlexample
> SELECT *
>     FROM sales AT(OFFSET => -86400);
> SELECT *
>     FROM sales AT(TIMESTAMP => '2018-07-27 12:00:00'::TIMESTAMP);
> ```
>
> For more details about `AT`, see [AT | BEFORE](at-before.md).

This example queries files located in a named stage:

> ```sqlexample
> SELECT
>     v.$1, v.$2, ...
>   FROM
>     @my_stage( FILE_FORMAT => 'csv_format', PATTERN => '.*my_pattern.*') v;
> ```

This example retrieves all metadata columns in a [directory table](../../user-guide/data-load-dirtables.md) for a stage named `mystage`:

> ```sqlexample
> SELECT * FROM DIRECTORY(@mystage);
> ```

This example retrieves the FILE_URL column values from a directory table for files greater than 100 K bytes in size:

> ```sqlexample
> SELECT FILE_URL FROM DIRECTORY(@mystage) WHERE SIZE > 100000;
> ```

This example retrieves the FILE_URL column values from a directory table for comma-separated value files:

> ```sqlexample
> SELECT FILE_URL FROM DIRECTORY(@mystage) WHERE RELATIVE_PATH LIKE '%.csv';
> ```
