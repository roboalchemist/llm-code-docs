# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures.md.txt

# LiveModelFutures

# LiveModelFutures


```
@PublicPreviewAPI
abstract class LiveModelFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures.Companion#from(com.google.firebase.vertexai.LiveGenerativeModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures#connect()()` Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` with the server for bidirectional streaming. |

## Public companion functions

### from

```
fun from(model: LiveGenerativeModel): LiveModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel` |

## Public functions

### connect

```
abstract fun connect(): ListenableFuture<LiveSessionFutures>
```

Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` with the server for bidirectional streaming.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures>` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.ServiceConnectionHandshakeFailedException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |