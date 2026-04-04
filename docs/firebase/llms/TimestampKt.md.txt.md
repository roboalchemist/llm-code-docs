# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt.md.txt

# TimestampKt

# TimestampKt


```
public final class TimestampKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/time/temporal/ChronoUnit.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = 26) https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt#convertUnit(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit)` Converts string units to `https://developer.android.com/reference/kotlin/java/time/temporal/TemporalUnit.html`. |
| `static final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt#isMicrosecondsInTimestampBounds(kotlin.Long)(long microseconds)` |
| `static final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt#isMillisecondsInTimestampBounds(kotlin.Long)(long milliseconds)` |
| `static final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt#isSecondsInTimestampBounds(kotlin.Long)(long seconds)` |
| `static final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/evaluation/TimestampKt#isTimestampInBounds(kotlin.Long,kotlin.Int)(long seconds, int nanos)` |

## Public methods

### convertUnit

```
@RequiresApi(value = 26)
public static final @NonNull ChronoUnit convertUnit(@NonNull String unit)
```

Converts string units to `https://developer.android.com/reference/kotlin/java/time/temporal/TemporalUnit.html`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/time/temporal/ChronoUnit.html` | the converted unit |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | if `unit` is not among the list of recognized units. |

### isMicrosecondsInTimestampBounds

```
public static final boolean isMicrosecondsInTimestampBounds(long microseconds)
```

### isMillisecondsInTimestampBounds

```
public static final boolean isMillisecondsInTimestampBounds(long milliseconds)
```

### isSecondsInTimestampBounds

```
public static final boolean isSecondsInTimestampBounds(long seconds)
```

### isTimestampInBounds

```
public static final boolean isTimestampInBounds(long seconds, int nanos)
```