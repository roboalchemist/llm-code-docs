# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-to/copy-to-with-delimiter.md

# COPY TO with Delimiter

## Overview

A delimiter is a character that separates text strings. Common delimiters include:

* Commas (,)
* Semicolon (;)
* Quotes ( ", ' )
* Dash (-)
* Pipes (|)
* Slashes ( / \ ).

## Syntax

The syntax for `COPY TO` with a delimiter is as follows:

```sql  theme={null}
COPY table_name TO 'file_path' (DELIMITER 'delimiter');
```

Parameters in the syntax include:

* `table_name`: The table containing the data to be exported.
* `file_path`: The CSV file location where the data will be saved.
* `DELIMITER ‘delimiter'`: The Delimiter used in the exported CSV file.

<Info>**Default delimiter is a comma (**`,`**).**</Info>

## Example

### Step #1: Create a Table

1. Before creating a table, check for duplicate tables using the following statement:

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
 public         | salary
```

<Warning>Ensure you are not creating duplicate tables.</Warning>

3. Create a "**customer**" table.

```sql  theme={null}
CREATE TABLE customer (
  cust_id int,
  cust_name text
);
INSERT INTO customer 
    (cust_id, cust_name) 
VALUES 
    (11001, 'Maya'),
    (11003, 'Ricky'),
    (11009, 'Sean'),
    (11008, 'Chris'),
    (11002, 'Emily'),
    (11005, 'Rue'),
    (11007, 'Tom'),
    (11006, 'Casey');
```

4. The table and data were created successfully.

```sql  theme={null}
COMPLETE
INSERT 0 8
```

### Step #2: Export Data to a CSV File using Delimiter

<Warning>**Important Notes:** <br /> - By default, the `COPY TO` command overwrites the CSV file if it already exists. <br /> - Please ensure that the directory where you save the file has a write permissions.</Warning>

In the example below, we are using a Comma ( `,` ).

```sql  theme={null}
COPY salary TO '/home/acer/Documents/customerexport.csv' (DELIMITER ',');
```

You will get the successful output below.

```sql  theme={null}
--
(0 rows)
```

Using the comma ( `,` ) as the delimiter for the `customer` table, the expected output would be:

```sql  theme={null}
cust_id,cust_name
11001,Maya
11003,Ricky
11009,Sean
11008,Chris
11002,Emily
11005,Rue
11007,Tom
11006,Casey
```
