# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion.md.txt

# FirebaseVertexAI.Companion

# FirebaseVertexAI.Companion


```
public static class FirebaseVertexAI.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#instance()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`. |

## Public fields

### instance

```
public static final @NonNull FirebaseVertexAI instance
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`

## Public methods

### getInstance

```
public static final @NonNull FirebaseVertexAI getInstance(@NonNull FirebaseApp app)
```

### getInstance

```
public static final @NonNull FirebaseVertexAI getInstance(@NonNull FirebaseApp app, @NonNull String location)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/FirebaseVertexAI.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location` | location identifier, defaults to `us-central1`; see available [Vertex AI regions](https://firebase.google.com/docs/vertex-ai/locations?platform=android#available-locations) . |