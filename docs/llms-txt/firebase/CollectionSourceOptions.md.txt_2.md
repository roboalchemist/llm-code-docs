# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions.md.txt

# CollectionSourceOptions

# CollectionSourceOptions


```
@Beta
class CollectionSourceOptions : AbstractOptions
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.CollectionSourceOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions) |

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions#CollectionSourceOptions()()` Creates a new, empty `CollectionSourceOptions` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions#withHints(com.google.firebase.firestore.pipeline.CollectionHints)(hints: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints)` Specifies query hints for the collection source. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(newOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subSection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions)` Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | |

## Public constructors

### CollectionSourceOptions

```
CollectionSourceOptions()
```

Creates a new, empty `CollectionSourceOptions` object.

## Public functions

### withHints

```
fun withHints(hints: CollectionHints): CollectionSourceOptions
```

Specifies query hints for the collection source.

| Parameters |
|---|---|
| `hints: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | The hints to apply to the collection source. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | A new `CollectionSourceOptions` with the specified hints. |