# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions.md.txt

# UnnestOptions

# UnnestOptions


```
@Beta
class UnnestOptions : AbstractOptions
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.UnnestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions) |

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions#UnnestOptions()()` Creates a new, empty `UnnestOptions` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions#withIndexField(kotlin.String)(@https://firebase.google.com/docs/reference/kotlin/javax/annotation/Nonnull indexField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Adds index field to emitted documents |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(newOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subSection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions)` Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | |

## Public constructors

### UnnestOptions

```
UnnestOptions()
```

Creates a new, empty `UnnestOptions` object.

## Public functions

### withIndexField

```
fun withIndexField(@Nonnull indexField: String): UnnestOptions
```

Adds index field to emitted documents

A field with name specified in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions#withIndexField(kotlin.String)` will be added to emitted document. The index is a numeric value that corresponds to array index of the element from input array.

| Parameters |
|---|---|
| `@https://firebase.google.com/docs/reference/kotlin/javax/annotation/Nonnull indexField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name of index field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | A new `UnnestOptions` that includes the specified index field. |