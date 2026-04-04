# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.md.txt

# FirebasePerformance

# FirebasePerformance


```
@Singleton
public class FirebasePerformance
```

<br />

*** ** * ** ***

The Firebase Performance Monitoring API.

It is automatically initialized by FirebaseApp.

This SDK uses FirebaseInstallations to identify the app instance and periodically sends data to the Firebase backend. To stop sending performance events, call `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean)`.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.HttpMethod` Valid HttpMethods for manual network APIs |

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_KEY_LENGTH() = 40` Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_VALUE_LENGTH() = 100` Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_CUSTOM_ATTRIBUTES() = 5` Maximum allowed number of attributes allowed in a trace. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#getInstance()()` Returns a singleton of FirebasePerformance. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#isPerformanceCollectionEnabled()()` Determines whether performance monitoring is enabled or disabled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.lang.String,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url, @https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.HttpMethod @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html httpMethod )` Creates a HttpMetric object for collecting network performance data for one request/response |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.net.URL,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url, @https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.HttpMethod @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html httpMethod )` Creates a HttpMetric object for collecting network performance data for one request/response |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#newTrace(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html traceName)` Creates a Trace object with given name. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean)(boolean enable)` Enables or disables performance monitoring. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#startTrace(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html traceName)` Creates a Trace object with given name and start the trace. |

## Constants

### MAX_ATTRIBUTE_KEY_LENGTH

```
public static final int MAX_ATTRIBUTE_KEY_LENGTH = 40
```

Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute

### MAX_ATTRIBUTE_VALUE_LENGTH

```
public static final int MAX_ATTRIBUTE_VALUE_LENGTH = 100
```

Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute

### MAX_TRACE_CUSTOM_ATTRIBUTES

```
public static final int MAX_TRACE_CUSTOM_ATTRIBUTES = 5
```

Maximum allowed number of attributes allowed in a trace.

### MAX_TRACE_NAME_LENGTH

```
public static final int MAX_TRACE_NAME_LENGTH = 100
```

Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`

### MAX_TRACE_NAME_LENGTH

```
public static final int MAX_TRACE_NAME_LENGTH = 100
```

Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`

## Public methods

### getInstance

```
public static @NonNull FirebasePerformance getInstance()
```

Returns a singleton of FirebasePerformance.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance` | the singleton FirebasePerformance object. |

### isPerformanceCollectionEnabled

```
public boolean isPerformanceCollectionEnabled()
```

Determines whether performance monitoring is enabled or disabled. This respects the Firebase Performance specific values first, and if these aren't set, uses the Firebase wide data collection switch.

| Returns |
|---|---|
| `boolean` | true if performance monitoring is enabled and false if performance monitoring is disabled. This is for dynamic enable/disable state. This does not reflect whether instrumentation is enabled/disabled in Gradle properties. |

### newHttpMetric

```
public @NonNull HttpMetric newHttpMetric(
    @NonNull String url,
    @FirebasePerformance.HttpMethod @NonNull String httpMethod
)
```

Creates a HttpMetric object for collecting network performance data for one request/response

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | a valid url String, cannot be empty |
| `@https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.HttpMethod @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html httpMethod` | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric` | the new HttpMetric object. |

### newHttpMetric

```
public @NonNull HttpMetric newHttpMetric(
    @NonNull URL url,
    @FirebasePerformance.HttpMethod @NonNull String httpMethod
)
```

Creates a HttpMetric object for collecting network performance data for one request/response

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url` | a valid URL object |
| `@https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.HttpMethod @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html httpMethod` | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric` | the new HttpMetric object. |

### newTrace

```
public @NonNull Trace newTrace(@NonNull String traceName)
```

Creates a Trace object with given name.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html traceName` | name of the trace, requires no leading or trailing whitespace, no leading underscore '_' character, max length is `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()` characters. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` | the new Trace object. |

### setPerformanceCollectionEnabled

```
public void setPerformanceCollectionEnabled(boolean enable)
```

Enables or disables performance monitoring. This setting is persisted and applied on future invocations of your application. By default, performance monitoring is enabled. If you need to change the default (for example, because you want to prompt the user before collecting performance stats), add:

```
<meta-data android:name=firebase_performance_collection_enabled android:value=false />
```
to your application's manifest. Changing the value during runtime will override the manifest value.

If you want to permanently disable sending performance metrics, add

```
<meta-data android:name="firebase_performance_collection_deactivated" android:value="true" />
```
to your application's manifest. Changing the value during runtime will not override the manifest value.

This is separate from enabling/disabling instrumentation in Gradle properties.

| Parameters |
|---|---|
| `boolean enable` | Should performance monitoring be enabled |

### startTrace

```
public static @NonNull Trace startTrace(@NonNull String traceName)
```

Creates a Trace object with given name and start the trace.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html traceName` | name of the trace. Requires no leading or trailing whitespace, no leading underscore \[_\] character, max length of `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()` characters. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` | the new Trace object. |