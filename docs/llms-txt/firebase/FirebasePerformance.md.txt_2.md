# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.md.txt

# FirebasePerformance

# FirebasePerformance


```
@Singleton
class FirebasePerformance
```

<br />

*** ** * ** ***

The Firebase Performance Monitoring API.

It is automatically initialized by FirebaseApp.

This SDK uses FirebaseInstallations to identify the app instance and periodically sends data to the Firebase backend. To stop sending performance events, call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean)`.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) annotation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod` Valid HttpMethods for manual network APIs |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_KEY_LENGTH() = 40` Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_VALUE_LENGTH() = 100` Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_CUSTOM_ATTRIBUTES() = 5` Maximum allowed number of attributes allowed in a trace. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#getInstance()()` Returns a singleton of FirebasePerformance. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#isPerformanceCollectionEnabled()()` Determines whether performance monitoring is enabled or disabled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.lang.String,java.lang.String)( url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, @https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod httpMethod: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates a HttpMetric object for collecting network performance data for one request/response |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.net.URL,java.lang.String)(url: https://developer.android.com/reference/kotlin/java/net/URL.html, @https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod httpMethod: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a HttpMetric object for collecting network performance data for one request/response |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newTrace(java.lang.String)(traceName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a Trace object with given name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean)(enable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Enables or disables performance monitoring. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#startTrace(java.lang.String)(traceName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a Trace object with given name and start the trace. |

## Constants

### MAX_ATTRIBUTE_KEY_LENGTH

```
const val MAX_ATTRIBUTE_KEY_LENGTH = 40: Int
```

Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute

### MAX_ATTRIBUTE_VALUE_LENGTH

```
const val MAX_ATTRIBUTE_VALUE_LENGTH = 100: Int
```

Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute

### MAX_TRACE_CUSTOM_ATTRIBUTES

```
const val MAX_TRACE_CUSTOM_ATTRIBUTES = 5: Int
```

Maximum allowed number of attributes allowed in a trace.

### MAX_TRACE_NAME_LENGTH

```
const val MAX_TRACE_NAME_LENGTH = 100: Int
```

Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`

### MAX_TRACE_NAME_LENGTH

```
const val MAX_TRACE_NAME_LENGTH = 100: Int
```

Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`

## Public functions

### getInstance

```
java-static fun getInstance(): FirebasePerformance
```

Returns a singleton of FirebasePerformance.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance` | the singleton FirebasePerformance object. |

### isPerformanceCollectionEnabled

```
fun isPerformanceCollectionEnabled(): Boolean
```

Determines whether performance monitoring is enabled or disabled. This respects the Firebase Performance specific values first, and if these aren't set, uses the Firebase wide data collection switch.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if performance monitoring is enabled and false if performance monitoring is disabled. This is for dynamic enable/disable state. This does not reflect whether instrumentation is enabled/disabled in Gradle properties. |

### newHttpMetric

```
fun newHttpMetric(
    url: String,
    @FirebasePerformance.HttpMethod httpMethod: String
): HttpMetric
```

Creates a HttpMetric object for collecting network performance data for one request/response

| Parameters |
|---|---|
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid url String, cannot be empty |
| `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod httpMethod: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric` | the new HttpMetric object. |

### newHttpMetric

```
fun newHttpMetric(url: URL, @FirebasePerformance.HttpMethod httpMethod: String): HttpMetric
```

Creates a HttpMetric object for collecting network performance data for one request/response

| Parameters |
|---|---|
| `url: https://developer.android.com/reference/kotlin/java/net/URL.html` | a valid URL object |
| `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod httpMethod: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric` | the new HttpMetric object. |

### newTrace

```
fun newTrace(traceName: String): Trace
```

Creates a Trace object with given name.

| Parameters |
|---|---|
| `traceName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the trace, requires no leading or trailing whitespace, no leading underscore '_' character, max length is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()` characters. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` | the new Trace object. |

### setPerformanceCollectionEnabled

```
fun setPerformanceCollectionEnabled(enable: Boolean): Unit
```

Enables or disables performance monitoring. This setting is persisted and applied on future invocations of your application. By default, performance monitoring is enabled. If you need to change the default (for example, because you want to prompt the user before collecting performance stats), add:

```kotlin
<meta-data android:name=firebase_performance_collection_enabled android:value=false />
```
to your application's manifest. Changing the value during runtime will override the manifest value.

If you want to permanently disable sending performance metrics, add

```kotlin
<meta-data android:name="firebase_performance_collection_deactivated" android:value="true" />
```
to your application's manifest. Changing the value during runtime will not override the manifest value.

This is separate from enabling/disabling instrumentation in Gradle properties.

| Parameters |
|---|---|
| `enable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Should performance monitoring be enabled |

### startTrace

```
java-static fun startTrace(traceName: String): Trace
```

Creates a Trace object with given name and start the trace.

| Parameters |
|---|---|
| `traceName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the trace. Requires no leading or trailing whitespace, no leading underscore \[_\] character, max length of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()` characters. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` | the new Trace object. |