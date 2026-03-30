# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion.md.txt

# GenerativeBackend.Companion

# GenerativeBackend.Companion


```
public static class GenerativeBackend.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#googleAI()()` References the Google Developer API backend. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#vertexAI(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location)` References the VertexAI Gemini API backend. |

## Public methods

### googleAI

```
public static final @NonNull GenerativeBackend googleAI()
```

References the Google Developer API backend.

### vertexAI

```
public static final @NonNull GenerativeBackend vertexAI(@NonNull String location)
```

References the VertexAI Gemini API backend.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location` | passes a valid cloud server location, defaults to "us-central1" |