# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message.md.txt

# StreamResponse.Message

# StreamResponse.Message


```
public final class StreamResponse.Message extends StreamResponse
```

<br />

|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                              |||
| â³ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse)                    ||
|   | â³ | [com.google.firebase.functions.StreamResponse.Message](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message) |

*** ** * ** ***

An event message received during the stream.

Messages are intermediate data chunks sent by the server while processing a request.

Example SSE format:  

```text
data: { "message": { "chunk": "foo" } }
```

## Summary

|                                                                                                         ### Public fields                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableResult](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult) | [message](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message#message()) the intermediate data received from the server. |

|                                                                                                                                                                                               ### Public constructors                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Message](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message#Message(com.google.firebase.functions.HttpsCallableResult))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableResult](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult)` message)` |

## Public fields

### message

```
publicÂ finalÂ @NonNull HttpsCallableResultÂ message
```

the intermediate data received from the server.  

## Public constructors

### Message

```
publicÂ Message(@NonNull HttpsCallableResultÂ message)
```