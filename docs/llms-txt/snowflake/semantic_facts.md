# Source: https://docs.snowflake.com/en/sql-reference/info-schema/semantic_facts.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/semantic_facts.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# SEMANTIC_FACTS view

This ACCOUNT_USAGE view displays a row for each fact defined in a [semantic view](../../user-guide/views-semantic/overview.md).

See also:
:   [SEMANTIC_FACTS view (Information Schema)](../info-schema/semantic_facts.md)

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| `semantic_fact_id` | NUMBER | ID of the fact in the semantic view. |
| `semantic_fact_name` | VARCHAR | Name of the fact in the semantic view. |
| `semantic_table_id` | NUMBER | ID of the semantic table the fact belongs to. |
| `semantic_table_name` | VARCHAR | Name of the semantic table the fact belongs to. |
| `semantic_view_id` | NUMBER | ID of the semantic view. |
| `semantic_view_name` | VARCHAR | Name of the semantic view. |
| `semantic_view_schema_id` | NUMBER | ID of the schema to which the semantic view belongs. |
| `semantic_view_schema_name` | VARCHAR | Schema to which the semantic view belongs. |
| `semantic_view_database_id` | NUMBER | ID of the database to which the semantic view belongs. |
| `semantic_view_database_name` | VARCHAR | Database to which the semantic view belongs. |
| `data_type` | VARCHAR | Data type of the fact expression. |
| `expression` | VARCHAR | The SQL expression used to calculate the fact. |
| `synonyms` | ARRAY(VARCHAR) | List of the synonyms for the fact. |
| `comment` | VARCHAR | Description of the fact. |
| `created` | TIMESTAMP_LTZ | Creation time of the fact. |
| `last_altered` | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| `deleted` | TIMESTAMP_LTZ | Date and time when the fact was dropped. |

## Usage notes

* Latency for the view can be up to 120 minutes (2 hours).
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Examples

Retrieve the list of all facts for the semantic view `O_TPCH_SEMANTIC_VIEW` in the database `MY_DB`:

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.SEMANTIC_FACTS
  WHERE semantic_view_name = 'O_TPCH_SEMANTIC_VIEW'
    AND semantic_view_database_name = 'MY_DB';
```

```output
+------------------+------------------------+-------------------+---------------------+------------------+----------------------+-------------------------+---------------------------+---------------------------+-----------------------------+--------------+--------------------------+----------+-------------------------------+-------------------------------+---------+---------+
| SEMANTIC_FACT_ID | SEMANTIC_FACT_NAME     | SEMANTIC_TABLE_ID | SEMANTIC_TABLE_NAME | SEMANTIC_VIEW_ID | SEMANTIC_VIEW_NAME   | SEMANTIC_VIEW_SCHEMA_ID | SEMANTIC_VIEW_SCHEMA_NAME | SEMANTIC_VIEW_DATABASE_ID | SEMANTIC_VIEW_DATABASE_NAME | DATA_TYPE    | EXPRESSION               | SYNONYMS | CREATED                       | LAST_ALTERED                  | DELETED | COMMENT |
|------------------+------------------------+-------------------+---------------------+------------------+----------------------+-------------------------+---------------------------+---------------------------+-----------------------------+--------------+--------------------------+----------+-------------------------------+-------------------------------+---------+---------|
|              386 | A_CUSTOMER_ORDER_COUNT |                99 | CUSTOMER            |               49 | O_TPCH_SEMANTIC_VIEW |                      92 | MY_SCHEMA                 |                         7 | MY_DB                       | NUMBER(18,0) | COUNT(orders.d_orderkey) | NULL     | 2025-02-28 16:16:04.388 -0800 | 2025-02-28 16:16:04.388 -0800 | NULL    | NULL    |
|              385 | D_ORDERKEY             |               100 | ORDERS              |               49 | O_TPCH_SEMANTIC_VIEW |                      92 | MY_SCHEMA                 |                         7 | MY_DB                       | NUMBER(38,0) | o_orderkey               | NULL     | 2025-02-28 16:16:04.388 -0800 | 2025-02-28 16:16:04.388 -0800 | NULL    | NULL    |
+------------------+------------------------+-------------------+---------------------+------------------+----------------------+-------------------------+---------------------------+---------------------------+-----------------------------+--------------+--------------------------+----------+-------------------------------+-------------------------------+---------+---------+
```
