# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions.md.txt

# Pipeline.ExecuteOptions

# Pipeline.ExecuteOptions


```
public final class Pipeline.ExecuteOptions extends AbstractOptions
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions) ||
|   | ↳ | [com.google.firebase.firestore.Pipeline.ExecuteOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions) |

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode` |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode.Companion` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions#ExecuteOptions()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions#withIndexMode(com.google.firebase.firestore.Pipeline.ExecuteOptions.IndexMode)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode indexMode)` |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.pipeline.AbstractOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?> newOptions)` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?> subSection)` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value)` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify generic `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` option | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions value)` Specify `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` object | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html values)` | |

## Public constructors

### ExecuteOptions

```
public ExecuteOptions()
```

## Public methods

### withIndexMode

```
public final @NonNull Pipeline.ExecuteOptions withIndexMode(@NonNull Pipeline.ExecuteOptions.IndexMode indexMode)
```