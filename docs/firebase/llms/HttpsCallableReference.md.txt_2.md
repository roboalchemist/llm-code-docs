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

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#call()()` Executes this HTTPS endpoint asynchronously without arguments. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#call(kotlin.Any)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Executes this Callable HTTPS trigger asynchronously. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#setTimeout(kotlin.Long,java.util.concurrent.TimeUnit)(timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, units: https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html)` Changes the timeout for calls from this instance of Functions. |
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#stream(kotlin.Any)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Streams data to the specified HTTPS endpoint. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#withTimeout(kotlin.Long,java.util.concurrent.TimeUnit)(timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, units: https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html)` Creates a new reference with the given timeout for calls. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference#timeout()` |

## Public functions

### call

```
fun call(): Task<HttpsCallableResult>
```

Executes this HTTPS endpoint asynchronously without arguments.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult>` | A Task that will be completed when the HTTPS request has completed. |

### call

```
fun call(data: Any?): Task<HttpsCallableResult>
```

Executes this Callable HTTPS trigger asynchronously.

The data passed into the trigger can be any of the following types:

- Any primitive type, including null, int, long, float, and boolean.

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`

- `https://developer.android.com/reference/kotlin/java/util/List.html`, where the contained objects are also one of these types.

- `https://developer.android.com/reference/kotlin/java/util/Map.html`, where the values are also one of these types.

- `https://developer.android.com/reference/kotlin/org/json/JSONArray.html`

- `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`

- `https://developer.android.com/reference/kotlin/org/json/JSONObject.html#NULL--`

If the returned task fails, the Exception will be one of the following types:

- `https://developer.android.com/reference/kotlin/java/io/IOException.html`

<!-- -->

- if the HTTPS request failed to connect.

<!-- -->

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException`

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Parameters |
|---|---|
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | Parameters to pass to the trigger. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult>` | A Task that will be completed when the HTTPS request has completed. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/org/json/JSONArray.html` |   |
| `https://developer.android.com/reference/kotlin/org/json/JSONObject.html` |   |
| `https://developer.android.com/reference/kotlin/java/io/IOException.html` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException` |   |

### setTimeout

```
fun setTimeout(timeout: Long, units: TimeUnit): Unit
```

Changes the timeout for calls from this instance of Functions. The default is 60 seconds.

| Parameters |
|---|---|
| `timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The length of the timeout, in the given units. |
| `units: https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html` | The units for the specified timeout. |

### stream

```
fun stream(data: Any? = null): Publisher<StreamResponse>
```

Streams data to the specified HTTPS endpoint.

The data passed into the trigger can be any of the following types:

- Any primitive type, including null, int, long, float, and boolean.

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`

- `https://developer.android.com/reference/kotlin/java/util/List.html`, where the contained objects are also one of these types.

- `https://developer.android.com/reference/kotlin/java/util/Map.html`, where the values are also one of these types.

- `https://developer.android.com/reference/kotlin/org/json/JSONArray.html`

- `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`

- `https://developer.android.com/reference/kotlin/org/json/JSONObject.html#NULL--`

If the returned streamResponse fails, the exception will be one of the following types:

- `https://developer.android.com/reference/kotlin/java/io/IOException.html`

<!-- -->

- if the HTTPS request failed to connect.

<!-- -->

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException`

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Parameters |
|---|---|
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html? = null` | Parameters to pass to the endpoint. Defaults to `null` if not provided. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse>` | `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher` that will emit intermediate data, and the final result, as it is generated by the function. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/org/json/JSONArray.html` |   |
| `https://developer.android.com/reference/kotlin/org/json/JSONObject.html` |   |
| `https://developer.android.com/reference/kotlin/java/io/IOException.html` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException` |   |

### withTimeout

```
fun withTimeout(timeout: Long, units: TimeUnit): HttpsCallableReference
```

Creates a new reference with the given timeout for calls. The default is 60 seconds.

| Parameters |
|---|---|
| `timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The length of the timeout, in the given units. |
| `units: https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html` | The units for the specified timeout. |

## Public properties

### timeout

```
val timeout: Long
```