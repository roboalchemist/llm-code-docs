# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference.md.txt

# HttpsCallableReference

# HttpsCallableReference


```
public final class HttpsCallableReference
```

<br />

*** ** * ** ***

A reference to a particular Callable HTTPS trigger in Cloud Functions.

## Summary

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#timeout()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#call()()` Executes this HTTPS endpoint asynchronously without arguments. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#call(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html data)` Executes this Callable HTTPS trigger asynchronously. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#setTimeout(kotlin.Long,java.util.concurrent.TimeUnit)(long timeout, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html units)` Changes the timeout for calls from this instance of Functions. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#stream(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html data)` Streams data to the specified HTTPS endpoint. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference#withTimeout(kotlin.Long,java.util.concurrent.TimeUnit)(long timeout, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html units)` Creates a new reference with the given timeout for calls. |

## Public fields

### timeout

```
public final long timeout
```

## Public methods

### call

```
public final @NonNull Task<@NonNull HttpsCallableResult> call()
```

Executes this HTTPS endpoint asynchronously without arguments.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult>` | A Task that will be completed when the HTTPS request has completed. |

### call

```
public final @NonNull Task<@NonNull HttpsCallableResult> call(Object data)
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

- `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException`

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html data` | Parameters to pass to the trigger. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult>` | A Task that will be completed when the HTTPS request has completed. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/org/json/JSONArray.html` |   |
| `https://developer.android.com/reference/kotlin/org/json/JSONObject.html` |   |
| `https://developer.android.com/reference/kotlin/java/io/IOException.html` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException` |   |

### setTimeout

```
public final void setTimeout(long timeout, @NonNull TimeUnit units)
```

Changes the timeout for calls from this instance of Functions. The default is 60 seconds.

| Parameters |
|---|---|
| `long timeout` | The length of the timeout, in the given units. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html units` | The units for the specified timeout. |

### stream

```
public final @NonNull Publisher<@NonNull StreamResponse> stream(Object data)
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

- `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException`

<!-- -->

- if the request connected, but the function returned an error.

The request to the Cloud Functions backend made by this method automatically includes a Firebase Instance ID token to identify the app instance. If a user is logged in with Firebase Auth, an auth token for the user will also be automatically included.

Firebase Instance ID sends data to the Firebase backend periodically to collect information regarding the app instance. To stop this, see `https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId()`. It will resume with a new Instance ID the next time you call this method.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html data` | Parameters to pass to the endpoint. Defaults to `null` if not provided. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse>` | `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` that will emit intermediate data, and the final result, as it is generated by the function. |

| See also |
|---|---|
| `https://developer.android.com/reference/kotlin/org/json/JSONArray.html` |   |
| `https://developer.android.com/reference/kotlin/org/json/JSONObject.html` |   |
| `https://developer.android.com/reference/kotlin/java/io/IOException.html` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException` |   |

### withTimeout

```
public final @NonNull HttpsCallableReference withTimeout(long timeout, @NonNull TimeUnit units)
```

Creates a new reference with the given timeout for calls. The default is 60 seconds.

| Parameters |
|---|---|
| `long timeout` | The length of the timeout, in the given units. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/TimeUnit.html units` | The units for the specified timeout. |