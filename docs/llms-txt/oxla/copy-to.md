# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-to/copy-to.md

# COPY TO

## Overview

The `COPY TO` statement is used to export tables, specific columns, or results of select queries into .csv files. It allows you to copy data from a table or query result and save it to a specified file.

## Syntax

The syntax for `COPY TO` is as follows:

```sql  theme={null}
COPY { table_name [ ( column_name [, ...] ) ] | ( query ) } TO 'filename' [( option [, ...] ) ];
```

Parameters in the syntax include:

* `table_name`: Table with the data to export.
* `column_name`: Optional. Specify columns for export.
* `query`: A `SELECT` statement for exporting specific results.
* `filename`: File name for saving the exported data.
* `option`: Optional parameters for customization.

## Example

### Step #1: Create a Table

1. Before creating The table, check for duplicate tables using the following statement:

```sql  theme={null}
DESCRIBE DATABASE
```

2. You will receive a list of existing tables in Oxla:

```sql  theme={null}
 namespace_name |      name      
----------------+----------------
 public         | client
 public         | distance_table
 public         | weight
 public         | product
```

<Warning>Ensure you are not creating duplicate tables.</Warning>

3. Now, let's create a table for exporting data to a CSV file. Here, we'll create a "**salary**" table:

```sql  theme={null}
CREATE TABLE salary (
  empid int,
  empname text,
  empdept text,
  empaddress text,
  empsalary int
);
INSERT INTO salary 
    (empid, empname, empdept, empaddress, empsalary) 
VALUES 
    (2001,'Paul','HR', 'California', null ),
    (2002,'Brandon','Product', 'Norway', 15000),
    (2003,'Bradley','Marketing', 'Texas', null),
    (2004,'Lisa','Marketing', 'Houston', 10000),
    (2005,'Emily','Marketing', 'Texas', 20000),
    (2006,'Bobby','Finance', 'Seattle', 20000),
    (2007,'Parker','Project', 'Texas', 45000);
```

4. The table and data were created successfully.

```sql  theme={null}
COMPLETE
INSERT 0 7
```

### Step #2: Copy the Table into the CSV File

<Warning>**Important Notes:** <br /> - By default, the `COPY TO` command overwrites the CSV file if it already exists. <br /> - Please ensure that the directory where you save the file has the necessary write permissions.</Warning>

**Option 1: Exporting all columns from a table**

Copy all columns in the table to the specified CSV file:

```sql  theme={null}
COPY salary TO '/path/to/exportsalary.csv';
```

You will get the following successful result:

```sql  theme={null}
--
(0 rows)
```

The data from the table will be exported to the CSV file.

**Option 2: Exporting specific columns from a table**

Copy only specific columns by specifying the column names in the query:

```sql  theme={null}
COPY salary (empid, empname, empsalary) TO 'exportsalary.csv';
```

You will get the following successful result:

```sql  theme={null}
--
(0 rows)
```

The data from the specified columns will be exported to the CSV file.

**Option 3: Exporting results of a SELECT statement**

In the example below, copy data only from the **Marketing department** using the `SELECT` statement and `WHERE` clause:

```sql  theme={null}
COPY (SELECT * FROM salary WHERE empdept = 'Marketing') TO 'exportsalary.csv';
```

You will get the following successful result:

```sql  theme={null}
--
(0 rows)
```

Data exported to CSV file is only from the Marketing department.
