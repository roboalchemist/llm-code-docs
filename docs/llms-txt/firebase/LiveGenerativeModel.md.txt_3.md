# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel.md.txt

# LiveGenerativeModel

# LiveGenerativeModel


```
@PublicPreviewAPI
class LiveGenerativeModel
```

<br />

*** ** * ** ***

Represents a multimodal model (like Gemini) capable of real-time content generation based on various input types, supporting bidirectional streaming.

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel#connect()()` Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` with the server for bidirectional streaming. |

## Public functions

### connect

```
suspend fun connect(): LiveSession
```

Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` with the server for bidirectional streaming.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |