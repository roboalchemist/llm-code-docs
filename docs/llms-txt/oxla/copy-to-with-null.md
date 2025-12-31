# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-to/copy-to-with-null.md

# COPY TO with NULL

## Overview

A `NULL` value indicates that the value does not exist in the database. In Oxla, you can use the `NULL` option in the `COPY TO` state to specify a string that will replace `NULL` values ​​when copying data from the table to a CSV file.

## Syntax

The syntax for using the `NULL` option in the `COPY TO` is as follows:

```sql  theme={null}
COPY table_name TO 'file_path' (NULL 'replacement_string');
```

Parameters in the syntax include:

* `table_name`: The table containing the data to be exported.
* `file_path`: A CSV file location where the data will be saved.
* `NULL ‘replacement_string'`: The specified string that will replace NULL values in the exported CSV file. The default value is `' '`.

## Example

1. Create a table with a `NULL` value.

```sql  theme={null}
CREATE TABLE example_table (
  id serial,
  name varchar(50),
  age int,
  city varchar(50)
);

INSERT INTO example_table (name, age, city) VALUES
  ('John', 25, 'New York'),
  ('Alice', NULL, 'Chicago'),
  ('Bob', 30, NULL);
```

2. Now, let's use `COPY TO` with an empty string:

```sql  theme={null}
COPY example_table TO '/path/to/exampleexport.csv' (NULL '');
```

3. The `NULL` values in the table are replaced with the empty string in the CSV file.

```
1,John,25,"New York"
2,Alice,null,"Chicago"
3,Bob,30,""
```

<Tip>You can specify another string to replace the null value, such as blank, empty, invalid, etc.</Tip>
