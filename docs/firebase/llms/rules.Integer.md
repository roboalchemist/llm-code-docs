# Source: https://firebase.google.com/docs/reference/rules/rules.Integer.md.txt

# Interface: Integer

# [rules](https://firebase.google.com/docs/reference/rules/rules).Integer

interface static

Primitive type representing a signed 64-bit integer value.

Integers can be compared using the `==`, `!=`,
`>`, `<`, `>=` and
`<=` operators.

Integers support the arithmetic operators `+`, `-`,
`/`, `*`, and `%`.

Integers can be negated using the `-` prefix.

Integer values will be coerced to type [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) when used in
comparison or arithmetic operations with a float value.

String and float values can be converted to integers using the
`int()` function:  

```text
int("2") == 2
int(2.0) == 2
```