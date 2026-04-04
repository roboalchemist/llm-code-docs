# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-supported-queries.md

# Supported queries for dynamic tables

Dynamic tables support standard SQL expressions and Snowflake-supported functions, including mathematical operations, string functions, date
functions, etc. This topic describes the expressions, constructs, functions, operators, and clauses that dynamic tables support in
incremental and full refresh modes.

If a query uses expressions, keywords, operators, or clauses that are not supported for incremental refresh, the automated refresh process
uses a full refresh instead, [which might incur an additional cost](dynamic-tables-cost.md).

For guidance on how different operators affect incremental refresh *performance*, see
[Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md).

## Supported data types

Dynamic tables support all [Snowflake SQL data types](../sql-reference/intro-summary-data-types.md)
for both incremental and full refresh, except:

* Structured data types.
* Geospatial data types (full refresh only).

## Supported queries in incremental and full refresh modes

| Keyword | Incremental Refresh Mode | Full Refresh Mode |
| --- | --- | --- |
| [DISTINCT](../sql-reference/sql/select.md) | Supported | Supported |
| [External functions](../sql-reference/external-functions-introduction.md) | Not supported | Not supported |
| [FROM](../sql-reference/constructs/from.md) | Source tables, views, Snowflake-managed Apache Iceberg™ tables, and other dynamic tables.  Subqueries outside of FROM clauses (for example, WHERE EXISTS) are not supported. | Supported |
| [GROUP BY](../sql-reference/constructs/group-by.md) | Supported | Supported |
| [CROSS JOIN](../sql-reference/constructs/join.md) | Supported. You can specify any number of tables in the join, and updates to all tables in the join are reflected in the results of the query. | Supported |
| [INNER JOIN](../sql-reference/constructs/join.md) | Supported. You can specify any number of tables in the join, and updates to all tables in the join are reflected in the results of the query. | Supported |
| [LATERAL](../sql-reference/constructs/join-lateral.md) JOIN | Not supported. However, you can use [LATERAL with FLATTEN()](lateral-join-using.md). For example:  ```sqlexample CREATE TABLE persons  AS   SELECT column1 AS id, parse_json(column2) AS entity   FROM values    (12712555,    '{ name:  { first: "John", last: "Smith"},      contact: [      { business:[        { type: "phone", content:"555-1234" },        { type: "email", content:"j.smith@example.com" } ] } ] }'),    (98127771,     '{ name:  { first: "Jane", last: "Doe"},      contact: [      { business:[        { type: "phone", content:"555-1236" },        { type: "email", content:"j.doe@example.com" } ] } ] }');```  ```sqlexample CREATE DYNAMIC TABLE my_dynamic_table  TARGET_LAG = DOWNSTREAM  WAREHOUSE = mywh  AS   SELECT p.id, f.value, f.path   FROM persons p,   LATERAL FLATTEN(input => p.entity) f;```  Note the following behavior for using lateral flatten with incremental refresh:   *Selecting the flatten SEQ column from a lateral flatten join is not supported.* When using the [AUTO](dynamic-tables-refresh.md) parameter, Snowflake typically chooses incremental refresh for queries with lateral flatten joins, unless prevented by other limitations. | Supported. |
| OUTER-EQUI JOIN. | Supported. You can specify any number of tables in the join, and updates to all tables in the join are reflected in the results of the query. | Supported |
| [{LEFT | RIGHT | FULL }] [OUTER JOIN](querying-joins.md) | The following is not supported:   *Outer joins where both sides are the same table.* Outer joins where both sides are a subquery with GROUP BY clauses. * Outer joins with non-equality predicates.   Otherwise, you can specify any number of tables in an outer join, and updates to all tables in the join are reflected in the results of the query. | Supported |
| [ML or LLM functions](snowflake-cortex/aisql.md) | Supported in the SELECT clause. | Supported |
| [PIVOT](../sql-reference/constructs/pivot.md) and [UNPIVOT](../sql-reference/constructs/unpivot.md) | Not supported | Not supported |
| [SAMPLE / TABLESAMPLE](../sql-reference/constructs/sample.md) | Not supported | Not supported |
| Scalar Aggregates | Supported | Supported |
| [SELECT](../sql-reference/sql/select.md) | Expressions including those using deterministic built-in functions and [immutable](../sql-reference/sql/create-function.md) [user-defined functions](../developer-guide/udf/udf-overview.md). | Supported |
| [Set operators](../sql-reference/operators-query.md) (UNION, MINUS, EXCEPT, INTERSECT) | Not supported, except for UNION. In incremental refresh, the UNION set operator works like the combination of the UNION ALL and SELECT DISTINCT operators. | Supported |
| [Sequences](querying-sequences.md). | Not supported | Not supported |
| All [subquery operators](../sql-reference/operators-subquery.md). | Not supported | Supported |
| [UNION ALL](../sql-reference/operators-query.md) | Supported | Supported |
| [User-defined functions](../developer-guide/udf/udf-overview.md) (UDFs) | Supported, except for the following limitations:   *UDFs written in Python, Java, Scala, or Javascript that specify the [VOLATILE](../sql-reference/sql/create-function.md) parameter are not supported.* UDFs written in SQL that contain subqueries are not supported (for example, a SELECT statement). *Replacing an [IMMUTABLE](../sql-reference/sql/create-function.md) UDF while it’s in use by a dynamic table that uses incremental refresh results in failed refreshes.* Importing UDFs from an external stage is not supported. | Supported |
| [User-defined table functions](../developer-guide/udf/udf-overview.md) (UDTFs) | Supported, except for the following limitations:   *UDTFs written in SQL are not supported.* SELECT blocks that read from UDTFs must explicitly specify columns and can’t use `*`. | Supported |
| [WHERE](../sql-reference/constructs/where.md) / [HAVING](../sql-reference/constructs/having.md) / [QUALIFY](../sql-reference/constructs/qualify.md) | Filters with the same expressions that are valid in SELECT are supported.  Filters with the CURRENT_TIMESTAMP, CURRENT_TIME, and CURRENT_DATE functions and their aliases are supported. | Supported.  Filters with the CURRENT_TIMESTAMP, CURRENT_TIME, and CURRENT_DATE functions and their aliases are supported. |
| [Window functions](../sql-reference/functions-window.md) | Supported, except for the following limitations:   *Using the window functions PERCENT_RANK, DENSE_RANK, RANK with sliding window frames is not supported.* Using ANY_VALUE is not supported since it’s a non-deterministic function. | Supported |
| [WITH](../sql-reference/constructs/with.md) | [Common table expressions (CTEs)](queries-cte.md) that use incremental refresh supported features in the subquery are supported.  WITH RECURSIVE is not supported. | Supported |

