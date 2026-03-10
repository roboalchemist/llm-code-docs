# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage.md.txt

# FindNearestStage

# FindNearestStage


```
@Beta
public final class FindNearestStage extends Stage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.FindNearestStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage) |

*** ** * ** ***

Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents in the result set.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage.Companion` |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure` |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure.Companion` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage#hashCode()()` |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value )` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public methods

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```