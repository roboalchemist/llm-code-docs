# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures.md.txt

# LiveModelFutures

# LiveModelFutures


```
@PublicPreviewAPI
abstract class LiveModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures.Companion#from(com.google.firebase.ai.LiveGenerativeModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures#connect()()` Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` with the server for bidirectional streaming. |

## Public companion functions

### from

```
fun from(model: LiveGenerativeModel): LiveModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` |

## Public functions

### connect

```
abstract fun connect(): ListenableFuture<LiveSessionFutures>
```

Start a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` with the server for bidirectional streaming.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures>` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |