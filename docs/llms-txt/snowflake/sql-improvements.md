# Source: https://docs.snowflake.com/en/release-notes/sql-improvements.md

# SQL improvements

Snowflake is continually introducing enhancements that make it easier to write queries. With these new keywords and functions,
you can write simpler, shorter SELECT statements.

## SQL improvements in 2025

The following SQL improvements were introduced in 2025:

| Date released | Improvement | Impact |
| --- | --- | --- |
| October 2025 | Directed joins are now generally available and are no longer in preview. You can enforce join ordering when you run a query with the [JOIN](../sql-reference/constructs/join.md) clause by adding the `DIRECTED` keyword. | You can more easily migrate workloads into Snowflake that have join order directives and possibly improve performance by scanning joined tables in a specific order. |
| October 2025 | In [PIVOT](../sql-reference/constructs/pivot.md) queries, you can use the AS clause to specify aliases for the pivot column names. In [UNPIVOT](../sql-reference/constructs/unpivot.md) queries, you can use the AS clause to specify aliases for column names that appear in the result of the UNPIVOT operation. | The AS clause makes it easier to customize column names that appear in the output for PIVOT and UNPIVOT operations. |
| October 2025 | You can use the `WHEN MATCHED ... THEN ALL BY NAME` and `WHEN NOT MATCHED ... THEN ALL BY NAME` subclauses in the [MERGE](../sql-reference/sql/merge.md) command to update or insert all columns in the target table with changes from the source. | When the target table and the source have the same number of columns and the same names for these columns, you can use these subclauses to avoid maintaining column lists in the INSERT and UPDATE clauses of MERGE statements. |
| September 2025 | You can use the [RESAMPLE](../sql-reference/constructs/resample.md) clause and a set of [interpolation functions](../sql-reference/functions/interpolate_bfill.md) to fill gaps in time-series data. | This SQL functionality simplifies the process of generating continuous, uniformly-sampled time-series data. |
| August 2025 | Preview support for directed joins. You can enforce join ordering when you run a query with the [JOIN](../sql-reference/constructs/join.md) clause by adding the `DIRECTED` keyword. | You can more easily migrate workloads into Snowflake that have join order directives and possibly improve performance by scanning joined tables in a specific order. |
| July 2025 | You can specify the [ORDER BY ALL](../sql-reference/constructs/order-by.md) clause to sort by all columns specified in the SELECT list. | You can sort results by all columns in the SELECT list without having to specify each column by name. |
| June 2025 | You can use the [UNION BY NAME operator](../sql-reference/operators-query.md) to combine rows by name instead of by position. | The UNION BY NAME operator simplifies combining subsets of columns that have different positions in the tables. |
| May 2025 | You can use the [pipe operator](../sql-reference/operators-flow.md) (`->>`) to chain SQL statements together. In the chain of SQL statements, the results of one statement can serve as the input to another statement. | The pipe operator can simplify the execution of dependent SQL statements and improve the readability and flexibility of complex SQL operations. |
| March 2025 | You can use the [spread operator](../sql-reference/operators-expansion.md) (`**`) to expand an array into a list of individual values. | The spread operator can simplify function calls and queries that accept a variable number of values. For more information, see the [Snowflake Introduces SQL Spread Operator (\*\*)](https://www.snowflake.com/en/engineering-blog/sql-spread-operator/) blog post. |
| February 2025 | The [SEARCH](../sql-reference/functions/search.md) function supports conjunctive (AND) semantics. | When you specify `'AND'` for the SEARCH_MODE argument, there is a match if the tokens extracted from at least one of the columns or fields being searched match all of the tokens extracted from the search string. |
| January 2025 | Support for row-based and range-based window frames in the [ARRAY_AGG](../sql-reference/functions/array_agg.md) function. | Users can aggregate subsets of data by collecting the values from moving window frames into an array. |

## SQL improvements in 2024

The following SQL improvements were introduced in 2024:

| Date released | Improvement | Impact |
| --- | --- | --- |
| November 2024 | [Full-text search](../user-guide/querying-with-search-functions.md) with the [SEARCH](../sql-reference/functions/search.md) and [SEARCH_IP](../sql-reference/functions/search_ip.md) functions is now generally available and is no longer in preview. | You can find character data (text) and IPv4 addresses in specified columns from one or more tables, including fields in VARIANT, OBJECT, and ARRAY columns. |
| October 2024 | Support for querying objects up to 128 MB in files on a stage. | You can more easily reduce the size of an object before storing it in a column. Also, with the 9.17 release, you can now store objects larger than 16 MB in a column. For more information, see [Size limits for database objects](../user-guide/data-load-considerations-prepare.md). |
| October 2024 | Support for [higher-order functions](../user-guide/querying-semistructured.md) extended with the [REDUCE](../sql-reference/functions/reduce.md) function. | You can use lambda expressions to reduce semi-structured and structured data, providing a concise, readable, and efficient way to perform data manipulation and advanced analysis. |
| September 2024 | Support for [selecting from a stored procedure](../developer-guide/stored-procedure/stored-procedures-selecting-from.md) that returns tabular data. | You can simplify the SQL statements for saving results to a table. For example, rather than using the [SQLID](../developer-guide/snowflake-scripting/query-id.md) Snowflake Scripting variable with the [RESULT_SCAN](../sql-reference/functions/result_scan.md) function to create a table containing the query results, you can use a query that directly selects from the results. |
| September 2024 | Support extended for [RANGE BETWEEN window frames with explicit offsets](../sql-reference/functions-window-syntax.md) (n PRECEDING and n FOLLOWING) to include the [FIRST_VALUE](../sql-reference/functions/first_value.md) and [LAST_VALUE](../sql-reference/functions/last_value.md) window functions. | You can use additional functions to run moving aggregations when expected or unexpected missing records cause gaps to occur in time-series data sets. |
| August 2024 | [RANGE BETWEEN window frames with explicit offsets](../sql-reference/functions-window-syntax.md) (n PRECEDING and n FOLLOWING) are now generally available and are no longer in preview. | You can more easily run moving aggregations when expected or unexpected missing records cause gaps to occur in time-series data sets. |
| August 2024 | Preview support for [full-text search](../user-guide/querying-with-search-functions.md) with the [SEARCH](../sql-reference/functions/search.md) function and the [SEARCH_IP](../sql-reference/functions/search_ip.md) function. | You can find character data (text) and IPv4 addresses in specified columns from one or more tables, including fields in VARIANT, OBJECT, and ARRAY columns. |
| August 2024 | Support for using the ILIKE and EXCLUDE keywords for filtering in a SELECT list or GROUP BY clause in [function calls](2024/8_30.md) and [object constants](../sql-reference/data-types-semistructured.md). | In function calls and object constants, you can filter for columns that match a pattern, and you can exclude specific columns. |
| July 2024 | Support for specifying wildcards in [OBJECT constants](../sql-reference/data-types-semistructured.md) for filtering in a SELECT list or GROUP BY clause. | You can construct an OBJECT value from the specified data using the attribute names as keys and the associated values as values. |
| June 2024 | Preview support for [RANGE BETWEEN window frames with explicit offsets](../sql-reference/functions-window-syntax.md) (n PRECEDING and n FOLLOWING) for the following window functions: [AVG](../sql-reference/functions/avg.md), [COUNT](../sql-reference/functions/count.md), [MIN](../sql-reference/functions/min.md), [MAX](../sql-reference/functions/max.md) and [SUM](../sql-reference/functions/sum.md). | You can more easily run moving aggregations when expected or unexpected missing records cause gaps to occur in time-series data sets. |
| May 2024 | Support for using the `{ INCLUDE | EXCLUDE } NULLS` option in an [UNPIVOT](../sql-reference/constructs/unpivot.md) subclause to specify whether to include rows with NULL values in the results. | You have more flexibility when you use the UNPIVOT subclause in a SQL statement. |
| May 2024 | Support for using the TABLE keyword to [get a reference to a table, view, secure view, or query](../developer-guide/stored-procedure/stored-procedures-calling-references.md) and to [call a method in a class in the FROM clause](../sql-reference/snowflake-db-classes.md). | You can use the TABLE keyword to write simpler SQL statements. |
| May 2024 | New [ASOF JOIN](../sql-reference/constructs/asof-join.md) construct. | You can write simpler SQL statements to join tables that contain [time-series data](../user-guide/querying-time-series-data.md). |
| May 2024 | Support for specifying the ANY keyword or a subquery with the [PIVOT](../sql-reference/constructs/pivot.md) construct. | You can easily pivot on all distinct values or on all values returned by a subquery. |
| May 2024 | Support for the [FILTER](../sql-reference/functions/filter.md) and [TRANSFORM](../sql-reference/functions/transform.md) [higher-order functions](../user-guide/querying-semistructured.md). | You can use lambda expressions to filter and transform semi-structured and structured data, providing a concise, readable, and efficient way to perform data manipulation and advanced analysis. |
| March 2024 | New [GREATEST_IGNORE_NULLS](../sql-reference/functions/greatest_ignore_nulls.md) and [LEAST_IGNORE_NULLS](../sql-reference/functions/least_ignore_nulls.md) functions. | You can return the lowest or highest non-NULL value from a list of expressions. |
| March 2024 | Support for trailing commas in [SELECT](../sql-reference/sql/select.md) lists. | You can delete or move the last columns in a SELECT list without having to delete the preceding comma. |
| February 2024 | Support for the `upper`, `lower`, and `trim` [collations](../sql-reference/collation.md) in [additional SQL functions](../sql-reference/collation.md). | You can pass strings that use the `upper`, `lower`, and `trim` collations to these functions without having to change the collation. |

## SQL improvements in 2023

The following SQL improvements were introduced in 2023:

| Date released | Improvement | Impact |
| --- | --- | --- |
| August 2023 | New [ARRAY_MIN](../sql-reference/functions/array_min.md), [ARRAY_MAX](../sql-reference/functions/array_max.md), and [ARRAY_SORT](../sql-reference/functions/array_sort.md) functions. | You can now easily select the array elements with the lowest value and the highest value.  You can easily get a sorted array of elements. |
| August 2023 | New ILIKE and REPLACE parameters in the [SELECT](../sql-reference/sql/select.md) command. | You can now select all columns that match a pattern containing SQL wildcards.  When selecting all columns, you can replace the value of specific columns with expressions. |
| July 2023 | New ALL keyword in the [GROUP BY](../sql-reference/constructs/group-by.md) construct. | You can group results by all non-aggregate columns in the SELECT list without having to specify each column by name. |
| February 2023 | Support for bankers’ rounding ([rounding half to even](https://en.wikipedia.org/wiki/Rounding#Rounding_half_to_even)) in the [ROUND](../sql-reference/functions/round.md) function. | You can now use bankers’ rounding when rounding values. |
| January 2023 | New [MIN_BY](../sql-reference/functions/min_by.md) and [MAX_BY](../sql-reference/functions/max_by.md) functions. | You can find the row containing the minimum or maximum value in a column and retrieve the value from a different column. |

## SQL improvements in 2022

The following SQL improvements were introduced in 2022:

| Date released | Improvement | Impact |
| --- | --- | --- |
| November 2022 | New EXCLUDE and RENAME parameters in the [SELECT](../sql-reference/sql/select.md) command. | You can now select all columns and specify that you want to exclude or rename specific columns. |
| November 2022 | New [ARRAY_EXCEPT](../sql-reference/functions/array_except.md) and [ARRAY_DISTINCT](../sql-reference/functions/array_distinct.md) functions. | You can now easily select the array elements that are in one array but not in another array.  You can easily get the distinct elements in an array. |
| May 2022 | New [REGEXP_SUBSTR_ALL](../sql-reference/functions/regexp_substr_all.md) function. | You can now easily extract the substrings that match a regular expression from a string.. |
