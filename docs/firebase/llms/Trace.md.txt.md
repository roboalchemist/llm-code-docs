# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace.md.txt

# Trace

# Trace


```
public class Trace implements Parcelable
```

<br />

*** ** * ** ***

Trace allows you to set beginning and end of a certain action in your app.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/kotlin/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#CREATOR()` A public static CREATOR field that implements `Parcelable.Creator` and generates instances of your Parcelable class from a Parcel. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#MAX_ATTRIBUTE_KEY_LENGTH() = 40` Maximum allowed length of the Key of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#MAX_ATTRIBUTE_VALUE_LENGTH() = 100` Maximum allowed length of the Value of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` attribute |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#MAX_TRACE_CUSTOM_ATTRIBUTES() = 5` Maximum allowed number of attributes allowed in a trace. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#MAX_TRACE_NAME_LENGTH() = 100` Maximum allowed length of the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#name()` |

| ### Public methods |
|---|---|
| `int` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#describeContents()()` Describes the kinds of special objects contained in this Parcelable's marshalled representation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#getAttribute(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute)` Returns the value of an attribute. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#getAttributes()()` Returns the map of all the attributes added to this trace. |
| `long` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#getLongMetric(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName)` Gets the value of the metric with the given name in the current trace. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#incrementMetric(java.lang.String,long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName, long incrementBy)` Atomically increments the metric with the given name in this trace by the incrementBy value. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#putAttribute(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Sets a String value for the specified attribute. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#putMetric(java.lang.String,long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName, long value)` Sets the value of the metric with the given name in this trace to the value provided. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#removeAttribute(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute)` Removes an already added attribute from the Traces. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#start()()` Starts this trace. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#stop()()` Stops this trace. |
| `void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#writeToParcel(android.os.Parcel,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/os/Parcel.html out, int flags)` Flatten this object into a Parcel. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/PerformanceKt.https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> block )` Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR-- = 1` | | `static final int` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE-- = 1` | |

## Constants

### CREATOR

```
@Keep
public static final Parcelable.Creator<Trace> CREATOR
```

A public static CREATOR field that implements `Parcelable.Creator` and generates instances of your Parcelable class from a Parcel.

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

## Public fields

### name

```
public final String name
```

## Public methods

### describeContents

```
@Keep
public int describeContents()
```

Describes the kinds of special objects contained in this Parcelable's marshalled representation.

| Returns |
|---|---|
| `int` | always returns 0. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/android/os/Parcelable.html` |   |

### getAttribute

```
@Keep
public @Nullable String getAttribute(@NonNull String attribute)
```

Returns the value of an attribute.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute` | name of the attribute to fetch the value for |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the value of the attribute if it exists or null otherwise. |

### getAttributes

```
@Keep
public @NonNull Map<String, String> getAttributes()
```

Returns the map of all the attributes added to this trace.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | map of attributes and its values currently added to this Trace |

### getLongMetric

```
@Keep
public long getLongMetric(@NonNull String metricName)
```

Gets the value of the metric with the given name in the current trace. If a metric with the given name doesn't exist, it is NOT created and a 0 is returned. This method is atomic.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName` | Name of the metric to get. Requires no leading or trailing whitespace, no leading underscore '_' character, max length is 100 characters. |

| Returns |
|---|---|
| `long` | Value of the metric or 0 if it hasn't yet been set. |

### incrementMetric

```
@Keep
public void incrementMetric(@NonNull String metricName, long incrementBy)
```

Atomically increments the metric with the given name in this trace by the incrementBy value. If the metric does not exist, a new one will be created. If the trace has not been started or has already been stopped, returns immediately without taking action.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName` | Name of the metric to be incremented. Requires no leading or trailing whitespace, no leading underscore \[_\] character, max length of 100 characters. |
| `long incrementBy` | Amount by which the metric has to be incremented. |

### putAttribute

```
@Keep
public void putAttribute(@NonNull String attribute, @NonNull String value)
```

Sets a String value for the specified attribute. Updates the value of the attribute if the attribute already exists. If the trace has been stopped, this method returns without adding the attribute. The maximum number of attributes that can be added to a Trace are `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformanceAttributable#MAX_TRACE_CUSTOM_ATTRIBUTES()`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute` | Name of the attribute |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | Value of the attribute |

### putMetric

```
@Keep
public void putMetric(@NonNull String metricName, long value)
```

Sets the value of the metric with the given name in this trace to the value provided. If a metric with the given name doesn't exist, a new one will be created. If the trace has not been started or has already been stopped, returns immediately without taking action. This method is atomic.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html metricName` | Name of the metric to set. Requires no leading or trailing whitespace, no leading underscore '_' character, max length is 100 characters. |
| `long value` | The value to which the metric should be set to. |

### removeAttribute

```
@Keep
public void removeAttribute(@NonNull String attribute)
```

Removes an already added attribute from the Traces. If the trace has been stopped, this method returns without removing the attribute.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html attribute` | Name of the attribute to be removed from the running Traces. |

### start

```
@Keep
public void start()
```

Starts this trace.

### stop

```
@Keep
public void stop()
```

Stops this trace.

### writeToParcel

```
@Keep
public void writeToParcel(@NonNull Parcel out, int flags)
```

Flatten this object into a Parcel. Please refer to https://developer.android.com/reference/android/os/Parcelable.html

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/os/Parcel.html out` | the Parcel in which the object should be written. |
| `int flags` | Additional flags about how the object should be written. |

## Extension functions

### PerformanceKt.trace

```
public final @NonNull T <T extends Object> PerformanceKt.trace(
    @NonNull Trace receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull Trace, @NonNull T> block
)
```

Measures the time it takes to run the `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.Trace).trace(kotlin.Function1)` wrapped by calls to start and stop using `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace`.