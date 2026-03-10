# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel.md.txt

# LiveGenerativeModel

# LiveGenerativeModel


```
@PublicPreviewAPI
public final class LiveGenerativeModel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a multimodal model (like Gemini) capable of real-time content generation based on various input types, supporting bidirectional streaming.

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/LiveGenerativeModel#connect()()` Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` with the server for bidirectional streaming. |

## Public methods

### connect

```
public final @NonNull LiveSession connect()
```

Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` with the server for bidirectional streaming.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ServiceConnectionHandshakeFailedException com.google.firebase.vertexai.type.ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |