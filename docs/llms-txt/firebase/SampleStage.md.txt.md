# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.md.txt

# SampleStage

# SampleStage


```
@Beta
public final class SampleStage extends Stage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.SampleStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage) |

*** ** * ** ***

Performs a pseudo-random sampling of the input documents.

The documents produced from this stage are non-deterministic, running the same query over the same dataset multiple times will produce different results. There are two different ways to dictate how the sample is calculated either by specifying a target output size, or by specifying a target percentage of the input size.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion` |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Mode` |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Mode.Companion` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage#hashCode()()` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)(int results)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)(double percentage)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results. |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value )` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public methods

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```

### withDocLimit

```
public static final @NonNull SampleStage withDocLimit(int results)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)` parameter represents the number of results to produce and must be a non-negative integer value. If the previous stage produces less than the specified number, the entire previous results are returned. If the previous stage produces more than the specified number, this stage samples the specified number of documents from the previous stage, with equal probability for each result.

| Parameters |
|---|---|
| `int results` | The number of documents to emit. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with specified documents. |

### withPercentage

```
public static final @NonNull SampleStage withPercentage(double percentage)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)` parameter is the target percentage (between 0.0 \& 1.0) of the number of input documents to produce. Each input document is independently selected against the given percentage. As a result the output size will be approximately documents \* `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`.

| Parameters |
|---|---|
| `double percentage` | The percentage of the prior stages documents to emit. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`. |