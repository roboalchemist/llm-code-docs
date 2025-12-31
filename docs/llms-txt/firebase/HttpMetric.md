# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/HttpMetric.md.txt

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

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_ATTRIBUTE_KEY_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_ATTRIBUTE_KEY_LENGTH())` = 40` Maximum allowed length of the Key of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute        |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_ATTRIBUTE_VALUE_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_ATTRIBUTE_VALUE_LENGTH())` = 100` Maximum allowed length of the Value of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_TRACE_CUSTOM_ATTRIBUTES](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_TRACE_CUSTOM_ATTRIBUTES())` = 5` Maximum allowed number of attributes allowed in a trace.                                                                                               |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_TRACE_NAME_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#MAX_TRACE_NAME_LENGTH())` = 100` Maximum allowed length of the name of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)                      |

|                                                                                                                                                                            ### Public functions                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                                                                        | [getAttribute](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#getAttribute(java.lang.String))`(attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of an attribute.                                                                                                                           |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | [getAttributes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#getAttributes())`()` Returns the map of all the attributes added to this HttpMetric.                                                                                                                                                                                                         |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [putAttribute](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#putAttribute(java.lang.String,java.lang.String))`(attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Sets a String value for the specified attribute. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [removeAttribute](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#removeAttribute(java.lang.String))`(attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Removes an already added attribute from the HttpMetric.                                                                                                |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [setHttpResponseCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setHttpResponseCode(int))`(responseCode: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Sets the httpResponse code of the request                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [setRequestPayloadSize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setRequestPayloadSize(long))`(bytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Sets the size of the request payload                                                                                                                           |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [setResponseContentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setResponseContentType(java.lang.String))`(contentType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Content type of the response such as text/html, application/json, etc...                                                              |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [setResponsePayloadSize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#setResponsePayloadSize(long))`(bytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Sets the size of the response payload                                                                                                                        |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [start](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#start())`()` Marks the start time of the request                                                                                                                                                                                                                                                     |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                               | [stop](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#stop())`()` Marks the end time of the response and queues the network request metric on the device for transmission.                                                                                                                                                                                  |

|                                ### Extension functions                                |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inline `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric)`.`[trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1))`(block: `[HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)) wrapped by calls to start and stop using [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric). |

## Constants

### MAX_ATTRIBUTE_KEY_LENGTH

```
constÂ valÂ MAX_ATTRIBUTE_KEY_LENGTH = 40:Â Int
```

Maximum allowed length of the Key of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute  

### MAX_ATTRIBUTE_VALUE_LENGTH

```
constÂ valÂ MAX_ATTRIBUTE_VALUE_LENGTH = 100:Â Int
```

Maximum allowed length of the Value of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute  

### MAX_TRACE_CUSTOM_ATTRIBUTES

```
constÂ valÂ MAX_TRACE_CUSTOM_ATTRIBUTES = 5:Â Int
```

Maximum allowed number of attributes allowed in a trace.  

### MAX_TRACE_NAME_LENGTH

```
constÂ valÂ MAX_TRACE_NAME_LENGTH = 100:Â Int
```

Maximum allowed length of the name of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)  

## Public functions

### getAttribute

```
funÂ getAttribute(attribute:Â String):Â String?
```

Returns the value of an attribute.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| `attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | name of the attribute to fetch the value for |

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value of the attribute if it exists or null otherwise. |

### getAttributes

```
funÂ getAttributes():Â (Mutable)Map<String!,Â String!>
```

Returns the map of all the attributes added to this HttpMetric.  

|                                                                                                                                                                                  Returns                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | map of attributes and its values currently added to this HttpMetric |

### putAttribute

```
funÂ putAttribute(attribute:Â String,Â value:Â String):Â Unit
```

Sets a String value for the specified attribute. Updates the value of the attribute if the attribute already exists. If the HttpMetric has been stopped, this method returns without adding the attribute. The maximum number of attributes that can be added to a HttpMetric are [MAX_TRACE_CUSTOM_ATTRIBUTES](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformanceAttributable#MAX_TRACE_CUSTOM_ATTRIBUTES()).  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|------------------------|
| `attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | name of the attribute  |
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)     | value of the attribute |

### removeAttribute

```
funÂ removeAttribute(attribute:Â String):Â Unit
```

Removes an already added attribute from the HttpMetric. If the HttpMetric has already been stopped, this method returns without removing the attribute.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `attribute: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | name of the attribute to be removed from the running Traces. |

### setHttpResponseCode

```
funÂ setHttpResponseCode(responseCode:Â Int):Â Unit
```

Sets the httpResponse code of the request  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `responseCode: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | valid values are greater than 0. Invalid usage will be logged. |

### setRequestPayloadSize

```
funÂ setRequestPayloadSize(bytes:Â Long):Â Unit
```

Sets the size of the request payload  

|                                      Parameters                                       |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `bytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | valid values are greater than or equal to 0. Invalid usage will be logged. |

### setResponseContentType

```
funÂ setResponseContentType(contentType:Â String?):Â Unit
```

Content type of the response such as text/html, application/json, etc...  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `contentType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | valid string of MIME type. Invalid usage will be logged. |

### setResponsePayloadSize

```
funÂ setResponsePayloadSize(bytes:Â Long):Â Unit
```

Sets the size of the response payload  

|                                      Parameters                                       |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `bytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | valid values are greater than or equal to 0. Invalid usage will be logged. |

### start

```
funÂ start():Â Unit
```

Marks the start time of the request  

### stop

```
funÂ stop():Â Unit
```

Marks the end time of the response and queues the network request metric on the device for transmission. Check logcat for transmission info.  

## Extension functions

### trace

```
inlineÂ funÂ HttpMetric.trace(block:Â HttpMetric.() -> Unit):Â Unit
```

Measures the time it takes to run the [block](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/package-summary#(com.google.firebase.perf.metrics.HttpMetric).trace(kotlin.Function1)) wrapped by calls to start and stop using [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric).