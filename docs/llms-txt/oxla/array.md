# Source: https://docs.oxla.com/sql-reference/sql-data-types/array.md

# Array

## Overview

In Oxla, an array allows you to represent a collection of elements that have the same data type (any built-in data type can be used).

<Info>Currently, the implementation is limited only to single-dimensional arrays</Info>

## Array Type Declaration

An array type can be declared by appending square brackets to the data type of its elements:

```sql  theme={null}
CREATE TABLE movie_night (
    event_date DATE NOT NULL,
    movies_planned TEXT[5] NOT NULL
);
```

The syntax above allows you to specify the size of the array. However, it does not enforce any limits and the behavior will be the same for arrays of unspecified length. There is also another way to declare an array, by prepending the `ARRAY` keyword after the data type of the elements:

```sql  theme={null}
CREATE TABLE movie_night (
    event_date DATE NOT NULL,
    movies_planned TEXT ARRAY NOT NULL
);
```

## Array Values

You can create array literals by using the `ARRAY` keyword and combining it with the array's values enclosed in square brackets and separated by commas:

```sql  theme={null}
ARRAY[ value1 , value2 , ... ]
```

Such a literal can be used with, e.g. `SELECT` or `INSERT INTO` statements:

```sql  theme={null}
SELECT ARRAY['10:14:25'::time, '22:58:11'::time];
      ?column?
---------------------
 {10:14:25,22:58:11}
(1 row)

INSERT INTO movie_night VALUES
('2024-12-01', ARRAY['Inception', 'Interstellar', 'The Prestige']);
INSERT 0 1

SELECT * FROM movie_night;
 event_date |             movies_planned
------------+-----------------------------------------
 2024-12-01 | {Inception,Interstellar,"The Prestige"}
(1 row)
```

You can also use a string representation of an array as another available option for array's values syntax. It requires the elements' values to be enclosed in curly braces and separated by commas:

```sql  theme={null}
'{ value1 , value2 , ... }'
```

Such an array value representation can be used in e.g. `INSERT INTO` statements with the `VALUES` clause:

```sql  theme={null}
INSERT INTO movie_night VALUES ('2024-12-15', '{The Matrix, John Wick}');
INSERT 0 1

SELECT * FROM movie_night;
event_date | movies_planned
------------+-----------------------------------------
2024-12-01 | {Inception,Interstellar,"The Prestige"}
2024-12-15 | {"The Matrix","John Wick"}
(2 rows)
```

Any element can be enclosed in double quotes and this is required, if the value contains commas or curly braces:

```sql  theme={null}
SELECT '{"{\"key1\": 1, \"key2\": \"value\"}", NULL, true}'::json[];
                   ?column?
-----------------------------------------------
 {"{\"key1\":1,\"key2\":\"value\"}",NULL,true}
(1 row)
```

<Info>In the example above, the double quotes which are a part of the JSON value are required to be escaped with a backslash, so that they are not mistaken with the double quote, which marks the end of the element</Info>

## Accessing Arrays

You can retrieve a single element from an array using the array subscript operator. When it comes to array values indexing, the elements of an n-length array start at index `1` and end at index `n`:

```sql  theme={null}
SELECT movies_planned,
       movies_planned[1] AS first_movie,
       movies_planned[3] AS third_movie
FROM   movie_night;
             movies_planned              | first_movie | third_movie
-----------------------------------------+-------------+--------------
 {Inception,Interstellar,"The Prestige"} | Inception   | The Prestige
 {"The Matrix","John Wick"}              | The Matrix  |
(2 rows)
```

<Info>If the index exceeds the length of an array, the returned value will be `NULL`</Info>

Arrays can also be accessed by using array slices. An array slice is denoted by writing `lower_bound:upper_bound`. The bounds can be omitted, in which case the slice is unbounded from a given side:

```sql  theme={null}
SELECT movies_planned[:]   as "unbounded slice",
       movies_planned[1:2] AS "[1:2] slice",
       movies_planned[2:]  AS "[2:] slice"
FROM   movie_night;
             unbounded slice             |        [1:2] slice         |          [2:] slice
-----------------------------------------+----------------------------+-------------------------------
 {Inception,Interstellar,"The Prestige"} | {Inception,Interstellar}   | {Interstellar,"The Prestige"}
 {"The Matrix","John Wick"}              | {"The Matrix","John Wick"} | {"John Wick"}
(2 rows)
```

## Limitations

### Field Size Limit

In Oxla, the field size limit for variable-size types is 32MB and this limit applies to arrays as well. If a value exceeds the given limit, an error is returned:

```sql  theme={null}
CREATE TABLE tb (array_column bigint[]);
CREATE

COPY tb FROM '/.oxla/long_array_value.csv';
ERROR:  Error in row 1, column array_column value exceeds size of 33554432
```

### Unsupported SQL Clauses

Array columns cannot be used as the key columns in `ORDER BY`, `GROUP BY` or `JOIN` operations. It is also impossible to use the array columns as a part of the index of a table. For all the operations mentioned above, an appropriate error message will be returned:

```sql  theme={null}
SELECT * FROM movie_night ORDER BY movies_planned;
ERROR:  could not identify an ordering operator for type text[]
```

Arrays can still be used in `ORDER BY` or `JOIN` operations, if the array column is not the key:

```sql  theme={null}
SELECT * FROM movie_night ORDER BY event_date ASC;
 event_date |             movies_planned
------------+-----------------------------------------
 2024-12-01 | {Inception,Interstellar,"The Prestige"}
 2024-12-15 | {"The Matrix","John Wick"}
(2 rows)
```

### Unsupported SQL Statements

Specific SQL statements currently do not support arrays. These include:

* `INSERT INTO` with `SELECT`: Arrays cannot be directly imported using an `INSERT INTO` with a `SELECT` statement. Instead, we encourage you to either use the `COPY FROM CSV` command or the `INSERT INTO` statement with the `VALUES` keyword
* `UPDATE` and `DELETE`: Updating or deleting records from a table, which contains array columns is not supported
* `COPY TO`: Exporting data from array columns using the `COPY TO` command is not available
* `CREATE INDEX`: Index on a table cannot be created on an array column.

Any effort to use such operations with arrays will result in an error. For now, these limitations should be considered when designing tables that include array columns.
