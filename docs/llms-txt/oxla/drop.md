# Source: https://docs.oxla.com/sql-reference/sql-statements/drop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# DROP

# Overview

In this section, we will learn how to delete the data from a table using the `DROP` statement.

<Warning>Running a `DROP` statement will also delete all existing records from the table.</Warning>

# Syntax

The basic syntax for the `DROP` statement is as follows:

```sql  theme={null}
DROP TABLE [IF EXISTS] table_name;
```

In this syntax:

* `table_name` defines which table you want to remove.
* `IF EXISTS` is an optional parameter used to ensure no error occurs if the table does not exist.

<Tip>The `DROP` example below is executed in the `public` schema. You can also drop a table from another specific schema.
Click [here](/sql-reference/schema) for more info.</Tip>

# Examples

## Case #1: Dropping the Table

1. Use the following query to create the table.

```sql  theme={null}
CREATE TABLE warehouse (
  id int,
  product text,
  qty int
);
INSERT INTO warehouse 
    (id, product, qty) 
VALUES 
    (889771,'Shirt',22),
    (777821,'Hat',99),
    (103829,'Bed Cover',12);
```

2. We can then use the SELECT statement to view the data in the table:

```sql  theme={null}
 SELECT * FROM warehouse;
```

It will generate the following result:

```sql  theme={null}
+---------+------------+---------+
| id      | product    | qty     | 
+---------+------------+---------+
| 889771  | Shirt      | 22      |
| 777821  | Hat        | 99      |
| 103829  | Bed Cover  | 12      |
+---------+------------+---------+
```

3. To delete the **warehouse** table and all its data, we can use the following query:

```sql  theme={null}
DROP TABLE warehouse;
```

4. If the query is executed successfully, we will get the following output:

```sql  theme={null}
DROP TABLE

Query returned successfully in 284 msec.
```

<Note>If you attempt to use the table for any operation, you will find that the table no longer exists.</Note>

## Case #2: Dropping the Table using IF EXISTS

IF EXISTS can be used to prevent errors when dropping the table if the table does not exist.

### Example without IF EXISTS

1. First, drop the table without using the `IF EXISTS` option.

```sql  theme={null}
DROP TABLE warehouse;
```

Output:

```sql  theme={null}
DROP
```

2. If you attempt to drop the table again without using IF EXISTS, it will result in an error.

```sql  theme={null}
DROP TABLE warehouse;
```

Output:

```sql  theme={null}
ERROR:  relation "warehouse" does not exist
```

### Example with IF EXISTS

Now, drop the table using the IF EXISTS.

```sql  theme={null}
DROP TABLE IF EXISTS warehouse;
```

The drop operation proceeds without errors even if the table doesn't exist.

```sql  theme={null}
DROP
```
