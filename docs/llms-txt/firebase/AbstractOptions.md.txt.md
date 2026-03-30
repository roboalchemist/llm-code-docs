# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions.md.txt

# AbstractOptions

# AbstractOptions


```
public abstract class AbstractOptions<T extends AbstractOptions<@NonNull T>>
```

<br />

Known direct subclasses [AggregateHints](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateHints), [AggregateOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateOptions), [CollectionGroupOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions), [CollectionHints](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionHints), [CollectionSourceOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions), [FindNearestOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestOptions), [Pipeline.ExecuteOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions), [RawOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions), [UnnestOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestOptions)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateHints` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionHints` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestOptions` |   |

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify generic `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` option |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.RawOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions value)` Specify `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` object |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option |

| ### Protected methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#adding(com.google.firebase.firestore.pipeline.AbstractOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?> newOptions)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,com.google.firebase.firestore.pipeline.AbstractOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?> subSection)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,[Error type: Unresolved type for Value])(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions#with(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html values)` |

## Public methods

### with

```
public final @NonNull T with(@NonNull String key, boolean value)
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` option

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `boolean value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value of option |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

### with

```
public final @NonNull T with(@NonNull String key, double value)
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` option

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `double value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` value of option |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

### with

```
public final @NonNull T with(@NonNull String key, @NonNull Field value)
```

Specify generic `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` option

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` value of option |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

### with

```
public final @NonNull T with(@NonNull String key, long value)
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` option

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `long value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value of option |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

### with

```
public final @NonNull T with(@NonNull String key, @NonNull RawOptions value)
```

Specify `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` object

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` object |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

### with

```
public final @NonNull T with(@NonNull String key, @NonNull String value)
```

Specify generic `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` option

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The option key |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value of option |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | A new options object. |

## Protected methods

### adding

```
protected final @NonNull T adding(@NonNull AbstractOptions<@NonNull ?> newOptions)
```

### with

```
protected final @NonNull T with(@NonNull String key, @NonNull AbstractOptions<@NonNull ?> subSection)
```

### with

```
protected final @NonNull T with(@NonNull String key, @NonNull <Error class: unknown class> value)
```

### with

```
protected final @NonNull T with(@NonNull String key, @NonNull String values)
```