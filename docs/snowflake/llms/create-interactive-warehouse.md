# Source: https://docs.snowflake.com/en/sql-reference/sql/create-interactive-warehouse.md

# CREATE INTERACTIVE WAREHOUSE

Creates a new interactive [virtual warehouse](../../user-guide/warehouses-overview.md) optimized for low-latency, high-concurrency workloads with interactive tables.

Interactive warehouses are designed to deliver optimal query performance when working with interactive tables, which provide
fast query responses for frequently accessed data through intelligent caching and optimization.

See also:
:   [CREATE WAREHOUSE](create-warehouse.md), [ALTER WAREHOUSE](alter-warehouse.md), [DESCRIBE WAREHOUSE](desc-warehouse.md), [DROP WAREHOUSE](drop-warehouse.md), [SHOW WAREHOUSES](show-warehouses.md), [CREATE INTERACTIVE TABLE](create-interactive-table.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] INTERACTIVE WAREHOUSE [ IF NOT EXISTS ] <name>
       [ TABLES ( <table_name> [ , <table_name> ... ] ) ]
       [ [ WITH ] objectProperties ]
       [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
       [ objectParams ]
```

Where:

> ```sqlsyntax
> objectProperties ::=
>   WAREHOUSE_SIZE = { XSMALL | SMALL | MEDIUM | LARGE | XLARGE | XXLARGE | XXXLARGE | X4LARGE | X5LARGE | X6LARGE }
>   MAX_CLUSTER_COUNT = <num>
>   MIN_CLUSTER_COUNT = <num>
>   AUTO_SUSPEND = { <num> | NULL }
>   AUTO_RESUME = { TRUE | FALSE }
>   INITIALLY_SUSPENDED = { TRUE | FALSE }
>   RESOURCE_MONITOR = <monitor_name>
>   COMMENT = '<string_literal>'
> ```
>
> ```sqlsyntax
> objectParams ::=
>   MAX_CONCURRENCY_LEVEL = <num>
>   STATEMENT_QUEUED_TIMEOUT_IN_SECONDS = <num>
>   STATEMENT_TIMEOUT_IN_SECONDS = <num>
> ```

## Parameters

`name`
:   Specifies the identifier for the interactive warehouse. The identifier must be unique within your account.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TABLES ( ... )`
:   Optionally specifies a comma-separated list of interactive table names to immediately associate with the interactive warehouse.
    Using this clause starts the cache-warming process for the specified tables when the warehouse is created.

    `table_name`
    :   Specifies the identifier for an interactive table to associate with the warehouse. You can specify multiple table names separated by commas.

        > **Note:**
        >
        > * All specified tables must be interactive tables created with the `INTERACTIVE` keyword.
        > * If this clause is omitted, you can associate interactive tables later using [ALTER WAREHOUSE](alter-warehouse.md) with the `ADD TABLES` clause.
        > * Cache warming may take significant time depending on the size of the data.

`WAREHOUSE_SIZE = string_constant`
:   Specifies the size of the interactive warehouse. Interactive warehouses support specific sizes optimized for interactive workloads.

    Valid values:
    :   * `XSMALL` , `'X-SMALL'`
        * `SMALL`
        * `MEDIUM`
        * `LARGE`
        * `XLARGE` , `'X-LARGE'`
        * `XXLARGE` , `X2LARGE` , `'2X-LARGE'`
        * `XXXLARGE` , `X3LARGE` , `'3X-LARGE'`

    Default:
    :   `XSMALL`

    > **Note:**
    >
    > * To use a value that contains a hyphen (for example, `'2X-LARGE'`), you must enclose the value in single quotes, as shown.
    > * Choose a warehouse size to match your workload requirements. You can adjust the
    >   `MIN_CLUSTER_COUNT` and `MAX_CLUSTER_COUNT` properties to optimize for concurrency.

`MAX_CLUSTER_COUNT = num`
:   Specifies the maximum number of clusters for a multi-cluster interactive warehouse.

    Valid values:
    :   `1` to `10` (depending on warehouse size)

    Default:
    :   `1` (single-cluster warehouse)

`MIN_CLUSTER_COUNT = num`
:   Specifies the minimum number of clusters for a multi-cluster interactive warehouse.

    Valid values:
    :   `1` to the value of MAX_CLUSTER_COUNT

    Default:
    :   `1`

`AUTO_SUSPEND = { num | NULL }`
:   Specifies the number of seconds of inactivity after which the interactive warehouse is automatically suspended.

    The minimum value for interactive warehouses is `86400` (24 hours). If you specify a value less
    than 86400, Snowflake uses 86400. Setting the value to `NULL` disables auto-suspend.

    Default:
    :   `NULL` (auto-suspend is disabled)

`AUTO_RESUME = { TRUE | FALSE }`
:   Specifies whether to automatically resume the interactive warehouse when a SQL statement is
    submitted to it.

    Default:
    :   `FALSE`

`INITIALLY_SUSPENDED = { TRUE | FALSE }`
:   Specifies whether the interactive warehouse is created in a suspended state.

    Default:
    :   `TRUE` (interactive warehouses are created suspended)

`RESOURCE_MONITOR = monitor_name`
:   Specifies the identifier of a resource monitor to assign to the interactive warehouse for credit usage control.

    Valid values:
    :   Any existing resource monitor

    Default:
    :   No value (no resource monitor assigned)

`COMMENT = 'string_literal'`
:   Specifies a comment for the interactive warehouse.

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`MAX_CONCURRENCY_LEVEL = num`
:   Specifies the concurrency level for SQL statements executed by the interactive warehouse cluster.

`STATEMENT_QUEUED_TIMEOUT_IN_SECONDS = num`
:   Specifies the time, in seconds, a SQL statement can be queued before being canceled.

`STATEMENT_TIMEOUT_IN_SECONDS = num`
:   Specifies the time, in seconds, after which a running SQL statement is canceled.
    Interactive warehouses have a maximum timeout interval of five seconds.
    Any larger values are ignored.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE WAREHOUSE | Account | Required to create any warehouse, including interactive warehouses. |
| USAGE | Interactive Table | Required on each interactive table specified in the `TABLES` clause, if used. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Interactive warehouses are created in a `SUSPENDED` state by default. Use [ALTER WAREHOUSE](alter-warehouse.md)
  with the RESUME clause to start the warehouse.
* When you specify the TABLES clause, cache warming begins immediately for the specified
  interactive tables. This process may take significant time depending on data size.
* Interactive warehouses can only query interactive tables. To query standard tables, use a standard
  warehouse created with [CREATE WAREHOUSE](create-warehouse.md).
* Interactive warehouses support auto-suspend and auto-resume. The minimum AUTO_SUSPEND value
  is 86400 seconds (24 hours). For more information, see [Resuming and suspending an interactive warehouse](../../user-guide/interactive.md).
* Interactive warehouses support multi-cluster configuration for handling high-concurrency workloads.
* If you don’t specify the `TABLES` clause during creation, you can associate interactive tables
  later using [ALTER WAREHOUSE](alter-warehouse.md) with the ADD TABLES clause.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Billing and pricing

For information about billing and pricing considerations for interactive warehouses, see
[Cost and billing considerations](../../user-guide/interactive.md).

## Examples

Create an interactive warehouse associated with specific interactive tables:

```sqlexample
CREATE OR REPLACE INTERACTIVE WAREHOUSE sales_interactive_wh
  TABLES (orders, customers, products)
  WAREHOUSE_SIZE = 'MEDIUM'
  COMMENT = 'Interactive warehouse for sales team analytics';
```

Create an interactive warehouse without associated tables (to be added later):

```sqlexample
CREATE INTERACTIVE WAREHOUSE analytics_interactive_wh
  WAREHOUSE_SIZE = 'LARGE'
  MAX_CLUSTER_COUNT = 3
  MIN_CLUSTER_COUNT = 3;
```

Create an interactive warehouse with resource monitoring:

```sqlexample
CREATE INTERACTIVE WAREHOUSE dev_interactive_wh
  WAREHOUSE_SIZE = 'XSMALL'
  RESOURCE_MONITOR = dev_resource_monitor
  COMMENT = 'Development interactive warehouse';
```

Resume an interactive warehouse and associate tables with it:

```sqlexample
-- Resume the warehouse
ALTER WAREHOUSE sales_interactive_wh RESUME;

-- Add additional tables if needed
ALTER WAREHOUSE sales_interactive_wh ADD TABLES (inventory);
```
