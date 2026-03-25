# Source: https://docs.snowflake.com/en/migrations/sma-docs/translation-reference/spark-sql/spark-sql-dml/select/distinct.md

# Snowpark Migration Accelerator: Distinct

## Description

Select all unique rows from the referenced tables. ([Databricks SQL Language Reference SELECT](https://docs.databricks.com/en/sql/language-manual/sql-ref-syntax-qry-select.html))

`DISTINCT` removes duplicate rows from your query results. ([Snowflake SQL Language Reference SELECT](https://docs.snowflake.com/en/sql-reference/sql/select#parameters))

### Syntax

```bnf
SELECT [ DISTINCT ] { named_expression | star_clause } [, ...]
  FROM table_reference
```

```bnf
SELECT [ DISTINCT ]
       {
         [{<object_name>|<alias>}.]<col_name>
         | [{<object_name>|<alias>}.]$<col_position>
         | <expr>
       }
       [ [ AS ] <col_alias> ]
       [ , ... ]
[ ... ]
```

## Sample Source Patterns

### Setup data

#### Databricks

```sql
CREATE TEMPORARY VIEW number1(c) AS VALUES (3), (1), (2), (2), (3), (4);
```

#### Snowflake

```sql
CREATE TEMPORARY TABLE number1(c int);
INSERT INTO number1 VALUES (3), (1), (2), (2), (3), (4);
```

### Pattern code

#### Databricks

```sql
SELECT DISTINCT c FROM number1;
```

| c |
| --- |
| 3 |
| 1 |
| 2 |
| 4 |

#### Snowflake

```sql
SELECT DISTINCT c FROM number1;
```

| c |
| --- |
| 3 |
| 1 |
| 2 |
| 4 |

### Known Issues

No issues were found

### Related EWIs

No related EWIs
