# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions.md.txt

# AbstractOptions

# AbstractOptions


```
abstract class AbstractOptions<T : AbstractOptions<T>>
```

<br />

Known direct subclasses [AggregateHints](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateHints), [AggregateOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateOptions), [CollectionGroupOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupOptions), [CollectionHints](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints), [CollectionSourceOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions), [FindNearestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions), [Pipeline.ExecuteOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions), [RawOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions), [UnnestOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateHints` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionHints` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` |   |

*** ** * ** ***

## Summary

| ### Public functions |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions)` Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option |

| ### Protected functions |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(newOptions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subSection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions<*>)` |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

## Public functions

### with

```
fun with(key: String, value: Boolean): T
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value of option |

| Returns |
|---|---|
| `T` | A new options object. |

### with

```
fun with(key: String, value: Double): T
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` value of option |

| Returns |
|---|---|
| `T` | A new options object. |

### with

```
fun with(key: String, value: Field): T
```

Specify generic `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` option

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` value of option |

| Returns |
|---|---|
| `T` | A new options object. |

### with

```
fun with(key: String, value: Long): T
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value of option |

| Returns |
|---|---|
| `T` | A new options object. |

### with

```
fun with(key: String, value: RawOptions): T
```

Specify `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawOptions` object |

| Returns |
|---|---|
| `T` | A new options object. |

### with

```
fun with(key: String, value: String): T
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The option key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value of option |

| Returns |
|---|---|
| `T` | A new options object. |

## Protected functions

### adding

```
protected fun adding(newOptions: AbstractOptions<*>): T
```

### with

```
protected fun with(key: String, subSection: AbstractOptions<*>): T
```

### with

```
protected fun with(key: String, value: <Error class: unknown class>): T
```

### with

```
protected fun with(key: String, vararg values: String): T
```