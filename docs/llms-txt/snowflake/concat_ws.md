# Source: https://docs.snowflake.com/en/sql-reference/functions/concat_ws.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# CONCAT_WS

Concatenates two or more strings, or concatenates two or more binary values, and uses
the first argument as a delimiter between the following strings.

> **Note:**
>
> Unlike some implementations of the CONCAT_WS function, the Snowflake CONCAT_WS function
> doesn’t skip NULL values.

See also:
:   [CONCAT](concat.md)

## Syntax

```sqlsyntax
CONCAT_WS( <separator> , <expression> [ , <expression> ... ] )
```

## Arguments

`separator`
:   The separator must meet the same requirements as `expression`.

`expression`
:   The input expressions must be all strings, or all binary values.

## Returns

The function returns a VARCHAR or BINARY value that contains the 2nd through Nth arguments,
separated by the first argument.

If any argument is NULL, the function returns NULL.

The data type of the returned value is the same as the data type of the input values.

## Usage notes

* Metadata functions such as [GET_DDL](get_ddl.md) accept only constants as input. Concatenated
  input generates an error.
* CONCAT_WS puts separators between arguments, not after the last argument. If CONCAT_WS is called
  with only one argument after the separator, then no separator is appended.

## Collation details

* The [collation specifications](../collation.md) of all input arguments must be compatible.
* The collation of the result of the function is the highest-[precedence](../collation.md) collation of the inputs.

## Examples

Call the CONCAT_WS function to concatenate three strings with a comma separator:

```sqlexample
SELECT CONCAT_WS(',', 'one', 'two', 'three');
```

```output
+---------------------------------------+
| CONCAT_WS(',', 'ONE', 'TWO', 'THREE') |
|---------------------------------------|
| one,two,three                         |
+---------------------------------------+
```

The following example shows that if any argument is NULL, the function returns NULL:

```sqlexample
SELECT CONCAT_WS(',', 'one', NULL, 'two');
```

```output
+------------------------------------+
| CONCAT_WS(',', 'ONE', NULL, 'TWO') |
|------------------------------------|
| NULL                               |
+------------------------------------+
```

The following example shows that when there is only one string to concatenate, the CONCAT_WS function
doesn’t append a separator:

```sqlexample
SELECT CONCAT_WS(',', 'one');
```

```output
+-----------------------+
| CONCAT_WS(',', 'ONE') |
|-----------------------|
| one                   |
+-----------------------+
```
