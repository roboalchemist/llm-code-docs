# Source: https://docs.oxla.com/sql-reference/sql-statements/describe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# DESCRIBE

## Overview

The `DESCRIBE` statement is used to show columns within a table as well as tables within a database.

<Check>It is recommended to be used before creating a new table to avoid tables duplication</Check>

## Syntax

Below you can find the basic syntax for describing tables within a database as well as columns within tables:

```sql  theme={null}
DESCRIBE DATABASE;
```

```sql  theme={null}
DESCRIBE TABLE table_name;
```

where:

`table_name`: name of the table that you want to show

<Info>This statement is available to all users with the `USAGE` privilege on the schema, where the table is located</Info>

## Examples

To get a better understanding of the `DESCRIBE` statement, take a look at some examples below:

### DESCRIBE Table

In this example, we will figure out the columns of the **part** table. In order to do so, you need to run the query below:

```sql  theme={null}
DESCRIBE TABLE part;
```

As a result, you will get a list of column names, column types, and nullable options from the **part** table:

```sql  theme={null}
+----------------+------------+-------------+-------+----------+ 
| database_name  | table_name |    name     | type  | nullable |
+----------------+------------+-------------+-------+----------+
| public         | part       | p_partkey   | INT   | f        |
| public         | part       | p_name      | TEXT  | f        |
| public         | part       | p_mfgr      | TEXT  | f        |
| public         | part       | p_category  | TEXT  | f        |
| public         | part       | p_brand     | TEXT  | f        |
| public         | part       | p_color     | TEXT  | f        |
| public         | part       | p_type      | TEXT  | f        |
| public         | part       | p_size      | INT   | f        |
| public         | part       | p_container | TEXT  | f        |
+----------------+------------+-------------+-------+----------+
```

<Check>The example above shows that the tables reside in the `public` schema (the default schema in Oxla). You can also display tables from other schemas, by following the doc [here](/sql-reference/schema)</Check>

### DESCRIBE Database

In order to describe the database, you need to execute the following query:

```sql  theme={null}
DESCRIBE DATABASE;
```

The output for the above code consists of all existing tables from the specified database, as presented below:

```sql  theme={null}
+-----------------------------+
| name                        | 
+-----------------------------+
| supplier_scale_1_no_index   | 
| features                    | 
| orders                      | 
| features2                   | 
| featurestable               | 
| featurestable1              | 
| featurestable10             | 
+-----------------------------+
```
