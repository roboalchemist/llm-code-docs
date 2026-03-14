# Source: https://docs.snowflake.com/en/sql-reference/sql/create-semantic-view.md

# CREATE SEMANTIC VIEW

Creates a new [semantic view](../../user-guide/views-semantic/overview.md) in the current/specified schema.

The semantic view must comply with [these validation rules](../../user-guide/views-semantic/validation-rules.md).

See also:
:   [ALTER SEMANTIC VIEW](alter-semantic-view.md) , [DESCRIBE SEMANTIC VIEW](desc-semantic-view.md) , [DROP SEMANTIC VIEW](drop-semantic-view.md) , [SHOW SEMANTIC VIEWS](show-semantic-views.md) , [SHOW SEMANTIC DIMENSIONS](show-semantic-dimensions.md) , [SHOW SEMANTIC DIMENSIONS FOR METRIC](show-semantic-dimensions-for-metric.md) , [SHOW SEMANTIC FACTS](show-semantic-facts.md) , [SHOW SEMANTIC METRICS](show-semantic-metrics.md) , [SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML](../stored-procedures/system_create_semantic_view_from_yaml.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SEMANTIC VIEW [ IF NOT EXISTS ] <name>
  TABLES ( logicalTable [ , ... ] )
  [ RELATIONSHIPS ( relationshipDef [ , ... ] ) ]
  [ FACTS ( factExpression [ , ... ] ) ]
  [ DIMENSIONS ( dimensionExpression [ , ... ] ) ]
  [ METRICS ( { metricExpression | windowFunctionMetricExpression } [ , ... ] ) ]
  [ COMMENT = '<comment_about_semantic_view>' ]
  [ AI_SQL_GENERATION '<instructions_for_sql_generation>' ]
  [ AI_QUESTION_CATEGORIZATION '<instructions_for_question_categorization>' ]
  [ COPY GRANTS ]
```

where:

* The parameters for logical tables are:

  ```sqlsyntax
  logicalTable ::=
    [ <table_alias> AS ] <table_name>
    [ PRIMARY KEY ( <primary_key_column_name> [ , ... ] ) ]
    [
      UNIQUE ( <unique_column_name> [ , ... ] )
      [ ... ]
    ]
    [
      CONSTRAINT [ <constraint_name> ]
        DISTINCT RANGE BETWEEN <start_column> AND <end_column> EXCLUSIVE
    ]
    [ WITH SYNONYMS [ = ] ( '<synonym>' [ , ... ] ) ]
    [ COMMENT = '<comment_about_table>' ]
  ```

* The parameters for relationships are:

  ```sqlsyntax
  relationshipDef ::=
    [ <relationship_identifier> AS ]
    <table_alias> ( <column_name> [ , ... ] )
    REFERENCES
    <ref_table_alias> [ (
      [ ASOF ] <ref_column_name> [ , ... ] |
      BETWEEN <start_column> AND <end_column> EXCLUSIVE
    ) ]
  ```

* The parameters for expressions in the definitions of facts are:

  ```sqlsyntax
  factExpression ::=
    [ { PRIVATE | PUBLIC } ] <table_alias>.<fact> AS <sql_expr>
    [ WITH SYNONYMS [ = ] ( '<synonym>' [ , ... ] ) ]
    [ COMMENT = '<comment_about_the_fact>' ]
  ```

* The parameters for expressions in the definitions of dimensions are:

  ```sqlsyntax
  dimensionExpression ::=
    [ PUBLIC ] <table_alias>.<dimension> AS <sql_expr>
    [ WITH SYNONYMS [ = ] ( '<synonym>' [ , ... ] ) ]
    [ COMMENT = '<comment_about_the_dimension>' ]
    [ WITH CORTEX SEARCH SERVICE <search_service_name> [ USING <search_service_column_name> ] ]
  ```

* The parameters for expressions in the definitions of metrics are:

  ```sqlsyntax
  metricExpression ::=
    [ { PRIVATE | PUBLIC } ] <table_alias>.<metric>
      [
        NON ADDITIVE BY (
          <dimension> [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ]
          [ , ... ]
        )
      ]
      AS <sql_expr>
    [ WITH SYNONYMS [ = ] ( '<synonym>' [ , ... ] ) ]
    [ COMMENT = '<comment_about_the_metric>' ]
  ```

* You can define a metric that uses a window function (a *window function metric*) by using the following syntax:

  ```sqlsyntax
  windowFunctionMetricExpression ::=
    [ { PRIVATE | PUBLIC } ] <table_alias>.<metric> AS
      <window_function>( <metric> ) OVER (
        [ PARTITION BY { <exprs_using_dimensions_or_metrics> | EXCLUDING <dimensions> } ]
        [ ORDER BY <exprs_using_dimensions_or_metrics> [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ]
        [ <windowFrameClause> ]
      )
  ```

  For information about this syntax, see Parameters for window function metrics.

> **Note:**
>
> The order of the clauses is important. For example, you must specify the FACTS clause before the DIMENSIONS clause.
>
> You can refer to semantic expressions that are defined in later clauses. For example, even if `fact_2` is defined after
> `fact_1`, you can still use `fact_2` in the definition of `fact_1`.

## Required parameters

`name`
:   Specifies the name of the semantic view; the name must be unique for the schema in which the table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`COMMENT = 'comment_about_semantic_view'`
:   Specifies a comment about the semantic view.

`AI_SQL_GENERATION 'instructions_for_sql_generation'`
:   Specifies [instructions for Cortex Analyst](../../user-guide/snowflake-cortex/cortex-analyst/custom-instructions.md) that explain
    how to generate the SQL statement.

    For more information, see [Providing custom instructions for Cortex Analyst](../../user-guide/views-semantic/sql.md).

`AI_QUESTION_CATEGORIZATION 'instructions_for_question_categorization'`
:   Specifies [instructions for Cortex Analyst](../../user-guide/snowflake-cortex/cortex-analyst/custom-instructions.md) that explain
    how to classify questions.

    For more information, see [Providing custom instructions for Cortex Analyst](../../user-guide/views-semantic/sql.md).

`COPY GRANTS`
:   When you specify OR REPLACE to replace an existing semantic view with a new semantic view, you can set this parameter to copy
    any privileges granted on the existing semantic view to the new semantic view.

    The command copies all privilege grants except OWNERSHIP from the existing semantic view to the new semantic view. The
    role that executes the CREATE SEMANTIC VIEW statement owns the new view.

    The new semantic view does not inherit any future grants defined for the object type in the schema.

    The operation to copy grants occurs atomically with the CREATE SEMANTIC VIEW statement (in other words, within the same
    transaction).

    If you omit COPY GRANTS, the new semantic view does not inherit any explicit access privileges granted on the existing
    semantic view but does inherit any future grants defined for the object type in the schema.

## Parameters for logical tables

These parameters are part of the syntax for logical tables:

`table_alias AS`
:   Specifies an optional alias for the logical table.

    * If you specify an alias, you must use this alias when referring to the logical table in relationships, facts, dimensions,
      and metrics.
    * If you do not specify an alias, you use the unqualified logical table name to refer to the table.

`table_name`
:   Specifies the name of the logical table.

`PRIMARY KEY ( primary_key_column_name [ , ... ] )`
:   Specifies the names of one or more columns in the logical table that serve as the primary key of the table.

`UNIQUE ( unique_column_name [ , ... ] )`
:   Specifies the name of a column containing a unique value or the names of columns that contain unique combinations of values.

    For example, if the column `service_id` contains unique values, specify:

    ```sqlexample
    TABLES(
      ...
      product_table UNIQUE (service_id)
    ```

    If the combination of values in the `product_area_id` and `product_id` columns is unique, specify:

    ```sqlexample
    TABLES(
      ...
      product_table UNIQUE (product_area_id, product_id)
      ...
    ```

    You can identify multiple columns and multiple combinations of columns as unique in a given logical table:

    ```sqlexample
    TABLES(
      ...
      product_table UNIQUE (product_area_id, product_id) UNIQUE (service_id)
      ...
    ```

    > **Note:**
    >
    > If you already identified a column as a primary key column (by using PRIMARY KEY), do not add the UNIQUE clause for that
    > column.

`CONSTRAINT [ constraint_name ]` . `DISTINCT RANGE BETWEEN start_column AND end_column EXCLUSIVE`
:   [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies a constraint for a [range join](../../user-guide/views-semantic/sql.md).

    `constraint_name`
    :   Specifies an optional name for the constraint.

        If you omit this name, the command uses a system-generated name for the constraint.

    `DISTINCT RANGE BETWEEN start_column AND end_column EXCLUSIVE` specifies that in each row, the range
    between `start_column` and `end_column` is a distinct range:

    * The range is a [half-open interval](https://en.wikipedia.org/wiki/Interval_(mathematics)#Definitions_and_terminology),
      where the range is closed on the left side (`start_column`) and open on the right
      (`end_column`).

      In other words, the time on the left is included in the range, but the time on the right is excluded from the range.

      For example, for a row in this table, if the value in `start_column` is `2024-01-15 00:00:00.000` and the value
      in `end_column` is `2024-02-01 00:00:00.000`, the range is:

      `2024-01-15 00:00:00.000 <= timestamp_from_other_table < 2024-02-01 00:00:00.000`

      The timestamp `2024-01-15 00:00:00.000` is included in this range, but the timestamp `2024-02-01 00:00:00.000` is not.
    * `start_column` and `end_column` must be physical columns from the same table or facts or dimensions from
      the same table.

`WITH SYNONYMS [ = ] ( 'synonym' [ , ... ] )`
:   Specifies one or more synonyms for the logical table. Unlike aliases, synonyms are used for informational purposes only. You do
    not use synonyms to refer to the logical table in relationships, dimensions, metrics, and facts.

`COMMENT = 'comment_about_table'`
:   Specifies a comment about the logical table.

## Parameters for relationships

These parameters are part of the syntax for relationships:

`relationship_identifier AS`
:   Specifies an optional identifier for the relationship.

`table_alias ( column_name [ , ... ] )`
:   Specifies one of the logical tables and one or more of its columns that refers to columns in another logical table.

`ref_table_alias [ ( ... ) ]`
:   Specifies the other logical table referred to by the first logical table.

    You can specify one of the following in parentheses, depending on how you want to join the tables:

    `ref_column_name [ , ... ]`
    :   Specifies a column identified with the PRIMARY KEY or UNIQUE constraint in the
        logical table definition.

    `ASOF ref_column_name [ , ... ] )`
    :   For an [ASOF join](../../user-guide/views-semantic/sql.md), specifies a column of one of
        [the supported types](../constructs/asof-join.md).

        > **Note:**
        >
        > You can specify at most one ASOF keyword in the definition of a given relationship. You can specify this keyword before any
        > column in the list.

    `BETWEEN start_column AND end_column EXCLUSIVE`
    :   [Preview Feature](../../release-notes/preview-features.md) — Open

        Available to all accounts.

        For a [range join](../../user-guide/views-semantic/sql.md), specifies the range of possible values in the first table.

        `start_column` . `end_column`
        :   Specifies the columns that define the start and end of the range.

            * You must define a constraint for these columns.
            * You cannot use the same column for both `start_column` and `end_column`.

              If you want to use the same column, use an [ASOF relationship](../../user-guide/views-semantic/sql.md).

            > **Note:**
            >
            > `column_name` must have a data type that can be [coerced](../data-type-conversion.md) to the
            > data types for `start_column` and `end_column`.

## Parameters for facts, dimensions, and metrics

In a semantic view, you must define at least one dimension or metric, which means that you must specify at least the DIMENSIONS
clause or the METRICS clause.

These parameters are part of the syntax for defining a fact,
dimension, or
metric:

`{ PRIVATE | PUBLIC }`
:   Specifies whether a fact or metric is [private](../../user-guide/views-semantic/sql.md) or public. Facts and metrics that are
    marked as private cannot be queried or used in a query condition.

    > **Note:**
    >
    > You cannot mark a dimension as private. Dimensions are always public. For a dimension, the effect is the same whether you
    > specify or omit PUBLIC.

    If you omit PRIVATE and PUBLIC, the dimension, fact, or metric is public by default.

`table_alias.semantic_expression_name`
:   Specifies a name for a dimension, fact, or metric.

    To define a [derived metric](../../user-guide/views-semantic/sql.md) (a metric that combines multiple metrics from
    different logical tables), omit `table_alias.` from the name.

    See [How Snowflake validates semantic views](../../user-guide/views-semantic/validation-rules.md) for the rules for defining a valid semantic view.

`NON ADDITIVE BY ( dimension [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ] [ , ... ] )`
:   Specifies a list of dimensions that should not be used when summing the metric.

    Instead, during query processing, the rows are sorted by the non-additive dimensions, and the values from the last rows (the
    *latest snapshots of values*) are aggregated to compute the metric.

    `{ ASC | DESC }`
    :   Optionally sorts the values of the non-additive dimensions in ascending (lowest to highest) or descending (highest to lowest)
        order, which determines what the last snapshot is.

        Default: ASC

    `NULLS { FIRST | LAST }`
    :   Optionally specifies whether NULL values are sorted before/after non-NULL values, based on the sort order (ASC or DESC). The
        sort order determines what the last snapshot is.

        Default: Depends on the sort order (ASC or DESC); see
        [the usage notes in the ORDER BY documentation](../constructs/order-by.md).

    Specifying the NON ADDITIVE BY clause makes the metric a *semi-additive* metric.

    For information, see [Identifying the dimensions that should be non-additive for a metric](../../user-guide/views-semantic/sql.md).

`AS sql_expr`
:   Specifies the SQL expression for computing the dimension, fact, or metric.

    See [Defining facts, dimensions, and metrics](../../user-guide/views-semantic/sql.md). For the validation rules for these expressions, see
    [How Snowflake validates semantic views](../../user-guide/views-semantic/validation-rules.md).

`WITH SYNONYMS [ = ] ( 'synonym' [ , ... ] )`
:   Specifies one or more optional synonyms for the dimension, fact, or metric. Note that synonyms are used for informational
    purposes only. You cannot use a synonym to refer to a dimension, fact, or metric in another dimension, fact, or metric.

`COMMENT = 'comment_about_dim_fact_or_metric'`
:   Specifies an optional comment about the dimension, fact, or metric.

`WITH CORTEX SEARCH SERVICE search_service_name [ USING search_service_column_name ]`
:   Specifies the
    [Cortex Search Service to use for this dimension](../../user-guide/views-semantic/sql.md).

    You can only specify this parameter for dimensions (and not for facts or metrics).

    If the Cortex Search Service is in a different database or schema,
    [qualify the name of the service](../name-resolution.md) (for example, `my_db.my_schema.my_service`).

    You can set the optional USING clause to the name of the column in the Cortex Search Service.

## Parameters for window function metrics

These parameters are part of the
syntax for defining window function metrics:

`metric`
:   Specifies a metric expression for this window function. You can specify a metric or any valid metric expression that you can use
    to define a metric in this entity.

`PARTITION BY ...`
:   Groups rows into partitions. You can either partition by a specified set of expressions or by all dimensions (except selected
    dimensions) specified in the query:

    `PARTITION BY exprs_using_dimensions_or_metrics`
    :   Groups rows into partitions by SQL expressions. In the SQL expression:

        * Any dimensions in the expression must be accessible from the same entity that defines the window function metric.
        * Any metrics must belong to the same table where this metric is being defined.
        * You cannot specify aggregates, window functions, or subqueries.

    `PARTITION BY EXCLUDING dimensions`
    :   Groups rows into partitions by all of the dimensions specified in the [SEMANTIC_VIEW](../constructs/semantic_view.md) clause of
        the query, except for the dimensions specified by `dimensions`.

        `dimensions` must only refer to dimensions that are accessible from the entity that defines the window function
        metric.

        For example, suppose that you exclude the dimension `table_1.dimension_1` from partitioning:

        ```sqlexample
        CREATE SEMANTIC VIEW sv
          ...
          METRICS (
            table_1.metric_2 AS SUM(table_1.metric_1) OVER
              (PARTITION BY EXCLUDING table_l.dimension_1 ORDER BY table_1.dimension_2)
          )
          ...
        ```

        Suppose that you run a query that specifies the dimension `table_1.dimension_1`:

        ```sqlexample
        SELECT * FROM SEMANTIC VIEW(
          sv
          METRICS (
            table_1.metric_2
          )
          DIMENSIONS (
            table_1.dimension_1,
            table_1.dimension_2,
            table_1.dimension_3
          );
        ```

        In the query, the metric `table_1.metric_2` is evaluated as:

        ```sqlexample
        SUM(table_1.metric_1) OVER (
          PARTITION BY table_1.dimension_2, table_1.dimension_3
          ORDER BY table_1.dimension_2
        )
        ```

        Note how `table_1.dimension_1` is excluded from the PARTITION BY clause.

        > **Note:**
        >
        > You cannot use EXCLUDING outside of metric definitions in semantic views. EXCLUDING is not supported in window function
        > calls in any other context.

`ORDER BY exprs_using_dimensions_or_metrics  [ ASC | DESC ] [ NULLS FIRST | LAST ] [, ... ]`
:   Orders rows within each partition. In the SQL expression:

    * Any dimensions in the expression must be accessible from the same entity that defines the window function metric.
    * Any metrics must belong to the same table where this metric is being defined.
    * You cannot specify aggregates, window functions, or subqueries.

`windowFrameClause`
:   See [Window function syntax and usage](../functions-window-syntax.md).

For additional information about the parameters for window functions and examples, see
[Defining and querying window function metrics](../../user-guide/views-semantic/querying.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SEMANTIC VIEW | Schema | Required to create a new semantic view. |
| SELECT | Table, view | Required on any tables and/or views used in the semantic view definition. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The semantic view must be valid and must follow the rules described in
  [How Snowflake validates semantic views](../../user-guide/views-semantic/validation-rules.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

See [Creating a semantic view](../../user-guide/views-semantic/sql.md).
