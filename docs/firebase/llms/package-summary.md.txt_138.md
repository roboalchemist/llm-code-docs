# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary.md.txt

# com.google.firebase.perf.ktx

# com.google.firebase.perf.ktx

## Top-level functions summary

|---|---|
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> [trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1))(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.() -> T)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.[trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.[trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1))(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.() -> T)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.ktx.Firebase).performance()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### trace

```
inline fun <T : Any?> [trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1))(name: String, block: Trace.() -> T): T
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension functions

### trace

```
inline fun HttpMetric.[trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))(block: HttpMetric.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### trace

```
inline fun <T : Any?> Trace.[trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1))(block: Trace.() -> T): T
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### performance

```
val Firebase.performance: FirebasePerformance
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)