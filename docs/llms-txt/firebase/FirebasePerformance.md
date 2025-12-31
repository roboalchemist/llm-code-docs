# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/FirebasePerformance.md.txt

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

This SDK uses FirebaseInstallations to identify the app instance and periodically sends data to the Firebase backend. To stop sending performance events, call [FirebasePerformance.setPerformanceCollectionEnabled(false)](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean)).

## Summary

|                                                                                                                                                            ### Nested types                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[Retention](https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `annotation `[FirebasePerformance.HttpMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod) Valid HttpMethods for manual network APIs |

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_ATTRIBUTE_KEY_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_KEY_LENGTH())` = 40` Maximum allowed length of the Key of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute        |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_ATTRIBUTE_VALUE_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_ATTRIBUTE_VALUE_LENGTH())` = 100` Maximum allowed length of the Value of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) attribute |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_TRACE_CUSTOM_ATTRIBUTES](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_CUSTOM_ATTRIBUTES())` = 5` Maximum allowed number of attributes allowed in a trace.                                                                                               |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_TRACE_NAME_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH())` = 100` Maximum allowed length of the name of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)                      |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_TRACE_NAME_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH())` = 100` Maximum allowed length of the name of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)                      |

|                                                        ### Public functions                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[FirebasePerformance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#getInstance())`()` Returns a singleton of FirebasePerformance.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                  | [isPerformanceCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#isPerformanceCollectionEnabled())`()` Determines whether performance monitoring is enabled or disabled.                                                                                                                                                                                                                                                                                                                                                                         |
| [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric)                         | [newHttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.lang.String,java.lang.String))`(` ` url: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` @`[FirebasePerformance.HttpMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod)` httpMethod: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) `)` Creates a HttpMetric object for collecting network performance data for one request/response |
| [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric)                         | [newHttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newHttpMetric(java.net.URL,java.lang.String))`(url: `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)`, @`[FirebasePerformance.HttpMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod)` httpMethod: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a HttpMetric object for collecting network performance data for one request/response                      |
| [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)                                   | [newTrace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#newTrace(java.lang.String))`(traceName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a Trace object with given name.                                                                                                                                                                                                                                                                                                                                  |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                        | [setPerformanceCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#setPerformanceCollectionEnabled(boolean))`(enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Enables or disables performance monitoring.                                                                                                                                                                                                                                                                                          |
| `java-static `[Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)                     | [startTrace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#startTrace(java.lang.String))`(traceName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a Trace object with given name and start the trace.                                                                                                                                                                                                                                                                                                          |

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

### MAX_TRACE_NAME_LENGTH

```
constÂ valÂ MAX_TRACE_NAME_LENGTH = 100:Â Int
```

Maximum allowed length of the name of the [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace)  

## Public functions

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebasePerformance
```

Returns a singleton of FirebasePerformance.  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebasePerformance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance) | the singleton FirebasePerformance object. |

### isPerformanceCollectionEnabled

```
funÂ isPerformanceCollectionEnabled():Â Boolean
```

Determines whether performance monitoring is enabled or disabled. This respects the Firebase Performance specific values first, and if these aren't set, uses the Firebase wide data collection switch.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if performance monitoring is enabled and false if performance monitoring is disabled. This is for dynamic enable/disable state. This does not reflect whether instrumentation is enabled/disabled in Gradle properties. |

### newHttpMetric

```
funÂ newHttpMetric(
Â Â Â Â url:Â String,
Â Â Â Â @FirebasePerformance.HttpMethod httpMethod:Â String
):Â HttpMetric
```

Creates a HttpMetric object for collecting network performance data for one request/response  

|                                                                                                                  Parameters                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `url: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                       | a valid url String, cannot be empty                                               |
| `@`[FirebasePerformance.HttpMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod)` httpMethod: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

|                                                   Returns                                                   |
|-------------------------------------------------------------------------------------------------------------|----------------------------|
| [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric) | the new HttpMetric object. |

### newHttpMetric

```
funÂ newHttpMetric(url:Â URL,Â @FirebasePerformance.HttpMethod httpMethod:Â String):Â HttpMetric
```

Creates a HttpMetric object for collecting network performance data for one request/response  

|                                                                                                                  Parameters                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `url: `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)                                                                                                                                                                | a valid URL object                                                                |
| `@`[FirebasePerformance.HttpMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance.HttpMethod)` httpMethod: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | One of the values GET, PUT, POST, DELETE, HEAD, PATCH, OPTIONS, TRACE, or CONNECT |

|                                                   Returns                                                   |
|-------------------------------------------------------------------------------------------------------------|----------------------------|
| [HttpMetric](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/HttpMetric) | the new HttpMetric object. |

### newTrace

```
funÂ newTrace(traceName:Â String):Â Trace
```

Creates a Trace object with given name.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `traceName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | name of the trace, requires no leading or trailing whitespace, no leading underscore '_' character, max length is [MAX_TRACE_NAME_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()) characters. |

|                                              Returns                                              |
|---------------------------------------------------------------------------------------------------|-----------------------|
| [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) | the new Trace object. |

### setPerformanceCollectionEnabled

```
funÂ setPerformanceCollectionEnabled(enable:Â Boolean):Â Unit
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

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------|
| `enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Should performance monitoring be enabled |

### startTrace

```
java-staticÂ funÂ startTrace(traceName:Â String):Â Trace
```

Creates a Trace object with given name and start the trace.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `traceName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | name of the trace. Requires no leading or trailing whitespace, no leading underscore \[_\] character, max length of [MAX_TRACE_NAME_LENGTH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/FirebasePerformance#MAX_TRACE_NAME_LENGTH()) characters. |

|                                              Returns                                              |
|---------------------------------------------------------------------------------------------------|-----------------------|
| [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) | the new Trace object. |