## Supported non-deterministic functions in incremental and full refresh modes

| Non-deterministic Function | Incremental Refresh Mode | Full Refresh Mode |
| --- | --- | --- |
| [ANY_VALUE](../sql-reference/functions/any_value.md) | Not supported | Not supported |
| [CLASSIFY_TEXT (SNOWFLAKE.CORTEX)](../sql-reference/functions/classify_text-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [COMPLETE (SNOWFLAKE.CORTEX)](../sql-reference/functions/complete-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [CURRENT_ACCOUNT](../sql-reference/functions/current_account.md) | Not supported | Supported |
| [CURRENT_DATE](../sql-reference/functions/current_date.md) (and aliases) | Supported only as a part of a WHERE/HAVING/QUALIFY clause. | Supported only as a part of a WHERE/HAVING/QUALIFY clause. |
| [CURRENT_REGION](../sql-reference/functions/current_region.md) | Not supported | Supported |
| [CURRENT_ROLE](../sql-reference/functions/current_role.md) | Not supported | Supported |
| [CURRENT_TIME](../sql-reference/functions/current_time.md) (and aliases) | Supported only as a part of a WHERE/HAVING/QUALIFY clause. | Supported only as a part of a WHERE/HAVING/QUALIFY clause. |
| [CURRENT_TIMESTAMP](../sql-reference/functions/current_timestamp.md) (and aliases) | Supported only as a part of a WHERE/HAVING/QUALIFY clause. | Supported only as a part of a WHERE/HAVING/QUALIFY clause. |
| Functions that rely on [CURRENT_USER](../sql-reference/functions/current_user.md). | Not supported. Dynamic table refreshes act as their owner role with a special SYSTEM user. | Not supported. Dynamic table refreshes act as their owner role with a special SYSTEM user. |
| [CURRENT_WAREHOUSE](../sql-reference/functions/current_warehouse.md) | Not supported | Supported |
| [DENSE_RANK](../sql-reference/functions/dense_rank.md) | Supported | Supported |
| [EMBED_TEXT_768 (SNOWFLAKE.CORTEX)](../sql-reference/functions/embed_text-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [EMBED_TEXT_1024 (SNOWFLAKE.CORTEX)](../sql-reference/functions/embed_text_1024-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [EXTRACT_ANSWER (SNOWFLAKE.CORTEX)](../sql-reference/functions/extract_answer-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [FINETUNE (SNOWFLAKE.CORTEX)](../sql-reference/functions/finetune-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [FIRST_VALUE](../sql-reference/functions/first_value.md) | Supported | Supported |
| [LAST_VALUE](../sql-reference/functions/last_value.md) | Supported | Supported |
| [NTH_VALUE](../sql-reference/functions/nth_value.md) | Supported | Supported |
| [RANK](../sql-reference/functions/rank.md) | Supported | Supported |
| [ROW_NUMBER](../sql-reference/functions/row_number.md) | Supported | Supported |
| [SENTIMENT (SNOWFLAKE.CORTEX)](../sql-reference/functions/sentiment-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [Sequence functions](../sql-reference/functions/seq1.md) (e.g., `SEQ1`, `SEQ2`) | Not supported | Supported |
| [TRANSLATE (SNOWFLAKE.CORTEX)](../sql-reference/functions/translate-snowflake-cortex.md) | Supported in the SELECT clause | Supported |
| [VOLATILE](../sql-reference/sql/create-function.md) user-defined functions | Not supported | Supported |

## Supported Snowflake Cortex AI functions

You can use [Snowflake Cortex AI Functions (including LLM functions)](snowflake-cortex/aisql.md) in the SELECT clause for dynamic tables in incremental refresh mode. The same
availability restrictions as described in [Cortex AI functions](snowflake-cortex/aisql.md) apply.

Cortex AI Functions let you add AI-powered insights directly to your dynamic tables, automatically analyzing data as it updates. For example, it can
classify customer reviews, support tickets, or survey responses as positive/negative or assign categories.

In the following example, `review_sentiment` uses AI_FILTER to evaluate each review with an LLM. Cortex AI Functions combine
the prompt `The reviewer enjoyed the restaurant` with the actual review text. The output column `enjoyed` is the classification
generated using Cortex AI Functions based on the prompt, indicating whether the reviewer enjoyed the restaurant.

```sqlexample
CREATE OR REPLACE TABLE reviews AS
  SELECT 'Wow... Loved this place.' AS review
  UNION ALL
  SELECT 'The pizza is not good.' AS review;

CREATE OR REPLACE DYNAMIC TABLE review_sentiment
  TARGET_LAG = DOWNSTREAM
  WAREHOUSE = mywh
  REFRESH_MODE = INCREMENTAL
  AS
    SELECT review, AI_FILTER(CONCAT('The reviewer enjoyed the restaurant', review), {'model': 'llama3.1-70b'}) AS enjoyed FROM reviews;
```
