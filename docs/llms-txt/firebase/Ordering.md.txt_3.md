# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.md.txt

# Ordering

# Ordering


```
@Beta
class Ordering
```

<br />

*** ** * ** ***

Represents an ordering criterion for sorting documents in a Firestore pipeline.

You create `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` instances using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)` helper methods.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html` |

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on field. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering#hashCode()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering#dir()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering#expr()` |

## Public companion functions

### ascending

```
fun ascending(expr: Expression): Ordering
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The order is based on the evaluation of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with ascending sort by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`. |

### ascending

```
fun ascending(fieldName: String): Ordering
```

Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on field.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field to sort documents. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with ascending sort by field. |

### descending

```
fun descending(expr: Expression): Ordering
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The order is based on the evaluation of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with descending sort by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`. |

### descending

```
fun descending(fieldName: String): Ordering
```

Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on field.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field to sort documents. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with descending sort by field. |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```

## Public properties

### dir

```
val dir: Ordering.Direction
```

### expr

```
val expr: Expression
```