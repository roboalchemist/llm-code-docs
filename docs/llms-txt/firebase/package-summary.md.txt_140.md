# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary.md.txt

# com.google.firebase.perf

# com.google.firebase.perf

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` | The Firebase Performance Monitoring API. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod` | Valid HttpMethods for manual network APIs |

## Top-level functions summary

|---|---|
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.() -> T)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop. |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric`. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.() -> T)` Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.Firebase).performance()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Top-level functions

### trace

```
inline fun <T : Any?> trace(name: String, block: Trace.() -> T): T
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop.

## Extension functions

### trace

```
inline fun HttpMetric.trace(block: HttpMetric.() -> Unit): Unit
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric`.

### trace

```
inline fun <T : Any?> Trace.trace(block: Trace.() -> T): T
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`.

## Extension properties

### performance

```
val Firebase.performance: FirebasePerformance
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.