# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.md.txt

# SampleStage

# SampleStage


```
@Beta
class SampleStage : Stage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.SampleStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage) |

*** ** * ** ***

Performs a pseudo-random sampling of the input documents.

The documents produced from this stage are non-deterministic, running the same query over the same dataset multiple times will produce different results. There are two different ways to dictate how the sample is calculated either by specifying a target output size, or by specifying a target percentage of the input size.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Mode` |

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)(results: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)(percentage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage#hashCode()()` |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public companion functions

### withDocLimit

```
fun withDocLimit(results: Int): SampleStage
```

Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)` parameter represents the number of results to produce and must be a non-negative integer value. If the previous stage produces less than the specified number, the entire previous results are returned. If the previous stage produces more than the specified number, this stage samples the specified number of documents from the previous stage, with equal probability for each result.

| Parameters |
|---|---|
| `results: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of documents to emit. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with specified documents. |

### withPercentage

```
fun withPercentage(percentage: Double): SampleStage
```

Creates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)` parameter is the target percentage (between 0.0 \& 1.0) of the number of input documents to produce. Each input document is independently selected against the given percentage. As a result the output size will be approximately documents \* `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`.

| Parameters |
|---|---|
| `percentage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The percentage of the prior stages documents to emit. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` with specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`. |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```