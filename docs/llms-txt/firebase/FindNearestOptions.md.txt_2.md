# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions.md.txt

# FindNearestOptions

# FindNearestOptions


```
@Beta
class FindNearestOptions : AbstractOptions
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.FindNearestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions) |

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#FindNearestOptions()()` Creates a new, empty `FindNearestOptions` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#withDistanceField(com.google.firebase.firestore.pipeline.Field)(distanceField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Add a field containing the distance to the result. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#withDistanceField(kotlin.String)(distanceField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Add a field containing the distance to the result. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#withLimit(kotlin.Long)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specifies the upper bound of documents to return. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(newOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subSection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions)` Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | |

## Public constructors

### FindNearestOptions

```
FindNearestOptions()
```

Creates a new, empty `FindNearestOptions` object.

## Public functions

### withDistanceField

```
fun withDistanceField(distanceField: Field): FindNearestOptions
```

Add a field containing the distance to the result.

| Parameters |
|---|---|
| `distanceField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` that will be added to the result. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | A new `FindNearestOptions` with the specified distance field. |

### withDistanceField

```
fun withDistanceField(distanceField: String?): FindNearestOptions?
```

Add a field containing the distance to the result.

| Parameters |
|---|---|
| `distanceField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The name of the field that will be added to the result. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions?` | A new `FindNearestOptions` with the specified distance field. |

### withLimit

```
fun withLimit(limit: Long): FindNearestOptions
```

Specifies the upper bound of documents to return.

| Parameters |
|---|---|
| `limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | must be a positive integer. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | A new `FindNearestOptions` with the specified limit. |