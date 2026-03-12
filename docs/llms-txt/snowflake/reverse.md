# Source: https://docs.snowflake.com/en/sql-reference/functions/reverse.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# REVERSE

Reverses the order of characters in a string, or of bytes in a binary value.

The returned value is the same length as the input, but with the characters/bytes in reverse order. If `subject` is NULL, the result is also NULL.

## Syntax

```sqlsyntax
REVERSE(<subject>)
```

## Collation details

* No impact.
* The collation of the result is the same as the collation of the input.
* In languages where the alphabet contains digraphs or trigraphs (such as “Dz” and “Dzs” in Hungarian), each character in each digraph and trigraph is treated as an independent character, not as part of a single multi-character letter.

  For example, languages with 2-character and 3-character letters (e.g. “dzs” in Hungarian, “ch” in Czech)
  are reversed based on the individual characters, not the letters. See the Examples section below for an example.

## Examples

This example reverses a string:

> ```sqlexample
> SELECT REVERSE('Hello, world!');
> +--------------------------+
> | REVERSE('HELLO, WORLD!') |
> |--------------------------|
> | !dlrow ,olleH            |
> +--------------------------+
> ```

This example reverses a date:

> ```sqlexample
> SELECT '2019-05-22'::DATE, REVERSE('2019-05-22'::DATE) AS reversed;
> +--------------------+------------+
> | '2019-05-22'::DATE | REVERSED   |
> |--------------------+------------|
> | 2019-05-22         | 22-50-9102 |
> +--------------------+------------+
> ```

The following shows that in languages where a single letter is composed of multiple characters, `REVERSE`
reverses based on characters, not letters:

> ```sqlexample
> CREATE TABLE strings (s1 VARCHAR COLLATE 'en', s2 VARCHAR COLLATE 'hu');
> INSERT INTO strings (s1, s2) VALUES ('dzsa', COLLATE('dzsa', 'hu'));
> ```
>
> ```sqlexample
> SELECT s1, s2, REVERSE(s1), REVERSE(s2)
>     FROM strings;
> +------+------+-------------+-------------+
> | S1   | S2   | REVERSE(S1) | REVERSE(S2) |
> |------+------+-------------+-------------|
> | dzsa | dzsa | aszd        | aszd        |
> +------+------+-------------+-------------+
> ```
