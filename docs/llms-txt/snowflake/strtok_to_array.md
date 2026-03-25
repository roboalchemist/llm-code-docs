# Source: https://docs.snowflake.com/en/sql-reference/functions/strtok_to_array.md

Categories:
:   [String & binary functions](../functions-string.md) (General) , [Semi-structured and structured data functions](../functions-semistructured.md) (Conversion/Casting)

# STRTOK_TO_ARRAY

Tokenizes the given string using the given set of delimiters and returns the tokens as an [ARRAY](../data-types-semistructured.md)
value.

## Syntax

```sqlsyntax
STRTOK_TO_ARRAY( <string> [ , <delimiter> ] )
```

## Arguments

**Required:**

`string`
:   Text to be tokenized.

**Optional:**

`delimiter`
:   Set of delimiters.

    Default: A single space character.

## Returns

This function returns a value of type ARRAY or NULL.

The function returns an empty array if tokenization produces no tokens.

If either argument is a NULL or [JSON null](../../user-guide/semistructured-considerations.md) value, the function returns NULL.

## Examples

The following example uses the STRTOK_TO_ARRAY function to split a string into an array:

```sqlexample
SELECT STRTOK_TO_ARRAY('a.b.c', '.') AS string_to_array;
```

```output
+-----------------+
| STRING_TO_ARRAY |
|-----------------|
| [               |
|   "a",          |
|   "b",          |
|   "c"           |
| ]               |
+-----------------+
```

The following example tokenizes on multiple delimiters (`.` and `@`):

```sqlexample
SELECT STRTOK_TO_ARRAY('user@snowflake.com', '.@') AS multiple_delimiters;
```

```output
+---------------------+
| MULTIPLE_DELIMITERS |
|---------------------|
| [                   |
|   "user",           |
|   "snowflake",      |
|   "com"             |
| ]                   |
+---------------------+
```
