# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel.md.txt

# LiveGenerativeModel

# LiveGenerativeModel


```
@PublicPreviewAPI
public final class LiveGenerativeModel
```

<br />

*** ** * ** ***

Represents a multimodal model (like Gemini) capable of real-time content generation based on various input types, supporting bidirectional streaming.

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel#connect()()` Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` with the server for bidirectional streaming. |

## Public methods

### connect

```
public final @NonNull LiveSession connect()
```

Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` with the server for bidirectional streaming.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |