# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage.md.txt

# Stage

# Stage


```
@Beta
public class Stage<T extends Stage<@NonNull T>>
```

<br />

Known direct subclasses [AggregateStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage), [CollectionGroupSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupSource), [CollectionSource](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSource), [FindNearestStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage), [RawStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawStage), [SampleStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage), [UnnestStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | Performs optionally grouped aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupSource` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSource` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents in the result set. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawStage` | Adds a stage to the pipeline by specifying the stage name as an argument. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | Performs a pseudo-random sampling of the input documents. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |

*** ** * ** ***

## Summary

| ### Protected constructors |
|---|
| `<T extends https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#Stage(kotlin.String,com.google.firebase.firestore.pipeline.InternalOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/InternalOptions options )` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter |

| ### Protected methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value )` |

## Protected constructors

### Stage

```
protected <T extends Stage<@NonNull T>> Stage(
    @NonNull String name,
    @NonNull InternalOptions options
)
```

## Public methods

### withOption

```
public final @NonNull T withOption(@NonNull String key, boolean value)
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of parameter |
| `boolean value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value of parameter |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | New stage with named parameter. |

### withOption

```
public final @NonNull T withOption(@NonNull String key, double value)
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of parameter |
| `double value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` value of parameter |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | New stage with named parameter. |

### withOption

```
public final @NonNull T withOption(@NonNull String key, @NonNull Field value)
```

Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` value of parameter |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | New stage with named parameter. |

### withOption

```
public final @NonNull T withOption(@NonNull String key, long value)
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of parameter |
| `long value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value of parameter |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | New stage with named parameter. |

### withOption

```
public final @NonNull T withOption(@NonNull String key, @NonNull String value)
```

Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value of parameter |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | New stage with named parameter. |

## Protected methods

### withOption

```
protected final @NonNull T withOption(
    @NonNull String key,
    @NonNull <Error class: unknown class> value
)
```