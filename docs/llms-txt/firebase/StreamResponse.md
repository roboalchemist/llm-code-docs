# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/StreamResponse.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.md.txt

# StreamResponse

# StreamResponse


```
abstract class StreamResponse
```

<br />

Known direct subclasses  
[StreamResponse.Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message), [StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result)  

|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [StreamResponse.Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message) | An event message received during the stream.                        |
| [StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result)   | The final result of the computation, marking the end of the stream. |

*** ** * ** ***

Represents a response from a Server-Sent Event (SSE) stream.

The SSE stream consists of two types of responses:

- [Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message): Represents an intermediate event pushed from the server.

- [Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result): Represents the final response that signifies the stream has ended.

## Summary

|                                                                                                                                                        ### Nested types                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[StreamResponse.Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message)` : `[StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse) An event message received during the stream.                      |
| `class `[StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result)` : `[StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse) The final result of the computation, marking the end of the stream. |