# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot.md.txt

# Pipeline.Snapshot

# Pipeline.Snapshot


```
class Pipeline.Snapshot : Iterable
```

<br />

*** ** * ** ***

A `Snapshot` contains the results of a pipeline execution. It can be iterated to retrieve the individual `PipelineResult` objects.

## Summary

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#hashCode()()` |
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#iterator()()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#toString()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#executionTime()` The time at which the pipeline producing this result is executed. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot#results()` List of all the results |

| ### Inherited functions |
|---|
| From [kotlin.collections.Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/for-each.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/util/function/Consumer.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult>)` | | `open https://developer.android.com/reference/kotlin/java/util/Spliterator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/spliterator.html()` | |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```

### iterator

```
open operator fun iterator(): Iterator<PipelineResult>
```

### toString

```
open fun toString(): String
```

## Public properties

### executionTime

```
val executionTime: Timestamp
```

The time at which the pipeline producing this result is executed.

### results

```
val results: List<PipelineResult>
```

List of all the results