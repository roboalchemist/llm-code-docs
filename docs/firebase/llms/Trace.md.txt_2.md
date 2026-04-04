# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.md.txt

# Trace

# Trace


```
class Trace : Parcelable
```

<br />

*** ** * ** ***

Trace allows you to set beginning and end of a certain action in your app.

## Summary

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/kotlin/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace!>!` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#CREATOR()` A public static CREATOR field that implements `Parcelable.Creator` and generates instances of your Parcelable class from a Parcel. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#MAX_ATTRIBUTE_KEY_LENGTH() = 40` Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#MAX_ATTRIBUTE_VALUE_LENGTH() = 100` Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` attribute |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#MAX_TRACE_CUSTOM_ATTRIBUTES() = 5` Maximum allowed number of attributes allowed in a trace. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#describeContents()()` Describes the kinds of special objects contained in this Parcelable's marshalled representation. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#getAttribute(java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of an attribute. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#getAttributes()()` Returns the map of all the attributes added to this trace. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#getLongMetric(java.lang.String)(metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets the value of the metric with the given name in the current trace. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#incrementMetric(java.lang.String,long)(metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, incrementBy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Atomically increments the metric with the given name in this trace by the incrementBy value. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#putAttribute(java.lang.String,java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sets a String value for the specified attribute. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#putMetric(java.lang.String,long)(metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the value of the metric with the given name in this trace to the value provided. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#removeAttribute(java.lang.String)(attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Removes an already added attribute from the Traces. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#start()()` Starts this trace. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#stop()()` Stops this trace. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#writeToParcel(android.os.Parcel,int)(out: https://developer.android.com/reference/kotlin/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Flatten this object into a Parcel. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#name()` |

| ### Extension functions |
|---|---|
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)(block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace.() -> T)` Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR-- = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE-- = 1` | |

## Constants

### CREATOR

```
@Keep
const val CREATOR: Parcelable.Creator<Trace!>!
```

A public static CREATOR field that implements `Parcelable.Creator` and generates instances of your Parcelable class from a Parcel.

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

### describeContents

```
@Keep
fun describeContents(): Int
```

Describes the kinds of special objects contained in this Parcelable's marshalled representation.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | always returns 0. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/android/os/Parcelable.html` |   |

### getAttribute

```
@Keep
fun getAttribute(attribute: String): String?
```

Returns the value of an attribute.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | name of the attribute to fetch the value for |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the value of the attribute if it exists or null otherwise. |

### getAttributes

```
@Keep
fun getAttributes(): (Mutable)Map<String!, String!>
```

Returns the map of all the attributes added to this trace.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | map of attributes and its values currently added to this Trace |

### getLongMetric

```
@Keep
fun getLongMetric(metricName: String): Long
```

Gets the value of the metric with the given name in the current trace. If a metric with the given name doesn't exist, it is NOT created and a 0 is returned. This method is atomic.

| Parameters |
|---|---|
| `metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the metric to get. Requires no leading or trailing whitespace, no leading underscore '_' character, max length is 100 characters. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | Value of the metric or 0 if it hasn't yet been set. |

### incrementMetric

```
@Keep
fun incrementMetric(metricName: String, incrementBy: Long): Unit
```

Atomically increments the metric with the given name in this trace by the incrementBy value. If the metric does not exist, a new one will be created. If the trace has not been started or has already been stopped, returns immediately without taking action.

| Parameters |
|---|---|
| `metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the metric to be incremented. Requires no leading or trailing whitespace, no leading underscore \[_\] character, max length of 100 characters. |
| `incrementBy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | Amount by which the metric has to be incremented. |

### putAttribute

```
@Keep
fun putAttribute(attribute: String, value: String): Unit
```

Sets a String value for the specified attribute. Updates the value of the attribute if the attribute already exists. If the trace has been stopped, this method returns without adding the attribute. The maximum number of attributes that can be added to a Trace are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformanceAttributable#MAX_TRACE_CUSTOM_ATTRIBUTES()`.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the attribute |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Value of the attribute |

### putMetric

```
@Keep
fun putMetric(metricName: String, value: Long): Unit
```

Sets the value of the metric with the given name in this trace to the value provided. If a metric with the given name doesn't exist, a new one will be created. If the trace has not been started or has already been stopped, returns immediately without taking action. This method is atomic.

| Parameters |
|---|---|
| `metricName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the metric to set. Requires no leading or trailing whitespace, no leading underscore '_' character, max length is 100 characters. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The value to which the metric should be set to. |

### removeAttribute

```
@Keep
fun removeAttribute(attribute: String): Unit
```

Removes an already added attribute from the Traces. If the trace has been stopped, this method returns without removing the attribute.

| Parameters |
|---|---|
| `attribute: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the attribute to be removed from the running Traces. |

### start

```
@Keep
fun start(): Unit
```

Starts this trace.

### stop

```
@Keep
fun stop(): Unit
```

Stops this trace.

### writeToParcel

```
@Keep
fun writeToParcel(out: Parcel, flags: Int): Unit
```

Flatten this object into a Parcel. Please refer to https://developer.android.com/reference/android/os/Parcelable.html

| Parameters |
|---|---|
| `out: https://developer.android.com/reference/kotlin/android/os/Parcel.html` | the Parcel in which the object should be written. |
| `flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Additional flags about how the object should be written. |

## Public properties

### name

```
val name: String!
```

## Extension functions

### trace

```
inline fun <T : Any?> Trace.trace(block: Trace.() -> T): T
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace`.