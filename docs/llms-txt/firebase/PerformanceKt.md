# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt.md.txt

# PerformanceKt

# PerformanceKt


```
public final class PerformanceKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                      ### Public fields                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebasePerformance](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance) | [performance](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.Firebase).performance()) Returns the [FirebasePerformance](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |

|                                               ### Public methods                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final void`                                                                                            | [PerformanceKt](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt)`.`[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpMetric](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric)` receiver,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpMetric](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> block` `)` Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)) wrapped by calls to start and stop using [HttpMetric](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric).                                                                         |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T` | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[PerformanceKt](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt)`.`[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace)` receiver,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T> block` `)` Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)) wrapped by calls to start and stop using [Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace). |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T` | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/PerformanceKt#trace(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T> block` `)` Creates a [Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace) object with given [name](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)) and measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)) wrapped by calls to start and stop.                        |

## Public fields

### performance

```
publicÂ finalÂ @NonNull FirebasePerformanceÂ performance
```

Returns the [FirebasePerformance](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

## Public methods

### PerformanceKt.trace

```
publicÂ staticÂ finalÂ voidÂ PerformanceKt.trace(
Â Â Â Â @NonNull HttpMetricÂ receiver,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull HttpMetric,Â Unit>Â block
)
```

Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)) wrapped by calls to start and stop using [HttpMetric](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric).  

### PerformanceKt.trace

```
publicÂ staticÂ finalÂ @NonNull TÂ <TÂ extendsÂ Object> PerformanceKt.trace(
Â Â Â Â @NonNull TraceÂ receiver,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull Trace,Â @NonNull T>Â block
)
```

Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)) wrapped by calls to start and stop using [Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace).  

### trace

```
publicÂ staticÂ finalÂ @NonNull TÂ <TÂ extendsÂ Object> trace(
Â Â Â Â @NonNull StringÂ name,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull Trace,Â @NonNull T>Â block
)
```

Creates a [Trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace) object with given [name](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)) and measures the time it takes to run the [block](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)) wrapped by calls to start and stop.