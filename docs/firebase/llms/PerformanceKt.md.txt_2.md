# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt.md.txt

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
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.ktx.Firebase).performance()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt.[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt.[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> block )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> [trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#trace(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> block )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### performance

```
public final @NonNull FirebasePerformance performance
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### PerformanceKt.trace

```
public static final void PerformanceKt.[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))(
    @NonNull HttpMetric receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpMetric, Unit> block
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### PerformanceKt.trace

```
public static final @NonNull T <T extends Object> PerformanceKt.[trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1))(
    @NonNull Trace receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull Trace, @NonNull T> block
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### trace

```
public static final @NonNull T <T extends Object> [trace](https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/PerformanceKt#trace(kotlin.String,kotlin.Function1))(
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull Trace, @NonNull T> block
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` object with given `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1)` and measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/ktx/package-summary#trace(kotlin.String,kotlin.Function1)` wrapped by calls to start and stop.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)