# Source: https://firebase.google.com/docs/reference/rules/rules.Boolean.md.txt

# Interface: Boolean

# [rules](https://firebase.google.com/docs/reference/rules/rules).Boolean

interface static

Primitive type representing a boolean value, `true` or
`false`.

Boolean values can be compared using the `==` and
`!=` operators.

Boolean values have the following logical operators:

*** ** * ** ***

| Operation | Expression |
|-----------|------------|
| **AND**   | `x && y`   |
| **OR**    | `x || y`   |
| **NOT**   | `!x`       |

Rule evaluation will short-circuit on a boolean expression:  

```scilab
// Short-circuits at 'true' so someFunction() will never run
true || someFunction()

// Short-circuits at 'false' so someFunction() will never run
false && someFunction()

// someFunction() will always run
false || someFunction()
```

Strings can be converted into booleans using the `bool()`
function:  

```text
bool("true") == true
```