# Source: https://docs.snowflake.com/en/developer-guide/udf/javascript/udf-javascript-scalar-functions.md

# Scalar JavaScript UDFs

This topic covers Scalar JavaScript UDFs (user-defined function).

## Introduction

A scalar JavaScript UDF returns one output row for each input row. The output row must contain only one column/value.

A basic example is in [Introduction to JavaScript UDFs](udf-javascript-introduction.md). Additional examples are below.

> **Note:**
>
> Scalar functions (UDFs) have a limit of 500 input arguments.

## Examples

This section contains examples of scalar JavaScript UDFs.

### Recursion

The following example shows that a JavaScript UDF can call itself (i.e. it can use recursion).

Create a recursive UDF:

```javascript
CREATE OR REPLACE FUNCTION RECURSION_TEST (STR VARCHAR)
  RETURNS VARCHAR
  LANGUAGE JAVASCRIPT
  AS $$
  return (STR.length <= 1 ? STR : STR.substring(0,1) + '_' + RECURSION_TEST(STR.substring(1)));
  $$
  ;
```

Call the recursive UDF:

```javascript
SELECT RECURSION_TEST('ABC');
+-----------------------+
| RECURSION_TEST('ABC') |
|-----------------------|
| A_B_C                 |
+-----------------------+
```

### Custom exception

The following example shows a JavaScript UDF that throws a custom exception.

Create the function:

```javascript
CREATE FUNCTION validate_ID(ID FLOAT)
RETURNS VARCHAR
LANGUAGE JAVASCRIPT
AS $$
    try {
        if (ID < 0) {
            throw "ID cannot be negative!";
        } else {
            return "ID validated.";
        }
    } catch (err) {
        return "Error: " + err;
    }
$$;
```

Create a table with valid and invalid values:

```javascript
CREATE TABLE employees (ID INTEGER);
INSERT INTO employees (ID) VALUES
    (1),
    (-1);
```

Call the function:

```javascript
SELECT ID, validate_ID(ID) FROM employees ORDER BY ID;
+----+-------------------------------+
| ID | VALIDATE_ID(ID)               |
|----+-------------------------------|
| -1 | Error: ID cannot be negative! |
|  1 | ID validated.                 |
+----+-------------------------------+
```

## Troubleshooting

See [Troubleshooting JavaScript UDFs](udf-javascript-troubleshooting.md).
