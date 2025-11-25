# Source: https://docs.oxla.com/sql-reference/sql-statements/create-table.md

# CREATE TABLE

## Overview

The `CREATE TABLE` statement creates a new table in a database. Each table has columns with specific data types like numbers, strings, or dates.

## Syntax

To create a table, you should name and define the columns with their data types.

```sql  theme={null}
CREATE TABLE [ IF NOT EXISTS ] table_name(
  column_1 datatype,
  column_2 datatype,
  column_3 datatype,
  .....
);
```

From the syntax above:

* `table_name`: Name of the table
* `column_1, column_2, column_n`: Names of the columns
* `datatype`: Data type for each column
* `IF NOT EXISTS` (Optional): Use this to avoid errors if the table already exists

<Info> SQL keywords cannot be used for table and column names unless they are quoted. Keep in mind that unquoted names are case-sensitive. For the full list of keywords, please refer to our [doc](/sql-reference/sql-statements/keywords).</Info>

## Constraints

When creating a table, we can add the **NOT NULL** constraint to ensure that values in a column cannot be NULL and will always contain a value. In other words, if you don't define **NOT NULL**, the column can be empty.

```sql  theme={null}
CREATE TABLE table_name(
column1 datatype NOT NULL,
column2 datatype NOT NULL,
column3 datatype NOT NULL,
.....
);
```

## Table index

You can add indexes to the table. See [here](/sql-reference/sql-statements/create-index) for more details.

<Note>By default, tables are created in the `public` schema, but you can specify a different schema. For more information, click [here](/sql-reference/schema).</Note>

## Examples

### Creating a Table

Create a sample table with the query below:

```sql  theme={null}
CREATE TABLE employees (
    employeeID INT,
    lastName TEXT,
    firstName TEXT NOT NULL,
    address TEXT
);
```

Once the table is created successfully, you will get the following output

```sql  theme={null}
CREATE
```

### Creating a Table with Values

Below is an example of creating a **client** table with values:

```sql  theme={null}
CREATE TABLE products (
  product_id INT,         
  product_name TEXT NOT NULL, 
  product_description TEXT
);
INSERT INTO products (product_id, product_name, product_description) 
VALUES 
    (101, 'Laptop', 'A high-performance laptop for professionals.'),
    (102, 'Smartphone', 'A latest model smartphone with excellent features.'),
    (103, 'Headphones', 'Noise-cancelling headphones for immersive audio experience.');
```

You can run the following command to verify the completed request:

```sql  theme={null}
SELECT * FROM products;
```

As a result, we''ll receive a table show below:

```sql  theme={null}
 product_id | product_name |                     product_description                     
------------+--------------+-------------------------------------------------------------
        101 | Laptop       | A high-performance laptop for professionals.
        102 | Smartphone   | A latest model smartphone with excellent features.
        103 | Headphones   | Noise-cancelling headphones for immersive audio experience.
(3 rows)
```

### Using Quoted names

1. Creating a table using the query below:

```sql  theme={null}
CREATE TABLE preferences (module TEXT);
```

2. This will fail with an error message:

```sql  theme={null}
ERROR:  syntax error, unexpected MODULE
ERROR:  syntax error at or near "module"
LINE 1: CREATE TABLE preferences (module TEXT);
                                 ^
```

3. It happens because "module" is a keyword. To use a keyword as a column name, you need to enclose it in double quotes.

```sql  theme={null}
CREATE TABLE preferences ("module" TEXT);
```

4. When querying the table, remember to use quotes around the column name:

```sql  theme={null}
SELECT "module" FROM preferences;
```

Note that names enclosed in quotes are case-sensitive. Therefore, this query will fail:

```sql  theme={null}
SELECT "Module" FROM preferences;
```

### Creating a Table with IF NOT EXISTS

To prevent errors when a table already exists, use the `IF NOT EXISTS` clause. See the following examples:

#### Example without IF NOT EXISTS

1. First, create the table without using the `IF NOT EXISTS` option:

```sql  theme={null}
CREATE TABLE products (
  productID INT,
  productName TEXT,
  category TEXT NOT NULL,
  price REAL
);
```

Output:

```sql  theme={null}
CREATE
```

2. Then, create the same table:

```sql  theme={null}
CREATE TABLE products (
  productID INT,
  productName TEXT,
  category TEXT NOT NULL,
  price REAL
);
```

Because you attempt to create the table without using `IF NOT EXISTS`, you will get the following error:

```sql  theme={null}
ERROR:  relation "products" already exists
```

#### Example with IF NOT EXISTS

Now, create the table using the `IF NOT EXISTS` option to avoid the error:

```sql  theme={null}
CREATE TABLE IF NOT EXISTS products (
  productID int,
  productName text,
  category text NOT NULL,
  price real
);
```

Using `IF NOT EXISTS` allows the query to succeed even if the table already exists.

```sql  theme={null}
CREATE
```
