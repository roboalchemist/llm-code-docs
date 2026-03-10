# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt.md.txt

# PerformanceKt

# PerformanceKt


```
public final class PerformanceKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.Firebase).performance()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt.https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt.https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> block )` Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#trace(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> block )` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop. |

## Public fields

### performance

```
public final @NonNull FirebasePerformance performance
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### PerformanceKt.trace

```
public static final void PerformanceKt.trace(
    @NonNull HttpMetric receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpMetric, Unit> block
)
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric`.

### PerformanceKt.trace

```
public static final @NonNull T <T extends Object> PerformanceKt.trace(
    @NonNull Trace receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull Trace, @NonNull T> block
)
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`.

### trace

```
public static final @NonNull T <T extends Object> trace(
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull Trace, @NonNull T> block
)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop.