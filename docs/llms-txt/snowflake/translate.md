# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/cortex-commands/translate.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/translate.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# TRANSLATE

Replaces characters in a string. Specifically, given a string, a set of characters to replace, and
the characters to substitute for the original characters, TRANSLATE makes the specified substitutions.

> **Attention:**
>
> This function doesn’t translate between languages. See the [TRANSLATE (SNOWFLAKE.CORTEX)](translate-snowflake-cortex.md) function
> for translating text between natural languages.

## Syntax

```sqlsyntax
TRANSLATE( <subject>, <sourceAlphabet>, <targetAlphabet> )
```

## Arguments

`subject`
:   A string expression that is translated. If a character in `subject` isn’t
    in `sourceAlphabet`, the character is added to the result without any translation.

`sourceAlphabet`
:   A string with all characters that are modified by
    this function. Each character is either translated to the corresponding
    character in the `targetAlphabet` or omitted in the result. A character is
    omitted in the result if the `targetAlphabet` has no corresponding character
    (that is, has fewer characters than the `sourceAlphabet`).

`targetAlphabet`
:   A string with all characters that are used to replace characters from the
    `sourceAlphabet`.

    If `targetAlphabet` is longer than `sourceAlphabet`, Snowflake reports the
    following error:

    ```output
    String '(target alphabet)' is too long and would be truncated.
    ```

## Returns

This function returns a value of type VARCHAR.

## Collation details

Arguments with collation specifications currently aren’t supported. Collation specifications are ignored without returning an error.

## Examples

Translate the character `ñ` to `n`:

```sqlexample
SELECT TRANSLATE('peña','ñ','n') AS translation;
```

```output
+-------------+
| TRANSLATION |
|-------------|
| pena        |
+-------------+
```

Translate `X` to `c`, `Y` to `e`, `Z` to `f`, and remove `❄` characters:

```sqlexample
SELECT TRANSLATE('❄a❄bX❄dYZ❄','XYZ❄','cef') AS translation;
```

```output
+-------------+
| TRANSLATION |
|-------------|
| abcdef      |
+-------------+
```
