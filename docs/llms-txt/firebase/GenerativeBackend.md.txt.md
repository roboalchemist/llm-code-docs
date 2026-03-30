# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.md.txt

# GenerativeBackend

# GenerativeBackend


```
public final class GenerativeBackend
```

<br />

*** ** * ** ***

Represents a reference to a backend for generative AI.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#googleAI()()` References the Google Developer API backend. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend#hashCode()()` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerativeBackend.Companion#vertexAI(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location)` References the VertexAI Gemini API backend. |

## Public methods

### equals

```
public boolean equals(Object other)
```

### googleAI

```
public static final @NonNull GenerativeBackend googleAI()
```

References the Google Developer API backend.

### hashCode

```
public int hashCode()
```

### vertexAI

```
public static final @NonNull GenerativeBackend vertexAI(@NonNull String location)
```

References the VertexAI Gemini API backend.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location` | passes a valid cloud server location, defaults to "us-central1" |