# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/LiveGenerativeModel.md.txt

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

|                                                ### Public functions                                                |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `suspend `[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) | [connect](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel#connect())`()` Start a [LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) with the server for bidirectional streaming. |

## Public functions

### connect

```
suspendÂ funÂ connect():Â LiveSession
```

Start a [LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) with the server for bidirectional streaming.  

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) | A [LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) that you can use to stream messages to and from the server. |

|                                                                                                                                  Throws                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException: `[com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException) | If the client was not able to establish a connection with the server. |