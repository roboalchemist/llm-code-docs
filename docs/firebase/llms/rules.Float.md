# Source: https://firebase.google.com/docs/reference/rules/rules.Float.md.txt

# Interface: Float

# [rules](https://firebase.google.com/docs/reference/rules/rules).Float

interface static

Primitive type representing a 64-bit IEEE floating point number.

Floats can be compared using the `==`, `!=`,
`>`, `<`, `>=` and
`<=` operators.

Floats support the arithmetic operators `+`, `-`,
`/`, `*`, and `%`.

Floats can be negated using the `-` prefix.

String and integer values can be converted to float values using the
`float()` function:  

```text
float("2.2") == 2.2
float(2) == 2.0
```