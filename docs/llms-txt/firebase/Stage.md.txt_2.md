# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage.md.txt

# Stage

# Stage


```
@Beta
sealed class Stage<T : Stage<T>>
```

<br />

Known direct subclasses [AggregateStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage), [CollectionGroupSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupSource), [CollectionSource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSource), [FindNearestStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage), [RawStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage), [SampleStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage), [UnnestStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | Performs optionally grouped aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupSource` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSource` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage` | Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents in the result set. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | Adds a stage to the pipeline by specifying the stage name as an argument. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | Performs a pseudo-random sampling of the input documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |

*** ** * ** ***

## Summary

| ### Protected constructors |
|---|
| `<T : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage<T>> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#Stage(kotlin.String,com.google.firebase.firestore.pipeline.InternalOptions)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/InternalOptions)` |

| ### Public functions |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter |

| ### Protected functions |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` |

## Protected constructors

### Stage

```
protected <T : Stage<T>> Stage(name: String, options: InternalOptions)
```

## Public functions

### withOption

```
fun withOption(key: String, value: Boolean): T
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of parameter |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value of parameter |

| Returns |
|---|---|
| `T` | New stage with named parameter. |

### withOption

```
fun withOption(key: String, value: Double): T
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of parameter |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` value of parameter |

| Returns |
|---|---|
| `T` | New stage with named parameter. |

### withOption

```
fun withOption(key: String, value: Field): T
```

Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of parameter |
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` value of parameter |

| Returns |
|---|---|
| `T` | New stage with named parameter. |

### withOption

```
fun withOption(key: String, value: Long): T
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of parameter |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value of parameter |

| Returns |
|---|---|
| `T` | New stage with named parameter. |

### withOption

```
fun withOption(key: String, value: String): T
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of parameter |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value of parameter |

| Returns |
|---|---|
| `T` | New stage with named parameter. |

## Protected functions

### withOption

```
protected fun withOption(key: String, value: <Error class: unknown class>): T
```