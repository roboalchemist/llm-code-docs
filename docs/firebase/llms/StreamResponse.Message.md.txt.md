# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message.md.txt

# StreamResponse.Message

# StreamResponse.Message


```
public final class StreamResponse.Message extends StreamResponse
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse) ||
|   | ↳ | [com.google.firebase.functions.StreamResponse.Message](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message) |

*** ** * ** ***

An event message received during the stream.

Messages are intermediate data chunks sent by the server while processing a request.

Example SSE format:

```
data: { "message": { "chunk": "foo" } }
```

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message#message()` the intermediate data received from the server. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message#Message(com.google.firebase.functions.HttpsCallableResult)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult message)` |

## Public fields

### message

```
public final @NonNull HttpsCallableResult message
```

the intermediate data received from the server.

## Public constructors

### Message

```
public Message(@NonNull HttpsCallableResult message)
```