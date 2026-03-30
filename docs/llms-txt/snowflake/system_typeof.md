# Source: https://docs.snowflake.com/en/sql-reference/functions/system_typeof.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$TYPEOF

Returns a string representing the SQL data type associated with an
expression.

See also:
:   [TYPEOF](typeof.md)

## Syntax

```sqlsyntax
SYSTEM$TYPEOF( <expr> )
```

## Arguments

`expr`
:   The argument can be a column name or a general expression.

## Returns

Returns a VARCHAR value that contains the data type of the input expression, for example, BOOLEAN, NUMBER, ARRAY, OBJECT, etc.

## Usage notes

* If TYPEOF is executed without the SYSTEM$ prefix (i.e. as a regular
  function rather than a system function), it returns different
  results (see [TYPEOF](typeof.md)).

## Examples

```sqlexample
SELECT SYSTEM$TYPEOF(NULL);
```

```output
+---------------------+
| SYSTEM$TYPEOF(NULL) |
|---------------------|
| NULL[LOB]           |
+---------------------+
```

```sqlexample
SELECT SYSTEM$TYPEOF(1);
```

```output
+------------------+
| SYSTEM$TYPEOF(1) |
|------------------|
| NUMBER(1,0)[SB1] |
+------------------+
```

```sqlexample
SELECT SYSTEM$TYPEOF(1e10);
```

```output
+---------------------+
| SYSTEM$TYPEOF(1E10) |
|---------------------|
| NUMBER(11,0)[SB8]   |
+---------------------+
```

```sqlexample
SELECT SYSTEM$TYPEOF(10000);
```

```output
+----------------------+
| SYSTEM$TYPEOF(10000) |
|----------------------|
| NUMBER(5,0)[SB2]     |
+----------------------+
```

```sqlexample
SELECT SYSTEM$TYPEOF('something');
```

```output
+----------------------------+
| SYSTEM$TYPEOF('SOMETHING') |
|----------------------------|
| VARCHAR(9)[LOB]            |
+----------------------------+
```

```sqlexample
SELECT SYSTEM$TYPEOF(CONCAT('every', 'body'));
```

```output
+----------------------------------------+
| SYSTEM$TYPEOF(CONCAT('EVERY', 'BODY')) |
|----------------------------------------|
| VARCHAR(9)[LOB]                        |
+----------------------------------------+
```
