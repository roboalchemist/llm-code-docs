# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot.md.txt

# Pipeline.Snapshot

# Pipeline.Snapshot


```
public final class Pipeline.Snapshot implements Iterable
```

<br />

*** ** * ** ***

A `Snapshot` contains the results of a pipeline execution. It can be iterated to retrieve the individual `PipelineResult` objects.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#executionTime()` The time at which the pipeline producing this result is executed. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#results()` List of all the results |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Iterator.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#iterator()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot#toString()()` |

| ### Inherited methods |
|---|
| From [kotlin.collections.Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html) |---|---| | `void` | `https://developer.android.com/reference/kotlin/java/lang/Iterable.html#forEach-java.util.function.Consumer[com.google.firebase.firestore.PipelineResult]-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/function/Consumer.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult> p0)` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Spliterator.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Iterable.html#spliterator--()` | |

## Public fields

### executionTime

```
public final @NonNull Timestamp executionTime
```

The time at which the pipeline producing this result is executed.

### results

```
public final @NonNull List<@NonNull PipelineResult> results
```

List of all the results

## Public methods

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```

### iterator

```
public @NonNull Iterator<@NonNull PipelineResult> iterator()
```

### toString

```
public @NonNull String toString()
```