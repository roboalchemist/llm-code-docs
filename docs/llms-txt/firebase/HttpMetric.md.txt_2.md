# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.md.txt

# HttpMetric

# HttpMetric


```
class HttpMetric
```

<br />

*** ** * ** ***

Metric used to collect data for network requests/responses. A new object must be used for every request/response. This class is not thread safe.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_ATTRIBUTE_KEY_LENGTH() = 40` Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_ATTRIBUTE_VALUE_LENGTH() = 100` Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_TRACE_CUSTOM_ATTRIBUTES() = 5` Maximum allowed number of attributes allowed in a trace. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#getAttribute(java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of an attribute. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#getAttributes()()` Returns the map of all the attributes added to this HttpMetric. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#putAttribute(java.lang.String,java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sets a String value for the specified attribute. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#removeAttribute(java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Removes an already added attribute from the HttpMetric. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setHttpResponseCode(int)(responseCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets the httpResponse code of the request |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setRequestPayloadSize(long)(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the size of the request payload |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setResponseContentType(java.lang.String)(contentType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Content type of the response such as text/html, application/json, etc... |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setResponsePayloadSize(long)(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the size of the response payload |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#start()()` Marks the start time of the request |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#stop()()` Marks the end time of the response and queues the network request metric on the device for transmission. |

| ### Extension functions |
|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric`. |

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

## Public functions

### getAttribute

```
fun getAttribute(attribute: String): String?
```

Returns the value of an attribute.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the attribute to fetch the value for |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The value of the attribute if it exists or null otherwise. |

### getAttributes

```
fun getAttributes(): (Mutable)Map<String!, String!>
```

Returns the map of all the attributes added to this HttpMetric.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | map of attributes and its values currently added to this HttpMetric |

### putAttribute

```
fun putAttribute(attribute: String, value: String): Unit
```

Sets a String value for the specified attribute. Updates the value of the attribute if the attribute already exists. If the HttpMetric has been stopped, this method returns without adding the attribute. The maximum number of attributes that can be added to a HttpMetric are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformanceAttributable#MAX_TRACE_CUSTOM_ATTRIBUTES()`.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the attribute |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | value of the attribute |

### removeAttribute

```
fun removeAttribute(attribute: String): Unit
```

Removes an already added attribute from the HttpMetric. If the HttpMetric has already been stopped, this method returns without removing the attribute.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the attribute to be removed from the running Traces. |

### setHttpResponseCode

```
fun setHttpResponseCode(responseCode: Int): Unit
```

Sets the httpResponse code of the request

| Parameters |
|---|---|
| `responseCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | valid values are greater than 0. Invalid usage will be logged. |

### setRequestPayloadSize

```
fun setRequestPayloadSize(bytes: Long): Unit
```

Sets the size of the request payload

| Parameters |
|---|---|
| `bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | valid values are greater than or equal to 0. Invalid usage will be logged. |

### setResponseContentType

```
fun setResponseContentType(contentType: String?): Unit
```

Content type of the response such as text/html, application/json, etc...

| Parameters |
|---|---|
| `contentType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | valid string of MIME type. Invalid usage will be logged. |

### setResponsePayloadSize

```
fun setResponsePayloadSize(bytes: Long): Unit
```

Sets the size of the response payload

| Parameters |
|---|---|
| `bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | valid values are greater than or equal to 0. Invalid usage will be logged. |

### start

```
fun start(): Unit
```

Marks the start time of the request

### stop

```
fun stop(): Unit
```

Marks the end time of the response and queues the network request metric on the device for transmission. Check logcat for transmission info.

## Extension functions

### trace

```
inline fun HttpMetric.trace(block: HttpMetric.() -> Unit): Unit
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric`.