# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures.md.txt

# LiveModelFutures

# LiveModelFutures


```
@PublicPreviewAPI
abstract class LiveModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel).  

|                                                      See also                                                       |
|---------------------------------------------------------------------------------------------------------------------|---|
| [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel) |   |

## Summary

|                                           ### Public companion functions                                           |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures) | [from](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures.Companion#from(com.google.firebase.ai.LiveGenerativeModel))`(model: `[LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel)`)` |

|                                                                                                                      ### Public functions                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures)`>` | [connect](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures#connect())`()` Start a [LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures) with the server for bidirectional streaming. |

## Public companion functions

### from

```
funÂ from(model:Â LiveGenerativeModel):Â LiveModelFutures
```  

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures) | a [LiveModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveModelFutures) created around the provided [LiveGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel) |

## Public functions

### connect

```
abstractÂ funÂ connect():Â ListenableFuture<LiveSessionFutures>
```

Start a [LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures) with the server for bidirectional streaming.  

|                                                                                                                       Returns                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures)`>` | A [LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures) that you can use to stream messages to and from the server. |

|                                                                                                                                  Throws                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException: `[com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException) | If the client was not able to establish a connection with the server. |