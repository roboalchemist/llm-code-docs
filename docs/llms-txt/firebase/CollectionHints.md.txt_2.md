# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints.md.txt

# CollectionHints

# CollectionHints


```
@Beta
class CollectionHints : AbstractOptions
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.CollectionHints](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints) |

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints#CollectionHints()()` Creates a new, empty `CollectionHints` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints#withForceIndex(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Forces the query to use a specific index. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints#withIgnoreIndexFields(kotlin.Array)(vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specifies fields to ignore in the index. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(newOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subSection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions)` Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | |

## Public constructors

### CollectionHints

```
CollectionHints()
```

Creates a new, empty `CollectionHints` object.

## Public functions

### withForceIndex

```
fun withForceIndex(value: String): CollectionHints
```

Forces the query to use a specific index.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the index to force. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | A new `CollectionHints` with the specified forced index. |

### withIgnoreIndexFields

```
fun withIgnoreIndexFields(vararg values: String): CollectionHints
```

Specifies fields to ignore in the index.

| Parameters |
|---|---|
| `vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The names of the fields to ignore in the index. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` | A new `CollectionHints` with the specified ignored index fields. |