# Source: https://docs.snowflake.com/en/sql-reference/functions/trim.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# TRIM

Removes leading and trailing characters from a string.

> **Note:**
>
> To remove characters in a string, you can use the [REPLACE](replace.md) function.

See also:
:   [LTRIM](ltrim.md) , [RTRIM](rtrim.md) , [String & binary data types](../data-types-text.md)

## Syntax

```sqlsyntax
TRIM( <expr> [, <characters> ] )
```

## Arguments

`expr`
:   A string expression to be trimmed.

`characters`
:   One or more characters to remove from the left and right side of `expr`.

    The default value is `' '` (a single blank space character).
    If no characters are specified, only blank spaces are removed.

## Returns

This function returns a value of VARCHAR data type or NULL. If either argument is NULL, returns NULL.

## Usage notes

* You can specify the characters in `characters` in any order.
* A specification of `' '` in `characters` does not remove other whitespace
  characters (such as tabulation characters, end-of-line characters, and so on). Explicitly
  specify these characters to remove them.

* To remove whitespace, the characters must be explicitly included in the
  argument. For example, `' $.'` removes all leading and trailing blank
  spaces, dollar signs, and periods from the input string.

## Collation details

[Collation](../collation.md) is supported when the optional second argument is omitted, or when it
contains only whitespace.

The collation specification of the returned value is the same as the collation specification of the first argument.

## Examples

Remove leading and trailing `*` and `-` characters from a string:

```sqlexample
SELECT '*-*ABC-*-' AS original,
       TRIM('*-*ABC-*-', '*-') AS trimmed;
```

```output
+-----------+---------+
| ORIGINAL  | TRIMMED |
|-----------+---------|
| *-*ABC-*- | ABC     |
+-----------+---------+
```

Remove a trailing new line from a string. This example uses the [CONCAT](concat.md) function to enclose
the strings in `>` and `<` characters to help you visualize the whitespace.

```sqlexample
SELECT CONCAT('>', CONCAT('ABC\n', '<')) AS original,
       CONCAT('>', CONCAT(TRIM('ABC\n', '\n'), '<')) AS trimmed;
```

```output
+----------+---------+
| ORIGINAL | TRIMMED |
|----------+---------|
| >ABC     | >ABC<   |
| <        |         |
+----------+---------+
```

Remove leading and trailing whitespace from a string. This example encloses
the strings in `>` and `<` characters to help you visualize the whitespace.
It also shows that the function returns NULL for NULL input.

```sqlexample
CREATE OR REPLACE TABLE test_trim_function(column1 VARCHAR);

INSERT INTO test_trim_function VALUES ('  Leading Spaces'), ('Trailing Spaces  '), (NULL);

SELECT CONCAT('>', CONCAT(column1, '<')) AS original_values,
       CONCAT('>', CONCAT(TRIM(column1), '<')) AS trimmed_values
  FROM test_trim_function;
```

```output
+---------------------+-------------------+
| ORIGINAL_VALUES     | TRIMMED_VALUES    |
|---------------------+-------------------|
| >  Leading Spaces<  | >Leading Spaces<  |
| >Trailing Spaces  < | >Trailing Spaces< |
| NULL                | NULL              |
+---------------------+-------------------+
```
