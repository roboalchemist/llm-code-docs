# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.md.txt

# StreamResponse

# StreamResponse


```
abstract class StreamResponse
```

<br />

Known direct subclasses [StreamResponse.Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message), [StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message` | An event message received during the stream. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result` | The final result of the computation, marking the end of the stream. |

*** ** * ** ***

Represents a response from a Server-Sent Event (SSE) stream.

The SSE stream consists of two types of responses:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message`: Represents an intermediate event pushed from the server.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result`: Represents the final response that signifies the stream has ended.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse` An event message received during the stream. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse` The final result of the computation, marking the end of the stream. |