# Source: https://docs.oxla.com/sql-reference/sql-data-types/numeric-type/numeric.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Numeric

## Int Type

The `INT` data type represents whole numbers without decimal points. It is a 32-bit signed integer with a range from -2147483648 to 2147483647.

### Format

```sql  theme={null}
column_name INT
```

### Example

The following is an example of how to create a column using an `INT` type.

```sql  theme={null}
CREATE TABLE cities (
    city_id INT,
    cityname TEXT,
    population INT
);
INSERT INTO cities (city_id, cityname, population)
VALUES 
(8557411, 'New York', 8419000),
(8557421, 'London', 8982000),
(8557451, 'Hongkong', 7482000),
(8557491, 'Seoul', 9776000);
```

Now, run the following query to display the table.

```sql  theme={null}
SELECT * FROM cities;
```

It will result in a table show below.

```sql  theme={null}
 city_id | cityname | population 
---------+----------+------------
 8557411 | New York |    8419000
 8557421 | London   |    8982000
 8557451 | Hongkong |    7482000
 8557491 | Seoul    |    9776000
(4 rows)
```

## Bigint Type

The `BIGINT` data type stores large whole numbers that exceed the `INT` range. It is a 64-bit signed integer with a range from -9223372036854775808 to 9223372036854775807.

### Format

```sql  theme={null}
column_name BIGINT
```

### Example

The following is an example of how to create a column using the `BIGINT` type:

```sql  theme={null}
CREATE TABLE galaxies (
    galaxy_name TEXT,
    star BIGINT
);
INSERT INTO galaxies (galaxy_name, star)
VALUES 
('Milky Way', 100000000000),
('Cigar', 30000000000),
('Andromeda', 1000000000000),
('Cosmos', 2000000000000000000);
```

Now, run the following query to display the table:

```sql  theme={null}
SELECT * FROM galaxies;
```

You will get the following output:

```sql  theme={null}
 galaxy_name |        star         
-------------+---------------------
 Milky Way   |        100000000000
 Cigar       |         30000000000
 Andromeda   |       1000000000000
 Cosmos      | 2000000000000000000
(4 rows)
```

## Real Type

The `REAL` data type is a 32-bit floating-point number compliant with the IEEE 754 binary32 format.

### Format

```sql  theme={null}
column_name REAL
```

### Example

**1. Create a Table**

Here, we are creating a table with a `REAL` column type.

```sql  theme={null}
CREATE TABLE numbers (
    column_1 REAL
);

INSERT into numbers (column_1)
VALUES (1.234568);
```

Display the table with the following query.

```sql  theme={null}
SELECT * FROM numbers;
```

The stored value is shown below.

```sql  theme={null}
 column_1 
----------
 1.234568
(1 row)
```

**2. Rounding**

Rounding might happen if the precision of an input number is too high.

```sql  theme={null}
CREATE TABLE numbers1 (
column_1 REAL
);

INSERT into numbers1 (column_1)
VALUES (1.2345689);
```

Display the table with the following query.

```sql  theme={null}
SELECT * FROM numbers1;
```

The table below shows the value after rounding.

```sql  theme={null}
 column_1 
----------
 1.234569
(1 row)
```

**3. Create a Table With Numbers Exceeding the Range**

The `REAL` type only stores 32-bit floating-point numbers. In this example, we input the numbers that exceed the range.

```sql  theme={null}
CREATE TABLE numbers2 (
    column_1 REAL
);

INSERT into numbers2 (column_1)
VALUES (1.2345682991822);
```

Display the table with the following query.

```sql  theme={null}
SELECT * FROM numbers2;
```

The final output will only return numbers that match the range.

```sql  theme={null}
 column_1  
-----------
 1.2345684
(1 row)
```

## Double Precision Type

The `DOUBLE PRECISION` data type is a 64-bit floating-point number compliant with the IEEE 754 binary64 format.

### Format

```sql  theme={null}
column_name DOUBLE PRECISION
```

### Example

**1. Create a Table**

Here, we are creating a table with a `DOUBLE PRECISION` type column.

```sql  theme={null}
CREATE TABLE numbersdouble (
    column_1 DOUBLE PRECISION
);

INSERT into numbersdouble (column_1)
VALUES (1.234568817283122);
```

Display the table with the following query.

```sql  theme={null}
SELECT * FROM numbersdouble;
```

The output is shown below.

```sql  theme={null}
     column_1      
-------------------
 1.234568817283122
(1 row)
```

**2. Rounding**

Rounding might happen if the precision of an input number is too high.

```sql  theme={null}
CREATE TABLE numbersdouble1 (
    column_1 DOUBLE PRECISION
);

INSERT into numbersdouble1 (column_1)
VALUES (1.234568817283122773);
```

Display the table with the following query.

```sql  theme={null}
SELECT * FROM numbersdouble1;
```

The table below shows the value after rounding.

```sql  theme={null}
      column_1      
--------------------
 1.2345688172831228
(1 row)
```

## Scientific Notation Support

Oxla now supports scientific notation for floating-point types. This feature allows you to use expressions like 1.1e+3, 1e-20, 1.1e02 and similar in your queries.

**Example**

```sql  theme={null}
SELECT 1.1e+3, 1e-20, 1.1e02;
```

***Output***

```sql  theme={null}
 ?column? | ?column? | ?column?
----------+----------+----------
     1100 |    1e-20 |      110
(1 row)
```
