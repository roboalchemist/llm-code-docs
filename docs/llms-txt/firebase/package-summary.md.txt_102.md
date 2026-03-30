# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary.md.txt

# com.google.firebase.firestore.pipeline.evaluation

# com.google.firebase.firestore.pipeline.evaluation

## Top-level functions summary

|---|---|
| `https://developer.android.com/reference/kotlin/java/time/temporal/ChronoUnit.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = 26) https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary#convertUnit(kotlin.String)(unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Converts string units to `https://developer.android.com/reference/kotlin/java/time/temporal/TemporalUnit.html`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary#isMicrosecondsInTimestampBounds(kotlin.Long)(microseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary#isMillisecondsInTimestampBounds(kotlin.Long)(milliseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary#isSecondsInTimestampBounds(kotlin.Long)(seconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/evaluation/package-summary#isTimestampInBounds(kotlin.Long,kotlin.Int)(seconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, nanos: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

## Top-level functions

### convertUnit

```
@RequiresApi(value = 26)
fun convertUnit(unit: String): ChronoUnit
```

Converts string units to `https://developer.android.com/reference/kotlin/java/time/temporal/TemporalUnit.html`.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/time/temporal/ChronoUnit.html` | the converted unit |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if `unit` is not among the list of recognized units. |

### isMicrosecondsInTimestampBounds

```
fun isMicrosecondsInTimestampBounds(microseconds: Long): Boolean
```

### isMillisecondsInTimestampBounds

```
fun isMillisecondsInTimestampBounds(milliseconds: Long): Boolean
```

### isSecondsInTimestampBounds

```
fun isSecondsInTimestampBounds(seconds: Long): Boolean
```

### isTimestampInBounds

```
fun isTimestampInBounds(seconds: Long, nanos: Int): Boolean
```