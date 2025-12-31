# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference.md.txt

# HttpsCallableReference

# HttpsCallableReference


```
class HttpsCallableReference
```

<br />

*** ** * ** ***

A reference to a particular Callable HTTPS trigger in Cloud Functions.

## Summary

|                                                                                                      ### Public functions                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)`>` | [call](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#call())`()` Executes this HTTPS endpoint asynchronously without arguments.                                                                                                                                                                                                                                                     |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)`>` | [call](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#call(kotlin.Any))`(data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)` Executes this Callable HTTPS trigger asynchronously.                                                                                                                                                                  |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                   | [setTimeout](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#setTimeout(kotlin.Long,java.util.concurrent.TimeUnit))`(timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`, units: `[TimeUnit](https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html)`)` Changes the timeout for calls from this instance of Functions. |
| [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse)`>`             | [stream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#stream(kotlin.Any))`(data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)` Streams data to the specified HTTPS endpoint.                                                                                                                                                                     |
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference)                                                                                               | [withTimeout](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#withTimeout(kotlin.Long,java.util.concurrent.TimeUnit))`(timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`, units: `[TimeUnit](https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html)`)` Creates a new reference with the given timeout for calls.    |

|                            ### Public properties                             |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [timeout](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#timeout()) |

## Public functions

### call

```
funÂ call():Â Task<HttpsCallableResult>
```

Executes this HTTPS endpoint asynchronously without arguments.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see [com.google.firebase.iid.FirebaseInstanceId.deleteInstanceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()). It will resume with a new Instance ID the next time you call this method.  

|                                                                                                            Returns                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)`>` | A Task that will be completed when the HTTPS request has completed. |

### call

```
funÂ call(data:Â Any?):Â Task<HttpsCallableResult>
```

Executes this Callable HTTPS trigger asynchronously.

The data passed into the trigger can be any of the following types:

- Any primitive type, including null, int, long, float, and boolean.

- [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

- [List](https://developer.android.com/reference/kotlin/java/util/List.html), where the contained objects are also one of these types.

- [Map](https://developer.android.com/reference/kotlin/java/util/Map.html), where the values are also one of these types.

- [org.json.JSONArray](https://developer.android.com/reference/kotlin/org/json/JSONArray.html)

- [org.json.JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)

- [org.json.JSONObject.NULL](https://developer.android.com/reference/kotlin/org/json/JSONObject.html#NULL--)

If the returned task fails, the Exception will be one of the following types:

- [java.io.IOException](https://developer.android.com/reference/kotlin/java/io/IOException.html)

<!-- -->

- if the HTTPS request failed to connect.

<!-- -->

- [FirebaseFunctionsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException)

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see [com.google.firebase.iid.FirebaseInstanceId.deleteInstanceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()). It will resume with a new Instance ID the next time you call this method.  

|                                      Parameters                                       |
|---------------------------------------------------------------------------------------|------------------------------------|
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | Parameters to pass to the trigger. |

|                                                                                                            Returns                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)`>` | A Task that will be completed when the HTTPS request has completed. |

|                                                                 See also                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------|---|
| [JSONArray](https://developer.android.com/reference/kotlin/org/json/JSONArray.html)                                                      |   |
| [JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)                                                    |   |
| [IOException](https://developer.android.com/reference/kotlin/java/io/IOException.html)                                                   |   |
| [FirebaseFunctionsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException) |   |

### setTimeout

```
funÂ setTimeout(timeout:Â Long,Â units:Â TimeUnit):Â Unit
```

Changes the timeout for calls from this instance of Functions. The default is 60 seconds.  

|                                               Parameters                                               |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                | The length of the timeout, in the given units. |
| `units: `[TimeUnit](https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html) | The units for the specified timeout.           |

### stream

```
funÂ stream(data:Â Any? = null):Â Publisher<StreamResponse>
```

Streams data to the specified HTTPS endpoint.

The data passed into the trigger can be any of the following types:

- Any primitive type, including null, int, long, float, and boolean.

- [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

- [List](https://developer.android.com/reference/kotlin/java/util/List.html), where the contained objects are also one of these types.

- [Map](https://developer.android.com/reference/kotlin/java/util/Map.html), where the values are also one of these types.

- [org.json.JSONArray](https://developer.android.com/reference/kotlin/org/json/JSONArray.html)

- [org.json.JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)

- [org.json.JSONObject.NULL](https://developer.android.com/reference/kotlin/org/json/JSONObject.html#NULL--)

If the returned streamResponse fails, the exception will be one of the following types:

- [java.io.IOException](https://developer.android.com/reference/kotlin/java/io/IOException.html)

<!-- -->

- if the HTTPS request failed to connect.

<!-- -->

- [FirebaseFunctionsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException)

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see [com.google.firebase.iid.FirebaseInstanceId.deleteInstanceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()). It will resume with a new Instance ID the next time you call this method.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`? = null` | Parameters to pass to the endpoint. Defaults to `null` if not provided. |

|                                                                                                      Returns                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse)`>` | [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher) that will emit intermediate data, and the final result, as it is generated by the function. |

|                                                                 See also                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------|---|
| [JSONArray](https://developer.android.com/reference/kotlin/org/json/JSONArray.html)                                                      |   |
| [JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)                                                    |   |
| [IOException](https://developer.android.com/reference/kotlin/java/io/IOException.html)                                                   |   |
| [FirebaseFunctionsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException) |   |

### withTimeout

```
funÂ withTimeout(timeout:Â Long,Â units:Â TimeUnit):Â HttpsCallableReference
```

Creates a new reference with the given timeout for calls. The default is 60 seconds.  

|                                               Parameters                                               |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                | The length of the timeout, in the given units. |
| `units: `[TimeUnit](https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html) | The units for the specified timeout.           |

## Public properties

### timeout

```
valÂ timeout:Â Long
```