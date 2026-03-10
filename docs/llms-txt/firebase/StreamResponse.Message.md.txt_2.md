# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message.md.txt

# StreamResponse.Message

# StreamResponse.Message


```
class StreamResponse.Message : StreamResponse
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse) ||
|   | ↳ | [com.google.firebase.functions.StreamResponse.Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message) |

*** ** * ** ***

An event message received during the stream.

Messages are intermediate data chunks sent by the server while processing a request.

Example SSE format:

```kotlin
data: { "message": { "chunk": "foo" } }
```

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message#Message(com.google.firebase.functions.HttpsCallableResult)(message: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message#message()` the intermediate data received from the server. |

## Public constructors

### Message

```
Message(message: HttpsCallableResult)
```

## Public properties

### message

```
val message: HttpsCallableResult
```

the intermediate data received from the server.