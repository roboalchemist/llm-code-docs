# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.md.txt

# UnnestStage

# UnnestStage


```
@Beta
class UnnestStage : Stage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.UnnestStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage) |

*** ** * ** ***

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)(arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable)` Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)(arrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage#hashCode()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage#withIndexField(kotlin.String)(indexField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds an index field to the output documents. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public companion functions

### withField

```
fun withField(arrayWithAlias: Selectable): UnnestStage
```

Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array is found in parameter `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)`, which can be an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` with an alias specified via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#alias(kotlin.String)`, or a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` that can also have alias specified. For each element of the input array, an augmented document will be produced. The element of input array will be stored in a field with name specified by the alias of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` parameter. If the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` is a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` with no alias, then the original array field will be replaced with the individual element.

| Parameters |
|---|---|
| `arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The input array with field alias to store output element of array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

### withField

```
fun withField(arrayField: String, alias: String): UnnestStage
```

Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array found in the previous stage document field specified by the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter, will for each element of the input array produce an augmented document. The element of the input array will be stored in a field with name specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter on the augmented document.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```

### withIndexField

```
fun withIndexField(indexField: String): UnnestStage
```

Adds an index field to the output documents.

A field with the name specified in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage#withIndexField(kotlin.String)` will be added to each output document. The value of this field is a numeric value that corresponds to the array index of the element from the input array.

| Parameters |
|---|---|
| `indexField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the index field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | A new `UnnestStage` that includes the specified index field. |